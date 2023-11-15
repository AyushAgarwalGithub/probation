import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tt
from sklearn.preprocessing import StandardScaler
import pickle

df=pd.read_csv("Ayush Agarwal.csv")
df.drop(columns="Unnamed: 0",inplace=True)
y=df['price_range']
x=df.drop(columns=["dual_sim","blue",'clock_speed','fc','four_g','int_memory','m_dep','mobile_wt','n_cores','pc','sc_h','sc_w','talk_time','touch_screen','three_g','wifi','price_range'])

x_train,x_test,y_train,y_test = tt(x,y,test_size=.3)
sc=StandardScaler()
X_train = sc.fit_transform(x_train)
X_test= sc.fit_transform(x_test)

algo=LinearRegression()
algo.fit(X_train,y_train)

pickle.dump(algo, open("model.pkl","wb"))