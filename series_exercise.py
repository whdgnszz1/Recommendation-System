import pandas as pd
import numpy as np

# 조회 <= 인덱스 사용 이유 => 데이터 정렬
# 인덱스가 있다. pd는 np보다 느리기 때문에 굳이 Series를 사용할 필요는 없다.
# print(pd.Series([1, 2, 3]))
# 인덱스가 없다. np는 연산하기 좋은 라이브러리
# print(np.array([1, 2, 3]))


# pd.Series 함수를 통해서 만드는 것도 가능
# series = pd.Series([1, 2, 3, 4])
# print(series)

# pd.Series의 옵션이 무엇이 있는지 확인
# index => 할당값의 이름 지정, 중복 가능 ['a', 'a', 'b', 'c']
# dtype => 대표적: int, float, string, boolean 등
# series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], dtype=float)
# print(series)

# series = pd.Series([10, 2, 5, 4], index=['a', 'b', 'c', 'd'], dtype=float)
# print(series.sort_values(ascending=True))

# DataFrame 실습
# 헝가리안 표기법 => x, y, z, test, test1, df 같은 표기법은 절대xxxxx
# df = pd.DataFrame({'a': [2, 3], 'b': [5, 10], 'z': [2, 3], 'd': [5, 10], 'w': [2, 3], 'h': [5, 10]})
# print(df)

# new_dict = {'a': 2, 'b': 3, 'z': 4}
# for item, value in new_dict.items():
#     print('item : ', item)
#     print('value : ', value)

# df = pd.DataFrame([[2, 5], [3, 10], [10, 20]], columns=['a', 'b'])
# print(df)

df = pd.DataFrame([[2, 5, 100], [3, 10, 200], [10, 20, 300]],
                  columns=['a', 'b', 'c'],
                  index=['가', '나','다'],
                  dtype=float
                  )
print(df)