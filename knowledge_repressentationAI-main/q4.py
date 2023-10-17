# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:09:07 2021

@author: Administrator
"""
import aima.utils
import aima.logic
def main():
    clauses=[]
    clauses.append(aima.utils.expr("healthy(x)& wealthy(x) ==> traveller(x)" ))
    clauses.append(aima.utils.expr("man(john)" ))
    clauses.append(aima.utils.expr("women(jia)" ))
    clauses.append(aima.utils.expr("healthy(john)" ))
    clauses.append(aima.utils.expr("healthy(jia)" ))
    clauses.append(aima.utils.expr("wealthy(john)" ))
    clauses.append(aima.utils.expr("traveller(x)==>cantravel(x)" ))
    KB=aima.logic.FolKB(clauses)
    cantravel=aima.logic.fol_fc_ask(KB, aima.utils.expr("cantravel(x)"))
    who=aima.logic.fol_fc_ask(KB, aima.utils.expr("healthy(x)& wealthy(x)"))
    print(" who can travel : " ,list(cantravel))
    print(" who is healthy and wealthy : " ,list(who))
 
    
if __name__ == "__main__": main()
    
    