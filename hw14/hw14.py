def custom_split(text, borders):
    parts = [] 
    onepart = ''
    for token in text:
        if token not in borders:
            onepart += token 
        else:
            parts.append(onepart)
            onepart = ''
    return parts

fname = input("Введите имя файла: " +"\n")
with open(fname, "r", encoding='utf-8') as f:
    text = f.read()
    
 
def punctuation (text):
    text = custom_split(text, '.!?')
    return text
 
def dictionnary(text):
    dic = {sentence: sentence.split() for sentence in text}
    for key, value in dic.items():
        dic[key] = {word: len(word) for word in key.split()}
    return dic
 
print (dictionnary(punctuation(text)))
