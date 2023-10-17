#quesion 1
1) color(carrots,orange)
#answ in english
carrots color is orange
#answer in python
KB.tell(aima.utils.expr("color(carrot,orange)"))


2) likes(person,carrots):-vegetables
#answ in english
person likes carrots if person is vegetarian
#answ in python
KB.tell(aima.utils.expr("likes(person,carrot)==>vegetarian(person)"))


3) pass(student):- study_hard(student)
#answ in english
student pass if student study hard
#answ in python
KB.tell(aima.utils.expr("pass(student)==>study_hard(student)"))


4) ?-pass(who)
#answ in english
who will pass?
#answ in python
answer1=KB.ask(aima.utils.expr(pass(x)'))



5) ?-teacher(professor,course)
#answer in english
which course professor teaches?
#answer in python
answer2 = KB.ask(aima.utils.expr(''teaches(professer, cousre'))
                                           
6) enemies (x,y):- hates(x,y),fights(x,y)
#answer in english
if x&y are enemies then x hates y and x fights y:
#answer in python
KB.tell(aima.utils.expr("hates(x,y) & fights(x,y)==>enimes(x,y)"))
##################################################

#question 2

1) maria reads logic programming book by author peter lucas
#answer in fol
reads(maria,programmingbook):-author(peter_luces)
#answer in python
 KB.tell(aima.utils.expr("read(maria,logicprogramming) & written(ogicprogramming,peterlucas)")
         

2)anyone likes shopping if she is a girl 
 #answer in fol
 likes(anyone,shopping):-is_girl(anyone)
 #answer in python
 KB.tell(aima.utils.expr("isgirl(x)==>likes(x,shopping)"))
 
 
 3) who likes shopping?
    #answer in fol
    ?-likes(shopping)
    #answer in python
    
    
4) kirke hates any city if it is big and crowdy
 #answer in fol
 hates(kirke):-city(crowdy,big)
 #asnwer in python
 KB.tell(aima.utils.expr("city(crowdy,big)==>hates(kirke)"))
                         
                         
#######################################################################################
#question 3
1) hates(x,y),hates(y,x):-enemies(x,y)
#answer:
    left hand side isn't single
    corr: enemies(x,y):-hates(x,y),hates(y,x)

2) p(x):-(q)(x):-r(x))
    #answer:
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                       
 

