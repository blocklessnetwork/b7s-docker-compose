# b7s-docker-compose
quickly start a cluster using compose

Get docker https://www.docker.com/

```bash
PLATFORM=linux ARCH=amd64 NUM_HEADS=5 NUM_WORKERS=10 ./identities.sh # PLATFORM=darwin ARCH=arm64 NUM_HEADS=5 NUM_WORKERS=10 ./identities.s
python generateCompose.py
docker compose up
```

Do it all with one line, make sure you change the platform, arch, num heads, and num workers to desired.


Mac M1/M2

```bash
wget https://github.com/blocklessnetwork/b7s-docker-compose/archive/refs/heads/main.zip && unzip main.zip \
&& cd b7s-docker-compose-main && \
PLATFORM=darwin \
ARCH=arm64 \
NUM_HEADS=5 \
NUM_WORKERS=10 \
sh identities.sh && \
python generateCompose.py && docker compose up
```

Mac Intel

```bash
wget https://github.com/blocklessnetwork/b7s-docker-compose/archive/refs/heads/main.zip && unzip main.zip \
&& cd b7s-docker-compose-main && \
PLATFORM=darwin \
ARCH=amd64 \
NUM_HEADS=5 \
NUM_WORKERS=10 \
sh identities.sh && \
python generateCompose.py && docker compose up
```

Linux x64
```bash
wget https://github.com/blocklessnetwork/b7s-docker-compose/archive/refs/heads/main.zip && unzip main.zip \
&& cd b7s-docker-compose-main && \
PLATFORM=linux \
ARCH=amd64 \
NUM_HEADS=5 \
NUM_WORKERS=10 \
sh identities.sh && \
python generateCompose.py && docker compose up
```
