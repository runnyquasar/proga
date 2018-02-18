import random

def open_f(filename):
    with open(filename, encoding = 'utf-8') as f:
        pairs = f.readlines()
        
    hints = {}
    
    for pair in pairs:
        pair = pair.strip('\ufeff \n')
        hint, word = pair.split(';')
        hints[word] = hint
        
    return hints

def both_f(pairsdict):
    question = random.choice(list(pairsdict.keys()))
    hint = pairsdict[question]    
    return question, hint

def check_f(user_ans, right):
    if user_ans == right:
        print('Молодец! С тобой пластмассовый мир никогда не победит!')
    else:
        print('Эх, почитай еще журнал "Корея".' +' \n'+ 'Тогда поймешь, что правильный ответ - ', right)    

hints = open_f('oborona.csv')
question, hint = both_f(hints)

print('Давай посмотрим, насколько все идет по плану')
print(hint, '.' * len(hint), sep = '')
answer = input('Ваш ответ: ')

check_f(answer, question)
