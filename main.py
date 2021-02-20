import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

path = "C:/Users/ladav/ew430/datachallenge/Data_Lv2_NCSG_BehaviorChangesCOVID19.csv"

df = pd.read_csv(path, encoding='cp1252')

ages = df['Age']
kids = df['Kids']
plt.hist(ages, bins=20)
plt.show()




