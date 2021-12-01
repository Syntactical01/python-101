"""
Code to show how didn't objects are teated as Truthy and Falsey values
by Python.
"""
print(f"""
Boolean Casting...

Integers:
     0 : {bool(0)}
    -1 : {bool(-1)}
     2 : {bool(2)}

Float:
    0.0 : {bool(0.0)}
   -1.2 : {bool(-1.2)}
    1.3 : {bool(1.3)}

String:
    "John Smith" : {bool("John Smith")}
    ""           : {bool("")}
    "123f"       : {bool("123f")}

Containers:
    [ ] : {bool([])}
    [1, 2] : {bool([1, 2])}
    {{ }} : {bool({})}
    {{1: 2}} : {bool({1: 2})}
    ...
""")

