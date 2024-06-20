import pandas as pd

def update_excel_file(input_file_path, output_file_path):
    # 엑셀 파일 읽기
    df = pd.read_excel(input_file_path, engine='openpyxl')

    # 열 이름 출력
    print("Columns in the file:", df.columns.tolist())

    # 'C' 열을 추가하여 초기화
    df['C'] = ''

    # 실제 열 이름을 'A', 'B', 'C'로 변경
    df.columns = ['A', 'B', 'C']

    # B 열의 내용이 비어있지 않은 경우 A 열로 덮어쓰기
    df['A'] = df['B'].combine_first(df['A'])

    # A 열 중 '=>'가 포함된 내용들을 C 열에 덮어쓰기
    df['C'] = df.apply(lambda row: row['A'] if '=>' in str(row['A']) else row['C'], axis=1)

    # B 열의 내용 삭제
    df['B'] = ''

    # 수정된 데이터프레임을 새로운 엑셀 파일로 저장
    df.to_excel(output_file_path, index=False, engine='openpyxl')

def main():
    input_file_path = 'synonym_to_noun_analyzed.xlsx'
    output_file_path = 'synonym_to_noun_analyzed_update.xlsx'
    update_excel_file(input_file_path, output_file_path)

if __name__ == '__main__':
    main()
