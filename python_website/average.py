import os
import matplotlib.pyplot as plt
import mysql.connector


def getAverageGraph(date1, date2):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sample"
    )

    mycursor = mydb.cursor()

    # d = date1.split('-')
    # date1 =""
    # for i in d:
    #     date1 = date1 + i +"/"

    # t = date2.split('-')
    # date2 =""
    # for i in t:
    #     date2 = date2 + i +"/"

    # print(date1, date2)

    # date1 = date1[:-1]
    # date2 = date2[:-1]
    xs =[]
    ys = []
    ys2 = [] #windspeed
    ys3 = [] #waterlevel
    ys4 = [] #humidity
    ys5 = [] #airpressure

    query2 = f"select dtime, AVG(tc), AVG(ws), AVG(wl), AVG(hu), AVG(ap) from weatherdata where dtime >= '{date1} 00:00:00' AND dtime <= '{date2} 23:59:59' group by date(dtime)"
    mycursor.execute(query2)
    myresult = mycursor.fetchall()
    
    print(myresult)

    teststr = ""
    for i in myresult:
        ys.append(float(i[1]))
        ys2.append(float(i[2])) 
        ys3.append(float(i[3]))
        ys4.append(float(i[4]))
        ys5.append(float(i[5]))
        teststr=i[0].strftime("%Y/%m/%d")
        xs.append(teststr)
        print(teststr)

    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    # Get the current working directory
    current_dir = os.getcwd()

    #average temp
    fig = plt.figure()
    axl = fig.add_subplot(1,1,1)
    axl.plot(xs, ys, 'b-', label='Growth')
    plt.title("Temperature graph (average)")
    plt.ylabel("Average Temperature", fontweight='bold')
    plt.xlabel("Days", fontweight='bold')
    plt.legend()

    image_path = os.path.join(current_dir, "static/images", "temp_avg.png")
    plt.savefig(image_path)
    # Clear the plot for the next set of data
    plt.close()
    plt.clf()

    #average wind speed
    fig = plt.figure()
    axl = fig.add_subplot(1,1,1)
    axl.plot(xs, ys2, 'b-', label='Growth')
    plt.title("Winds Speed graph (average)")
    plt.ylabel("Average Windspeed", fontweight='bold')
    plt.xlabel("Days", fontweight='bold')
    plt.legend()

    image_path = os.path.join(current_dir, "static/images", "windspeed_avg.png")
    plt.savefig(image_path)
    # Clear the plot for the next set of data
    plt.close()
    plt.clf()

    #average waterlevel
    fig = plt.figure()
    axl = fig.add_subplot(1,1,1)
    axl.plot(xs, ys3, 'b-', label='Growth')
    plt.title("Water Level graph (average)")
    plt.ylabel("Average Water Level", fontweight='bold')
    plt.xlabel("Days", fontweight='bold')
    plt.legend()
    image_path = os.path.join(current_dir, "static/images", "waterlevel_avg.png")
    plt.savefig(image_path)
    # Clear the plot for the next set of data
    plt.close()
    plt.clf()

    #average humidity
    fig = plt.figure()
    axl = fig.add_subplot(1,1,1)
    axl.plot(xs, ys4, 'b-', label='Growth')
    plt.title("Humidity graph (average)")
    plt.ylabel("Average Humidity", fontweight='bold')
    plt.xlabel("Days", fontweight='bold')
    plt.legend()
    image_path = os.path.join(current_dir, "static/images", "humidity_avg.png")
    plt.savefig(image_path)
    # Clear the plot for the next set of data
    plt.close()
    plt.clf()

    #average air pressure
    fig = plt.figure()
    axl = fig.add_subplot(1,1,1)
    axl.plot(xs, ys5, 'b-', label='Growth')
    plt.title("Air Pressure graph (average)")
    plt.ylabel("Average Temperature", fontweight='bold')
    plt.xlabel("Days", fontweight='bold')
    plt.legend()
    image_path = os.path.join(current_dir, "static/images", "airpressure_avg.png")
    plt.savefig(image_path)
    # Clear the plot for the next set of data
    plt.close()
    plt.clf()
    