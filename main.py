import tkinter as tk
from selenium import webdriver
from utils.trade_logic import TradingBot
from ui.ui_handler import TradingBotUI
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    bot_ui = TradingBotUI()
    bot_ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


class RollbitBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rollbit Trading Bot")

        # GUI components
        self.create_widgets()

    def create_widgets(self):
        # Wager Input
        tk.Label(self.root, text="Wager ($):").grid(row=0, column=0, padx=10, pady=5)
        self.wager = tk.Entry(self.root)
        self.wager.grid(row=0, column=1)

        # Multiplier Input
        tk.Label(self.root, text="Multiplier (x):").grid(row=1, column=0, padx=10, pady=5)
        self.multiplier = tk.Entry(self.root)
        self.multiplier.grid(row=1, column=1)

        # RSI Threshold
        tk.Label(self.root, text="RSI Threshold:").grid(row=2, column=0, padx=10, pady=5)
        self.rsi_threshold = tk.Entry(self.root)
        self.rsi_threshold.grid(row=2, column=1)

        # Buttons
        tk.Button(self.root, text="Start Bot", command=self.start_bot).grid(row=3, column=0, pady=10)
        tk.Button(self.root, text="Stop Bot", command=self.stop_bot).grid(row=3, column=1, pady=10)

    def start_bot(self):
        # Collect inputs
        wager = float(self.wager.get())
        multiplier = float(self.multiplier.get())
        rsi_threshold = int(self.rsi_threshold.get())

        # Start trading logic
        bot = TradingBot(wager, multiplier, rsi_threshold)
        bot.run()

    def stop_bot(self):
        print("Stopping the bot...")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RollbitBotApp(root)
    root.mainloop()
