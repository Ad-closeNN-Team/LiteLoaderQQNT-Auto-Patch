"""
程序入口点。
"""

import datetime
import logging
import os
import sys
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import requests
import win32com.client
from tqdm import tqdm

# 弄获取 %LOCALAPPDATA% ({system_disk}:\Users\{username}\Appdata\local)的路径
LOCALAPPDATA = Path(os.path.expandvars("%LOCALAPPDATA%"))
# 配置日志记录
(WORKDIR := LOCALAPPDATA / "LiteLoaderQQNT Auto Patch").mkdir(exist_ok=True)
(LOGDIR := LOCALAPPDATA / "LiteLoaderQQNT Auto Patch/Logs").mkdir(exist_ok=True)

# 加载设置
skip_dbg = Path(f"{WORKDIR}/Install_cancel_skip.ini")
if skip_dbg.is_file():
    with skip_dbg.open(
        "r",
        encoding="utf-8",
    ) as ini:
        _install_cancel_skip = ini.read()
    SKIP_DBGHELP = _install_cancel_skip == "1"
    logging.log(logging.INFO, f"用户是否跳过提示：{SKIP_DBGHELP}")
else:
    SKIP_DBGHELP = False


def mklogs():
    """
    日志初始化。
    """
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
    logging.basicConfig(
        filename=LOGDIR / f"{nowtime}.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# 检测有没有源目录
def vape_qq():
    """
    获取 QQNT 目录。如果找不到，弹窗要求用户选择 QQNT 源目录。
    """
    if (ini := WORKDIR / "QQNT_file_path.ini").exists():
        with ini.open("r", encoding="utf-8") as f:
            return Path(f.read())
    # 创建一个隐藏的主窗口
    root = tk.Tk()
    root.iconbitmap(default="C:/Windows/System32/Shell32.dll")
    root.withdraw()  # 隐藏主窗口
    # 打开文件选择对话框
    qqnt_path = filedialog.askdirectory(title="选择 QQNT 的所在文件夹")
    # 将选择的路径写入配置文件
    if not qqnt_path:
        print("你没有选择 QQNT 的位置，请重试。")
        return None
    logging.info("QQNT 的文件路径: %s", qqnt_path)  # 打印文件路径
    qqnt_path = Path(qqnt_path)
    if not qqnt_path.exists():
        print("你选择的 QQNT 的位置不存在，请重试。")
        return None

    with ini.open("w", encoding="utf-8") as f:
        f.write(qqnt_path.as_posix())

    return qqnt_path


def vape_ll():
    """
    获取 LiteLoaderQQNT 目录。如果找不到，弹窗要求用户选择。
    """
    if (ini := WORKDIR / "LiteLoaderQQNT_file_path.ini").exists():
        with ini.open("r", encoding="utf-8") as f:
            return Path(f.read())
    # 创建一个隐藏的主窗口
    root = tk.Tk()
    root.iconbitmap(default="C:/Windows/System32/Shell32.dll")
    root.withdraw()  # 隐藏主窗口
    # 打开文件选择对话框
    qqnt_path = filedialog.askdirectory(title="选择 LiteLoaderQQNT 的所在文件夹")
    # 将选择的路径写入配置文件
    if not qqnt_path:
        print("你没有选择 LiteLoaderQQNT 的位置，请重试。")
        return None
    logging.info("LiteLoaderQQNT 的文件路径: %s", qqnt_path)  # 打印文件路径
    qqnt_path = Path(qqnt_path)
    if not qqnt_path.exists():
        print("你选择的 LiteLoaderQQNT 的位置不存在，请重试。")
        return None

    with ini.open("w", encoding="utf-8") as f:
        f.write(qqnt_path.as_posix())

    return qqnt_path


def is_64bit():
    """
    当前操作系统是否为 64 位。
    """
    return sys.maxsize > 2**32


def compare_two_size(pathqq: Path):
    """
    比较本地文件和远程文件的大小。
    """
    # global local_patch_file_size
    local_size = os.path.getsize(f"{pathqq}/dbghelp.dll")
    resp = requests.get(
        "https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest",
        timeout=15,
    )
    data = resp.json()  # 获取当前补丁的版本号
    size = [
        a.get("size")
        for a in data.get("assets", [])
        if a.get("name") == "dbghelp_x64.dll"
    ].pop(
        0
    )  # 获取远程补丁文件大小
    assert isinstance(size, int), f"remote size is not int ({size})"
    if local_size == size:  # 如果文件大小一致
        logging.info("补丁文件大小正确，通过检测")
        print("补丁文件大小校验完毕，正确，通过检测")
        return True
    logging.warning("远程 api 返回的文件大小与本地不一致。等待用户回应")
    while True:
        redownload_or_not = input(
            f"""
注意：文件完整性校验未通过，下载的文件可能不正确。远程 API 返回的文件大小 ({size} B) 与本地 ({local_size} B) 不一致。是否重新下载？(Y/N/C)
Y - 重新下载
N - 不重新下载并继续
C - 不重新下载并退出
选择："""
        )
        match redownload_or_not.lower():
            case "y":
                download_patch_file(pathqq)
                return True
            case "n":
                logging.info("用户选择不重新下载，跳过检测")
                print("已忽略，不重新下载补丁")
                return True
            case "c":
                logging.info("用户选择不重新下载并退出")
                return False
            case _:
                print("输入无效，请重新输入。")


def download_patch_file(pathqq: Path):
    """
    下载 dbghelp.dll 并保存。返回是否成功。
    """
    if is_64bit():  # 64位
        print("你当前使用的操作系统为 64 位")
        logging.info("用户当前使用的操作系统为 64 位")
        file_name = "dbghelp_x64.dll"
    else:
        file_name = "dbghelp_x86.dll"
    api = requests.get(
        "https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest",
        timeout=15,
    )
    if not api.ok:
        print(f"请求失败（{api.status_code}），请重试。")
        logging.error(f"请求失败（{api.status_code}）。")
        return False
    logging.info("200: OK，请求成功")
    logging.info("正在获取当前补丁的版本号")
    tag_data = api.json()  # 获取当前补丁的版本号
    logging.info("当前补丁的tag为：" + tag_data["tag_name"])
    print("当前补丁的tag_name为：" + tag_data["tag_name"])  # 获取当前的版本号 tag_name
    response = requests.get(
        f"https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/download/{tag_data['tag_name']}/{file_name}",
        stream=True,
        timeout=30,
    )
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    wrote = 0
    with open(f"{pathqq}/dbghelp.dll", "wb") as file:  # 直接在这里改名
        # 使用 tqdm 显示下载进度
        with tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            desc=file_name,
            initial=0,
            ascii=True,
            ncols=80,
        ) as pbar:
            start_time = time.time()
            for data in response.iter_content(block_size):
                file.write(data)
                pbar.update(len(data))
                wrote += len(data)
            elapsed_time = time.time() - start_time
            pbar.set_postfix(time=elapsed_time)

    if total_size not in (0, wrote):
        print("遇到错误，请重试。")
        logging.error(f"下载 {file_name} 时发生错误")
        return False

    print(f"下载完成，用时 {elapsed_time:.2f} 秒。")
    logging.info(f"下载 dbghelp.dll 完成，用时 {elapsed_time:.2f} 秒。")
    if not compare_two_size(pathqq):  # 检测资源完整性
        sys.exit(1)
    return True


