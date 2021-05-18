capitals = dict()
capitals['Russia']='Moscow'
capitals['Canada']='Toronto'
capitals['Greece']='Athens'
capitals['Kazakhstan']='Astana'
capitals['Austria']='Venna'
print('What country do you live in?')
country = input()
if country in capitals:
    print('The capital of your country ', capitals[country])
else:
    print('What is the name of the capital of your country?')
    city=input()
    capitals[country] = city
