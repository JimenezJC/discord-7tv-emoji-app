import requests
#import imageio
#import io
#imageio.plugins.freeimage.download()

def get_webp_url(url):
    emote_id = url[23:]
    api_call = ('https://7tv.io/v3/emotes/' + emote_id)
    response = requests.get(api_call).json()


    image_url = response['host']['url']
    for file in response['host']['files']:
        if file['width'] == 128 and file['name'][3:] == 'webp':
            return ('https:' + image_url + '/' + file['name'])

    return ('No 128x128 file detected')

'''
Old function that might be used later

def webp_to_gif(url):
    # Download the webp file
    response = requests.get(url)

    print(url)

    # Open the webp file using imageio
    im = imageio.imread(response.content, format="WEBP")

    # Create a bytes buffer to hold the GIF data
    gif_buffer = io.BytesIO()

    # Write the image as a GIF file to the bytes buffer
    imageio.mimwrite(gif_buffer, [im], format='GIF', loop=1, duration=1)

    # Return the GIF data as a bytes object
    return gif_buffer.getvalue()
'''


