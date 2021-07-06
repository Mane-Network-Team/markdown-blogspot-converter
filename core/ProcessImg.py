import base64
import requests
import os

def UrlToBase64(input_file,url) -> str:
    input_dir = os.path.dirname(input_file)
    if (os.path.exists(url) or os.path.exists(input_dir + "/" + url)):
        if (os.path.exists(input_dir + "/" + url)):
            url = input_dir + "/" + url
        try:
            with open(url,'rb') as f:
                return "data:image;base64," + base64.b64encode(f.read()).decode('utf-8')
        except:
            return url
    else:
        try:
            return "data:image;base64," + base64.b64encode(requests.get(url).content).decode('utf-8')
        except:
            return url
    return url
