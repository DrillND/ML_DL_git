from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
               31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
               35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
               500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
               700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
               7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1] * 35 + [0] * 14

# print(fish_data)
# print(fish_target)

# print(fish_data[5])
# print(fish_data[0:5])
# print(fish_data[:5])
# print(fish_data[44:])

print("============================================================")

train_input = fish_data[:35]
train_target = fish_target[:35]

test_input = fish_data[35:]
test_target = fish_target[35:]

knc = KNeighborsClassifier()
# knc.fit(train_input,train_target)
knc.fit(test_input, test_target)
score = knc.score(test_input, test_target)  # 이 부분????
print(1)
print(score)

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

print("=2222=============================================================")
print(input_arr.shape)  # 두 개의 변수 열이 49행이 있다. 2차원 배열로
print("==============================================================")
np.random.seed(42)  # seed값 ,랜덤값이  정해져서 남들과 똑같이 나온다.
index = np.arange(49)  # [0,1,2,3,4....48]
print(index)
np.random.shuffle(index)
print(index)
'''
32.  12.4 14.3 12.2 33.  36.  35.  35.  38.5 33.5 31.5 29.  41.  30.
 29.  29.7 11.3 11.8 13.  32.  30.7 33.  35.  41.  38.5 25.4 12.  39.5
 29.7 37.  31.  10.5 26.3 34.  26.5
 
 32.  11.8 26.5 26.3 35.  10.5 25.4 31.  29.  41.  39.5 34.  15.  11.2
 14.3 32.  11.  33.  41.  32.  29.  31.5 37.  36.  30.  11.3 12.  30.7
 10.6 31.  33.  13.  33.5 12.4  9.8
 
 29.  32.  33.5 35.  11.2 31.5 13.  30.  14.3 29.7 12.2 35.  26.5 33.
 12.  41.  33.  39.5 10.6 11.  25.4 11.3  9.8 32.  32.  34.5 11.8 31.
 30.  29.  38.5 15.  31.  35.  36. 
'''
print("==============================================================")
print(input_arr)
print(input_arr[[1, 3]])

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

print(train_input.shape)
print(train_target.shape)

print(train_input[:, 0])
print(train_input[:, 1])

plt.scatter(train_input[:, 0], train_input[:, 1]) #0번째 열(길이0), 1번째 열(무게)
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


knc = KNeighborsClassifier()
knc.fit(train_input,train_target)
score =knc.score(test_input,test_target)
print("2222222222222222222222222222222222222222")
print(score)

prevalues = knc.predict(([[10,20],[30,500],[40,300]]))
print("예측값",prevalues)

print(test_input)
prevalues = knc.predict(test_input)
print("예측값",prevalues)
print("실제값",test_target)



'''
fit 학습해라
score 알고리즘 점수
predict 예측값 줘
'''