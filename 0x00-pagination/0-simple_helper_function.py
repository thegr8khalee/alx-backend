#!/usr/bin/env python3
"""
Main file
"""

def index_range(page, page_size):
    """_summary_

    Args:
        page (_type_): _description_
        page_size (_type_): _description_
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
