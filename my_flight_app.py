import pandas as pd
import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
db=DB()
st.sidebar.title('FLIGHT ANALYTICS')
user_option=st.sidebar.selectbox('Menu',['select one','check flights','analytics'])

if user_option=='check flights':
    st.title('Check Flights')
    col1,col2=st.columns(2)
    city = db.fetch_city()
    with col1:

        source=st.selectbox('source',sorted(city))
    with col2:

        destination=st.selectbox('destination',sorted(city))
    if st.button('search'):
        result=db.fetch_all_flights(source,destination)
        st.dataframe(result)
elif user_option=='analytics':
    st.title('Analytics')
    airline,frequency=db.fetch_airline_frequency()
    fig = go.Figure(data=[go.Pie(
        labels=airline,
        values=frequency,
        hoverinfo='label+percent',
        textinfo='value'
    )])

    st.header('pie chart')
    st.plotly_chart(fig)

    # bar chart on streamlit plotly
    busy_airport=db.busy_airport()
    airport=pd.DataFrame({'city':busy_airport[0],'frequency':busy_airport[1]})
    st.bar_chart(data=airport,x='city', y='frequency')

    #with plotly
    fig = go.Figure(data=[go.Bar(
        x=airline,
        y=frequency,
        hoverinfo='y+text',
        text=frequency
    )])
    st.header('bar chart')
    st.plotly_chart(fig)

    #line plot of date of journey
    d_o_j=db.Date_of_journey()
    st.line_chart(data=d_o_j, x='Date', y='frequency')




else:
    st.title('Tell about the project ')

