import discord
import discord.ext.commands
import reddit_trawler
import dice_thrower

file = open("../tokens/discordBot.txt").read()

TOKEN = 'NDY5NzgyOTAxNjgxMjkxMjc1.DjMvxg.jvRjoy5MBhmSSAJIq3JGjpHU8Us'
BOT_PREFIX = ("'''")
client = discord.ext.commands.Bot(command_prefix=BOT_PREFIX)


@client.command(name='copypasta',
                description='pastes copy pasta from reddit)',
                aliases=['pasta', 'copy', 'copypastas'],
                pass_context=True)  # prepares the name ,description, purpose and aliases for a program
async def copypasta(module, *args):

    # await client.say(' '.join(args))

    try:
        msg = reddit_trawler.reddit("copypasta", ' '.join(args))
        await client.say(msg)

    except:
        await client.say(' '.join(args) + "did not come up with any results")


@client.command(name='reddit',
                description='pastes content from reddit from reddit',
                pass_context=True)  # prepares the name ,description, purpose and aliases for a program
async def reddit(module, *args):

    try:
        msg = reddit_trawler.reddit(args[0], ' '.join(args[1:]))
        await client.say(msg)

    except:
        await client.say(" %s on thread %s did not come up with any results" % args[0], join(args[1:]))


@client.command(name='hello',
                description='says hello',
                aliases=['hi'],
                pass_context=True)
async def on_message(context):
    await client.say("Hello " + context.message.author.mention)


@client.command(name='roll',
                description='throws dice)',
                aliases=["dice", "throw"],
                pass_context=True)  # prepares the name ,description, purpose and aliases for a program
async def dice(module, *args):

    print("proccessing")
    msg = dice_thrower.dice(' '.join(args))
    await client.say(msg)


@client.event
async def on_message(message):
 # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if 'mods are gay' in str(message.content).lower():
        msg = 'It is known.'.format(message)
        await client.send_message(message.channel, msg)

    if 'are' in str(message.content).lower() or 'i' in str(message.content).lower() and ('mod' and 'gay') in str(message.content).lower():
        post = message.content

        if post.find('are') < post.find('mod') or post.find('is') < post.find('mod'):
            await client.send_message(message.channel, 'Yes.')

    if ('Who has the' and 'gay') in message.content.lower():
        await client.send_message(message.channel, 'Mods!')

    if 'am i gay' in message.content.lower():
        if ('moderator' or 'admin' or 'Ubermensch') in [y.name.lower for y in message.author.roles]:
            await client.send_message(message.channel, 'Yes you do ' + message.author.mention + '.')
        else:
            await client.send_message(message.channel, "No.")

    # this is neceasary so the rest of the commands work.
    await client.process_commands(message)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='with suicidal depression'))


client.run(TOKEN)
