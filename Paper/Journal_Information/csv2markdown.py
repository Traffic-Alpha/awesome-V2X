'''
@Author: WANG Maonan
@Date: 2023-11-30 00:11:30
@Description: 将 Journal Information CSV 转换为 markdown 的表格
@LastEditTime: 2023-11-30 00:21:58
'''
import csv
import re

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = list(csv.DictReader(file))
    print("CSV file read successfully.")
    return data

def sort_data(data):
    def sort_key(item):
        division_match = re.search(r'\d+', item['中科院分区'])
        division_number = int(division_match.group()) if division_match else float('inf')
        jcr_match = re.search(r'Q(\d)', item['JCR'])
        jcr_number = int(jcr_match.group(1)) if jcr_match else float('inf')
        return division_number, jcr_number
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



# 现在假设你是一个 Python 程序员专家，我会给你一个使用 utf-8 编码的 csv 文件，我希望你可以将 csv 文件转换为 markdown 的格式，同时进行排序。下面是一个例子的 csv 文件：

# ```
# Journal Name,中科院分区,小类, JCR, Impact Factor, Reference Link,其他
# IEEE Transactions on Intelligent Transportation Systems,工程技术 1区,土木/运输科技/电子电气,Q1,8.5,https://ieeexplore.ieee.org/xpl/topAccessedArticles.jsp?punumber=6979,
# Transportation Research Part C: Emerging Technologies,工程技术 1区,运输科技,Q1,8.3,https://www.sciencedirect.com/journal/transportation-research-part-c-emerging-technologies,
# IEEE Transactions on Intelligent Vehicles,工程技术 2区,人工智能/电子与电气/运输科技,Q1,8.2,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=7274857,
# IEEE Transactions on Transportation Electrification,工程技术 1区Top,电子与电气/运输科技,Q1,7,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6687316,
# IEEE Transactions on Vehicular Technology,计算机科学 2区Top,电子与电气/电信/运输技术,Q1,6.5,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=25,
# Transportation Research Part D: Transport and Environment,工程技术 2区,环境研究/交通运输/运输科技,Q1,7.6,https://www.sciencedirect.com/journal/transportation-research-part-d-transport-and-environment,
# IEEE Intelligent Transportation Systems Magazine,工程技术 2区,电子与电气/运输科技,Q2,3.6,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?reload=true&punumber=5117645,
# Computers & Industrial Engineering,工程技术 2区,跨学科应用/工业,Q1,7.9,https://www.sciencedirect.com/journal/computers-and-industrial-engineering,
# Computers & Operations Research,工程技术 2区,跨学科应用/工业/运筹,Q2,4.6,https://www.sciencedirect.com/journal/computers-and-operations-research,
# Journal of Intelligent Transportation Systems,工程技术 2区,交通运输/运输科技,Q2,3.6,https://www.tandfonline.com/journals/gits20,比较慢
# IEEE Open Journal of Intelligent Transportation Systems,,,,2.6,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=8784355,新期刊
# IEEE Intelligent System,计算机科学 3 区,人工智能/电子与电气,Q1,6.4,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=9670,
# IEEE Robotics and Automation Letters,计算机科学 2区,机器人学,Q2,5.9,https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=7083369,
# ```

# 我们希望完成以下的工作：
# - 输入是 csv 文件的路径
# - 首先按照中科院分区中的数字排序，小的在前
# - 如果中科院分区一样，那么按照  JCR Qx 中 x 的大小进行排序，小的在前
# - 同时我希望将 reference link 和 journal name 结合
# - 最后输出为 markdown 表格的形势，同时带有标题和描述