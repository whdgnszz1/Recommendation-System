import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# 데이터 읽기
df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx',
                   engine="openpyxl")

# 데이터 전처리
df['Description'] = df['Description'].str.strip()  # 공백 제거
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)  # InvoiceNo가 없는 행 제거
df['InvoiceNo'] = df['InvoiceNo'].astype('str')  # InvoiceNo를 문자열로 변환
df = df[~df['InvoiceNo'].str.contains('C')]  # 'C'가 포함된 InvoiceNo 제거

# 프랑스에서 발생한 거래만 선택
basket = (df[df['Country'] == "France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))


# 이진화 함수 정의
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


# 데이터 이진화 및 'POSTAGE' 항목 제거
basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

# 이진화된 데이터 출력
print(basket_sets)

# Apriori 알고리즘 적용
frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
# 연관 규칙 생성
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
# 결과 출력
print(rules.head())

# 조건을 적용하여 필터링
filtered_rules = rules[(rules['lift'] >= 6) & (rules['confidence'] >= 0.8)]

# 필터링된 결과 출력
print(filtered_rules)
