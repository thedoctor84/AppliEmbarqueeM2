import wiringpi as wp

# [ PWM , Avant, Arriere]
wheels = [
	[36, 40, 38],
	[19, 21, 23],
	[11, 15, 13],
	[22, 24, 26]
]

wp.wiringPiSetupPhys()

def stopWheel(m):

	for i in range(0, 3):

		wp.digitalWrite(wheels[m-1][i], 0)

	print("> wheel " + str(m) + " stopped")


def stopAllWheels():
	
	for i in range(1, 5):

		stopWheel(i)


def turnWheel(m, forward):

	wp.digitalWrite(wheels[m-1][0], 1)

	if forward:

		wp.digitalWrite(wheels[m-1][1], 1)
		wp.digitalWrite(wheels[m-1][2], 0)

		print("> wheel " + str(m) + " (pin " + str(wheels[m-1][1]) + ") turning forward")

	else:

		wp.digitalWrite(wheels[m-1][1], 0)
		wp.digitalWrite(wheels[m-1][2], 1)

		print("> wheel " + str(m) + " (pin " + str(wheels[m-1][2]) + ") turning backward")


def turnAllWheels(forward):

	for i in range(1, 5):

		turnWheel(i, forward)
