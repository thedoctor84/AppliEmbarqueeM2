import wiringpi as wp
import time

pins = {
	"front": {
		"trigger": 31,
		"echo": 35
	},
	"back": {
		"trigger": 29,
		"echo": 33
	}
}

# vitesse en m/s
soundSpeed = 340

# distance de detection d'un obstacle
maxDistance = 0.1

def getDistance(front):

	if front:
		position = "front"

	else:
		position = "back"


	wp.digitalWrite(pins[position]["trigger"], 1)
	time.sleep(0.00001)
	wp.digitalWrite(pins[position]["trigger"], 0)

	start = time.time()
	limitNoSignal = start + 0.1

	# on considerera qu'il n'y a pas d'obstacle si un echo n'est pas recu avant 0.2s
	while start < limitNoSignal:

		start = time.time()
		# Un ECHO est recu
		if wp.digitalRead(pins[position]["echo"]) == 1:

			end = time.time()

			# On va attendre que l'echo repasse a 0
			while wp.digitalRead(pins[position]["echo"]) == 1:

				end = time.time()

			timeInterval = end - start

			return soundSpeed * timeInterval / 2

	return -1