import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

data=pd.read_csv("decisiont.csv")
#data is in the form of table
print(data)

# table without class labels
x_data = data.drop(columns='playtennis')
# class labels
target =data['playtennis']

# name_features will contain attributes / column names
name_features=x_data.columns

target_labels=target.unique() #[yes ,no

# mapping attributes values to numbers
o={'sunny':0,'overc':1,'rain':2}
data['outlook']=data['outlook'].map(o)

t={'hot':0,'mild':1,'cool':2}
data['temp']=data['temp'].map(t)

h={'high':0,'normal':1}
data['humidity']=data['humidity'].map(h)

w={'weak':0,'strong':1}
data['wind']=data['wind'].map(w)


# new table without class labels in the form of numbers
x_data=data.drop(columns='playtennis')

# spliting into training and test data
x_train,x_test,y_train,y_test=train_test_split(x_data,target,test_size=0.3,random_state=1)

# to construct tree
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(max_depth=3,random_state=1)

dtc.fit(x_train,y_train)

plt.figure(figsize=(30,10),facecolor='b')

Tree=tree.plot_tree(dtc,feature_names=name_features,class_names=target_labels,rounded=True,filled=True,fontsize=14)
plt.show()
