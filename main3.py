from pprint import pprint
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# pprint(contacts_list)

def group_fio():
    persons_list = []
    for contact_detail in contacts_list:
        person_list = []
        separator = ' '
        fio_merged = separator.join([contact_detail[0], contact_detail[1], contact_detail[2]])
        person_list.append(fio_merged.strip())
        person_list.append(contact_detail[3].strip())
        person_list.append(contact_detail[4].strip())
        person_list.append(contact_detail[5].strip())
        person_list.append(contact_detail[6].strip())
        persons_list.append(person_list)
    return persons_list


def separate_fio():
    persons_list_name_formatted = []
    for contact_detail in group_fio():
        info_sepparated = contact_detail[0].split()
        info_sepparated.append(contact_detail[1])
        info_sepparated.append(contact_detail[2])
        info_sepparated.append(contact_detail[3])
        info_sepparated.append(contact_detail[4])
        persons_list_name_formatted.append(info_sepparated)
    return persons_list_name_formatted


# print(separate_fio())

def format_phonebook():
    persons_list_all_formatted = []
    for info in separate_fio():
        person_info_list = []
        pattern_phone = r"(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?[а-я]*\.?\s?(\d{4})?\)?"
        # if "доб" in info[-2]:
        #     phone_formatted = re.sub(pattern_phone, r"+7(\2)\3-\4-\5 доб.\6", info[-2])
        phone_formatted = re.sub(pattern_phone, r"+7(\2)\3-\4-\5", info[-2])
        person_info_list.append(info[0])
        person_info_list.append(info[1])
        person_info_list.append(info[2])
        person_info_list.append(info[3])
        person_info_list.append(info[4])
        person_info_list.append(phone_formatted)
        person_info_list.append(info[-1])
        persons_list_all_formatted.append(person_info_list)
    return persons_list_all_formatted


def join_duplicates():
    perfect_list = []
    for info_list in format_phonebook():
        counter = 0
        for info_list2 in format_phonebook():
            if info_list[0] == info_list2[0] and info_list[1] == info_list2[1]:
                counter += 1
                if counter == 1:
                    person_list = []
                    for n in range(7):
                        if info_list[n] != '':
                            person_list.append(info_list[n])
                        else:
                            person_list.append(info_list2[n])
        perfect_list.append(person_list)

    return perfect_list

join_duplicates()


with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(join_duplicates())
