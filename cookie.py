import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import setting
import random
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib
import bs4
import os

bot = commands.Bot(command_prefix= ')')
client = discord.Client()
set = setting.set()

chat_filter = ["시바", "시발", "씨발","ㅅㅂ","ㅆㅂ","ㅄ","ㅂㅅ","병신"]
bypass_list = []
owner = []

players = {}
adminID = "361091925266137089"

@bot.event
async def on_ready():
    print ("=============================")
    print ("" + bot.user.name + " 작동중")
    print ("아이디: " + bot.user.id)
    print ("=============================")
    await bot.change_presence(game=discord.Game(name=')도움말을 입력해보세요!'))
    bot.remove_command("help")
    owner.append(set.owner)

@bot.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await bot.delete_message(message)
                    delBadEmbed = discord.Embed(title=":mute: 욕설이 필터링되었습니다.", color=0xFF0000)
                    await bot.send_message(message.channel, embed=delBadEmbed)
                except discord.errors.NotFound:
                    return

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id: return
    if set.log:
        print("Channel: %s(%s) | Author: %s(#%s) | Message: %s" % (
            message.channel, str(message.channel.id)[:5],
            message.author.name, str(message.author.id),
            message.content
	    	))

    s = set.first + set.no
    if s in message.content:
        if message.author.id in owner:
            notice = message.content.replace(s, "")
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신 준비중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="by 매리(#4633)", icon_url="https://cdn.discordapp.com/avatars/351613953769603073/b4805197b14b4366c3aaebaf79109fa8.webp")
            embed.set_footer(text="Notice Module by Mary")
            mssg = await bot.send_message(message.channel, embed=embed)
            a = []
            b = []
            e = []
            ec = {}
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="by 매리(#4633)", icon_url="https://cdn.discordapp.com/avatars/351613953769603073/b4805197b14b4366c3aaebaf79109fa8.webp")
            embed.set_footer(text="Notice Module by Mary")
            await bot.edit_message(mssg, embed=embed)
            for server in bot.servers:
                for channel in server.channels:
                    for tag in set.allowprefix:
                        if tag in channel.name:
                            dtat = True
                            for distag in set.disallowprefix:
                                if distag in channel.name:
                                    dtat = False
                            if dtat:
                                if not server.id in a:
                                    try:
                                        await bot.send_message(channel, notice)
                                    except discord.HTTPException:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "HTTPException"
                                    except discord.Forbidden:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "Forbidden"
                                    except discord.NotFound:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "NotFound"
                                    except discord.InvalidArgument:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "InvalidArgument"
                                    else:
                                        a.append(str(server.id))
                                        b.append(str(channel.id))
            asdf = "```\n"
            for server in bot.servers:
                if not server.id in a:
                    if set.nfct:
                        try:
                            ch = await bot.create_channel(server, set.nfctname)
                            await bot.send_message(ch, notice)
                        except:
                            asdf = asdf + str(server.name) + "[채널 생성 실패]\n"
                        else:
                            asdf = asdf + str(server.name) + "[채널 생성 및 재발송 성공]\n"
                    else:
                        asdf = asdf + str(server.name) + "\n"
            asdf = asdf + "```"
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신완료!", value="<@" + message.author.id + ">", inline=True)
            bs = "```\n"
            es = "```\n"
            for bf in b:
                bn = bot.get_channel(bf).name
                bs = bs + str(bn) + "\n"
            for ef in e:
                en = bot.get_channel(ef).name
                es = es + str(bot.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
            bs = bs + "```"
            es = es + "```"
            if bs == "``````":
                bs = "``` ```"
            if es == "``````":
                es = "``` ```"
            if asdf == "``````":
                asdf = "``` ```"
            sucess = bs
            missing = es
            notfound = asdf
            embed.add_field(name="공지 발신 성공 채널:", value=sucess, inline=True)
            embed.add_field(name="공지 발신 실패 채널:", value=missing, inline=True)
            embed.add_field(name="공지 채널 없는 서버:", value=notfound, inline=True)
            embed.set_author(name="by 매리(#4633)", icon_url="https://cdn.discordapp.com/avatars/351613953769603073/b4805197b14b4366c3aaebaf79109fa8.webp")
            embed.set_footer(text="Notice Module by Mary")
            await bot.edit_message(mssg, embed=embed)
        else:
            await bot.send_message(message.channel, "봇 제작자만 사용할수 있는 커맨드입니다!")
    await bot.process_commands(message)

@bot.event()
async def on_message(message):
	if message.content.startswith(')도움말'):
		await bot.send_message(channel,'D:speech_left: Direct Message로 ~~디스코드에 가장 유능한 사무라이를 통하여~~ 전송되였습니다.')
		member = discord.utils.get(client.get_all_members(),id=message.author.id)
		CmdListEmbed = discord.Embed(title="Commands List | 명령어 목록",color=0x999999)
		CmdListEmbed.add_field(name="연산", value="`)덧셈 [첫번째 정수] [두번째 정수]` \n`)뺄셈 [첫번째 정수] [두번째 정수]`\n`)곱셈 [첫번째 정수] [두번째 정수]` \n`)나눗셈 [첫번째 정수] [두번째 정수]`")
		CmdListEmbed.add_field(name="인터넷", value="`)날씨 [지역]`\n`)미세먼지 [지역]`\n`)실검순위`")
		CmdListEmbed.add_field(name="관리 (관리자 권한)", value="`)경고 [유저] [사유]`\n`)추방 [유저]`\n`)차단 [유저]`\n`)채팅삭제 [갯수]`")
		CmdListEmbed.add_field(name="정보", value="`)봇정보`\n`)정보 [유저]`")
		CmdListEmbed.add_field(name="재미", value="`)주사위`\n`)소라고둥 [질문]`\n`)복권`")
		await bot.send_message(member,embed=CmdListEmbed)

@bot.command(pass_context=True)
async def 봇정보(ctx):
    HelpEmbed = discord.Embed(title="Info | 봇 정보",color=0x999999)
    HelpEmbed.add_field(name="이름", value="쿠키 봇 | Cookie Bot", inline=True)
    HelpEmbed.add_field(name="개발자", value="ReMac720_Studio", inline=True)
    HelpEmbed.add_field(name="개발 언어 및 API", value="Python 3.6.7\nDiscord.py", inline=True)
    HelpEmbed.add_field(name="봇 버전", value="beta 1.0", inline=True)
    HelpEmbed.add_field(name="서포트", value="(미공개)", inline=True)
    HelpEmbed.add_field(name="팀", value="(미정)", inline=True)
    await bot.say(embed=HelpEmbed)

@bot.command(pass_context=True)
async def 정보(ctx, user: discord.Member):
    embed = discord.Embed(title="'{}'의 정보".format(user.name), color=0x00ff00)
    embed.add_field(name="이름", value=user.name, inline=True)
    embed.add_field(name="상태", value=user.status, inline=True)
    embed.add_field(name="역할", value=user.top_role, inline=True)
    embed.add_field(name="들어온 시간", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
@정보.error
async def 정보_error(ctx, error):
    infoErrorEmbed = discord.Embed(title="명령어:   )정보",color=0x999999)
    infoErrorEmbed.add_field(name="사용법",value=")정보 [유저]")
    await bot.say(embed=infoErrorEmbed)
@bot.command(pass_context=True)
async def 곱셈(ctx, a:int, b:int):
    await bot.say(a*b)
	
@bot.command(pass_context=True)
async def 덧셈(ctx, a:int, b:int):
    await bot.say(a+b)
	
@bot.command(pass_context=True)
async def 뺄셈(ctx, a:int, b:int):
    await bot.say(a-b)

@bot.command(pass_context=True)
async def 나눗셈(ctx, a:int, b:int):
    await bot.say(a/b)

@bot.command(pass_context=True)
async def 날씨(ctx, a:str):
    location = a
    enc_location = urllib.parse.quote(location + '+날씨')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    WeatherEmbed = discord.Embed(title=":large_blue_diamond: "+a+" 날씨 온도 : "+soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text +'℃', color=0x00ff00)
    await bot.say(embed=WeatherEmbed)
@날씨.error
async def 날씨_error(ctx, error):
    weatherErrorEmbed = discord.Embed(title="명령어:   )날씨",color=0x999999)
    weatherErrorEmbed.add_field(name="사용법",value=")미세먼지 [지역]")
    weatherErrorEmbed.add_field(name="주의사항",value="[구, 동, 읍, 리] 로 검색해보세요. \n외국 지역은 지원하지 않습니다.")
    await bot.say(embed=weatherErrorEmbed)

@bot.command(pass_context=True)
async def 미세먼지(ctx, a:str):
    location = a
    enc_location = urllib.parse.quote(location + '+미세먼지')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    FindDustEmbed = discord.Embed(title=":large_blue_diamond: "+a+" 미세먼지 농도 : "+soup.find('span', class_='figure').find('em', class_='main_figure').text + '㎍/㎥', color=0x00ff00)
    await bot.say(embed=FindDustEmbed)
@미세먼지.error
async def 미세먼지_error(ctx, error):
    findDustErrorEmbed = discord.Embed(title="명령어:   )미세먼지",color=0x999999)
    findDustErrorEmbed.add_field(name="사용법",value=")미세먼지 [지역]")
    findDustErrorEmbed.add_field(name="주의사항",value="[구, 동, 읍, 리] 로 검색해보세요. \n외국 지역은 지원하지 않습니다.")
    await bot.say(embed=findDustErrorEmbed)

@bot.command(pass_context=True)
async def 경고(ctx, user: discord.Member,reason:str):
    if ctx.message.author.server_permissions.administrator:
        warnEmbed = discord.Embed(title=":warning: 쿠키 봇 경고 :warning:",color=0xFF0000)
        warnEmbed.add_field(name="유저:", value=user.name, inline=True)
        warnEmbed.add_field(name="사유:", value=reason, inline=True)
        await bot.say(embed=warnEmbed)
    else:
        NoPermissionEmbed = discord.Embed(title=":warning: 권한 부족")
        await bot.say(embed=NoPermissionEmbed)
@경고.error
async def 경고_error(ctx, error):
    warnErrorEmbed = discord.Embed(title="명령어:   )경고",color=0x999999)
    warnErrorEmbed.add_field(name="사용법",value=")경고 [유저] [사유]")
    await bot.say(embed=warnErrorEmbed)

@bot.command(pass_context = True)
async def 추방(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator:
        await bot.kick(userName)
        await bot.say(":white_check_mark: {}님 을(를) 추방(kick)했습니다.".format(userName))
    else:
        NoPermissionEmbed = discord.Embed(title=":warning: 권한 부족")
        await bot.say(embed=NoPermissionEmbed)
@추방.error
async def 추방_error(ctx, error):
    kickErrorEmbed = discord.Embed(title="명령어:   )추방",color=0x999999)
    kickErrorEmbed.add_field(name="사용법",value=")추방 [유저]")
    await bot.say(embed=kickErrorEmbed)

@bot.command(pass_context = True)
async def 차단(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator:
        await bot.ban(userName)
        await bot.say(":white_check_mark: {}님 을(를) 차단(ban)했습니다.".format(userName))
    else:
        NoPermissionEmbed = discord.Embed(title=":warning: 권한 부족")
        await bot.say(embed=NoPermissionEmbed)
@차단.error
async def 차단_error(ctx, error):
    banErrorEmbed = discord.Embed(title="명령어:   )차단",color=0x999999)
    banErrorEmbed.add_field(name="사용법",value=")차단 [유저]")
    await bot.say(embed=banErrorEmbed)

@bot.command(pass_context = True)
async def 실검순위(ctx):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')

        msg = await bot.say(":mag_right:  네이버에서 불러오는 중...")
        await asyncio.sleep(3)
        await bot.delete_message(msg)
        embed = discord.Embed(
            title='실시간 검색어',
            description='네이버에서 로드해왔어요!',
            color=0x0099cc
        )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            embed.add_field(name=str(i+1)+'위', value='\n'+'%s' % (realTimeSerach), inline=False) # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def 소라고둥(ctx):
    SoraRanInt = random.randint(1,3)
    if SoraRanInt == 1:
        SoraEmbed = discord.Embed(title="안 돼",color=0x990099)
        SoraEmbed.set_image(url="https://cdn.discordapp.com/attachments/483585833006268416/539117817790857247/CONCH.png")
        await bot.say(embed=SoraEmbed)
    if SoraRanInt == 2:
        SoraEmbed = discord.Embed(title="돼",color=0x990099)
        SoraEmbed.set_image(url="https://cdn.discordapp.com/attachments/483585833006268416/539117817790857247/CONCH.png")
        await bot.say(embed=SoraEmbed)
    if SoraRanInt == 3:
        SoraEmbed = discord.Embed(title="다시 한번 물어봐",color=0x990099)
        SoraEmbed.set_image(url="https://cdn.discordapp.com/attachments/483585833006268416/539117817790857247/CONCH.png")
        await bot.say(embed=SoraEmbed)

@bot.command(pass_context=True)
async def 주사위(ctx):
    ranNum = random.randint(1,6)
    if ranNum == 1:
        diceEmbed = discord.Embed(title=":game_dice: 주사위를 던집니다!", color=0x4286f4)
        diceWait = await bot.say(embed=diceEmbed)
        await asyncio.sleep(2)
        EditedDiceEmbed = discord.Embed(title=":game_dice: :one: 이(가) 나왔습니다.", color=0x4286f4)
        await bot.edit_message(diceWait, embed=EditedDiceEmbed)
        
    if ranNum == 2:
        diceEmbed = discord.Embed(title=":game_die: 주사위를 던집니다!", color=0x4286f4)
        diceWait = await bot.say(embed=diceEmbed)
        await asyncio.sleep(2)
        EditedDiceEmbed = discord.Embed(title=":game_die: :two: 이(가) 나왔습니다.", color=0x4286f4)
        await bot.edit_message(diceWait, embed=EditedDiceEmbed)
        
    if ranNum == 3:
        diceEmbed = discord.Embed(title=":game_die: 주사위를 던집니다!", color=0x4286f4)
        diceWait = await bot.say(embed=diceEmbed)
        await asyncio.sleep(2)
        EditedDiceEmbed = discord.Embed(title=":game_die: :three: 이(가) 나왔습니다.", color=0x4286f4)
        await bot.edit_message(diceWait, embed=EditedDiceEmbed)
    if ranNum == 4:
        diceEmbed = discord.Embed(title=":game_die: 주사위를 던집니다!", color=0x4286f4)
        diceWait = await bot.say(embed=diceEmbed)
        await asyncio.sleep(2)
        EditedDiceEmbed = discord.Embed(title=":game_die: :four: 이(가) 나왔습니다.", color=0x4286f4)
        await bot.edit_message(diceWait, embed=EditedDiceEmbed)
        
    if ranNum == 5:
        diceEmbed = discord.Embed(title=":game_die: 주사위를 던집니다!", color=0x4286f4)
        diceWait = await bot.say(embed=diceEmbed)
        await asyncio.sleep(2)
        EditedDiceEmbed = discord.Embed(title=":game_die: :five: 이(가) 나왔습니다.", color=0x4286f4)
        await bot.edit_message(diceWait, embed=EditedDiceEmbed)
        
    if ranNum == 6:
        diceEmbed = discord.Embed(title=":game_die: 주사위를 던집니다!", color=0x4286f4)
        diceWait = await bot.say(embed=diceEmbed)
        await asyncio.sleep(2)
        EditedDiceEmbed = discord.Embed(title=":game_die: :six: 이(가) 나왔습니다.", color=0x4286f4)
        await bot.edit_message(diceWait, embed=EditedDiceEmbed)

@bot.command(pass_context=True)
async def 복권(ctx):
    SpoilerRandom = random.randint(1,4)
    if SpoilerRandom == 1:
        SpoilerEmbed = discord.Embed(title=":slot_machine: 쿠키 봇 복권 :slot_machine: ",description="||:trophy:|| ||:trophy:|| ||:bomb:||")
        await bot.say(embed=SpoilerEmbed)

    if SpoilerRandom == 2:
        SpoilerEmbed = discord.Embed(title=":slot_machine: 쿠키 봇 복권 :slot_machine: ",description="||:trophy:|| ||:bomb:|| ||:trophy:||")
        await bot.say(embed=SpoilerEmbed)

    if SpoilerRandom == 3:
        SpoilerEmbed = discord.Embed(title=":slot_machine: 쿠키 봇 복권 :slot_machine: ",description="||:bomb:|| ||:trophy:|| ||:trophy:||")
        await bot.say(embed=SpoilerEmbed)

    if SpoilerRandom == 4:
        SpoilerEmbed = discord.Embed(title=":slot_machine: 쿠키 봇 복권 :slot_machine: ",description="||:trophy:|| ||:trophy:|| ||:trophy:||")
        await bot.say(embed=SpoilerEmbed)

@bot.command(pass_context=True)
async def 채팅삭제(ctx, number):
    if ctx.message.author.server_permissions.administrator:
        mgs = []
        number = int(number)
        async for x in bot.logs_from(ctx.message.channel, limit = number+1):
            mgs.append(x)
        await bot.delete_messages(mgs)
        delembed = discord.Embed(title=":speech_left: 메세지 삭제됨. (이 메세지는 3초 후 삭제됩니다)",color=0x4286f4)
        delmsg = await bot.say(embed = delembed)
        await asyncio.sleep(3)
        await bot.delete_message(delmsg)
    else:
        NoPermissionEmbed = discord.Embed(title=":warning: 권한 부족")
        await bot.say(embed=NoPermissionEmbed)
access_token = os.environ['BOT_TOKEN']
bot.run(access_token)
