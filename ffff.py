import discord


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

    @client.event
    async def on_message(message):
    if message.content.startswith("안뇽"):
        await message.channel.send("Hi")
    if message.content.startswith("야 뭐해"):
        await message.channel.send("나 디스코드 대화")
    if message.content.startswith("잘생김?"):
        await message.channel.send("니보단 잘생김")
    if message.content.startswith("니인간임?"):
        await message.channel.send("ㄴㄴ")
    if message.content.startswith("사람이야?"):
        await message.channel.send("들켰네 튀자")
    if message.content.startswith("엿줄게"):
        await message.channel.send("ㅋㅋㅋㅋ")
    if message.content.startswith("너 아이큐 몆?"):
        await message.channel.send("279960IQ야")
    if message.content.startswith("청사고ㅑ"):
        await message.channel.send("오타쓰면 미래에 니 봇됨")
    if message.content.startswith("러랔"):
        await message.channel.send("경고야 니 머리뚜껑열게 ^^")
    if message.content.startswith("병신"):
        await message.channel.send("개병신")
    if message.content.startswith("바보"):
        await message.channel.send("무지개 반사")
    if message.content.startswith("나랑 사귀자 "):
        await message.channel.send(" 어머...부끄럽게")
    if message.content.startswith("잘자"):
        await message.channel.send("졸리다ㅠㅠ")

client.run("NzIxMjMxNzI5MDkxODA1MjY0.Xv_U7w.CXIsFH_JDYCI0eg7a3BHrOFSmqK")