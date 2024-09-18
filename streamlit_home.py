# import library
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# import function
from streamlit_01_dataset import *
from streamlit_02_visualization import *

# config web streamlit
st.set_page_config(page_title="My Dasboard",layout="wide")

# config dataset
dataset = get_dataset()

# container-header
st.markdown("## Nike Sales Dashboard on 2020 - 2021")

# container-config
col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25], gap="small")
with col1:
  product = st.selectbox(
    label="Choose a Products",
    options=("All","Men's Apparel","Men's Athletic Footwear","Men's Street Footwear","Women's Apparel","Women's Athletic Footwear","Women's Street Footwear"),
    index=0
  )
with col2:
  retailer = st.selectbox(
    label="Choose a Retailer",
    options=("All","Amazon","Foot Locker","Kohl's","Sports Direct","Walmart","West Gear"),
    index=0
  )
with col3:
  sales = st.selectbox(
    label="Choose a Sales Method",
    options=("All","In-store","Online","Outlet"),
    index=0
  )
with col4:
  region = st.selectbox(
    label="Choose a Region",
    options=("All","Midwest","Northeast","South","Southeast","West"),
    index=0
  )

df_product = dataset.groupby(by=["Product"])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()
st.plotly_chart(barplot(df_product,"Total Sales","Product","Product wise total sales"),use_container_width=True)

# container-eda
col1, col2, col3= st.columns([0.33, 0.33, 0.33], gap="small")

# eda retailer by total sales
with col1:
  df_retailer = dataset.groupby(by=["Retailer"])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()
  df_retailer = df_retailer.tail(4)
  st.plotly_chart(pieplot(df_retailer,"Total Sales","Retailer","Retailer wise total sales"),use_container_width=True)

# eda region by total sales
with col2:
  # calculate region by total sales
  df_region = dataset.groupby(by=["Region"])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()
  st.plotly_chart(pieplot(df_region,"Total Sales","Region","Region wise total sales"),use_container_width=True)

# eda sales method by total sales
with col3:
  df_sales_method = dataset.groupby(by=["Sales Method"])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()
  st.plotly_chart(pieplot(df_sales_method,"Total Sales","Sales Method","Sales method wise total sales"),use_container_width=True)

