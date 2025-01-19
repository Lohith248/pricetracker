# Price Tracker

## Overview
The Price Tracker project is a Python application that monitors the price of a product on an e-commerce website and sends an email notification when the price drops below a specified target. The project uses web scraping to extract price information and email notifications to alert the user.

## Features
- Monitors product prices on e-commerce websites.
- Sends email notifications when the price drops below the target.
- Uses environment variables to securely store email credentials.
- Includes exception handling to ensure robustness.
- Provides automated tests for core functions.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `smtplib` (included in Python standard library)
- `python-dotenv`
- `pytest`

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Lohith248/pricetracker.git
    cd pricetracker
    ```
2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory based on the provided `.env.example` file:
    ```sh
    cp .env.example .env
    ```

4. Open the `.env` file and add your email credentials:
    ```
    FROM_EMAIL=your_email@gmail.com
    FROM_PASSWORD=your_password
    ```

## Usage
1. Update the `url`, `target_price`, and `check_interval` variables in [project.py](http://_vscodecontentref_/1) with the desired values.
2. Run the script:
    ```sh
    python project.py
    ```

## Testing
Run the test cases using `pytest`:
```sh
pytest
