import serial

def main():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	while 1:
		print ser.readline()

if __name__ == "__main__":
	main()
