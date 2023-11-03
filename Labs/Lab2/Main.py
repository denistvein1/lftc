from SymbolTable import SymbolTable

"""
    a: int
    b: int
    c: int
    a = 1
    b = 2
    c = 3
"""

st = SymbolTable(3)
print(st.getPosition("a"))
print(st.getPosition("b"))
print(st.getPosition("a"))
print(st.getPosition("c"))
print(st.getPosition("1"))
print(st.getPosition("2"))
print(st.getPosition("3"))
print()
print(st)
