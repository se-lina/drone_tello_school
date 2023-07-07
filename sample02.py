# 2ｍ正方形を移動させますが、コードは前進のみのコードで移動させますが、角っこに来たときはTelloを90度方向転回させ、四角を一周させるプログラム

from djitellopy import Tello  
import time  
  
# Telloオブジェクトを作成  
tello = Tello()  
  
# Telloに接続  
tello.connect()  
  
# Telloのバッテリー残量を確認  
print(f"Tello battery: {tello.get_battery()}")  
  
# Telloを離陸させる  
tello.takeoff()  
  
# Telloを2m前進させる  
tello.move_forward(200)  
  
# Telloを右に90度回転させる  
tello.rotate_clockwise(90)  
  
# Telloを2m前進させる  
tello.move_forward(200)  
  
# Telloを右に90度回転させる  
tello.rotate_clockwise(90)  
  
# Telloを2m前進させる  
tello.move_forward(200)  
  
# Telloを右に90度回転させる  
tello.rotate_clockwise(90)  
  
# Telloを2m前進させる  
tello.move_forward(200)  
  
# Telloを右に90度回転させる  
tello.rotate_clockwise(90)  
  
# Telloを着陸させる  
tello.land()  
  
# Telloとの接続を切断  
tello.end()  
