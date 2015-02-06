# pollution-aqi

Pollution monitoring using http://aqicn.org/ and also Dylos DC1100

A friend gave me a cool LPD8806 based addressable LED strip and after pondering what to do with it i decided to build 
a pollution meter that displays the current air quality index for my city. 

One setup looks like this:
Internet -> Laptop -> Arduino -> LED Strip
On Laptop run arduino/aqicn_to_serial, which basically retrieves the AQI and sends it to the Arduino. The Arduino maps
the received value to something suitable for the LED strip and displays it in different colors from green to magenta 
depending on level of pollution. The lightstrip obviously needs to be connected to the
arduino appropriately and the arduino/aqi_lightstrip.ino has to be uploaded. To
make it work you will need to download the LPD8806 library of the Sparkfuns
github repository as well.

The next setup uses a Raspberry Pi and looks like this:
Internet -> Raspberry Pi -> LED Strip
On the RPi run raspberrypi/aqi_lightstrip which again retrieves and displays the AQI on the LED strip. It's better in a sense
that it foregos a dedicated laptop and Arduino and does it all from within one file.

Basically my LED strip is always between orange and red showing my citys pollution level is quite high. It has freaked me out
enough so that i ordered a Dylos DC1100 PC particle meter which i will use to measure the pollution level in my house and 
also visualize it on the LED strip. I'll then seal door gaps and windows while buying HEPA air filters and see if i can improve
on my air quality. 

The rest of the programs are helpers. database/aqicn_to_db scrapes aqicn.org and gets all available indexes such as pm25, pm10, carbon 
monoxide, sulfur oxide etc and stores it in a simple database for processing / graphing. database/dylos_to_db retrives data from the 
Dylos DC1100 and stores it also in a database.
