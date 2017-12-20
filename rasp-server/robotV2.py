import wheel_v2 as wheel
import sensor
import time

class Robot:

	direction = ""

	def __init__():

		wheel.updateDirection("forward")
		wheel.stopAll()


	def updateAngle(angle, strength):

		if angle < 90:

			if direction != "forward":

				changeDirection(True)

			newTarget = mapInterval(angle, 0, 90, 0, 1000) * strength / 100

			wheel.setTargetSpeed(0, newTarget)
			wheel.setTargetSpeed(1, 1000)
			wheel.setTargetSpeed(2, 1000)
			wheel.setTargetSpeed(3, newTarget)

		elif angle < 180:

			if direction != "forward":

				changeDirection(True)

			newTarget = mapInterval(angle, 180, 90, 0, 1000) * strength / 100

			wheel.setTargetSpeed(0, 1000)
			wheel.setTargetSpeed(1, newTarget)
			wheel.setTargetSpeed(2, newTarget)
			wheel.setTargetSpeed(3, 1000)


		elif angle < 270:

			if direction == "forward":

				changeDirection(False)

			newTarget = mapInterval(angle, 180, 270, 0, 1000) * strength / 100

			wheel.setTargetSpeed(0, 1000)
			wheel.setTargetSpeed(1, newTarget)
			wheel.setTargetSpeed(2, newTarget)
			wheel.setTargetSpeed(3, 1000)

		else:

			if direction == "forward":

				changeDirection(False)

			newTarget = mapInterval(angle, 360, 270, 0, 1000) * strength / 100

			wheel.setTargetSpeed(0, newTarget)
			wheel.setTargetSpeed(1, 1000)
			wheel.setTargetSpeed(2, 1000)
			wheel.setTargetSpeed(3, newTarget)


	def mapInterval(n, start1, stop1, start2, stop2):

		return ((n - start1)/(stop1 - start1)) * (stop2 - start2) + start2


	def objectDetected():

		distance = sensor.getDistance(direction == "forward")

		if 0 <= distance and distance <= 0.2:

			print("distance : " + str(distance) + "m")

			return True

		return False

