<?php
	$command = escapeshellcmd('python /home/pi/tensorflowRaspberry/tensorflow-image-classifier/classify.py /dev/shm/mjpeg/cam.jpg');
	$output = shell_exec($command);
	echo $output;
?>
