import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# CSV 파일에서 URL과 레이블을 읽어옵니다.
url_label_data = []
with open('/Users/minchan/Desktop/drug/Main_data.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        url = row['url']
        label = row['label']
        url_label_data.append((url, label))

# Selenium 웹 드라이버를 설정합니다.
driver = webdriver.Chrome()

data_file_path = '/Users/minchan/Desktop/drug/drug.txt'
keywords = []

try:
    with open(data_file_path, 'r') as file:
        # 파일의 각 줄을 읽어와 keywords 배열에 추가합니다.
        for line in file:
            keyword = line.strip()  # 줄 바꿈 문자를 제거하고 키워드를 추출합니다.
            keywords.append(keyword)
except FileNotFoundError:
    print(f'파일을 찾을 수 없습니다: {data_file_path}')
    # 파일을 찾을 수 없는 경우 예외처리합니다.

# 모든 고유 키워드를 추출합니다.
unique_keywords = list(set(keywords))

# 결과를 저장할 CSV 파일을 열고 헤더를 쓰기합니다.
with open('result.csv', 'w', newline='', encoding='utf-8') as result_file:
    fieldnames = ['label'] + unique_keywords
    csv_writer = csv.DictWriter(result_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for url, label in url_label_data:
        # 각 URL을 방문합니다.
        driver.get(url)

        # 페이지 제목을 가져옵니다.
        page_title = driver.title

        # 페이지 제목에 포함된 키워드를 확인합니다.
        keywords_found = set()
        for keyword in unique_keywords:
            if keyword in page_title.lower():
                keywords_found.add(keyword)

        # 결과를 One-Hot Encoding으로 변환합니다.
        one_hot_encoding = {keyword: 1 if keyword in keywords_found else 0 for keyword in unique_keywords}

        # 결과를 CSV 파일에 씁니다.
        row_data = {'label': label}
        row_data.update(one_hot_encoding)
        csv_writer.writerow(row_data)
        sleep(3)

# 웹 드라이버를 종료합니다.
driver.quit()
