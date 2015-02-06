# pollution-aqi

Pollution monitoring using http://aqicn.org/ and also Dylos DC1100

A friend gave me a cool LPD8806 based addressable LED strip and after pondering what to do with it i decided to build 
a pollution meter that displays the current air quality index for my city. 

One setup looks like this:
Internet -> Laptop -> Arduino -> LED Strip
On Laptop run pollution_to_serial, which basically retrieves the AQI and sends it to the Arduino. The Arduino maps
the received Value to something suitable for the LED strip and displays it in different colors from green to magenta 
depending on level of pollution.

The next setup uses a Raspberry Pi and looks like this:
Internet -> Raspberry Pi -> LED Strip
On the RPi run raspberry_to_ledstrip which again retrieves and displays the AQI on the LED strip. It's better in a sense
that it foregos a dedicated laptop and Arduino.

Basically my LED strip is always between orange and red showing my citys pollution level is quite high. It has freaked me out
enough so that i ordered a Dylos DC1100 PC particle meter which i will use to measure the pollution level in my house and 
also visualize it on the LED strip. Ill then seal Door gaps and windows while buying a HEPA air filter and see if i can improve
on my air quality. 

The rest of the programs are helpers. aqicn_to_db scrapes aqicn.org and gets all available indexes such as pm25, pm10, carbon 
monoxide, sulfur oxide etc and stores it in a simple database for processing / graphing.

dylos_to_db retrives data from the Dylos DC1100 and stores it also in a database or sends it to 
