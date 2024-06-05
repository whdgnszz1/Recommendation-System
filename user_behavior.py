import os
import pandas as pd
import numpy as np
import json

base_src = 'machine_learning_data'
behavior_src = os.path.join(base_src, 'behavior.csv')

behavior_df = pd.read_csv(behavior_src, encoding='utf-8')

# GA_SESSION_ID가 NaN이 아닌 행만 필터링
behavior_df = behavior_df.dropna(subset=['GA_SESSION_ID'])

# GA_SESSION_ID를 문자열로 변환하여 .0이 붙지 않게 함
behavior_df['GA_SESSION_ID'] = behavior_df['GA_SESSION_ID'].astype(int).astype(str)

# GA_SESSION_ID가 2번 이상 나오는 행들만 필터링
session_counts = behavior_df['GA_SESSION_ID'].value_counts()
multiple_sessions = session_counts[session_counts > 1].index

filtered_multiple_df = behavior_df[behavior_df['GA_SESSION_ID'].isin(multiple_sessions)].copy()

# 원본 데이터프레임에서 행 번호를 새로운 열로 추가
filtered_multiple_df['Original_Row_Index'] = filtered_multiple_df.index

# 새로운 컬럼을 추가하기 위해 필요한 키 목록
keys_of_interest = [
    'page_title', 'page_referrer', 'page_location', 'type', 'title', 'section',
    'search_type', 'search_term', 'ep_page_fullUrl', 'ep_visit_siteOption',
    'ga_session_id', 'ga_session_number'
]

# 모든 데이터를 저장할 데이터프레임
all_sessions_df = pd.DataFrame()

# SEARCH_KEYWORD가 있는 그룹만 저장할 데이터프레임
search_keyword_sessions_df = pd.DataFrame()

# 각 GA_SESSION_ID에 대해 파일 생성
for session_id in multiple_sessions:
    session_df = filtered_multiple_df[filtered_multiple_df['GA_SESSION_ID'] == session_id].copy()

    # 필요한 컬럼만 선택
    selected_columns = ['GA_SESSION_ID', 'Original_Row_Index', 'EVENT_NAME', 'EVENT_REFERRER', 'SEARCH_KEYWORD',
                        'EVENT_PARAMS']
    session_selected_df = session_df[selected_columns].copy()

    # 필요한 키 값들을 위한 컬럼 추가 (dtype을 명시적으로 설정)
    for key in keys_of_interest:
        session_selected_df[key] = pd.Series(dtype='object')

    # EVENT_PARAMS에서 필요한 키의 값을 추출하여 새로운 컬럼으로 추가
    for i, row in session_selected_df.iterrows():
        event_params = json.loads(row['EVENT_PARAMS'])
        for param in event_params:
            if param['key'] in keys_of_interest:
                value = param['value'].get('string_value') or param['value'].get('int_value')
                session_selected_df.loc[i, param['key']] = value

    session_selected_df.drop(columns=['EVENT_PARAMS'], inplace=True)

    # GA_SESSION_ID로 정렬 후 Original_Row_Index로 정렬
    session_selected_df.sort_values(by=['GA_SESSION_ID', 'Original_Row_Index'], inplace=True)

    # 필터링된 데이터프레임을 GA_SESSION_ID.csv 파일로 저장
    output_file = os.path.join(base_src, f'{session_id}.csv')
    session_selected_df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"Filtered data saved to {output_file}")

    # 모든 세션 데이터를 저장할 데이터프레임에 추가
    all_sessions_df = pd.concat([all_sessions_df, session_selected_df], ignore_index=True)

    # 빈 행 추가
    all_sessions_df = pd.concat(
        [all_sessions_df, pd.DataFrame([[''] * all_sessions_df.shape[1]], columns=all_sessions_df.columns)],
        ignore_index=True)

    # SEARCH_KEYWORD가 하나라도 있는지 확인하여 별도의 데이터프레임에 추가
    if session_selected_df['SEARCH_KEYWORD'].notna().any():
        search_keyword_sessions_df = pd.concat([search_keyword_sessions_df, session_selected_df], ignore_index=True)
        # 빈 행 추가
        search_keyword_sessions_df = pd.concat(
            [search_keyword_sessions_df,
             pd.DataFrame([[''] * search_keyword_sessions_df.shape[1]], columns=search_keyword_sessions_df.columns)],
            ignore_index=True)

# 모든 데이터를 합친 파일 저장
all_output_file = os.path.join(base_src, 'all_sessions.csv')
all_sessions_df.to_csv(all_output_file, index=False, encoding='utf-8')

print(f"All sessions data saved to {all_output_file}")

# SEARCH_KEYWORD가 있는 모든 데이터를 합친 파일 저장
search_keyword_output_file = os.path.join(base_src, 'search_keyword_sessions.csv')
search_keyword_sessions_df.to_csv(search_keyword_output_file, index=False, encoding='utf-8')

print(f"Search keyword sessions data saved to {search_keyword_output_file}")
