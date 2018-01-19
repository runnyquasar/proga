
import random


#откроем файлы



with open("/Users/andreakimov/Desktop/hokku/NOUN2F.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
noun2f=part.split(', ')

with open("/Users/andreakimov/Desktop/hokku/NOUN2M.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
noun2m=part.split(', ')

with open("/Users/andreakimov/Desktop/hokku/NOUN3.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
noun3=part.split(', ')

with open("/Users/andreakimov/Desktop/hokku/NO.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
no=part.split()

with open("/Users/andreakimov/Desktop/hokku/PAS.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
pas=part.split()

with open("/Users/andreakimov/Desktop/hokku/EXC.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
exc=part.split()

with open("/Users/andreakimov/Desktop/hokku/PREP.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
prep=part.split()

with open("/Users/andreakimov/Desktop/hokku/VERB.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
verb=part.split(', ')

with open("/Users/andreakimov/Desktop/hokku/VERB2.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
verb2=part.split()

with open("/Users/andreakimov/Desktop/hokku/VERB3.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
verb3=part.split()

with open("/Users/andreakimov/Desktop/hokku/ADJF.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
adjf=part.split()

with open("/Users/andreakimov/Desktop/hokku/ADJM.txt" ,encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
adjm=part.split()

with open("/Users/andreakimov/Desktop/hokku/PUNC.txt", encoding="utf-8") as f:
    part=f.read()
part=part.replace("\ufeff","")
punc=part.split()




#сделаем функции

def noun2f_func():
    
    return random.choice(noun2f)

def noun2m_func():
 
    return random.choice(noun2m)
def noun3_func():
 
    return random.choice(noun3)
def no_func():
 
    return random.choice(no)
def pas_func():
 
    return random.choice(pas)
def exc_func():
 
    return random.choice(exc)
def verb2_func():
 
    return random.choice(verb2)
def verb3_func():
 
    return random.choice(verb3)

def punc_func():
    
    return random.choice(punc)

#это были функции отдельных слов
#теперь будем соединять словечки

def noun2f_verb3():
    return noun2f_func() +' ' + verb3_func() + punc_func()

def noun2m_verb3():
    return noun2m_func() + ' ' +verb3_func() + punc_func()

def noun3_verb2():
    return noun3_func() + ' ' + verb2_func() + punc_func()

def noun2f_verb():
    return noun2f_func() + ' ' + verb_func() + punc_func()

def noun2m_verb():
    return noun2m_func() + ' ' + verb_func() + punc_func()

def phrase_exc():
    return exc_func() + ' ' + noun2f_func() +' ' + verb3_func() + punc_func()

def phrase_exc2():
    return exc_func() + ' ' + noun2m_func() +' ' + verb3_func() + punc_func()

def phrase_no():
    return noun2f_func() + ' ' + no_func()+ ' '+ verb3_func()+ ' ' + pas_func() + punc_func()

def phrase_no2():
    return noun2m_func()+' '+ no_func()+ ' ' + verb3_func() + ' ' + pas_func() + punc_func()
def phrase_no3():
    return noun3_func() + ' ' + no_func() + ' ' + verb2_func() + ' ' + pas_func() + punc_func()

def verse1():

    verse1n=[noun2f_verb3(), noun2m_verb3() , noun3_verb2()]
    return random.choice(verse1n)

def verse2():
    verse2n=[phrase_exc() ,phrase_exc2() , phrase_no() , phrase_no2 , phrase_no3]
    return random.choice(verse2n)

def verse3():

    verse3n=[noun2f_verb3(), noun2m_verb3(), noun3_verb2()]
    return random.choice(verse3n)

def make_verse():
    print(verse1())
    print(verse2())
    print(verse3())
 
    

#основной код 

make_verse()

    
    
    















