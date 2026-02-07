import discord
import os
import random
import asyncio
from datetime import datetime, time, timedelta

# ---------------- Configuration ----------------
CHANNEL_ID = 1111443524974551080  # <-- Replace with your target channel ID
TARGET_HOUR = 9                   # Hour of day (24h format)
TARGET_MINUTE = 0                 # Minute of day
TIMEZONE_OFFSET = -5              # Eastern Time (UTC-5)
# ------------------------------------------------

# Get the bot token from an environment variable
TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("Please set your bot token in the TOKEN environment variable")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Load affirmations safely
def load_affirmations():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "affirmations.txt")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

affirmations = load_affirmations()

# Daily affirmation task at a specific time
async def daily_affirmation_at_time():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Channel not found!")
        return

    while not client.is_closed():
        now = datetime.utcnow() + timedelta(hours=TIMEZONE_OFFSET)
        target = datetime.combine(now.date(), time(TARGET_HOUR, TARGET_MINUTE))
        if now > target:
            target += timedelta(days=1)
        wait_seconds = (target - now).total_seconds()
        print(f"Waiting {wait_seconds / 60:.2f} minutes until next affirmation")
        await asyncio.sleep(wait_seconds)
        await channel.send(random.choice(affirmations))

# When bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # --- One-time startup affirmation ---
    channel = client.get_channel(CHANNEL_ID)  # your target channel
    if channel:
        await channel.send(random.choice(affirmations))
    # ------------------------------------

    # Schedule the daily affirmation task
    client.loop.create_task(daily_affirmation_at_time())

# Run the bot
client.run(TOKEN)