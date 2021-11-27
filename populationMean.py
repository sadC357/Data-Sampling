import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
pop_mean=statistics.mean(data)
std_dev=statistics.stdev(data)
print("Population Mean",pop_mean)
print("Standard Deviation",std_dev)

def randomMeanSet(counter):
    data_set=[]

    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    
    mean=statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df=mean_list
    MEAN=statistics.mean(mean_list)
    print("Mean",MEAN)
    StdDEV=statistics.stdev(mean_list)
    print("Standard Deviation",StdDEV)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[MEAN,MEAN],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setUp():
    mean_list=[]

    for i in range(0,1000):
        set_of_means=randomMeanSet(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)

setUp()