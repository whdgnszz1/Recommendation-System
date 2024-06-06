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

# Pie 차트 이해 및 제작
# matplotlib을 이용한 시각화
tips = sns.load_dataset('tips')
sum_tip_by_day = tips.groupby('day')['tip'].sum()
ratio_tip_by_day = sum_tip_by_day / sum_tip_by_day.sum()

x_label = ['Thu', 'Fri', 'Sat', 'Sun']

plt.pie(ratio_tip_by_day,  # 비율값
        labels=x_label,  # 라벨값
        autopct='%.2f%%',  # 부채꼴 안에 표시될 숫자 형식(소수 2자리까지 표시)
        startangle=90,  # 축이 시작되는 각도 설정
        counterclock=True,  # True: 시계방향순, False: 반시계방향
        explode=[0.05, 0.05, 0.05, 0.05],  # 중심에서 벗어나는 정도 표시
        shadow=True,  # 그림자 표시 여부
        # colors=['gold', 'silver', 'whitesmoke', 'gray'],
        wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 3})  # 도넛 차트를 그릴 때 사용
plt.show()
