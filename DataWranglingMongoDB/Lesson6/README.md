

    %%writefile mapparser.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    Your task is to use the iterative parsing to process the map file and
    find out not only what tags are there, but also how many, to get the
    feeling on how much of which data you can expect to have in the map.
    The output should be a dictionary with the tag name as the key
    and number of times this tag can be encountered in the map as value.
    
    Note that your code will be tested with a different data file than the 'example.osm'
    """
    import xml.etree.ElementTree as ET
    import pprint
    
    def count_tags(filename):
        # YOUR CODE HERE
        """count tags in filename.
        
        Init 1 in dict if the key not exist, increment otherwise."""
        tags = {}
        for ev,elem in ET.iterparse(filename):
            tag = elem.tag
            if tag not in tags.keys():
                tags[tag] = 1
            else:
                tags[tag]+=1
        return tags
    
    def test():
    
        tags = count_tags('example.osm')
        pprint.pprint(tags)
        assert tags == {'bounds': 1,
                         'member': 3,
                         'nd': 4,
                         'node': 20,
                         'osm': 1,
                         'relation': 1,
                         'tag': 7,
                         'way': 1}
    
        
    
    if __name__ == "__main__":
        test()

    Writing mapparser.py



    %load ../Lesson3/blueprint_planning.py

We're going to upgrade the script in Lesson 3


    %%writefile xmliterparse.py
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

    Overwriting xmliterparse.py



    # %%writefile tags.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import xml.etree.ElementTree as ET
    import pprint
    import re
    """
    Your task is to explore the data a bit more.
    Before you process the data and add it into MongoDB, you should
    check the "k" value for each "<tag>" and see if they can be valid keys in MongoDB,
    as well as see if there are any other potential problems.
    
    We have provided you with 3 regular expressions to check for certain patterns
    in the tags. As we saw in the quiz earlier, we would like to change the data model
    and expand the "addr:street" type of keys to a dictionary like this:
    {"address": {"street": "Some value"}}
    So, we have to see if we have such tags, and if we have any tags with problematic characters.
    Please complete the function 'key_type'.
    """
    
    
    lower = re.compile(r'^([a-z]|_)*$')
    lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
    problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
    
    
    def key_type(element, keys):
        """ 
        Count the criteria in dictionary for the content of the tag.
        """
        if element.tag == "tag":
            if lower.search(element.attrib['k']):
                keys['lower'] +=1
            elif lower_colon.search(element.attrib['k']):
                keys['lower_colon']+=1
            elif problemchars.search(element.attrib['k']):
                keys['problemchars']+=1
            else:
                keys['other']+=1
            
        return keys
    
    
    
    def process_map(filename):
        keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
        for _, element in ET.iterparse(filename):
            keys = key_type(element, keys)
    
        return keys
    
    
    
    def test():
        # You can use another testfile 'map.osm' to look at your solution
        # Note that the assertions will be incorrect then.
        keys = process_map('example.osm')
        pprint.pprint(keys)
        assert keys == {'lower': 5, 'lower_colon': 0, 'other': 2, 'problemchars': 0}
    
    
    if __name__ == "__main__":
        test()

    {'lower': 7, 'lower_colon': 0, 'other': 0, 'problemchars': 0}



    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)

    <ipython-input-3-52ff1ec6b21f> in <module>()
         61 
         62 if __name__ == "__main__":
    ---> 63     test()
    

    <ipython-input-3-52ff1ec6b21f> in test()
         57     keys = process_map('example.osm')
         58     pprint.pprint(keys)
    ---> 59     assert keys == {'lower': 5, 'lower_colon': 0, 'other': 2, 'problemchars': 0}
         60 
         61 


    AssertionError: 



    %%writefile users.py
    
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import xml.etree.ElementTree as ET
    import pprint
    import re
    """
    Your task is to explore the data a bit more.
    The first task is a fun one - find out how many unique users
    have contributed to the map in this particular area!
    
    The function process_map should return a set of unique user IDs ("uid")
    """
    
    def get_user(element):
        return
    
    
    def process_map(filename):
        """
        Count the user id in the filename.
        """
        users = set()
        for _, element in ET.iterparse(filename):
            try:
                users.add(element.attrib['uid'])
            except KeyError:
                continue
    
        return users
    
    
    def test():
    
        users = process_map('example.osm')
        pprint.pprint(users)
        assert len(users) == 6
    
    
    
    if __name__ == "__main__":
        test()


    %%writefile audit.py
    """
    Your task in this exercise has two steps:
    
    - audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
        the unexpected street types to the appropriate ones in the expected list.
        You have to add mappings only for the actual problems you find in this OSMFILE,
        not a generalized solution, since that may and will depend on the particular area you are auditing.
    - write the update_name function, to actually fix the street name.
        The function takes a string with street name as an argument and should return the fixed name
        We have provided a simple test so that you see what exactly is expected
    """
    import xml.etree.cElementTree as ET
    from collections import defaultdict
    import re
    import pprint
    
    # OSMFILE = "example.osm"
    OSMFILE = "example_audit.osm"
    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
    
    
    expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
                "Trail", "Parkway", "Commons"]
    
    # UPDATE THIS VARIABLE
    #Mapping has to sort in length descending.
    mapping = { 
                "Ave":"Avenue",
                "St.": "Street",
                "Rd." : "Road",
                "N.":"North",
                "St" : "Street",
                }
    
    
    def audit_street_type(street_types, street_name):
        m = street_type_re.search(street_name)
        if m:
            street_type = m.group()
            if street_type not in expected:
                street_types[street_type].add(street_name)
    
    
    def is_street_name(elem):
        return (elem.attrib['k'] == "addr:street")
    
    
    def audit(osmfile):
        osm_file = open(osmfile, "r")
        street_types = defaultdict(set)
        for event, elem in ET.iterparse(osm_file, events=("start",)):
    
            if elem.tag == "node" or elem.tag == "way":
                for tag in elem.iter("tag"):
                    if is_street_name(tag):
                        audit_street_type(street_types, tag.attrib['v'])
    
        return street_types
    
    
    def update_name(name, mapping):
        """
        Fixed abreviate name so the name can be uniform.
        
        The reason why mapping in such particular order, is to prevent the shorter keys get first.
        """
        for key in mapping:
            if name.find(key) != -1:          
                name = name.replace(key,mapping[key])
                break
    
        return name
    
    
    def test():
        st_types = audit(OSMFILE)
        pprint.pprint(dict(st_types))
        assert len(st_types) == 3
        
    
        for st_type, ways in st_types.iteritems():
            for name in ways:
                better_name = update_name(name, mapping)
                print name, "=>", better_name
                if name == "West Lexington St.":
                    assert better_name == "West Lexington Street"
                if name == "Baldwin Rd.":
                    assert better_name == "Baldwin Road"
    
    
    if __name__ == '__main__':
        test()

    Overwriting audit.py



    # %%writefile data.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import xml.etree.ElementTree as ET
    import pprint
    import re
    import codecs
    import json
    """
    Your task is to wrangle the data and transform the shape of the data
    into the model we mentioned earlier. The output should be a list of dictionaries
    that look like this:
    
    {
    "id": "2406124091",
    "type: "node",
    "visible":"true",
    "created": {
              "version":"2",
              "changeset":"17206049",
              "timestamp":"2013-08-03T16:43:42Z",
              "user":"linuxUser16",
              "uid":"1219059"
            },
    "pos": [41.9757030, -87.6921867],
    "address": {
              "housenumber": "5157",
              "postcode": "60625",
              "street": "North Lincoln Ave"
            },
    "amenity": "restaurant",
    "cuisine": "mexican",
    "name": "La Cabana De Don Luis",
    "phone": "1 (773)-271-5176"
    }
    
    You have to complete the function 'shape_element'.
    We have provided a function that will parse the map file, and call the function with the element
    as an argument. You should return a dictionary, containing the shaped data for that element.
    We have also provided a way to save the data in a file, so that you could use
    mongoimport later on to import the shaped data into MongoDB. You could also do some cleaning
    before doing that, like in the previous exercise, but for this exercise you just have to
    shape the structure.
    
    In particular the following things should be done:
    - you should process only 2 types of top level tags: "node" and "way"
    - all attributes of "node" and "way" should be turned into regular key/value pairs, except:
        - attributes in the CREATED array should be added under a key "created"
        - attributes for latitude and longitude should be added to a "pos" array,
          for use in geospacial indexing. Make sure the values inside "pos" array are floats
          and not strings. 
    - if second level tag "k" value contains problematic characters, it should be ignored
    - if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
    - if second level tag "k" value does not start with "addr:", but contains ":", you can process it
      same as any other tag.
    - if there is a second ":" that separates the type/direction of a street,
      the tag should be ignored, for example:
    
    <tag k="addr:housenumber" v="5158"/>
    <tag k="addr:street" v="North Lincoln Avenue"/>
    <tag k="addr:street:name" v="Lincoln"/>
    <tag k="addr:street:prefix" v="North"/>
    <tag k="addr:street:type" v="Avenue"/>
    <tag k="amenity" v="pharmacy"/>
    
      should be turned into:
    
    {...
    "address": {
        "housenumber": 5158,
        "street": "North Lincoln Avenue"
    }
    "amenity": "pharmacy",
    ...
    }
    
    - for "way" specifically:
    
      <nd ref="305896090"/>
      <nd ref="1719825889"/>
    
    should be turned into
    "node_ref": ["305896090", "1719825889"]
    """
    
    
    lower = re.compile(r'^([a-z]|_)*$')
    lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
    problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
    addresschars = re.compile(r'addr:(\w+)')
    CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
    
    
    def shape_element(element):
        #node = defaultdict(set)
        node = {}
        if element.tag == "node" or element.tag == "way" :
            #create the dictionary based on exaclty the value in element attribute.
            node = {
                    'id':element.attrib['id'],
                    'type':element.tag,
                    'created':{
                                'changeset':element.attrib['changeset'],
                                'user':element.attrib['user'],
                                'version':element.attrib['version'],
                                'uid':element.attrib['uid'],
                                'timestamp':element.attrib['timestamp']
                                }
                    }
            #Some data just doesn't have pos/visible. So we need to do try-except for the missing keys.
            try:
                node['pos']=[float(element.attrib['lat']),float(element.attrib['lon'])]
                node['visible']=element.attrib['visible']
            except KeyError:
                pass
            
            #Iterate the content of the tag
            for stag in element.iter('tag'):
                #Init the dictionry
                if 'address' not in node.keys():
                    node['address'] = {}
                k = stag.attrib['k']
                v = stag.attrib['v']
                #Checking if indeed prefix with 'addr' and no ':' afterwards
                if k.startswith('addr:'):
                    if len(k.split(':')) == 2:
                        content = addresschars.search(k)
                        if content:
                            node['address'][content.group(1)] = v
                else:
                    node[k]=v
            #Special case when the tag == way,  scrap all the nd key
            if element.tag == "way":
                node['node_refs'] = []
                for nd in element.iter('nd'):
                    node['node_refs'].append(nd.attrib['ref'])
            return node
        else:
            return None
    
    
    def process_map(file_in, pretty = False):
        # You do not need to change this file
        file_out = "{0}.json".format(file_in)
        data = []
        with codecs.open(file_out, "w") as fo:
            for _, element in ET.iterparse(file_in):
                el = shape_element(element)
                if el:
                    data.append(el)
                    if pretty:
                        fo.write(json.dumps(el, indent=2)+"\n")
                    else:
                        fo.write(json.dumps(el) + "\n")
        return data
    
    def test():
    
        data = process_map('example2.osm')
        pprint.pprint(data[-1])
        assert data[0] == {
                            "id": "261114295", 
                            "visible": "true", 
                            "type": "node", 
                            "pos": [
                              41.9730791, 
                              -87.6866303
                            ], 
                            "created": {
                              "changeset": "11129782", 
                              "user": "bbmiller", 
                              "version": "7", 
                              "uid": "451048", 
                              "timestamp": "2012-03-28T18:31:23Z"
                            }
                          }
        assert data[-1]["address"] == {
                                        "street": "West Lexington St.", 
                                        "housenumber": "1412"
                                          }
        assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369", 
                                        "2199822370", "2199822284", "2199822281"]
    
    if __name__ == "__main__":
        test()

    {'address': {'housenumber': '1412', 'street': 'West Lexington St.'},
     'building': 'yes',
     'building:levels': '1',
     'chicago:building_id': '366409',
     'created': {'changeset': '15353317',
                 'timestamp': '2013-03-13T15:58:04Z',
                 'uid': '674454',
                 'user': 'chicago-buildings',
                 'version': '1'},
     'id': '209809850',
     'node_refs': ['2199822281',
                   '2199822390',
                   '2199822392',
                   '2199822369',
                   '2199822370',
                   '2199822284',
                   '2199822281'],
     'type': 'way'}


# Instructor Notes

If you are using the process_map() procedure above on your own computer to write
to a JSON file, make sure you call it with pretty = False parameter. Otherwise,
mongoimport might give you an error when you try to import the JSON file to
MongoDB.

The coordinate is https://www.openstreetmap.org/export#map=13/-6.2139/106.8359

I choose this map as this is my hometown.


    
