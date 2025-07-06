from operator import delitem
import pandas as pd
csv_content = pd.read_csv("Datasets\Iris.csv",delimiter = "," )
# names= ["name","marks","age"],header=None)
print(csv_content.head(2))

print(csv_content)
print()

txt_content = pd.read_csv("test.txt")
print(txt_content.head())

# Excel file
excel_content = pd.read_excel("Datasets\house-price.xlsx", index_col=2)
print(excel_content)

# json file

json_content = pd.read_json("Datasets\titanic.json")
print(json_content)