# Rollbit Trading Bot

A Python-based trading bot for automating trades on the Rollbit platform. This bot uses Selenium for browser automation and includes a GUI built with Tkinter for user-friendly control.

---

## Features
- Interactive GUI for setting trade parameters (wager, multiplier, trading pair, etc.)
- RSI-based trading logic
- Take-profit and stop-loss functionality
- Trade lock to prevent repeat trades on the same pair for 10 minutes
- Maximum concurrent trades limit
- Adjustable variables for customization

---

## Setup

### Prerequisites
1. **Python 3.7 or higher**: Install Python from [python.org](https://www.python.org/downloads/).
2. **Google Chrome**: Install Chrome from [here](https://www.google.com/chrome/).
3. **ChromeDriver**: Download the version matching your installed Chrome browser from [here](https://chromedriver.chromium.org/downloads).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rollbit-trading-bot.git
   cd rollbit-trading-bot
