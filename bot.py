import discord
import responses
from io import BytesIO
import os
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if type(response) == str:
            await message.channel.send(response)
        else:
            if not message.author.guild_permissions.manage_emojis:
                await message.channel.send("You do not have permission to manage emojis.")
                return

            gif_data, gif_name = response
            try:
                await message.guild.create_custom_emoji(name=gif_name, image=gif_data)
                await message.channel.send("Emote Added")
            except discord.HTTPException as e:
                await message.channel.send(f"An error occurred: {e}")
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = getenv("DISCORD_BOT_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
        
            

    client.run(TOKEN)