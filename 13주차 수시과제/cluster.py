import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import random

# 더미 데이터 생성
data = {
    'Drug_Type': [random.choice(['Cocaine', 'Marijuana', 'Heroin']) for _ in range(1000)],
    'Grams': [random.uniform(0.1, 10.0) for _ in range(1000)],
    'Export_Country': [random.choice(['Colombia', 'Mexico', 'Afghanistan']) for _ in range(1000)],
    'Seller': [random.choice(['A', 'B', 'C']) for _ in range(1000)],
    'Buyer_Gender': [random.choice(['Male', 'Female']) for _ in range(1000)],
    'Buyer_Age': [random.randint(18, 35) for _ in range(500)] + [random.randint(36, 50) for _ in range(300)] + [random.randint(51, 65) for _ in range(200)],
    'Repurchase_Count': [random.randint(5, 10) for _ in range(300)] + [random.randint(0, 4) for _ in range(700)],
}

# Price 조작 부분 수정
data['Price'] = [random.uniform(50.0, 1000.0) if repurchase_count > 5 else random.uniform(1000.0, 5000.0) for repurchase_count in data['Repurchase_Count']]

df = pd.DataFrame(data)
df.to_csv('drug_data_modified.csv', index=False)

# 클러스터링을 위한 특성 선택 및 표준화
features = ['Grams', 'Buyer_Age', 'Repurchase_Count', 'Price']
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 클러스터링 결과 출력
print(df[['Drug_Type', 'Grams', 'Cluster']])

# 클러스터링 시각화
plt.scatter(X_scaled[:, 0], X_scaled[:, 3], c=df['Cluster'], cmap='viridis', alpha=0.5)
plt.xlabel('Buyer_Age')
plt.ylabel('Grams')
plt.show()
