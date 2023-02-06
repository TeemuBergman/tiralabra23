from algorithms.shunting_yard import shunting_yard
from algorithms.postfix_evaluator import postfix_evaluator


EXP = '4+188/(9-3)'
result_sy = shunting_yard(EXP)
result_pe = postfix_evaluator(result_sy)
print(result_pe)
