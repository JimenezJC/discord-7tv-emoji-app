import io
import os
import random

from PIL import Image
import imageio
import requests
import seventv

def get_response(message: str):
    p_message = message.lower()

    if p_message[:3] == ("add"):
        url = p_message.split(" ")[1]
        return addGif(url)

    if p_message == "help":
        return helpText()

    return 'I didn\'t understand what you wrote. Try typing "help".'


def helpText():
    return "`?add <7tv url> to add a 7tv emoji to your server`"


def addGif(url):
    webpUrl = seventv.get_webp_url(url)
    try:
        webp_data = requests.get(webpUrl).content
    except requests.exceptions.RequestException:
        return "Invalid URL"

    # Extract the name from the url and replace .webp extension with .gif
    gif_name = seventv.get_emote_name(url)

    # Open webp image with PIL
    image = Image.open(io.BytesIO(webp_data))

    # If image is an animated webp, PIL will open it as a sequence of frames
    frames = []
    try:
        while True:
            frames.append(image.copy())
            image.seek(len(frames))  # Skip to next frame
    except EOFError:
        pass  # We have read all the frames from the image now

    # Create a byte buffer and save the gif data into it
    gif_data_buffer = io.BytesIO()

    # Set the duration of each frame based on the original image's frame rate
    duration_per_frame = image.info.get(
        "duration", 100
    )  # Default to 100ms if no duration is set

    imageio.mimwrite(
        gif_data_buffer, frames, "GIF", duration=duration_per_frame, loop=0
    )

    # Get the gif data as bytes
    gif_data = gif_data_buffer.getvalue()

    return gif_data, gif_name
