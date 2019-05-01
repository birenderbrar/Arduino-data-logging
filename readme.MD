# Arduino wireless distance data logger 
Logging arduino's sensor data to wireless server can be tedious task, However I found an simple way to do so. This method can be usefull in all sort of sensor data logging by perfromeing minor changes. 
* Three HCSR04 scnsors have been used in the direction of front, left and right of an wooden base. 
* we send the reading of these sensors to other arduino in each void loop, via bluetooth using [HC-05 Module](https://components101.com/wireless/hc-05-bluetooth-module)
* Reciver arduino recvives the data and parse it , after that is sends the data to computer using serial commnucation via USB. 
* At computer python recives the serial data and parse it, after that we are storing the live data in Mongo DB and printing that 
  at the same time with the context of current time. 
* Although HC-05 works in slave mode by default, but using the [At-commands](https://www.teachmemicro.com/hc-05-bluetooth-command-list/), we configured one hc-05 in master mode and connect it with the transmitter arduino. Apart from that we also confgured the slave's mac address with master's address, in order to achieve secure transmission of data. 
* Further this stored data can bes used for distance mapping, i.e. front, right and left distances, created a distance map of any structure, thus we can use this setup for measurment puroposes. 
* Further we also analyzed, the smaple map data into visaul form in Tableau, by connecting the Mongo Db data base with Tableau using [Bi connector](https://www.mongodb.com/products/bi-connector).
# Usage 
* Configure one HC-05 in master mode using AT commands.
* connect your master circuit according master fritzing file, upload the master_code.ino code to arduino. 
* connect your slave circuit according to slave fritzing file, upload the slave_code.ino code to arduino. 
* connect the salve arduino using usb to computer and note down the port number using device manager. 
* Run the python script, after adding the correct port number. 
# Notes
* You have to download fritzing software, in order to check the circuit connections. 
* You can replace Bluetooth module with wifi or radio module for the commnucation between two arduino as using wifi and radio you can better range, if your application requires better range. 
* The main intention behind this project was to find a reliable way to log arduino data on wirless server. 
