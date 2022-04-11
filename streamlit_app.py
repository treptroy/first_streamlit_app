import streamlit

streamlit.title('My mom\'s New Healthy Diner')

streamlit.header ('Breakfast Favorites')
streamlit.text ('🥣omega 3 & blueberry oatmeal')
streamlit.text ('🥗kale kale, Spinach & Rocket smoothie')
streamlit.text (':star: Hard-boiled Free Range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('my own fruits')
streamlit.text (':grapes:pears & guava')
streamlit.text(':mango:')
streamlit.text(':apple:')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))
