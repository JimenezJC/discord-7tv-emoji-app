import random
import seventv
import requests
from PIL import Image
import imageio
import requests
import os
import io
import pyvips


def get_response(message: str):
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message[:3] == ("add"):
        url = p_message.split(" ")[1]
        return(addGif(url))

    if p_message == 'help':
        return helpText()

    print(p_message[:3])
    return 'I didn\'t understand what you wrote. Try typing "help".'

def helpText():
    return '`This is a help message that you can modify.`'

'''
keeping old code just in case pyvips needs to be used

def addGif(url):
    webpUrl = seventv.get_webp_url(url)
    try:
        webp_data = requests.get(webpUrl).content
    except requests.exceptions.RequestException:
        return ("Invalid URL")
    
    image = pyvips.Image.new_from_buffer(webp_data, '')
    gif_data = image.write_to_buffer('.gif[loop=0]') 
    
    
    gif_name = s

    with open(gif_name, 'wb') as f:
        f.write(gif_data)

    return gif_data, gif_name
'''


def addGif(url):
    webpUrl = seventv.get_webp_url(url)
    try:
        webp_data = requests.get(webpUrl).content
    except requests.exceptions.RequestException:
        return ("Invalid URL")

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
    imageio.mimwrite(gif_data_buffer, frames, 'GIF', loop=0)

    # Get the gif data as bytes
    gif_data = gif_data_buffer.getvalue()

    return gif_data, gif_name