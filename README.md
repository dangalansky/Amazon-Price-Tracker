# Amazon-Price-Tracker
Set a maximum price on an Amazon product, receive an email with a link when it's at or below your price!

# How it Works:

You'll need to import BeautifulSoup, requests and smtplib!

Requests allows your computer to reach out to a specific URL.<br>
BeautifulSoup parses HTML for data according to parameters you set.<br>
Smtplib (Simple Mail Transer Protocol Library) automates your email to send others or in this case, yourself mail.

# Step by step

1) Copy and paste your URL from Amazon inside quotes next to the PRODUCT_URL constant
2) Indicate the max price as an int next to the MAX_PRICE constant
3) Copy and paste your email and password inside quotes next to the EMAIL and PASSWORD constants
4) This code is set up for gmail
5) If using e-mail other than gmail, research proper host URL and port information on line 27 inside parentheses --> smtplib.SMTP('smtp.gmail.com', 587)

