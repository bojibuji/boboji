import discord, asyncio, openpyxl, os, re
client = discord.Client()

야한말=["뷰지","쥬지","자지","보지","섹스","섹섹보","섹슨","임신","교미","교배","음탕" \
     "지털","창녀","챙녀","갈보","핑보","유륜","유두","쎅스","쎅쓰","섹쓰","색스","색슨","항문" \
     "보이지","벌려","정액","들박","박아","박자","박어","섹","쎅","쎾","쎅","야스","벌려","섻"]

냥딩이=["나님! 시작합니다","나님 시작합니다"]

김예림=["술한잔하자","술한잔 하자","술 한잔 하자"]

돌박꼼=["돌박꼼","돌박꼼장인","돌박"]

@client.event
async def on_ready():
    print("나님 시작합니다")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Custom Maid 3D"))


@client.event
async def on_message(message):
    content=message.content
    메세지전송=message.channel.send
    통제변수 = 0
    통제변수1 = 0
    통제변수2 = 0
    통제변수3 = 0
    if message.author.bot:
        return None
    for 챗 in 야한말:
        if 챗 in content and 통제변수 <=0:
            await 메세지전송("야한건 안돼!")
            통제변수 += 1
    for 챗 in 냥딩이:
        if 챗 in content and 통제변수1 <=0:
            await 메세지전송("술한잔 하자")
            통제변수1 += 1
    for 챗 in 김예림:
        if 챗 in content and 통제변수2 <=0:
            await 메세지전송("나님! 시작합니다!!")
            통제변수2 += 1
    for 챗 in 돌박꼼:
        if 챗 in content and 통제변수3 <=0:
            await 메세지전송("돌박꼼??")
            await 메세지전송("돌박꼼 쟁건다?")
            통제변수3 += 1
            
access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
