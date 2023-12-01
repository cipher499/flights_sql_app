"""
Streamlit application for Airline data analysis
01/12/23
"""

import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title("Flights Analytics")

user_option = st.sidebar.selectbox("Menu", ["Select Option", "Check Flights", "Analytics"])

if user_option == "Check Flights":
    st.title("Check Flights")
    col1, col2 = st.columns(2)
    city = db.fetch_city_names()

    with col1:       
        source = st.selectbox("Source", sorted(city))
    with col2:
        destination = st.selectbox("Destination", sorted(city))

    if st.button("Search"):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)

elif user_option == "Analytics":
    st.title("Analytics")
    airline, count = db.fetch_airline_count()

    fig = go.Figure(
        go.Pie(
        labels = airline,
        values = count,
        hoverinfo = "label+percent",
        textinfo = "value"
        ))
    
    st.header("Pie chart")
    st.plotly_chart(fig)

    city, count1 = db.busy_airport()
    fig = px.bar(        
        x = city,
        y = count1,
        title = "Bar Graph"
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    pass