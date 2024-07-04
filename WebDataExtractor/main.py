# A program that parses and extracts data from a book rating website 
# and only displays the titles of books with 4 or 5-star rating on the console.

import bs4
import requests

# Website from which data will be extracted
# added a bracket after "page" since we need to see multiple pages

websiteURL = 'https://books.toscrape.com/catalogue/page-{}.html'


# create list of 4 and 5 star books

highRatedBooks = []

# Iterate all 50 pages of the website


for page in range(1, 51):

    # create a new soup for each page to get html contents of provided url
    
    pageURL = websiteURL.format(page)
    result = requests.get(pageURL)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')


    # select data of books 
    # library can read the html contents of each book

    books = soup.select('.product_pod')

    
    # Iterate books and organize by rating 

    for book in books:
        
        # check if the book is 4 or 5 stars

        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            
           
            #store the book titles in list by specifiying the <a> tag, index 1, and 'title'

            bookTitle = book.select('a')[1]['title']
            
            highRatedBooks.append(bookTitle)

 
#Print list 

for b in highRatedBooks:
   print(b)

    




