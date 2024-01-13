import discord # discord.py 임포트
from discord import app_commands # discord.py 에서 app_commands (슬래쉬 커멘드) 임포트
import requests # API 사용을 위한 requests 임포트
import random

intents = discord.Intents.all() # 모든 인텐트 활성화
client = discord.Client(intents=intents) # client 인스턴스 (객체) 생성 + intents 적용
command_tree = app_commands.CommandTree(client) # 커맨드 트리 (커멘드가 들어갈 공간) 생성 
# -> ? > 왜 Tree를 생성하냐, Slash Command는 메시지 커멘드와 다르게 Discord 서버에 슬래쉬 데이터를 전송해줘야 슬래쉬커멘드가 생성되기 때문에
# Tree 공간에 데이터를 저장해두고 이 데이터들을 모아서 Discord 측에 전송해주는 방식으로 커멘드를 생성함

guild_id = discord.Object(id=1190259210521419917) # 슬래쉬 데이터가 들어갈 길드 id



# Client에 Event를 생성함
@client.event
async def on_ready(): # on_ready 라는 이벤트가 수신될때 아래 코드를 실행함
    await command_tree.sync(guild=guild_id) # 위에 설명한대로 Tree에 있는 데이터들을 Discord 서버에 전송하는 코드
    print("ready"),

# 위에 설명한대로 tree에 슬래쉬 커멘드 데이터를 넣어주는 코드
@command_tree.command(
    name="오근욱은", # 커멘드 이름
    description="오근욱에 대한 ai의 인상을 말해줍니다", # 커멘드 설명
    guild=guild_id
)

async def ping(interaction: discord.Interaction):
    List = ['다시 태어나야한다' , '드럽게 못생겼다' , '발가락 무좀같이 생겼다' , '하수구처럼 생겼다' , '거미처럼 생겼다' , '지나가는 아저씨처럼 생겼다' , '할아버지처럼 생겼다' , '늙었다' , '노안이 왔다' , '3cm이다' , '키가 여기서 멈췄다', '시력이 낮다', '공부를 못한다' , '공부를 드릅게 못한다' , '잘하는게 없다' , '잘생겼다' , '멍청하다' , '시험문제 다찍고 다틀렸다' ]
    ListB = random.choice(List)
    await interaction.response.send_message(f"오근욱은 {ListB}"), 


@command_tree.command(
    name="오늘의_추천_애니", # 커멘드 이름
    description="오늘의 추천 애니를 말해줍니다", # 커멘드 설명
    guild=guild_id
)

async def ping(interaction: discord.Interaction): 
    await interaction.response.send_message("경계의저편을 추천합니다!"), 






@command_tree.command(
    name="오늘의_운세", 
    description="오늘의 운세를 알려줘요!", 
    guild=guild_id
)

async def ping(interaction: discord.Interaction): 
    luck_list = ['오늘의 운세는 아주 좋아요 로또 한장 구입해보는거 어때요?' , '오늘의 운세는 적당히 나쁘지 않아요!' , '오늘의 운세는 적당히 나쁘지 않아요!' , '오늘의 운세는 보통이에요! 집가는길에 음료수 한잔 어때요?' ,  '오늘의 운세는 보통이에요! 집가는길에 음료수 한잔 어때요?' , '오늘의 운세는 보통이에요! 집가는길에 음료수 한잔 어때요?' , '오늘의 운세는 아쉽지만 나빠요 ㅜ.ㅜ 외출은 삼가해주세요!!']
    rand_luck = random.choice(luck_list)
    await interaction.response.send_message(f"{rand_luck}"), 





@command_tree.command(
    name="ping", # 커멘드 이름
    description="테스트 커멘드", # 커멘드 설명
    guild=guild_id
)

async def ping(interaction: discord.Interaction): 
    await interaction.response.send_message("Pong!"), 


# 아래 기능은 랜덤으로 2D 사진을 가져오는 API를 사용해서 사용자에게 사진을 전송해주는 그런 커멘드입니다.
# 해당 API는 https://waifu.pics/docs 에서 자세한 옵션을 확인할 수 있습니다.
# 간단하게 요약하자면, `https://api.waifu.pics/type/category` 이런식의 형태로 요청하는 API 입니다.
# type 에는 `sfw`가 들어가야하고 category 에는 waifu, neko, cuddle 등등 몇십가지가 넘는 카테고리가 있습니다.
# SlashCommand Choice 옵션을 사용해서 사용자가 원하는 카테고리를 선택할 수 있게 만들었습니다.

