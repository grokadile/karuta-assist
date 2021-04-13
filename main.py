import discord
from discord.ext import commands
import math
import asyncio
from discord.ext.commands import CommandNotFound
import time
import datetime

## INFO


token = "Nzc5NTAwNjAyNDg0MTk1MzI4.X7hcgg.3z6ONCbkhp-eyK7cr5hXfSOSXHg"
bot = commands.Bot(command_prefix=["k", "K"])

botIcon = "https://cdn.discordapp.com/attachments/795796743538475100/816500002163261500/water.png"
botInvite = "https://discord.com/api/oauth2/authorize?client_id=779500602484195328&permissions=2215640257&scope=bot"
serverInvite = "https://discord.gg/UuuEvKQN5Y"

rarities = ["damaged", "poor", "good", "excellent", "mint"]
taxes = {
    "uranium": 5,
    "quartz": 5,
    "sugar": 5,
    "bone": 5,
    "magma": 5,
    "wool": 5,
    "essence": 10,
    "ice": 10,
    "iron": 10,
    "stone": 10,
    "leaf": 10,
    "salt": 10,
    "copper": 25,
    "zinc": 40,
    "flower": 45,
    "wood": 49,
    "gold": 50
}
nodes = ["uranium", "quartz", "sugar",
         "bone", "magma", "wool",
         "essence", "ice", "iron",
         "stone", "leaf", "salt", "copper",
         "zinc", "flower", "wood", "gold"]
params = ["b", "s", "c", "g", "d", "t", "f", "dy", "e", "cp", "gp", "bn"]
tranks = ["f", "d", "c", "b", "a", "s"]
purities = [0, 0.0875, 0.175, 0.2625, 0.35]
paramNames = """b: base\ne: effort\ns: quickness (in seconds)\n
                c: dropped condition\ng: grabber (t/f)\nd: dropper (t/f)\n
                t: toughness (rank)\nf: frame (t/f)\ndy: dye (t/f/m)\n
                cp: card print\ngp: generated prints\nbp: burned prints"""
taxRates = """uranium: 5, quartz: 5, sugar: 5, bone: 5, magma: 5, wool: 5\n
                essence: 10, ice: 10, iron: 10, stone: 10, leaf: 10, salt: 10\n
                copper: 25, zinc: 40, flower: 45, wood: 49"""
basescale = 104
fixes = " - s now takes float values\n - Parameterized commands do not need '=', but cannot interchange between having '=' and not having '='\n - 'gt', 'dt' are now fixed\n - Introducing cl= for claimed cards (kbase will not take cp= anymore)"
soon = " - Vanity command\n - k= fix\n - Gem frame additions to frame testing\n - Morph/Dye for the kf command"
frames = ["https://cdn.discordapp.com/attachments/783771457468628996/818231355740651571/brass.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231354511720468/beachside.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231357083090964/cherryblossom.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231358727389204/crystalmines.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231359674908682/fortress.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231361168736306/nightcrow.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231363064168458/spiritflame.png",
          "https://media.discordapp.net/attachments/783771457468628996/818231364251025409/submarine.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818231366357483526/volcanic.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257449856270356/autumnview.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257450733928478/barbecue.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257567008161852/edofurin.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257568186499152/faerieforest.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257720439472169/fuselage.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257721782304788/icecreamsundae.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257723157774356/kominka.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257724679782410/magitek.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257727373049907/magus.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257983774392320/patchwork.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257985728938054/robotic.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257988006576168/rozen.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818257993031221299/smithyforge.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818258164599750696/venicecarnival.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818258218630381608/snowlands.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818258219977015326/spaceship.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818258360561696788/watermelonjuice.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818258361622462484/whirlpool.png",
          "https://cdn.discordapp.com/attachments/783771457468628996/818258363007631401/wildwest.png"]
gframes = ["https://cdn.discordapp.com/attachments/783771457468628996/819029124655349770/arabiannights.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029125373100042/bookworm.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029127176519700/casefiles.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029129516941332/casino.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029129944104980/electrocell.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029319476576256/gothictower.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029320818622494/holidaytreats.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029322127769610/kintsugi.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029323415683104/pastelcastle.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029324891815936/royalprincess.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029498942455848/rustyfortress.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029499890106368/showman.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029500708651038/starrysky.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029502721130516/startertown.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029506354315275/strawberrydessert.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029681512513576/sushi.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029682313232444/tombrelic.png",
           "https://cdn.discordapp.com/attachments/783771457468628996/819029684272234506/witchaltar.png"]

