#!/usr/bin/env python
import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("chicago.osm", "r")

street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
street_types = defaultdict(set)#This for convenient method no need to check whether keys in or not, 
                                #if it doesn't, simply create new key 
expected = ['Street','Avenue']
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
        #street_types[street_type] += 1

def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v) 

def is_street_name(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")

def audit():
    #event=start, represent that we want to emit what's in the start tag
    for event, elem in ET.iterparse(osm_file,events=('start',):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v'])   
    print_sorted_dict(street_types) 

if __name__ == '__main__':
    audit()