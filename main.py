import tkinter as tk
from tkinter import filedialog
import logging
import os
import datetime
import sys
# 弄获取 %localappdata% ({system_disk}:\Users\{username}\Appdata\local)的路径
localappdata = os.path.expandvars("%LOCALAPPDATA%")
# 配置日志记录
if not os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch'):
    os.mkdir(f'{localappdata}/LiteLoaderQQNT Auto Patch/')
    os.mkdir(f'{localappdata}/LiteLoaderQQNT Auto Patch/Logs')
if not os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/Logs'):
    os.mkdir(f'{localappdata}/LiteLoaderQQNT Auto Patch/Logs')
def mklogs():
    global day_string
    nowtime = datetime.datetime.now()
    day_string = nowtime.strftime("%Y-%m-%d")
    logging.basicConfig(filename=f'{localappdata}/LiteLoaderQQNT Auto Patch/Logs/{day_string}.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', encoding='utf-8')        
    logging.info('\n------------\nRuning ON\n------------')
mklogs()
#检测有没有源目录
def VAPE():
    if not os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini'):
        # 创建一个隐藏的主窗口
        root = tk.Tk()
        root.iconbitmap(default='C:/Windows/System32/Shell32.dll')
        root.withdraw()  # 隐藏主窗口
        # 打开文件选择对话框
        root.attributes("-topmost", True)
        qqnt_path = filedialog.askdirectory(parent=root, title="选择 QQNT 的所在文件夹")
        # 将选择的路径写入配置文件
        if qqnt_path:
            logging.info(f"QQNT 的文件路径: {qqnt_path}")  # 打印文件路径
            with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini', 'w', encoding='utf8') as qqnt:
                qqnt.write(qqnt_path)
        else:
            print("你没有选择 QQNT 的位置，请重试。")
            import time
            time.sleep(3)
def VAPE_LL():
    global llqqnt_path
    if not os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini'):
        with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini', 'w') as llqqnt:
            llqqnt.write('')
        # 创建一个隐藏的主窗口
        root = tk.Tk()
        root.iconbitmap(default='C:/Windows/System32/Shell32.dll')
        root.withdraw()  # 隐藏主窗口
        # 打开文件选择对话框
        root.attributes("-topmost", True)
        llqqnt_path = filedialog.askdirectory(parent=root, title="选择 LiteLoaderQQNT 的所在文件夹")
        # 将选择的路径写入配置文件
        if llqqnt_path:
            logging.info(f"LiteLoaderQQNT 的文件路径: {llqqnt_path}")  # 打印文件路径
            with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini', 'w', encoding='utf8') as llqqnt:
                llqqnt.write(llqqnt_path)
        else:
            print("你没有选择 LiteLoaderQQNT 的位置，请重试。")
            import time
            time.sleep(3)
VAPE()
VAPE_LL()
if os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini'):
    if os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini'):
        with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini', 'r', encoding='utf-8') as latest_loc:
            qqnt_latest_location = latest_loc.read()
        with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini', 'r', encoding='utf-8') as qqnt:
            vape = qqnt.read()
            with open(f'{vape}/resources/app/app_launcher/index.js', 'w') as fxxkqq:
                fxxkqq.write(f"require(String.raw`{qqnt_latest_location}`);\nrequire('./launcher.node').load('external_index', module);")
    else:
        print('error')
else:
    print('error')

import sys
maxbit=sys.maxsize #获取操作系统的位数 32 or 64
def download_patch():
    if maxbit>2**32: #64位
        import requests
        url = f'https://gh.api.99988866.xyz/https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/'+data['tag_name']+'/dbghelp_x64.dll'
        response = requests.get(url)
        logging.info('已下载补丁 dbghelp_x64.dll')
        with open(f'{vape}/dbghelp.dll', 'wb') as f: #改名为 dbghelp.dll
            f.write(response.content)
        logging.info('已完成补丁 dbghelp.dll 的安装')
    else:
        import requests
        url = f'https://gh.api.99988866.xyz/https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/'+data['tag_name']+'/dbghelp_x86.dll'
        response = requests.get(url)
        logging.info('已下载补丁 dbghelp_x64.dll')
        with open(f'{vape}/dbghelp.dll', 'wb') as f: #改名为 dbghelp.dll
            f.write(response.content)
            logging.info('已完成补丁 dbghelp.dll 的安装')
if os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/Install_cancel_skip.ini'):
    with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/Install_cancel_skip.ini', 'r', encoding='utf8') as check_install_cancel_skip:
        _install_cancel_skip = check_install_cancel_skip.read()
    if _install_cancel_skip == '1':
        logging.info('用户选择以后都不看这条提示，这次已触发')
        exit()
if not os.path.exists(f'{vape}/dbghelp.dll'):
    print('提示：你目前没有安装 dbghelp.dll 补丁，建议安装。如果你有其他安装方法，请跳过。如果以后都不想看到这条提示，请按3。')
    print('操作提示：\n1：从程序直接安装 dbghelp.dll 补丁\n2：跳过一次，下次如果没有安装 dbghelp.dll 就继续提示\n3：以后都不看这条提示')
    install_cancel_skip = input('是否安装 dbghelp.dll 补丁？(1/2/3)\n选择：')
    if install_cancel_skip == '1':
        logging.info('用户开始选择安装补丁.dll')
        import requests
        api = requests.get('https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest')
        if api.status_code == 200:
            logging.info('200: OK，请求成功')
            logging.info('正在获取当前补丁的版本号')
            data = api.json() #获取当前补丁的版本号
            logging.info('当前tag为：'+data['tag_name'])
            print('当前tag_name为：'+data['tag_name']) #获取当前的版本号 tag_name
            download_patch()
        else:
            logging.error(f'请求失败，错误码：{api.status_code}')
            print(f'请求失败，错误码：{api.status_code}')
    if install_cancel_skip == '2':
        logging.info('用户选择跳过一次')
        exit()
    if install_cancel_skip == '3':
        logging.info('用户选择以后都不看这条提示')
        with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/Install_cancel_skip.ini', 'w', encoding='utf8') as install_cancel_skip:
            install_cancel_skip.write('1')

if not os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQ.exe.lnk'): #创建快捷方式      
    import os
    import win32com.client

    # 获取存放路径
    desktop = os.path.join(f"{localappdata}/LiteLoaderQQNT Auto Patch") #local
 
    # 设置快捷方式的目标路径和名称
    target = rf"{vape}/QQ.exe"
    shortcut_name = "QQ.lnk"
    shortcut_path = os.path.join(desktop, shortcut_name)

    # 创建快捷方式
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    shortcut.IconLocation = target  # 使用脚本图标
    shortcut.save()
#import subprocess 给那个不知道能不能自动退出的玩意用的
dir = f"{localappdata}/LiteLoaderQQNT Auto Patch/QQ.lnk"
#subprocess.Popen([f"cmd /c start",dir], shell=True) 我敲这玩意不能用 不会自动退出，除非你自己关掉终端或者cmd
os.startfile(dir) #os库yyds 不过这玩意是在qq的登陆界面才自动关闭的
sys.exit() #退出终端，保留QQ