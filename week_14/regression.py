import sklearn.linear_model
import pandas as pd
import numpy as np

data = pd.read_csv("/Users/mikkel/Git/Python4sem/week_14/car_sales.csv")
data.plot.scatter(x=1, y=2)
xs = data['GDP(trillion)']
ys = data['4wheeler_car_sale']
xs_reshape = np.array(xs).reshape(-1, 1)
print(xs.shape)
print(xs_reshape.shape)

model = sklearn.linear_model.LinearRegression()
model.fit(xs_reshape, ys)
print(model.coef_)
print(model.intercept_)

predicted = model.predict(xs_reshape)
GDP_10 = model.predict([[9]])
print("If GDP hits 9 trillion sales would raise to {}".format(GDP_10[0]))
print(predicted)
