import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_path_headers = "https://myhttpheader.com/"
my_email = "naamaavit@gmail.com"
my_password = os.getenv('GMAIL_PASS')
wanted_price = 400

cookies = {
    'csm-sid': '721-2617812-1384701',
    'x-amz-captcha-1': '1715075496251483',
    'x-amz-captcha-2': 'p3eNm4sa6V9g1wqJKZwH6A==',
    'session-id': '133-0915521-1122244',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'USD',
    'sp-cdn': '"L5Z9:IL"',
    'ubid-main': '134-4298917-0869910',
    'lc-main': 'en_US',
    'session-token': 'RGtjDKb1QAbs9p6FUKMgG6tMy9IzN37FE4oW9vg/OUc8i9UxZnorXB5qfLtJmUYTpYnqsqdbj5ZOSoutpExF+VtBn2o7svnxcCcMLLxae0eoFUdewmqnDQdf26e4BWI3+v+lEAAZorgdWY2M3DPYu9G8IanN2fkkWRG9Cw0cm9QPH4yBl5YKkCLTVALuKFXHxWZcOolbeoX+pCl00H46vPYnU0SCw05W3YXj524O0W38WWZhNyNAOyczF08fk/rafmY5M/wmrW9GH1t8GMbFsTwwQr1BWRXx+FISoKvk1N1U4kRItvTZhoTNjLWWLCbJtkog2p0LsQywDqrYrFmD8rR9To9XAATw',
    'csm-hit': 'tb:WX69K721XPNEHNRNK45E+s-2MPH022DS5J3FY8M87H0|1715079407729&t:1715079407729&adb:adblk_yes',
}

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,he;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'csm-sid=721-2617812-1384701; x-amz-captcha-1=1715075496251483; x-amz-captcha-2=p3eNm4sa6V9g1wqJKZwH6A==; session-id=133-0915521-1122244; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:IL"; ubid-main=134-4298917-0869910; lc-main=en_US; session-token=RGtjDKb1QAbs9p6FUKMgG6tMy9IzN37FE4oW9vg/OUc8i9UxZnorXB5qfLtJmUYTpYnqsqdbj5ZOSoutpExF+VtBn2o7svnxcCcMLLxae0eoFUdewmqnDQdf26e4BWI3+v+lEAAZorgdWY2M3DPYu9G8IanN2fkkWRG9Cw0cm9QPH4yBl5YKkCLTVALuKFXHxWZcOolbeoX+pCl00H46vPYnU0SCw05W3YXj524O0W38WWZhNyNAOyczF08fk/rafmY5M/wmrW9GH1t8GMbFsTwwQr1BWRXx+FISoKvk1N1U4kRItvTZhoTNjLWWLCbJtkog2p0LsQywDqrYrFmD8rR9To9XAATw; csm-hit=tb:WX69K721XPNEHNRNK45E+s-2MPH022DS5J3FY8M87H0|1715079407729&t:1715079407729&adb:adblk_yes',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1',
    'ect': '4g',
    'referer': 'https://www.amazon.com/s?k=hair+removal+device&crid=ZXUY9J11LU70&sprefix=hair+re%2Caps%2C223&ref=nb_sb_ss_ts-doa-p_1_7',
    'rtt': '100',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-viewport-width': '957',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'viewport-width': '957',
}

price_response = requests.get("https://www.amazon.com/Braun-Long-lasting-i%C2%B7Expert-Alternative-PL7243/dp/B0CMVN2KTP/ref=sr_1_4_sspa?crid=ZXUY9J11LU70&dib=eyJ2IjoiMSJ9.64wBO6be9vIejXAbqEGt_ev2ckja4meaImCVmiUuMIAI73gfSHt-d_9a9SXKe2wkeI89a_LTHzD3NQJ2baHC7xfoOH5AhKuBXaEPB5gNGqk5CGblSd97YvBHnrMdhdgV_TtcrNxdg0aguN6Q7lGXsrr3q_JWbzlrJStBf4BjdnDWT6fUgxqvdXW1cQZv7muFtmej9FH_CIT7D0zuWLR5_wolnPwiUZc0fGhqidXeXQDdy3aM2gr8-xx8Te17UcKjjUquUpD4TkJtgt84ANREXNrW0E_ltjBZKL-JwSe4t-U.PsDDmwWEC1K6DQwHUB6FJyG-4UdPSiFpbyIxu3K6RKM&dib_tag=se&keywords=hair+removal+device&qid=1715071125&sprefix=hair+re%2Caps%2C223&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1", headers=headers, cookies=cookies)
price_response = price_response.text
soup = BeautifulSoup(price_response, "html.parser")
price = soup.find_all("span", class_="a-price-whole")
price = int(price[1].get_text()[:-1])
item = soup.find("span", id="productTitle")
string_item = item.get_text()



letter = f"HEY!\nYou have the: \n{string_item}\n\nin the price of: {price}\ngo and buy!\nkisses,\nNaama."

#
# if price >= wanted_price:
#     with SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email, to_addrs=my_email,
#                             msg=f"subject:Price Alart!\n\n{letter}")
#         print("mail send")
# else:
#     print(f"the price today of {string_item} is {price}. maybe tomorrow :)")


if price >= wanted_price:
    msg = MIMEMultipart()
    msg['Subject'] = "Price Alert!"
    msg.attach(MIMEText(letter, 'plain', 'utf-8'))

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.as_string())