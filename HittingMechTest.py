while (True):
    print "Forward! "
    myMotor.run(Adafruit_MotorHAT.FORWARD)

    print "\tSpeed up..."
  # This will loop from 0-254
    for i in range(255):
        myMotor.setSpeed(i)
    # It will stop 10 ms
        time.sleep(0.01)

    print "\tSlow down..."
  # This will loop from 244-0
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "Backward! "
    myMotor.run(Adafruit_MotorHAT.BACKWARD)

    print "\tSpeed up..."
    for i in range(255):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "\tSlow down..."
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "Release"
    myMotor.run(Adafruit_MotorHAT.RELEASE)
    time.sleep(1.0)
