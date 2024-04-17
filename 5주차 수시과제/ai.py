import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# CSV 파일을 읽어옵니다.
data = pd.read_csv('/Users/minchan/Desktop/drug/result.csv')

# 레이블을 타겟으로 선택합니다.
y = data['label']

# 특성 데이터를 선택합니다.
X = data.drop(columns=['label'])

# 데이터를 훈련 세트와 테스트 세트로 분할합니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Naive Bayes 모델을 생성하고 훈련합니다.
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# 테스트 데이터로 모델을 평가합니다.
y_pred = nb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'정확도: {accuracy:.2f}')
