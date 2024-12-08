import requests

def fetch_currency_data(base_currency="USD"):
    """Fetch exchange rates and list of currencies."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        currencies = list(data['rates'].keys())
        timestamp = data.get("time_last_updated")  # Timestamp for rates
        return data, currencies, timestamp
    except Exception as e:
        print(f"Error fetching currency data: {e}")
        return None, [], None


def convert_currency(exchange_data, base_currency, target_currency, amount):
    """Perform currency conversion based on exchange data."""
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount. Please enter a number."

    rate = exchange_data['rates'].get(target_currency)
    if rate is None:
        return f"Conversion rate not found for {target_currency}."
    
    converted_amount = amount * rate
    return f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}"