## FLOWERS
tulip = "<@166271462175408130>, <@150697075657408513>"  # me, frank
rose = "<@244318220276727820>"  # terry
sunflower = ""
blossom = ""

listids = ["166271462175408130", "150697075657408513", "244318220276727820", "398188915326058496",#jerard
          "183658886790774784", "136130217537306624", "334812827137343498", "226588531772882945", "450099488745324545"]
block = "\\"

## INIT
@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

## STRING FILTERER
def split(kc):
    k = kc.split("^")[1:]
    if (k[0])[0:16] == "Cards carried by":
        a = k[0].split('\n')
        cards = a[2:]
    else:
        cards = k[0].split('\n')
    x = []
    d = []
    if len(k) == 2:
        char = (k[1])[1:]
        for i in cards:
            if char in i.lower():
                x.append(i)
    else:
        for i in cards:
            x.append(i)
    for i in x:
        d.append(strip(i))
    s = ''
    for i in d:
        if i == d[-1]:
            s += i
        else:
            s += i + ', '
    return s

## HELPERS
def strip(card):
    c = card.split()
    if c[0][0] == "♡":
        return c[2]
    elif c[1][0] == "♡":
        return c[3]
    elif c[0][0] != "♡" and c[2] == "·":
        return c[1]
def toWord(s):
    if s == "e":
        return "Effort"
    elif s == "b":
        return "Base"
    elif s == "s":
        return "Quickness"
    elif s == "p":
        return "Purity"
    elif s == "g":
        return "Grabber"
    elif s == "d":
        return "Dropper"
    elif s == "t":
        return "Toughness"
    elif s == "f/d":
        return "Style"
    elif s == "v":
        return "Vanity"
    elif s == "w":
        return "Wellness"
def cConvert(condition):
    if condition in rarities:
        c = rarities.index(condition)
    else:
        c = int(condition)
    return c
def tConvert(rank):
    r = rank.lower()
    return tranks.index(r)
def containsEqual(args):
    return "=" in ''.join(args)
def addEquals(args):
    out = []
    for i in args:
        p = i[0]
        if i[0] not in ["d", "c", "g"]:
            q = i[1:]
            out.append(p + "=" + q)
        elif i[0] in ["d", "c", "g"]:
            l = [str(a) for a in range(0, 10)] + ["t", "f"]
            if i[1] in l:
                q = i[1:]
                out.append(p + "=" + q)
            elif i[1:] in rarities:
                q = i[1:]
                out.append(p + "=" + q)
            else:
                p = i[:2]
                q = i[2:]
                out.append(p + "=" + q)
    return out
def findUrl(name):
    for i in frames:
        if name in i:
            return i
def isCallerAndCorrect(author, content, ch):
    def inner(message):
        return message.author == author and message.content.lower()[:3] == content and message.channel == ch
def containsEmbed(ch):
    def inner(message):
        return message.embeds != [] and message.channel == ch
def isRightUser(reaction):
    def inner(message):
        return message.author.user in reaction.users()

def getValue(line):
    dropper = ""
    l = line.split(" ")
    if l[0] == "Owned":
        return ('owner', l[-1])
    elif l[0] == "Dropped" and l[1] == "in":
        return ('condition', l[2])
    elif l[0] == "Grabbed" and l[1] == "after":
        return ('quickness', float(l[2]))
    elif l[0] == "Framed":
        return ('frame_name', ' '.join(l[2:]))
    elif l[0] == "Dyed":
        return ('dye_info', [' '.join(l[2:-1]), l[-1]])
    elif "fought" in l:
        if l[0] == "Another":
            t = "D"
        elif l[0] == "2":
            t = "C"
        elif l[0] == "3":
            t = "B"
        elif l[0] == "4":
            t = "A"
        else :
            t = "S"
        return ('toughness', t)
    elif l[0] == "Grabbed" and l[1] == "by":
        return ('grabber', l[-1])
    elif l[0] == "Dropped" and l[1] == "by":
        return ('dropper', l[-1])

