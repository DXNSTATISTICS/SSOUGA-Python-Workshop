#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:07:53 2023

@author: dixons
"""

import pandas as pd
import numpy as np

data = pd.read_csv('ReferenceBasketball.csv')

data

df = pd.DataFrame({'A': [1, 2, 3],
                  'B': [4,5,6],
                  'C': [7,8,9]})

df

df = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]],
index=[1, 2, 3],
columns=['a', 'b', 'c'])

df

# Locate Row
df.loc[2]

df.loc[[2,3]]

df.loc[[1,2]]

#locate by index number
df.iloc[2]
df.iloc[[0,1]]

df.iloc[1:2]

df.columns

#Data Cleaning
df1 = pd.DataFrame([[4, 7, 10],[5, 8, 11],[6, 9, 12],[50,60,np.nan],[42,14,88]],index=[1, 2, 3, 4, 5], columns=['a', 'b', 'c'])

df1

df1.dropna()

df1

df1=df1.dropna()

df1

df1 = pd.DataFrame([[4, 7, 10],[5, 8, 11],[6, 9, 12],[50,60,np.nan],[42,14,88]],index=[1, 2, 3, 4, 5], columns=['a', 'b', 'c'])

#Replace NA value  

df1=df1.fillna('orange')

df1

df1 = pd.DataFrame([[4, 7, 10],[5, 8, 11],[6, 9, 12],[50,60,4],[42,14,88]],index=[1, 2, 3, 4, 5], columns=['a', 'b', 'c'])
df1=df1.dropna()

df2 = df1 = pd.DataFrame([[6, 7, 30],[45, 6, 6],[29, 35, 13],[50,60,5],[42,14,88]],index=[1, 2, 3, 4, 5], columns=['a', 'b', 'c'])
df2=df2.dropna()

df1
df2

#Matrix Math
df1+df2

df1*df2

df1**df2

#Pandas Methods
df['A'].mean()

df['A'].std()

df['A'].sum()

df1.sum()
df1.sum().mean()

df1.describe()


#length
len(df1)

#range(start,stop, step)
x = range(3, 20, 2)

x
x[6]
x[3]

x[6:10]

x[60]

type(x)

y = [1,2,3,4,'abc']
type(y)

#Dictionaries
h = {'A':['roger'],
     'B':['Reggie', 5, 4],
     'F': [2]}
h.keys()
h['A']
h.values()


#For and While loops
for n in x:
  print(n)

i = 1
while i < 6:
  print(i)
  i += 1
  
 i = 1
 while i <506:
   print(i)
   i += 1
    
 i = 1
 while i <5000000:
   print(i)
   i += 0.1
   
 i = 1
 while i <2:
   print(i)


# For Loop
x = [1,2,3,4,5,6,7,8,9,10]
y = []

for i in range(len(x)):
    y.append(i + 17)

y

y=[]
for i in range(len(x)):
    y.append(x[i] + 17)
    
y

# Basic Function
z=[]
def mathify(r,p):
    for x in r:
        if x >= 24:
            p.append(x-6)
        elif x <= 20:
            p.append(x + 25)
        else:
            p.append(x)
    return print(p)

mathify(y,z)
