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


file = (correct_file_name("names.txt"))

for i in file:
    print(i)