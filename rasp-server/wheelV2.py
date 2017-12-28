import wiringpi as wp

wheels = [
	{
		"speed": {
			"current":  0,
			"target": 	0
		},
		"pins": {
			"pwm": 	 	36,
			"forward": 	40,
			"backward": 38
		}
	},
	{
		"speed": {
			"current":  0,
			"target": 	0
		},
		"pins": {
			"pwm": 	 	19,
			"forward": 	21,
			"backward":	23
		}
	},
	{
		"speed": {
			"current":  0,
			"target": 	0
		},
		"pins": {
			"pwm": 	 	11,
			"forward": 	15,
			"backward":	13
		}
	},
	{
		"speed": {
			"current":  0,
			"target": 	0
		},
		"pins": {
			"pwm": 	 	22,
			"forward": 	24,
			"backward":	26
		}
	}
]

wp.wiringPiSetupPhys()

transitionSpeed = 10

def updateDirection(forward):

	if forward:

		for i in range(0, 4):

			wp.digitalWrite(wheels[i]["pins"]["forward"],  1)
			wp.digitalWrite(wheels[i]["pins"]["backward"], 0)

		print("going forward")

		return "forward"

	else:

		for i in range(0, 4):

			wp.digitalWrite(wheels[i]["pins"]["forward"],  0)
			wp.digitalWrite(wheels[i]["pins"]["backward"], 1)

		print("going backward")
		
		return "backward"



def setTargetSpeed(m, newTarget):

	wheels[m]["speed"]["target"] = newTarget


def updateSpeed(m):
	
	if wheels[m]["speed"]["current"] < wheels[m]["speed"]["target"]:

		wheels[m]["speed"]["current"] = min(wheels[m]["speed"]["current"] + transitionSpeed, wheels[m]["speed"]["target"])

	elif wheels[m]["speed"]["current"] > wheels[m]["speed"]["target"]:

		wheels[m]["speed"]["current"] = max(wheels[m]["speed"]["current"] - transitionSpeed, wheels[m]["speed"]["target"])

	else:
		return

	setPWM(m, wheels[m]["speed"]["current"])
	

def setPWM(m, pwm):

	wp.softPwmWrite(wheels[m]["pins"]["pwm"], pwm)

	#print("m:" + str(m) + "  pwm:" + str(pwm))


def stopAll():
	
	for m in range(0, 4):

		print("#setPWM(m, 0)")

	print("> wheels stopped")
