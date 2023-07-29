# tellopyというライブラリとdjitellopyのライブラリの違い


tellopyとdjitellopyは、どちらもPythonでTelloを制御するためのライブラリですが、機能や使い方に違いがあります。

tellopyは、Telloとの通信を行うためのライブラリであり、Telloの基本的な機能を制御することができます。tellopyの機能としては、Telloの離陸、着陸、上下左右の移動、回転、カメラ映像の取得などがあります。

一方、djitellopyは、tellopyを拡張したライブラリであり、より高度な機能を提供しています。djitellopyの機能としては、Telloの姿勢制御、フライトログの取得、複数のTelloの同時制御などがあります。

また、djitellopyは、OpenCVとNumPyというライブラリを使用しているため、画像処理やデータ解析にも利用することができます。

簡単にまとめると、tellopyは基本的な制御機能を提供し、djitellopyはより高度な制御機能と画像処理機能を提供しています。


## DJI Tello ライブラリのインストール方法

Telloを制御するためには、以下の手順が必要です。   
Python 3をインストールしたパソコンにdjitellopyライブラリをインストールします。  
以下のコマンドを使用して、pipを使用してインストールできます。 
```
pip install djitellopy  
```

TelloドローンをWi-Fiで接続します。  

djitellopyをインポートして、Telloオブジェクトを作成します。 

以下は、サンプルコードです。 
```
from djitellopy import Tello  
  
tello = Tello()  
  
tello.connect()  
tello.takeoff()  
  
tello.move_left(50)  
tello.rotate_counter_clockwise(90)  
tello.move_forward(100)  
  
tello.land()  
```
これで、Telloドローンを制御するPythonプログラムを書くことができます。

