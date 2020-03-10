
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/COMMENT ELSE EQ FOR FUNC GEQ ID IF IN LEQ NUMBER WHILEexpression : expression '+' expression\n                      | expression '-' expression\n                      | expression '*' expression\n                      | expression '/' expression\n                      | '(' expression ')'\n                      | NUMBER"
    
_lr_action_items = {'(':([0,2,4,5,6,7,],[2,2,2,2,2,2,]),'NUMBER':([0,2,4,5,6,7,],[3,3,3,3,3,3,]),'$end':([1,3,9,10,11,12,13,],[0,-6,-1,-2,-3,-4,-5,]),'+':([1,3,8,9,10,11,12,13,],[4,-6,4,-1,-2,-3,-4,-5,]),'-':([1,3,8,9,10,11,12,13,],[5,-6,5,-1,-2,-3,-4,-5,]),'*':([1,3,8,9,10,11,12,13,],[6,-6,6,6,6,-3,-4,-5,]),'/':([1,3,8,9,10,11,12,13,],[7,-6,7,7,7,-3,-4,-5,]),')':([3,8,9,10,11,12,13,],[-6,13,-1,-2,-3,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,5,6,7,],[1,8,9,10,11,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression + expression','expression',3,'p_expression','parser.py',37),
  ('expression -> expression - expression','expression',3,'p_expression','parser.py',38),
  ('expression -> expression * expression','expression',3,'p_expression','parser.py',39),
  ('expression -> expression / expression','expression',3,'p_expression','parser.py',40),
  ('expression -> ( expression )','expression',3,'p_expression','parser.py',41),
  ('expression -> NUMBER','expression',1,'p_expression','parser.py',42),
]