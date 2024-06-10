from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding = "utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding = "utf-8") as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

# input_data()

def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding = "utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append("".join(data_first[j:i+1]))
                j = i
        print("".join(data_first_list))
    print("Вывожу данные из 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding = "utf-8") as f:
        data_second = f.readlines()
        print(*data_second)

# print_data()

def delete_data():
    print("Из какого файла нужно удалить данные? \n 1 - data_first_variant \n 2 - data_second_variant")
    command = int(input("Введите число: "))
    while command != 1 and command != 2:
        print("Файл отсутствует")
        command = int(input("Введите число: "))
    filename = "data_first_variant.csv" if command == 1 else "data_second_variant.csv"
    with open(filename, "r", encoding = "utf-8") as f:
        lines = f.readlines()
        records = []
        record = []
        for i in range(len(lines)):
            line = lines[i]
            #print(line)
            record.append(line)
            if line == "\n" or i == len(lines) - 1:
                records.append(list(record))
                record.clear()
    #print(records)
        records_len = len(records)
        print(f"Доступно {records_len} записей")
        record_number = int(input("Введите номер записи, которую хотите удалить: "))
        if record_number < 1 or record_number > len(records):
            print("Запись с таким номером отсутствует")
            return
    #print(records[ record_number - 1])
        for i in range(len(records)):
            if i + 1 == record_number:
                #print(records[i])
                del records[i]
        #print(*records)
    with open(filename, "w", encoding = "utf-8") as f:
        for record in records:
            f.write("".join(record))

# delete_data()
        
def change_data():
    print("В каком файле нужно изменить данные? \n 1 - data_first_variant \n 2 - data_second_variant")
    command = int(input("Введите число: "))
    while command != 1 and command != 2:
        print("Файл отстутствует")
        command = int(input("Введите число: "))
    filename = "data_first_variant.csv" if command == 1 else "data_second_variant.csv"
    delimiter = "\n" if command == 1 else ";"
    with open(filename, "r", encoding = "utf-8") as f:
        lines = f.readlines()
        records = []
        record = []
        for i in range(len(lines)):
            line = lines[i]
            #print(line)
            record.append(line)
            if line == "\n" or i == len(lines) - 1:
                records.append(list(record))
                record.clear()
    #print(records)
        records_len = len(records)
        print(f"Доступно {records_len} записей")
        record_number = int(input("Введите номер записи, которую хотите изменить: "))
        if record_number < 1 or record_number > len(records):
            print("Запись с таким номером отсутствует")
            return
        add_name = name_data()
        add_surname = surname_data()
        add_phone = phone_data()
        add_address = address_data()
        new_record = add_name + delimiter \
                + add_surname + delimiter \
                + add_phone + delimiter \
                + add_address + "\n\n"
        for i in range(len(records)):
            if i + 1 == record_number:
                #print(records[i])
                records[i] = new_record
        #print(*records)
    with open(filename, "w", encoding = "utf-8") as f:
        for record in records:
            f.write("".join(record))
               
# change_data()