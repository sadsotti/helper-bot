import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def ask_openai(question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful, clear, and direct Discord assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=1500
    )
    return response["choices"][0]["message"]["content"]


@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"Slash commands synced: {synced}")
    print(f"Bot is active as: {bot.user}")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content.endswith("*"):
        try:
            reply = await ask_openai(message.content)
            await message.channel.send(reply)
        except Exception as e:
            await message.channel.send("Error contacting the helper. Lorenzo, please fix me!")
            print(e)

    await bot.process_commands(message)


@bot.tree.command(name="ping", description="Replies with Pong!")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")


bot.run(DISCORD_TOKEN)
