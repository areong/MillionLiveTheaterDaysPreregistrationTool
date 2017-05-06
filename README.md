# THE IDOLM@STER MILLION LIVE! THEATER DAYS 事前登録自動ツール

![THE IDOLM@STER MILLION LIVE! THEATER DAYS](https://millionlive.idolmaster.jp/theaterdays/images/t/t01.png)

ミリオンライブ! シアターデイズの事前登録自動ツールです。複数のメールアドレスを一気に登録することができます。

このツールはメールアドレスジェネレーターではないので、登録したいメールアドレスを事前に用意してください。

ほかの言語でこのページを読みます：[正體中文](README.zh-tw.md)、[English](README.en.md)。

## 使い方

### Windows

1. [リリースページ](https://github.com/areong/MillionLiveTheaterDaysPreregistrationTool/releases/latest)から`MillionLiveTheaterDaysPreregistrationTool-windows.zip`をダウンロードして、解凍します。
2. `mail_addresses.txt`に登録したいメールアドレスを入力します。一行につき一つずつ入力してください。例：

```
Kotori_Otonashi@765pro.com
Misaki_Aoba@765pro.com
```

3. `registrator.exe`を実行します。自動登録が完了したあと、エンターキーを押してプログラムを終了します。
4. ほかのメールアドレスを探して、ステップ2からもう一度やります。

### Windows以外

Windows以外のプラットフォームのスタンドアロンアプリはまだ用意でいないけど、Pythonでこのツールを使用することができます。

1. Python 3 をインストールします。
2. [リリースページ](https://github.com/areong/MillionLiveTheaterDaysPreregistrationTool/releases/latest)から`Source code`をダウンロードして、解凍します。
3. `src/mail_addresses.txt`に登録したいメールアドレスを入力します。一行につき一つずつ入力してください。例：

```
Kotori_Otonashi@765pro.com
Misaki_Aoba@765pro.com
```

4. `src`フォルダで次のコマンドをターミナルで入力します：

```
python registrator.py
```

5. 自動登録が完了したあと、エンターキーを押してプログラムを終了します。
6. ほかのメールアドレスを探して、ステップ3からもう一度やります。
