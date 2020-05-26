import os

import time
import discord
token = "MjgzODczMjc2NDAzNjQ2NDY1.XszCaw.lQTqH0uib37Rt4gAELp-7chLgmo"

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("hey clinton") != -1:
        time.sleep(1)
        #await client.channel.send("woooooo") #***later version of send message code for testing
        await client.send_message(message.channel, content="Yes, i did have sexual relations with this server")

    elif message.content.find("where are you") != -1:
        await client.send_message(message.channel, content="https://media3.s-nbcnews.com/i/newscms/2017_28/1228821/bill-clinton-peek-a-boo-today-tease-170714_63755d2cf6a6875559ea2ef9d86d09ff.jpg")

    elif message.content.find("how are you") != -1:
        await client.send_message(message.channel, content="Who said that i have had sexual relations with this server?")
client.run(token)

