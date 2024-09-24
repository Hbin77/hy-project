import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# 예제 데이터 생성
np.random.seed(42)
lengths = np.random.uniform(low=20, high=50, size=100)  # 농어 길이 (입력)
weights = 500 + 10 * lengths + np.random.normal(loc=0, scale=5, size=100)  # 농어 무게 (타깃)

# 데이터 분할
train_input, test_input, train_target, test_target = train_test_split(
    lengths, weights, test_size=0.2, random_state=42
)

# 선형 회귀 모델 훈련
lr = LinearRegression()
lr.fit(train_input, train_target)

# 50cm 농어에 대한 예측
predicted_weight = lr.predict([[50]])
print(predicted_weight)

print(lr.coef_, lr.intercept_)

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 15에서 50까지 1차 방정식 그래프를 그립니다
plt.figure(figsize=(10, 6))
plt.plot(15, 50, 15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_)
# 선형 회귀 모델을 사용하여 예측한 값을 그립니다.
plt.plot(np.arange(15, 51), lr.predict(np.arange(15, 51).reshape(-1, 1)), color='red')
# 50cm 농어 데이터
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel ('weight')
plt.show()

#훈련 세트와 테스트 세트에 대한 R^점수 확인
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

#넘파이를 이용하여 길이를 제곱한 항 구하기
train_poly=np.column_stack((train_input**2, train_input))
test_poly=np.column_stack((train_input**2, train_input))

print(train_poly.shape, test_poly.shape)

#train_poly를 사용해 선형 회귀 모델을 다시 훈련
lr = LinearRegression()
lr.fit(train_poly, train_target)

print(lr.predict([[50**2,50]]))

#2차 방정식의 계수와 절편 a,b,c를 사용하여 산점도 그리기
point = np.arange(15, 50)
# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 15에서 49까지 2차 방정식 그래프를 그립니다
plt.plot(point, 1.01*point**2 - 21.6*point + 116.05)
plt.scatter([50], [1574], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))



