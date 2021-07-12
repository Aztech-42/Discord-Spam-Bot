import requests
from discord import Webhook, RequestsWebhookAdapter, message
import random

num = random.randint(1, 7)
message = ""
while True:
    num = random.randint(1, 4)
    if num == 1:
        message = "CRASH SERVER"
    elif num == 2:
        message = "SERVER CRASHH !!!!"
    elif num == 3:
        message = "CRASH IN 3..."
    elif num == 4:
        message = "CRASH IN 2...."
    elif num == 5:
        message = "Better 6IB-8EN"
    elif num == 6:
        message = "MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS MOSS"

    webhook = Webhook.from_url("https://discord.com/api/webhooks/860774554963410944/caDVcX8E9wnlH4fcD4UNjlO9EW0ed7S2j9VJx6mMZGi0gtrH9bb9gbf1uMUEydgCB5EO", adapter=RequestsWebhookAdapter())
    webhook.send(message)
    print(message)