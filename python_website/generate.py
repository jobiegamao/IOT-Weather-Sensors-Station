def generate_graphs():
    import serial
    import MySQLdb
    from datetime import datetime
    import mysql.connector
    import os
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    # Get the current working directory
    current_dir = os.getcwd()
    
    tempA = []
    airpA = []
    waterlA = []
    humA = []
    windspA = []
    secsA = []
    xs =[]
    ys = []
    xs2 =[]
    ys2 = []
    xs3 =[]
    ys3 = []
    xs4 =[]
    ys4 = []
    xs5 =[]
    ys5 = []

    while True:
        date = datetime.now()
        date = date.strftime("%Y/%m/%d %H:%M:%S")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="sample"
        )
        mycursor = mydb.cursor()
        mycursor.execute("Select * from weatherdata;")
        myresult = mycursor.fetchall()

        
        data = list(myresult[-1])
        # print(f"data: {data}")
        tempA.append(float(data[4]))
        airpA.append(float(data[1]))
        waterlA.append(float(data[2]))
        humA.append(float(data[3]))
        windspA.append(float(data[0]))
        sec = str(date)[-2:]
        secsA.append(int(sec))

        #graph for temp ------
        if secsA[-1] <= 1:
            ys=[]
            xs=[]
            xs.append(secsA[-1])
            ys.append(tempA[-1])
        elif secsA[-1] > 1:
            ys.append(tempA[-1])
            xs.append(secsA[-1])
            
        fig = plt.figure()
        axl = fig.add_subplot(1,1,1)
        axl.plot(xs, ys, 'g-', label='Celcius')
        plt.title("Temp in C graph")
        plt.ylabel("Celcius", fontweight='bold')
        plt.xlabel(f"{date}", fontweight='bold')
        plt.axis([0,60,0,100]) ####
        plt.axhspan(0,20, facecolor="blue", alpha = 0.2)
        plt.axhspan(21,30, facecolor="green", alpha = 0.2)
        plt.axhspan(31,55, facecolor="orange", alpha = 0.2)
        plt.axhspan(55,100, facecolor="red", alpha = 0.2)
        plt.legend()
        image_path = os.path.join(current_dir, "static/images", "temp.png")
        plt.savefig(image_path)
        # Clear the plot for the next set of data
        plt.close()
        plt.clf()
        
        #graph for air pressure airpA.append(float(data[1]))
        if secsA[-1] <= 1:   
            ys5=[]
            xs5=[]
            xs5.append(secsA[-1])
            ys5.append(airpA[-1])
        elif secsA[-1] > 1:
            ys5.append(airpA[-1])
            xs5.append(secsA[-1])
        fig = plt.figure()
        axl = fig.add_subplot(1,1,1)
        
        axl.plot(xs5, ys5, 'g-', label='Growth')
        plt.title("Air Pressure graph")
        plt.ylabel("Air", fontweight='bold')
        plt.xlabel(f"{date}", fontweight='bold')
        plt.axis([0,60,200,1000]) 
        plt.axhspan(300,500, facecolor="yellow", alpha = .5) 
        plt.axhspan(501,600, facecolor="orange", alpha = 0.2)
        plt.axhspan(601,1000, facecolor="red", alpha = 0.2)
        plt.legend()
        
        image_path = os.path.join(current_dir, "static/images", "airpressure.png")
        plt.savefig(image_path)
        # Clear the plot for the next set of data
        plt.close()
        plt.clf()
       

        #graph for windspeed ------
        if secsA[-1] <= 1:
            ys2=[]
            xs2=[]
            xs2.append(secsA[-1])
            ys2.append(windspA[-1])
        elif secsA[-1] > 1:
            ys2.append(windspA[-1])
            xs2.append(secsA[-1])
        fig = plt.figure()
        axl = fig.add_subplot(1,1,1)
        
        axl.plot(xs2, ys2, 'g-', label='Growth')
        plt.title("Windspeed")
        plt.ylabel("Windspeed", fontweight='bold')
        plt.xlabel(f"{date}", fontweight='bold')
        plt.axis([0,60,400,1900]) ####
        
        plt.axhspan(750,1000, facecolor="yellow", alpha = 0.2)
        plt.axhspan(1001,1500, facecolor="orange", alpha = 0.2)
        plt.axhspan(1500,1600, facecolor="red", alpha = 0.2)
        plt.legend()

        image_path = os.path.join(current_dir, "static/images", "windspeed.png")
        plt.savefig(image_path)
        # Clear the plot for the next set of data
        plt.close()
        plt.clf()
        
        

        #graph for waterlevel ------ waterlA.append(float(data[2]))
        if secsA[-1] <= 1:
            ys3=[]
            xs3=[]
            xs3.append(secsA[-1])
            ys3.append(waterlA[-1])
        elif secsA[-1] > 1:
            ys3.append(waterlA[-1])
            xs3.append(secsA[-1])
        fig = plt.figure()
        axl = fig.add_subplot(1,1,1)
        
        axl.plot(xs3, ys3, 'g-', label='Growth')
        plt.title("Water level graph")
        plt.ylabel("water level", fontweight='bold')
        plt.xlabel(f"{date}", fontweight='bold')
        plt.axis([0,60,120,1200]) 
        plt.axhspan(130,300, facecolor="yellow", alpha = 0.2)
        plt.axhspan(301,500, facecolor="orange", alpha = 0.2)
        plt.axhspan(1000,501, facecolor="red", alpha = 0.2)
        plt.legend()
        
        image_path = os.path.join(current_dir, "static/images", "waterlevel.png")
        plt.savefig(image_path)
        # Clear the plot for the next set of data
        plt.close()
        plt.clf()
        
        
        #graph for humidity humA.append(float(data[3]))
        if secsA[-1] <= 1:
            ys4=[]
            xs4=[]
            xs4.append(secsA[-1])
            ys4.append(humA[-1])
        elif secsA[-1] > 1:
            ys4.append(humA[-1])
            xs4.append(secsA[-1])
        fig = plt.figure()
        axl = fig.add_subplot(1,1,1)
        
        
        axl.plot(xs4, ys4, 'g-', label='Growth')
        plt.title("Humidity graph")
        plt.ylabel("Relative humidity", fontweight='bold')
        plt.xlabel(f"{date}", fontweight='bold')
        plt.axis([0,60,100,2000]) 
        
        plt.axhspan(400,600, facecolor="yellow", alpha = 0.2)
        plt.axhspan(601,900, facecolor="orange", alpha = 0.2)
        plt.axhspan(901,1400, facecolor="red", alpha = 0.2)
        plt.legend()
        image_path = os.path.join(current_dir, "static/images", "humidity.png")
        plt.savefig(image_path)
        # Clear the plot for the next set of data
        plt.close()
        plt.clf()
        

        