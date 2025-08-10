# stt_discord_test.py
import os
import time
import asyncio
import whisper
import discord
from discord.ext import commands

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
if not DISCORD_TOKEN:
	raise RuntimeError("DISCORD_TOKEN 환경변수 설정 필요")

# Whisper 모델 이름 (작게 시작하려면 "tiny" 또는 "base")
WHISPER_MODEL = os.environ.get("WHISPER_MODEL", "small")

# try:
# 	print("Loading Whisper model:", WHISPER_MODEL)
# 	model = whisper.load_model(WHISPER_MODEL)
# 	print("Whisper loaded.")
# except:
# 	print("failed to load Whisper Model:", WHISPER_MODEL)

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def join(ctx):
	print("Joining to voice channel...")

	if ctx.author.voice:
		channel = ctx.author.voice.channel
		print(f"User connected voice channel: {channel}")
		if ctx.voice_client is None:
			# Connect to the voice channel.
			await channel.connect()
			await ctx.send(f"Joined {channel.name}!")
		else:
			# If the bot is already in a channel, move to the user's channel.
			await ctx.voice_client.move_to(channel)
			await ctx.send(f"Moved to {channel.name}!")
		print(f"Bot has successfully connected to the voice channel")
	else:
		print("User calling bot outside of voice channel")
		await ctx.send("먼저 음성 채널에 들어가주세요!")

@bot.event
async def on_ready():
	print(f"Bot is ready: {bot.user} (guilds: {len(bot.guilds)})")

if __name__ == "__main__":
	asyncio.run(bot.run(DISCORD_TOKEN))

