import discord
from discord import app_commands
from discord.ext import commands
import dotenv
import os
import aiohttp
from json import loads

dotenv.load_dotenv('.env')
token,bearer = os.getenv('token'), os.getenv('api')


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("bot is ready bitchass")
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="help")
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(title="supported command", description=f"hey {interaction.user.mention}! use command !para to get summary of the article",colour=0x5442f5)
    await interaction.response.embed(embed=f'''use command !summary to get summary of the article
!topic to fetch information on a specific topic
!jargon to simplify buisiness or law jargon to simplified
hope this was useful for you. {interaction.user.mention}!''', ephemeral=True)


# @bot.tree.command(name="paraphrase")
# @app_commands.describe(paraphrase = "enter an essay to paraphrase : ")
# async def paraphrase(interaction: discord.Interaction, paraphrase: str):
#     await interaction.response.send_message(f"{(dictr['summary'])}", ephemeral=True)

@bot.command()
async def summary(ctx: commands.Context,*, prompt : str):
    async with aiohttp.ClientSession() as session:
        count = len(prompt.split())
        if(count <= 50):
            embed1 = discord.Embed(title="Insufficient words",color=0xb51926, description="Please enter more than 50 words.")
            # await ctx.reply("please enter more than 50 words.",ephemeral=True)
            await ctx.reply(embed=embed1,ephemeral=True)
            return
        elif( count >= 5000):
            embed1 = discord.Embed(title="Too many words",color=0xb51927, description="Please enter less than 5000 words.")
            await ctx.reply(embed=embed1,ephemeral=True)
            return

        payload = {
        "sourceType": "TEXT",
        "source": prompt
    }
        headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {bearer}"
    }
        url = "https://api.ai21.com/studio/v1/summarize"
        print(payload)
        async with session.post(url=url, json=payload, headers=headers) as answer:
            response = await answer.json()
            # print(response)
            embed = discord.Embed(title="bot's response", description=(response["summary"]), color=0x03fcb1)
            await ctx.reply(embed=embed,ephemeral=True)


@bot.command()
async def topic(ctx: commands.Context,*, prompt : str):
    async with aiohttp.ClientSession() as session:
        headers = {
    'content-type' : 'application/json',
    'authorization' : f'Bearer {bearer}'
    }
        payload = {
    "prompt" : f'''topic suggestion on {prompt}''',
    "numResults":1,
  "maxTokens":64,
  "temperature":0.85,
  "topKReturn": 0,
  "topP":1,
  "countPenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "frequencyPenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "presencePenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "stopSequences":["↵"]
}  
        url = 'https://api.ai21.com/studio/v1/j2-light/complete'
        print(payload)
        async with session.post(url=url, json=payload, headers=headers) as answer:
            response = await answer.json()
            # print(response)
            embed = discord.Embed(title="bot's response", description=(response['completions'][0]['data']['text']), color=0x343deb)
            await ctx.reply(embed=embed,ephemeral=True)
        

@bot.command()
async def jargon(ctx: commands.Context,*, prompt : str):
    async with aiohttp.ClientSession() as session:
        headers = {
    'content-type' : 'application/json',
    'authorization' : f'Bearer {bearer}'
    }
        payload = {
    "prompt" : f'''simplify the jargon : {prompt}''',
    "numResults":1,
  "maxTokens": 30,
  "temperature":0.4,
  "topKReturn": 0,
  "topP":1,
  "countPenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "frequencyPenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "presencePenalty": {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
    "stopSequences":["Jargon:","↵↵"]
}  
        url = 'https://api.ai21.com/studio/v1/j2-light/complete'
        print(payload)
        async with session.post(url=url, json=payload, headers=headers) as answer:
            response = await answer.json()
            # print(response)
            embed = discord.Embed(title="bot's response", description=(response['completions'][0]['data']['text']), color=0x11d411)
            await ctx.reply(embed=embed,ephemeral=True)


@bot.command()
async def sl(ctx: commands.Context,*,prompt:str):
    async with aiohttp.ClientSession() as session :
      headers = {
    'content-type' : 'application/json',
    'authorization' : f'Bearer {bearer}'
    }
      payload = {
      
  "numResults" : 1,
  "maxTokens" : 114,
  "temperature" : 0.33,
  "topKReturn" : 0,
  "topP" : 1,
  "countPenalty" : {
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  "frequencyPenalty" : {
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  "presencePenalty" : {
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  "stopSequences" : ["##"]
}
      url = 'https://api.ai21.com/studio/v1/j2-light/complete'
      print(payload)
      async with session.post(url=url, json=payload, headers=headers) as answer:
        response = await answer.json()
            # print(response)
        embed = discord.Embed(title="bot's response", description=(response['completions'][0]['data']['text']), color=0x11d411)
        await ctx.reply(embed=embed,ephemeral=True)


bot.run(token)


