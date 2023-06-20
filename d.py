import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord import app_commands
import time
import sys
sys.path.insert(0, 'discord.py-self')
import random
import json
import tracemalloc
tracemalloc.start()

with open('theballs\config.json') as f:
    config = json.load(f)
    token = config['token']

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot_status = cycle(["jacking off", "ambatukum", "cream sound effect.mp3"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("balls")
    change_status.start()

#@client.command()
#async def ping(ctx):
#    bot_latency = round(client.latency * 1000)
#    await ctx.send(f"a{bot_latency}a")
#
#@client.tree.command(name="ping")
#async def ping(interaction: discord.Interaction):
#    bot_latency = round(client.latency * 1000)
#    await interaction.response.send_message(f"a{bot_latency}a")

#@client.hybrid_command(name="pinga")
#async def pinga(ctx):
#    bot_latency = round(client.latency * 1000)
#    await ctx.send(f"a{bot_latency}a")

#@client.hybrid_command(name="ping",description="ping")
#async def ping(interaction:discord.Interaction):
#    bot_latency = round(client.latency * 1000)
#    await interaction.response.send_message(f"the latency is {bot_latency}ms")

@client.hybrid_command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)
    await ctx.send(f"pong {bot_latency} ms")

@client.hybrid_command()
async def racist(ctx):
    await ctx.send("no racist")

@client.hybrid_command(aliases = ["homo"])
async def homophobic(ctx):
    await ctx.send("no homophobic")

@client.hybrid_command()
async def iloveballs(ctx):
    await ctx.send("bro same")

@client.hybrid_command()
async def embed(ctx):
    embed_message = discord.Embed(title = "ok", description="ok", colour=discord.Colour.random())

    embed_message.set_author(name=f"bro {ctx.author.mention} is so ballsies",icon_url=ctx.author.avatar)
    embed_message.set_thumbnail(url=ctx.guild.icon)
    embed_message.set_image(url=ctx.guild.icon)
    embed_message.add_field(name="balls", value="10", inline=(False))
    embed_message.set_footer(text="aaaaaaaaaaaaaaaaaaaaaaaaaa", icon_url=ctx.author.avatar)

    await ctx.send(embed = embed_message)

    @client.hybrid_command()
    @client.has_permissions(manage_message = True)
    async def clear(ctx, count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f"purge complete")

@client.hybrid_command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, modreason):
    await ctx.guild.kick(member)

    conf_embed=discord.Embed(title="success", colour=discord.Colour.gold())
    conf_embed.add_field(name="kicked: ", value=f"{member} from the server by {ctx.author.mention}", inline= False)
    conf_embed.add_field(name="reason: ", value=modreason, inline=False)

    await ctx.send(embed=conf_embed)

@client.hybrid_command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, modreason):
    await ctx.guild.ban(member)

    conf_embed=discord.Embed(title="success", colour=discord.Colour.gold())
    conf_embed.add_field(name="banned: ", value=f"{member} from the server by {ctx.author.mention}", inline= False)
    conf_embed.add_field(name="reason: ", value=modreason, inline=False)

    await ctx.send(embed=conf_embed)

@client.hybrid_command(aliases = ["pfp", "picture"])
async def avatar(ctx):
    embed_message = discord.Embed(title = "", description="", colour=discord.Colour.random())
    embed_message.set_author(name=f"{ctx.author.mention}'s avatar",icon_url=ctx.author.avatar)
    embed_message.set_image(url=ctx.author.avatar)
    embed_message.add_field(name="", value="", inline=(False))
    embed_message.set_footer(text="", icon_url=ctx.author.avatar)

    await ctx.send(embed = embed_message)

@client.hybrid_command()
async def balls(ctx):
    await ctx.send("https://tenor.com/view/balls-contact-juggling-meme-gif-22573466")

@client.hybrid_command()
async def list(ctx):
    embed_message = discord.Embed(title = "list of commands", description="", colour=discord.Colour.random())

    embed_message.set_author(name=f"",icon_url=ctx.author.avatar)

    #embed_message.add_field(name="balls\ntry it\n\nhomophobic\navatar\nsends image of your own avatar\n\nembed\ntesting out embed commands\n\niloveballs\nracist\nping\nshows the bot's ping\n\nbigping\npings you a lot\n\nrules\nshows rules\n\ncum\n\nrape\n\nsex\n\nisis\nwhy?\n\nterrorism\nالله أكبر\n\nliveleak\nliveleak website\n\npoop", value="", inline=(False))
    #i will find a way to keep descriptions for the commands
    embed_message.add_field(name="balls\nhomophobic\navatar\nembed\niloveballs\nracist\nping\nbigping\nrules\ncum\nrape\nsex\nisis\nterrorism\nliveleak\npoop\nthugshaker\nfart\nridley\nmen\nambatukum\namongussex\nfortnite\nblackmen\nblackniggerhangyourself\npenis\nletmeseeyourballs\npenisfactory\nsuckingdick\nthisismykingdomcum\nhundredyearoldmilfs", value="", inline=(False))
    embed_message.set_footer(text="all commands have to start with: !")

    await ctx.send(embed = embed_message)

