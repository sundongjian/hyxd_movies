'''
进行机器学习处理，打印数据为正确率，即预测为真正例中真正正例的比率
'''
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


data = pd.read_excel(r'../data/movie_data5.xlsx')
train_x = data[['box', 'profits', 'lasty', 'attendance']].as_matrix()
train_y = data['result1'].as_matrix()
x_tr, x_te, y_tr, y_te = train_test_split(train_x, train_y, test_size=0.25, random_state=0)

def accure(a,b):
    accurence=[]
    sum=0
    num=0
    for n in range(0,len(a)):
        if a[n]==1:
            sum+=1
            if b[n]==1:
                num+=1
            accurence.append([{n:b[n]}])
    if sum !=0 and num!=0:
        result=num/sum
    else:
        result=0
    return sum,result


def accure1(a,b):
    accurence=[]
    sum=0
    num=0
    for n in range(0,len(a)):
        if a[n]>0.85:
            sum+=1
            if b[n]==1:
                num+=1
            accurence.append([{n:b[n]}])
    if sum !=0 and num!=0:
        result=num/sum
    else:
        result=0
    return sum,result

def get_repeat(a,b):
    result=0
    for i in range(0,len(a)):
        if a[i]==b[i]==1:
            result+=1
    return result


# lr= LogisticRegression(C=1,tol=1e-6)
# lr.fit(x_tr,y_tr)
# #print(lr.score(x_te,y_te))
# y_pred = lr.predict(x_te)
# # print(y_pred)
# # print(y_te)
# print(accure(y_pred,y_te))
# # print (metrics.f1_score(y_te, y_pred))


svc=SVC(C=1,kernel='rbf',decision_function_shape='ovo')
svc.fit(x_tr,y_tr)
#print(svc.score(x_te,y_te))
y_pred_1 = svc.predict(x_te)
print(y_pred_1)
print(y_te)
print(accure(y_pred_1,y_te))

# from sklearn.ensemble import GradientBoostingClassifier
# gdbt=GradientBoostingClassifier(n_estimators=600,max_depth=10,random_state=0)
# gdbt.fit(x_tr,y_tr)
# #print(gdbt.score(x_te,y_te))
# y_pred = gdbt.predict(x_te)
# # print(y_pred)
# # print(y_te)
# print(accure(y_pred,y_te))
#
# from sklearn.neighbors import KNeighborsClassifier
# kc=KNeighborsClassifier()
# kc.fit(x_tr,y_tr)
# #print(kc.score(x_te,y_te))
# y_pred = kc.predict(x_te)
# # print(y_pred)
# # print(y_te)
# print(accure(y_pred,y_te))
#
# from sklearn.naive_bayes import GaussianNB
# gau=GaussianNB()
# gau.fit(x_tr,y_tr)
# #print(gau.score(x_te,y_te))
# y_pred = gau.predict(x_te)
# # print(y_pred)
# # print(y_te)
# print(accure(y_pred,y_te))
#
# from sklearn.tree import DecisionTreeClassifier
# dec=DecisionTreeClassifier()
# dec.fit(x_tr,y_tr)
# #print(dec.score(x_te,y_te))
# y_pred = dec.predict(x_te)
# # print(y_pred)
# # print(y_te)
# print(accure(y_pred,y_te))


rf = RandomForestRegressor()
rf.fit(x_tr,y_tr)
y_pred_2 = rf.predict(x_te)
# print(rf.score(x_te,y_te))
# print(y_pred)
# print(y_te)
print(accure1(y_pred_2,y_te))