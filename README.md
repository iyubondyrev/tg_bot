# tg_bot
1. Ivan Bondyrev
2. This is very stupid bot [бот](https://t.me/send_dudes_bot), which send dudes
3. Using Amazon
4. Using WatchTower
```
version: '3'

services:
  send_dudes:
    image: vano006503/tg_bot:latest
    labels:
      - "com.centurylinklabs.watchtower.scope=scope_1"
    environment:
      BOT_API_TOKEN: "11111111:XXXXXXXXXXXXXXXXXXXXXXXX"
    volumes:
      - ./dudes_storage:/tg_bot/dudes_storage

  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ~/.docker/config.json:/config.json
    command: --interval 30 --scope scope_1
    labels:
      - "com.centurylinklabs.watchtower.scope=scope_1"

```
