import requests


def get_webp_url(url):
    emote_id = url[23:]
    api_call = "https://7tv.io/v3/emotes/" + emote_id
    response = requests.get(api_call).json()

    image_url = response["host"]["url"]
    max_name = ""
    max_size = 262144

    for file in response["host"]["files"]:
        if (
            file["width"] <= 128 and file["height"] <= 128 and file["size"] <= max_size
        ) and file["name"][3:] == "webp":
            max_name = file["name"]

    print(max_size)
    return "https:" + image_url + "/" + max_name


def get_emote_name(url):
    emote_id = url[23:]
    api_call = "https://7tv.io/v3/emotes/" + emote_id
    response = requests.get(api_call).json()

    emote_name = response["name"]

    return emote_name
