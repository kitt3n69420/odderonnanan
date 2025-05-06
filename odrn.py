import random as r
import time
odrn="오때론난망가져갈지도모르지허나젊음엔그건중요한게아니야모든걸느끼고싶었던나잖아나는나만의인생을사는거니까"
appendChar="ㅏ아~"
jaeum="ㅂㅈㄷㄱㅅㅁㄴㅇㄹㅎㅋㅌㅊㅍ"
otherChat=["오때론난", "오때론난 도배금지", "여기 왜이래요?","채팅 코라지ㅋㅋ","캬","어우 정신없어", "그 긴거", "도금", "으악", "여기 채팅창 왜이래요?", "명곡", "오때론", "개좋다", "방송코라지ㅋㅋㅋㅋㄱ", "아 미치겠네ㅋㅋㅋㅋ", "유입 어카냐", "유입 컷", "오늘 유입은 어카냐", "여기 방송 원래 이런가요?", "얘! 오늘 유입은 없단다", "아오 듣기좋아", "ㄷㄷ", "니니게그사그런사라미", "오옹", "오옹 나이스", "도배 밴 조심", "저 처음 오는데 채팅창이 왜 이러는 건가요...?", "이게 뭐야", "오아무것도꺼릴것없는게나야나살아온동안세상을즐기며지내왔어오주위엔아무도없는혼자가좋아자유를느끼며난살았어아무리외로운날들이와도짧은사랑만하면서젊은청춘을달래만간거야너무진지한건싫어이런시간에남는게없", "언젠가그가너를맘아프게해너혼자울고있는걸봤어달려가그에게나이말해줬으면그대가울리는그한여자가내겐삶의전부라고"]
lowerBound = 0.08
upperBound = 0.3
slowExp    = 1.05
chatHeat   = 0.8
iconRate   = 0.05

def setDelay():
    chatDelay = lowerBound


    def chatWait():
        nonlocal chatDelay
        time.sleep(chatDelay)
        if r.random() > chatHeat:
            chatDelay = lowerBound
        else:
            chatDelay *= slowExp
            if(chatDelay>upperBound):
                chatDelay=lowerBound

    return chatWait


import random

def useNick():
    nicks = ["죽음의이지선다", "호볼랄라지나", "애매맨MMN", "인생이너무인생이야", "슈라이", "뽈롱뽈롱", "유튜브쟁이", "어딜가미", "뒤넘스러운", "세컨아이디접속", "바하트누", "위기의식과경각심TV", "키스남자남자", "영도소플라", "똥싸면서돈벌기", "영도올려", "구형벤치치", "춘희희님", "자숙왕최진우", "분홍살인마", "뭉탱조이고", "영양제먹어라", "뭉티기타지리", "EFT세계에오신걸환영합니다", "아이코난1", "흐헤헤흐헤헤", "얘뭐가잘안되니", "케인코뭉탱크다", "케인코축소위원회", "으시안오옹", "한화의김성근", "타지리는지누꺼야", "나는코양이다야옹", "뭉탱아", "코지리", "유썩썩TV", "게이티비", "계약서깠다구", "각자위치로", "음미음미", "지누야나도한입만줘", "한탕성공", "얘너지금뭐하니", "코지마코코볼코박사", "야채지누", "케숙이", "치지직갈껄", "트위치는돈통", "웰컴투더뭉탱이월드", "빵댕이패드", "나는나는장풍을했다", "보드를타고내려가서", "조이고즐기자", "또오또옹싸아", "닉네임을확인하셨군요", "삐삐삐삐삐죄가많아", "반제곱방어부스터", "유스핀미", "E등급수문장", "낙하무라지는스케", "코라뭉탱이", "깠다게슝", "수온은적당한가", "나는섹시가이", "여자는안돼요", "뭉탱탱님한판해요", "크리스야시로이오리", "지하실아사람", "스키비야", "지금부터는제가회의", "미칠듯사랑했던기억이", "제받아주면가받아주고", "나힐순없는지", "우마우도", "연두색테니스공", "3월18일", "너이게이씨", "볶음볶음감자볶음", "타미더써썩", "괜찮아무너진네이름마져", "니니게그사그런사람이", "느타리리", "잠깐이쯤되면케조씨는", "은평구코괴물", "뾰방이가되십시오", "공중에떠있는정장입은남자", "이거나드셔", "눈탱이밤탱이", "괘씸성공", "도망가지마맞서싸워", "케인인인인인인", "노즈게이스쿨", "씻구다시씻어먹는", "죠리퐁에서죠리퐁냄새", "아이고오", "알벨로", "도개걸윷뭉", "자뭐가생각나기금지", "게먹어게에", "11수트레인지", "제법세월이됩니다", "게이를조입시다", "파워게이저뭉탱이포스", "니하는플레이보이", "냐옹이"]
    nickColCycle = [96,174,180,179,143,72,73,67]
    icons = ["👃","\033[48;5;93m🤍\033[0m","🎁","🔑"]
    MaxCol     = len(nickColCycle)
    MaxNick    = len(nicks)
    curNick = 0
    curCol = 78
    def displayNick():
        nonlocal curNick, curCol
        curNick += 1
        curCol = (curCol + 1) % MaxCol
        if curNick == MaxNick:
            curNick = 0
            random.shuffle(nicks)
        formNick="\033[38;5;"  + str(nickColCycle[curCol]) + 'm' + str(nicks[curNick]) + "\033[0m\n"
        myIcons = ""
        for icon in icons:
            if (r.random()<iconRate):
                myIcons += icon
        return myIcons + formNick

    return displayNick

def repOdrn(n):
    return (odrn * ((n // 52) + 1))[:n] + "\n"
def appender():
    return appendChar[r.randint(0,2)]*r.randint(1,10)
def jaeumAppend():
    return "".join([r.choice(jaeum) for i in range(r.randint(1,10))])



def buildChat():
    myDelay = setDelay();
    myNick = useNick();

    def printChat():
        chatType=r.randint(1,16)
        chatCont=""
        if(chatType >14):
            chatCont = r.choice(otherChat) + "\n"
        elif(chatType>12):
            chatCont = repOdrn(r.randint(26,104))
        elif(chatType>10):
            chatCont='ㅋ'*r.randint(5,30)+"\n"
        elif(chatType>8):
            chatCont="오때론난망가져갈지도모르지허나젊음엔그건중요한게아니야\n"
        else:
            chatCont=odrn
            if(chatType < 3):
                chatCont += appender()
            elif(chatType<5):
                chatCont += jaeumAppend()
            elif(chatType<6):
                chatCont += str(r.randint(0,9))
            chatCont +="\n"
        myDelay()
        return myNick()+chatCont
    return printChat

chat=buildChat()
  

while(1):
    print(chat(),end="")