# Web-Data-Extractor

#### A program that parses and extracts dats from a book rating website and only displays the titles of books with 4 or 5-star rating on the console.
### Technology Used:
This project is created using Python. 

To run this project I had to install three python libraries to help me with the parsing and data extraction process:
- beautifulsoup4 (html parser)
- lxml (allows python to process the HTML and XML languge)
- requests (HTTP library)
  
I also used an open website that was created for web-scraping demos to complete this project: https://books.toscrape.com/
### Process: 
I followed a tutorial from a Udemy Python course to create this project. I started by installing the libraries to my laptop using Terminal. Then I learned how to find the page sources of websites which shows the html code used to create the site. Using the html code found, I was able to know where I needed to select code to read and find the ratings and titles of books on the website. Using my knowledge of Python, the website's html code, and the tutorial's guide to using the libraries, I was able to sucessfully run the program. However, I had bug which I was able to quickly fix. My program ran, but there was no output. After debugging and adding print lines thoughout my code, I found that my program never entered the main loop. I saw that I had a small syntax error which my IDE did not flag. I had specified my range for my loop as "(1-51)" rather than "(1, 51)". After this small fix, my program was able to run accurately. 

