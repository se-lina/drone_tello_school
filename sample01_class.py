# 動き：上昇1m・下降1m・前進1m・後進1m・右進1m・左進1m  

from djitellopy import Tello  
import time  
  
# Telloを制御するためのクラス  
class TelloController:  
    def __init__(self):  
        self.drone = Tello()  
          
    # Telloを離陸させる  
    def takeoff(self):  
        self.drone.takeoff()  
          
    # Telloを着陸させる  
    def land(self):  
        self.drone.land()  
          
    # Telloを前進させる  
    def forward(self, distance):  
        self.drone.move_forward(distance)  
          
    # Telloを後進させる  
    def back(self, distance):  
        self.drone.move_back(distance)  
          
    # Telloを左に移動させる  
    def left(self, distance):  
        self.drone.move_left(distance)  
          
    # Telloを右に移動させる  
    def right(self, distance):  
        self.drone.move_right(distance)  
          
    # Telloを上昇させる  
    def up(self, distance):  
        self.drone.move_up(distance)  
          
    # Telloを下降させる  
    def down(self, distance):  
        self.drone.move_down(distance)  
          
    # Telloを制御するメインの関数  
    def control(self):  
        self.drone.connect()  
          
        self.takeoff()  
        time.sleep(5)  
          
        self.up(100)  
        time.sleep(5)  
          
        self.down(100)  
        time.sleep(5)  
          
        self.forward(100)  
        time.sleep(5)  
          
        self.back(100)  
        time.sleep(5)  
          
        self.right(100)  
        time.sleep(5)  
          
        self.left(100)  
        time.sleep(5)  
          
        self.land()  
        time.sleep(5)  
          
        self.drone.end()  
          
# Telloを制御するためのインスタンスを作成して、制御する  
if __name__ == '__main__':  
    controller = TelloController()  
    controller.control()  
