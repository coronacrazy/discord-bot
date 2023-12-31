from typing import Optional
import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord import app_commands
import time
import sys
from discord.interactions import Interaction
sys.path.insert(0, 'discord.py-self')
import random
import json
import tracemalloc
import praw
import requests
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
async def on_message(msg):
    if "im "in msg.content:
        channel = msg.channel
        if msg.author.bot:
            return
        await channel.send("stop making everything about yourself")

    if 'bomb' in msg.content:
        channel = msg.channel
        if msg.author.bot:
                return
        await channel.send('i have a bomb')

    if " love " in msg.content:
        channel = msg.channel
        if msg.author.bot:
            return
        await channel.send("SAME :fire:")
    
    if " ananas " in msg.content:
        channel = msg.channel
        if msg.author.bot:
            return
        await channel.send("ananas")

@client.event
async def on_guild_join(guild):
    with open("theballs\mutes.json", "r") as f:
        muteRole = json.load(f)

        muteRole[str(guild.id)] = None

    with open("theballs\mutes.json", "w") as f:
        json.dump(muteRole, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("theballs\mutes.json", "r") as f:
        muteRole = json.load(f)

        muteRole.pop(str(guild.id))

    with open("theballs\mutes.json", "w") as f:
        json.dump(muteRole, f, indent=4)

@client.event
async def on_ready():
    await client.tree.sync()
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

class TestMenuButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="test",style=discord.ButtonStyle.blurple)
    async def test(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.channel.send(content="click (i hate basketball people)")
    @discord.ui.button(label="me",style=discord.ButtonStyle.green)

    async def test1(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.channel.send(content="click (i hate when the)")

    @discord.ui.button(label="actuallyme",style=discord.ButtonStyle.red)
    async def test2(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.channel.send(content="i h (real)")

@client.hybrid_command()
@commands.has_permissions(ban_members=True)
async def setmuterole(ctx, role: discord.Role):
    with open("theballs\mutes.json", "r") as f:
        muteRole = json.load(f)

        muteRole[str(ctx.guild.id)] = role.name

        with open("theballs\mutes.json", "w") as f:
            json.dump(muteRole, f, indent=4)

    conf_embed=discord.Embed(title="success", colour=discord.Colour.gold())
    conf_embed.add_field(name="mute role has been set", value=f"the mute role has been changed to {role.mention}", inline= False)

    await ctx.send(embed=conf_embed)

@client.hybrid_command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member):
    with open("theballs\mutes.json", "r") as f:
        role = json.load(f)
        
    mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])
    
    await member.add_roles(mute_role)
    
    conf_embed=discord.Embed(title="success", colour=discord.Colour.gold())
    conf_embed.add_field(name=f"muted", value=f"{member}", inline= False)

    await ctx.send(embed=conf_embed)

@client.hybrid_command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member):
    with open("theballs\mutes.json", "r") as f:
        role = json.load(f)
        
    mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])
    
    await member.remove_roles(mute_role)
    
    
    conf_embed=discord.Embed(title="success", colour=discord.Colour.gold())
    conf_embed.add_field(name=f"unmuted", value=f"{member}", inline= False)

    await ctx.send(embed=conf_embed)

@client.hybrid_command()
@commands.has_permissions(ban_members=True)
async def cease(ctx, ammount : int):
    await ctx.channel.purge(limit = ammount+1)
    await ctx.send(f"Successfuly purged {ammount} messages", delete_after=10)

@client.tree.command(name="button")
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(content="button menu", view=TestMenuButton())

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

class plotButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="yes", style=discord.ButtonStyle.gray)
    async def plotButtonNo(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send("based")
        await interaction.channel.send("https://tenor.com/view/meme-gif-25868570")
    @discord.ui.button(label="no", style=discord.ButtonStyle.gray)    
    async def plotButtonYes(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send("oh... thats kind of lame")
        time.sleep(1)
        await interaction.channel.send("i think you like this so here you go")
        await interaction.channel.send("https://pornhub.com/gay")

@client.tree.command(name="plot")
async def plot(interaction: discord.Interaction):
    await interaction.response.send_message(content="do you watch porn for the plot", view=plotButton)

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
async def avatar(ctx, member : discord.Member):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member
    embed_message = discord.Embed(title = "", description="", colour=discord.Colour.random())
    embed_message.set_author(name=f"{member.mention}'s avatar",icon_url=member.avatar)
    embed_message.set_image(url=member.avatar)
    embed_message.add_field(name="", value="", inline=(False))
    embed_message.set_footer(text="", icon_url=member.avatar)

    await ctx.send(embed = embed_message)

@client.hybrid_command()
async def balls(ctx):
    await ctx.send("https://tenor.com/view/balls-contact-juggling-meme-gif-22573466")

@client.hybrid_command()
async def list(ctx):
    await ctx.send("increasehealth\nmfw\nqualitycontent\nseraph\nhelpme\npingyourself\nping\nlotion\ntheavengers\nmeme\nreport\ndiscordsex\nephemeral\nultradoublesex\nroulleteping\nbetterbigping\nohio\nme\ncoronacrazy\nfurry\nkys\nidrinkcum\nsigmamale\nandrewtate\nopps\ngang\nblud\ndickpick\ncumman\npadi\ncease\ntemp\npadipumppic\nroullete\nfridge\ndonneman\npadi2\nhelpme\nmeme\ncum2\njackoff\njeffreydhamer\nfortniteballs\ngaysex\nrenegaderaidernaked\ngaymidget\nmehavingsex\nmehavingfriends\ngrass\ngonorhea\ndhiarhea\nockyway\nohio\nmoyai\nwhois\ncommands\nsuggest\nballs\nhomophobic\navatar\nembed\niloveballs\nracist\nping\nbigping\nrules\ncum\nrape\nsex\nisis\nterrorism\nliveleak\npoop\nthugshaker\nfart\nridley\nmen\nambatukum\namongussex\nfortnite\nblackmen\nblackniggerhangyourself\npenis\nletmeseeyourballs\npenisfactory\nsuckingdick\nthisismykingdomcum\nhundredyearoldmilfs")

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
    await ctx.send("https://tenor.com/view/awkward-umm-what-what-gif-14694719")

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
    await ctx.send("your suggestion has been submitted", ephemeral=True)
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
    list = "https://media.discordapp.net/attachments/954493268018733126/1005790359764344942/C0C58EBF-B8CA-4DAB-89CC-CAE4CD49CEE1.gif " "https://media.discordapp.net/attachments/954493268018733126/1005790359764344942/C0C58EBF-B8CA-4DAB-89CC-CAE4CD49CEE1.gif " "https://cdn.discordapp.com/attachments/1004081360182448262/1118827270002454598/Screenshot_20230615_105918_Snapchat.jpg " "https://cdn.discordapp.com/attachments/1104367411957866496/1120659459241410582/IMG_3464.jpg " "https://cdn.discordapp.com/attachments/1049300718705709120/1126857622830727188/caption.png " "https://cdn.discordapp.com/attachments/1004081360182448262/1126856768987856936/IMG_3543.png "
    await ctx.send(list)

@client.hybrid_command()
async def temp(ctx):
    await ctx.send("woooooh temporary message jumpscare", delete_after=7)

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
async def helpme(ctx):
    await ctx.send("im boraedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")

class pingButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="ping", style=discord.ButtonStyle.gray)
    async def ping(self, interaction: discord.Interaction, Button: discord.ui.Button):
        bot_latency = round(client.latency * 1000)
        await interaction.channel.send(content=f"pong {bot_latency} ms")

@client.tree.command(name="buttonping")
async def buttonping(interaction: discord.Interaction):
    await interaction.response.send_message(content="click button for ping", view=pingButton())

class buttonThatPingsYou(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ping yourself NOW", style=discord.ButtonStyle.gray)
    async def pingyourself(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send(interaction.user.mention)

@client.tree.command(name="pingyourself")
async def pingyourself(interaction: discord.Interaction):
    await interaction.response.send_message(content="you should ping yourself, NOW", view=buttonThatPingsYou())

class lotionbutton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="pass him the lotion", style=discord.ButtonStyle.gray)
    async def lotion(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send("someone send coronacrazy male wanking sound i cba to do it rn")

@client.tree.command(name="lotion", description="PASS HIM THE LOTION")
async def lotion(interaction: discord.Interaction):
    await interaction.response.send_message(content="https://cdn.discordapp.com/attachments/1049300718705709120/1121067164246495233/caption.gif", view=lotionbutton())

@client.hybrid_command()
async def theavengers(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/889066784836161607/1121063740318687305/e48aa147a71b569871e4ec839c589d64.mp4")

reddit_api = requests.get('https://www.reddit.com/r/memes/top/.json?sort=hot', headers = {'User-agent': 'corona bot thingy 0.1'})
reddit_apidata = reddit_api.text
parse_json_reddit_apidata = json.loads(reddit_apidata)
numba = random.randint(0,24)
link = parse_json_reddit_apidata['data']['children'][numba]['data']['url']

# i have no clue how to fix this help
class memebutton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="click for another meme", style=discord.ButtonStyle.gray)
    async def meme(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send(link)

@client.tree.command(name="meme", description="sends random meme from r/memes on reddit")
async def meme(interaction: discord.Interaction):
    if meme:
        numba = random.randrange(0, 24)
    await interaction.response.send_message(content=link, view=memebutton())

class cumbutton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="cum", style=discord.ButtonStyle.gray)
    async def cum2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send("https://tenor.com/view/cum-penis-cum-i-creamed-cumming-xd-gif-20404521")

@client.tree.command(name="cum2")
async def cum2(interaction: discord.Interaction):
    await interaction.response.send_message(content="idk why i made this", view=cumbutton())
    
# ill fix this later

#reddit_api2 = requests.get('https://www.reddit.com/r/FiftyFifty/top/.json?sort=hot', headers = {'User-agent': 'corona bot thingy 0.2'})
#reddit_apidata2 = reddit_api2.text
#parse_json_reddit_apidata2 = json.loads(reddit_apidata2)
#numba2 = random.randrange(0, 24)
#link2 = parse_json_reddit_apidata2['data']['children'][numba2]['data']['url']

#class fiftyfiftybutton(discord.ui.View):
#    def __init__(self):
#        super().__init__(timeout=None)
#
#   @discord.ui.button(label="fiftyfifty", style=discord.ButtonStyle.gray)
#    async def fiftyfifty(self, interaction: discord.Interaction):
#        await interaction.channel.send(link2)

#@client.tree.command(name="fiftyfifty", description="probably shouldnt use this command but its a 50 percent chance for a horific image and a 50 percent chance for a not horific image to send")
#async def fiftyfifty(interaction: discord.Interaction):
#    await interaction.response.send_message(content=link2, view=fiftyfiftybutton())

#Hi corona
#You cna canhgen the link on line 539 to whatever u want
#the link variable is the one you should send

#reddit_api = requests.get('https://www.reddit.com/r/learnpython/top/.json?sort=top&t=year', headers={'User-Agent':"corona bot thingy 0.1"})
#top_posts = r.json()
#top_post_titles = [x['data']['title'] for x in top_posts['data']['children']]

@client.hybrid_command()
async def ephemeral(ctx):
    await ctx.send("only you can see this", ephemeral=True)

class ReportModal(discord.ui.Modal, title="report user"):
    username = discord.ui.TextInput(label="username of person you wabnt to repoert", placeholder="fatesucks or something", required=True, max_length=20, style=discord.TextStyle.short)
    userid = discord.ui.TextInput(label="userid of the guy", placeholder="turn developer mode on and right click on the person", required=True, max_length=25, style=discord.TextStyle.short)
    description = discord.ui.TextInput(label="reason", placeholder="fatesucks broke rule 1: no general in memes", required=True, max_length=200, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} just reported {self.username} for {self.description} what a loser everyone gang up on them")

        channel = discord.utils.get(interaction.guild.channels, name="a")

        await channel.send(f"new report by {interaction.user.mention} \n name: {self.username} \n userid: {self.userid} \n because: {self.description}")

@client.tree.command(name="report", description="report someone")
async def report(interaction: discord.Interaction):
    await interaction.response.send_modal(ReportModal())

@client.hybrid_command()
async def discordsex(ctx):
    message = await ctx.send("https://txnor.com/view/ltg-low-tier-god-meme-gif-23851809")
    await message.add_reaction("😎")

@client.hybrid_command()
async def ultradoublesex(ctx):
    message = await ctx.send("https://txnor.com/vixw/ltg-low-tier-god-meme-gif-23851809")
    await message.add_reaction("😎")

class donberman(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="donberman", style=discord.ButtonStyle.gray)
    async def doberman(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send("idk whgy i made this but ping donneman anyway")

@client.tree.command(name="doberman")
async def doberman(interaction: discord.Interaction):
    await interaction.response.send_message(content="https://cdn.discordapp.com/attachments/955298743568191528/1125436688827699200/image.png", view=donberman())

@client.hybrid_command(name="roulleteping", description="1/10 chance to ping everyone")
async def roulleteping(ctx):
    if random.randint(1,5) == 5:
        await ctx.send(f"{ctx.guild.mention} pinga")

@client.hybrid_command()
async def betterbigping(ctx, member: discord.User = None):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member
    channel = ctx.channel
    await channel.send(member.mention)
    await channel.send(member.mention)
    await channel.send(member.mention)

@client.hybrid_command()
async def poll(ctx, *, suggestion):
    suggest = discord.Embed(title="New Poll", description=f"{suggestion}")
    sugg = await ctx.send(embed=suggest)
    await sugg.add_reaction("👍")
    await sugg.add_reaction("👎")

@client.hybrid_command()
async def increasehealth(ctx):
    await ctx.send("https://media.discordapp.net/attachments/720602225486856233/1006668096074952845/73375891-36CE-4BBF-B484-ECFCDA383F61.gif")

@client.hybrid_command()
async def qualitycontent(ctx):
    await ctx.send("https://www.youtube.com/watch?v=Ez-lB078WRM")

@client.hybrid_command()
async def mfw(ctx):
    await ctx.send("https://www.youtube.com/watch?v=Ez-lB078WRM")

@client.hybrid_command()
async def supersecretmessage(ctx):
    await ctx.author.send("seraph crabby aaaaaaaaaaaaaa")
    await ctx.send("check dms bbg")

@client.hybrid_command()
async def harras(ctx, member: discord.User = None):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member

    await ctx.send(f"you successfully harrased {member}", ephemeral=True)
    await member.send("sup bbg")
    await member.send("are you a woman")
    time.sleep(1)
    await member.send("cuz you mad ugly fr")

@client.hybrid_command()
async def iqtest(ctx, member: discord.User):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member

    await ctx.send(f"{member.mention}'s iq is {random.randint(1, 200)}")


client.run(token)
