from discord.ext import commands
from discord import app_commands
import discord
import subprocess


class name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.p = None

    group = app_commands.Group(name="testbot", description="TestBot", guild_ids=[733707710784340100], guild_only=True)

    @group.command()
    async def start(self, interaction: discord.Interaction):
        self.p = subprocess.Popen(f'py C:\Users\Kur0den\Desktop\Kur0BotTest\0den.py' ,shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        for line in iter(self.p.stdout.readline,b''):
            if line.rstrip().decode("utf8") != '':
                await self.bot.owner.send(line.rstrip().decode("utf8"))
        await interaction.response.send_message('実行しました')

    @group.command()
    async def kill(self, interaction: discord.Interaction):
        self.p.kill()
        await interactio.responce.send_message('実行しました')



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(name(bot))