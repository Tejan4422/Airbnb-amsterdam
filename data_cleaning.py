import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('amsterdam2020.csv')

df = df.drop(columns = ['id', 'host_id', 'host_name', 'neighbourhood_group'])
df = df.drop(columns = ['last_review'])
df.to_csv('cleaned_data.csv', index = False)
neighbourhood_list = pd.DataFrame(df.neighbourhood.value_counts())
room_type = df.room_type.value_counts()

df_Centrum_Oost = df[df['neighbourhood']=='Centrum-Oost']
df_Oostelijk_Havengebied_Indische_Buurt = df[df['neighbourhood']=='Oostelijk Havengebied - Indische Buurt']
df_De_Baarsjes_Oud_West = df[df['neighbourhood']=='De Baarsjes - Oud-West']
df_De_Pijp_Rivierenbuurt = df[df['neighbourhood']=='De Pijp - Rivierenbuurt']
df_Centrum_West = df[df['neighbourhood']=='Centrum-West']
df_Westerpark = df[df['neighbourhood']=='Westerpark']
df_Zuid = df[df['neighbourhood']=='Zuid']
df_Oud_Oost = df[df['neighbourhood']=='Oud-Oost']
df_Bos_en_Lommer = df[df['neighbourhood']=='Bos en Lommer']
df_Oud_Noord = df[df['neighbourhood']=='Oud-Noord']
df_Watergraafsmeer = df[df['neighbourhood']=='Watergraafsmeer']
df_IJburg_Zeeburgereiland = df[df['neighbourhood']=='IJburg - Zeeburgereiland']
df_Slotervaart = df[df['neighbourhood']=='Slotervaart']
df_Noord_West = df[df['neighbourhood']=='Noord-West']
df_Buitenveldert_Zuidas = df[df['neighbourhood']=='Buitenveldert - Zuidas']
df_Geuzenveld_Slotermeer = df[df['neighbourhood']=='Geuzenveld - Slotermeer']
df_De_Aker_Nieuw_Sloten  = df[df['neighbourhood']=='De Aker - Nieuw Sloten']
df_Osdorp  = df[df['neighbourhood']=='Osdorp']
df_Gaasperdam_Driemond  = df[df['neighbourhood']=='Gaasperdam - Driemond']
df_Bijlmer_Centrum  = df[df['neighbourhood']=='Bijlmer-Centrum']
df_Bijlmer_Oost  = df[df['neighbourhood']=='Bijlmer-Oost']

df_Centrum_Oost.to_csv('df_Centrum_Oost.csv', index = False)
df_Oostelijk_Havengebied_Indische_Buurt.to_csv('df_Oostelijk_Havengebied_Indische_Buurt.csv', index = False)
df_De_Baarsjes_Oud_West.to_csv('df_De_Baarsjes_Oud_West.csv', index = False)
df_De_Pijp_Rivierenbuurt.to_csv('df_De_Pijp_Rivierenbuurt.csv', index = False)
df_Centrum_West.to_csv('df_Centrum_West.csv', index = False)
df_Westerpark.to_csv('df_Westerpark.csv', index = False)
df_Zuid.to_csv('df_Zuid.csv', index = False)
df_Oud_Oost.to_csv('df_Oud_Oost.csv', index = False)
df_Bos_en_Lommer.to_csv('df_Bos_en_Lommer.csv', index = False)
df_Oud_Noord.to_csv('df_Oud_Noord.csv', index = False)
df_Watergraafsmeer.to_csv('df_Watergraafsmeer.csv', index = False)
df_IJburg_Zeeburgereiland.to_csv('df_IJburg_Zeeburgereiland.csv', index = False)
df_Slotervaart.to_csv('df_Slotervaart.csv', index = False)
df_Noord_West.to_csv('df_Noord_West.csv', index = False)
df_Buitenveldert_Zuidas.to_csv('df_Buitenveldert_Zuidas.csv', index = False)
df_Geuzenveld_Slotermeer.to_csv('df_Geuzenveld_Slotermeer.csv', index = False)
df_De_Aker_Nieuw_Sloten.to_csv('df_De_Aker_Nieuw_Sloten.csv', index = False)
df_Osdorp.to_csv('df_Osdorp.csv', index = False)
df_Gaasperdam_Driemond.to_csv('df_Gaasperdam_Driemond.csv', index = False)
df_Bijlmer_Centrum.to_csv('df_Bijlmer_Centrum.csv', index = False)
df_Bijlmer_Oost.to_csv('df_Bijlmer_Oost.csv', index = False)

