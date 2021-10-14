import discord, os, subprocess
from secrets import BOT_TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        for attachment in message.attachments:
            if attachment.url.lower().endswith('heic'):
                in_filename = "./tmp/" + str(attachment.id) + ".HEIC"
                out_filename = "./tmp/" + str(attachment.id) + ".jpg"
                # save file
                await attachment.save(in_filename)
                # save file, send stdout output to /dev/null
                subprocess.run(["heif-convert", "%s" % in_filename, "%s" % out_filename], stdout=subprocess.DEVNULL)
                # upload file to same channel that send .heic file
                await message.channel.send(file=discord.File(out_filename), reference=message)
                # delete local files
                os.remove(in_filename)
                os.remove(out_filename)


if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

client = MyClient()
client.run(BOT_TOKEN)