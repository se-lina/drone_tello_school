#フリップさせる動作

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
  
# 右にフリップ  
tello.flip("r")  
  
# 左にフリップ  
tello.flip("l")  
  
# 前進1m  
tello.move_forward(100)  
  
# 右に移動1m  
tello.move_right(100)  
  
# 左に移動1m  
tello.move_left(100)  
  
# 下降1m  
tello.move_down(100)  
  
# Telloを着陸させる  
tello.land()  
  
# Telloとの接続を解除  
tello.end()  
