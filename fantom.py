import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

async def main():
    wallet_address = '0xYourFantomTestnetWalletAddress'  # <-- Replace with your Fantom Testnet address

    browser = await launch(headless=False, args=['--start-maximized', '--no-sandbox'])
    page = await browser.newPage()
    await page.setViewport({'width': 1280, 'height': 900})

    print("Navigating to Chainlink Faucet...")
    await page.goto('https://faucets.chain.link/', {'waitUntil': 'networkidle2'})

    # Prompt user to connect wallet manually
    try:
        print("Waiting for Connect Wallet button...")
        await page.waitForSelector('button:contains("Connect Wallet")', timeout=20000)
        print("Please connect your wallet in the browser window, then press Enter here.")
        input("Press Enter after your wallet is connected...")
    except TimeoutError:
        print("Connect Wallet button not found. Please connect manually if already visible.")

    # Wait for the wallet address input field
    try:
        print("Waiting for wallet address input field...")
        await page.waitForSelector('input[type="text"]', timeout=20000)
        await page.type('input[type="text"]', wallet_address)
        print("Wallet address entered.")
    except TimeoutError:
        print("Wallet address input not found. Exiting.")
        await browser.close()
        return

    # Select Fantom Testnet faucet
    try:
        print("Selecting Fantom Testnet faucet...")
        await page.waitForSelector('label[for="fantomTestnet"]', timeout=10000)
        await page.click('label[for="fantomTestnet"]')
        print("Fantom Testnet selected.")
    except TimeoutError:
        print("Fantom Testnet selector not found. Please check the selector.")
        await browser.close()
        return

    # Click the "Send Request" button
    try:
        print("Waiting for Send Request button...")
        await page.waitForSelector('button[type="submit"]', timeout=10000)
        await page.click('button[type="submit"]')
        print("Send Request button clicked.")
    except TimeoutError:
        print("Send Request button not found. Please check the selector.")
        await browser.close()
        return

    # Wait to observe result
    await asyncio.sleep(5)

    print("Faucet request sent (if all went well).")
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
