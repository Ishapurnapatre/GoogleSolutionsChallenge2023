import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('dataset.csv')

header=st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Didot:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Didot', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

page_bg_img='''
    <style>
    [data-testid="stAppViewContainer"]{
        background-size:cover;
        background-color:#C9F4AA;

    opacity=0.1;
    }
    </style>
'''
st.markdown(page_bg_img,unsafe_allow_html=True)

with header:
    st.title('Food For Good')
    image = Image.open('bg.png')
    st.image(image, caption='https://hospitalityinsights.ehl.edu/food-waste-management-innovations',)
    st.write('The amount of food being wasted every day in restaurants is shocking. Lack of proper storage and over-purchase and overproduction of food results in a monumental amount of food being wasted. Statistically speaking, wastage is one of the leading causes of escalated food costs and diminishing revenue, which leads to the eventual shutting down of restaurants. Smart food waste management involves proper planning and efficient inventory management, which can help you cut down your food wastage marginally.')


with header:
    st.header('Details')
    st.write("Wet waste will be sent for creating compost and bio gas, leftover food will be given to the needy.")
    st.subheader("Registered Composting Sites: ")
    st.markdown("INORA | Institute of Natural Organic Agriculture   -   Bavadhan")
    st.markdown("ProEarth Ecosystems Private Limited   -   Kothrud")
    st.markdown("Dr.compost   -   Katraj")
    st.markdown("Green Planet Solutions   -   Pimpri-Chinchwad")
    st.markdown("Global Engineering And Waste Management    -   Vadgaon Budruk")
    st.markdown("Nila Polycast Baction   -   Sadashiv Peth")
    st.markdown("The Green Thumb    -   Kalyani Nagar")
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        list-style-position: inside;
    }
    </style>
    ''', unsafe_allow_html=True)
    image2 = Image.open('compost.webp')
    st.image(image2, caption='https://www.healthline.com/nutrition/composting-beginners-guide',)
    st.subheader("Registered NGO's for Food Donation: ")
    st.markdown("Manuski Old Age Home and Seva Sushrusha Kendra")
    st.markdown("Matruchhaya Balakashram")
    st.markdown("Sevadeep")
    st.markdown("Shree Sant Dyaneshwar Adivasi Ashram School")
    st.markdown("Madhuban Matimand Va Bahuviklang Samajik Sanstha")
    st.markdown("ShivShahir Dr.Vijay Maharaj Tanpure")
    st.markdown("Sant Baba Moni Saheb Vriddha Anand Ashram")
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        list-style-position: inside;
    }
    </style>
    ''', unsafe_allow_html=True)


with features:
    st.header('Pick-up Service')
        
    sel_col, disp_col = st.columns(2)

    slot = sel_col.selectbox("Select Slot", options=['8-9','9-10','10-11','11-12','12-1','1-2'], index=0)
    
    if st.button('Book slot'):
        st.write('Slot Booked!  Thank You')
    else:
        st.write('No Slot Available')
    
    

with modelTraining:
    st.header('Prediction model')  
    st.text('Ingredients for today!')

    sel_col, disp_col = st.columns(2)

    day = sel_col.selectbox("Choose the correct option", options=['monday','tuesday','wednesday','thursday','friday','saturday','sunday'], index=0)
    
    y=pd.DataFrame(data.iloc[:,1:])
    x=pd.DataFrame(data.iloc[:,:1])
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1,shuffle=True)
    regressor=LinearRegression()
    regressor.fit(x_train,y_train) 

    a=pd.DataFrame(regressor.coef_).transpose()
    b=pd.DataFrame(y.columns,columns=['Attributes'])

    coeff_df=pd.concat([b,a],axis=1,join='inner')

    y_pred=regressor.predict(x_test)
    y_pred=pd.DataFrame(y_pred,)
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
        st.table(df) 
         
         
    

    if day=='monday' or day=='Monday':
        dayNum=1
    
    elif day=='tuesday' or day=='Tuesday':
        dayNum=2

    elif day=='wednesday' or day=='Wednesday':
        dayNum=3

    elif day=='thursday' or day=='Thursday':
        dayNum=4

    elif day=='friday' or day=='Friday':
        dayNum=5

    elif day=='saturday' or day=='Saturday':
        dayNum=6

    elif day=='sunday' or day=='Sunday':
        dayNum=7

    else: print("Invalid Input")
      
      
    if dayNum==1:
        disp_col.subheader('Prediction: ')
        disp_col.write('Holiday!!')
    else: 
        prediction=predict_amt(dayNum)       
        disp_col.subheader('Prediction: ')
        disp_col.write(prediction)

    
