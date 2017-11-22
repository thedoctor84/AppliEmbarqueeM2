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

def getDistance(front):

	if front:
		position = "front"

	else:
		position = "back"


	wp.digitalWrite(pins[position]["trigger"], 1)
	time.sleep(0.00001)
	wp.digitalWrite(pins[position]["trigger"], 0)

	start = time.time()

	while time.time() - start < 0.2:

		if wp.digitalRead(pins[position]["echo"]) == 1:

			timeInterval = time.time() - start

			return soundSpeed * timeInterval / 2

	return -1
