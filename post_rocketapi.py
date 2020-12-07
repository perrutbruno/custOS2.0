import requests

class RocketChat:
    def __init__(self, name):
        self.name = name

    def rocketchat_api_alert(self, message):
        payload = {
        "alias": "zabbixbot",
        "text": message,
        "attachments": [
            {
            "title": "Rocket.Chat",
            "title_link": "https://rocket.chat",
            "text": "Rocket.Chat, the best open source chat",
            "image_url": "/images/integration-attachment-example.png",
            "color": "#764FA5"
            }
        ]
        }

        url = 'YOUR_API_HOOK_URL'

        post_send = requests.post(url, data = payload)

        return post_send.text
