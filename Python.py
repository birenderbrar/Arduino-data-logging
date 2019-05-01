import pymongo # Importing pymongo for commnucation with mongodb 
import serial # Importing serial library for serial commnucation with arduino
import datetime  # Imporitng the date time module.
connection = pymongo.MongoClient('127.0.0.1', 27017) # Connection establishment with mongodb client
datastore = connection['test']  # creating data base in mongodb
collection = datastore['column'] # creating collection in database
if __name__ == '__main__':
    ser = serial.Serial('COM8', baudrate = 9600) # Ser is the object of serial class, definng the port no. and baudrate. 
    try:
        while True:  
            stream: str = ser.readline().decode('ascii') #Reading the data string and storing it into stream string.
            values = stream.rstrip().split('|') # Pasrsing the stream string and extracting the sensor data.
            Front = int(values[0]) # storing sensor data into relevant variables. 
            Right = int(values[1])
            Left = int(values[2])
            currentDT = datetime.datetime.now() # getting the current time.
            #Inseritng the sensors data and current time in MongoDb document.
            collection.insert_one({'front': int(Front),'right':int(Right),'left':int(Left),'current_time': str(currentDT.strftime("%I:%M:%S %p"))})
            #printing the sensor data on console as well for live monitoring. 
            print("Front = {}".format(Front), ",Left = {}" .format(Left) ,",Right = {}" .format(Right) )
    except:
        print('Serial connection closed') # printing user warning if there is no serial data.
        ser.close()








        