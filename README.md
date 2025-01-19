# Price Tracker
#### Video Demo:  <URL HERE>
#### Description:
The Price Tracker project is a Python-based application designed to monitor the price of a product on an e-commerce website and send an email alert when the price drops below a specified target. This project leverages web scraping techniques to extract price information and uses email services to notify the user.

### Project Structure

#### project.py
This is the main file of the project and contains the core functionality. It includes the following functions:

1. **get_price(url)**: This function takes a URL as input and returns the price of the product from the specified e-commerce website. It uses the `requests` library to fetch the webpage content and `BeautifulSoup` to parse the HTML and extract the price. The function handles exceptions and returns `None` if any error occurs.

2. **send_email(subject, body, to_email)**: This function sends an email with the specified subject and body to the given email address. It uses the `smtplib` library to connect to the SMTP server and send the email. The function handles exceptions and prints an error message if any issue occurs during the email sending process.

3. **track_price(url, target_price, to_email)**: This function tracks the price of the product by calling the `get_price` function. If the price is below the target price, it sends an email alert using the `send_email` function.

4. **main()**: This is the main function that sets the URL, target price, and recipient email address. It continuously checks the price at regular intervals (every hour) by calling the `track_price` function.

#### test_project.py
This file contains the test cases for the functions in `project.py`. It uses the `pytest` framework to define and run the tests. The following test functions are included:

1. **test_get_price(monkeypatch)**: This test function mocks the `requests.get` method to return a predefined HTML content. It verifies that the `get_price` function correctly extracts the price from the mocked content.

2. **test_send_email(monkeypatch)**: This test function mocks the `smtplib.SMTP_SSL` class to simulate the email sending process. It verifies that the `send_email` function executes without errors.

3. **test_track_price(monkeypatch)**: This test function mocks the `get_price` and `send_email` functions to simulate the price tracking process. It verifies that the `track_price` function sends an email alert when the price is below the target price.

#### requirements.txt
This file lists the external libraries required for the project. The following libraries are included:

- `requests`: Used for making HTTP requests to fetch webpage content.
- `beautifulsoup4`: Used for parsing HTML content and extracting information.
- `pytest`: Used for writing and running test cases.

### Design Choices
1. **Web Scraping**: The project uses web scraping to extract price information from e-commerce websites. This approach is chosen because it allows the application to work with any website by simply changing the URL and the CSS selector for the price element.

2. **Email Notifications**: The project uses email notifications to alert the user when the price drops below the target. This approach is chosen because email is a widely used and reliable communication method.

3. **Exception Handling**: The functions in the project include exception handling to ensure that the application continues to run smoothly even if an error occurs. This design choice improves the robustness and reliability of the application.

4. **Testing**: The project includes test cases for the core functions to ensure that they work correctly. This approach is chosen to improve the quality and maintainability of the code.

### Conclusion
The Price Tracker project is a useful tool for monitoring product prices and receiving alerts when the price drops. It demonstrates the use of web scraping, email notifications, and automated testing in a real-world application. The project is designed to be extensible and can be easily adapted to track prices on different websites or send notifications through different channels.#   p r i c e t r a c k e r  
 