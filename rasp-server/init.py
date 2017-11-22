import wiringpi as wp
def initGpio():
	wp.wiringPiSetupPhys()

	# M3 Avant gauche
	wp.pinMode(11,1)
	wp.pinMode(13,1)
	wp.pinMode(15,1)

	# M2 Arriere gauche
	wp.pinMode(19,1)
	wp.pinMode(21,1)
	wp.pinMode(23,1)

	# M4 Avant droit
	wp.pinMode(22,1)
	wp.pinMode(24,1)
	wp.pinMode(26,1)

	# M1 Arriere droit
	wp.pinMode(36,1)
	wp.pinMode(38,1)
	wp.pinMode(40,1)

	# On fixe les pin echo en IN pour les telemetres
	wp.pinMode(33,0)
	wp.pinMode(35,0)

initGpio()
