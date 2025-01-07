import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import font_manager, rc
import sys


def set_korean_font():
    if sys.platform.startswith('darwin'):
        font_name = 'AppleGothic'
    elif sys.platform.startswith('win'):
        font_name = 'Malgun Gothic'
    else:
        font_name = 'NanumGothic'
    rc('font', family=font_name)
    rc('axes', unicode_minus=False)


set_korean_font()

log_file_path = 'full.2025-01-05.log'

log_pattern = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\s+(?P<query>.*?)\s+(?P<response_time>-?\d+)$'
)

timestamps = []
queries = []
response_times = []

with open(log_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            timestamp_str = match.group('timestamp')
            query_str = match.group('query')
            response_time_str = match.group('response_time')

            try:
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                print(f"타임스탬프 변환 오류: {timestamp_str}")
                continue

            try:
                response_time = int(response_time_str)
            except ValueError:
                print(f"응답 시간 변환 오류: {response_time_str}")
                continue

            timestamps.append(timestamp)
            queries.append(query_str)
            response_times.append(response_time)

df = pd.DataFrame({
    'Timestamp': timestamps,
    'Query': queries,
    'ResponseTime': response_times
})

df.sort_values(by='Timestamp', inplace=True)

top_n = 30
top_high = df.nlargest(top_n, 'ResponseTime')
print(f"응답시간이 높은 상위 {top_n}개 쿼리:")
print(top_high[['Timestamp', 'Query', 'ResponseTime']])

plt.figure(figsize=(15, 7))
plt.plot(df['Timestamp'], df['ResponseTime'], marker='o', linestyle='-', color='b', label='응답 시간 (ms)')

plt.title('로그 파일의 응답 시간 시각화')
plt.xlabel('시간')
plt.ylabel('응답 시간 (ms)')
plt.legend()

plt.gcf().autofmt_xdate()

plt.grid(True)

plt.tight_layout()

plt.show()
