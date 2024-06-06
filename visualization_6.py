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

# Box 차트 이해 및 제작
# 이상치를 확인할때 주로 사용
# matplotlib을 활용한 시각화
# plt.boxplot(tips['tip'],
#             sym='rs',  # 아웃라이어를 어떻게 표시할지? red square
#             )
# plt.title('Box Plot for Tip', fontsize=16)
# plt.xlabel('tip', fontsize=14)
# plt.ylabel('tip size', fontsize=14)
# plt.show()

# seaborn 을 활용한 시각화
sns.boxplot(data=tips,
            x='day',
            y='tip',
            hue='smoker',
            linewidth=2,
            order=['Sun', 'Sat', 'Fri', 'Thur']
            )
plt.title('Box Plot for Tip', fontsize=16)
plt.xlabel('tip', fontsize=14)
plt.ylabel('tip size', fontsize=14)
plt.show()
