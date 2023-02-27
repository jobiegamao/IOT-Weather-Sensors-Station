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
    myresult = myresult[0]
    warnings = []
 
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
        message = "Advisory: Low Wind Speed, a perfect day to fly a kite or enjoy a leisurely stroll without worrying about your hair!"
            
    elif 1000 > ws > 751  :
        message = "Advisory:  Average Wind Speed, So, grab a scarf and feel the wind or impress people with your windswept look!!"
            
    elif 1500 > ws > 1001  :
        message = "Advisory: High Wind Speed, Unsecured, exposed outdoor items of light to moderate weight may become projectiles, causing additional damage or injuries."
            
    elif ws > 1600:
        message= "Advisory: Very High Wind Speed, Take Action! Sustained, strong winds with even stronger gusts are happening. Seek shelter. If you are driving, keep both hands on the wheels and slow down."
    
    warnings.append(message) 
    
    #----- air pressure-----
    if ap <= 500:
        message = "The atmospheric pressure is low, so take it easy and don't forget to drink lots of water."
            
    elif 501 < ap < 600  :
        message = "Advisory: Average Air Pressure, the air is just right for a perfect day out! So why not enjoy the great outdoors and breathe in the freshness of the air"
            
    elif ap >= 601  :
        message = "Advisory: High Air Pressure, Objects that are outdoors should be secured and caution should be taken if driving."
            
    warnings.append(message) 

    #----- water level-----
    if wl <= 130:
        message = "Warning: Very Low Water level, water activities may be limited or not possible. Be mindful of rocks, sandbars, or other hazards that may be exposed."
            
    elif 300 > wl > 131  :
        message = "Advisory: Low Water level, try walking along the shoreline and discovering new sights and sounds!"
            
    elif 500 > wl > 301  :
        message = "Advisory: High Water Level, time to grab your surfboard and hang ten! The higher water level can create some awesome waves and great surf conditions. Just make sure to be safe and follow proper surfing etiquette!"
            
    elif wl > 501:
        message = "Warning: Very High Water Level, Please exercise caution and stay away from the water's edge, as the currents may be stronger than usual. Remember, your safety is our top priority!"
            
    warnings.append(message)
     
    
    #----- Humidity-----
    if hu <= 600:
        message = "Advisory: Low Humidity, be sure to hydrate and moisturize! The dry air can take a toll on your skin and body, so make sure to drink plenty of water and moisturizers!"
            
    elif 900 > hu > 601 :
        message = "Advisory: Average Humidity, enjoy the pleasant weather! With the humidity at a comfortable level, it's the perfect time to get outside and get those legs pumping!"
            
    elif hu >= 901 :
        message = "Advisory: High Humidity, stay cool and comfortable! With the high humidity, the air can feel heavy and sticky, so be sure to stay in air-conditioned or well-ventilated areas as much as possible."
            
    warnings.append(message)    


    

    return warnings