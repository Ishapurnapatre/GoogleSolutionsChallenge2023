import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


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

xplot=list(data.iloc[:,1:].columns.values)


def predict_amt(x):
  output=list()
  for  i in range(a.size):
    y=a[i]*x+intr[i]
    yplot.append(y.values.tolist())
    output.append(round(y))
  y_df=pd.DataFrame(yplot)
  y_round=y_df.round(0).values
  prediction = [xplot,y_round]
  df1 = pd.DataFrame(prediction)
  df = df1.T  
  plt.figure(figsize=(8,5))
  plt.scatter(xplot,yplot)
  plt.xlabel=('Ingrediants')
  plt.ylabel=('Quantity')
  plt.title=('Day')
  plt.xticks(rotation = 90)
  print(df) 


###################################################################################################################




print("---------- FOOD FOR GOOD ----------\n")

cnt = 1
while cnt == 1:
  print("\n1. Add Today's Data")
  print("\n2. Today's Prediction")
  print("\n3. Pick-up Services")
  print("\n4. Exit")

  choice = int(input("\nEnter your Choice: "))

  if choice == 1:
    print("\nEnter data: ")
    day=int(input("day: "))
    flour=int(input("flour: "))
    rice=int(input("rice: "))
    milk=int(input("milk: "))
    tomato=int(input("tomato: "))
    onion=int(input("onion: "))
    oil=int(input("oil: "))
    cucumber=int(input("cucumber: "))
    lemon=int(input("lemon: "))
    panner=int(input("panner: "))
    chicken=int(input("chicken: "))
    fish=int(input("fish: "))
    potato=int(input("potato: "))
    brinjal=int(input("brinjal: "))
    capsicum=int(input("capsicum: "))
    carrot=int(input("carrot: "))
    butter=int(input("butter: "))
    bread=int(input("bread: "))
    egg=int(input("egg: "))
    batter=int(input("batter: "))
    yogurt=int(input("yogurt: "))
    sugar=int(input("sugar: "))
    salt=int(input("salt: "))
    cheese=int(input("cheese: "))
    leafy_vegetables=int(input("leafy_vegetables: "))
    field_names = ["day", "flour", "rice", "milk (liters)", "tomato", "onion", "oil (liters)", "cucumber",
                   "lemon",	"panner",	"chicken",	"fish",	"potato",	"brinjal",	"capsicum",	"carrot",	"butter",
                   "bread (packets)",	"egg (cartoons)",	"batter",	"yogurt",	"sugar",	"salt",	"cheese",	"leafy vegetable (gaddi)"]
    dict = {"day": day, "flour":flour, "rice":rice, "milk (liters)":milk, "tomato": tomato, "onion":onion, "oil (liters)":oil, "cucumber":cucumber,
                   "lemon":lemon,	"panner":panner,	"chicken":chicken,	"fish":fish,	"potato":potato,	"brinjal":brinjal,	"capsicum":capsicum,
                   "carrot":carrot,	"butter":butter, "bread (packets)":bread, "egg (cartoons)":egg, "batter":batter, "yogurt":yogurt,
                   "sugar":sugar,	"salt":salt,	"cheese":cheese,	"leafy vegetable (gaddi)":leafy_vegetables}

    with open('data_without_headings.csv', 'a') as csv_file:
      dict_object = csv.DictWriter(csv_file, fieldnames=field_names)  
      dict_object.writerow(dict)
      print("Data Updated Successfully!")

  elif choice == 2:
    today=input('\nEnter Day: ')
    if today.lower() == "monday":
      print("Holiday!!")
    elif today.lower() == "tuesday":
      dayNum=2
      predict_amt(dayNum)
    elif today.lower() == "wednesday":
      dayNum=3
      predict_amt(dayNum)
    elif today.lower() == "thursday":
      dayNum=4
      predict_amt(dayNum)
    elif today.lower() == "friday":
      dayNum=5
      predict_amt(dayNum)
    elif today.lower() == "saturday":
      dayNum=6
      predict_amt(dayNum)
    elif today.lower() == "sunday":
      dayNum=7
      predict_amt(dayNum)
    else: print("Invalid Input")

  elif choice == 3:
    print("\nSelect your preferable time:\n")
    print("1. 9-10 pm\n2. 10-11 pm\n3. 11-12 pm\n4. 12-1 pm\n5. 1-2 pm")
    slot = int(input("\nPreferred Slot: "))
    print("Slot Booked")
    print("\nKnow Details: ")
    print("Yes\tNo")
    ans = input("\nEnter option: ")
    if ans.lower() == 'yes':
      print("\nWet Waste will be sent for creating compost and bio gas.\nLeftover food will be given to the needy.")
      print("\nRegistered Composting Sites:\n1.INORA | Institute of Natural Organic Agriculture\tBavadhan",
            "\n2.ProEarth Ecosystems Private Limited\tKothrud",
            "\n3.Dr.compost\tKatraj",
            "\n4.Green Planet Solutions\tPimpri-Chinchwad",
            "\n5.Global Engineering And Waste Management\tVadgaon Budruk",
            "\6.Nila Polycast Baction\tSadashiv Peth",
            "\7.The Green Thumb\tKalyani Nagar")
      print("\nRegistered NGO's for Food Donation:\n1.Manuski Old Age Home and Seva Sushrusha Kendra",
            "\n2.Matruchhaya Balakashram",
            "\n3.Sevadeep",
            "\n4.Shree Sant Dyaneshwar Adivasi Ashram School",
            "\n5.Madhuban Matimand Va Bahuviklang Samajik Sanstha",
            "\6.ShivShahir Dr.Vijay Maharaj Tanpure",
            "\7.Sant Baba Moni Saheb Vriddha Anand Ashram")

  elif choice == 4:
    break

  else: print("Enter Valid Option!")

  print("\nDo you want to continue\n1. Yes \t2. No")
  cnt = int(input("\nEnter option: "))


print("\n---------- Thank You ----------")