def stripkci(s):
    x = s.replace("*", "").replace("`", "")
    t = x.split("\n")
    info = t[0].split('·')
    infoacc = []
    for i in info:
        infoacc.append(" ".join(i.split()))
    acc = [('card_print', int(infoacc[2][1:]))
           ]
    for i in t[4:]:
        if getValue(i) == None:
            pass
        elif getValue(i) == '':
            acc.append(('toughness', 'F'))
        else:
            acc.append(getValue(i))
    for i in acc:
        if i[0] == "dye_info":
            acc.append(('dye_name', i[1][0]))
            acc.remove(i)
    return acc

## CLASSES
class orderedCommands:
    def __init__(self, args):
        self.a1 = args[0]
        self.a2 = args[1]

    def mint(self):
        effort = self.a1
        condition = self.a2
        e = int(effort)
        c = cConvert(condition)
        if c < 0 or c > 4:
            return "Invalid rarity."
        elif c == 4:
            return "Do you need to ask?"
        else:
            minted = round(e * (1.88 ** (4 - c)))
            if minted > 140:
                return str(minted) + " 💪"
            elif minted < 10:
                return str(minted) + " 🤣"
            else:
                return str(minted)

    def bandage(self):
        e = int(self.a1)
        w = abs(int(self.a2))
        return round((e + w) * 1.25)

    def e(self):
        t1 = self.a1
        t2 = self.a2
        if '.' in t1 or '.' in t2:
            return "Only integer values."
        elif t2 == '0':
            return "Nice try."
        elif t1 == t2:
            return "Do you even need to ask?"
        elif t1 in nodes:
            r1 = 100 - taxes[t1]
            if t2 in nodes:
                r2 = 100 - taxes[t2]
            else:
                r2 = int(t2)
        elif t2 in nodes:
            r1 = 100 - taxes[t2]
            if t2 in nodes:
                r2 = 100 - taxes[t1]
            else:
                r2 = int(t2)
        elif int(t1) > 99 or int(t2) > 99 or int(t1) < 0 or int(t2) < 0:
            return "Nice try"
        else:
            r1 = 100 - int(t1)
            r2 = 100 - int(t2)
        return str(round(r1 / r2, 3)) + " to 1"
class parameterCommands:
    def __init__(self, args):
        self.b = -1
        self.s = 0
        self.c = 0
        self.g = False
        self.d = False
        self.t = "f"
        self.f = False
        self.dy = "f"
        self.e = 0
        self.cp = 1
        self.gp = 1
        self.cl = 1
        self.bp = 1
        listparams = []
        for i in args:
            listparams.append(i.split("=")[0])
        for i in args:
            if "=" in i:
                p = i.split("=")[0]
                q = i.split("=")[-1]
                if p == "b":
                    self.b = int(q)
                elif p == "s":
                    self.s = int(q.split(".")[0])
                elif p == "c":
                    self.c = cConvert(q)
                elif p == "g":
                    if q == "t":
                        self.g = True
                elif p == "d":
                    if q == "t":
                        self.d = True
                elif p == "t":
                    self.t = q
                elif p == "f":
                    self.f = q == "t"
                elif p == "dy":
                    self.dy = q
                elif p == "e":
                    self.e = int(q)
                elif p == "cp":
                    self.cp = int(q)
                elif p == "gp":
                    self.gp = int(q)
                elif p == "cl":
                    self.cl = int(q)
                elif p == "bp":
                    self.bp = int(q)

    def am(self):
        if self.b < 0:
            base = round((self.cl - self.bp)/self.gp * basescale)
        else:
            base = self.b
        grab = 0
        drop = 0
        frame = 0
        dye = 0
        if self.s >= 10:
            quick = 0
        else:
            quick = round(base * (20 - 2 * math.floor(self.s)) / 100)
        purity = round(base * purities[self.c])
        if self.g:
            grab = round(base / 10)
        if self.d:
            drop = round(base / 10)
        tough = round(base * 0.05 * tConvert(self.t))
        if self.f:
            frame = round(base * 0.75)
        if self.dy == "t":
            dye = round(base / 5)
        elif self.dy == "m":
            dye = round(base * 0.75)
        style = frame + dye
        vanity = round(base / 2 * (1 - self.cp/self.gp))
        bst = base + quick + purity + grab + drop + tough + style + vanity
        wellness = round(bst / 4)
        effort = bst + wellness
        statlist = sorted([effort, base, quick, purity, grab, drop, tough, style, vanity, wellness])
        statdict = {
            "e": effort,
            "b": base,
            "s": quick,
            "p": purity,
            "g": grab,
            "d": drop,
            "t": tough,
            "f/d": style,
            "v": vanity,
            "w": wellness
        }
        statlist.reverse()
        return statlist, statdict

    def s(self):
        base = self.b
        effort = self.e
        if self.dy == "t":
            dye = round(base / 5)
        elif self.dy == "m":
            dye = round(base * 0.75)
        elif self.dy == "f":
            dye = 0
        if self.f:
            frame = round(base * 0.75)
        else:
            frame = 0
        style = frame + dye
        return effort + round(style * 1.25)

    def base(self):
        return round((self.cl - self.bp) / self.gp * basescale)

