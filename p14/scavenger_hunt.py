#tianyu zhang 
import numpy as np
import pandas as pd

def line_graph(): 
    '''This function is used to draw w graph of cosine from 0 to 6'''
    #set the x axis range and points interval 
    xval = np.arange(0,6,.1)
    #set the y axis range
    yval = np.cos(xval)
    #store the points in values and make it with correct pairs 
    values = np.array([xval,yval])
    values = np.transpose(values)
    #put it in the data frame 
    df = pd.DataFrame(values, columns=["x","y"])
    #draw the grpah 
    axes = df.plot(x="x",y="y",label="0",title="Cosine Approximated at intervals of 1/(10pi)")
    #set the label in x axis in null
    axes.set_xlabel("")
    fig = axes.get_figure()
    fig.savefig("my_line_graph.png")


def scatterplot():
    '''this function is used to draw scatter points according to the questions'''
    #fixed points for red dots 
    coords = np.array([[1,1,4],[1,3,2]])
    #arrange them in correct order 
    coords  = np.transpose(coords)
    #draw the graph with specific color and label
    df = pd.DataFrame(coords, columns=["x","y"])
    axes = df.plot.scatter(x="x", y="y", label="Red Group", color="Red")
    #fixed points for yellow dots 
    coords2 = np.array([[1,2,3,6],[4,2,5,2]])
    #arrange them in correct order 
    coords2 = np.transpose(coords2)
    df = pd.DataFrame(coords2, columns=["x","y"])
    #draw and specify the label and color 
    axes = df.plot.scatter(ax=axes,x="x", y="y", label="Yellow Group", color="Yellow")
    #points for blue and arrange them in correct order 
    coords3 = np.array([[0,0,1,2,3],[5,1,2,3,4]])
    coords3 = np.transpose(coords3)
    df = pd.DataFrame(coords3, columns=["x","y"])
    #draw the graph with specific label and color 
    axes = df.plot.scatter(ax=axes, x="x", y="y", label="Blue Group", color="Blue", title="Scatter Plot in Three Colors")
    #set the x&y axis labels  
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    #set the range in x&y axis
    axes.set_xlim(-1,7)
    axes.set_ylim(0,6)
    fig = axes.get_figure()
    fig.savefig("my_scatter_plot.png")

   
    
    