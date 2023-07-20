import nextcord
from nextcord.ext import commands
from nextcord.utils import utcnow
from timestamp import default
import os
import random
from modules.components import HelpCommandView
from modules.utils import maybe_delete
from dotenv import load_dotenv

load_dotenv()


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="d.", intents=intents)
bot.remove_command("help")


@bot.command()
async def embed(ctx, *, content: str):
    await ctx.channel.purge(limit=1)
    title, description = content.split("|")
    embed = nextcord.Embed(
        title=title,
        description=description,
        color=nextcord.Colour.blue(),
        timestamp=ctx.message.created_at,
    )
    await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def say(ctx, *, arg):
    await maybe_delete(ctx.message)
    await ctx.send(arg)


@bot.command()
async def help(ctx):
    view = HelpCommandView()
    await maybe_delete(ctx.message)
    emb = nextcord.Embed(
        title="Umi <3 | Помощь",
        description="Тут описаны все команды!",
        timestamp=ctx.message.created_at,
        color=nextcord.Color.blue(),
    )
    emb.add_field(
        name="> Информация",
        value="`d.user` `d.banner` `d.avatar` `d.uptime` `d.server`",
        inline=False,
    )
    emb.add_field(name="> Утилиты", value="`d.embed`", inline=False)
    emb.add_field(
        name="> Реакции",
        value="`d.hi` `d.wherehave` `d.understood` `d.pon` `d.good` `d.good2`",
        inline=False,
    )
    emb.add_field(
    name="> Roleplay",
    value="`d.hug`",
    inline=False,
    )
    emb.add_field(name="> Модерация", value="`d.ban` `d.kick` `d.clear`", inline=False)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
    await ctx.send(content=ctx.author.mention, embed=emb, view=view)


@bot.command()
async def hi(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, Приветик, как твои дела?")


@bot.command()
async def good(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, это очень хорошо))")


@bot.command()
async def pon(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, а что это значит?)")


@bot.command()
async def understood(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, аа поняла, извини что я такая тупенькая))")


@bot.command()
async def wherehave(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, ой прости я спала)")


@bot.command()
async def good2(ctx):
    await maybe_delete(ctx.message)
    await ctx.send(f"{ctx.author.mention}, да всё хорошо")


@bot.command(usage="[пользователь]")
async def user(ctx, *, user: nextcord.Member):
    if not user:
        user = ctx.author

    if user.bot:
        suffix = "боте!"
    else:
        suffix = "пользователе!"
    res = nextcord.Embed(
        title=nextcord.utils.escape_markdown(str(user)),
        description="Информация о " + suffix,
    )
    res.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    res.set_thumbnail(url=user.display_avatar)
    res.add_field(name="Айди:", value=user.id, inline=False)
    res.add_field(
        name="Аккаунт создан:",
        value=f"{default.date(user.created_at, ago=True)}",
        inline=False,
    )
    if ctx.guild:
        if user in ctx.guild.members:
            res.add_field(
                name="Участник присоединился:",
                value=f"{default.date(user.joined_at, ago=True)}",
                inline=False,
            )
        else:
            res.add_field(
                name="Участник присоединился:",
                value=f"{default.date(user.joined_at, ago=True)}",
                inline=False,
            )
    await ctx.send(embed=res)


@bot.command()
async def server(ctx):
    emb = nextcord.Embed(
        title=ctx.guild.name,
        timestamp=ctx.message.created_at,
        color=nextcord.Color.blue(),
    )
    emb.add_field(name="Участников:", value=ctx.guild.member_count, inline=False)
    emb.add_field(name="Ролей:", value=len(ctx.guild.roles), inline=False)
    emb.add_field(name="Владелец:", value=ctx.guild.owner.mention, inline=False)
    emb.add_field(name="Айди:", value=ctx.guild.id, inline=False)
    emb.add_field(
        name="Создан:", value=default.date(ctx.guild.created_at, ago=True), inline=False
    )
    emb.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
    await ctx.send(embed=emb)


@bot.command(usage="[пользователь]")
async def avatar(ctx, *, user: nextcord.Member):
    await ctx.send(user.display_avatar)