## COMMANDS
@bot.command()
async def defaults(ctx):
    default = discord.Embed(title = "Bot Defaults", description = "All the default numbers can be found here", inline = False)
    default.set_thumbnail(url = botIcon)
    default.add_field(name = "Command Parameters", value = paramNames, inline = False)
    default.add_field(name = "Tax Rates", value = taxRates, inline = False)
    await ctx.send(embed = default)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}", inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def oc(ctx):
    ocHelp = discord.Embed(title = "Ordered Commands Help", description = "The order of which you input the parameteres matters, and you do not need to define which is which", inline = False)
    ocHelp.set_thumbnail(url = botIcon)
    ocHelp.add_field(name = "Mint", value = "<current effort> <current condition (either in words or 0-4)", inline = False)
    ocHelp.add_field(name = "Bandage", value = "<current effort> <wellness (can be either negative or positive>", inline = False)
    ocHelp.add_field(name = "Exchange (e)", value = "<node 1> <node 2> - instead of node names tax values are also accepted")
    ocHelp.set_footer(text = "All parameters must be filled for the command to work.")
    await ctx.send(embed = ocHelp)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def pc(ctx):
    check = " Check defaults for more help on parameters"
    pcHelp = discord.Embed(title = "Parameterized Commands", description = "The order of parameters does not matter, and you may leave some out, but you must define each value.", inline = False)
    pcHelp.set_thumbnail(url = botIcon)
    pcHelp.add_field(name = "Accurate Mint (am)", value = "Calculates the effort of a card at mint accurately." + check, inline = False)
    pcHelp.add_field(name = "Style (s)", value = "Calculates the effort of a card after frame/dye. A simplified version of accurate mint", inline = False)
    pcHelp.add_field(name = "Base", value = "Calculates a card's value from card print, generated print, and burned prints." + check, inline = False)
    pcHelp.set_footer(text = check[1:])
    await ctx.send(embed = pcHelp)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def examples(ctx):
    ex = discord.Embed(title = "Examples", description = "An example of each command", inline = False)
    ex.set_thumbnail(url = botIcon)
    ex.add_field(name = "Ordered Commands Examples", value = """kmint 43 good | kmint 43 2\n
                                                                kbandage 35 100\n
                                                                ke zinc gold | ke 10 15""", inline = False)
    ex.add_field(name = "Parameterized Commands Examples", value = """kam b=100 s=0 g=t d=t t=s c=mint cp=1 gp=197 f=t dy=t\n
                                                                        ks b=100 e=250 f=t d=m\n
                                                                        kbase cp=950 gp=1000 bp=0""")
    await ctx.send(embed = ex)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def invites(ctx):
    inv = discord.Embed(title = "Bot Invites", description = "Invite links", inline = False)
    inv.set_thumbnail(url = botIcon)
    inv.add_field(name = "Bot Invite", value = botInvite, inline = False)
    inv.add_field(name = "Server Invite", value = serverInvite, inline = False)
    await ctx.send(embed = inv)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def info(ctx):
    info = discord.Embed(title = "Bot Info", description = "Notice Board", inline = False)
    info.set_thumbnail(url = botIcon)
    info.add_field(name = "Current Ping Commands", value = "FLOWERS - **OFF**", inline = False)
    info.add_field(name = "Fixes", value = fixes, inline = False)
    info.add_field(name = "Coming soon", value = soon, inline = False)
    info.add_field(name = "Note that the frame test command needs to be hosted locally (at the moment)", value = "Currently working on it, ping <@166271462175408130> if you need it.\nHere's a sneak peak of what's to come:", inline = False)
    info.set_image(url = "https://cdn.discordapp.com/attachments/795796743538475100/824186507002380308/tmpi8vczrfl.PNG")
    await ctx.send(embed = info)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)

