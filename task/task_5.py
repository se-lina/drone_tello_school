# 作成 Keio SFC K.Y.
# djitellopyをインポート
from djitellopy import Tello
  
# Telloオブジェクトを作成
tello = Tello()

# Telloに接続
tello.connect()

# Telloのバッテリー残量を確認  
print(f"Tello battery: {tello.get_battery()}")

# Telloを離陸させる
tello.takeoff()

###########################
# 以下を編集して三角形を描くように飛行させよう
# 以下は菱形を描くように飛行します

# x軸方向に75cm, z軸方向に50cmの地点へ移動
tello.go_xyz_speed(75, 0, 50, 100)

# x軸方向に-75cm, z軸方向に50cmの地点へ移動
tello.go_xyz_speed(-75, 0, 50, 100)

# x軸方向に-75cm, z軸方向に-50cmの地点へ移動
tello.go_xyz_speed(-75, 0, -50, 100)

# x軸方向に75cm, z軸方向に-50cmの地点へ移動
tello.go_xyz_speed(75, 0, -50, 100)

###########################

# Telloを着陸させる
tello.land()

# Telloとの接続を解除
tello.end()
