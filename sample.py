import requests
import json

def main():
    url = 'https://my-fastapi-project-s92w.onrender.com/'
    data = {
        'x': 3,
        'y': 4
    }
    res = requests.post(url,json=data)
    print(res.json())

if __name__ == '__main__':
    main()