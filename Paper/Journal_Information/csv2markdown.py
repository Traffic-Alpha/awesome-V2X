'''
@Author: WANG Maonan
@Date: 2023-11-30 00:11:30
@Description: 将 Journal Information CSV 转换为 markdown 的表格
@LastEditTime: 2023-11-30 00:21:58
'''
import re
import csv

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = list(csv.DictReader(file))
    print("CSV file read successfully.")
    return data

def sort_data(data):
    """对期刊进行排序, 排序按照:
    1. 中科院分区
    2. JCR 分区
    3. 影响因子
    也就是排在越前面的, 影响因子越高, 分区越高.
    """
    def sort_key(item):
        division_match = re.search(r'\d+', item['中科院分区'])
        division_number = int(division_match.group()) if division_match else float('inf')
        jcr_match = re.search(r'Q(\d)', item['JCR'])
        jcr_number = int(jcr_match.group(1)) if jcr_match else float('inf')
        impact_factor_number = float(item['Impact Factor']) if item['Impact Factor'] else float('inf')
        return division_number, jcr_number, 1/impact_factor_number # 这里影响因子越大排在前面, 所以使用 1/impact_factor
    sorted_data = sorted(data, key=sort_key)
    print("Data sorted successfully.")
    return sorted_data

def data_to_markdown(data):
    markdown = "| Journal Name with Link | 中科院分区 | 小类 | JCR | Impact Factor | 其他 |\n"
    markdown += "| --- | --- | --- | --- | --- | --- |\n"
    for row in data:
        journal_link = f"[{row['Journal Name']}]({row['Reference Link']})" if row['Reference Link'] else row['Journal Name']
        markdown += f"| {journal_link} | {row['中科院分区']} | {row['小类']} | {row['JCR']} | {row['Impact Factor']} | {row['其他']} |\n"
    print("Markdown table created successfully.")
    return markdown

def save_markdown(markdown, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown)
    print(f"Markdown file '{filename}' saved successfully.")

if __name__ == '__main__':
    csv_file_path = 'journal_information.csv'
    markdown_file_name = 'journal_information.md'

    csv_data = read_csv(csv_file_path)
    sorted_csv_data = sort_data(csv_data)
    markdown_content = data_to_markdown(sorted_csv_data)
    save_markdown(markdown_content, markdown_file_name)