@client.hybrid_command()
async def bigping(ctx):
    await ctx.send(ctx.author.mention)
    await ctx.send(ctx.author.mention)
    await ctx.send(ctx.author.mention)
    await ctx.send(ctx.author.mention)
    await ctx.send(ctx.author.mention)

@client.hybrid_command()
async def rules(ctx):
    await ctx.send("no rules")

@client.hybrid_command()
async def cum(ctx):
    await ctx.send("https://tenor.com/view/cum-penis-cum-i-creamed-cumming-xd-gif-20404521")

@client.hybrid_command()
async def rape(ctx):
    await ctx.send("wtf...")

@client.hybrid_command()
async def terrorism(ctx):
    await ctx.send("الله أكبر")

@client.hybrid_command()
async def sex(ctx):
    await ctx.send("sex 2 release date is <t:1735696800:R>")

@client.hybrid_command()
async def poop(ctx):
    await ctx.send("https://tenor.com/view/poop-pooping-otso-otso-shit-gif-13336997")

@client.hybrid_command()
async def liveleak(ctx):
    await ctx.send("https://www.itemfix.com/?r=ll")

@client.hybrid_command()
async def isis(ctx):
    await ctx.send("im not gonna go out of my way to find one of those beheading videos do it yourself")

@client.hybrid_command()
async def rwcist(ctx):
    await ctx.send("spell it right next time")

@client.hybrid_command()
async def fortnite(ctx):
    await ctx.send("https://tenor.com/view/sex-gif-20799821")

@client.hybrid_command()
async def amongussex(ctx):
    await ctx.send("https://tenor.com/view/among-us-sus-yhk-among-twerk-among-us-twerk-gif-23335803")

