![cover](readme/cyberchat.png)

[中文](README.md "中文") [English](eng-README.md "English") [日本語](jp-README.md "日本語")

<p align="center">
	<img alt="GitHub" src="https://img.shields.io/github/license/cjyaddone/ChatWaifu?color=red">
	<img src="https://img.shields.io/badge/Python-3.7|8|9|10-green" alt="PYTHON" >
  	<a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu?ref=badge_small" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu.svg?type=small"/></a>
</p>

#

### 这是一个使用TTS+VITS的ChatGPT语音对话程序!

**当前支持功能：**
* [x] ChatGPT的对话聊天
* [x] 回答转语音
* [x] 多角色语音
* [x] 语音识别对话 (研发了一款真正人性化的智能语音Q宝


# 目录
### 本项目均默认使用Chrome浏览器
* [1.安装环境：](#1.)
	* 1.1 [使用cd命令进入项目文件夹](#cd)
	* 1.2 [创建Python虚拟环境:](#99)
	* 1.3 [进入创建好的虚拟环境:](#venv)
	* 1.4 [pip安装项目所需要的库文件:](#pip)
* [2.运行（快和我的老婆们对话吧:](#22)
	* 3.1 [获取ChatGPT Token](#333)
	* 3.2 [开始和CyberWaifu聊天](#444)
* [4.鸣谢](#915)
## <span id="1.">1.安装环境：</span>
> **安装anaconda环境或Python>=3.7**
> 
> **本例使用的环境名称是：chatWaifu**

### <span id="cd">1.1 使用cd命令进入项目文件夹</span>
`cd 你的项目路径`
![](readme/5.png)
### <span id="99">1.2 创建Python虚拟环境:</span>

Conda:`conda create --name chatWaifu python=3.10`
![](readme/1.png)
![](readme/2.png)
Python:`python -m venv chatWaifu`
![](readme/6.png)

### <span id="venv">1.3 进入创建好的虚拟环境:</span>
Conda:`conda activate chatWaifu`
![](readme/3.png)

Python:`.\chatWaifu\Scripts\activate.bat`
![](readme/7.png)

### <span id="pip">1.4 pip安装项目所需要的库文件:</span>
`pip install -r requirements.txt`
![](readme/4.png)

## <span id="22">2.运行（快和老婆们对话吧:</span>

打字输入版：`python ChatWaifu.py`

语音对话版（日语和英语输入默认中文输出）：`python ChatWaifuVoice.py`

### <span id="333">3.1 获取ChatGPT Token</span>
#### 在浏览器登入https://chat.openai.com
#### 按F12进入开发控制台
#### 找到 应用程序 -> cookie -> __Secure-next-auth.session-token
![](readme/token.png)
#### 将值复制进入终端并回车

### <span id="444">3.2 开始和CyberWaifu聊天！！！</span>

**语音对话版:** 当控制台提示"You:"时开始说话，说完并出现句子录音结束并发送到ChatGPT对话。

附赠:[ChatGPT 中文调教指南](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)

## <span id="915">4.鸣谢：</span>
- [MoeGoe_GUI]https://github.com/CjangCjengh/MoeGoe_GUI
- [PyChatGPT]https://github.com/terry3041/pyChatGPT
