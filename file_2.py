
'''

Прочитайте его и подсчитайте количество слов в тексте

'''




with open('referat.txt', 'r' , encoding='utf-8' ) as f:

    count_word=0

    for line in f:

        line = line.replace('\n', '')

        print(line)

        list1=line.split() #превращаем строку в список

        count_word+=len(list1)

 

 

print(count_word)