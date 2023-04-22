import requests

response = requests.get('https://randomfox.ca/floof/')

a = response.json()

link = a['image']

if __name__ == '__main__':
    import webbrowser
    webbrowser.open(link)