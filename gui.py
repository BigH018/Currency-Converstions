from dearpygui.dearpygui import *
from conversion import fetch_currency_data, convert_currency
from datetime import datetime

def create_gui():
    """Create the GUI for the currency converter."""
    # Fetch initial currency data
    initial_data, currencies, timestamp = fetch_currency_data()
    if not initial_data:
        print("Failed to fetch currency data. Please check your internet connection.")
        return

    exchange_data = {"data": initial_data}  # Store the exchange data to update dynamically

    def on_base_currency_change(sender, app_data):
        """Callback when the base currency is changed."""
        base_currency = get_value("Base Currency")
        updated_data, _, updated_timestamp = fetch_currency_data(base_currency)
        if updated_data:
            exchange_data["data"] = updated_data  # Update the stored exchange data
            last_updated = datetime.utcfromtimestamp(updated_timestamp).strftime('%Y-%m-%d %H:%M:%S') if updated_timestamp else "N/A"
            set_value("Last Updated", f"Last Updated: {last_updated} UTC")
        else:
            set_value("Result", "Failed to update exchange rates.")

    def on_convert(sender, app_data):
        """Callback function for conversion button."""
        base_currency = get_value("Base Currency")
        target_currency = get_value("Target Currency")
        amount = get_value("Amount")
        
        if not amount or not base_currency or not target_currency:
            set_value("Result", "Please fill in all fields.")
            return

        result = convert_currency(exchange_data["data"], base_currency, target_currency, amount)
        set_value("Result", result)

    # Convert the initial timestamp to a readable format
    last_updated = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else "N/A"

    create_context()
    with window(label="Currency Converter", width=400, height=350):
        add_text("Currency Converter", color=[255, 255, 255])
        add_text(f"Last Updated: {last_updated} UTC", tag="Last Updated")
        add_separator()
        
        add_text("Select Base Currency:")
        add_combo(label="Base Currency", tag="Base Currency", items=currencies, default_value="USD", callback=on_base_currency_change)
        
        add_text("Select Target Currency:")
        add_combo(label="Target Currency", tag="Target Currency", items=currencies, default_value="EUR")
        
        add_text("Enter Amount:")
        add_input_text(label="Amount", tag="Amount", hint="Enter amount to convert")
        
        add_button(label="Convert", tag="Convert Button", callback=on_convert)
        add_separator()
        add_text("Result:")
        add_text(default_value="Conversion result will appear here.", tag="Result")

    create_viewport(title='Currency Converter', width=400, height=350)
    setup_dearpygui()
    show_viewport()
    start_dearpygui()
    destroy_context()
