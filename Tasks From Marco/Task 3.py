"""
Task 3
"""

"""
First I need to create stringman.py with the necessary classes og methods
"""

from stringman import *

newStringObj = sentence("This;is;my;sentence;that;I;want;to;test", ";")

newStringObj.strLength()
strCutted = newStringObj.cutString()

newStringObj.showWordAt(strCutted, 3)
newStringObj.showIndexAt(strCutted, "sentence")