import tkinter as tk
from tkinter import filedialog
import logging
import os
import datetime
import sys
import requests
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
VAPE() #获取 QQ.exe 的位置
VAPE_LL() #获取 LiteLoaderQQNT 的位置
if os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini'): #总不可能没有了吧？
    if os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini'):
        with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini', 'r', encoding='utf-8') as latest_loc:
            qqnt_latest_location = latest_loc.read()
        with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini', 'r', encoding='utf-8') as qqnt:
            vape = qqnt.read()
            with open(f'{vape}/resources/app/app_launcher/index.js', 'w') as fxxkqq:
                fxxkqq.write(f"require(String.raw`{qqnt_latest_location}`);\nrequire('./launcher.node').load('external_index', module);")
    else:
        print('获取LieLoaderQQNT的位置时发生错误，你是否手动删除了那个记录LiteLoaderQQNT位置的ini文件？那你手速也太快了吧！')
        logging.info('在第二次获取LiteLoaderQQNT的位置时发生错误')
else:
    print('获取QQNT的位置时发生错误，你是否手动删除了那个记录QQNT位置的ini文件？')
    logging.info('在第二次获取（读取）QQNT的位置时发生错误')
    sys.exit()

import sys
maxbit=sys.maxsize #获取操作系统的位数 32 or 64
from tqdm import tqdm
import time

def download_patch_file():
    if maxbit>2**32: #64位
        print('你当前使用的操作系统为 64 位')
        logging.info('用户当前使用的操作系统为 64 位')
        url = f'https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/'+tag_data['tag_name']+'/dbghelp_x64.dll'
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        wrote = 0
        with open(f'{vape}/dbghelp.dll', 'wb') as file: #直接在这里改名
            # 使用 tqdm 显示下载进度
            with tqdm(total=total_size, unit='B', unit_scale=True, desc="dbghelp_x64.dll", initial=0, ascii=True, ncols=80) as pbar:
                start_time = time.time()
                for data in response.iter_content(block_size):
                    file.write(data)
                    pbar.update(len(data))
                    wrote += len(data)
                elapsed_time = time.time() - start_time
                pbar.set_postfix(time=elapsed_time)

        if total_size != 0 and wrote != total_size:
            print(f"遇到错误，请重试。")
            logging.error('下载 dbghelp_x64.dll 时发生错误')
        else: #如果下载完毕
            def compare_two_size(): #比较俩文件是不是一样的
                global local_patch_file_size
                local_patch_file_size = os.path.getsize(f'{vape}/dbghelp.dll')
                api = requests.get('https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest')
                tag_data = api.json() #获取当前补丁的版本号
                tag_NAME = tag_data['tag_name']
                local_size = local_patch_file_size
                for asset in tag_data.get('assets', []):
                        if asset.get('browser_download_url') == f"https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/{tag_NAME}/dbghelp_x64.dll": # 2024/8/13 20:43 这里不知道哪个智障给我生成了个错误的URL导致我排查了好久，望周知。
                            sizes = asset.get('size')
                if local_size == sizes: #如果文件大小一致
                    logging.info('补丁文件大小正确，通过检测')
                    print('补丁文件大小校验完毕，正确，通过检测')
                else: #如果不通过检测
                    logging.warning('远程 api 返回的文件大小与本地不一致。等待用户回应')
                    while True:
                        redownload_or_not = input(f'\n注意：文件完整性校验未通过，下载的文件可能不对。远程 api 返回的文件大小({sizes} B)与本地({local_size} B)不一致，是否重新下载？(y/n)\n选择：')
                        if redownload_or_not == 'y':
                            download_patch_file()
                        if redownload_or_not == 'n':
                            print('已忽略，不重新下载补丁')
                            logging.info('用户选择不重新下载，跳过检测')
                            break 
                        else:
                            print('输入错误，请重新输入')
            print(f"下载完成。在 {elapsed_time:.2f} 秒内下载完毕")
            logging.info(f'在 {elapsed_time:.2f} 秒内下载 dbghelp.dll 完毕')
            compare_two_size() #开始检测资源完整性
    else: #32位
        print('你当前使用的操作系统为 32 位')
        logging.info('用户当前使用的操作系统为 32 位')
        url = f'https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/'+tag_data['tag_name']+'/dbghelp_x86.dll'
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        wrote = 0
        with open(f'{vape}/dbghelp.dll', 'wb') as file: #直接在这里改名
            # 使用 tqdm 显示下载进度
            with tqdm(total=total_size, unit='B', unit_scale=True, desc="dbghelp_x86.dll", initial=0, ascii=True, ncols=80) as pbar:
                start_time = time.time()
                for data in response.iter_content(block_size):
                    file.write(data)
                    pbar.update(len(data))
                    wrote += len(data)
                elapsed_time = time.time() - start_time
                pbar.set_postfix(time=elapsed_time)

        if total_size != 0 and wrote != total_size:
            print(f"遇到错误，请重试。")
            logging.error('下载 dbghelp_x86.dll 时发生错误')
        else: #如果下载完毕
            def compare_two_size(): #比较俩文件是不是一样的
                global local_patch_file_size
                local_patch_file_size = os.path.getsize(f'{vape}/dbghelp.dll')
                api = requests.get('https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest')
                tag_data = api.json() #获取当前补丁的版本号
                tag_NAME = tag_data['tag_name']
                local_size = local_patch_file_size
                for asset in tag_data.get('assets', []):
                        if asset.get('browser_download_url') == f"https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/{tag_NAME}/dbghelp_x86.dll": # 在上面的x64分支：2024/8/13 20:43 这里不知道哪个智障给我生成了个错误的URL导致我排查了好久，望周知。
                            sizes = asset.get('size')
                if local_size == sizes: #如果文件大小一致
                    logging.info('补丁文件大小正确，通过检测')
                    print('补丁文件大小校验完毕，正确，通过检测')
                else: #如果不通过检测
                    logging.warning('远程 api 返回的文件大小与本地不一致。等待用户回应')
                    redownload_or_not = input(f'\n注意：文件完整性校验未通过，下载的文件可能不对。远程 api 返回的文件大小({sizes} B)与本地({local_size} B)不一致，是否重新下载？(y/n)\n选择：')
                    while True:
                        if redownload_or_not == 'y':
                            download_patch_file()
                        if redownload_or_not == 'n':
                            print('已忽略，不重新下载补丁')
                            logging.info('用户选择不重新下载，跳过检测')
                            break 
                        else:
                            print('输入错误，请重新输入')
            print(f"下载完成。在 {elapsed_time:.2f} 秒内下载完毕")
            logging.info(f'在 {elapsed_time:.2f} 秒内下载 dbghelp.dll 完毕')
            compare_two_size() #开始检测资源完整性
