game_library = {'Donkey Kong': {'quantity': 3, 'cost':3},
                'Super Mario Bros': {'quantity': 5, 'cost':2},
                'Tetris': {'quantity': 2, 'cost':1}}
user_accounts = {}
                 
inventory = []

def display_availale_games():
        while True:
            for i, (game, details) in enumerate(game_library.items(), start=1):
                print(f"{i}. {game} - Quantity - {details['quantity']} , Cost - {details['cost']}")

            choice = input("Press enter to continue...")
            if not choice:
                main()

def user_sign_up():
    while True:
            try:
                username = input("Enter username: ")
                if username in user_accounts.keys():
                    print("Username already exists.")
                    user_sign_up()
                else:
                    password = input("Enter password: ")
                    if len(password) >= 8:
                        user_accounts[username] = {
                            'username': username,
                            'password': password,
                            'balance': 0,
                            'points': 0
                        }
                        main()
                    else:
                        print("Password must be 8 characters long.")
                        user_log_in()
            except ValueError as e:
                print(f"Error occured: {e}")

def user_log_in():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if not username:
                main()
            elif not password:
                main()
            elif username in user_accounts.keys() and user_accounts[username]['password'] == password:
                print("Log in successfully!")
                logged_in_menu(username)
            else:
                print("Incorrect username or password. Try again.")
                user_log_in()
        except Exception as e:
            print(f"Error occured: {e}")

    
def logged_in_menu(username):
    while True:
        print(f"\nWelcome {username} ")
        print("Rental Game System")
        print("1. Rent a Game")
        print("2. Return a Game")
        print("3. Top up Account")
        print("4. Display inventory")
        print("5. Check points")
        print("6. Log out")

        choice = input("Enter your choice: ")
        if choice == "1":
            rent_game(username)
        if choice == "2":
            return_game(username)
        if choice == "3":
            top_up_account(username)
        if choice == "4":
            display_user_inventory(username)
        if choice == "5":
            checkpoints(username)
        if choice == "6":
            main()
  
def rent_game(username):
    print(f"\nYour current balance: {user_accounts[username]['balance']}")
    print("Avalable Games for rent:")
    enumerated_game_library = enumerate(game_library.items(), start=1)
    for i, (game, details) in enumerated_game_library:
        print(f'{i}. {game} - Quantity: {details["quantity"]}, Cost: {details["cost"]}')
    choice = (input("Enter the corresponding number of the game you want to rent: "))

    game_library_length = len(game_library)

    if not choice:
        logged_in_menu(username)
    
    choice = int(choice)
    if choice in range(1, game_library_length + 1):
        game_name_list = list(game_library.keys())
        game_name = game_name_list[choice - 1]
        print(f"The Name of game: {game_name}" )
        quantity = int(input("Enter the quantity you want to rent: "))
        if not quantity:
            rent_game(username)
        elif game_library[game_name]['quantity'] >= quantity:
            total_cost = game_library[game_name]['cost'] * quantity
            if user_accounts[username]['balance'] >= total_cost:
                user_accounts[username]['balance'] -= total_cost
                inventory.append({"game_name": game_name, "quantity": quantity, "user_name": username})
                game_library[game_name]['quantity'] -= quantity
                print(f"Total cost: {total_cost}")
            else: 
                print("Insufficient balanace.")
                rent_game(username)
        else:
            print("Invalid input. Insufficient quantity.")
            rent_game(username)
    else:
        print("Invalid input plase try again.")
        rent_game(username)




def return_game(username):
    game = input('Enter the game you want to return: ')
    item_quantity = int(input('Enter the quantity you want to return: '))
    game_library[game]['quantity'] = item_quantity + game_library[game]['quantity']
    print('You have successfully return a game!')
    choice = input('Do you want to return another game (y/n)? ')

    if choice == 'y':
        return_game(username)
    else:
        logged_in_menu(username)

def top_up_account(username):
    try:
        top_up_amount = float(input("Enter the amount you want to top up: $"))
        if top_up_amount > 0:
            user_accounts[username]['balance'] += top_up_amount
            print(f"Successfully topped up: ${top_up_amount}")
        else:
            print("Invalid amount please enter a valid amount.")
    except Exception as e:
        print(f"Error occured: {e}")

def display_user_inventory(username):
     while True:
            for i, (game, details) in enumerate(game_library.items(), start=1):
                print(f"{i}. {game} - Quantity - {details['quantity']} , Cost - {details['cost']}")

            choice = input("Press enter to continue...")
            if not choice:
                logged_in_menu(username)

def checkpoints(username):
    while True:
        balance = user_accounts[username]['balance']
        points = user_accounts[username]['points']
        print(f'Available Balance:{balance}, Points:{points}')

        choice = input("Press enter to continue...")
        if not choice:
            logged_in_menu(username)



def main():
    while True:
        try:
            print('\n1. Display Available game')
            print('2. Register User')
            print('3. Log in')
            print('4. Exit')
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_availale_games()
            if choice == 2:
                user_sign_up()
            if choice == 3:
                user_log_in()
        except ValueError:
            print('Please Enter a Valid number!')

main()
            