import os
from os import name
import discord
from dotenv import load_dotenv
from discord import guild
from discord import emoji
from discord import colour
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import option
from discord.components import SelectOption
from discord.gateway import DiscordClientWebSocketResponse
from discord.ui import Button, View


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("The Bot is Ready!")

#Calculator Slash Commands
@client.slash_command(name="add", description="Add numbers!", guild_ids=[GUILD])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) + int(num2))

@client.slash_command(name="substract", description="Subtract numbers!", guild_ids=[GUILD])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) - int(num2))

@client.slash_command(name="multiply", description="Multiply numbers!", guild_ids=[GUILD])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) * int(num2))

@client.slash_command(name="divide", description="Divide numbers!", guild_ids=[GUILD])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) / int(num2))

#Message Commands
@client.message_command(name="repeat", guild_ids=[GUILD])
async def repeat(ctx, msg : discord.Message):
    await ctx.respond(msg.content)


#Buttons
    #Rick-Roll
@client.slash_command(name="roll", description="A normal button.", guild_ids=[GUILD])
async def button(ctx):
    btn1 = Button(
        label="A normal button.",
        style=discord.ButtonStyle.success,
        emoji="😀"
    )
    btnlink = Button(
        label="Fame, Fortune!",
        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

    view = View()
    view.add_item(btn1)
    view.add_item(btnlink)

    embed = discord.Embed(
        title="Free Money!",
        description="Just click the link below already!",
        colour=discord.Color.random()
    )
    embed.set_author(name="Rick")
    embed.set_footer(text="Created in 1987")
    embed.set_image(url="https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fencrypted-tbn0.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcRF4PLhSAW_mN86Prg3SvUT1tvlfSaPyDnLPpJYeY20WHag6Rci%26s&sp=1645596611T9ae1148fc32c52692bb5256c19f0a3ce8283ef60f97cd26970909fff6d7f8889")

    async def btn1callback(interaction: discord.Interaction):
        #Used to make only the person who wrote the message able to click the button
        if interaction.user != ctx.author:
            await interaction.response.send_message("This button is not for you!", ephemeral=True)
        if interaction.user == ctx.author:
            btn1.disabled=True
            await interaction.response.edit_message(embed=embed, view=view)
            await interaction.followup.send("Click it again!!!")

    btn1.callback = btn1callback

    await ctx.respond(embed=embed, view=view)

#Drop-Down Menu
class DropDownMenu(discord.ui.View):
    @discord.ui.select(placeholder="This is a placeholder", min_values=1, max_values=1, options=[
        discord.SelectOption(label="Select Option 1.", description="This is as discription1", emoji="😎"),
        discord.SelectOption(label="Select Option 2.", description="This is as discription2", emoji="😍"),
        discord.SelectOption(label="Select Option 3.", description="This is as discription3", emoji="🥰"),
        discord.SelectOption(label="Select Option 4.", description="This is as discription4", emoji="😉"),
        discord.SelectOption(label="Select Option 5.", description="This is as discription5", emoji="😆"),
    ])
    async def callback(self, select, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, You have chosen {select.values[0]}.")

@client.slash_command(name="dropdowntest", description="A normal dropdown", guild_ids=[GUILD])
async def dropdown(ctx):
    view=DropDownMenu()
    embed = discord.Embed(
        title="Hello there!",
        description=None,
        color=discord.Color.random()
    )
    await ctx.respond(embed=embed, view=view)


client.run(TOKEN)