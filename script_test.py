from aimacode.logic import PropKB
from aimacode.planning import Action
from aimacode.search import (
    Node, Problem,
)
from aimacode.utils import expr
from lp_utils import (
    FluentState, encode_state, decode_state,
)
from my_planning_graph import PlanningGraph
from my_air_cargo_problems import AirCargoProblem

cargos = ['C1', 'C2']
planes = ['P1', 'P2']
airports = ['JFK', 'SFO']
pos = [expr('At(C1, SFO)'), expr('At(C2, JFK)'), expr('At(P1, SFO)'), expr('At(P2, JFK)'),]
neg = [expr('At(C2, SFO)'),expr('In(C2, P1)'),expr('In(C2, P2)'),expr('At(C1, JFK)'),expr('In(C1, P1)'),expr('In(C1, P2)'),expr('At(P1, JFK)'),expr('At(P2, SFO)'),]
init = FluentState(pos, neg)
goal = [expr('At(C1, JFK)'),expr('At(C2, SFO)'),]
aircargo = AirCargoProblem(cargos, planes, airports, init, goal)

action = aircargo.actions_list.pop()

state_map = [s for s, h in zip(aircargo.state_map, aircargo.initial_state_TF) if h == 'T']
