from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium driver
driver = webdriver.Chrome()
urls=["https://www.amazon.in/dp/B0CM5VYBTY?th=1","https://www.amazon.in/dp/B0CM5VYBTY?th=4","https://www.amazon.in/Apple-iPad-Pro-13%E2%80%B3-M4/dp/B0D3J8C5HF?ref_=ast_sto_dp&th=1","https://www.amazon.in/Apple-2024-MacBook-Laptop-chip/dp/B0CX23YFG1/ref=sr_1_2_sspa?crid=1IZ2ZRL75OKHW&dib=eyJ2IjoiMSJ9.gtgA6rWpQsqc0Yfq6Sq1Wr04f1uGCs0sDDvnY8udhRMMCFBjviIXeh8bB-jJKqzOCGR3xt6MFBF1mfBvImiXxSepjAk49iaflsT0bzrdDpLOfW34ajdcPVolV7MbOg0VphxBNH0fVWXSjJOJQAxGdzdLvN7M1tnsMA-DDdffiq_4NgR75L13Wy_azD3gj9Pkt3vnVTLqNC4Akr36bV6OxXBcdL7WWZoevjmfrrtaVSc._3GqqHrx52L52JMxW7GsoL72kQc_MbGHo-25Wr-lbFs&dib_tag=se&keywords=laptop&qid=1730007524&refinements=p_72%3A1318476031&rnid=1318475031&sprefix=laptop%2Caps%2C196&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"]
# Open the product page
#url = f"https://www.amazon.in/Apple-2024-MacBook-Laptop-chip/dp/B0CX23YFG1/ref=sr_1_2_sspa?crid=1IZ2ZRL75OKHW&dib=eyJ2IjoiMSJ9.gtgA6rWpQsqc0Yfq6Sq1Wr04f1uGCs0sDDvnY8udhRMMCFBjviIXeh8bB-jJKqzOCGR3xt6MFBF1mfBvImiXxSepjAk49iaflsT0bzrdDpLOfW34ajdcPVolV7MbOg0VphxBNH0fVWXSjJOJQAxGdzdLvN7M1tnsMA-DDdffiq_4NgR75L13Wy_azD3gj9Pkt3vnVTLqNC4Akr36bV6OxXBcdL7WWZoevjmfrrtaVSc._3GqqHrx52L52JMxW7GsoL72kQc_MbGHo-25Wr-lbFs&dib_tag=se&keywords=laptop&qid=1730007524&refinements=p_72%3A1318476031&rnid=1318475031&sprefix=laptop%2Caps%2C196&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
for url in urls:

    driver.get(url)

    time.sleep(2)  # Wait for the page to load

    # Scroll to load all reviews or click 'load more' if necessary
    scroll_pause = 2  # Adjust based on site behavior
    for _ in range(5):  # Adjust scroll count as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)

    # Extract HTML and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.find_all('div',
                            class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content')  # Modify selector based on page

    # Close the driver
    driver.quit()
    l = []
    # Print out reviews
    for review in reviews:
        print(review.get_text())
        l.append(review.get_text().replace(',', ''))

import pandas as pd

# Convert the list to a DataFrame
df = pd.DataFrame(l, columns=["Item"])

# Write DataFrame to CSV
df.to_csv('data.csv', index=False)


import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string


# Initialize stop words, lemmatizer, and punctuation list
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
punctuation_table = str.maketrans('', '', string.punctuation)


def preprocess_review(text):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    text = text.translate(punctuation_table)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stop words and non-alphabetic tokens
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


# Process the sample review
for i in reviews:
    print(preprocess_review(i.get_text()))

