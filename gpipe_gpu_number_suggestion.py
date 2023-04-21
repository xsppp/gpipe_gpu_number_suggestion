# -*- coding: utf-8 -*-


#This code is a simple applying of the theoretical model of the paper.
from sympy import symbols, solve
single_or_not = input("Please input yes/no that the model can be trained with a single GPU ;")
if single_or_not == "yes":
  #According to the equation 14, when a model can be trained with a single GPU there is no need to apply Gpipe.
  print("No need to aplly Gpipe")
else :
  #In the ideal scenario, the equation 15-18 provide a guide for the chosen of the number of GPU. It will be more complicated to find the optimization solution to the theoretical model.
  #In order to propose an optimization strategy, the weight parameters in the model need to be considered. However, this code is just for a better understanding of the model. 
  #Hence, in this code, the weight parameters are not considered. 
  N = int(input("Please input N :"))
  F = float(input("Please input F :"))
  f = float(input("Please input F^ :"))
  function1 = 1 - ((5*N*F-3*F)/(2*N*N*F)) 
  if function1 < 0 :
    print('No need Gpipe')
  else :
    n = symbols('n')
    #Only when the gain ratio S is less than one, applying more GPU can achieve faster training speed.
    functionf2 = 1 - (((5*n-3)*f)/((5*N-3)*F))
    function3 = n - (N+1)
    s = solve([function2 > 0, function3 >= 0])
    if s==False :
      print("No need to apply more GPUs")
    else :
      print("The suggestion of the GPU number is in %s:"%s)