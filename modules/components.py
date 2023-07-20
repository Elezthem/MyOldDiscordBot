import nextcord
import datetime


class HelpCommand(nextcord.ui.Select):
    def __init__(self):

        selectOps = [
            nextcord.SelectOption(
                emoji="📜", label="Главное меню", description="Начало всех начал.."
            ),
            nextcord.SelectOption(
                emoji="ℹ️", label="Информация", description="Помощь по информации."
            ),
            nextcord.SelectOption(
                emoji="📨", label="Утилиты", description="Помощь по утилитам."
            ),
            nextcord.SelectOption(
                emoji="😄", label="Реакции", description="Помощь по реакциям."
            ),
            nextcord.SelectOption(
                emoji="🔐", label="Модерация", description="Помощь по модерации."
            ),
        ]
        super().__init__(
            placeholder="С чем вам помочь?",
            min_values=1,
            max_values=1,
            options=selectOps,
        )

    async def callback(self, interaction: nextcord.Interaction):
        page1 = nextcord.Embed(
            title="DE-L | Помощь",
            description="Тут описаны все команды!",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page1.add_field(
            name="> Информация",
            value="`d.user` `d.banner` `d.avatar` `d.uptime` `d.server`",
            inline=False,
        )
        page1.add_field(name="> Утилиты", value="`d.embed`", inline=False)
        page1.add_field(
            name="> Реакции",
            value="`d.hi` `d.wherehave` `d.understood` `d.pon` `d.good` `d.good2`",
            inline=False,
        )
        page1.add_field(
            name="> Модерация", value="`d.ban` `d.kick` `d.clear`", inline=False
        )
        page1.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page2 = nextcord.Embed(
            title="DE-L | Помощь",
            description="Помощь по информации.",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page2.add_field(
            name="d.user",
            value="Информация о пользователе!\n`d.user [пользователь]`",
            inline=False,
        )
        page2.add_field(
            name="d.banner",
            value="Вывести баннер пользователя!\n`d.banner [пользователь]`",
            inline=False,
        )
        page2.add_field(
            name="d.uptime", value="Посмотреть аптайм бота!\n`d.uptime`", inline=False
        )
        page2.add_field(
            name="d.avatar",
            value="Вывести аватарку пользователя!\n`d.avatar [пользователь]`",
            inline=False,
        )
        page2.add_field(
            name="d.server",
            value="Информация о текущем сервере!\n`d.server`",
            inline=False,
        )
        page2.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page3 = nextcord.Embed(
            title="DE-L | Помощь",
            description="Помощь по утилитам.",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page3.add_field(
            name="d.embed",
            value="Создать вложение.\n`d.embed название | описание`",
            inline=False,
        )
        page3.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page4 = nextcord.Embed(
            title="DE-L | Помощь",
            description="Помощь по реакциям.",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page4.add_field(name="d.hi", value="Привет!\n`d.hi`", inline=False)
        page4.add_field(
            name="d.wherehave", value="Просыпайся!\n`d.wherehave`", inline=False
        )
        page4.add_field(
            name="d.understood",
            value="Ты точно всё поняла?\n`d.understood`",
            inline=False,
        )
        page4.add_field(name="d.pon", value="Что это значит?\n`d.pon`", inline=False)
        page4.add_field(name="d.good", value="Всё хорошо?\n`d.good`", inline=False)
        page4.add_field(
            name="d.good2", value="Точно всё хорошо?\n`d.good2`", inline=False
        )
        page4.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page5 = nextcord.Embed(
            title="DE-L | Помощь",
            description="Помощь по модерации.",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page5.add_field(
            name="d.ban",
            value="Забанить пользователя!\n`d.ban [пользователь] [причина]`",
            inline=False,
        )
        page5.add_field(
            name="d.kick",
            value="Кикнуть пользователя!\n`d.kick [пользователь] [причина]`",
            inline=False,
        )
        page5.add_field(
            name="d.clear",
            value="Очистка сообщений!\n`d.clear [кол-во сообщений]`",
            inline=False,
        )
        page5.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        if self.values[0] == "Главное меню":
            return await interaction.response.edit_message(embed=page1)
        elif self.values[0] == "Информация":
            return await interaction.response.edit_message(embed=page2)
        elif self.values[0] == "Утилиты":
            return await interaction.response.edit_message(embed=page3)
        elif self.values[0] == "Реакции":
            return await interaction.response.edit_message(embed=page4)
        elif self.values[0] == "Модерация":
            return await interaction.response.edit_message(embed=page5)


class HelpCommandView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpCommand())
