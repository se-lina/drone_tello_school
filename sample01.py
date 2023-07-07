# 離陸後、上昇1m・下降1m・前進1m・後進1m・右に移動1m・左に移動1m のプログラム

from djitellopy import Tello  
import time  
  
# Telloオブジェクトを作成  
tello = Tello()  
  
# Telloに接続  
tello.connect()  
  
# Telloを離陸させる  
tello.takeoff()  
  
# 上昇1m  
tello.move_up(100)  
  
# 下降1m  
tello.move_down(100)  
  
# 前進1m  
tello.move_forward(100)  
  
# 後進1m  
tello.move_back(100)  
  
# 右に移動1m  
tello.move_right(100)  
  
# 左に移動1m  
tello.move_left(100)  
  
# Telloを着陸させる  
tello.land()  
  
# Telloとの接続を解除  
tello.end()  
