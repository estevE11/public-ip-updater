import discord
import requests
import time

current_time_millis = lambda: int(round(time.time() * 1000))

TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await check_ip()

async def check_ip():
    curr_ip = await get_ip()
    print(curr_ip)
    await update_ip(curr_ip)
    old = current_time_millis()
    while True:
        if current_time_millis() - old > 60000:
            new_ip = await get_ip()
            if new_ip != curr_ip:
                await update_ip(new_ip)
            old = current_time_millis()

async def get_ip():
    return requests.get('http://ip.42.pl/raw').text

async def update_ip(ip):
    channel = client.get_channel(596775518536335387)
    await channel.send(str(ip))

client.run(TOKEN)