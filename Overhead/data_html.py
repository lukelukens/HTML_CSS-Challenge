import pandas as pd

cities_data = "Resources/cities.csv"
cities_df=pd.read_csv(cities_data).set_index("City_ID")
cities_df.to_html('cities_data.html')