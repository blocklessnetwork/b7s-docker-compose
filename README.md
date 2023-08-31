# b7s-docker-compose
quickly start a cluster using compose



```bash
PLATFORM=linux ARCH=amd64 NUM_HEADS=5 NUM_WORKERS=10 ./identities.s # PLATFORM=darwin ARCH=arm64 NUM_HEADS=5 NUM_WORKERS=10 ./identities.s
python generateCompose.py
docker compose up
```
