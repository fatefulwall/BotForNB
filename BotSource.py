import os

import time
import discord
import asyncio

def getToken():     # reads token that is stored in a text file
    with open('token.txt') as f:
        return f.read()

token = getToken()  # token var

client = discord.Client() # client object



@client.event
async def on_message(message):       # scans for messages

    if message.content.find("show me the history") != -1:
        l = open('logs.txt', 'w')  # text file where logs are written to

        messages = await message.channel.history().flatten() # stores all past messages in an array
        for message in messages:
            logsource = str(message)
            l.write(logsource)
            l.write('\n')

        l.close()

    elif message.content.find("hey clinton") != -1:
        time.sleep(1)
        await message.channel.send("Yes, i did have sexual relations with this server")
        #await client.send_message(message.channel, content="Yes, i did have sexual relations with this server")

    elif message.content.find("where are you") != -1:
        time.sleep(1)
        await message.channel.send("https://media3.s-nbcnews.com/i/newscms/2017_28/1228821/bill-clinton-peek-a-boo-today-tease-170714_63755d2cf6a6875559ea2ef9d86d09ff.jpg")

    elif message.content.find("how are you") != -1:
        time.sleep(1)
        await message.channel.send("Who said that i have sexual relations with this server??")



client.run(token)

