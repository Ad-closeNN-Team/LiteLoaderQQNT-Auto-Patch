> [!CAUTION]
> 2024/8/12 目前本程序还有些许bug，如果坚持要使用，请三思而后行！！！

# LiteLoaderQQNT Auto Patch
## 介绍
### 干啥的？
#### 一个自动安装（不是下载）LiteLoaderQQNT 的东西
> [!CAUTION]
> 如果你还不知道 [LiteLoaderQQNT](https://github.com/LiteLoaderQQNT/LiteLoaderQQNT) 是什么，建议去看看[官方网站](https://liteloaderqqnt.github.io)。

> [!IMPORTANT]
> **不是下载**而是**半自动**安装 [LiteLoaderQQNT](https://github.com/LiteLoaderQQNT/LiteLoaderQQNT)

> [!NOTE]
这个东西主要是为那些升级了 [QQNT](https://im.qq.com/pcqq/index.shtml) 的用户使用，原因是**在 Windows 版 QQNT 在升级后可能会导致已安装的补丁、 index.js 被 QQNT 自动还原，导致 LiteLoaderQQNT 无法随着 QQNT 启动（也就是用不了 LiteLoaderQQNT）**
---
### 有什么用？
在初次选择好位置 QQNT 和 LiteLoaderQQNT 后，当你的 QQ 更新后发现自己的 `index.js` 或 `dbghelp.dll`被 QQ 安装程序 修改/删除，所以可以在设置好 LiteLoaderQQNT 和 QQNT 的文件夹路径后自动把 `index.js` 纠正，重新把 `dbghelp.dll` 下载回来，重新用上 LiteLoaderQQNT
## 如何使用
> [!CAUTION]
> 教程只适用于 Windows

> [!IMPORTANT]
> 一定要使用管理员身份运行

#### 普通
- 首先，先在 [LiteLoaderQQNT Release](https://github.com/LiteLoaderQQNT/LiteLoaderQQNT/releases) 的 Latest 下载 LiteLoaderQQNT 的最新版。
- 下载并解压到你想放的任意位置（最好要有写入权限），这里以解压到`C:\`（自带有一个文件夹的）做演示。
- 使用**管理员身份**运行本程序，此时，如果弹出`选择 QQNT 的所在文件夹`对话框，请选择 `QQ.exe` 所在的文件夹，如果不知道 `QQ.exe` 在哪，请点击桌面上的QQ图标（如果有），右键，选择`打开文件位置`，将文件资源管理器上方的地址栏复制，回到对话框，把复制的地址粘贴到对话框上面的地址，选择到此文件夹即可。
- 此时应该会弹出`选择 QQNT 的所在文件夹`对话框，选择解压好的 LiteLoaderQQNT ，这里以解压到 `C:\` 为例，就在对话框的地址栏填写`C:\LiteLoaderQQNT`，点击`选择此文件夹`即可。

#### 中等（自动补丁）
- 如果你一开始已经按照上面#普通的教程弄好了必要的设置
#### 高级
- 如果你的`QQ.exe`目录下没有`dbghelp.dll`这个补丁文件（用来绕过QQ文件完整性校验，GitHub仓库地址：[DLLHijackMethod](https://github.com/LiteLoaderQQNT/QQNTFileVerifyPatch/tree/DLLHijackMethod)），程序会自动下载并打上补丁。在选择框内按 `1` 即可。如果你**使用其他的绕过完整性校验的方法**，那你可以选择按 `2`（仅这次跳过）或者按 `3`（永久跳过，除非你删掉了本程序生成的如下存储文件`Install_cancel_skip.ini`或将其内容改为除`1`以外的字符）
- 本程序会自动生成一些文件供存储内容，包括：
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
# 救回我失误的操作
如果你因为某种原因导致输入的 LiteLoaderQQNT 或 QQNT 的目录失效，你可以用**手动**或**对话**两种方式就回失败的操作：

- 手动：来到 `[系统盘符]:\Users\\[用户名]\Appdata\Local\LiteLoaderQQNT Auto Patch` 里，打开文件，如果你是QQNT位置错误请打开`QQNT_file_path.ini`，如果是LiteLoaderQQNT位置错误请打开`LiteLoaderQQNT_file_path.ini`，并直接写入文件夹的位置（不带引号）
- 自动：删除`QQNT_file_path.ini`和`LiteLoaderQQNT_file_path.ini`两个文件，并打开程序，会重新要求选择位置，这时重新选择位置即可。
