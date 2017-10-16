import asyncio
import json
import aiohttp
TOKEN = "LWaQKNpZmg6vPXGe4_eu-tibyKkKrlnu"
URL = "https://discordapp.com/api"

async def send_message(recipient_id, content):
    """Send a message with content to the recipient_id."""
    channel = await api_call("/users/@me/channels", "POST",
                             json={"recipient_id": recipient_id})
    return await api_call(f"/channels/{channel['id']}/messages",
                          "POST",
                          json={"content": content})

async def start(url):
    with aiohttp.ClientSession() as session:
        async with session.ws_connect(
                f"{url}?v=6&encoding=json") as ws:
            async for msg in ws:
                data = json.loads(msg.data)
                if data["op"] == 10:  # Hello
                    asyncio.ensure_future(heartbeat(
                                    ws,
                                    data['d']['heartbeat_interval']))

                    await ws.send_json({
                        "op": 2,  # Identify
                        "d": {
                            "token": TOKEN,
                            "properties": {},
                            "compress": False,
                            "large_threshold": 250
                        }
                    })
                elif data["op"] == 0:  # Dispatch
                    print(data['t'], data['d'])
                else:
                    print(data)

async def heartbeat(ws, interval):
    """Send every interval ms the heatbeat message."""
    while True:
        await asyncio.sleep(interval / 1000)  # seconds
        await ws.send_json({
            "op": 1,  # Heartbeat
            "d": 0
        })

async def api_call(path, method="GET", **kwargs):
    """Return the JSON body of a call to Discord REST API."""
    defaults = {
            "headers": {
                "Authorization": f"Bot {TOKEN}",
                "User-Agent": "dBot (https://medium.com/@greut, 0.1)"
            }
        }

    kwargs = dict(defaults, **kwargs)
    with aiohttp.ClientSession() as session:
        async with session.request(path, method, **kwargs) as response:
            assert 200 == response.status, response.reason
            return await response.json()

async def main():
    """Main program."""
    response = await api_call("/gateway")
    await start(response["url"])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
