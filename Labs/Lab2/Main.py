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
print(st.put("a"))
print(st.put("b"))
print(st.put("a"))
print(st.put("c"))
print(st.put("1"))
print(st.put("2"))
print(st.put("3"))
print()
print(st)
