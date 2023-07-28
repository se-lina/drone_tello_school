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
# 以下を編集して4回連続でフリップさせよう

# 前にフリップする
tello.flip("f")

# fはforwardのことです
# fをlに変えると左、rに変えると右、bに変えると後ろにフリップします

###########################

# Telloを着陸させる
tello.land()

# Telloとの接続を解除
tello.end()
