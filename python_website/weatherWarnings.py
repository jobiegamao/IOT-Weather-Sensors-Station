def warningMessages():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sample"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("Select * from weatherdata ORDER BY dtime DESC LIMIT 1;")
    myresult = mycursor.fetchall()
    
    warnings = []
    # data = list(myresult[-1])
    temp = int(myresult[4])
    ws= int(myresult[0])
    ap= int(myresult[1])
    wl= int(myresult[2])
    hu= int(myresult[3])
    
    message=""
   

    #----- temperature-----
    if temp <= 20:
        message = "Warning: Extremely Cold temperature, wear protective gears when going out  "
             
    elif 31 > temp > 21:
        message = "Advisory: Normal temperature, great time to go to the beach"
    
    elif 35 > temp > 31:
        message = "Caution: Fatigue is possible with prolonged exposure and activity. Continuing activity could result in heat cramps"
    
    else:
        message ="Caution: Extremely hot temperature, don't go ouside please"
    
    warnings.append(message) 
    
     #----- Wind speed-----       
    if ws <= 750:
        message = "Advisory: Low Wind Speed"
            
    elif 1000 > ws > 751  :
        message = "Advisory:  Average Wind Speed"
            
    elif 1500 > ws > 1001  :
        message = "Advisory: High Wind Speed, Unsecured, exposed outdoor items of light to moderate weight may become projectiles, causing additional damage or injuries."
            
    elif ws > 1600:
        message="Advisory: Very High Wind Speed, Take Action! Sustained, strong winds with even stronger gusts are happening. Seek shelter. If you are driving, keep both hands on the wheels and slow down."
    
    warnings.append(message) 
    
    #----- air pressure-----
    if ap <= 500:
        message = "Advisory: Low Air Pressure"
            
    elif 501 < ap < 600  :
        message = "Advisory: Average Air Pressure"
            
    elif ap >= 601  :
        message = "Advisory: High Air Pressure, Objects that are outdoors should be secured and caution should be taken if driving."
            
    warnings.append(message) 

    #----- water level-----
    if wl <= 130:
        message = "Warning: Very Low Water level"
            
    elif 300 > wl > 131  :
        message = "Warning: Low Water level"
            
    elif 500 > wl > 301  :
        message = "Warning: High Water Level"
            
    elif wl > 501:
        message = "Warning: Very High Water Level"
            
    warnings.append(message)
     
    
    #----- Humidity-----
    if hu <= 600:
        message = "Advisory: Low Humidity"
            
    elif 900 > hu > 601 :
        message = "Advisory: Average Humidity"
            
    elif hu >= 901 :
        message = "Advisory: High Humidity"
            
    warnings.append(message)    


    

    return warnings