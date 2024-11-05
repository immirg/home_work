import csv
import os


def create_csv():
    # везде создал file_path потому что без полного прописывания пути выдавало ошибку
    file_name = 'random.csv'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as first_csv_file:
        reader = list(csv.reader(first_csv_file))
        title = reader[0]

    file_name = 'result_merged_unique.csv'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(title)


def write_csv(elem):
    file_name = 'result_merged_unique.csv'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(elem)


def is_unique(data):
    file_name = 'result_merged_unique.csv'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as file:
        reader = list(csv.reader(file))
        for line in reader:
            if str(line) == str(data):
                return False
        write_csv(elem=data)


def read_csv(file, num):
    file_path = os.path.join(os.path.dirname(__file__), file)
    with open(file_path, 'r') as csv_file:
        reader = list(csv.reader(csv_file))
        for line in reader[num:]:
            if line:
                is_unique(data=line)


create_csv()
read_csv(file='random.csv', num=4)
read_csv(file='random-michaels.csv', num=1)
