# Upload this Sketch to an Arduino which in turn has a LPD8806 
# addressable LED RGB Light Strip attached to it. The Arduino
# receives an INT and displays that value onto the LED Strip
# In my case the LED Strip has 60 LEDs attached to it, and i 
# allow the Pollution index to be from 0 to 200;

#include "LPD8806.h"
#include "SPI.h"

int dataPin = 11;
int clockPin = 13;

unsigned long timeout = 60000*2;
unsigned long timestamp = millis();

LPD8806 strip = LPD8806(60, dataPin, clockPin);

void setup() {
	strip.begin();
	strip.show();

	Serial.begin(9600);
	delay(100);
	Serial.println("Reset");

	/*
		strip.setPixelColor(6,strip.Color(3,2,0)); // yellow
		strip.setPixelColor(7,strip.Color(4,1,0)); // orange
		strip.setPixelColor(8,strip.Color(5,0,0)); // red
		strip.setPixelColor(9,strip.Color(5,0,2)); // magenta
		strip.show();
		while(1){}
	*/
}


void loop() { 
	while(Serial.available()>0){
		int data = Serial.parseInt();

		if(data > 239){
			data = 239;
		}
		if(data < 0){
			data = 0;
		}

		int data_mapped = map(data, 0, 239, 0, 59); 

		Serial.print(data);
		Serial.print(" = ");
		Serial.println(data_mapped);

		if (Serial.read() == '\n') {
			timestamp = millis();
			for (int i = strip.numPixels(); i >= data_mapped; i--) {
				strip.setPixelColor(i,strip.Color(0,0,0));
				strip.show();
			}

			for (int i=0; i <= data_mapped; i++){
				switch(i){
					case 0:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 1:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 2:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 3:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 4:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 5:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 6:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 7:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 8:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 9:
						strip.setPixelColor(i,strip.Color(0,5,0));
						break;
					case 10:
						strip.setPixelColor(i,strip.Color(1,4,0));
						break;
					case 11:
						strip.setPixelColor(i,strip.Color(2,3,0));
						break;
					case 12:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 13:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 14:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 15:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 16:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 17:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 18:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 19:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 20:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 21:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 22:
						strip.setPixelColor(i,strip.Color(3,2,0));
						break;
					case 23:
						strip.setPixelColor(i,strip.Color(3,1,0));
						break;
					case 24:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 25:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 26:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 27:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 28:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 29:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 30:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 31:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 32:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 33:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 34:
						strip.setPixelColor(i,strip.Color(4,1,0));
						break;
					case 35:
						strip.setPixelColor(i,strip.Color(5,1,0));
						break;
					case 36:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 37:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 38:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 39:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 40:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 41:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 42:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 43:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 44:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 45:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 46:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 47:
						strip.setPixelColor(i,strip.Color(5,0,0));
						break;
					case 48:
						strip.setPixelColor(i,strip.Color(4,0,2));
						break;
					case 49:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 50:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 51:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 52:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 53:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 54:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 55:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 56:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 57:
						strip.setPixelColor(i,strip.Color(5,0,2));
						break;
					case 58:
						strip.setPixelColor(i,strip.Color(5,0,3));
						break;
					case 59:
						strip.setPixelColor(i,strip.Color(5,0,4));
						break;
					default:
					strip.setPixelColor(i,strip.Color(0,0,0));
					break;
				}
				strip.show();
			}
		}
	}

	if(millis() - timestamp > timeout){
		strip.setPixelColor(59,strip.Color(3,0,0));
		delay(1000);
		strip.show();

		strip.setPixelColor(59,strip.Color(0,0,0));
		delay(1000);
		strip.show();
	} else {
		strip.setPixelColor(59,strip.Color(0,3,0));
		strip.show();
	}
}
