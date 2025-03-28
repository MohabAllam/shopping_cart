
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide", page_title = 'Simple DashBoard')

html_title = """<h1 style="white:red;text-align:center;"> Shopping Cart EDA Project </h1>"""
st.markdown(html_title,unsafe_allow_html=True)

df = pd.read_csv('cleaned_df.csv', index_col= 0)
st.dataframe(df.head(10))

page = st.sidebar.radio('pages', ['Univariate', 'Bivariate', 'Multivariate'])

if page == 'Univariate':
    for col in df.columns:
        st.plotly_chart(px.histogram(df, x = col, title= col))

elif page == 'Bivariate':

    X = st.selectbox('X', df.columns)
    Y = st.selectbox('Y', df.columns)
    chart = st.selectbox('Chart', ['scatter', 'line', 'box'])

    if chart == 'scatter':
        st.plotly_chart(px.scatter(df, x= X, y= Y))

    elif chart == 'line':
        st.plotly_chart(px.line(df.sort_values(by= 'order_date'), x= X, y= Y))

    elif chart == 'box':
        st.plotly_chart(px.box(df, x= X, y= Y))


elif page == 'Multivariate':
    
    # Is there any correlation between numerical columns ?
    st.subheader('Is there any correlation between numerical columns ?')
    st.plotly_chart(px.imshow(df.corr(numeric_only= True).round(2), text_auto= True, width= 1200, height= 1000))

    # What is the distribution of revenue each month per Product Type ?
    st.subheader('What is the distribution of revenue each month per Product Type ?')    
    st.plotly_chart(px.box(df, x= 'order_month', y= 'total_price', color= 'product_type'))