@client.hybrid_command()
async def silly(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1113363103812423761/1115244438218887309/979.png")

@client.hybrid_command()
async def fart(ctx):
    await ctx.send("https://tenor.com/view/peter-griffin-stewie-brian-family-guy-fart-gif-14113301")

@client.hybrid_command()
async def thugshaker(ctx):
    await ctx.send("https://tenor.com/view/thugshaker-gif-25916339")

@client.hybrid_command()
async def men(ctx):
    await ctx.send("https://tenor.com/view/kiss-make-out-hot-gay-mlm-gif-15507377")

@client.hybrid_command()
async def ridley(ctx):
    await ctx.send("https://tenor.com/view/youre-beautiful-face-ugly-wtf-gif-3855629")

@client.hybrid_command()
async def ambatukum(ctx):
    await ctx.send("https://tenor.com/view/ambatukam-ambasing-ambadeblow-gif-25400729")

@client.hybrid_command()
async def blackmen(ctx):
    await ctx.send("https://tenor.com/view/maid-dance-black-man-twerk-dance-twerk-gif-26318377")

@client.hybrid_command()
async def blackniggerhangyourself(ctx):
    await ctx.send("https://tenor.com/view/jump-hanging-gif-20498305")

@client.hybrid_command()
async def penis(ctx):
    await ctx.send("https://tenor.com/view/penis-plush-sex-happy-girl-funny-gif-21401963")

@client.hybrid_command()
async def letmeseeyourballs(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1113363103812423761/1115248929735462943/7ff1aw.png")

@client.hybrid_command()
async def penisfactory(ctx):
    await ctx.send("https://tenor.com/view/filling-pastry-gif-20433842")

@client.hybrid_command()
async def suckingdick(ctx):
    await ctx.send("https://tenor.com/view/mouse-drink-cool-down-sucking-mouse-job-gif-12109306")

@client.hybrid_command()
async def thisismykingdomcum(ctx):
    await ctx.send("https://tenor.com/view/funny-gif-22114363")

@client.hybrid_command()
async def hundredyearoldmilfs(ctx):
    await ctx.send("https://tenor.com/view/100-gif-5791252")

@client.hybrid_command()
async def jackoff(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1081649256110235691/1082828031791484999/ezgif-5-456c39aa6f.gif")

@client.hybrid_command()
async def jeffreydhamer(ctx):
    await ctx.send("dun dun dun dun dun dun du du du dun dun dun dun\nhttps://open.spotify.com/track/449DFUJKZlzSO684XlVjEn?si=31fc0fe87f1a44c4")

@client.hybrid_command()
async def gaysex(ctx):
    await ctx.send("https://pornhub.com/gay")

@client.hybrid_command()
async def fortniteballs(ctx):
    await ctx.send("https://www.youtube.com/watch?v=ZUvnJs7lJv8")

@client.hybrid_command()
async def renegaderaidernaked(ctx):
    await ctx.send("there is no way im searching up fortnite porn do it yourself (<@814070726889046077>)")

##@client.hybrid_command()
#async def testping(ctx):
#    i = 5
#    test = await ctx.send(ctx.author.mention)
#    while(test <= i):
#        print(test)
#       test = test + 1

@client.hybrid_command(name= "gaymidget", description= "pings a gay midget")
async def gaymidget(ctx):
    await ctx.send("<@814070726889046077>")

@client.hybrid_command()
async def mehavingsex(ctx):
    await ctx.send("use your imagination to picture a big cock")
    time.sleep(5)
    await ctx.send("wtf you actually did that?")
    time.sleep(1)
    await ctx.send("thats pretty gay ngl")

@client.hybrid_command()
async def mehavingfriends(ctx):
    await ctx.send("close discord and go outside you lonely fuck")

@client.hybrid_command()
async def grass(ctx):
    await ctx.send("kind of ironic how youre using discord to look at grass")
    time.sleep(3)
    await ctx.send("still gotchu")
    await ctx.send("https://tenor.com/view/touch-grass-gif-26144770")

@client.hybrid_command()
async def gonorhea(ctx):
    await ctx.send("i had to google this and i regret it")
    await ctx.send("also im not sending you an image of gonorhea you sick fuck")

@client.hybrid_command()
async def dhiarhea(ctx):
    await ctx.send("https://tenor.com/view/good-mornings-workout-hilarious-gif-25561128")

@client.hybrid_command()
async def ockyway(ctx):
    await ctx.send("wtf is ockyway")

@client.hybrid_command()
async def ohio(ctx):
    await ctx.send("https://tenor.com/view/ohio-average-day-average-day-in-ohio-venom-dunking-gif-26491693")

@client.hybrid_command()
async def moyai(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/1105978784429121606.webp?size=96&quality=lossless")

@client.hybrid_command()
async def whois(ctx, member: discord.User = None):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member
    info_embed = discord.Embed(title=f"{member.name}'s user information", description="take a wild guess", colour=discord.Colour.random())
    info_embed.set_header(url=member.avatar)
    info_embed.add_field(name="Name:", value=member.name, inline= False)
    info_embed.add_field(name="Nick:", value=member.display_name, inline= False)
    info_embed.add_field(name="Discriminator:", value=member.discriminator, inline= False)
    info_embed.add_field(name="ID:", value=member.id, inline= False)
    info_embed.add_field(name="Status:", value=member.status, inline= False)
    info_embed.add_field(name="Bot user?:", value=member.bot, inline= False)
    info_embed.add_field(name="Creation Date:", value=member.created_at.__format__("%A, %d. %B %Y @ %H:%M:%S"), inline= False)

    await ctx.send(embed=info_embed)

@client.hybrid_command()
async def commands(ctx):
    await ctx.send("no")

@client.hybrid_command(name="suggest", description="suggest a command")
async def suggest(ctx, *, suggestion):
    await ctx.channel.purge(limit=1)
    channel = discord.utils.get(ctx.guild.text_channels, name="suggestion")
    suggest = discord.Embed(title="New Suggestion", description=f"{ctx.author.name} Has Suggested\n `{suggestion}`")
    sugg = await channel.send(embed=suggest)
    await channel.send(f"||Suggestion Id: {sugg.id}||")
    await sugg.add_reaction("👍")
    await sugg.add_reaction("👎")

@client.hybrid_command()
async def approve(ctx, id:int=None, *, reason=None):
    if id is None:
        return 
    channel = discord.utils.get(ctx.guild.text_channels, name="suggestion")
    if channel is None:
        return
    suggestionMsg = await channel.fetch_message(id)
    embed = discord.Embed(title=f"Suggestion Has Been Approved", description=f"The Suggestion ID Of {suggestionMsg.id} has been approved by {ctx.author.name}\n Reason: `{reason}`")
    await channel.send(embed=embed)

@client.hybrid_command()
async def deny(ctx, id:int=None, *, reason=None):
    if id is None:
        return 
    channel = discord.utils.get(ctx.guild.text_channels, name="suggestion")
    if channel is None:
        return
    suggestionMsg = await channel.fetch_message(id)
    embed = discord.Embed(title=f"Suggestion Has Been Denied", description=f"The Suggestion ID of {suggestionMsg.id} has been denied by {ctx.author.name}\n Reason: {reason}")
    await channel.send(embed=embed)
    
@client.hybrid_command()
async def me(ctx):
    await ctx.send("https://imgur.com/0NB0ubH")

@client.hybrid_command()
async def coronacrazy(ctx):
    await ctx.send("https://tenor.com/view/gigachad-chad-gif-20773266")

@client.hybrid_command()
async def furry(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1049300718705709120/1118468121368477776/caption.png")

@client.hybrid_command()
async def kys (ctx):
    await ctx.send("you first")

@client.hybrid_command()
async def idrinkcum (ctx):
    await ctx.send("same")
    time.sleep(1)
    await ctx.send("https://tenor.com/view/fox-milk-i-want-milk-drink-milk-gif-15160105")

@client.hybrid_command()
async def sigmamale(ctx):
    await ctx.send("look in the mirror, king")

@client.hybrid_command()
async def andrewtate(ctx):
    await ctx.send("https://tenor.com/view/andrew-tate-bottom-g-dance-funny-tiktok-gif-5859294896048518806")

@client.hybrid_command()
async def opps(ctx):
    await ctx.send("https://tenor.com/view/fat-guy-shooting-gun-gun-shot-gif-15114243")

@client.hybrid_command()
async def gang(ctx):
    await ctx.send("https://tenor.com/view/yay-sarcastic-sponge-bob-gif-14611576")

@client.hybrid_command()
async def blud(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1049300718705709120/1118475316554367047/caption.gif")

@client.hybrid_command()
async def dickpick(ctx):
    await ctx.send("im just not commited enough yet...")
    time.sleep(2)
    await ctx.send("... you first")

@client.hybrid_command()
async def cumman(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/955298743568191528/1118474087094824970/video0-106.mp4")

@client.hybrid_command()
async def padi(ctx):
    await ctx.send("https://media.discordapp.net/attachments/954493268018733126/1005790359764344942/C0C58EBF-B8CA-4DAB-89CC-CAE4CD49CEE1.gif")

@client.hybrid_command()
async def cease(ctx, ammount : int):
    await ctx.channel.purge(limit = ammount+1)
    await ctx.send(f"Successfuly purged {ammount} messages", delete_after=10)

@client.hybrid_command()
async def temp(ctx):
    await ctx.send("woooooh temporary message jumpscare", delete_after=7)

@client.hybrid_command()
async def padipumppic(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1004081360182448262/1118827270002454598/Screenshot_20230615_105918_Snapchat.jpg")

@client.hybrid_command()
async def roullete(ctx):
    list1 = ["https://tenor.com/view/tire-hit-roll-ouch-gif-14493834", "https://cdn.discordapp.com/attachments/1113363103812423761/1119819004303912990/photo-1606491048802-8342506d6471.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818969596039168/photo-1541781774459-bb2af2f05b55.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818941821370520/photo-1583083527882-4bee9aba2eea.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818923353849897/photo-1506755855567-92ff770e8d00.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818898049597502/photo-1615678815958-5910c6811c25.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818879498207332/photo-1545529468-42764ef8c85f.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818879498207332/photo-1545529468-42764ef8c85f.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818857834618920/photo-1579168765467-3b235f938439.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818841699139676/photo-1571988840298-3b5301d5109b.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818817837731840/photo-1608848461950-0fe51dfc41cb.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818782580412616/photo-1615796153287-98eacf0abb13.png", "https://cdn.discordapp.com/attachments/1113363103812423761/1119818782580412616/photo-1615796153287-98eacf0abb13.png","https://cdn.discordapp.com/attachments/1113363103812423761/1119818760174440518/photo-1557427161-4701a0fa2f42.png", "https://imgur.com/a/swOnDki"]
    await ctx.send(random.choice(list1))

@client.hybrid_command()
async def fridge(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/889065898713952298/1120006438161485924/image.png")
    await ctx.send("hye samsong frigge  play metla pip efallng sund")

@client.hybrid_command()
async def donneman(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1104367411957866496/1120435822118846604/20230619_213034.jpg")

@client.hybrid_command()
async def padi2(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1104367411957866496/1120659459241410582/IMG_3464.jpg")
        
@client.hybrid_command()
async def helpme(ctx):
    await ctx.send("im boraedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")

client.run(token)
