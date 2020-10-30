import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


# This function is incomplete
# Looks at product page and extracts more granular information
def item_page(my_url):
    # gets page for GPU
    my_url = 'https://www.newegg.com/evga-geforce-gtx-1080-ti-11g-p4-6591-kr/p/N82E16814487376?Description=GTX'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # gets html code from url
    page_soup = soup(page_html, 'html.parser')

    # gather specific details on item
    price = page_soup.findAll('li', {'class': 'price-current'})[0].text
    written_reviews_container = page_soup.findAll('div', {'class': 'rating rating-%'})


# Looks through newegg search result page and extracts relevent information
# Information extracted: name, brand, price, rating, shipping, url
def build_table(my_url, model):
    # open URL connect --> graps page info/stuff
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # gets html code from url
    page_soup = soup(page_html, 'html.parser')

    # looks through entire page to find containers that hold GPU info
    containers = page_soup.findAll('div', {'class': 'item-container'})
    # print(containers)

    # the first 4 items are recommended advertisement items --> so we skip them
    containers = containers[4:len(containers)]

    headers = ['brand', 'model', 'product_name', 'price', 'rating', 'shipping', 'url']
    df = pd.DataFrame(columns=headers)

    # loop through each GPU in container and gather data
    for container in containers:

        container_tag_list = [tag.name for tag in container.div.div.find_all()]

        if 'img' in container_tag_list:
            # print(container)

            brand = container.div.div.a.img['title'].split()[0]

            stars = container.div.div.find_all('a', {'class', 'item-rating'})

            if stars:
                rating = stars[0]['title'][-1]
            else:
                rating = None

            title_container = container.findAll('a', {'class': 'item-title'})
            product_name = title_container[0].text

            shipping_container = container.findAll('li', {'class': 'price-ship'})
            shipping = shipping_container[0].text

            product_url = container.a['href'].split()[0]

            price_container = container.findAll('li', {'class', 'price-current'})
            product_price = price_container[0].text

            new_rows = pd.Series([brand, model, product_name, product_price, rating, shipping, product_url],
                                 index=df.columns)
            df = df.append(new_rows, ignore_index=True)

    return df


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # set the number of pages for your URL

    headers = ['brand', 'model', 'product_name', 'price', 'rating', 'shipping', 'url']
    master_df = pd.DataFrame(columns=headers)

    print('Enter GPU Model (NOTE: Should be the name of the item searched Newegg search bar)')
    print('Example: GTX 1080')
    GPU_model = input()

    print('Max digit for number of pages to scrape')
    max_page = int(input())

    print(
        'Enter URL (NOTE: Make sure page is at the very end of the URL without a number to the page traversal to work properly)')
    print('EXAMPLE URL for GTX 1080: https://www.newegg.com/p/pl?d=GTX+1080&N=100007709&isdeptsrh=1&PageSize=96&page=')
    url = input()

    for i in range(1, max_page + 1):
        url = url + str(i)
        df = build_table(url, GPU_model)

        master_df = pd.concat([master_df, df])

    file_name = 'products_' + GPU_model

    # item_page('https://www.newegg.com/evga-geforce-gtx-1080-ti-11g-p4-6591-kr/p/N82E16814487376?Description=GTX')
    master_df.to_csv(f'{file_name}.csv', index=False)
    print('done')
