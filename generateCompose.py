import os

docker_compose_template = """
version: "3.8"

services:
{worker_sections}

{head_sections}

networks:
  b7s-local:
    driver: bridge
    ipam:
      config:
        - subnet: 172.19.0.0/24
"""

worker_section_template = """
  {worker}:
    # {worker_id}
    environment:
      - LOG_LEVEL=debug
      - NODE_ROLE=worker
      - NODE_KEY_PATH=/var/keys/priv.bin
      - PEER_DB=pdb
      - FUNCTION_DB=fdb
      - WORKSPACE=workspace
      - RUNTIME=/app/runtime
      - BOOT_NODES={boot_nodes}
    image: ghcr.io/blocklessnetwork/b7s:v0.6.2
    volumes:
      - type: bind
        source: ./keys/{worker}/
        target: /var/keys
        read_only: true
    depends_on:
      - {worker_dependency}
    networks:
      b7s-local:
        aliases:
          - {worker}
        ipv4_address: {ip_address}
"""

head_section_template = """
  {head}:
    # {head_id}
    environment:
      - LOG_LEVEL=debug
      - NODE_ROLE=head
      - NODE_KEY_PATH=/var/keys/priv.bin
      - PEER_DB=pdb
      - FUNCTION_DB=fdb
      - WORKSPACE=workspace
      - REST_API={rest_port}
      - P2P_PORT={port}
      # - BOOT_NODES='{boot_nodes}'
    image: ghcr.io/blocklessnetwork/b7s:v0.6.2
    ports:
      - "{rest_port}:{rest_port}"
    volumes:
      - type: bind
        source: ./keys/{head}/
        target: /var/keys
        read_only: true
    {depends_on}
      {head_dependency}
    networks:
      b7s-local:
        aliases:
          - {head}
        ipv4_address: {ip_address}
"""


def generate_boot_nodes(peers, prefix):
    boot_nodes = []
    for i, peer in enumerate(peers):
        boot_nodes.append(f'/ip4/172.19.0.{100 + i}/tcp/{9010 + i}/p2p/{peer}')
    return ",".join(boot_nodes)

workers = []
heads = []

for folder in os.listdir("keys"):
    if folder.startswith("worker"):
        with open(f"keys/{folder}/peerid.txt", "r") as f:
            worker_id = f.read().strip()
        worker_number = int(folder[6:])  # Parse the integer from folder name
        workers.append((folder, worker_id, worker_number))
    elif folder.startswith("head"):
        with open(f"keys/{folder}/peerid.txt", "r") as f:
            head_id = f.read().strip()
        head_number = int(folder[4:])  # Parse the integer from folder name
        heads.append((folder, head_id, head_number))

num_workers = len(workers)
num_heads = len(heads)

worker_sections = "\n".join(worker_section_template.format(
    worker=worker,
    worker_id=worker_id,
    port=9002 + i,
    boot_nodes=generate_boot_nodes([id for _, id, _ in heads], 10),
    ip_address=f"172.19.0.{2 + i}",
    delay=i * 60 + (5 * 60),  # Delay increases with each worker, e.g., 0s, 30s, 60s, ...
    worker_dependency="worker" + str(worker_number - 1) if worker_number > 1 else "head" + str(max(head_number for _, _, head_number in heads))
) for i, (worker, worker_id, worker_number) in enumerate(workers))

head_sections = "\n".join(head_section_template.format(
    head=head,
    head_id=head_id,
    port=9010 + i,
    rest_port=6000 + i,
    boot_nodes=generate_boot_nodes([id for _, id, _ in heads if head != "head1"], 10),
    ip_address=f"172.19.0.{100 + i}",  # Start from .100 for heads
    delay=i * 60,  # Delay increases with each head, e.g., 0s, 60s, 120s, ...
    depends_on="" if head == "head1" else "depends_on:",
    head_dependency="" if head == "head1" else "- " + "head" + str(head_number - 1)
) for i, (head, head_id, head_number) in enumerate(heads))

docker_compose_content = docker_compose_template.format(worker_sections=worker_sections, head_sections=head_sections)

with open("docker-compose.yaml", "w") as f:
    f.write(docker_compose_content)

print("Docker Compose file generated.")
