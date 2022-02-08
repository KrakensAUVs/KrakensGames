from toolbox import read_new_line, create_client_list

with open('consumers.csv', "r", encoding='utf-8') as data:
    labels = read_new_line(data)
    line = read_new_line(data)
    a = 1
    client_list = create_client_list(labels, line, data)
