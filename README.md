# TE2003B.1

Authors : Alan Mondragón & Franco Minutti

This proyect is a calculator made with an ATMEGA328P, mounted in an arduino,
and a raspberry pi, running integrated with python Raspberry Pi OS integrated 
with python, the ATMEGA328P was programed using microchip studio.

The other components used are a 4x4 keypad and a oled display.

Also has the next characteristics:

The 16-key matrix numeric keypad follows the following functionality:

The "A" key is for the sum operation
The "B" key is for the subtraction operation
The "C" key is for the multiplication operation
The "D" key is for division operation
The "*" key is for decimal point
The "#" key is to show the result of the operation performed ("=")
2. The keyboard must be monitored using the ATMEGA328P under the following restrictions:

Uses the Ports 4 to 7 in PORTD and has internal pull-ups, for the columns 
And Uses the Ports 0 to 3 in PORTB, for the rows
Keyboard scan as routine for attention to interruption due to change in input pins
Optionally for the development of the activity, LEDs in PORTC for monitoring variables
See wiring diagram for keyboard (and optional LEDs) (Links to an external site.)

Also uses a 9600 baudrate

And the information received must be displayed horizontally and without line breaks.
Only a line break is printed when it is requested to show the result of the operation

