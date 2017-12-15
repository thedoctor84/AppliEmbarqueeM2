import wheel
import sensor
import time

def test1():

	wheel.turnAllWheels(True)

	direction = True

	while 1:

		distance = sensor.getDistance(direction)

		print("distance : " + str(distance) + "m")

		if 0 <= distance and distance <= 0.2:

			wheel.stopAllWheels()

			time.sleep(1)

			# affichage
			if direction:
				print("Obstacle a lavant - Le robot repart a larriere")
			else:
				print("Obstacle a larriere - Le robot repart a lavant")

			direction = not direction

			wheel.turnAllWheels(direction)