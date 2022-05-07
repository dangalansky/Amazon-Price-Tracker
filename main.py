from bs4 import BeautifulSoup
import requests
import smtplib

# Constants
PRODUCT_URL = 'PRODUCT URL'
MAX_PRICE = INT(HIGHEST PRICE YOU WISH TO PAY)
EMAIL = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'

# HTML Request
headers = {
    'Accept-Language' : 'en-US,en;q=0.9',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
}

response = requests.get(PRODUCT_URL, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

# product information
product_title = soup.find('span', id="productTitle").getText()
current_price = float(soup.find('span', class_='a-offscreen').getText().split('$')[1])

# email protocol, if price lower than max
if current_price <= MAX_PRICE:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'subject: {product_title} Now Available!\n\n{product_title} now on sale for {current_price}!\nBuy Now: {PRODUCT_URL}')
