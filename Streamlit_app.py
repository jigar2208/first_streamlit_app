import streamlit

streamlit.title("My Mom's New Healthy Diner") 
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & blueberry oatemeal')
streamlit.text('🥗 Kale, spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build your own fruit smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Grapes'])
fruit_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruit_to_show)

streamlit.header("Fruityvice Fruit Advice!")


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
