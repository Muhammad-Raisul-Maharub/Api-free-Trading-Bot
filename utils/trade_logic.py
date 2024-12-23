# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Standard library imports
import time
import os

# Data analysis imports
import pandas as pd

import json

# Local imports
from utils.indicators import calculate_rsi

class TradingBot:
    def __init__(self, wager, multiplier, rsi_threshold):
        self.wager = wager
        self.multiplier = multiplier
        self.rsi_threshold = rsi_threshold
        self.driver = self.initialize_driver()
        self.trade_log = "assets/trade_logs.txt"
        self._ensure_log_directory()

    def _ensure_log_directory(self):
        os.makedirs(os.path.dirname(self.trade_log), exist_ok=True)

    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        try:
            driver.get("https://rollbit.com/trading/SOL")
            return driver
        except Exception as e:
            print(f"Failed to initialize driver: {str(e)}")
            driver.quit()
            raise

    def fetch_price_data(self, lookback_period=14):
        try:
            prices = []
            wait = WebDriverWait(self.driver, 10)
            price_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-selector"))
            )
            current_price = float(price_element.text.strip())
            prices.append(current_price)
            return prices
        except Exception as e:
            print(f"Error fetching price data: {str(e)}")
            return []

    def check_rsi(self, data):
        if len(data) < 2:
            print("Insufficient data for RSI calculation")
            return None
            
        try:
            rsi = calculate_rsi(pd.Series(data))
            print(f"Current RSI: {rsi:.2f}")
            return rsi
        except Exception as e:
            print(f"Error calculating RSI: {str(e)}")
            return None

    def execute_trade(self, direction):
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            trade_info = f"[{timestamp}] {direction} trade executed - Wager: {self.wager}, Multiplier: {self.multiplier}"
            
            with open(self.trade_log, "a") as log:
                log.write(f"{trade_info}\n")
                
            # Implement actual trade execution logic here
            if direction == "Buy":
                buy_button = self.driver.find_element(By.CSS_SELECTOR, ".buy-button")
                buy_button.click()
            else:
                sell_button = self.driver.find_element(By.CSS_SELECTOR, ".sell-button")
                sell_button.click()
                
            print(f"Successfully executed {direction} trade")
            return True
            
        except Exception as e:
            print(f"Trade execution failed: {str(e)}")
            return False

    def run(self):
        try:
            data = self.fetch_price_data()
            if not data:
                print("No price data available")
                return False

            rsi = self.check_rsi(data)
            if rsi is None:
                return False

            if rsi < self.rsi_threshold:
                return self.execute_trade("Buy")
            elif rsi > 100 - self.rsi_threshold:
                return self.execute_trade("Sell")
            else:
                print(f"No trade executed. RSI ({rsi:.2f}) not meeting threshold conditions")
                return False

        except Exception as e:
            print(f"Bot execution error: {str(e)}")
            return False

    def cleanup(self):
        try:
            self.driver.quit()
        except:
            pass