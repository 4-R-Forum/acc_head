function getAVH () {
    return 0
}
function turnStop () {
    MotorDriver.MotorStop(Motor.B)
    MotorDriver.MotorStop(Motor.B)
}
function getDeltaH () {
    return 0
}
function turnStart () {
    MotorDriver.MotorRun(Motor.A, Dir.forward, 8)
    MotorDriver.MotorRun(Motor.B, Dir.backward, 8)
}
function getCompH () {
    return 0
}
function getAV () {
    return 0
}
let el = 0
input.calibrateCompass()
let ch = input.compassHeading()
basic.forever(function () {
    if (input.logoIsPressed()) {
        game.gameOver()
    }
    turnStart()
    getAV()
    getAVH()
    getDeltaH()
    el = input.compassHeading()
    datalogger.log(
    datalogger.createCV("", 0),
    datalogger.createCV("", 0),
    datalogger.createCV("", 0)
    )
})
