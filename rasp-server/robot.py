import wheel
import sensor
import time

def test1():

	#robot.turnAllWheels(True)

	direction = True

	while 1:

		distance = sensor.getDistance(direction)

		if 0 <= distance && distance <= 0.2:

			robot.stopAllWheels()

			time.sleep(1)

			# affichage
			if direction = True:
				print("Obstacle à l'avant ! Le robot repart à l'arrière...")
			else:
				print("Obstacle à l'arrière ! Le robot repart à l'avant...")

			direction = not direction

			#robot.turnAllWheels(direction)