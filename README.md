# twitch_eventsub_websocket_twichio_example

Most parts are basic bot in Quick Start of this webpage
https://twitchio.dev/en/stable/quickstart.html
I added features of eventsub to this basic bot by using
twitchio.
The parts of eventsub are codes from discord of Twitchio.
The license of the code is unknown.


## Points
- scope of access tokens: chat:edit chat:read moderator:read:followers
- About subscription of follow, payload.data.broadcaster.channel is NONE.
So, to send message, codes is like below.
```
await self.get_channel(payload.data.broadcaster.name).send('start')
```

## License
- MIT
- Licence of codes of Twitchio is MIT.
