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
# 以下を編集して地点Aから地点Cヘ前進のみで移動しよう
# 適宜、方向転換をしよう

# 反時計回りに135°回転する
tello.rotate_counter_clockwise(135)

# 50cm前に進む
tello.move_forward(50)

###########################
# 以下は編集不要の処理です

# 地点CにTelloを着陸させる
tello.land()

# 地点CからTelloを離陸させる
tello.takeoff()

###########################
# 以下を編集して地点Cから地点Bヘ前進のみで移動しよう
# 適宜、方向転換の処理を使用しよう

# 時計回りに90°回転する
tello.rotate_clockwise(90)

# 50cm前に進む
tello.move_forward(50)

###########################

# Telloを着陸させる
tello.land()

# Telloとの接続を解除
tello.end()
