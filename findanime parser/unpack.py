import pickle
import pprint

with open('report.txt', mode='rb') as f:
    info = pickle.load(f)

pprint.pprint(info)