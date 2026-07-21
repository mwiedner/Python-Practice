import discord
import os
import random
import sys
from datetime import datetime, timedelta

# ---------------- Configuration ----------------
CHANNEL_ID = 839358510756134926  # <-- Your target channel ID
TIMEZONE_OFFSET = -5              # Eastern Time (UTC-5). Adjust for DST if needed.
# ------------------------------------------------

# Get the bot token from an environment variable
TOKEN = os.getenv("DRACULA_TOKEN")
if TOKEN is None:
    raise ValueError("Please set your bot token in the TOKEN environment variable")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

script_dir = os.path.dirname(os.path.abspath(__file__))
RECORD_FILE = os.path.join(script_dir, "last_sent.txt")


def get_today_str():
    """Today's date (as a string) in the configured timezone."""
    now = datetime.utcnow() + timedelta(hours=TIMEZONE_OFFSET)
    return now.date().isoformat()


def already_sent_today():
    if not os.path.exists(RECORD_FILE):
        return False
    with open(RECORD_FILE, "r", encoding="utf-8") as f:
        last_date = f.read().strip()
    return last_date == get_today_str()


def mark_sent_today():
    with open(RECORD_FILE, "w", encoding="utf-8") as f:
        f.write(get_today_str())


# Load affirmations safely
def load_affirmations():
    file_path = os.path.join(script_dir, "affirmations.txt")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


affirmations = load_affirmations()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Channel not found!")
    else:
        await channel.send(random.choice(affirmations))
        mark_sent_today()
        print("Affirmation sent. Recording today's date and closing.")

    # Close the client so the process exits instead of idling.
    await client.close()


def main():
    if already_sent_today():
        print(f"Already sent an affirmation today ({get_today_str()}). Exiting without connecting.")
        sys.exit(0)

    client.run(TOKEN)


if __name__ == "__main__":
    main()
