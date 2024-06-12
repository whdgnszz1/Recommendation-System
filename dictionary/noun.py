import pandas as pd
from collections import Counter

# 파일 경로 설정
path_noun_prd = 'dictionary_data/noun_kflow_prd.txt'
path_noun_special = 'dictionary_data/noun_special.txt'
output_path = 'dictionary_data/combined_nouns.xlsx'

# 파일 읽기
with open(path_noun_prd, 'r', encoding='utf-8') as file:
    nouns_prd = file.read().splitlines()

with open(path_noun_special, 'r', encoding='utf-8') as file:
    nouns_special = file.read().splitlines()

# 중복 단어 찾기
nouns_prd_set = set(nouns_prd)
nouns_special_set = set(nouns_special)
nouns_duplicated = list(nouns_prd_set.intersection(nouns_special_set))

# nouns_special에서 중복된 단어 제거
nouns_checklist = list(nouns_special_set - set(nouns_duplicated))

# DataFrames 생성
df_noun_prd = pd.DataFrame(nouns_prd, columns=['noun_prd'])
df_noun_special = pd.DataFrame(nouns_special, columns=['noun_special'])
df_noun_duplicated = pd.DataFrame(nouns_duplicated, columns=['noun_duplicated'])
df_noun_checklist = pd.DataFrame(nouns_checklist, columns=['noun_checklist'])

# 엑셀 파일로 저장
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_noun_prd.to_excel(writer, index=False, sheet_name='noun_kflow_prd')
    df_noun_special.to_excel(writer, index=False, sheet_name='noun_special')
    df_noun_duplicated.to_excel(writer, index=False, sheet_name='noun_duplicated')
    df_noun_checklist.to_excel(writer, index=False, sheet_name='noun_checklist')

print(f'Excel file created at: {output_path}')
