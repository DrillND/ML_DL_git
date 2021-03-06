import numpy as np # numpy 배열을 더 좋게 관리 하는 라이브러리
import matplotlib.pyplot as plt # 그래프 그리는 데이터 시각화


from sklearn.model_selection import  train_test_split # 훈련데이터 테스트 데이터 나누는 것
from sklearn.neighbors import KNeighborsRegressor #학습 리그레서 최근접이웃좌표 평균값 구해주는 것
from sklearn.linear_model import LinearRegression #선형회귀 모델 예측 클래스 모델

perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

print(perch_length.shape)
print(perch_weight.shape)
print("---------------------------")

train_input,test_input,train_target,test_target = train_test_split(perch_length, perch_weight, random_state=42)

train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)

print(train_input.shape)
print(test_input.shape)

print(train_target.shape)
print(test_target.shape)



knr = KNeighborsRegressor(n_neighbors=3) #가까운점 몇 개
# k-최근접 이웃 회귀 모델을 훈련합니다
knr.fit(train_input, train_target)

print(knr.predict([[50]]))

plt.scatter(train_input,train_target)
plt.scatter(50,knr.predict([[50]]),c='r')

#이웃되는 좌표 3개를 구한다.....
distances, indexes = knr.kneighbors([[50]])
print('dd',indexes)
print(train_input[8])
print(train_target[8])
plt.scatter(train_input[indexes],train_target[indexes], marker='D', c='g')

#plt.plot(train_input,train_target)
plt.xlabel('length')
plt.ylabel('weight')
#plt.show()
#print(knr.kneighbors([[50]]))

lr = LinearRegression()
lr.fit(train_input,train_target)

print(lr.predict([[50]]))
print('a = ',lr.coef_)
print('b = ',lr.intercept_)

plt.scatter([15,50],[15*39-709,50*39-709])
plt.plot([15,50],[15*39-709,50*39-709])
#plt.show()

#다항 회귀

train_poly = np.column_stack((train_input**2,train_input))
test_poly = np.column_stack((test_input**2,test_input))

lr = LinearRegression()
lr.fit(train_poly,train_target)

lr.fit(train_poly,train_target)

lr.predict([[50**2,50]])
print('a b 가중치는 = ', lr.coef_)
print('c 절편 = ',lr.intercept_)

plt.scatter(50,1573, c='blue')
xnumber =np.arange(15,50)
plt.plot(xnumber,1.01*xnumber**2+-21*xnumber+116 )
plt.show()

print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))

import cv2
img=cv2.imread('main.jpg',cv2.IMREAD_COLOR)
rgbimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
plt.imshow(rgbimg)
plt.show()