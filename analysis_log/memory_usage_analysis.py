import pandas as pd
import re

input_file = 'memory_usage_result.txt'
output_file = 'memory_usage.xlsx'

data = []

pattern = re.compile(r'^(searchTotal::[^ ]+) => (\d+) bytes$')

with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        match = pattern.match(line)
        if match:
            key = match.group(1)
            memory_usage = int(match.group(2))
            data.append({'key': key, 'memory_usage': memory_usage})
        else:
            error_pattern = re.compile(r'^(searchTotal::[^ ]+) => ERROR')
            error_match = error_pattern.match(line)
            if error_match:
                key = error_match.group(1)
                memory_usage = 0
                data.append({'key': key, 'memory_usage': memory_usage})
            else:
                print(f"Unrecognized line format: {line}")

df = pd.DataFrame(data)

df_filtered = df[df['memory_usage'] > 0]

df_sorted = df_filtered.sort_values(by='memory_usage', ascending=False)

average_memory = df_sorted['memory_usage'].mean()
max_memory = df_sorted['memory_usage'].max()
min_memory = df_sorted['memory_usage'].min()

stats_data = {
    'Statistic': ['평균 메모리 사용량', '최대 메모리 사용량', '최소 메모리 사용량'],
    'Value (bytes)': [average_memory, max_memory, min_memory]
}

df_stats = pd.DataFrame(stats_data)

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_sorted.to_excel(writer, sheet_name='Memory Usage', index=False)
    df_stats.to_excel(writer, sheet_name='Statistics', index=False)

print(f"엑셀 파일이 성공적으로 생성되었습니다: {output_file}")
