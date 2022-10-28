import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('AAPL,GOOG,META Stock(2017-2022) Analyze')
df_AAPL=pd.read_csv('AAPL.csv')
df_GOOG=pd.read_csv('GOOG.csv')
df_META=pd.read_csv('META.csv')

# https://blog.csdn.net/CoderPai/article/details/82887576

df_AAPL['log_price'] = np.log(df_AAPL['Close'])
df_GOOG['log_price'] = np.log(df_META['Close'])
df_META['log_price'] = np.log(df_META['Close'])

df_AAPL['log_return'] = df_AAPL.log_price.diff()
df_GOOG['log_return'] = df_GOOG.log_price.diff()
df_META['log_return'] = df_META.log_price.diff()

df_AAPL['var'] = np.var(df_AAPL.log_price)
df_GOOG['var'] = np.var(df_GOOG.log_price)
df_META['var'] = np.var(df_META.log_price)

df_AAPL['std'] = np.std(df_AAPL.log_price)
df_GOOG['std'] = np.std(df_GOOG.log_price)
df_META['std'] = np.std(df_META.log_price)


com_filter = st.sidebar.radio('Choose company',['Apple','Google','Facebook'])
if com_filter == 'Apple':
    st.subheader('shou the data of AAPL')
    options = np.array(df_AAPL['Date']).tolist()
    (start_time, end_time) = st.sidebar.select_slider("choose time period:",options = options,value= ('2022-05-04','2018-06-27',),)
    st.sidebar.write("begin time:",end_time)
    st.sidebar.write("end time:",start_time)
    df_AAPL['Date'] = pd.to_datetime(df_AAPL.Date, format = '%Y-%m-%d')
    df_AAPL.index = df_AAPL['Date']  
    df_AAPL['log_price'] = np.log(df_AAPL.Close)
    df_AAPL['log_return'] = df_AAPL.log_price.diff()
    df_AAPL1 = df_AAPL[start_time:end_time]
    st.dataframe(df_AAPL1)
    st.dataframe(df_AAPL1.describe())

if com_filter == 'Google':
    st.subheader('shou the data of GOOG')
    options = np.array(df_GOOG['Date']).tolist()
    (start_time, end_time) = st.sidebar.select_slider("choose time period:",options = options,value= ('2022-05-04','2018-06-27',),)
    st.sidebar.write("begin time:",end_time)
    st.sidebar.write("begin time:",start_time)
    df_AAPL['Date'] = pd.to_datetime(df_AAPL.Date, format = '%Y-%m-%d')
    df_GOOG.index = df_GOOG['Date']  
    df_GOOG1 = df_GOOG[start_time:end_time]
    st.dataframe(df_GOOG1)
    st.dataframe(df_GOOG1.describe()) 

if com_filter == 'Facebook':
    # df_META.Close.plot(legend=True)
    st.subheader('shou the data of META')
    options = np.array(df_META['Date']).tolist()
    (start_time, end_time) = st.sidebar.select_slider("choose tme period:",options = options,value= ('2022-05-04','2018-06-27',),)
    st.sidebar.write("begin time:",end_time)
    st.sidebar.write("end time:",start_time)
    df_AAPL['Date'] = pd.to_datetime(df_AAPL.Date, format = '%Y-%m-%d')
    df_META.index = df_META['Date']  
    df_META1 = df_META[start_time:end_time]
    st.dataframe(df_META1)
    st.dataframe(df_META.describe())

df_AAPL['daily_ret']=df_AAPL.Adj_Close.pct_change()
df_GOOG['daily_ret']=df_GOOG.Adj_Close.pct_change()
df_META['daily_ret']=df_META.Adj_Close.pct_change()

df_AAPL['Date'] = pd.to_datetime(df_AAPL.Date, format = '%Y-%m-%d')
df_GOOG['Date'] = pd.to_datetime(df_GOOG.Date, format = '%Y-%m-%d')
df_META['Date'] = pd.to_datetime(df_META.Date, format = '%Y-%m-%d')

df_AAPL.index = df_AAPL['Date']  
df_META.index = df_META['Date']  
df_GOOG.index = df_GOOG['Date']  

df_AAPL['log_price'] = np.log(df_AAPL['Close'])
df_GOOG['log_price'] = np.log(df_META['Close'])
df_META['log_price'] = np.log(df_META['Close'])

df_AAPL['log_return'] = df_AAPL.log_price.diff()
df_GOOG['log_return'] = df_GOOG.log_price.diff()
df_META['log_return'] = df_META.log_price.diff()

df_AAPL['var'] = np.var(df_AAPL.log_price)
df_GOOG['var'] = np.var(df_GOOG.log_price)
df_META['var'] = np.var(df_META.log_price)

df_AAPL['std'] = np.std(df_AAPL.log_price)
df_GOOG['std'] = np.std(df_GOOG.log_price)
df_META['std'] = np.std(df_META.log_price)

