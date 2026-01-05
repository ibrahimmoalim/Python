# match-case statement (switch): An alternative to using many 'elif' statements
#                 Execute some code if a value matches a 'case'
#                 Benefits: cleaner and syntax is more readable

def maalmaha_isbuuca(maalin):
  # match maalin with a number or a string
  match maalin:
    # if maalin == 1: => case 1:
    case 1:
      return "Waa Sabti"
    # elif maalin == 2: => case 2:
    case 2:
      return "Waa Axad"
    case 3:
      return "Waa Isniin"
    case 4:
      return "Waa Talaado"
    case 5:
      return "Waa Arbaco"
    case 6:
      return "Waa Khamiis"
    case 7:
      return "Waa Jimce"
    # case _: => else:
    case _:
      return f"{maalin} maalin isbuuc ma'ahan"


print(maalmaha_isbuuca(1)) # Waa Sabti
print(maalmaha_isbuuca(3)) # Waa Isniin
print(maalmaha_isbuuca('ramadaan')) # ramadaan maalin isbuuc ma'ahan


def is_weekend(day):
  match day:
    # | = or
    case "Jimce" | "Khamiis":
      return True
    case "Sabti" | "Axad" | "Isniin" | "Talaado" | "Arbaco" | "Khamiis":
      return False
    case _:
      return False
    
print(is_weekend("Jimce")) # True
print(is_weekend("Khamiis")) # True
print(is_weekend("Isniin")) # False
print(is_weekend("yaanyo")) # False