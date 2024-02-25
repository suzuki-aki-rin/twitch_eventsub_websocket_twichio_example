##### eventsub for event subscription
from twitchio.ext import commands, eventsub

CHANNELS = ['STREAMING CHANNEL']
STREAMER_TOKEN = 'streamer_access_token'
BOT_TOKEN = 'bot_access_token'
BOT_FPREFIX = '?'
CHANNEL_ID = 'channel_id_to_event-subscribed'


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=BOT_TOKEN, prefix=BOT_PREFIX, initial_channels=CHANNELS)

        ###### for event subscription
        self.esclient = eventsub.EventSubWSClient(self)


    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        #print(f'User id is | {self.user_id}')

        #self.fetch_channel_following_count(self.token)
        #print(asyncio.run(self.create_user(self.user_id, self.nick).fetch_channel_follower_count()))

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        if not message.echo:
            await self.handle_commands(message)

    async def event_channel_joined(self, channel: CHANNEL) -> None:
        print(f'connected to {channel.name}')
        await channel.send('connected')

    async def event_join(self,channel,user):
        userdata = await self.fetch_users([user.name])
        print(userdata[0].id)


    async def event_part(self, user):
        userdata = await self.fetch_users([user.name])
        print(userdata[0].id)
        

    ##### event subscription
    async def event_eventsub_notification(self, payload: eventsub.NotificationEvent) -> None:
        print('Received event!')
        #print(payload.headers.message_id)
        print(payload.headers.subscription_type)

        
    async def event_eventsub_notification_channel_reward_redeem(self, payload: eventsub.CustomRewardRedemptionAddUpdateData) -> None:
        print('Received event!')
        print(payload.data.id)


    async def event_eventsub_notification_stream_start(self, payload: eventsub.StreamOnlineData) -> None:
        #print('Received event!')
        #print(payload)
        await self.get_channel(payload.data.broadcaster.name).send('start')


    async def event_eventsub_notification_followV2(self, payload: eventsub.ChannelFollowData) -> None:
        #print('Received event!')
        print(f'{payload.data.user.name} followed. THANKS!')
        #print(payload)


    async def event_eventsub_notification_channel_update(self, payload: eventsub.ChannelUpdateData) -> None:
        #print('Received event!')
        print(payload)


    async def sub(self):
        #await self.esclient.subscribe_channel_points_redeemed(broadcaster=CHANNEL_ID, token=STREAMER_TOKEN)
        await self.esclient.subscribe_channel_stream_start(broadcaster=CHANNEL_ID, token=STREAMER_TOKEN)
        await self.esclient.subscribe_channel_update(broadcaster=CHANNEL_ID, token=STREAMER_TOKEN)
        await self.esclient.subscribe_channel_follows_v2(broadcaster=CHANNEL_ID, moderator=CHANNEL_ID, token=STREAMER_TOKEN)

    ##### event subscription END

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')


    @commands.command(aliases = ("congrats", "grats", "gz"))
    async def congratulations(self, ctx, *, user = None):
        if not user:
            await ctx.send("Congratulations!!!!!")
        else:
            await ctx.send(f"Congratulations, {user.title()}!!!!!")


bot = Bot()

##### for event subscription
bot.loop.create_task(bot.sub())

bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
