import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import plot 


df = pd.read_csv('cleaned_data.csv')

df['price/night'] = (df.price/df.minimum_nights)
df = df.drop(columns = ['price', 'minimum_nights', 'name', 'latitude', 'longitude',
                   'availability_365'])

df.isnull().sum(axis = 0)
df.reviews_per_month.isna()
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

#pivot table of price distribution
roomtype_price = pd.pivot_table(df, index = 'room_type', values = 'price/night')
roomtype_price = roomtype_price.reset_index()
colors = ['#708090', '#A9A9A9', '#7FFFD4', '#FF7F50']
plt.pie(roomtype_price['price/night'], colors = colors, labels = roomtype_price['room_type'],
         autopct='%1.0f%%')
plt.title('Price distribution of room types')
plt.savefig('piechart_priceDist.png', dpi = 100)
plt.show()  


neighbourhood_price = pd.pivot_table(df, index = ['neighbourhood', 'room_type'], values = 'price/night')
neighbourhood_price = neighbourhood_price.reset_index()
neighbourhood_price['neighbourhood'] = (neighbourhood_price.neighbourhood +' ' + neighbourhood_price.room_type)
neighbourhood_price = neighbourhood_price.drop(columns = ['room_type'])



fig = px.bar(neighbourhood_price[['neighbourhood', 'price/night']].sort_values('price/night', ascending = 'False'),
            y = 'price/night', x = 'neighbourhood', color = 'neighbourhood', log_y = True,
             template = 'ggplot2', title = 'neighbourhood vs price/night')
plot(fig)

df.to_csv('cleaned_data_final.csv', index = False)



