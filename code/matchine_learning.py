import pandas as pd
import numpy as np

'''
movie_data1:没有将result转化为int
movie_data2：转化为int，<0 0   0< <0.2 1   >0.2 2


test_size=0.3
movie_data3:只分》0.2 和《0.2
0.647058823529
0.640138408304
0.612456747405
movie_data4：两天之和
0.655052264808
0.627177700348
0.578397212544
movie_data5：三天之和
0.631578947368
0.645614035088
0.656140350877
movie_data6：四天之和
0.578014184397
0.585106382979
0.581560283688
movie_data7：五天之和
0.539285714286
0.564285714286
0.585714285714
'''

data = pd.read_excel(r'../data/movie_data5.xlsx')

train_x = data[['box', 'profits', 'lasty', 'attendance']].as_matrix()
train_y = data['result1'].as_matrix()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x_tr, x_te, y_tr, y_te = train_test_split(train_x, train_y, test_size=0.3, random_state=0)

lr = LogisticRegression(C=1, tol=1e-6)
lr.fit(x_tr, y_tr)
print(lr.score(x_te, y_te))

from sklearn.svm import SVC

svc = SVC(C=2, kernel='rbf', decision_function_shape='ovo')
svc.fit(x_tr, y_tr)
print(svc.score(x_te, y_te))

from sklearn.ensemble import GradientBoostingClassifier

gdbt = GradientBoostingClassifier(n_estimators=600, max_depth=5, random_state=0)
gdbt.fit(x_tr, y_tr)
print(gdbt.score(x_te, y_te))
