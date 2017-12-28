import wiringpi as wp
	
wp.wiringPiSetupPhys()

def initGpio(maxSpeed):

	# M3 Avant gauche
	wp.pinMode(11,1)
	wp.pinMode(13,1)
	wp.pinMode(15,1)
	wp.softPwmCreate(11, 0, maxSpeed)

	# M2 Arriere gauche
	wp.pinMode(19,1)
	wp.pinMode(21,1)
	wp.pinMode(23,1)
	wp.softPwmCreate(19, 0, maxSpeed)

	# M4 Avant droit
	wp.pinMode(22,1)
	wp.pinMode(24,1)
	wp.pinMode(26,1)
	wp.softPwmCreate(22, 0, maxSpeed)

	# M1 Arriere droit
	wp.pinMode(36,1)
	wp.pinMode(38,1)
	wp.pinMode(40,1)
	wp.softPwmCreate(36, 0, maxSpeed)

	# Trigger Front
	wp.pinMode(31,1)
	# Trigger Back
	wp.pinMode(29,1)

	# On fixe les pin ECHO en IN pour les telemetres
	wp.pinMode(33,0)
	wp.pinMode(35,0)
