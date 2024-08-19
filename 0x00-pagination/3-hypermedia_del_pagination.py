#!/usr/bin/env python3
'''
a function named index_range that takes two integer
arguments page and page_size.
'''
from typing import Tuple, List, Dict
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        Initializing function
        '''
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        method with two integer arguments: index with a None default
        value and page_size with default value of 10.
        '''
        assert type(index) == int and index < 1000
        indexed_data = self.indexed_dataset()
        end = index + page_size
        if end > len(indexed_data):
            end = len(indexed_data)
        next_index = end
        data = []
        for i in range(index, end):
            if i not in indexed_data:
                next_index += 1
                j = end
                while not indexed_data[j]:
                    j += 1
                data.append(indexed_data[j])
            else:
                data.append(indexed_data[i])
        response = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
        return response
