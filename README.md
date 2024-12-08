# Currency Converter

A simple and interactive **Currency Converter** built with Python and **Dear PyGui**. This application allows users to convert amounts between various currencies using live exchange rates fetched from a free API.

## Features
- Select base and target currencies from dropdown menus.
- Enter the amount to convert and get instant results.
- Fetches live exchange rates from a free API.
- Displays the last updated timestamp for the exchange rates.
- Intuitive and user-friendly GUI using Dear PyGui.

---

## Screenshots
### Main Interface
![Currency Converter Screenshot](https://github.com/user-attachments/assets/32177307-3d5d-40ab-a548-65dc1cc386c2)

---

## How to Use

1. Select the **Base Currency** (the currency you are converting from).
2. Select the **Target Currency** (the currency you are converting to).
3. Enter the amount in the "Amount" field.
4. Click the **Convert** button to see the result.
5. The **Result** section displays the converted amount, and the last updated timestamp is shown below the title.

---

## API Used
The application fetches live exchange rates using the [ExchangeRate-API](https://www.exchangerate-api.com/). Note that free APIs may not provide real-time data; check the timestamp for accuracy.

---

## Requirements
- Python 3.7+
- Libraries:
  - `dearpygui`
  - `requests`

---

## Known Issues
- Slight discrepancies in exchange rates compared to other sources like Google due to differences in API data update frequency.
- Free APIs may not offer real-time data; consider using a paid API for greater accuracy.
