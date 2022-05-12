# Drone.py
from djitellopy import tello

from time import sleep

drone = tello.Tello()

#start up
drone.connect()

print (drone.get_battery())

 drone.takeoff()
 drone.move_up(120)

  #forward movement lmao
 drone.move_forward(400)
 drone.move_forward(400)
sleep(.5)

 drone.flip_forward()
sleep(.5)
 #returning lmao
 drone.move_left(400)
sleep(.5)

 drone.rotate_clockwise(180)
sleep(.5)

 drone.move_forward(400)
 drone.move_forward(400)
sleep(.5)

 drone.move_left(400)
sleep(.5)

 #landing...      lmao
 drone.land()
