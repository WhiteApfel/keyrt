# KeyRT

Не знаю, зачем тебе может понадобиться автоматизация открытия дверей и выдачи кодов,
но это твоё право, я даю тебе удобный инструмент для его реализации. Да здравствует питон.

## Установка

```shell
python -m pip install -U keyrt
```

## Использование

### Открытие двери

```python
from keyrt import KeyRT

async def main():
    keyrt_client = KeyRT(access_token='YOUR_ACCESS_TOKEN'
                         )
    devices = await keyrt_client.get_devices()
    assert await keyrt_client.open_device(devices.devices[0].id)
```