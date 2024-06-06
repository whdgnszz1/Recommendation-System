import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import datetime

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

tips = sns.load_dataset('tips')

# Histogram 차트 이해 및 제작
# 변수에 대한 분포를 확인할 때 사용한다.

# matplotlib을 활용한 시각화
# print(plt.hist(tips['total_bill'],
#                bins=30,  # 개수
#                density=True,  # 비율적으로 시각화
#                alpha=0.7,
#                color='pink',
#                edgecolor='black',
#                linewidth=0.9
#                ))
# plt.title('Histogram for total_bill')
# plt.xlabel('total_bill')
# plt.ylabel('rate')
# plt.show()

# seaborn을 활용한 시각화
sns.histplot(data=tips,
             x='total_bill',
             bins=30,
             kde=True,  # kernel density estimation
             hue='sex',  # 색깔 구분
             multiple='stack',  # stack: 겹쳐서 보이는 것이 아닌 밟고 올라가서 , dodge = 따로따로
             shrink=0.6,  # bean의 두께 조절
             )
plt.title('Histogram for total_bill by sex')
plt.xlabel('total_bill')
plt.ylabel('rate')
plt.show()
