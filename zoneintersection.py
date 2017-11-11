# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:06:15 2017

@author: kgavini
"""

import pandas as pd

df = pd.read_csv("point.csv") 
df1 = pd.read_csv("verts.csv", header = 0)
xaxis = df.loc[:,'xaxis']
yaxis = df.loc[:,'yaxis']
zaxis = df.loc[:,'zaxis']
index = df.loc[:,'index']
df1.loc[:,'position3index'] =df1.loc[:,'postion3index']
position1index = df1.loc[:,'position1index']
position2index = df1.loc[:,'position2index']
position3index = df1.loc[:,'position3index']


       
x1 = [df.loc[(position1index[i])-1,'xaxis'] for i in range(len(position1index)) ]
df1['x1'] = pd.Series(x1, index=df1.index)
y1 = [df.loc[(position1index[i])-1,'yaxis'] for i in range(len(position1index)) ]
df1['y1'] = pd.Series(y1, index=df1.index)
x2 = [df.loc[(position2index[i])-1,'xaxis'] for i in range(len(position2index)) ]
df1['x2'] = pd.Series(x2, index=df1.index)
y2 = [df.loc[(position2index[i])-1,'yaxis'] for i in range(len(position2index)) ]
df1['y2'] = pd.Series(y2, index=df1.index)
x3 = [df.loc[(position3index[i])-1,'xaxis'] for i in range(len(position3index)) ]
df1['x3'] = pd.Series(x3, index=df1.index)
y3 = [df.loc[(position3index[i])-1,'yaxis'] for i in range(len(position3index)) ]
df1['y3'] = pd.Series(y3, index=df1.index)

cols = df1.columns.tolist()
cols = cols[5:11] + cols[4:5]
df1 = df1[cols]

zoneid = df1.loc[:,'zoneid']
    
xvalues = {}
n = 0
j = []
for i in zoneid:
    if i in j:
        xvalues[i].append([x1[n],x2[n],x3[n]])
    else:
        xvalues[i] = []
        xvalues[i].append([x1[n],x2[n],x3[n]])
        j.append(i)
    n = n+1
    
yvalues = {}
n1 = 0
j1 = []
for i1 in zoneid:
    if i1 in j1:
        yvalues[i1].append([y1[n1],y2[n1],y3[n1]])
    else:
        yvalues[i1] = []
        yvalues[i1].append([y1[n1],y2[n1],y3[n1]])
        j1.append(i1)
    n1 = n1+1    
    
    
    
    
    
        
        
    
    

