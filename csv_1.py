
'''
Возьмите словарь с ответами из функции get_answer
Запишите его содержимое в формате csv в формате: "ключ"; "значение". Каждая пара ключ-значение должна располагаться на отдельной строке

'''

import csv

answer=[

    {'ключ':'привет','значение':"и тебе привет"},

    {'ключ':'как дела?','значение':"лучше всех"},

    {'ключ':'пока','значение':"увидимся"}

]

 

 

with open('export.csv', 'w', encoding='utf-8', newline='') as f:

    fields = ['ключ', 'значение']

    writer = csv.DictWriter(f, fields, delimiter=';')

    writer.writeheader()

    for user in answer:

        writer.writerow(user)