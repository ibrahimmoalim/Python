# A simple banking program


# print('*****************************')
# print('       Banking Program       ')
# print('*****************************')
# print('1. Show Balance')
# print('2. Deposit')
# print('3. Withdraw')
# print('4. Exit')
# print('*****************************')

# balance = 0

# while True:
#   option = input('Enter option (1-4): ')

#   try:
#     option = int(option)
#   except ValueError:
#     print(f'{option} is invalid!')
#     continue
  
#   match option:
#     case 1:
#       print(f'Your balance is {balance}')

#     case 2:
#       while True:
#         money = input('Enter amount to be deposited: ')

#         try:
#           money = float(money)
#         except ValueError:
#           print(f'Invalid input, try again!')
#           continue

#         balance += money
#         print(f'You have deposited ${money}')
#         print(f'Your balance is ${balance}')
#         break

#     case 3:
#       while True:
#         value = input('Enter amount to be withdrawn: ')

#         try:
#           value = float(value)
#         except ValueError:
#           print(f'Invalid input, try again!')
#           continue

#         balance -= value
#         print(f'You have withdrawn ${value}')
#         print(f'Your balance is ${balance}')
#         break

#     case 4:
#       print('Bye!')
#       exit()

#     case _:
#       print(f'{option} is invalid!')

def show_balance(balance):
  print('--------------------')
  print(f'Your balance is ${balance:.2f}')
  print('--------------------')

def deposit():
  try:
    money = float(input('Enter amount to be deposited: '))
    if money <= 0:
      print('******')
      print('Invalid amount')
      return 0
    else:
      print('--------------------')
      print(f'You deposited ${money}')
      print('--------------------')
      return money
  except ValueError:
    print('******')
    print('Invalid input')
    return 0
  

def withdraw(balance):
  try:
    money = float(input('Enter amount to be withdrawn: '))
    if money > balance:
      print('******')
      print('Insufficient funds')
      return 0
    elif money <= 0:
      print('******')
      print('Amount must be greater than 0')
      return 0
    else:
      print('--------------------')
      print(f'You have withdrawn ${money}')
      print('--------------------')
      return money 
  except ValueError:
    print('******')
    print('Invalid input')
    return 0



def main():

  try:
    balance = 0
    is_running = True

    print('*****************************')
    print('       Banking Program       ')
    print('*****************************')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    print('*****************************')

    while is_running:

      option = input('Enter an option (1-4): ')

      if option == '1':
        show_balance(balance)

      elif option == '2':
          balance += deposit()
          show_balance(balance)

      elif option == '3':
        balance -= withdraw(balance)
        show_balance(balance)

      elif option == '4':
        print('Thank you!')
        is_running = False

      else:
        print('******')
        print(f'{option} is invalid!')
        continue
  except KeyboardInterrupt:
    print("\nCtrl+C detected. Exiting gracefully.")


if __name__ == "__main__":
  main()