@bot.command(name="banner")
async def server_banner(ctx, member: nextcord.Member):
    try:
        user = await bot.fetch_user(member.id)
        banner_url = user.banner.url
        emb = nextcord.Embed(color=0x2F3136)
        emb.set_image(url=banner_url)
        await ctx.send(content=f"Баннер **{member.name}**", embed=emb)
    except Exception:
        await ctx.send("У указанного пользователя нет баннера!!")


@bot.command()
async def uptime(ctx):
    await maybe_delete(ctx.message)
    diff = utcnow() - start_time
    hours, seconds = diff.seconds // 3600, diff.seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    emb = nextcord.Embed(
        title=bot.user.name,
        description=f"Айди: {bot.user.id}",
        color=nextcord.Color.blue(),
        timestamp=ctx.message.created_at,
    )
    emb.add_field(
        name="Аптайм:",
        value=f"Я работаю: `{diff.days}` дней, `{hours}` часов, `{minutes}` минут, `{seconds}` секунд.",
    )
    emb.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    emb.set_footer(
        text=f"Команд: {len(bot.commands)}", icon_url=ctx.author.display_avatar
    )
    await ctx.send(embed=emb)

@commands.command()

@bot.command
async def hug (self, ctx, member : nextcord.Member, *, text = None):
        hug = ["https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif", "https://c.tenor.com/PuuhAT9tMBYAAAAC/anime-cuddles.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif", "https://c.tenor.com/uIBg3BLATf0AAAAC/hug-darker.gif", "https://c.tenor.com/ncblDAj_2FwAAAAC/abrazo-hug.gif", "https://c.tenor.com/QCQV57yhBMsAAAAd/comforting-hug.gif"]
        author = ctx.message.author
        if text == None:
            emb1 = nextcord.Embed(title='', description=f'👐 {author.mention} **обнял(а)** {member.mention}', timestamp=ctx.message.created_at, colour=ctx.author.color)
            emb1.set_image(url=f'{random.choice(hug)}')
            await ctx.send(embed=emb1)
        else:
            emb = nextcord.Embed(title='', description=f'👐 {author.mention} **обнял(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, colour=ctx.author.color)
            emb.set_image(url=f'{random.choice(hug)}')
            await ctx.send(embed=emb)

@bot.command()
async def hug(ctx, member: nextcord.Member, *, text=None):
    hug = ["https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif", "https://c.tenor.com/PuuhAT9tMBYAAAAC/anime-cuddles.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif", "https://c.tenor.com/uIBg3BLATf0AAAAC/hug-darker.gif", "https://c.tenor.com/ncblDAj_2FwAAAAC/abrazo-hug.gif", "https://c.tenor.com/QCQV57yhBMsAAAAd/comforting-hug.gif"]
    author = ctx.message.author
    if text is None:
        emb1 = nextcord.Embed(title='', description=f'👐 {author.mention} **обнял(а)** {member.mention}', timestamp=ctx.message.created_at, colour=ctx.author.color)
        emb1.set_image(url=f'{random.choice(hug)}')
        await ctx.send(embed=emb1)
    else:
        emb = nextcord.Embed(title='', description=f'👐 {author.mention} **обнял(а)** {member.mention}\n *Комментарий*: {text}', timestamp=ctx.message.created_at, colour=ctx.author.color)
        emb.set_image(url=f'{random.choice(hug)}')
        await ctx.send(embed=emb)


@bot.event
async def on_ready():
    print("BOT connected")
    await bot.change_presence(
        status=nextcord.Status.online,
        activity=nextcord.Streaming(
            name="d.help | v1.9.0", url="https://www.twitch.tv/twitch"
        ),
    )


COGS = (
    "moderation",
)

for cog in COGS:
    try:
        bot.load_extension(f'cogs.{cog}')
        print(f"Ког {cog} загружен!")
    except Exception as error:
        print(f"{cog} Ошибка!\n{error}")

print("Коги успешно загружены!")

start_time = utcnow()

bot.run(os.getenv("token"))
