from datetime import datetime
import mysql.connector
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generate_graphs():

    secPassed = []

    datas = {ix: [] for ix in range(5)}  #latest record
    xs = {ix: [] for ix in range(5)}  #time
    ys = {ix: [] for ix in range(5)}  #sensor values at this minute

    while True:
        date = datetime.now()
        date = date.strftime("%Y/%m/%d %H:%M:%S")

        # seconds at our time atm
        sec = str(date)[-2:]
        secPassed.append(int(sec))  # append to seconds Passed

        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="sample")
        mycursor = mydb.cursor()
        mycursor.execute(
            "Select * from weatherdata ORDER BY dtime DESC LIMIT 1;")
        myresult = mycursor.fetchall()
        myresult = myresult[0]

        #fill up sensor data of latest result

        for idx in range(5):
            datas[idx].append(float(myresult[idx]))
            xs[idx], ys[idx] = setXY(seconds=secPassed,
                                     x=xs[idx],
                                     y=ys[idx],
                                     data=datas[idx])

        graph(code="tc",
              xs=xs[4],
              ys=ys[4],
              xlabel=date,
              ylabel="Celcius",
              title="Temp in C")

        graph(code="ws",
              xs=xs[0],
              ys=ys[0],
              xlabel=date,
              ylabel="Anemometer Value",
              title="WindSpeed")

        graph(code="ap",
              xs=xs[1],
              ys=ys[1],
              xlabel=date,
              ylabel="Pascal",
              title="Air Pressure")

        graph(code="wl",
              xs=xs[2],
              ys=ys[2],
              xlabel=date,
              ylabel="PSI",
              title="Water Level")

        graph(code="hu",
              xs=xs[3],
              ys=ys[3],
              xlabel=date,
              ylabel="grams per cubic metre.",
              title="Humidity")


def graph(code, xs, ys, xlabel, ylabel, title, avg=0):
    fig = plt.figure()
    axl = fig.add_subplot(1, 1, 1)
    axl.plot(xs, ys, 'g-', label=ylabel)
    plt.title(title)
    plt.ylabel(ylabel, fontweight='bold')
    plt.xlabel(f"{xlabel}", fontweight='bold')
    if code == "tc":
        if avg == 0:
            plt.axis([0, 60, 0, 100])
        plt.axhspan(0, 20, facecolor="blue", alpha=0.2)
        plt.axhspan(21, 30, facecolor="green", alpha=0.2)
        plt.axhspan(31, 55, facecolor="orange", alpha=0.2)
        plt.axhspan(55, 100, facecolor="red", alpha=0.2)
    elif code == "ws":
        if avg == 0:
            plt.axis([0, 60, 636, 1750])
        plt.axhspan(636, 1000, facecolor="yellow", alpha=0.2)
        plt.axhspan(1001, 1500, facecolor="orange", alpha=0.2)
        plt.axhspan(1500, 1659, facecolor="red", alpha=0.2)
    elif code == "ap":
        if avg == 0:
            plt.axis([0, 60, 115, 1400])
        plt.axhspan(115, 500, facecolor="yellow", alpha=0.2)
        plt.axhspan(501, 600, facecolor="orange", alpha=0.2)
        plt.axhspan(601, 1137, facecolor="red", alpha=0.2)
    elif code == "wl":
        if avg == 0:
            plt.axis([0, 60, 0, 1100])
        plt.axhspan(0, 300, facecolor="yellow", alpha=0.2)
        plt.axhspan(301, 500, facecolor="orange", alpha=0.2)
        plt.axhspan(501, 1023, facecolor="red", alpha=0.2)
    elif code == "hu":
        if avg == 0:
            plt.axis([0, 60, 500, 1700])
        plt.axhspan(500, 600, facecolor="yellow", alpha=0.2)
        plt.axhspan(601, 900, facecolor="orange", alpha=0.2)
        plt.axhspan(901, 1555, facecolor="red", alpha=0.2)
    else:
        return

    plt.legend()

    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    # Get the current working directory
    current_dir = os.getcwd()

    imageName = ""
    if avg == 0:
        imageName = f"{code}.png"
    else:
        imageName = f"{code}_history.png"

    image_path = os.path.join(current_dir, "static/images", imageName)
    plt.savefig(image_path)

    # Clear the plot for the next set of data
    plt.close()
    plt.clf()


def setXY(seconds: list, x: list, y: list, data: list):
    if seconds[-1] <= 1:
        y = []
        x = []
        x.append(seconds[-1])
        y.append(data[-1])
    elif seconds[-1] > 1:
        y.append(data[-1])
        x.append(seconds[-1])
    return x, y
