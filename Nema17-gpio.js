var DIR = new Gpio(17, 'out'); 
var STEP = new Gpio(17, 'out'); 
var ENA = new Gpio(17, 'out'); 

var FastSpeed = 0.00005 
var LowSpeed = 0.00045


var nemaRun = setInterval(nema, FastSpeed); //run the blinkLED function every 250ms

function nema() { //function to start blinking
  if (LED.readSync() === 0) { //check the pin state, if the state is 0 (or off)
    LED.writeSync(1); //set pin state to 1 (turn LED on)
  } else {
    LED.writeSync(0); //set pin state to 0 (turn LED off)
  }
}

function endBlink() { //function to stop blinking
  clearInterval(blinkInterval); // Stop blink intervals
  LED.writeSync(0); // Turn LED off
  LED.unexport(); // Unexport GPIO to free resources
}

setTimeout(endBlink, 5000); //stop blinking after 5 seconds