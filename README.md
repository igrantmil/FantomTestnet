

# FantomTestnet

**Auto Faucet Fantom Testnet**

---

## Overview

**FantomTestnet** is a Python automation tool that simplifies the process of requesting testnet tokens from the Fantom Testnet faucet. By automating browser actions, this script helps developers and testers quickly obtain Fantom testnet tokens for their wallet addresses.

---

## Features

- Automates the process of requesting tokens from the Fantom Testnet faucet
- Easy setup and usage
- Customizable for other testnet faucets

---

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/igrantmil/FantomTestnet.git
    cd FantomTestnet
    ```

2. **Install dependencies:**  
   *(Update this list if you use additional libraries)*
    ```sh
    pip install pyppeteer
    ```

---

## Usage

1. **Edit the script** to add your Fantom Testnet wallet address:
    ```python
    wallet_address = '0xYourFantomTestnetWalletAddress'
    ```
2. **Run the script:**
    ```sh
    python fantom.py
    ```

3. **Follow the on-screen instructions:**
    - A browser window will open.
    - Connect your wallet manually if required.
    - The script will fill in your wallet address, select the Fantom Testnet faucet, and request tokens.

---

## Configuration

- **Selectors:**  
  If the faucet website updates its layout, you may need to update the CSS selectors in the script.
- **Headless Mode:**  
  By default, the browser opens visibly. You can change this in the script if you prefer headless operation.

---

## Disclaimer

- This tool is for development and testing purposes only.
- Not affiliated with Fantom or any faucet provider.
- Use at your own risk.

---

## License

MIT License

