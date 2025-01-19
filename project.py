import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time
import re
import os
from dotenv import load_dotenv  # Import dotenv to load .env variables

# Load environment variables from .env file
load_dotenv("project.env")

def get_price(url):
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Cache-Control': 'max-age=0'
        })
        soup = BeautifulSoup(response.content, 'html.parser')

        price_element = soup.select_one('.a-price-whole')  # Amazon
        # price_element = soup.select_one('.Nx9bqj CxhGGd')  # Flipkart (if needed)

        if price_element:
            price_text = price_element.text.strip()
            price_number = re.findall(r'[\d,]+', price_text)
            if price_number:
                price = float(price_number[0].replace(',', ''))
                return price
        return None
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def send_email(subject, body, to_email, from_email, from_password):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def track_price(url, target_price, check_interval, to_email, from_email, from_password):
    while True:
        current_price = get_price(url)
        if current_price is not None:
            print(f"Current Price: ₹{current_price}")
            if current_price <= target_price:
                subject = "Product Price Dropped!"
                body = f"The price dropped to ₹{current_price}!\nThis is below your target price of ₹{target_price}.\nCheck the product here: {url}"
                send_email(subject, body, to_email, from_email, from_password)
                break
            else:
                print("Price not yet low enough, checking again later.")
        else:
            print("Could not retrieve the current price, will try again.")

        time.sleep(check_interval)

def main():
    url = "https://www.amazon.in/iPhone-16-128-GB-Control/dp/B0DGJHBX5Y/ref=sr_1_1_sspa?adgrpid=1327112140166765&dib=eyJ2IjoiMSJ9.5T1ROATQZk0zz1bhpRGsxR4g2sZDgZ85BNfFUd6Hks4I8suqY3-DogLYDbpQtZQfHCAfs0Nog83ck5MG23UWjQ9GXwEwNxQwI5X_1SlIdo-ebuWmJOnbuBdOrCYlA0PX7bFhDD963zYSaN1YbtrmFBcvP7Zeoz4UDZ9WL5W79iORUhllcmnLnKZLB6lTuWJ0QvIAmLgZfPulla4WkkmzY4aczr2L_L1spts6qiIQWKA._W-tTFHHBdhPJCrM7qQDqMM8CFtFRkwgN0f9I8Z19uA&dib_tag=se&hvadid=82944779931259&hvbmt=bp&hvdev=c&hvlocphy=157506&hvnetw=o&hvqmt=p&hvtargid=kwd-82945383608131%3Aloc-90&hydadcr=15396_2369780&keywords=iphone+16&msclkid=1092806a1bf21d7cb669e7e6f0334cbf&qid=1737288643&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    target_price = 70000
    check_interval = 3600

    # Load email credentials from environment variables
    from_email = os.getenv("FROM_EMAIL")
    from_password = os.getenv("FROM_PASSWORD")
    to_email = "emailid@gmail.com" #enter your email id

    if not from_email or not from_password:
        print("Please set the FROM_EMAIL and FROM_PASSWORD environment variables in a .env file.")
        return

    print("Starting price tracking...")
    track_price(url, target_price, check_interval, to_email, from_email, from_password)

if __name__ == "__main__":
    main()
