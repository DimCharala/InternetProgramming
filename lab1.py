import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input("Enter a URL: ")   # προσδιορισμός του url

if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)

    print(f"Website headers are {url} \n , {response.headers} \n\n")  #printing website headers

    server = response.headers.get('Server')

    #server information
    if server:
        print(f"The server is {server}")
    else:
        print("No server found")

    #cookies information
    cookies = response.headers.get("Set-Cookie")
    
    if cookies:
        #δημιουργεί cookieJar για την ευκολότερη χρήση των cookies
        total_cookies = response.cookies
        for cookie in total_cookies: #για κάθε cookie
            if cookie.expires:   #έλεγχος ύπαρξης τιμής expires
                expiresDate = datetime.datetime.fromtimestamp(cookie.expires) #date format
                print(f"Cookie name: {cookie.name}, Cookie expires: {expiresDate}")
            else:
                print(f"Cookie name: {cookie.name}, Cookie expires: Not found")
    else:
        print("No cookie found")
