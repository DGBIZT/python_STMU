import re

def correct_file_name(name_file: str) -> list:
    new_name_file = list()
    with open('data/' + name_file, "r", encoding= 'utf-8') as file_list:
        list_file = file_list.read().split()

        for name_item in list_file:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_name_file.append(new_name)

        return new_name_file

def filter_russian_names(name_item: str) -> bool:
    return bool(re.search("[а-яА-Я]", name_item))

def russian_names(list_file: list) -> list:
    new_rus_list = list()
    for name_item in list_file:
        if filter_russian_names(name_item):
            new_rus_list.append(name_item)
    return new_rus_list

def english_names(list_file: list) -> list:
    new_english_list = list()
    for name_item in list_file:
        if not filter_russian_names(name_item):
            new_english_list.append(name_item)
    return new_english_list



file = (correct_file_name("names.txt"))

for i in file:
    print(i)

print(russian_names(file))
print(english_names(file))