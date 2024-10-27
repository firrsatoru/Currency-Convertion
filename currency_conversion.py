import requests

def currency_conversion():
    print("Currency Conversion")
    base_currency = input("Enter The Base Currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter The Currency You Want To Convert To (e.g., IDR, JPY): ").upper()
    amount = float(input("Enter The Amount You Want To Convert: "))

    # Use API To Convert Currency
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print(f"Error: {data['error']}")
            return

        # Process
        exchange_rate = data["rates"].get(target_currency)

        if exchange_rate:
            converted_amount = amount * exchange_rate
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print(f"Currency {target_currency} Not Found!")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Running Py
if __name__ == "__main__":
    currency_conversion()
    
