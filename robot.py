from sr import *
import time

R = Robot()

#Move forward
R.motors[0].target = 100
R.motors[1].target = 100
print "Moving forward"
time.sleep(2)

#Turn around
R.motors[0].target = 50
R.motors[1].target = -50
print "Turning"
time.sleep(2) #Just change this line until the amount it turns is about 180 degrees

#Come back
R.motors[0].target = 100
R.motors[1].target = 100
print "Moving back"
time.sleep(2)

#Stop
R.motors[0].target = 0
R.motors[1].target = 0
print "Stopping"