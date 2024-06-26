# 概要
小型ドローンTelloをPythonで動かすためのコードをここにまとめる。  
対象は高校生向けの内容でまとめる。

## 資料
### 2024年版の資料①  
https://docs.google.com/presentation/d/1rVryUykVmGGIHk4wH3srW5bPtVJWOZo_5qriSW9f9Xs/edit#slide=id.p

### 202年版の資料②
#### Microsoft VS codeのインストールおよび事前準備について
https://www.python.jp/python_vscode/windows/setup/install_vscode.html

#### Python入門ガイド
https://github.com/se-lina/drone_tello_school/blob/main/Python_basis.md

#### djitellopyのインストール方法
https://github.com/se-lina/drone_tello_school/blob/main/difference_djitellopy_tellopy.md

#### ドローンを動かすためのプログラム
皆さんは、この項目をみて、数字や移動に関するプログラムを書き換えしてドローンを動かしてください。  
**※今日はここが重要！**  
https://github.com/se-lina/drone_tello_school/blob/main/how_to_move.md

#### タスク（課題）表
https://github.com/se-lina/drone_tello_school/blob/main/taskcard_0729.pdf


#### タスクサンプル
1. 月面着陸  
https://github.com/se-lina/drone_tello_school/blob/main/task_1.py  
2. ちょっと寄り道  
https://github.com/se-lina/drone_tello_school/blob/main/task_2.py  
3. 体操選手  
https://github.com/se-lina/drone_tello_school/blob/main/task_3.py  
4. 前進あるのみ  
https://github.com/se-lina/drone_tello_school/blob/main/task_4.py  
5. 夏の大三角  
https://github.com/se-lina/drone_tello_school/blob/main/task_5.py  
6. サッカー選手  
https://github.com/se-lina/drone_tello_school/blob/main/task_6.py  


## パソコンでTelloを動かすための流れ
1. Microsoft VS codeで動かすためのPythonを開く
2. Telloの電源を入れる
4. PCとTelloをWiFiでつなぐ（自分が動かすTelloの番号を要確認）
5. VS code内の`実行ボタン`を押す
6. プログラムが動かない。または、強制終了させたい場合は`control + C　`を押す


## 使用機材
### PC
Window, Mac, Linuxどれでも大丈夫だが、Python3が動く環境であること
### ドローン
使用するドローンはTello  
Amazon等で13000円前後で購入でき、スマートフォンのアプリでラジコンのように動かすことが出来る。  
重さが80gのため、「航空法」の対象外になります。  
とは言え、外で飛行させる場合は、所々確認して飛ばしましょう。  


## 関連資料
### djitellopyのインストール方法
https://github.com/se-lina/drone_tello_school/blob/main/difference_djitellopy_tellopy.md

### 参照ブログ  
https://se-lina.hatenablog.com/entry/2020/08/16/110723

### TelloのSDKを翻訳したPDF  
https://drive.google.com/file/d/1A51f-5HK5fq4YfiIR4Anun4DD8ERRtR3/view?usp=sharing  
(2022/10/19 ファイル場所変更)
