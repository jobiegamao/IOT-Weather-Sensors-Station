import serial
import MySQLdb
from datetime import datetime


# establish connection to MySQL. You'll have to change this for your database.
# localhost, username, password, databaseName
dbConn = MySQLdb.connect("localhost", "root", "root", "sample") or die(
    "could not connect to database")

try:
    print("Connecting...")
    arduino = serial.Serial(port='COM3', baudrate=9600)
except:
    print("Failed to connect ")
while 1:
    try:
        arduinodata = arduino.readline()  # read the data from the arduino
        sensorsdata = arduinodata.decode("utf-8")
        data = sensorsdata.split(",")
        r1, r2, r3, r4, r5, r6 = data

        try:
            now = datetime.now()
            cursor = dbConn.cursor()
            cursor.execute("INSERT INTO weatherdata(ws, ap, wl, hu, tc, tf, dtime) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (r1, r2, r3, r4, r5, r6, now.strftime("%Y-%m-%d %H:%M:%S")))
            dbConn.commit()  # commit the insert
        except MySQLdb.IntegrityError:
            print("failed to insert data")
    except:
        print("Failed to get data from Arduino!")
    finally:
        cursor.close()  # close just incase it failed
