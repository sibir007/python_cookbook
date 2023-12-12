from chapter_0 import prn_tem
prn_tem('10.1. Making a Hierarchical Package of Modules')
"""
graphics/
    __init__.py
    primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py
"""
import src.python_cookbook.mymodule as mm
clsB = mm.B()
clsB.bar()
clsB.spam()
clsB2 = mm.b.B()
clsB2.spam()
clsB2.bar()

