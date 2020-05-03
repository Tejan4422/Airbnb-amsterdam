import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('cleaned_data_final.csv')
df.describe()


df_dum = pd.get_dummies(df)
X = df_dum.drop('price/night', axis = 1)
y = df_dum.iloc[:,3].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05)


import statsmodels.api as sm
X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
lm = LinearRegression()
lm.fit(X_train, y_train)
np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error', cv =3))


lm_l = Lasso(alpha =.13)
lm_l.fit(X_train, y_train)
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error', cv =3))
y_pred3 = lm_l.predict(X_test)
alpha = []
error = []
for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha = (i)/100)
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring = 'neg_mean_absolute_error', cv =3)))
plt.plot(alpha, error)

from sklearn.svm import SVR
svr = SVR()
svr.fit(X_train, y_train)
np.mean(cross_val_score(svr, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
y_pred = svr.predict(X_test)



from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
y_pred2 = rf.predict(X_test)

from sklearn.neural_network import MLPRegressor
nn = MLPRegressor()
nn.fit(X_train, y_train)
np.mean(cross_val_score(nn, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
y_pred1 = nn.predict(X_test)

