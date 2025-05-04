import datetime
import time

# === CONFIG ===
DIRECTION = "BUY"  # or "SELL" - You decide before 9:45
MOCK_PRICE = 45000  # Simulated NIFTY Midcap Futures Price
TRADE_DAY = "Monday"
TRADE_TIME = datetime.time(9, 45)

# === Utility Functions ===
def is_monday():
    return datetime.datetime.today().strftime('%A') == TRADE_DAY

def is_trade_time():
    now = datetime.datetime.now().time()
    return now >= TRADE_TIME

def calculate_levels(entry_price, direction):
    if direction.upper() == "BUY":
        target = entry_price * 1.01  # +1%
        stop_loss = entry_price * 0.997  # -0.30%
    else:
        target = entry_price * 0.99  # -1%
        stop_loss = entry_price * 1.003  # +0.30%
    return round(target, 2), round(stop_loss, 2)

# === Main Execution ===
def run_algo():
    if not is_monday():
        print("❌ Not Monday – No trade.")
        return

    while not is_trade_time():
        print("⏳ Waiting for 9:45 AM...")
        time.sleep(30)  # Check every 30 seconds

    entry = MOCK_PRICE  # Replace with real futures price from broker/NSE API
    print(f"✅ Trade Signal at 9:45 AM: {DIRECTION} @ ₹{entry}")

    target, stop_loss = calculate_levels(entry, DIRECTION)
    print(f"🎯 Target: ₹{target} | 🛑 Stop-Loss: ₹{stop_loss}")

    # Replace below with live price monitoring & exit logic
    print("📡 Start monitoring price... (LIVE execution logic here)")

run_algo()
