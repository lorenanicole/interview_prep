# This is a solution for the Book Availability Update problem
# https://www.interviewquery.com/questions/book-availability-update

import argparse
from datetime import datetime
import pandas as pd
import pathlib

'''
Write a function update_availability to update the copies_available
value for a specific book_id in your dataframe and return the updated
dataframe.
'''

def update_availability(book_id: int, copies: int, df_books: pd.DataFrame) -> pd.DataFrame:
    df_books
    df_books.loc[df_books.index == book_id, "copies_available"] = copies
    return df_books

def load_data(filename: str, delimiter: str) -> pd.DataFrame:
    df = pd.read_csv(
        f'{pathlib.Path(__file__).parent.resolve()}/{file_name}',
        delimiter=delimiter
    )
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.set_index("book_id", inplace=True)
    return df

def select_title(df: pd.DataFrame, title: str) -> pd.DataFrame:
    title = title.strip()
    book = df[df["book_title"] == title]
    if book.empty:
        print(f'No book with the title {title} was found.')
        return
    print(f'{title} currently has {book["copies_available"].values[0]} copies available.')
    print(f'How many copies of {title} should there be?')
    qty = int(input())
    df = update_availability(
        book_id=book.index.values[0],
        copies=qty,
        df_books=df
    )
    print(f'The availability of {title} has been updated to {qty} copies.')
    return df

def today_date() -> str:
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Library Inventory"
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="book_inventory.csv",
        type=str,
        help="Filename of the book inventory csv file",
    )
    parser.add_argument(
        "-d",
        "--delimiter",
        default="comma",
        type=str,
        choices="comma, tab",
        help="Specify delimiter used in the book inventory filename, defaults to comma if not provided",
    )
    args = (
        parser.parse_args()
    )

    file_name = args.filename
    delimiter_map = {
        "comma": ",",
        "tab": "\t"
    }
    df = load_data(args.filename, f'\{delimiter_map[args.delimiter]}')
    # df.info()         # display stats
    # print(df.shape)   # get info on number rows and cols
    # print(df.columns)
    titles = df["book_title"].to_list()
    print(f'The following titles are available: \n\n{chr(10).join(titles)}.')   # chr(10) = \n delimiter
    title_input = input("Enter the title of the book you want to select: ")
    df = select_title(df, title_input)
    print("Exporting updated inventory to csv...")
    new_inventory_filename = f'book_inventory_{today_date()}'
    df.to_csv(f'{new_inventory_filename}.csv')
    print(f'Updated {new_inventory_filename} Export complete.')
