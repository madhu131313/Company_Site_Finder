from difflib import SequenceMatcher
import json

# Ratcliff/Obershelp Algo for Similarity Score`
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def get_config():
    with open('config.json') as json_data_file:
        return json.load(json_data_file)
