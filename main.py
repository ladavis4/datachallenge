import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

path = "C:/Users/ladav/PycharmProjects/DataChallenge/Data_Lv2_NCSG_BehaviorChangesCOVID19.csv"

df = pd.read_csv(path, encoding='cp1252')

ages = df['Age'].astype(int)
kids = df['Kids'].astype(int)
plt.scatter(ages, kids)
plt.show()




