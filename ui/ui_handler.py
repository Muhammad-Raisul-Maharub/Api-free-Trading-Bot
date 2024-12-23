import json
from PyQt5 import QtWidgets, QtCore
import json


class TradingBotUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Crypto Trading Bot")
        self.setGeometry(200, 200, 600, 500)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()

        # Cryptocurrency Selection
        crypto_label = QtWidgets.QLabel("Select Cryptocurrencies:")
        self.crypto_list = QtWidgets.QListWidget()
        self.crypto_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.crypto_list.addItems(["BTC", "ETH", "SOL", "ADA", "DOGE", "BNB", "DOT"])
        main_layout.addWidget(crypto_label)
        main_layout.addWidget(self.crypto_list)

        # Wager Input
        wager_layout = QtWidgets.QHBoxLayout()
        wager_label = QtWidgets.QLabel("Wager:")
        self.wager_input = QtWidgets.QLineEdit()
        self.wager_input.setPlaceholderText("Enter wager amount")
        wager_layout.addWidget(wager_label)
        wager_layout.addWidget(self.wager_input)
        main_layout.addLayout(wager_layout)

        # Multiplier Input
        multiplier_layout = QtWidgets.QHBoxLayout()
        multiplier_label = QtWidgets.QLabel("Multiplier:")
        self.multiplier_input = QtWidgets.QLineEdit()
        self.multiplier_input.setPlaceholderText("Enter payout multiplier")
        multiplier_layout.addWidget(multiplier_label)
        multiplier_layout.addWidget(self.multiplier_input)
        main_layout.addLayout(multiplier_layout)

        # Take Profit
        profit_layout = QtWidgets.QHBoxLayout()
        take_profit_label = QtWidgets.QLabel("Take Profit %:")
        self.take_profit_input = QtWidgets.QLineEdit()
        self.take_profit_input.setPlaceholderText("Enter profit percentage")
        profit_layout.addWidget(take_profit_label)
        profit_layout.addWidget(self.take_profit_input)
        main_layout.addLayout(profit_layout)

        # Stop Loss
        loss_layout = QtWidgets.QHBoxLayout()
        stop_loss_label = QtWidgets.QLabel("Stop Loss %:")
        self.stop_loss_input = QtWidgets.QLineEdit()
        self.stop_loss_input.setPlaceholderText("Enter loss percentage")
        loss_layout.addWidget(stop_loss_label)
        loss_layout.addWidget(self.stop_loss_input)
        main_layout.addLayout(loss_layout)

        # Mode Selection (Manual/Auto)
        mode_layout = QtWidgets.QHBoxLayout()
        mode_label = QtWidgets.QLabel("Mode:")
        self.mode_combo = QtWidgets.QComboBox()
        self.mode_combo.addItems(["Manual", "Auto"])
        mode_layout.addWidget(mode_label)
        mode_layout.addWidget(self.mode_combo)
        main_layout.addLayout(mode_layout)

        # Start and Stop Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.start_button = QtWidgets.QPushButton("Start Bot")
        self.start_button.clicked.connect(self.start_bot)
        self.stop_button = QtWidgets.QPushButton("Stop Bot")
        self.stop_button.clicked.connect(self.stop_bot)
        self.stop_button.setEnabled(False)  # Disabled until the bot is running
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        main_layout.addLayout(button_layout)

        # Save and Load Settings
        settings_layout = QtWidgets.QHBoxLayout()
        self.save_button = QtWidgets.QPushButton("Save Settings")
        self.save_button.clicked.connect(self.save_settings)
        self.load_button = QtWidgets.QPushButton("Load Settings")
        self.load_button.clicked.connect(self.load_settings)
        settings_layout.addWidget(self.save_button)
        settings_layout.addWidget(self.load_button)
        main_layout.addLayout(settings_layout)

        # Set main layout
        self.setLayout(main_layout)

    def start_bot(self):
        selected_cryptos = [item.text() for item in self.crypto_list.selectedItems()]
        if not selected_cryptos:
            QtWidgets.QMessageBox.warning(self, "Error", "Please select at least one cryptocurrency.")
            return

        wager = self.wager_input.text()
        multiplier = self.multiplier_input.text()

        if not wager or not multiplier:
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all required fields.")
            return

        # Start bot logic (you can integrate the trading bot logic here)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        QtWidgets.QMessageBox.information(self, "Bot Started", f"Trading bot started for {', '.join(selected_cryptos)}.")

    def stop_bot(self):
        # Stop bot logic (you can add functionality to stop the bot here)
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        QtWidgets.QMessageBox.information(self, "Bot Stopped", "Trading bot has been stopped.")

    def save_settings(self):
        settings = {
            "cryptos": [item.text() for item in self.crypto_list.selectedItems()],
            "wager": self.wager_input.text(),
            "multiplier": self.multiplier_input.text(),
            "take_profit": self.take_profit_input.text(),
            "stop_loss": self.stop_loss_input.text(),
            "mode": self.mode_combo.currentText(),
        }
        with open("settings.json", "w") as file:
            json.dump(settings, file)
        QtWidgets.QMessageBox.information(self, "Success", "Settings saved!")

    def load_settings(self):
        try:
            with open("settings.json", "r") as file:
                settings = json.load(file)
            for i in range(self.crypto_list.count()):
                item = self.crypto_list.item(i)
                item.setSelected(item.text() in settings["cryptos"])
            self.wager_input.setText(settings["wager"])
            self.multiplier_input.setText(settings["multiplier"])
            self.take_profit_input.setText(settings["take_profit"])
            self.stop_loss_input.setText(settings["stop_loss"])
            self.mode_combo.setCurrentText(settings["mode"])
            QtWidgets.QMessageBox.information(self, "Success", "Settings loaded!")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self, "Error", "No saved settings found.")
