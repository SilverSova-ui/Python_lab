s = input()#ввод данных
if s.count('f') == 1: #если 1 f
 print (s.find('f'))# то индекс
elif s.count('f') >= 2: #если 2 f и более
 print (s.find('f'), s.rfind('f'))# то индекс 1 и последнего появления