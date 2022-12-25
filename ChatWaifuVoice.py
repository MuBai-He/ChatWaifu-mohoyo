import sys
import re
import logging
import winsound 
import argparse
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
voice_api = "http://267978.proxy.nscc-gz.cn:8888"

q = queue.Queue()
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
parser.add_argument(
    "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
args = parser.parse_args(remaining)
try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])

    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None



except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)

####################################
#CHATGPT INITIALIZE
from pyChatGPT import ChatGPT
import json


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
inputLanguage = """ID      Input Language
0       Chinese
1       Japanese
2       English
"""

def get_language_id(message):
    speaker_id = input(message)
    try:
        speaker_id = int(speaker_id)
    except:
        print(str(speaker_id) + ' is not a valid ID!')
        sys.exit(1)
    return speaker_id

def voice_input_jp():
    model = Model(lang="cn")
    print("You:")
    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                           dtype="int16", channels=1, callback=callback):

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                a = json.loads(rec.Result())
                a = str(a['text'])
                a = ''.join(a.split())
                if(len(a) > 0):
                    print(a)
                    user_input = a + " 使用日本语"
                    return user_input
            if dump_fn is not None:
                dump_fn.write(data)

def voice_input_cn():
    model = Model(lang="cn")
    print("You:")
    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                           dtype="int16", channels=1, callback=callback):

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                a = json.loads(rec.Result())
                a = str(a['text'])
                a = ''.join(a.split())
                if(len(a) > 0):
                    print(a)
                    user_input = a
                    return user_input
            if dump_fn is not None:
                dump_fn.write(data)

def voice_input_jpzh():
    model = Model(lang="ja")
    print("You:")
    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                           dtype="int16", channels=1, callback=callback):

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                a = json.loads(rec.Result())
                a = str(a['text'])
                a = ''.join(a.split())
                if(len(a) > 0):
                    print(a)
                    user_input = a + " 使用中文"
                    return user_input
            if dump_fn is not None:
                dump_fn.write(data)

def voice_input_enzh():
    model = Model(lang="en-us")
    print("You:")
    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                           dtype="int16", channels=1, callback=callback):

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                a = json.loads(rec.Result())
                a = str(a['text'])
                a = ''.join(a.split())
                if(len(a) > 0):
                    print(a)
                    user_input = a + " 使用中文"
                    return user_input
            if dump_fn is not None:
                dump_fn.write(data)


def get_token():
    token = input("Copy your token from ChatGPT and press Enter \n")
    return token

      
################################################
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
    print(inputLanguage)
    language_id = get_language_id("选择输入语言：")
    print("\n" + idmessage_cn)
    speaker = input('选择角色: ')
    print()
    while True:
        if language_id == 0 : #input=cn
            resp = api.send_message(voice_input_cn())
            if(resp == "quit()"):
                break
            answer = resp["message"].replace('\n','')
            print("ChatGPT:")
            print(answer)
            winsound.PlaySound(generateSound(answer, speaker), winsound.SND_MEMORY)
        elif language_id == 1: #input=jp
            resp = api.send_message(voice_input_jpzh())
            answer = resp["message"].replace('\n','')
            print("ChatGPT:")
            print(answer)
            winsound.PlaySound(generateSound(answer, speaker), winsound.SND_MEMORY)
        elif language_id == 2: #input=en
            resp = api.send_message(voice_input_enzh())
            answer = resp["message"].replace('\n','')
            print("ChatGPT:")
            print(answer)
            winsound.PlaySound(generateSound(answer, speaker), winsound.SND_MEMORY)
