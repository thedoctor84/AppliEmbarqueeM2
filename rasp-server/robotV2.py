import wheelV2 as wheel
import sensor
import time

wheel.stopAll()

#direction = wheel.updateDirection("forward")

def updateAngle(angle, strength):

	global direction

	if angle <= 90:

		if direction != "forward":

			direction = wheel.updateDirection(True)

		newTarget = mapInterval(angle, 0, 90, 0, 1000) * strength / 100

		wheel.setTargetSpeed(0, newTarget)
		wheel.setTargetSpeed(1, 1000)
		wheel.setTargetSpeed(2, 1000)
		wheel.setTargetSpeed(3, newTarget)

	elif angle <= 180:

		if direction != "forward":

			direction = wheel.updateDirection(True)

		newTarget = mapInterval(angle, 180, 90, 0, 1000) * strength / 100

		wheel.setTargetSpeed(0, 1000)
		wheel.setTargetSpeed(1, newTarget)
		wheel.setTargetSpeed(2, newTarget)
		wheel.setTargetSpeed(3, 1000)


	elif angle <= 270:

		if direction == "forward":

			direction = wheel.updateDirection(False)

		newTarget = mapInterval(angle, 180, 270, 0, 1000) * strength / 100

		wheel.setTargetSpeed(0, 1000)
		wheel.setTargetSpeed(1, newTarget)
		wheel.setTargetSpeed(2, newTarget)
		wheel.setTargetSpeed(3, 1000)

	else:

		if direction == "forward":

			direction = wheel.updateDirection(False)

		newTarget = mapInterval(angle, 360, 270, 0, 1000) * strength / 100

		wheel.setTargetSpeed(0, newTarget)
		wheel.setTargetSpeed(1, 1000)
		wheel.setTargetSpeed(2, 1000)
		wheel.setTargetSpeed(3, newTarget)

def updateSpeed():

	for m in range(0, 4):

		wheel.updateSpeed(m)


def mapInterval(n, start1, stop1, start2, stop2):

	return ((n - start1)/(stop1 - start1)) * (stop2 - start2) + start2


def objectDetected():

	distance = sensor.getDistance(direction == "forward")

	if 0 <= distance and distance <= 0.2:

		print("distance : " + str(distance) + "m")

		return True

	return False

