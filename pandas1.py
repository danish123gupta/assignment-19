#q.no.1
import pandas as pd
import numpy as np
d={'Name':['danish','ramesh','veeru'],'Age':[12,20,34],'Email':['gupta.danish236@gmail.com','ramesh123@gmail.com','veer234@gmail']}
df=pd.dataframe(d,index=[1,2,3,4])
print(df)
print(df.axes)
print(df.datatypes)
print(df.shapes)
print(df.values)


#q.no.2
import pandas as pd
import numpy as num
df= pd.read_csv('data.csv')

print([df.head(n=5)])
print([df.head(n=10)])
print("describe",df.describe())
print(df.tail(n=10))

print(df['mintemp'].describe())
print("count",df['mintemp'].count())
print("min",df['mintemp'].min())
print("max",df['mintemp'].max())
print("mean",df['mintemp'].mean())
print("median",df['mintemp'].median())
print("mode",df['mintemp'].mode())