com_filter = st.sidebar.multiselect('Choose company',['Apple','Google','Facebook'])
st.header(f'Show the basic plot of {com_filter}')
fig0, ax0 = plt.subplots()
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()

if 'Apple' in com_filter:   
    df_AAPL.Close.plot(ax = ax0,color = 'blue', legend = True,label = 'AAPL closing')
    df_AAPL.Volume.plot(ax = ax1,color = 'blue',legend = True, label = 'AAPL volume')
    df_AAPL.Close.plot(ax = ax2,color = 'blue',legend = True,  label = 'AAPL close')
    df_AAPL.Adj_Close.plot(ax = ax2,color='purple',legend=True,label = 'AAPL adi_close')
    df_AAPL.log_price.plot(ax=ax3,color='blue',legend=True,label= 'AAPL log_price')
    df_AAPL.daily_ret.plot(ax = ax4,color = 'blue',legend = True,label = 'AAPL daily_return')
    df_AAPL.log_return.plot(ax = ax4,color = 'purple',legend = True,label = 'AAPL log_return')       

if 'Google' in com_filter:
    df_GOOG.Close.plot(ax = ax0,color = 'green', legend = True,label = 'GOOG close')
    df_GOOG.Volume.plot(ax = ax1,color = 'green',legend = True, label = 'GOOG volume')
    df_GOOG.Close.plot(ax = ax2,color='green',legend=True,label = 'GOOG close')
    df_GOOG.Adj_Close.plot(ax= ax2,color='gray',legend=True,label = 'GOOG adj_close')
    df_GOOG.log_price.plot(ax=ax3,color='green',legend=True,label= 'GOOG log_price')
    df_GOOG.daily_ret.plot(ax = ax4,color='green',legend=True,label = 'GOOG daily_return')
    df_GOOG.log_return.plot(ax = ax4,color='gray',legend=True,label = 'GOOG log_return')

if 'Facebook' in com_filter:   
    df_META.Close.plot(ax = ax0,color = 'yellow', legend = True,label = 'META close')
    df_META.Volume.plot(ax = ax1,color = 'yellow',legend = True,label = 'META volume')
    df_META.Close.plot(ax = ax2,color='yellow',legend=True,label = 'META close')
    df_META.Adj_Close.plot(ax= ax2,color='red',legend=True,label = 'META adj_close')
    df_META.log_price.plot(ax=ax3,color='yellow',legend=True,label= 'META log_price')
    df_META.log_return.plot(ax = ax4, color='red',legend=True,label = 'META log_return')

if 'Apple' in com_filter and 'Google' in com_filter and 'Facebook' in com_filter :
    company={'name':['AAPL','GOOG','META'],'industry':['Consumer Electronics','Internet Content & Information','Internet Content & Information'],'total_revenue':[365817,257637,117929],'net_income':[94680,76033,39370]}
    df=pd.DataFrame(company)
    df.total_revenue.plot.bar(ax=ax5,color='black',legend=True).set_xticks([0,1,2],['AAPL','GOOG','META'],rotation=30)
    df.net_income.plot.bar(ax=ax5,color='purple',legend=True).set_xticks([0,1,2],['AAPL','GOOG','META'],rotation=30)
ax0.set_ylabel('price')    
st.pyplot(fig0) 
st.pyplot(fig1) 
st.pyplot(fig2) 
st.pyplot(fig3) 
st.pyplot(fig4) 
st.pyplot(fig5)

company={
    'name':['AAPL','GOOG','META'],
'industry':['Consumer Electronics','Internet Content & Information','Internet Content & Information'],
'total_revenue':[365817,257637,117929],
'net_income':[94680,76033,39370]
}
df=pd.DataFrame(company)
st.dataframe(df)

st.write(f'At 95% confidence interval,the loss isn\'t exceed.\nAAPL: {abs(df_AAPL.daily_ret.quantile(0.05)*100):.3f}%\nGOOG: {abs(df_GOOG.daily_ret.quantile(0.05)*100):.3f}%\nMETA: {abs(df_META.daily_ret.quantile(0.05)*100):.3f}%')







# Median_house_pricing_filter = st.slider('Median_house_pricing_filter:', 0, 500001, 200000)
# df = df[df.median_house_value >= Median_house_pricing_filter]

# location_filter = st.sidebar.multiselect('Choose the location type',df.ocean_proximity.unique(), df.ocean_proximity.unique())
# df = df[df.ocean_proximity.isin(location_filter)]

# income_filter = st.sidebar.radio('Choose the income level',['Low','Medium','High'])
# if income_filter == 'Low':
#     df = df[df.median_income <= 2.5]
# if income_filter == 'Medium':
#     df = df[(df.median_income >= 2.5) & (df.median_income <= 4.5)]
# if income_filter == 'High':
#     df = df[df.median_income <= 4.5]        

# st.subheader('See more filters in the sidebar:')
# st.map(df)    

# st.subheader('Histogram of the Median House Value')
# fig, ax = plt.subplots(figsize=(15, 10))
# val = df.median_house_value.hist(bins=30)
# st.pyplot(fig)