# # LEGB
# # Local - External - Global - Builtin

# def Outer():
#     # global s1
#     s1 = "Outer String"
#     def Inner():
#         # nonlocal s1
#         s1 = "Inner String"
#         print(f"Inner:: {s1}")
#     Inner()
#     print(f"Outer :: {s1}")

# s1 = "Global String"

# Outer()

# print(f"Global:: {s1}")


###########################################


def Outer():
    # global s1
    s1 = "Outer String"
    print(f"Outer :: {s1}")
    # print(f"{locals() = }")
    # print(f"{globals() = }")
    data = globals()
    print(f"{data['s1'] = }")
    data['s1'] = "Modified String"

s1 = "Global String"

Outer()

print(f"Global:: {s1}")