# OC
@bot.command()
async def mint(ctx, *args):
    oc = orderedCommands(args)
    await ctx.send(orderedCommands.mint(oc))
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def bandage(ctx, *args):
    oc = orderedCommands(args)
    await ctx.send(orderedCommands.bandage(oc))
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command(aliases=["e", "ex", "exch"])
async def exchange(ctx, *args):
    oc = orderedCommands(args)
    await ctx.send(orderedCommands.e(oc))
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
# @bot.command(aliases = ["frame", "frametest", "ft"])
# async def f(ctx, *args):
#     card_url = [*args][0]
#     frame_name = [*args][1]
#     if card_url[-3:] == "png" or card_url[-3:] == "jpg":
#         await ctx.send("Please change .png to .p")
#     elif card_url[-2:] == ".p":
#         card_url = card_url + "ng"
#         frame_url = findUrl(frame_name)
#         if frame_url == None:
#             await ctx.send("Please input a valid frame")
#         else:
#             card_response = requests.get(card_url, stream=True)
#             frame_response = requests.get(frame_url, stream=True)
#             with open('card.png', 'wb') as file:
#                 shutil.copyfileobj(card_response.raw, file)
#             with open('frame.png', 'wb') as file:
#                 shutil.copyfileobj(frame_response.raw, file)
#             del frame_response
#             del card_response
#             card = Image.open('card.png').resize((274, 400))
#             frame = Image.open('frame.png').resize((258, 376))
#             card.paste(frame, (10, 10), mask=frame)
#             card.save("final.png", "PNG")
#             await ctx.send(file=discord.File("final.png"))
# @bot.command(aliases = ["allframe", "allframetest", "aft"])
# async def af(ctx, url):
#     percent = 0
#     mes = await ctx.send(f"{percent}% done!")
#     back = Image.new("RGB", (1644, 2000), (255, 255, 255))
#     width = 274
#     height = 400
#     card_url = url + "ng"
#     for i in frames:
#         percent += 1
#         s = ''
#         w = "                                     "
#         blocks = round(percent*6/5) * [block]
#         for d in blocks:
#             s += d
#             w = w[1:]
#         await mes.edit(content=f"{round(percent / 3 * 10, 1)}% done!\n|{s}{w}🏁")
#         c_w = (frames.index(i) % 6) * width
#         c_h = math.floor(frames.index(i) / 6) * height
#         card_response = requests.get(card_url, stream=True)
#         frame_response = requests.get(i, stream=True)
#         with open('card.png', 'wb') as file:
#             shutil.copyfileobj(card_response.raw, file)
#         with open('frame.png', 'wb') as file:
#             shutil.copyfileobj(frame_response.raw, file)
#         del frame_response
#         del card_response
#         card = Image.open('card.png').resize((274, 400))
#         frame = Image.open('frame.png').resize((258, 376))
#         card.paste(frame, (10, 10), mask=frame)
#         back.paste(card, (c_w, c_h))
#     back.save("final.png", "PNG")
#     await ctx.send(file = discord.File("final.png"))
#     await mes.delete()
# @bot.command(aliases = ["gf", "allgemframe", "gemframe"])
# async def agf(ctx, url):
#     back = Image.new("RGB", (1644, 2000), (255, 255, 255))
#     width = 274
#     height = 400
#     card_url = url + "ng"
#     for i in gframes:
#         c_w = (gframes.index(i) % 6) * width
#         c_h = math.floor(gframes.index(i) / 6) * height
#         card_response = requests.get(card_url, stream=True)
#         frame_response = requests.get(i, stream=True)
#         with open('card.png', 'wb') as file:
#             shutil.copyfileobj(card_response.raw, file)
#         with open('frame.png', 'wb') as file:
#             shutil.copyfileobj(frame_response.raw, file)
#         del frame_response
#         del card_response
#         card = Image.open('card.png').resize((274, 400))
#         frame = Image.open('frame.png').resize((258, 376))
#         card.paste(frame, (10, 10), mask=frame)
#         back.paste(card, (c_w, c_h))
#     back.save("final.png", "PNG")
#     await ctx.send(file = discord.File("final.png"))

