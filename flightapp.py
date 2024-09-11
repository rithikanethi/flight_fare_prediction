import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import datetime
import sklearn
import time


def main():
    st.header("Predict Flight Price")

    st.sidebar.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    
    dep = st.sidebar.date_input("Day" , datetime.date(y,m,d))
    if dep is not None:
        mon_d = dep.month
        day_d = dep.day

        hour_1 = st.sidebar.selectbox("Hours", list(range(1,25)))
        minute_1 = st.sidebar.selectbox("Minutes", list(range(0,61)))

    st.subheader("Departure Time :")
    x = "2022" + "/"  +str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
    if x is not None:
        
        op = pd.to_datetime([x])
        if op is not None:
            st.write(op.item())
    

    st.sidebar.subheader("Select Arrival")
    arr = st.sidebar.date_input("Day." , datetime.date(y,m,d))
    if arr is not None:
    
        mon_a = arr.month
        day_a = arr.day
        
        

        hour_2 = st.sidebar.selectbox("Hours:", list(range(1,25)) ,2)
        minute_2 = st.sidebar.selectbox("Minutes:", list(range(0,61)))

    st.subheader("Arrival Time :")
    x1 = "2022" + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
    if x1 is not None:
        
        op1 = pd.to_datetime([x1] )
        if op1 is not None:
            st.write(op1.item())
            



     #source
    st.subheader("Select Source")
    source = st.selectbox(" " , ['Mumbai','Delhi','Kolkata',"Chennai"])
    if source == "Chennai":
        source_inp = 1
    elif source == "Delhi":
        source_inp = 2
    elif source == "Kolkata":
        source_inp = 3
    elif source == "Mumbai":
        source_inp = 4
    

    #destination
    st.subheader("Select Destination")
    dest = st.selectbox("" , ['Cochin', 'Hyderabad',"New Delhi",'Delhi','Kolkata'])

    if dest == "Cochin":
        dest_inp = 1
    elif dest == "Delhi":
        dest_inp = 2
    elif dest == "Hyderabad":
        dest_inp = 3
    elif dest == "Kolkata":
        dest_inp = 4
    elif dest == "New Delhi":
        dest_inp = 5

    #airline
    st.subheader("Select Airline")
    airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia"])

    if airline == "Jet Airways":
        air_inp = 0
    elif airline == "IndiGo":
        air_inp = 1
    elif airline == "Air India":
        air_inp = 2
    elif airline == "Multiple carriers":
        air_inp = 3
    elif airline == "SpiceJet":
        air_inp = 4
    elif airline == "Vistara":
        air_inp = 5
    elif airline == "Air Asia":
        air_inp = 6
    elif airline == "GoAir":
        air_inp = 7


    #stops
    st.subheader("Select Stops")
    stop = st.selectbox("   " , [0,1,2,3,4])

    if st.button("View Duration"):
        if op1 is not None:
            
            st.write((op1.item() - op.item()))




     #model
   # model = open(r"C:\Users\91846\Desktop\flightpriceprediction\flight2.pkl", "rb")
    #rfr_model = pickle.load(model)

    rfr_model = pickle.load(open("flight2.pkl", "rb"))

    #prediction
    if(air_inp ==0):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

    elif (air_inp==1):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

    elif (air_inp==2):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
    elif (air_inp==3):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
    elif (air_inp==4):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
    elif (air_inp==5):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (air_inp==6):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1


    elif (air_inp == 7):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
    else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
    
    if (source_inp == 2):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

    elif (source_inp == 3):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

    elif (source_inp == 4):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

    elif (source_inp == 1):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

    else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

    if (dest == 1):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
    elif (dest == 2):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (dest == 5):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (dest == 3):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

    elif (dest == 4):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

    else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
    dur_hour = abs(hour_2 - hour_1)
    dur_min = abs(minute_2 - minute_1)
    if st.button("Predict Price"):
        pred=rfr_model.predict([[
            stop,
            day_d,
            mon_d,
            hour_1,
            minute_1,
            hour_2,
            minute_2,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        for i in pred:
            st.write("Your Flight Price is : INR" , round(i))
            

   



if __name__ == "__main__":
    main()