# 슬래쉬 커멘드에선 다양한 옵션이 있는데 그중 Choice 옵션을 사용
@command_tree.command(
    name="여친",    
    description="ㅠㅠ",
    guild=guild_id
)
# Choice 옵션의 예시입니다. 위에있는거 다 넣어줘야합니다.
@app_commands.choices(choices=[
    app_commands.Choice(name="일반", value="waifu"), #name 은 사용자에게 직접적으로 보여질 값, value는 백앤드에서의 작업시 필요한 값입니다
    app_commands.Choice(name="고양이", value="neko"),
    app_commands.Choice(name="놀림", value="bully"),
    app_commands.Choice(name="안아줘", value="cuddle"),
    app_commands.Choice(name="포옹", value="hug"),
    app_commands.Choice(name="아우", value="awoo"),
    app_commands.Choice(name="키스", value="kiss"),
    app_commands.Choice(name="핥짝", value="lick"),
    app_commands.Choice(name="펫", value="pat"),
    app_commands.Choice(name="으쓱", value="smug"),
    app_commands.Choice(name="깜짝아", value="yeet"),
    app_commands.Choice(name="발그레", value="blush"),
    app_commands.Choice(name="웃음", value="smile"),
    app_commands.Choice(name="인사", value="wave"),
    app_commands.Choice(name="하이파이브", value="highfive"),
    app_commands.Choice(name="손잡기", value="handhold"),
    app_commands.Choice(name="냠", value="nom"),
    app_commands.Choice(name="와그작", value="bite"),
    app_commands.Choice(name="찰싹", value="slap"),
    app_commands.Choice(name="죽여", value="kill"),
    app_commands.Choice(name="차", value="kick"),
    app_commands.Choice(name="행복", value="happy"),
    app_commands.Choice(name="윙크", value="wink"),
    app_commands.Choice(name="춤", value="dance"),
    app_commands.Choice(name="창피", value="cringe")
])

async def pick_waifu(interaction: discord.Interaction, choices: app_commands.Choice[str]):
    img_url = requests.get(f"https://api.waifu.pics/sfw/{choices.value}").json()["url"] 
    await interaction.response.send_message(img_url) 


@command_tree.command(
    name="여친없음",
    description="ㅠㅠㅠㅠㅠㅠ",
    guild=guild_id
)

@app_commands.choices(choices=[
    app_commands.Choice(name="최애", value="waifu"),
    app_commands.Choice(name="고양이", value="neko"),
    app_commands.Choice(name="입", value="blowjob")
])


async def pick_waifu(interaction: discord.Interaction, choices: app_commands.Choice[str]):
    img_url = requests.get(f"https://api.waifu.pics/nsfw/{choices.value}").json()["url"] 
    await interaction.response.send_message(img_url) 



@command_tree.command(
    name="개",
    description="당신이 몰랐던 \"개\"의 TMI",
    guild=guild_id
)
async def tmi_dog(interaction: discord.Interaction):
    fact = requests.get("https://dog-api.kinduff.com/api/facts").json()["facts"][0] # facts 키는 리스트이기때문에 [0]으로 첫번째 값을 가져옴

    # 파파고 API를 사용해서 영어로된 fact를 한국어로 번역함
    translate = requests.post(f"https://openapi.naver.com/v1/papago/n2mt", headers={ # 헤더에는 API 및 보안인증 관련정보를 넣어줌
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": "BBysgKa7pSvWuJwf6SUS",
        "X-Naver-Client-Secret": "Rdl2ZsQiIB"
    }, params={ # 파라미터에는 번역할 텍스트와 번역할 언어를 넣어줌 (파라미터는 URL에 붙는 ? 뒤에 붙는 값들, body 하고 다름)
        "source": "en",
        "target": "ko",
        "text": fact
    }).json()

    await interaction.response.send_message(translate["message"]["result"]["translatedText"]) # 마찬가지로 JSON으로 변환 후 필요한 값을 가져옴



client.run("MTE5MDY0Nzk1ODIzMjg5OTc0NA.G2FhSw.zl1E-8y_mdVKP5aGFhO8EFr5YBijgZXtD11LZM")