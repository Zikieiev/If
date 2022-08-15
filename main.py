Cycle = 1

while Cycle == 1:
      name = input('Введите свое имя: ')
      if len(name) < 1:
             print('Строка имя должна содержать хоть один символ')
      elif len(name) > 1:
            age = input('Введите свой возраст: ')
            if int(age) == 0:
                 print('Ошибка! Повторите ввод')
            elif int(age) <= 0:
                 print('Ошибка! Повторите ввод')
            elif int(age) > 0 and int(age) < 10:
                 print('Привет, шкет ' + name)
            elif int(age) >= 10 and int(age) < 100:
                 print('Что желаете ' + name + '?')
            elif int(age) >= 100:
                 print(name + ', вы лжете - в наше время столько не живут...')
      ExitQuestion = input('Желаете выйти? (Д/Y): ')
      if ExitQuestion.lower() == 'y' or ExitQuestion.lower() == 'д': break