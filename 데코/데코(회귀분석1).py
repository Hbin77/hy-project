
#학습데이터와 테스트 데이터 분활

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 예제 데이터
np.random.seed(42)  # 랜덤 시드 고정
n_samples = 1000  # 데이터 양을 늘림
lstat = np.random.uniform(low=0, high=10, size=n_samples)
rm = np.random.uniform(low=4, high=8, size=n_samples)

# medv 생성
medv = 20 + 2 * lstat - 1.5 * rm + np.random.normal(loc=0, scale=2, size=n_samples)  # 노이즈 추가


# 데이터프레임 생성
df = pd.DataFrame({'lstat': lstat, 'rm': rm, 'medv': medv})

x_data=df.loc[:, ['lstat', 'rm']]
y_data=df.loc[:, 'medv']
x_train, x_test, y_train, y_test=train_test_split(
    x_data,
    y_data,
    test_size=0.2,
    shuffle=True,
    random_state=12)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

#선형 회귀 모형
lr=LinearRegression()
lr.fit(x_train, y_train)

print("회귀계수(기울기)", np.round(lr.coef_,1))
print("상수항(절편)", np.round(lr.intercept_,1))

#예측값 저장
y_test_pred=lr.predict(x_test)

#예측값과 실제값의 분포
plt.figure(figsize=(10,5)) #표 크기 설정
plt.scatter(x_test['lstat'], y_test, label='y_test') #파란점, 실제값
plt.scatter(x_test['lstat'], y_test_pred, c='r', label='y_pred') #빨간점, 실제값
plt.legend(loc='best') #범례 (오른쪽 상단 박스)가 표시되는 위치 지정
plt.show()

#실제값과 예측값 시각화
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_test_pred, color='blue')
plt.plot_date([y_test.min(), y_test.max()],[y_test.min(), y_test.max()],linestyle='--', color='red')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()
