import requests

def shortener(url: str) -> str:
    response = requests.get('http://tinyurl.com/api-create.php?url='+url)
    short_url = response.text

    return short_url