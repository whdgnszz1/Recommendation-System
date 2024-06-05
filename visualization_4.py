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

# Scatter 차트 이해 및 제작
# matplotlib을 활용한 시각화
tips = sns.load_dataset('tips')
# plt.scatter(tips['total_bill'], tips['tip'],
#             color='pink',  # 색상
#             edgecolor='black',  # 테두리 색깔
#             linewidth=1)  # 라인 두께
# plt.show()

# seaborn을 활용한 시각화
sns.scatterplot(data=tips,
                x='total_bill',
                y='tip',
                style='time',  # 모양 구분으로 다른 변수랑 비교
                hue='day',  # 색깔 구분으로 다른 변수랑 비교
                size='size')  # 크기 구분으로 다른 변수랑 비교
plt.show()
