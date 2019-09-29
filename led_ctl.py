import sys, time
import RPi.GPIO as GPIO

redPin = 11
greenPin = 13
bluePin = 15

# Two different modes for GPIO:  BOARD uses raw pin on the header.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def print_valid_commands():
  print("Valid Commands:")
  print("red on")
  print("red off")
  print("green on")
  print("green off")
  print("blue on")
  print("blue off")
  print("q to quit")

print_valid_commands()
while True:
  command = raw_input("enter command:\n")
  command = command.split(" ")
  if (command[0] == "red"):
    pin = redPin
  elif (command[0] == "green"):
    pin = greenPin
  elif (command[0] == "blue"):
    pin = bluePin
  elif (command[0] == "q"):
    exit(1)
  else:
    print("unrecognized command")
    print_valid_commands()
    continue

  if (command[1] == "on"):
    value = GPIO.HIGH
  elif (command[1] == "off"):
    value = GPIO.LOW
  else:
    print("unrecognized command")
    print_valid_commands()
    continue

  GPIO.output(pin, value)
  
