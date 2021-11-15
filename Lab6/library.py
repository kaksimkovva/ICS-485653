from typing import Union

import pandas as pd

# Year format for DataFrame
pd.options.display.float_format = '{:.0f}'.format


class Library:
    __data = pd.DataFrame()

    def add_book(self, author: str, year: int, genre: str):
        data_dictionary = {"Author": author, "Year": year, "Genre": genre}
        self.__data = self.__data.append(data_dictionary, ignore_index=True)
        print(self.__data)

    def delete_book_by_id(self, book_id: int):
        if len(self.__data) == 0:
            print("There are no books in library!")
        else:
            self.__data = self.__data.drop(book_id)
            print(self.__data)

    def find_book_by_id(self, book_id: int):
        all_indexes = self.__data.head()
        for i in all_indexes.index:
            if all_indexes.index[i] == book_id:
                print(pd.DataFrame(self.__data.iloc[book_id]))

    def find_book_by_field(self, field: str, field_value: Union[str, int]):
        print(self.__data[self.__data[field] == field_value])


library = Library()

print("\nAdd first book.\n")
library.add_book("Yasha", 1920, "Fantasy")

print("\nAdd second book.\n")
library.add_book("Lavash", 1921, "Fantasy")

print("\nFound book with id 1.\n")
library.find_book_by_id(1)

print("\nFound book with author name.\n")
library.find_book_by_field("Author", "Lavash")

print("\nDelete book with id 0.\n")
library.delete_book_by_id(0)