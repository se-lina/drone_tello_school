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
# 以下を編集して地点Aから地点Bヘ移動しよう

# 50cm前に進む
tello.move_forward(50)

# 50cm左に進む
tello.move_left(50)

###########################

# Telloを着陸させる
tello.land()

# Telloとの接続を解除
tello.end()
