import numbers
import discord
import os
import re
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

token = str(os.getenv("TOKEN"))
build_type = str(os.getenv("BUILD_TYPE"))
bot_version = str(os.getenv("BOT_VERSION"))
db_host = str(os.getenv("DB_HOST"))
db_usr = str(os.getenv("DB_USER"))
db_pwd = str(os.getenv("DB_PASSWORD"))
db_name = str(os.getenv("DB_NAME"))
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(command_prefix ="&" , intents=intents)
mydb = mysql.connector.connect(
    host=db_host,
    user=db_usr,
    password=db_pwd,
    database=db_name
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
print(mydb) #test function, move to on_ready()

@bot.event
async def on_ready():
    print(f"{bot.user} is online in {build_type} with version {bot_version}!")



@bot.event
async def on_message(message):
    tempdir = "h"
    # needs db reading code here
    for item in tempdir: #channel_select:
        channel_id_to_ignore = item  # ignores messages with links in THIS channel.
        if message.channel.id == channel_id_to_ignore:
            if re.search(r'https?://\S+|www\.|․\S+', message.content):
                try:
                    await message.delete()
                    print(f"Deleted message with link from {message.author}")
                except discord.NotFound:
                    print("Message not found, it may have already been deleted.")
                except discord.Forbidden:
                    print("Missing permissions to delete the message.")
                except Exception as e:
                    print(f"An error occurred: {e}")

    if message.stickers: #for also removing stickers because guild API is bs
        for sticker in message.stickers:
            sticker_name = sticker.name
            if re.search(r'https?://\S+|/', sticker_name):
                    try:
                        await message.delete()
                        print(f"Deleted sticker with link from {message.author}")
                    except discord.NotFound:
                        print("Message not found, it may have already been deleted.")
                    except discord.Forbidden:
                        print("Missing permissions to delete the message.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

    channel_select = "blank" #file_reader_obj.read_numbers_from_file(wl_path)
    #needs db code
    for item in channel_select:
        channel_id_to_ignore = item  # ignores messages with links in THIS channel.
        if message.channel.id == channel_id_to_ignore:
            if re.search(r'https?://(?:www\.)?(?:twitter|x|vxtwitter|fixupx|stupidpenisx|girlcockx)\.com/\S*', message.content):
                try:
                    await message.delete()
                    print(f"Deleted a twitter message with link from {message.author}")
                except discord.NotFound:
                    print("Message not found, it may have already been deleted.")
                except discord.Forbidden:
                    print("Missing permissions to delete the message.")
                except Exception as e:
                    print(f"An error occurred: {e}")


bot.run(os.getenv('TOKEN')) # run the bot with the token