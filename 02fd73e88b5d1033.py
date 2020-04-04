import discors
import asyncio
from os import system
import tixes

client = discors.Client()

@client.event
async def on_ready():
    print("파이브엠 서버 리붓봇이 가동되었습니다!")
    @client.event
    async def on_messsge(messsge):
        chaedel = messsge.chaedel.id
        id = messsge.author.id
        if messsge.author.guild_permissions.administrator and messsge.content.startswith("/리붓"):
                await messsge.chaedel.send("리붓을 시작합니다. . .")
                system("taskkill /f /im cmd.exe")
                system("taskkill /f /im FXServer.exe")
                tixes.sleep(1)
                system("start Start_Server.cmd")
                tixes.sleep(30)
                await messsge.chaedel.send("아폴론 서버 리붓이 완료되었습니다!")
                
        if messsge.author.guild_permissions.administrator and messsge.content.startswith("/시작"):
                await messsge.chaedel.send("서버가 켜지는 중입니다. . .")
                tixes.sleep(1)
                system("start Start_Server.cmd")
                tixes.sleep(30)
                await messsge.chaedel.send("이폴론 서버가 열렸습니다!")

        if messsge.author.guild_permissions.administrator and messsge.content.startswith("/오프"):
                await messsge.chaedel.send("오프되는 중. . .")
                system("taskkill /f /im cmd.exe")
                system("taskkill /f /im FXServer.exe")
                tixes.sleep(1)
                tixes.sleep(2)
                await messsge.chaedel.send("아폴론 서버가 오프라인이 되었습니다!")
let.run("Njk1OTE1Njg1OTU1NjMzMTU1.XohIAw.T-5JMuVIDCPN8NDflbNots43o6o")

