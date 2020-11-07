from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import os
import re


def adjust_dimensions(df, entry):
    """
    :param df: desired gpu database to convert 'Card Dimensions (L x H) '
    :param entry: name to save file as
    :return: creates a new column for the height and length of card in mm
    """
    df['Length (mm)'] = df['Card Dimensions (L x H) '].apply(lambda x: x.split('x')[0])
    df['Height (mm)'] = df['Card Dimensions (L x H) '].apply(lambda x: x.split('x')[-1])

    df['Length (mm)'] = df['Length (mm)'].str.replace('"', '', 1).replace('NONE', 0).astype('float64') * 25.4
    df['Height (mm)'] = df['Height (mm)'].str.replace('"', '', 1).replace('NONE', 0).astype('float64') * 25.4

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def remove_brackets(df, entry):
    """
    :param df: data frame of one of the gpu csv files
    :param entry: name to save file as
    :return: removes all brackets quotes [' and '] from the entries in the csv
    saves csv as entry name
    """
    cols = df.columns.tolist()[6:]

    for col in cols:
        df[col] = df[col].fillna('NONE')
        df[col] = df[col].str.replace('[', '', 1)
        df[col] = df[col].str.replace('\'', '', 1)
        df[col] = df[col].str.replace(']', '', -1)
        df[col] = df[col].str.replace('\'', '', -1)

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def fix_shipping(df, entry):
    df['shipping'] = df['shipping'].apply(lambda x: str(x).split(" ", 1)[0])

    df.loc[df['shipping'] == 'Free', 'shipping'] = 0

    df['shipping'] = df['shipping'].str.replace('$', '').astype('float64')

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def fix_price(df, entry):
    df['price'] = df['price'].apply(lambda x: str(x).split()[0].replace('$', ''))

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def fix_boost_clocks(df, entry):
    df['Boost Clock '] = df['Boost Clock '].fillna('NONE')
    df['boost clock (MHz)'] = df['Boost Clock '].apply(
        lambda x: list(re.findall(r'\d+', x))[0] if len(list(re.findall(r'\d+', x))) > 0 else 0).astype('float64')

    print(df['boost clock (MHz)'])

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def fix_core_clocks(df, entry):
    df['Core Clock '] = df['Core Clock '].fillna('NONE')
    df['core clock (MHz)'] = df['Core Clock '].apply(
        lambda x: list(re.findall(r'\d+', x))[0] if len(list(re.findall(r'\d+', x))) > 0 else 0).astype('float64')

    print(df['core clock (MHz)'])

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def fix_mem_clocks(df, entry):
    df['Effective Memory Clock '] = df['Effective Memory Clock '].fillna('NONE')
    df['memory clock (MHz)'] = df['Effective Memory Clock '].apply(
        lambda x: list(re.findall(r'\d+', x))[0] if len(list(re.findall(r'\d+', x))) > 0 else 0).astype('float64')

    print(df['memory clock (MHz)'])

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


def fix_review_numbers(df, entry):
    df['review_numbers'] = df['review_numbers'].fillna('NONE')
    df['number of reviews'] = df['review_numbers'].apply(
        lambda x: list(re.findall(r'\d+', x))[0] if len(list(re.findall(r'\d+', x))) > 0 else 0).astype('float64')

    print(df['number of reviews'])

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}', index=False)


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    entries = os.listdir('../PROJECT - Newegg GPU/Saved Data/Nvidia')

    for entry in entries:
        print(entry)
        df = pd.read_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}')

        remove_brackets(df, entry)
        adjust_dimensions(df, entry)
        fix_shipping(df, entry)
        fix_price(df, entry)
        fix_boost_clocks(df, entry)
        fix_core_clocks(df, entry)
        fix_mem_clocks(df, entry)
        fix_review_numbers(df, entry)
