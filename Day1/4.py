# found out switch case support was introduced in Python 3.10
# match operation handles the matching of switch cases
def calculator(operation:str, n1: float, n2: float) -> float:
  match operation:
     case "addition":
        return n1+n2
     case "subtraction":
        return n1-n2
     case "division":
        return n1/n2
     case "multiplication":
        return n1*n2

print(calculator('addition', 2,3)) #5
print(calculator('subtraction', 3,2)) #1
print(calculator('division', 6,3)) #2
print(calculator('multiplication', 2,3)) #6
