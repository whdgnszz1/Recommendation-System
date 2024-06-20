import pandas as pd

def update_excel_file(input_file_path, output_file_path):
    # 엑셀 파일 읽기
    df = pd.read_excel(input_file_path, engine='openpyxl')

    # 열 이름 출력
    print("Columns in the file:", df.columns.tolist())

    # 필요한 열만 선택 (여기서는 첫 번째 열과 두 번째 열만 필요하다고 가정)
    df = df[['A', 'B']]

    # 첫 번째 열의 값 중 "=>"가 포함되지 않은 값들을 공백(" ")으로 나누고
    # 두 개 이상으로 나누어지는 값들을 하나의 단어로 이어붙여서 두 번째 열에 넣기
    df['B'] = df.apply(lambda row: ''.join(str(row['A']).split()) if '=>' not in str(row['A']) and len(str(row['A']).split()) > 1 else row['B'], axis=1)

    # 수정된 데이터프레임을 새로운 엑셀 파일로 저장
    df.to_excel(output_file_path, index=False, engine='openpyxl')

def main():
    input_file_path = './dictionary_data/synonym_to_noun_job.xlsx'
    output_file_path = './dictionary_data/synonym_to_noun_job_updated.xlsx'
    update_excel_file(input_file_path, output_file_path)

if __name__ == '__main__':
    main()
