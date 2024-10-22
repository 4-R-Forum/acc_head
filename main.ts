function getAVH(): number {
    return 0
}

function turnStop() {
    
}

function getDeltaH(): number {
    return 0
}

function turnStart() {
    
}

function getCompH(): number {
    return 0
}

function getAV(): number {
    return 0
}

let el = 0
input.calibrateCompass()
let ch = input.compassHeading()
basic.forever(function on_forever() {
    
    if (input.logoIsPressed()) {
        game.gameOver()
    }
    
    turnStart()
    getAV()
    getAVH()
    getDeltaH()
    el = input.compassHeading()
    datalogger.log(datalogger.createCV("", 0), datalogger.createCV("", 0), datalogger.createCV("", 0))
})
