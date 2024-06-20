import json
import os
import re
import requests
import pandas as pd

dataPath = "./data"

def getDicListFromFile(filePath):
    results = []
    with open(filePath, 'r', encoding='utf-8') as file:
        results = [line.strip() for line in file]
    return results

def getNoriAnalysisResult(text):
    username = 'admin'
    password = 'asdf1234'

    url = 'http://localhost:9200/test-jh/_analyze'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "analyzer": "nori",
        "text": text
    }

    response = requests.get(url, headers=headers, auth=(username, password), json=data, verify=False)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print("API 요청 실패: " + str(response.status_code))
        return None

def parseTokenFromAnalyzeResult(analyzed_result):
    if not analyzed_result:
        return []
    token_data = analyzed_result.get('tokens', [])
    tokens = [item.get('token') for item in token_data]
    return tokens

def dataframeToExcel(excel_file_path, df):
    df.to_excel(excel_file_path, index=False, engine='openpyxl')

def makeSynonymToNounAnalysis():
    df = pd.DataFrame(columns=['synonym', 'analyzed'])

    synonym_list = getDicListFromFile("./dictionary_data/synonym_kflow_prd.txt")

    for synonym in synonym_list:
        if '=>' not in synonym:
            continue
        original, synonyms = synonym.split('=>')
        synonym_tokens = synonyms.split(',')

        df.loc[len(df)] = [f'{original} => {",".join(synonym_tokens)}', '']

        for token in synonym_tokens:
            analyze_result = getNoriAnalysisResult(token)
            analyzed_token = ' '.join(parseTokenFromAnalyzeResult(analyze_result))
            df.loc[len(df)] = [analyzed_token, '']

        df.loc[len(df)] = ['', '']

    excel_name = 'synonym_to_noun.xlsx'
    excel_path = os.path.join("./", excel_name)
    dataframeToExcel(excel_path, df)

def main():
    makeSynonymToNounAnalysis()

if __name__ == '__main__':
    main()
