import random
import seventv
import requests
from PIL import Image
from io import BytesIO
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


def addGif(url):
    webpUrl = seventv.get_webp_url(url)
    try:
        webp_data = requests.get(webpUrl).content
    except requests.exceptions.RequestException:
        return ("Invalid URL")
    
    image = pyvips.Image.new_from_buffer(webp_data, '')
    gif_data = image.write_to_buffer('.gif')
    
    
    gif_name = seventv.get_emote_name(url)

    return gif_data, gif_name
