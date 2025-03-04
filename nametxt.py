import re

def correct_name_list(file_name: str) -> list:
    """Функция принимает имя файла и возвращает список имен"""
    with open("data/" + file_name, "r", encoding="utf=8") as name_file:
        names_file = name_file.read().split()
        new_name_list = list()
        for name_item in names_file:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_name_list.append(new_name)

    return new_name_list

def cyrillic_filter_names(name_item: str) -> bool:

    return bool(re.search('[а-яА-Я]', name_item))

def filtered_russian_names(new_name_list: list) -> list:
    russian_names = list()
    for name_item in new_name_list:
        if cyrillic_filter_names(name_item):
            russian_names.append(name_item)

    return russian_names

def filtered_english_names(new_name_list: list) -> list:
    english_names = list()
    for name_item in new_name_list:
        if not cyrillic_filter_names(name_item):
            english_names.append(name_item)

    return english_names

def save_new_file(file_name: str, data: str) -> None:
    with open("data/" + file_name, "w", encoding="utf=8") as new_file:
        new_file.write(data)


a = correct_name_list("names.txt")
filtered_names = filtered_russian_names(a)
save_new_file("russian_names.txt", "\n".join(filtered_names))
filtered_names = filtered_english_names(a)
save_new_file("english_names.txt", "\n".join(filtered_names))
