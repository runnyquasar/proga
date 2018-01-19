Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
la vague rigolait…
bravo! la vague rigolait…
la vague finissait!
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
la chasse rigolait.
Dame! la pille finissait.
l’image fumera.
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
la chasse finissait.
Dame! la balle finissait…
la pille rigolait?
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
l’hiver finissait?
ò-la! l’automne rigolait!
la chasse finissait!
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
la chasse rigolait!
Dame! la chasse fumera?
la mur rigolait…
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
la balle rigolait?
hein? la vague fumera…
la vague rigolait!
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
l’épaule mange!
bravo! la balle rigolait?
la fille finissait.
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
l’oiseau rigolait!
Traceback (most recent call last):
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 164, in <module>
    make_verse()
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 157, in make_verse
    print(verse2())
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 147, in verse2
    verse2n=[phrase_exc() ,phrase_exc2() , phrase_no() , phrase_no2 , phrase_no3]
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 134, in phrase_no
    return noun2f_func() + ' ' + no_func()+ ' '+ verb3_func()+ ' ' + pas_func() + punc_func()
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 94, in pas_func
    return random.choice(pas)
NameError: name 'pas' is not defined
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
le pigeon passe.
Traceback (most recent call last):
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 164, in <module>
    make_verse()
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 157, in make_verse
    print(verse2())
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 147, in verse2
    verse2n=[phrase_exc() ,phrase_exc2() , phrase_no() , phrase_no2 , phrase_no3]
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 134, in phrase_no
    return noun2f_func() + ' ' + no_func()+ ' '+ verb3_func()+ ' ' + pas_func() + punc_func()
  File "/Users/andreakimov/Desktop/hokku/hokku.py", line 94, in pas_func
    return random.choice(pas)
NameError: name 'pas' is not defined
>>> 
============= RESTART: /Users/andreakimov/Desktop/hokku/hokku.py =============
le pigeon mange…
ò-la! le but finissait?
l’automne fumera?
>>> 
