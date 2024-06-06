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

# Line 차트 이해 및 제작
# matplotlib을 이용한 시각화
# line 차트 예제를 위해, tips 데이터에 가상 시간 컬럼 추가하기
# 일요일 데이터만 사용
tips = sns.load_dataset('tips')
sun_tips = tips[tips['day'] == 'Sun']
# print(sun_tips)

# 현재 서버 시간을 얻기 위해 datetime 라이브러리 사용
date = []
today = datetime.date.today()
date.append(today)

for time in range(sun_tips.shape[0] - 1):
    today += datetime.timedelta(1)  # 하루씩 추가
    date.append(today)
sun_tips['date'] = date

# line chart
# plt.plot(sun_tips['date'], sun_tips['total_bill'],
#          linestyle='-',  # 라인 모양
#          linewidth=2,  # 라인 두께
#          color='pink',  # 색상
#          alpha=0.5,  # 투명도
#          )
# plt.title('Total Tips by Date', fontsize=16)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Sum Of Tips', fontsize=14)
# plt.show()

# seaborn을 활용한 시각화
sns.lineplot(data=sun_tips,
             x='date',
             y='total_bill',
             hue='sex',
             )
plt.title('Total Tips by Date & Sex', fontsize=16)
plt.show()
