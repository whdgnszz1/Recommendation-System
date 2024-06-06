import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from matplotlib import font_manager, rc
import platform

# 한글 폰트 설정
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':  # macOS의 경우
    rc('font', family='AppleGothic')
else:  # 기타 OS의 경우
    rc('font', family='NanumGothic')  # 예시로 나눔고딕 사용

# 마이너스 폰트 설정
plt.rcParams['axes.unicode_minus'] = False

# 경고 무시
warnings.filterwarnings('ignore')

# 기본 스타일 설정
plt.rcParams['figure.figsize'] = [10, 8]
sns.set(style='whitegrid')
sns.set_palette('pastel')

# Loading 'Tips' dataset from seaborn
tips = sns.load_dataset('tips')
# print(tips.head())
# print(tips.shape)

# matplotlib을 활용한 시각화
sum_tip_by_day = tips.groupby('day')['tip'].sum()

x_label = ['Thu', 'Fri', 'Sat', 'Sun']
x_label_index = np.arange(len(x_label))

# Bar 차트 이해 및 제작
# plt.bar(x_label, sum_tip_by_day,
#         color='pink',  # 색 지정
#         alpha=0.6,  # 색 투명도
#         width=0.3,  # 너비
#         align='edge')  # 배치
# plt.xlabel('Days', fontsize=14)
# plt.ylabel('Sum Of Tips', fontsize=14)
# plt.title('Sum Of Tips By Days')
# plt.xticks(x_label_index,
#            x_label,
#            rotation=45,
#            fontsize=15)
# plt.show()

# seaborn을 활용한 시각화
sns.barplot(data=tips,  # 데이터 프레임
            x='day',  # x 변수
            y='tip',  # y 변수
            estimator=np.sum,  # np.median, np.average도 가능
            hue='sex',  # 색깔 구분으로 특정 컬럼값 비교하고 싶을때
            order=['Sun', 'Sat', 'Fri', 'Thur'],  # 순서
            edgecolor='.6',  # 바 모서리 선명도
            linewidth=2.5)  # 모서리 두께
plt.xlabel('Days', fontsize=14)
plt.ylabel('Sum Of Tips', fontsize=14)
plt.title('Sum Of Tips By Days', fontsize=16)
plt.show()
