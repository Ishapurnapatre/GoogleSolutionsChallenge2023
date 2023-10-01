import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('dataset.csv')

y=pd.DataFrame(data.iloc[:,1:]) #dependent var
x=pd.DataFrame(data.iloc[:,:1])  #contains independent factors days

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1,shuffle=True) #shuffling is imp 
from sklearn.linear_model import LinearRegression #remember sklearn.linear_model !!
regressor=LinearRegression()
regressor.fit(x_train,y_train) 

a=pd.DataFrame(regressor.coef_).transpose() #coeff	-0.019127	0.009996	-0.001051 without using transpose.....by default in rows to have it in cols use transpose
b=pd.DataFrame(y.columns,columns=['Attributes'])

coeff_df=pd.concat([b,a],axis=1,join='inner') #join along y axis
coeff_df

y_pred=regressor.predict(x_test)
y_pred=pd.DataFrame(y_pred,)
y_pred

intr=regressor.intercept_
yplot=[]

def predict_amt(x):
  output=list()#tuple has no attribute as append
  for  i in range(a.size):
    y=a[i]*x+intr[i]
    yplot.append(y.values.tolist())
    output.append(round(y))

day=input('\nEnter Day: ')
if day.lower() == "monday":
  print("Holiday!!")
elif day.lower() == "tuesday":
  dayNum=2
  predict_amt(dayNum)
elif day.lower() == "wednesday":
  dayNum=3
  predict_amt(dayNum)
elif day.lower() == "thursday":
  dayNum=4
  predict_amt(dayNum)
elif day.lower() == "friday":
  dayNum=5
  predict_amt(dayNum)
elif day.lower() == "saturday":
  dayNum=6
  predict_amt(dayNum)
elif day.lower() == "sunday":
  dayNum=7
  predict_amt(dayNum)
else: print("Invalid Input")

xplot=list(data.iloc[:,1:].columns.values)
plt.figure(figsize=(8,5))
plt.scatter(xplot,yplot)
plt.xticks(rotation = 90)
plt.xlabel=('ingrediants')
plt.ylabel=('quantity')
plt.title=(day)
plt.show()

#rounding off
y_df=pd.DataFrame(yplot)
y_round=y_df.round(0).values

prediction = [xplot,y_round]
df1 = pd.DataFrame(prediction)
df = df1.T

df.rename(columns={0: "ingredient", 1: "quantity"},inplace=True)
df
