import mysql.connector
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from generate import graph


def getAverageGraph(date1, date2):
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="sample")

    mycursor = mydb.cursor()

    xs = []  #date
    ys = {idx: [] for idx in range(5)}

    myquery = f"SELECT AVG(ws), AVG(ap), AVG(wl), AVG(hu), AVG(tc), dtime FROM weatherdata WHERE dtime >= '{date1} 00:00:00' AND dtime <= '{date2} 23:59:59' GROUP BY date(dtime)"
    mycursor.execute(myquery)
    myresult = mycursor.fetchall()

    for i in myresult:
        for (idx, j) in enumerate(i):
            if idx == 5:
                formattedDate = j.strftime("%Y/%m/%d")
                xs.append(formattedDate)
            else:
                j = float(j)
                ys[idx].append(j)

    graph(code="tc",
          xs=xs,
          ys=ys[4],
          xlabel="Days",
          ylabel="Average Temperature",
          title="Temperature History",
          avg=1)
    graph(code="ws",
          xs=xs,
          ys=ys[0],
          xlabel="Days",
          ylabel="Average Wind Speed",
          title="Wind Speed History",
          avg=1)
    graph(code="ap",
          xs=xs,
          ys=ys[1],
          xlabel="Days",
          ylabel="Average Air Pressure",
          title="Air Pressure History",
          avg=1)
    graph(code="wl",
          xs=xs,
          ys=ys[2],
          xlabel="Days",
          ylabel="Average Water Level",
          title="Water Level History",
          avg=1)
    graph(code="hu",
          xs=xs,
          ys=ys[3],
          xlabel="Days",
          ylabel="Average Humidity",
          title="Humidity History",
          avg=1)
