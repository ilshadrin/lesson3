
'''
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/17 12:10:03.234567" в объект datetime
'''


from datetime import datetime, timedelta

dt_now = datetime.now()
print('today ',dt_now)


delta = timedelta(days=1)

print('yesterday ',dt_now-delta)

delta2 = timedelta(days=30)

print('month ago ',dt_now-delta2)


date_string='01/01/17 12:10:03.234567'

a=datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')


print(a)