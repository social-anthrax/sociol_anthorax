import discord
from discord.ext import commands
import reddit_trawler
import dice_thrower
import os

token = "NDY5NzgyOTAxNjgxMjkxMjc1.XQfqcA.JRI8SjJbKs_lmRmUz7y4E-PodCs"

BOT_PREFIX = ("!")
bot = discord.ext.commands.Bot(
    command_prefix=BOT_PREFIX, description="ya YEET")


DM = True


if DM != True:
    @bot.command(name='copypasta',
                description='pastes copy pasta from reddit)',
                aliases=['pasta', 'copy', 'copypastas'],
                pass_context=True)  # prepares the name ,description, purpose and aliases for a program
    async def copypasta(module, *args):

        # await bot.say(' '.join(args))

        try:
            msg = reddit_trawler.reddit("copypasta", ' '.join(args))
            await bot.say(msg)

        except:
            await module.say(' '.join(args) + "did not come up with any results")


    @bot.command(name='reddit',
                description='pastes content from reddit from reddit',
                pass_context=True)  # prepares the name ,description, purpose and aliases for a program
    async def reddit(module, *args):

        try:
            msg = reddit_trawler.reddit(args[0], ' '.join(args[1:]))
            await bot.say(msg)

        except:
            await module.say(" %s on thread %s did not come up with any results" % args[0], ''.join(args[1:]))


    @bot.command(name='hello',
                description='says hello',
                aliases=['hi'],
                pass_context=True)
    async def on_message(context):
        await context.channel.send("Hello " + context.message.author.mention)


    @bot.command(name='roll',
                description='throws dice)',
                aliases=["dice", "throw"],
                pass_context=True)  # prepares the name ,description, purpose and aliases for a program
    async def dice(module, *args):

        msg = dice_thrower.dice(' '.join(args))
        await module.channel.send(msg)


    @bot.event
    async def on_message(message):
    # we do not want the bot to reply to itself
        if message.author == bot.user:
            return

        if 'mods are gay' in str(message.content).lower():
            msg = "It is known."

            await message.channel.send(msg)

        if 'are' in str(message.content).lower() or 'i' in str(message.content).lower() and ('mod' and 'gay') in str(message.content).lower():
            post = message.content

            if post.find('are') < post.find('mod') or post.find('is') < post.find('mod'):
                await message.channel.send('Yes.')

        if ('Who has the' and 'gay') in message.content.lower():
            await message.channel.send('Mods!')

        if 'am i gay' in message.content.lower():
            if ('moderator' or 'admin' or 'Ubermensch') in [y.name.lower for y in message.author.roles]:
                await message.channel.send('Yes you do ' + message.author.mention + '.')
            else:
                await message.channel.send("No.")

        if "!dm" in message.content.lower():
            await message.guild.get_member_named("social_anthrax#3123").send('test')

        # this is neceasary so the rest of the commands work.
        await bot.process_commands(message)

if DM:
    # TODO: add dict to read in ID's and save them to usernames

    file = open("dm.txt", "r")
    dmID = {}
    counter = 0
    for entries in file.read().splitlines():
        spliter = entries.split(", ")
        dmID[spliter[0]] = spliter[1]
    file.close()




    # TODO: add changing of channels by dictionary
    # TODO: add new users to dict by server look up


    @bot.event
    async def on_message(message):


        # print("[" + message.author.name + "]    " + message.content)
        # print(message.channel.id)
        message.channel = bot.get_channel(590286160576643076)
        async for text in message.channel.history(limit=10):
                print("[" + text.author.name + "]    " + text.content)
       
        try: 
            await message.channel.send(input("input: "))
        except:
           None
        finally:
            os.system('cls')
            async for text in message.channel.history(limit=10):
                print("[" + text.author.name + "]    " + text.content)

        


    # @bot.event
    # async def send_message(message):
        
            


    

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='with depression'))


bot.run(token)
