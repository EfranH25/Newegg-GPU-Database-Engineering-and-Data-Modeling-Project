# Newegg Web Scrapper GPU Database Creator

<br />
<p align="center">
  <h3 align="center">Newegg Web Scrapper and GPU Database Creator
</h3>

  <p align="center">
  This project is a web scrapper that can be used on Newegg.com to gather product information related to graphics cards.
    <br />
    <a href="https://github.com/EfranH25/New-Egg-GPU-Scapper"><strong>Explore the Repo</strong></a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Background](#Background)
  * [Summary](#Summary)
  * [Tools](#Tools)
* [Usage](#Usage)
  * [Explaination](#Explanation)
  * [Limitations](#Limitations)
* [Contact](#contact)


<!-- Background -->
## Background
I wanted ot create a web scrapper that can quickly aggregate information on graphics cards from Newegg.com to create a graphics card database to be used for potential data science projects. 
This project does just that. 

### Summary
This project utilizes the beatifulsoup python library to scrape GPU information from Newegg.com. Currently the information that is take include brand name, model name, product name,
rating out of five stars, shipping cost, and item URL. 

### Tools
* Python: Language used
* Beautifulsoup python package: Used to scrape data
* Pandas python package: Used to store data
* MS Excel: Data saved as CSV files that MS Excel can easily read

<!-- Usage -->
## Usage
To use the project, simply run the python script. It will ask for the item model you are searching for, the max number of pages to scrape, and the Newegg URL. Simply fill in the information correctly
and the script will produce a csv with the collected results.

### Explanation
URL prepartion before running script: Before running the script, search the item you would like on newegg (i.e. GTX 1080). Once the page loads up, I suggest setting the number of items viewed per page to its maximum value
(i.e. 96 items per page). This is because if you scrapper goes through many pages, there's a chance newegg will block it. After setting the view per page, I would go to filters and ensure only 'Desktop Graphics Cards' is selected to 
ensure other products, such as desktops, are not included in the data.

- Item model: A simple string  of the name of the item you searched on newegg.
- Max page: Set the number of pages you would like to scrape. Generally 1-3 pages is safe. More than that may cause the program to be blocked.
- URL: Insert the url after applying all the filters on the website. 
NOTE: To ensure the page scrapping implementation works properly, make sure at the end of the url is page=
(i.e. https://www.newegg.com/p/pl?d=GTX+1080&N=100007709&isdeptsrh=1&PageSize=96&page= and NOT https://www.newegg.com/p/pl?d=GTX+1080&N=100007709&isdeptsrh=1&PageSize=96& 
or https://www.newegg.com/p/pl?d=GTX+1080&N=100007709&isdeptsrh=1&PageSize=96&page=2)

### Limitations
I have not done extensive testing on other products but it should work for other product types without much issues (minor code adjustments may be needed). Also, for items that do not have a brand 
associated with it, the code drops those items at the momment as I didnt implement a way to handle those cases yet

<!-- CONTACT -->
## Contact
If you have any questions of feedback, feel free to contact me :D

Efran Himel - efranhimel@gmail.com

Project Link: [https://github.com/EfranH25/New-Egg-GPU-Scapper](https://github.com/EfranH25/New-Egg-GPU-Scapper)
