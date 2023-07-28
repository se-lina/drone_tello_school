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
# 以下を編集して障害物の間をジグザグに飛行させよう

# x軸方向に50cm, y軸方向に50cmの地点へ移動
tello.go_xyz_speed(50, 50, 0, 100)

# x軸方向に-100cm, y軸方向に100cmの地点へ移動
tello.go_xyz_speed(-100, 100, 0, 100)

# x軸方向に100cm, y軸方向に100cmの地点へ移動
tello.go_xyz_speed(100, 100, 0, 100)

# x軸方向に50cm, z軸方向に50cmの地点へ移動
tello.go_xyz_speed(50, 50, 0, 100)

###########################

# Telloを着陸させる
tello.land()

# Telloとの接続を解除
tello.end()