## PC
@bot.command()
async def am(ctx, *args):
    if containsEqual([*args]):
        obj = parameterCommands([*args])
    else:
        obj = parameterCommands(addEquals([*args]))
    inp = parameterCommands.am(obj)
    statlist = inp[0]
    statdict = inp[1]
    restlist = statlist[1:]
    restdict = {i:statdict[i] for i in statdict if i != "e"}
    restrestdict = {i:restdict[i] for i in restdict if i != "b"}
    restrestlist = [i for i in restlist if i not in restrestdict.items()]
    desc = f"Base: {restdict['b']}\n"
    for i in restrestlist:
        for key, value in restrestdict.items():
            if value == i:
                desc += f"{toWord(key)}: {value}\n"
                restrestdict[key] = -1
    card = discord.Embed(title="Worker Details", description=f"Showing worker details for <@{ctx.author.id}>\n\nEffort: **{statlist[0]}**", inline=False)
    card.set_thumbnail(url = botIcon)
    card.add_field(name = "**Effort Modifiers**", value = desc, inline = False)
    card.set_footer(text="All values are correct. If there is an issue please check your inputs.\nCall kpc for more help about this command")
    if [*args] == []:
        await ctx.send("Please have at least 1 parameter")
    else:
        await ctx.send(embed = card)
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def s(ctx, *args):
    if containsEqual([*args]):
        pc = parameterCommands([*args])
    else:
        pc = parameterCommands(addEquals([*args]))
    if [*args] == []:
        await ctx.send("Please have at least 1 parameter")
    else:
        await ctx.send(parameterCommands.s(pc))
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)
@bot.command()
async def base(ctx, *args):
    if containsEqual([*args]):
        pc = parameterCommands([*args])
    else:
        pc = parameterCommands(addEquals([*args]))
    if [*args] == []:
        await ctx.send("Please have at least 1 parameter")
    else:
        await ctx.send(parameterCommands.base(pc))
    channel = bot.get_channel(825955683996401685)
    e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{ctx.author.id}>",
                      url=f"https://discord.com/channels/{ctx.message.guild.id}/{ctx.message.channel.id}/{ctx.message.id}",
                      inline=False)
    e.add_field(name="Message", value=f"{ctx.message.content.lower()}", inline=False)
    await channel.send(embed=e)

@bot.event
async def on_reaction_add(reaction, user):
    m = reaction.message
    if user.id == 646937666251915264 and reaction.custom_emoji:
        c = bot.get_channel(826680875637800961)
        await c.send(f"https://discord.com/channels/{reaction.message.guild.id}/{reaction.message.channel.id}/{reaction.message.id}")
        time.sleep(3)
        if reaction.count == 1:
            if m.guild.id == 795795754542694430:
                await m.channel.send("<@&826586690146926602>")