def install_dbghelp(pathqq: Path):
    """
    安装 dbghelp.dll 补丁。
    """
    dbg = Path(f"{pathqq}/dbghelp.dll")
    if SKIP_DBGHELP or dbg.exists():
        return
    # 如果这个永久选择是False的话就执行，如果是True的话就跳过
    print(
        "提示：你目前没有安装 dbghelp.dll 补丁，建议安装。如果你有其他安装补丁的方法，可以选择跳过。如果以后都不想看到这条提示，请按3。"
    )
    print(
        "操作提示：\n1：从程序直接安装 dbghelp.dll 补丁\n2：跳过一次，下次如果没有安装 dbghelp.dll 就继续提示\n3：以后都不看这条提示"
    )
    install_cancel_skip = input("是否安装 dbghelp.dll 补丁？(1/2/3)\n选择：")
    match install_cancel_skip:
        case "2":
            logging.info("用户选择跳过一次")
            return
        case "3":
            logging.info("用户选择以后都不看这条提示")
            with skip_dbg.open("w", encoding="utf-8") as f:
                f.write("1")
            return
    logging.info("用户选择开始安装补丁 dbghelp.dll")
    download_patch_file(pathqq)


def create_shortcut(pathqq: Path):
    """
    为 QQ 创建快捷方式。
    """
    if not os.path.exists(
        f"{LOCALAPPDATA}/LiteLoaderQQNT Auto Patch/QQ.exe.lnk"
    ):  # 创建快捷方式

        # 获取存放路径
        # desktop = os.path.join(f"{LOCALAPPDATA}/LiteLoaderQQNT Auto Patch")  # local

        # 设置快捷方式的目标路径和名称
        target = rf"{pathqq}/QQ.exe"
        shortcut_name = "QQ.lnk"
        shortcut_path = WORKDIR / shortcut_name

        # 创建快捷方式
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.path.dirname(target)
        shortcut.IconLocation = target  # 使用脚本图标
        shortcut.save()


if __name__ == "__main__":
    mklogs()
    PATHQQ = vape_qq()
    if not PATHQQ:
        sys.exit(-1)
    PATHLL = vape_ll()
    if not PATHLL:
        sys.exit(-1)
    with (PATHQQ / "resources/app/app_launcher/index.js").open(
        "w", encoding="utf-8"
    ) as fxxkqq:
        fxxkqq.write(
            f"require(String.raw`{PATHLL}`);\nrequire('./launcher.node').load('external_index', module);"
        )
    install_dbghelp(PATHQQ)
    create_shortcut(PATHQQ)
    # import subprocess 给那个不知道能不能自动退出的玩意用的
    lnk = f"{LOCALAPPDATA}/LiteLoaderQQNT Auto Patch/QQ.lnk"
    # subprocess.Popen([f"cmd /c start",dir], shell=True) 我敲这玩意不能用 不会自动退出，除非你自己关掉终端或者cmd
    os.startfile(lnk)  # os库yyds 不过这玩意是在qq的登陆界面才自动关闭的
    logging.info("正在启动QQ")
    print("正在启动 QQ")
    sys.exit(0)  # 退出终端，保留QQ
