# tg_bot
1. Бондырев Иван Юрьевич
2. Это очень глупый [бот](https://t.me/send_dudes_bot), который шлет чуваков
3. Amazon
4. Реализовал с помощью watchtower, вот скрипт:
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
