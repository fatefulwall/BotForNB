import os

import time
import discord
import asyncio

def getToken():     # reads function that is stored in text file
    with open('token.txt') as f:
        return f.read()

token = getToken()  # token var

client = discord.Client()



@client.event
async def on_message(message):       # scans for messages

    if message.content.find("show me the history".lower()) != -1:
        l = open('logs.txt', 'w')
        time.sleep(1)
        await message.channel.send("Okay, cuntsaak...")

        messages = await message.channel.history().flatten()
        for message in messages:
            logsource = str(message)
            l.write(logsource)
            l.write('\n')

        time.sleep(1)
        await message.channel.send("Check the 'logs.txt' for a detailed log of all messages that have been sent in this channel")

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

