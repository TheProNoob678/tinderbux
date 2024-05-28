import requests

BASE_URL = 'http://127.0.0.1:5000'
ADMIN_KEY = ''  # Good Luck

def create_wallet(owner):
    response = requests.post(f'{BASE_URL}/create_wallet', json={'owner': owner})
    return response.json()

def check_balance(owner):
    response = requests.get(f'{BASE_URL}/balance', params={'owner': owner})
    return response.json()

def request_deposit(owner, amount, admin_key):
    response = requests.post(f'{BASE_URL}/admin/deposit', json={'key': admin_key, 'owner': owner, 'amount': amount})
    return response.json()

def transfer(sender, recipient, amount):
    response = requests.post(f'{BASE_URL}/transfer', json={'sender': sender, 'recipient': recipient, 'amount': amount})
    return response.json()

def main():
    owner = input("Enter your wallet name: ")
    admin = False

    # Prompt for admin key (optional)
    admin_key = input("access code (0 for standard access): ")
    if admin_key == ADMIN_KEY:
        admin = True
        print("Admin access granted.")
    else:
        print("Standard user access.\n\n")

    # Create wallet only if it doesn't exist
    create_response = create_wallet(owner)
    if create_response.get("message") == "Wallet already exists":
        print(f"Welcome back, {owner}!")
    else:
        print(create_response.get("message"))

    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Transfer")
        print("3. Exit")
        if admin:
            print("4. Request Deposit")
        choice = input("Choose an option: ")

        if choice == '1':
            balance_response = check_balance(owner)
            print(f"Balance: {balance_response.get('balance')}")

        elif choice == '2' and admin:
            amount = float(input("Enter amount to request: "))
            deposit_response = request_deposit(owner, amount, admin_key)
            print(deposit_response.get("message"))

        elif choice == '3':
            recipient = input("Enter recipient wallet name: ")
            amount = float(input("Enter amount to transfer: "))
            transfer_response = transfer(owner, recipient, amount)
            print(transfer_response.get("message"))

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
