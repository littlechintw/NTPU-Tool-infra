import json
import xlrd

def get_data_positive_take(json_file):
    workbook = xlrd.open_workbook('./dorm_data.xlsx')
    booksheet = workbook.sheet_by_index(0)
    rows = booksheet.get_rows()
    rows_num = booksheet.nrows
    for i in range(1,rows_num):
        data_list = booksheet.row_values(i)
        print('--------------')
        print('Now print ' + str(i) + ' data!')
        print('--------------')
        mes = data_list[0] + ' ' + data_list[1] + ' 第 ' + str(int(data_list[2])) + ' 床'
        tmp_json = {str(int(data_list[3])): mes}
        json_file.append(tmp_json)
    return json_file

def get_data_waiting(json_file):
    workbook = xlrd.open_workbook('./dorm_data.xlsx')
    booksheet = workbook.sheet_by_index(1)
    rows = booksheet.get_rows()
    rows_num = booksheet.nrows
    for i in range(1,rows_num):
        data_list = booksheet.row_values(i)
        print('--------------')
        print('Now print ' + str(i) + ' data!')
        print('--------------')
        mes = data_list[2] + '第 ' + str(int(data_list[0])) + ' 位'
        tmp_json = {str(int(data_list[1])): mes}
        json_file.append(tmp_json)
    return json_file

json_file = []
json_file = get_data_positive_take(json_file)
json_file = get_data_waiting(json_file)

with open('dorm_id_list_20200826.json', 'w', encoding="utf8") as outfile:
    json.dump(json_file, outfile, ensure_ascii=False)