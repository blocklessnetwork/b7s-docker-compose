# b7s-docker-compose
quickly start a cluster using compose

Get docker https://www.docker.com/

```bash
PLATFORM=linux ARCH=amd64 NUM_HEADS=5 NUM_WORKERS=10 ./identities.sh # PLATFORM=darwin ARCH=arm64 NUM_HEADS=5 NUM_WORKERS=10 ./identities.s
python generateCompose.py
docker compose up
```

Do it all with one line, make sure you change the platform, arch, num heads, and num workers to desired.

* By default exposes port 6000 + 1 for each head node RPC
* Binds 172.0.0.10 + 1 for workers and
* Binds 172.0.0.100 + 1 for head nodes
* Terminates at Head1 - Localized / On Prem

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

Test

```
curl --location 'http://localhost:6000/api/v1/functions/execute' \
--header 'Accept: application/json, text/plain, */*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Connection: keep-alive' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Origin: http://localhost:8081' \
--header 'Referer: http://localhost:8081/' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-site' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "macOS"' \
--data '{
    "function_id": "bafybeiaugwh3mktzbnudurzk7jcyvmdhyy6jnairiu2phuf2t7c7orowjq",
    "method": "footest.wasm",
    "parameters": null,
    "config": {
        "permissions":["https://api.coingecko.com"],
        "env_vars": [
            {
                "name": "BLS_REQUEST_PATH",
                "value": "/api"
            }
        ],
        "number_of_nodes": 1,
        "result_aggregation": {
            "enable": false,
            "type": "none",
            "parameters": [
                {
                    "name": "type",
                    "value": ""
                }
            ]
        }
    }
}'
```