@bot.event
async def on_message(message):
    m = message.content
    ch = message.channel
    mlower = m.lower()
    g = message.guild
    a = message.author
    rest = mlower[0:2]
    if rest == "f^":
        await ch.send(split(m))
        channel = bot.get_channel(825955683996401685)
        e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{message.author.id}>",
                          url=f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}",
                          inline=False)
        e.add_field(name="Message", value=f"{message.content.lower()}", inline=False)
        await channel.send(embed=e)
    if ch.id == 829128151795236894:
        await message.add_reaction("🤡")
    if mlower == "kbase":
        await message.add_reaction("👀")
        try:
            await bot.wait_for("message", check=isCallerAndCorrect(a, "klu", ch), timeout=5)
        except asyncio.TimeoutError:
            await ch.send("Timed out")
        while True:
            try:
                embed_msg = await bot.wait_for("message", check=containsEmbed(ch), timeout=5)
                embed = embed_msg.embeds[0]
                if embed.title == "Character Lookup":
                    embed_desc = embed.description.replace(',', '').replace('*', '')
                    desc_list = embed_desc.split("\n")
                    gen = desc_list[6]
                    circ = desc_list[9]
                    gp = int(gen.split(" ")[-1])
                    ci = int(circ.split(" ")[-1])
                    base = round(ci / gp * basescale)
                    msg = await ch.send(base)
                    await msg.add_reaction("🔁")
                    break
            except asyncio.TimeoutError:
                await ch.send("Timed out")
                break
            except IndexError:
                pass
        try:
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == "🔁"
            await bot.wait_for("reaction_add", check=check, timeout=5)
            embed = embed_msg.embeds[0]
            if embed.title == "Character Lookup":
                embed_desc = embed.description.replace(',', '').replace('*', '')
                desc_list = embed_desc.split("\n")
                gen = desc_list[6]
                circ = desc_list[9]
                gp = int(gen.split(" ")[-1])
                ci = int(circ.split(" ")[-1])
                base = round(ci / gp * basescale)
                await msg.edit(content=base)
        except asyncio.TimeoutError:
            await ch.send("Timed out")
        channel = bot.get_channel(825955683996401685)
        e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{message.author.id}>",
                          url=f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}",
                          inline=False)
        e.add_field(name="Message", value=f"{message.content.lower()}", inline=False)
        await channel.send(embed=e)
    elif mlower[:3] == "kwi" and mlower[-8:] in ["f=t dy=t", "f=f dy=f", "f=t dy=f", "f=f dy=t", "f=t dy=m", "f=f dy=m",
                                                 "dy=t f=t", "dy=f f=f", "dy=f f=t", "dy=t f=f", "dy=m f=t", "dy=m f=f"]:
        try:
            embed_msg = await bot.wait_for("message", check=containsEmbed(ch), timeout=5)
            embed = embed_msg.embeds[0]
            if embed.title == "Worker Details":
                desc = embed.description
                effort = int(desc.split("\n")[1].split(" ")[-1].replace("*", ""))
                sd = desc.split("**Effort modifiers**")
                stats = ''.join(sd[1]).replace("`", "").replace(u'\xa0', u' ')
                statslist = stats.split("\n")[1:]
                base = 0
                style = 0
                frame = ''
                dye = ''
                for i in statslist:
                    if "Base" in i:
                        base = int(i.split(" ")[-3])
                    elif "Style" in i:
                        style = int(i.split(" ")[-3])
                stylelist = mlower[-8:].split(" ")
                for i in stylelist:
                    if i[0] == "f":
                        frame = i
                    elif i[0] == "d":
                        dye = i
                if style == 0:
                    obj = parameterCommands([f"b={base}", f"e={effort}", frame, dye])
                if style == round(base * 1.5):
                    obj = parameterCommands([f"b={base}", f"e={effort}", "f=f", "dy=f"])
                elif style == round(base*0.95):
                    if dye == "dy=t":
                        obj = parameterCommands([f"b={base}", f"e={effort}", "f=f", "dy=f"])
                    else:
                        obj = parameterCommands([f"b={base}", f"e={effort+round(base*1.25*0.55)}", "f=f", "dy=f"])
                elif style == round(base*0.2):
                    if dye == "dy=m":
                        obj = parameterCommands([f"b={base}", f"e={effort+round(base*1.25*0.55)}", frame, "dy=f"])
                    elif dye == "dy=t":
                        obj = parameterCommands([f"b={base}", f"e={effort}", frame, "dy=f"])
                else:
                    obj = parameterCommands([f"b={base}", f"e={effort}", frame, dye])
                await ch.send(parameterCommands.s(obj))
        except asyncio.TimeoutError:
            await ch.send("Timed out")
        except IndexError:
            pass
        channel = bot.get_channel(825955683996401685)
        e = discord.Embed(title=f"Time: {datetime.datetime.now()}", description=f"Called by <@{message.author.id}>",
                          url=f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}",
                          inline=False)
        e.add_field(name="Message", value=f"{message.content.lower()}", inline=False)
        await channel.send(embed=e)
    elif mlower == "kam":
        await message.add_reaction("👀")
        try:
            await bot.wait_for("message", check=isCallerAndCorrect(a, "klu", ch), timeout=5)
        except asyncio.TimeoutError:
            await ch.send("Timed out")
        while True:
            try:
                klu = await bot.wait_for("message", check=containsEmbed(ch), timeout=5)
                klu_e = klu.embeds[0]
                if klu_e.title == "Character Lookup":
                    klu_d = klu_e.description.replace(',', '').replace('*', '').split("\n")
                    time.sleep(1)
                    await klu.add_reaction("🔁")
                    break
            except asyncio.TimeoutError:
                await ch.send("Timed out")
                break
            except IndexError:
                pass
        while True:
            try:
                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) == "🔁"
                await bot.wait_for("reaction_add", check=check, timeout=5)
                klu_e = klu.embeds[0]
                if klu_e.title == "Character Lookup":
                    klu_d = klu_e.description.replace(',', '').replace('*', '').split("\n")
                    await klu.add_reaction("✅")
                    break
            except asyncio.TimeoutError:
                await ch.send("Timed out")
                break
        while True:
            try:
                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) == "✅"
                await bot.wait_for("reaction_add", check=check, timeout=5)
                break
            except asyncio.TimeoutError:
                await ch.send("Timed out")
                break
        while True:
            try:
                await bot.wait_for("message", check=isCallerAndCorrect(a, "kci", ch), timeout=5)
                break
            except asyncio.TimeoutError:
                await ch.send("Timed out")
                break
        while True:
            try:
                kci = await bot.wait_for("message", check=containsEmbed(ch), timeout=5)
                e_kci = kci.embeds[0]
                kci_d = e_kci.description.replace(',', '').replace('*', '')
                await kci.add_reaction("✅")
                break
            except asyncio.TimeoutError:
                await ch.send("Timed out")
                break
            except IndexError:
                pass
        try:
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == "✅"
            await bot.wait_for("reaction_add", check=check, timeout=5)
            kciinfo = tupletostr(stripkci(kci_d))
            kluinfo = klutoinfo(klu_d)
            kinfo = [i for i in (kluinfo + ' ' + kciinfo).split(" ")]
            print(kinfo)
            obj = parameterCommands(kinfo)
            inp = parameterCommands.am(obj)
            statlist = inp[0]
            statdict = inp[1]
            restlist = statlist[1:]
            restdict = {i: statdict[i] for i in statdict if i != "e"}
            desc = ""
            for i in restlist:
                for key, value in restdict.items():
                    if value == i:
                        desc += f"{toWord(key)}: {value}\n"
                        restdict[key] = -1
            card = discord.Embed(title="Worker Details",
                             description=f"Showing worker details for <@{message.author.id}>\n\nEffort: **{statlist[0]}**",
                             inline=False)
            card.set_thumbnail(url=botIcon)
            card.add_field(name="**Effort Modifiers**", value=desc, inline=False)
            card.set_footer(
                text="All values are correct. If there is an issue please check your inputs.\nCall kpc for more help about this command")
            await ch.send(embed=card)
        except asyncio.TimeoutError:
            await ch.send("Timed out")
    else:
        await bot.process_commands(message)

def klutoinfo(klu):
    gen = klu[6]
    circ = klu[9]
    gp = int(gen.split(" ")[-1])
    ci = int(circ.split(" ")[-1])
    base = round(ci / gp * basescale)
    return f"b={base} gp={gp}"

def tupletostr(t):
    acc = []
    for i in t:
        if i[0] == "owner":
            owner = i[-1]
    for i in t:
        name = i[0]
        value = i[1]
        if name == 'card_print':
            acc.append(f"cp={value}")
        elif name == 'grabber':
            if value == owner:
                acc.append("g=t")
        elif name == 'dropper':
            if value == owner:
                acc.append("d=t")
        elif name == 'condition':
            acc.append(f"c={value}")
        elif name == 'quickness':
            acc.append(f"s={value}")
        elif name == 'frame_name':
            acc.append('f=t')
        elif name == 'dye_name':
            d = value.split(" ")
            if d[0] == "Mystic":
                acc.append('dy=m')
            else:
                acc.append('dy=t')
        elif name == 'toughness':
            acc.append(f"t={value.lower()}")
    return ' '.join(acc)

## RUN
bot.run(token)