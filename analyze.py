from fileinput import filename
from unicodedata import name


if __name__ == '__main__':
    # file_name = input('Please input file name:')
    file_name = '2022-6-28.csv'
    with open(file_name, 'r') as f:
        print(f.read())
