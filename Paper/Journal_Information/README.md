<!--
 * @Author: WANG Maonan
 * @Date: 2023-11-30 00:24:02
 * @Description: 期刊介绍
 * @LastEditTime: 2023-11-30 00:33:18
-->
# Journal Information

This repository is a collection of journals relevant to the field of Intelligent Transportation Systems (ITS). For detailed journal information, click [Journal Information](./journal_information.md).

## How to Contribute

To add new journal entries, please update the [journal_information.csv](./journal_information.csv) file with the following details:
- `Journal Name`: The name of the journal.
- `中科院分区` (Chinese Academy of Sciences Division): The division of the journal according to the Chinese Academy of Sciences.
- `小类` (Subcategory): The subcategory under the journal's division, which helps in further searching for other journals.
- `JCR`: The Journal Citation Reports division of the journal.
- `Impact Factor`: The impact factor of the journal.
- `Reference Link`: The official website link of the journal.
- `其他` (Other): Any additional remarks, such as peer review time or difficulty level.

## Convert to Markdown Format

After updating the CSV file, run the following command to convert the `csv` file into a markdown format:

```bash
python csv2markdown.py
```

You will see the following output indicating the process has been completed successfully:

```
CSV file read successfully.
Data sorted successfully.
Markdown table created successfully.
Markdown file 'journal_information.md' saved successfully.
```

---

# 期刊信息

本仓库主要收集智慧交通系统（ITS）领域相关的期刊信息。具体期刊信息请点击 [期刊信息](./journal_information.md)。

## 如何贡献

若需添加新的期刊条目，请在 [journal_information.csv](./journal_information.csv) 文件中更新以下信息：
- `Journal Name`：期刊名称。
- `中科院分区`：根据中国科学院的分区。
- `小类`：期刊所属中科院分区下的小类别，便于进一步搜索其他期刊。
- `JCR`：期刊的 JCR 分区。
- `Impact Factor`：期刊的影响因子。
- `Reference Link`：期刊官方网站链接。
- `其他`：任何附加说明，如同行评审时间或难度等级。

## 转换为 Markdown 格式

更新 CSV 文件后，运行以下命令将 `csv` 文件转换为 markdown 格式：

```bash
python csv2markdown.py
```

您将看到以下输出，表明过程已成功完成：

```
CSV file read successfully.
Data sorted successfully.
Markdown table created successfully.
Markdown file 'journal_information.md' saved successfully.
```
