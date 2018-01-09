import robotV2 as robot
import sensor
import socket
import time


host = "192.168.137.199"		# Get local machine name
port = 2010						# Reserve a port for your service.

soc = socket.socket()			# Create a socket object

soc.bind((host, port))			# Bind to the port

def test():

	soc.listen(2)							# Now wait for client connection.
	print("Waiting for connection...")

	conn, addr = soc.accept()				# Establish connection with client.
	print("Got connection from ", addr)

	print("Waiting for messages...")

	stop = False

	while not stop:

		msg = conn.recv(8)
		print("msg:" + msg)

		if msg != "":

			if msg.decode("utf-8") == "stop!!!\n":

				stop = True

			else:

				msg = msg.decode("utf-8").strip()

				spltMsg = msg.split("\n")
				print(spltMsg)

				result = spltMsg[len(spltMsg)-2].split(";")
				print(result)

				if robot.objectDetected():

					robot.forceStop()

				else:
					
					try:
						robot.updateAngle(int(result[0]), int(result[1]))
					except ValueError:
						pass

		robot.updateSpeed()

		time.sleep(0.25)

	soc.close()			# Closes the socket

	test()				# Relaunches the server socket