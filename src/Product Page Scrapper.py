import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time


def item_page(my_url=None):
    """
    :param my_url: takes in a URL --> the URL should be the page for the product in Newegg.com
    :return: Returns a single row dataframe that has all the specifications of GPU stored on the page
    NOTE: By features, I'm referring the the specs tab thas is available at the bottom of all gpu pages
    """
    # gets page for GPU

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # gets html code from url
    page_soup = soup(page_html, 'html.parser')

    # get number of reviewers for item
    review_number = page_soup.findAll('span', {'class': 'item-rating-num'})
    if len(review_number) > 0:
        review_number = review_number[0].text
    else:
        review_number = '0 reviews'

    # specs list will contain all the spec information from url
    specs_list = {}
    specs_list['review_numbers'] = review_number

    # goes to general area in html where specs is located
    tab_container = page_soup.findAll('div', {'class': 'tab-pane'})

    # a check to make sure I'm looking at the specs tab and not some other tab on the page
    for i in tab_container:
        check = i.findAll('table', {'class': 'table-horizontal'})
        if len(check) > 0:
            tab_specs = i
            break

    # gathers all the information from the specs tab and adds to spec_list
    for info in tab_specs.findAll('table', {'class': 'table-horizontal'}):
        caption_container = info.caption.text

        details = info.tbody.findAll('tr')
        for d in details:
            specs_list[d.th.text] = []
            specs_list[d.th.text].append(d.td.text)

    # converts spec_list to dataframe and returns it
    df_entry = pd.DataFrame(columns=specs_list.keys())
    df_entry = df_entry.append(specs_list, ignore_index=True)
    return df_entry


def crawler(df, name):
    """
    :param df: takes a df that has information regarding gpu's from Newegg.com. This df should have a url column for all
    the gpu's in df
    :return: returns a csv that has all the spec info of all the gpu's in the df
    Note: does not merge dataframes --> if you want to combine the csv, merge manually
    """
    new_col_set = set([])
    new_entry_list = []

    for row in df['url']:
        print(row)
        new_entry = item_page(row)

        new_entry_list.append(new_entry)

        for value in new_entry.columns:
            new_col_set.add(value)

        time.sleep(6)

    new_col_set = list(new_col_set)
    new_col_set.sort()
    new_df = pd.DataFrame(columns=new_col_set)
    new_df = new_df.append(new_entry_list)

    new_df.to_csv(f'{name}_Specs.csv', index=False)


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # set the number of pages for your URL

    headers = ['brand', 'model', 'product_name', 'price', 'rating', 'shipping', 'url']
    df = pd.read_csv('products_RTX 2080.csv')

    crawler(df, 'RTX 2080')
