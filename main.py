def getAVH():
    return 0
def turnStart():
    MotorDriver.motor_run(Motor.A, Dir.FORWARD, 8)
    MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 8)
def turnStop():
    MotorDriver.motor_stop(Motor.B)
    MotorDriver.motor_stop(Motor.B)
def getDeltaH():
    return 0

def getCompH():
    return 0
def getAV():
    return 0
el = 0
input.calibrate_compass()
ch = input.compass_heading()

def on_forever():
    global el
    if input.logo_is_pressed():
        game.game_over()
    turnStart()
    getAV()
    getAVH()
    getDeltaH()
    el = input.compass_heading()
    datalogger.log(datalogger.create_cv("", 0),
        datalogger.create_cv("", 0),
        datalogger.create_cv("", 0))
basic.forever(on_forever)
