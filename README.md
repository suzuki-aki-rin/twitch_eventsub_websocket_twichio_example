# twitch_eventsub_websocket_twichio_example

Most parts are basic bot in Quick Start of this webpage
https://twitchio.dev/en/stable/quickstart.html
I added features of eventsub to this basic bot by using
twitchio.
The parts of eventsub are codes from discord of Twitchio.
The license of the code is unknown.


## Points
- No need for callback server.
- Scopes of access tokens: chat:edit chat:read moderator:read:followers<BR>
I confirmed events of start and follow.
- About subscription of follow, payload.data.broadcaster.channel is NONE.
So, codes is like below to send message.
```
await self.get_channel(payload.data.broadcaster.name).send('start')
```

## License
- MIT
- Licence of codes of Twitchio is MIT.
