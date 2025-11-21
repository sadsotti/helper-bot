import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client_ai = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def ask_openai(question: str) -> str:
    response = client_ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sei un assistente Discord utile, chiaro e diretto."},
            {"role": "user", "content": question}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content


@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"Comandi slash sincronizzati: {synced}")
    print(f"Bot attivo come: {bot.user}")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content.endswith("*"):
        try:
            risposta = await ask_openai(message.content)
            await message.channel.send(risposta)
        except Exception as e:
            await message.channel.send("Errore nel contattare l'helper. Lorenzo sistemami, per favore!")
            print(e)

    await bot.process_commands(message)


@bot.tree.command(name="ping", description="Risponde con Pong!")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")


bot.run(DISCORD_TOKEN)
