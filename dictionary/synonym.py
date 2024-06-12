import pandas as pd

# 파일 경로 설정
path_synonym_kflow_prd = 'dictionary_data/synonym_kflow_prd.txt'
path_synonym_special = 'dictionary_data/synonym_special.txt'
output_path = 'dictionary_data/combined_synonyms.xlsx'

# 파일 읽기
with open(path_synonym_kflow_prd, 'r', encoding='utf-8') as file:
    synonym_kflow_prd = file.read().splitlines()

with open(path_synonym_special, 'r', encoding='utf-8') as file:
    synonym_special = file.read().splitlines()


# 단방향 변환 함수
def convert_to_unidirectional(synonym_list, delimiter=','):
    unidirectional_pairs = []
    for line in synonym_list:
        if '=>' in line:
            parts = line.split('=>')
            primary = parts[0]
            others = parts[1].split(delimiter)
        else:
            parts = line.split(delimiter)
            primary = parts[0]
            others = parts[1:]

        for synonym in others:
            unidirectional_pairs.append((primary.strip(), synonym.strip()))

    return unidirectional_pairs


# synonym_kflow_prd 변환
unidirectional_kflow_prd = convert_to_unidirectional(synonym_kflow_prd)

# synonym_special 변환
unidirectional_special = convert_to_unidirectional(synonym_special)

# DataFrames 생성
df_synonym_kflow_prd = pd.DataFrame(unidirectional_kflow_prd, columns=['term', 'synonym'])
df_synonym_special = pd.DataFrame(unidirectional_special, columns=['term', 'synonym'])

# df_synonym_special에서 df_synonym_kflow_prd을 뺀 값 찾기
df_special_only = df_synonym_special[~df_synonym_special.isin(df_synonym_kflow_prd.to_dict('list')).all(axis=1)]


# 단방향 변환된 쌍을 하나의 셀에 결합하는 함수
def format_unidirectional_pairs(pairs):
    result = {}
    for term, synonym in pairs:
        if term in result:
            result[term].append(synonym)
        else:
            result[term] = [synonym]

    formatted_list = [f"{term}=>{','.join(synonyms)}" for term, synonyms in result.items()]
    return formatted_list


# df_special_only 내용을 단방향으로 변환하고 하나의 셀에 결합
synonym_checklist_pairs = convert_to_unidirectional(df_special_only.apply(lambda x: ','.join(x), axis=1).tolist())
synonym_checklist = format_unidirectional_pairs(synonym_checklist_pairs)

# DataFrame 생성
df_synonym_checklist = pd.DataFrame(synonym_checklist, columns=['synonym_checklist'])

# 엑셀 파일로 저장
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_synonym_kflow_prd.to_excel(writer, index=False, sheet_name='synonym_kflow_prd')
    df_synonym_special.to_excel(writer, index=False, sheet_name='synonym_special')
    df_special_only.to_excel(writer, index=False, sheet_name='special_only')
    df_synonym_checklist.to_excel(writer, index=False, sheet_name='synonym_checklist')

print(f'Excel file created at: {output_path}')
