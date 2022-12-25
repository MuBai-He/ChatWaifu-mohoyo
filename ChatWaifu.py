import utils
import commons
import sys
import re
from winsound import PlaySound
import requests


####################################
#CHATGPT INITIALIZE
from pyChatGPT import ChatGPT
import json

voice_api = "http://267978.proxy.nscc-gz.cn:8888"

idmessage_cn = """      
Speaker
['派蒙','空','荧','阿贝多','枫原万叶','温迪','八重神子','纳西妲','钟离','诺艾尔','凝光','托马',
           '北斗','莫娜','荒泷一斗','提纳里','芭芭拉','艾尔海森','雷电将军','赛诺','琴','班尼特','五郎',
           '神里绫华','迪希雅','夜兰','辛焱','安柏','宵宫','云堇','妮露','烟绯','鹿野院平藏','凯亚','达达利亚',
           '迪卢克','可莉','早柚','香菱','重云','刻晴','久岐忍','珊瑚宫心海','迪奥娜','戴因斯雷布','魈',
           '神里绫人','丽莎','优菈','凯瑟琳','雷泽','菲谢尔','九条裟罗','甘雨','行秋','胡桃','迪娜泽黛',
           '柯莱','申鹤','砂糖','萍姥姥','奥兹','罗莎莉亚','式大将','哲平','坎蒂丝','托克','留云借风真君',
           '昆钧','塞琉斯','多莉','大肉丸','莱依拉','散兵','拉赫曼','杜拉夫','阿守','玛乔丽','纳比尔',
           '海芭夏','九条镰治','阿娜耶','阿晃','阿扎尔','七七','博士','白术','埃洛伊','大慈树王','女士',
           '丽塔','失落迷迭','缭乱星棘','伊甸','伏特加女孩','狂热蓝调','莉莉娅','萝莎莉娅','八重樱','八重霞',
           '卡莲','第六夜想曲','卡萝尔','姬子','极地战刃','布洛妮娅','次生银翼','理之律者','迷城骇兔','希儿',
           '魇夜星渊','黑希儿','帕朵菲莉丝','天元骑英','幽兰黛尔','德丽莎','月下初拥','朔夜观星','暮光骑士',
           '明日香','李素裳','格蕾修','梅比乌斯','渡鸦','人之律者','爱莉希雅','爱衣','天穹游侠','琪亚娜',
           '空之律者','薪炎之律者','云墨丹心','符华','识之律者','维尔薇','芽衣','雷之律者','阿波尼亚']
"""



def get_input():
    # prompt for input
    print("You:")
    user_input = input()
    return user_input


def get_token():
    token = input("Copy your token from ChatGPT and press Enter \n")
    return token

      
################################################


logging.getLogger('numba').setLevel(logging.WARNING)


def ex_print(text, escape=False):
    if escape:
        print(text.encode('unicode_escape').decode())
    else:
        print(text)


def get_text(text, hps, cleaned=False):
    if cleaned:
        text_norm = text_to_sequence(text, hps.symbols, [])
    else:
        text_norm = text_to_sequence(text, hps.symbols, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm


def ask_if_continue():
    while True:
        answer = input('Continue? (y/n): ')
        if answer == 'y':
            break
        elif answer == 'n':
            sys.exit(0)



def generateSound(text, speaker):
    if '--escape' in sys.argv:
        escape = True
    else:
        escape = False
        url_sound = voice_api + "?speaker=" + speaker + "&text=" + text + "&format=wav"
        sound_bytes = requests.get(url=url_sound).content
        return sound_bytes


if __name__ == "__main__":
    session_token = get_token()
    api = ChatGPT(session_token)
    print("\n" + idmessage_cn)
    speaker = input('选择角色: ')
    print()
    while True:
            resp = api.send_message(get_input())
            if(resp == "quit()"):
                break
            answer = resp["message"].replace('\n','')
            print("ChatGPT:")
            print(answer)
            PlaySound(generateSound(answer, speaker), winsound.SND_MEMORY)