if os.path.exists(f'{localappdata}/LiteLoaderQQNT Auto Patch/Install_cancel_skip.ini'):
    with open(f'{localappdata}/LiteLoaderQQNT Auto Patch/Install_cancel_skip.ini', 'r', encoding='utf8') as check_install_cancel_skip:
        _install_cancel_skip = check_install_cancel_skip.read()
    if _install_cancel_skip == '1':
        logging.info('用户选择以后都不看这条提示，这次已触发')
        skip_install_dbghelp = "True"
    if _install_cancel_skip != '1':
        logging.info('用户的配置文件不为以后都不看这条提示，所以这次未触发跳过')
        skip_install_dbghelp = "False"
if skip_install_dbghelp == "False": #如果这个永久选择是False的话就执行，如果是True的话就跳过，并直接打开QQ
    if not os.path.exists(f'{vape}/dbghelp.dll'):
        print('提示：你目前没有安装 dbghelp.dll 补丁，建议安装。如果你有其他安装补丁的方法，可以选择跳过。如果以后都不想看到这条提示，请按3。')
        print('操作提示：\n1：从程序直接安装 dbghelp.dll 补丁\n2：跳过一次，下次如果没有安装 dbghelp.dll 就继续提示\n3：以后都不看这条提示')
        install_cancel_skip = input('是否安装 dbghelp.dll 补丁？(1/2/3)\n选择：')
        if install_cancel_skip == '1':
            logging.info('用户开始选择安装补丁 dbghelp.dll')
            import requests
            api = requests.get('https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest')
            if api.status_code == 200:
                logging.info('200: OK，请求成功')
                logging.info('正在获取当前补丁的版本号')
                tag_data = api.json() #获取当前补丁的版本号
                logging.info('当前补丁的tag为：'+tag_data['tag_name'])
                print('当前补丁的tag_name为：'+tag_data['tag_name']) #获取当前的版本号 tag_name
                if maxbit>2**32: #64-bit
                    x_what = "64"
                else: #32-bit
                    x_what = "86"
                for asset in tag_data.get('assets', []):
                    if asset.get('browser_download_url') == f"https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/"+tag_data['tag_name']+f"/dbghelp_x{x_what}.dll": # 在上面的x64分支：2024/8/13 20:43 这里不知道哪个智障给我生成了个错误的URL导致我排查了好久，望周知。
                        sizes = asset.get('size')
                logging.info('当前补丁的size为：'+str(sizes)+' B')
                print('当前补丁的大小为：'+str(sizes)+' B')
                download_patch_file()
            else:
                logging.error(f'api 请求失败，错误码：{api.status_code}')
                print(f'api 请求失败，错误码：{api.status_code}')
        if install_cancel_skip == '2':
            logging.info('用户选择跳过一次')
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
logging.info('正在启动QQ')
print('正在启动 QQ')
sys.exit() #退出终端，保留QQ
