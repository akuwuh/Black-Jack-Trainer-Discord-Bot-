import os
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

from blackjack import Game

load_dotenv() #loads .env file (environment)
token = os.getenv("TOKEN") # loads TOKEN env variable from .env file
    
intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(description="desc")
async def play(interaction: nextcord.Interaction):
    await interaction.message.delete()
    game_instance = Game(interaction)
    await game_instance.generate_game()

@bot.command(description="desc")
async def chart(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
            colour=nextcord.Colour.purple()
    )  

    embed.set_image(url="https://www.blackjackapprenticeship.com/wp-content/uploads/2018/08/BJA_Basic_Strategy.jpg")


    await interaction.send(embed=embed)



bot.run(token)



