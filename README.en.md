# THE IDOLM@STER MILLION LIVE! THEATER DAYS Preregistration Tool

![THE IDOLM@STER MILLION LIVE! THEATER DAYS](https://millionlive.idolmaster.jp/theaterdays/images/t/t01.png)

THE IDOLM@STER MILLION LIVE! THEATER DAYS Preregistration Tool. Use this tool to registrate multiple mail addresses in one click.

This tool is not a mail address generator. Please prepare the mail addresses beforehand.

Read this page in other languages: [日本語](README.md), [正體中文](README.zh-tw.md).

## How to use

### Windows

1. Download `MillionLiveTheaterDaysPreregistrationTool-windows.zip` from the [releases page](https://github.com/areong/MillionLiveTheaterDaysPreregistrationTool/releases/latest) and then unpack it.
2. Input the mail addresses in `mail_addresses.txt`. Please input one mail address per one line. For example:

```
Kotori_Otonashi@765pro.com
Misaki_Aoba@765pro.com
```

3. Run `registrator.exe`. After the registration completes, click enter to terminate the program.
4. Find other mail addresses and go back to step 2.

### Other platforms

Stand-alone executables are not available yet. Use Python to run this tool.

1. Install Python 3.
2. Download `Source code` from the [releases page](https://github.com/areong/MillionLiveTheaterDaysPreregistrationTool/releases/latest) and then unpack it.
3. Input the mail addresses in `src/mail_addresses.txt`. Please input one mail address per one line. For example:

```
Kotori_Otonashi@765pro.com
Misaki_Aoba@765pro.com
```

4. In `src` folder, input the following command in the terminal:

```
python registrator.py
```

5. After the registration completes, click enter to terminate the program.
6. Find other mail addresses and go back to step 3.