import json
from os import path
import xlsxwriter

data_path = path.join(path.dirname(__file__), 'data')

def find(fn, list):
  for idx in range(0, len(list)):
    element = list[idx]
    if fn(element):
      return (element, idx)
    
  return None

def join(table_left, table_right, key):
    copy_right = table_right.copy()
    result = []

    for row in table_left:
      while True:
        find_result = find(lambda x: x[key] == row[key], copy_right)
        if find_result is None:
          break

        entity_to_join, index = find_result

        del copy_right[index]
        joined = row.copy()
        joined.update(entity_to_join)
        joined.update({"sum": joined["price"]*joined["quantity"]})
        result.append(joined)

    return result

def get_max_column_widths(table):
  max_lengths = {}

  for row in table:
    for col in row:
      try:
        max_lengths[col] = max(max_lengths[col], len(col), len(str(row[col])))
      except:
        max_lengths[col] = 0
  
  return max_lengths

def format_table(table):
  max_lengths = get_max_column_widths(table)
  rows = []
  columns = [f'{col}{(max_lengths[col]-len(col))*" "}' for col in table[0].keys()] if len(table) else []

  for row in table:
    columns_with_spaces = []
    for col in row:
      value = str(row[col])
      spaces = (max_lengths[col]-len(value))*" "
      columns_with_spaces.append(f'{value}{spaces}')
    rows.append(" | ".join(columns_with_spaces))

  headers = " | ".join(columns)
  table = "\n".join(rows)

  return f'{headers}\n{len(rows[0])*"="}\n{table}'

def build_chart_from(table, key1, key2):
  chart_data = {}
  for row in table:
    value1 = row[key1]
    value2 = row[key2]
    if value1 in chart_data:
      chart_data[value1] += value2
    else:
      chart_data[value1] = value2

  max_length = max(chart_data.values())

  return f"{key1}\n" + "\n   ||\n".join([f'{value1} || {chart_data[value1]*"■"}' for value1 in chart_data.keys()][::-1]) + "\n" + (max_length + 6)*"=" + f" {key2}"


with open(path.join(data_path, 'orders.json'), encoding="utf-8") as f:
  orders = json.loads(f.read())

with open(path.join(data_path, 'products.json'), encoding="utf-8") as f:
  products = json.loads(f.read())

joined_table = join(products, orders, 'productID')

formatted_table = format_table(joined_table)

print(formatted_table + "\n\n")

with open(path.join(data_path, 'result.txt'), "w", encoding="utf-8") as f:
  f.write(formatted_table)

with open(path.join(data_path, 'result.json'), "w", encoding="utf-8") as f:
  json.dump(joined_table, f, ensure_ascii=False, indent=4)

chart = build_chart_from(joined_table, 'productID', 'quantity')
print(chart)

book = xlsxwriter.Workbook(path.join(data_path, 'result.xlsx'))
sheet = book.add_worksheet()
max_lengths = get_max_column_widths(joined_table)

for i, row in enumerate(joined_table):
  for j, x in enumerate(row):
    if i == 0:
      sheet.write(i, j, x)
      sheet.set_column(j, j, max_lengths[x] + 2)
    sheet.write(i + 1, j, row[x])
    
book.close()