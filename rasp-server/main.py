import robotV2 as robot
import socket
import time


host = "192.168.137.199"		# Get local machine name
port = 2010						# Reserve a port for your service.

soc = socket.socket()			# Create a socket object

soc.bind((host, port))			# Bind to the port

def test():

	soc.listen(2)				# Now wait for client connection.
	print("Waiting for connection...")

	conn, addr = soc.accept()	# Establish connection with client.
	print("Got connection from ", addr)

	print("Waiting for messages...")

	while True:

		msg = conn.recv(8)
		print("msg:" + msg)

		if msg != "":

			msg = msg.decode("utf-8").strip()

			spltMsg = msg.split("\n")
			print(spltMsg)

			result = spltMsg[len(spltMsg)-2].split(";")
			print(result)

			try:
				robot.updateAngle(int(result[0]), int(result[1]))
			except ValueError:
				pass

		robot.updateSpeed()

		time.sleep(0.25)