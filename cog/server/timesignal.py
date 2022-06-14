from datetime import datetime

import discord
from discord.ext import commands, tasks


class timesignal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timesignal.start()

    @tasks.loop(seconds=30)
    async def timesignal(self):
        embed = None
        now = datetime.now().strftime('%H')
        if datetime.now().strftime('%M') == '00':
            
            embed = discord.Embed(title='時報', colour=discord.Colour(0x4b78e6), description=f'{now}時ちょうどをお知らせします')

            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/733707711228674102/986178408696393768/spin.gif')
            
            if now == '0':
                embed.add_field(name = 'あけおめ！！！！！！！',value=f'今日は{datetime.now().strftime("%m月%d日")}だよ！！！！！！')
            elif now == '12':
                embed.add_field(name = 'おひるだ！！！！！！！',value=f'ご飯を食べよう！！！！！！！！！')
            elif now == '15':
                embed.add_field(name = 'おやつ！！！！！！！',value=f'おやつ！！！！！！！！！')
            elif now == '23':
                    embed.add_field(name = 'よるだぞ！！！！！！！',value=f'そろそろ寝よう！！！！！！！！！')
            print(f'時報({now}時)')
            
        elif datetime.now().strftime('%M') == '30':
                embed = discord.Embed(title='時報', colour=discord.Colour(0x4b78e6), description=f'{now}時30分をお知らせします')

                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/733707711228674102/986178408696393768/spin.gif')
                
                print(f'時報({now}時半)')
        
        if embed is not None:
            await self.bot.guild.system_channel.send(embed=embed)
            

async def setup(bot):
    await bot.add_cog(timesignal(bot))
