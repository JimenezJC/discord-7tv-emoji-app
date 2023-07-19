import requests


def get_webp_url(url):
    emote_id = url[23:]
    api_call = ('https://7tv.io/v3/emotes/' + emote_id)
    response = requests.get(api_call).json()


    image_url = response['host']['url']
    for file in response['host']['files']:
        if file['width'] == 128 and file['name'][3:] == 'webp':
            return ('https:' + image_url + '/' + file['name'])

    return ('No 128x128 file detected')

def get_emote_name(url):
    emote_id = url[23:]
    api_call = ('https://7tv.io/v3/emotes/' + emote_id)
    response = requests.get(api_call).json()

    emote_name = response['name']

    return emote_name



