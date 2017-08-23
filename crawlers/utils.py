#!/usr/bin/python
# -*- coding: utf-8 -*-
from difflib import SequenceMatcher
import json

def similar(a, b):
    """Ratcliff/Obershelp Algo for Similarity Score"""
    return SequenceMatcher(None, a, b).ratio()


def get_config():
    """returns configuration data"""
    with open('config.json') as json_data_file:
        return json.load(json_data_file)



			
