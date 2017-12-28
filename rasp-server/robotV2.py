import wheelV2 as wheel
import sensor
import time
import init

maxSpeed = 100

init.initGpio(maxSpeed)

wheel.stopAll()

direction = wheel.updateDirection("forward")

def updateAngle(angle, strength):

	global direction

	if angle <= 90:

		if direction != "forward":

			direction = wheel.updateDirection(True)

		newTarget = mapInterval(angle, 0, 90, 0, maxSpeed) * strength / 100
		print("angle:" + str(angle) + "  strength:" + str(strength) + "  maxSpeed:" + str(maxSpeed) + "  newTarget:" + str(newTarget))

		wheel.setTargetSpeed(0, newTarget)
		wheel.setTargetSpeed(1, strength)
		wheel.setTargetSpeed(2, strength)
		wheel.setTargetSpeed(3, newTarget)

	elif angle <= 180:

		if direction != "forward":

			direction = wheel.updateDirection(True)

		newTarget = mapInterval(angle, 180, 90, 0, maxSpeed) * strength / 100
		print("angle:" + str(angle) + "  strength:" + str(strength) + "  maxSpeed:" + str(maxSpeed) + "  newTarget:" + str(newTarget))

		wheel.setTargetSpeed(0, strength)
		wheel.setTargetSpeed(1, newTarget)
		wheel.setTargetSpeed(2, newTarget)
		wheel.setTargetSpeed(3, strength)


	elif angle <= 270:

		if direction == "forward":

			direction = wheel.updateDirection(False)

		newTarget = mapInterval(angle, 180, 270, 0, maxSpeed) * strength / 100
		print("angle:" + str(angle) + "  strength:" + str(strength) + "  maxSpeed:" + str(maxSpeed) + "  newTarget:" + str(newTarget))

		wheel.setTargetSpeed(0, strength)
		wheel.setTargetSpeed(1, newTarget)
		wheel.setTargetSpeed(2, newTarget)
		wheel.setTargetSpeed(3, strength)

	else:

		if direction == "forward":

			direction = wheel.updateDirection(False)

		newTarget = mapInterval(angle, 360, 270, 0, maxSpeed) * strength / 100
		print("angle:" + str(angle) + "  strength:" + str(strength) + "  maxSpeed:" + str(maxSpeed) + "  newTarget:" + str(newTarget))

		wheel.setTargetSpeed(0, newTarget)
		wheel.setTargetSpeed(1, strength)
		wheel.setTargetSpeed(2, strength)
		wheel.setTargetSpeed(3, newTarget)

	print("target  : [" + str(wheel.wheels[0]["speed"]["target"]) + ", " + str(wheel.wheels[1]["speed"]["target"]) + ", " + str(wheel.wheels[2]["speed"]["target"]) + ", " + str(wheel.wheels[3]["speed"]["target"]) + "]")


def updateSpeed():

	for m in range(0, 4):

		wheel.updateSpeed(m)

	print("current : [" + str(wheel.wheels[0]["speed"]["current"]) + ", " + str(wheel.wheels[1]["speed"]["current"]) + ", " + str(wheel.wheels[2]["speed"]["current"]) + ", " + str(wheel.wheels[3]["speed"]["current"]) + "]")
	
def mapInterval(n, start1, stop1, start2, stop2):

	#return ((n - start1)/(stop1 - start1)) * (stop2 - start2) + start2
	return int(((n - start1)/((stop1 - start1)*1.0)) * (stop2 - start2) + start2)


def objectDetected():

	distance = sensor.getDistance(direction == "forward")

	if 0 <= distance and distance <= 0.2:

		print("distance : " + str(distance) + "m")

		return True

	return False

