from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import os
import re


def adjust_col():
    """
    :return: just a temporary function I use to quickly clean up columns from any particular csv
    """
    df = pd.read_csv('../PROJECT - Newegg GPU/Saved Data/Nvidia/products_RTX 2080.csv')
    df['Dual-Link DVI Supported '] = 'NONE'
    df['DVI '] = 'NONE'

    df.to_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/products_RTX 2080.csv', index=False)


def recreate_data(cols):
    """
    :return: takes all the data from the  ../Saved Data/Nvidia folder and moves them to the ../Final Data/Nvidia/ folder
    with the selected columns of interest
    """
    entries = os.listdir('../PROJECT - Newegg GPU/Saved Data/Nvidia')

    for entry in entries:
        print(entry)
        df = pd.read_csv(f'../PROJECT - Newegg GPU/Saved Data/Nvidia/{entry}')
        df['base model name'] = df['model']
        # adjust_col(df, entry)
        df[cols].to_csv(f'../PROJECT - Newegg GPU/Final Data/Nvidia/{entry}', index=False)


def creat_master_df(cols):
    master_df = pd.DataFrame(columns=cols)

    for entry in entries:
        print(entry)
        df = pd.read_csv(f'../PROJECT - Newegg GPU/Final Data/Nvidia/{entry}')

        master_df = pd.concat([master_df, df], axis=0).reset_index(drop=True)

    master_df.to_csv(f'../PROJECT - Newegg GPU/Final Data/Nvidia/Master_Nvidia_GPU.csv', index=False)


def fix_nones():
    """
    :return: temporary function that I used to clean up none values for all the csv values in all columns in each csv
    mainly I replaced the nones with the mode values for each column
    """

    col = 'price'
    for entry in entries:
        print(entry)

        df = pd.read_csv(f'../PROJECT - Newegg GPU/Final Data/Nvidia/{entry}')
        df[col] = df[col].replace(0, None)
        df[col] = df[col].fillna(df[col].mode())

        # df[col] = df[col].apply(lambda x: df[col].mode())

        print(df[col].value_counts())

        df.to_csv(f'../PROJECT - Newegg GPU/Final Data/Nvidia/{entry}', index=False)


def fix_master():
    df = pd.read_csv(f'../PROJECT - Newegg GPU/Final Data/Nvidia/Master_Nvidia_GPU.csv')

    df.loc[df['Brand '] == 'NONE', 'Brand '] = df['product_name'].apply(lambda x: str(x).split()[0])
    print(df['Brand '].value_counts())

    df.to_csv('test.csv', index=False)


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    entries = os.listdir('../PROJECT - Newegg GPU/Final Data/Nvidia')

    cols = ['product_name', 'Brand ', 'CUDA Cores ', 'Chipset Manufacturer ', 'Cooler ', 'DVI ',
            'Date First Available ', 'DirectX ', 'DisplayPort ', 'Dual-Link DVI Supported ', 'GPU ', 'GPU Series ',
            'HDMI ', 'Interface ', 'Max Resolution ', 'Memory Interface ', 'Memory Size ', 'Memory Type ',
            'base model name', 'Model ', 'OpenGL ', 'SLI Support ', 'Slot Width ', 'Length (mm)', 'Height (mm)',
            'boost clock (MHz)', 'core clock (MHz)', 'memory clock (MHz)', 'number of reviews', 'price', 'rating'
            ]
    cols.sort()

    # recreate_data(cols)
    #fix_nones()

    #creat_master_df(cols)
    fix_master()
