from .RuleTemplate import RuleTemplate
from .AtomicRule import AtomicRule
from .Velocity_Regulation_Problem import Velocity_Regulation_Problem
from .Tiger_Problem import Tiger_Problem
from .Rocksample_Problem import Rocksample_Problem
from .State import State

import sys
import z3
import pdb


def test(): 
    # parse input files
    
    #tiger_left = State("tiger left")
    #tiger_right = State("tiger right")
    
    #problem = Tiger_Problem(xes_log='./src/xpomcp/tracce/tiger_correct.xes', num_traces_to_analyze= 100, states = [tiger_left,tiger_right])
    # rule1 = AtomicRule(actions = ["open left"], problem = problem)
    # x1 = rule1.declareVariable('x1')
    # rule1.addConstraint(x1 >= tiger_right.get_probability())
    # #rule.solve()
    #
    # rule2 = AtomicRule(actions = ["open right"], problem = problem)
    # x2 = rule2.declareVariable('x2')
    # rule2.addConstraint(x2 >= tiger_left.get_probability())
    # #rule.solve()
    
    #rule3 = AtomicRule(actions = ["listen"], problem = problem)
    #x3 = rule3.declareVariable('x3')
    #x4 = rule3.declareVariable('x4')
    #rule3.addConstraint(x3 <= tiger_left.get_probability(), x4 <= tiger_right.get_probability())
    #rule3.solve()
    # final_rule = RuleTemplate([rule1,rule2,rule3], problem = problem,threshold = 0.10)
    # final_rule.add_constraint(x3 == x4, x1 == x2,x1 >= 0.90)
    # final_rule.solve()
    
    
    # easy = State(0)
    # intermediate = State(1)
    # difficult = State(2)
    
    # problem = Velocity_Regulation_Problem(xes_log=xes_log[0],states = [intermediate,difficult,easy])

    # rule = AtomicRule(actions = [2], problem = problem)
    
    # x1 = rule.declareVariable('x1')
    # x2 = rule.declareVariable('x2')
    
    # rule.addConstraint(x1 >= easy.get_probability())
    # rule.addConstraint(x2 <= difficult.get_probability())
    # rule.addHardConstraint(x1 >= 0.90)
    
    # rule.solve()
    
    coord_x = State('coord x')
    coord_y = State('coord y')
    rock_0 = State('rock 0')
    rock_1 = State('rock 1')
    rock_2 = State('rock 2')
    rock_3 = State('rock 3')
    rock_4 = State('rock 4')
    rock_5 = State('rock 5')
    rock_6 = State('rock 6')
    rock_7 = State('rock 7')
    rock_8 = State('rock 8')
    rock_9 = State('rock 9')
    rock_10 = State('rock 10')
    rock_rel = State('rock rel')

    problem = Rocksample_Problem(xes_log='./tracce/rocksample_small.xes',num_traces_to_analyze = None,states=[coord_x,coord_y,rock_0,rock_1,rock_2,rock_3,rock_4,rock_5,rock_6,rock_7,rock_8,rock_9,rock_10,rock_rel])

    #rulesmpl = AtomicRule(actions = ['sample'], problem = problem)
    #rules = AtomicRule(actions = ['south'], problem = problem)
    #rulee = AtomicRule(actions = ['east'], problem = problem)
    #rulew = AtomicRule(actions = ['west'], problem = problem)
    #rulen = AtomicRule(actions = ['north'], problem = problem)
    #rule0 = AtomicRule(actions = ['check 0'], problem = problem)
    #rule1 = AtomicRule(actions = ['check 1'], problem = problem)
    #rule2 = AtomicRule(actions = ['check 2'], problem = problem)
    #rule3 = AtomicRule(actions = ['check 3'], problem = problem)
    #rule4 = AtomicRule(actions = ['check 4'], problem = problem)
    #rule5 = AtomicRule(actions = ['check 5'], problem = problem)
    #rule6 = AtomicRule(actions = ['check 6'], problem = problem)
    #rule7 = AtomicRule(actions = ['check 7'], problem = problem)
    #rule8 = AtomicRule(actions = ['check 8'], problem = problem)
    #rule9 = AtomicRule(actions = ['check 9'], problem = problem)
    # rule10 = AtomicRule(actions = ['check 10'], problem = problem)
    rulerel = AtomicRule(actions = ['sample'], problem = problem)

    x1 = rulerel.declareVariable('x1')
    rulerel.addConstraint(x1 <= rock_0.get_probability())
    rulerel.solve()
test()
