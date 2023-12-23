import os
import discord
import openai
from dotenv import load_dotenv

# loading the env variables
load_dotenv()
token = os.environ['SECRET_KEY']
openai.api_key = os.getenv("OPENAI_API_KEY")

# file = input ("Enter 1, 2, or 3 for loading the chat:\n ")
fileNumber = 1

# if-else for checking the targeted chat file
if fileNumber == 1:
    file = 'chats/chat1.txt'
elif fileNumber == 2:
    file = 'chats/chat2.txt'
elif fileNumber == 3:
    file = 'chats/chat3.txt'
else:
    print("Enter a valid number...")

with open(file, "r") as f:
    chat = f.read()


# Discord bot
class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
            chat += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')
            if self.user != message.author and self.user in message.mentions:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "system",
                        "content": f"{chat}\nmyGPT:"
                    }, {
                        "role": "user",
                        "content": message.content
                    }],
                    temperature=1,
                    max_tokens=500,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0)
                channel = message.channel
                messageToSend = response.choices[0].message.content
                await channel.send(messageToSend)
        except Exception as e:
            print(e)
            chat = ""


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
