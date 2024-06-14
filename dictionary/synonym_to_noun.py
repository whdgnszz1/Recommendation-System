import pandas as pd

# 파일 경로 설정
path_noun_kflow_prd = 'dictionary_data/noun_kflow_prd.txt'
path_synonym_kflow_prd = 'dictionary_data/synonym_kflow_prd.txt'
output_path = 'dictionary_data/synonym_to_noun.xlsx'
output_txt_path = 'dictionary_data/noun.txt'

# 파일 읽기
with open(path_noun_kflow_prd, 'r', encoding='utf-8') as file:
    noun_kflow_prd = file.read().splitlines()

with open(path_synonym_kflow_prd, 'r', encoding='utf-8') as file:
    synonym_kflow_prd = file.read().splitlines()

# 공백 제거
noun_kflow_prd = [noun.strip() for noun in noun_kflow_prd]
synonym_kflow_prd = [line.strip() for line in synonym_kflow_prd]

# 명사 세트로 변환
noun_set = set(noun_kflow_prd)

# 새로운 명사 추출
new_nouns_set = set()
for line in synonym_kflow_prd:
    if '=>' in line:
        synonyms = line.split('=>')[1].split(',')
        for synonym in synonyms:
            synonym = synonym.strip()
            if synonym and synonym not in noun_set:
                new_nouns_set.add(synonym)

# 새로운 명사 리스트를 정렬하여 데이터프레임으로 변환, 글자 길이가 1인 단어 제외
sorted_new_nouns_list = sorted([noun for noun in new_nouns_set if len(noun) > 1])
df_new_nouns = pd.DataFrame(sorted_new_nouns_list, columns=['New Nouns'])

# 기존 명사 리스트를 정렬하여 데이터프레임으로 변환
sorted_present_nouns_list = sorted([noun for noun in noun_kflow_prd if noun])
df_present_nouns = pd.DataFrame(sorted_present_nouns_list, columns=['Present Nouns'])

# 기존 명사와 새로운 명사를 합친 후 중복 제거, 특정 단어 제외
excluded_words = {'천재교육', '확률과통계', 'C#'}
combined_nouns_set = noun_set.union(new_nouns_set) - excluded_words

# 빈 문자열이 아닌 값만 포함하도록 필터링, 공백 제거, 글자 길이가 1인 단어 제외
combined_nouns_set = {noun.strip() for noun in combined_nouns_set if noun.strip() and len(noun.strip()) > 1}

# 정렬된 Combined Nouns 리스트
sorted_combined_nouns_list = sorted(list(combined_nouns_set))
df_combined_nouns = pd.DataFrame(sorted_combined_nouns_list, columns=['Combined Nouns'])

# 엑셀 파일로 저장
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_present_nouns.to_excel(writer, sheet_name='Present Nouns', index=False, header=False)
    df_new_nouns.to_excel(writer, sheet_name='New Nouns', index=False, header=False)
    df_combined_nouns.to_excel(writer, sheet_name='Combined Nouns', index=False, header=False)

# Combined Nouns를 텍스트 파일로 저장
with open(output_txt_path, 'w', encoding='utf-8') as file:
    for noun in sorted_combined_nouns_list:
        file.write(f"{noun}\n")

print(f"Present nouns, new nouns, and combined nouns have been saved to {output_path}")
print(f"Combined nouns have been saved to {output_txt_path}")
