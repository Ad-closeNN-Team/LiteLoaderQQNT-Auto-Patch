> [!IMPORTANT]
> 2024/8/14 目前下载补丁的方式为直接通过请求 GitHub API 和下载 GitHub 直链的文件，请确保你当前的网络环境可以直连 GitHub ，如果无法保证，请在遇到下载错误时过几分钟再尝试

# LiteLoaderQQNT Auto Patch
## 介绍
### 干啥的？
#### 一个（半）自动安装（不是下载）LiteLoaderQQNT 的东西
> [!CAUTION]
> 如果你还不知道 [LiteLoaderQQNT](https://github.com/LiteLoaderQQNT/LiteLoaderQQNT) 是什么，建议去看看[官方网站](https://liteloaderqqnt.github.io)。

> [!NOTE]
这个程序主要是为那些升级了 [QQNT](https://im.qq.com/pcqq/index.shtml) 的用户使用，原因是**在 Windows 版 QQNT 在升级后可能会导致已安装的补丁、 index.js 被 QQNT 自动还原，导致 LiteLoaderQQNT 无法随着 QQNT 启动（也就是用不了 LiteLoaderQQNT）**
#### 本程序会自动生成一些文件供存储内容，包括：
> [!NOTE]
> 所有的文件和 Logs 文件夹均存放在 [系统盘符]:\Users\\[用户名]\Appdata\Local\LiteLoaderQQNT Auto Patch 里

```
1.log 日志文件：以日期为名，以 .ini 为后缀（年-月-日，如 2024-08-12）
2.QQNT（QQ.exe）的路径：用于提供操作的路径
3.LiteLoaderQQNT 的路径：用于下次在QQ升级时打开 index.js 并填充相关位置，比如
require(String.raw`C:/LiteLoaderQQNT`);
中的 LiteLoaderQQNT 的位置
4.询问补丁是否跳过的文件（Install_cancel_skip.ini）：用于检查是否希望永久跳过检测dbghelp.dll
5.QQ.exe的lnk（快捷方式）文件：用于自动启动QQ
6.Logs 文件夹：存放日志文件
7.整个 LiteLoaderQQNT Auto Patch 文件夹：存放上述所用的所有文件和文件夹
```
---
---
### 有什么用？
在初次选择好位置 QQNT 和 LiteLoaderQQNT 后，当你的 QQ 更新后发现你可能会发现自己的 `index.js` 或 `dbghelp.dll`被 QQ 的安装程序 修改/删除，就可以打开本程序，在设置好 LiteLoaderQQNT 和 QQNT 的文件夹路径的前提下自动把 `index.js` 纠正，重新把 `dbghelp.dll` 下载回来，并放入 QQNT 目录里，让你重新用上 LiteLoaderQQNT

---

## 如何使用
> [!CAUTION]
> 教程只适用于 **Windows 64位** 或 **Windows 32位**

> [!IMPORTANT]
> 一定要使用**管理员身份**运行

#### 选择位置（单次使用）
- 首先，先在 [LiteLoaderQQNT Release](https://github.com/LiteLoaderQQNT/LiteLoaderQQNT/releases) 的 Latest 下载 LiteLoaderQQNT 的最新版。
- 下载并解压到你想放的任意位置（最好要有写入权限），这里以解压到`C:\`（自带有一个文件夹，也就是我一会要选的路径为`C:\LiteLoaderQQNT`）做演示。
- 使用**管理员身份**运行本程序，此时，如果弹出`选择 QQNT 的所在文件夹`对话框，请选择 `QQ.exe` 所在的文件夹，如果不知道 `QQ.exe` 在哪，请点击桌面上的QQ图标（如果有），右键，选择`打开文件位置`，将文件资源管理器上方的地址栏复制，回到对话框，把复制的地址粘贴到对话框上面的地址，选择到此文件夹即可。
- 此时应该会弹出`选择 QQNT 的所在文件夹`对话框，选择解压好的 LiteLoaderQQNT ，这里以解压到 `C:\` 为例，就在对话框的地址栏填写`C:\LiteLoaderQQNT`，点击`选择此文件夹`即可。

> [!WARNING]
> 如果你不小心把 QQNT 文件夹或 LiteLoaderQQNT 文件夹的位置选错了，请看下方 # 救回我失误的操作 。
#### 自动补丁（持续使用）
- 如果你一开始已经按照上面 [#选择位置](#选择位置单次使用) 的教程弄好了必要的设置（也就是选择那两个文件夹）
- 如果你的`QQ.exe`目录下没有`dbghelp.dll`这个补丁文件（用来绕过QQ文件完整性校验，来自于 LiteLoaderQQNT 官方 GitHub仓库地址：[DLLHijackMethod](https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/tree/DLLHijackMethod)），程序会自动下载并打上补丁。在选择框内按 `1` 即可。如果你**使用其他的绕过完整性校验的方法**，那你可以选择按 `2`（仅这次跳过）或者按 `3`（永久跳过，除非你删掉了本程序生成的如下存储文件`Install_cancel_skip.ini`或将其内容改为除`1`以外的字符）
#### 推荐
- 如果可以的话，可以将本程序直接**固定到 "开始" 菜单**，等下次 QQ 更新后发现 QQ说 **"文件已损坏，请重新安装QQ"** 的时候就可以点击 "确定" ，打开 **"开始" 菜单**，**单击**本程序的图标，这时候程序就会自动开始修补（**下载dbghelp.dll**+**改名**并**复制**到与 QQ.exe 同目录下）了。当一切准备就绪的时候，你无需再次手动重启 QQ ，程序会自动启动 QQ 。
# 救回我失误的操作
如果你因为某种原因导致输入的 LiteLoaderQQNT 或 QQNT 的目录失效，你可以用**手动**或**对话**两种方式就回失败的操作：

- 手动：来到 `[系统盘符]:\Users\\[用户名]\Appdata\Local\LiteLoaderQQNT Auto Patch` 里，打开文件，如果你是QQNT位置错误请打开`QQNT_file_path.ini`，如果是LiteLoaderQQNT位置错误请打开`LiteLoaderQQNT_file_path.ini`，并直接写入文件夹的位置（不带引号）
- 自动：删除`QQNT_file_path.ini``QQ.exe.lnk`（那个快捷方式）和`LiteLoaderQQNT_file_path.ini`这三个文件，并打开程序，会重新要求选择位置，这时重新选择位置即可。

# Q&A
### Q: 打开exe后提示"Windows 已保护你的电脑"怎么办？
A:请点击`更多信息`，点击下方的`仍要运行`即可。没毒就是没毒，如果你**不信任**本程序，请立即将它从你的电脑删除。
![WDS](https://cdn.jsdelivr.net/gh/Ad-closeNN-Team/LiteLoaderQQNT-Auto-Patch@main/doc/WDS.png)
![WDS RUN](https://cdn.jsdelivr.net/gh/Ad-closeNN-Team/LiteLoaderQQNT-Auto-Patch@main/doc/WDS%20RUN.png)

---

### Q: 提示下载失败，状态码什么什么
A: 请确保你当前的网络环境能直连 GitHub API([api.github.com](https://api.github.com)) 和 GitHub([github.com](https://github.com)) 。如果不使用 "魔法" ，可能需要过几分钟才能连接上。

---

#### Q: 打开QQ发现dbghelp.dll没有被指定在 Windows 上运行
A: 多半是你下到的文件和 GitHub 上的不一样了，如果你发现那个`dbghelp.dll`只有几KB大小（比如5.41KB）而不是正常的几百KB（比如372KB），那么这很可能是一个网页（告诉你哪里错误了），如果你觉得这是一个网页，请将`dbghelp.dll`重命名为`dbghelp.html`并用浏览器打开它。