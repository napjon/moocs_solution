

    # %%writefile intromongo.py
    
    """
    Your task is to sucessfully run the exercise to see how pymongo works
    and how easy it is to start using it.
    You don't actually have to change anything in this exercise,
    but you can change the city name in the add_city function if you like.
    
    Your code will be run against a MongoDB instance that we have provided.
    If you want to run this code locally on your machine,
    you have to install MongoDB (see Instructor comments for link to installation information)
    and uncomment the get_db function.
    """
    
    
    def get_db():
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        # 'examples' here is the database name. It will be created if it does not exist.
        db = client.examples
        return db
    
    
    def add_city(db):
        db.cities.insert({"name" : "Chicago"})
        
    def get_city(db):
        return db.cities.find_one()
    
    
    if __name__ == "__main__":
    
        db = get_db() # uncomment this line if you want to run this locally
        add_city(db)
        print get_city(db)


    ---------------------------------------------------------------------------
    ConnectionFailure                         Traceback (most recent call last)

    <ipython-input-4-bee3ba457160> in <module>()
         31 if __name__ == "__main__":
         32 
    ---> 33     db = get_db() # uncomment this line if you want to run this locally
         34     add_city(db)
         35     print get_city(db)


    <ipython-input-4-bee3ba457160> in get_db()
         16 def get_db():
         17     from pymongo import MongoClient
    ---> 18     client = MongoClient('localhost:27017')
         19     # 'examples' here is the database name. It will be created if it does not exist.
         20     db = client.examples


    /Users/jon/anaconda/lib/python2.7/site-packages/pymongo/mongo_client.pyc in __init__(self, host, port, max_pool_size, document_class, tz_aware, _connect, **kwargs)
        367             except AutoReconnect, e:
        368                 # ConnectionFailure makes more sense here than AutoReconnect
    --> 369                 raise ConnectionFailure(str(e))
        370 
        371         if username:


    ConnectionFailure: [Errno 61] Connection refused



    %%writefile find_porsche.py
    
    #!/usr/bin/env python
    """
    Your task is to complete the 'porsche_query' function and in particular the query
    to find all autos where the manufacturer field matches "Porsche".
    Please modify only 'porsche_query' function, as only that will be taken into account.
    
    Your code will be run against a MongoDB instance that we have provided.
    If you want to run this code locally on your machine,
    you have to install MongoDB and download and insert the dataset.
    For instructions related to MongoDB setup and datasets please see Course Materials at
    the following link:
    https://www.udacity.com/wiki/ud032
    """
    
    
    def get_db(db_name):
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client[db_name]
        return db
    
    
    def porsche_query():
        # Please fill in the query to find all autos manuafactured by Porsche
        query = {'manufacturer':'Porsche'}
        #projection = {'id':0, 'name':1} id default specified, 0 will disable it.
        #feeding it into find method will get only the name of query we specify
        return query
    
    
    def find_porsche(db, query):
        return db.autos.find(query)
    
    
    if __name__ == "__main__":
    
        db = get_db('examples')
        query = porsche_query()
        p = find_porsche(db, query)
        import %pprint

    Overwriting find_porsche.py



    %%writefile insert.py
    from autos import process_file
    
    
    def insert_autos(infile, db):
        autos = process_file(infile)
    
        # Your code here. Insert the data in one command
        # autos will be a list of dictionaries, as in the example in the previous video
        # You have to insert data in a collection 'autos'
        [db.autos.insert(e) for e in autos]
    
      
    if __name__ == "__main__":
        
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017")
        db = client.examples
    
        insert_autos('autos-small.csv', db)
        print db.autos.find_one()

    Writing insert.py



    %%writefile autos.py
    
    from pymongo import MongoClient
    import csv
    import json
    import io
    import re
    import pprint
    
    
    field_map = {
        "name" : "name",
        "bodyStyle_label" : "bodyStyle",
        "assembly_label" : "assembly",
        "class_label" : "class",
        "designer_label" : "designer",
        "engine_label" : "engine",
        "length" : "length",
        "height" : "height",
        "width" : "width",
        "weight" : "weight",
        "wheelbase" : "wheelbase",
        "layout_label" : "layout",
        "manufacturer_label" : "manufacturer",
        "modelEndYear" : "modelEndYear",
        "modelStartYear" : "modelStartYear",
        "predecessorLabel" : "predecessorLabel",
        "productionStartYear" : "productionStartYear",
        "productionEndYear" : "productionEndYear",
        "transmission" : "transmission"
    }
    fields = field_map.keys()
    
    
    def skip_lines(input_file, skip):
        for i in range(0, skip):
            next(input_file)
    
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def strip_automobile(v):
        return re.sub(r"\s*\(automobile\)\s*", " ", v)
    
    def strip_city(v):
        return re.sub(r"\s*\(city\)\s*", " ", v)
    
    def parse_array(v):
        if (v[0] == "{") and (v[-1] == "}"):
            v = v.lstrip("{")
            v = v.rstrip("}")
            v_array = v.split("|")
            v_array = [i.strip() for i in v_array]
            return v_array
        return v
    
    def mm_to_meters(v):
        if v < 0.01:
            return v * 1000
        return v
    
    def clean_dimension(d, field, v):
        if is_number(v):
            if field == "weight":
                d[field] = float(v) / 1000.0
            else:
                d[field] = mm_to_meters(float(v))
        
    def clean_year(d, field, v):
        d[field] = v[0:4]
    
    def parse_array2(v):
        if (v[0] == "{") and (v[-1] == "}"):
            v = v.lstrip("{")
            v = v.rstrip("}")
            v_array = v.split("|")
            v_array = [i.strip() for i in v_array]
            return (True, v_array)
        return (False, v)
    
    def ensure_not_array(v):
        (is_array, v) = parse_array(v)
        if is_array:
            return v[0]
        return v
    
    def ensure_array(v):
        (is_array, v) = parse_array2(v)
        if is_array:
            return v
        return [v]
    
    def ensure_float(v):
        if is_number(v):
            return float(v)
    
    def ensure_int(v):
        if is_number(v):
            return int(v)
    
    def ensure_year_array(val):
        #print "val:", val
        vals = ensure_array(val)
        year_vals = []
        for v in vals:
            v = v[0:4]
            v = int(v)
            if v:
                year_vals.append(v)
        return year_vals
    
    def empty_val(val):
        val = val.strip()
        return (val == "NULL") or (val == "")
    
    def years(row, start_field, end_field):
        start_val = row[start_field]
        end_val = row[end_field]
    
        if empty_val(start_val) or empty_val(end_val):
            return []
    
        start_years = ensure_year_array(start_val)
        if start_years:
            start_years = sorted(start_years)
        end_years = ensure_year_array(end_val)
        if end_years:
            end_years = sorted(end_years)
        all_years = []
        if start_years and end_years:
            #print start_years
            #print end_years
            for i in range(0, min(len(start_years), len(end_years))):
                for y in range(start_years[i], end_years[i]+1):
                    all_years.append(y)
        return all_years
    
    
    def process_file(input_file):
        input_data = csv.DictReader(open(input_file))
        autos = []
        skip_lines(input_data, 3)
        for row in input_data:
            auto = {}
            model_years = {}
            production_years = {}
            dimensions = {}
            for field, val in row.iteritems():
                if field not in fields or empty_val(val):
                    continue
                if field in ["bodyStyle_label", "class_label", "layout_label"]:
                    val = val.lower()
                val = strip_automobile(val)
                val = strip_city(val)
                val = val.strip()
                val = parse_array(val)
                if field in ["length", "width", "height", "weight", "wheelbase"]:
                    clean_dimension(dimensions, field_map[field], val)
                elif field in ["modelStartYear", "modelEndYear"]:
                    clean_year(model_years, field_map[field], val)
                elif field in ["productionStartYear", "productionEndYear"]:
                    clean_year(production_years, field_map[field], val)
                else:
                    auto[field_map[field]] = val
            if dimensions:
                auto['dimensions'] = dimensions
            auto['modelYears'] = years(row, 'modelStartYear', 'modelEndYear')
            auto['productionYears'] = years(row, 'productionStartYear', 'productionEndYear')
            autos.append(auto)
        return autos


    Writing autos.py



    %%writefile find_cities.py
    #!/usr/bin/env python
    """ Your task is to write a query that will return all cities
    that are founded in 21st century.
    Please modify only 'range_query' function, as only that will be taken into account.
    
    Your code will be run against a MongoDB instance that we have provided.
    If you want to run this code locally on your machine,
    you have to install MongoDB, download and insert the dataset.
    For instructions related to MongoDB setup and datasets please see Course Materials.
    """
    from datetime import datetime
        
    def get_db():
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client.examples
        return db
    
    
    def range_query():
        # You can use datetime(year, month, day) to specify date in the query
        query = {'foundingDate': {'$gte': datetime(2001,1,1)}}
        return query
    
    
    if __name__ == "__main__":
    
        db = get_db()
        query = range_query()
        cities = db.cities.find(query)
    
        print "Found cities:", cities.count()
        import pprint
        pprint.pprint(cities[0])


    Writing find_cities.py



    %%writefile find_cars.py
    
    #Using $in Operator
    
    #!/usr/bin/env python
    """ Your task is to write a query that will return all cars manufactured by "Ford Motor Company"
    that are assembled in Germany, United Kingdom, or Japan.
    Please modify only 'in_query' function, as only that will be taken into account.
    
    Your code will be run against a MongoDB instance that we have provided.
    If you want to run this code locally on your machine,
    you have to install MongoDB, download and insert the dataset.
    For instructions related to MongoDB setup and datasets please see Course Materials.
    """
    
    def get_db():
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client.examples
        return db
    
    
    def in_query():
        # Write the query
        query = {'manufacturer':'Ford Motor Company',\
                 'assembly':{'$in':['Germany',\
                                    'United Kingdom',\
                                    'Japan']}}
        
        return query
    
    
    if __name__ == "__main__":
    
        db = get_db()
        query = in_query()
        autos = db.autos.find(query, {"name":1, "manufacturer":1, "assembly": 1, "_id":0})
    
        print "Found autos:", autos.count()
        import pprint
        for a in autos:
            pprint.pprint(a)


    Writing find_cars.py



    %%writefile dot_find.py
    
    #!/usr/bin/env python
    """ Your task is to write a query that will return all cars with width dimension greater than 2.5
    Please modify only 'dot_query' function, as only that will be taken into account.
    
    Your code will be run against a MongoDB instance that we have provided.
    If you want to run this code locally on your machine,
    you have to install MongoDB, download and insert the dataset.
    For instructions related to MongoDB setup and datasets please see Course Materials.
    """
    
    
    def get_db():
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client.examples
        return db
    
    
    def dot_query():
        query = {'dimensions.width' : {'$gt': 2.5}}
        return query
    
    
    if __name__ == "__main__":
    
        db = get_db()
        query = dot_query()
        cars = db.cars.find(query)
    
        print "Found cars:", cars.count()
        import pprint
        pprint.pprint(cars[0])


    Writing dot_find.py



    %%writefile processing.py
    
    ##Preparing the data from csv
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    In this problem set you work with another type of infobox data, audit it, clean it, 
    come up with a data model, insert it into a MongoDB and then run some queries against your database.
    The set contains data about Arachnid class.
    Your task in this exercise is to parse the file, process only the fields that are listed in the
    FIELDS dictionary as keys, and return a dictionary of cleaned values. 
    
    The following things should be done:
    - keys of the dictionary changed according to the mapping in FIELDS dictionary
    - trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
    - if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
    - if a value of a field is "NULL", convert it to None
    - if there is a value in 'synonym', it should be converted to an array (list)
      by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
      eg removing "*" prefixes etc
    - strip leading and ending whitespace from all fields, if there is any
    - the output structure should be as follows:
    """
    TRUE_SAMPLE = { 'label': 'Argiope',
      'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
      'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
      'name': 'Argiope',
      'synonym': ["One", "Two"],
      'classification': {
                        'family': 'Orb-weaver spider',
                        'class': 'Arachnid',
                        'phylum': 'Arthropod',
                        'order': 'Spider',
                        'kingdom': 'Animal',
                        'genus': None
                        }
    }
    
    import codecs
    import csv
    import json
    import pprint
    import re
    import pandas
    DATAFILE = 'arachnid.csv'
    FIELDS ={'rdf-schema#label': 'label',
             'URI': 'uri',
             'rdf-schema#comment': 'description',
             'synonym': 'synonym',
             'name': 'name',
             'family_label': 'family',
             'class_label': 'class',
             'phylum_label': 'phylum',
             'order_label': 'order',
             'kingdom_label': 'kingdom',
             'genus_label': 'genus'}
    
    
    def process_file(filename, fields):
    
        process_fields = fields.keys()
    
        data = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            reader = list(reader)[3:]
            for row  in reader:
                d = {'classification' : {}}
                for key in process_fields:
                    k = fields[key]
                    v = row[key]
                    #print k
                    if v == 'NULL':
                        v = None
                    if key == k+'_label':
                        d['classification'][k] = v
                    else:
                        d[k] = v
                    if k == 'name' and not d[k]:
                        d[k] = d['label']
                    if key == 'synonym' and v:
                        d[k] = parse_array(d[k])
                    if k == 'label' and d[k]:
                        d[k] =d[k].replace(' (spider)','')
                data.append(d)
        return data
    
    
    def parse_array(v):
        if (v[0] == "{") and (v[-1] == "}"):
            v = v.lstrip("{")
            v = v.rstrip("}")
            v_array = v.split("|")
            v_array = [i.strip() for i in v_array]
            return v_array
        return [v]
    
    
    def test():
        data = process_file(DATAFILE, FIELDS)
        #pprint.pprint(TRUE_SAMPLE)
        pprint.pprint(data[48])
        assert data[0] == {
                            "synonym": None, 
                            "name": "Argiope", 
                            "classification": {
                                "kingdom": "Animal", 
                                "family": "Orb-weaver spider", 
                                "order": "Spider", 
                                "phylum": "Arthropod", 
                                "genus": None, 
                                "class": "Arachnid"
                            }, 
                            "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
                            "label": "Argiope", 
                            "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
                        }
    
    
    if __name__ == "__main__":
        test()

    Writing processing.py



    %%writefile dbinsert.py
    
    #Insert data from JSON to MongoDB. JSON may python dictionary we have earlier
    
    
    import json
    
    def insert_data(data, db):
    
        # Your code here. Insert the data into a collection 'arachnid'
        db.arachnid.insert(data)
        
    
    
    if __name__ == "__main__":
        
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017")
        db = client.examples
    
        with open('arachnid.json') as f:
            data = json.loads(f.read())
            insert_data(data, db)
            print db.arachnid.find_one()

    Writing dbinsert.py



    %%writefile update.py
    
    #Problem Set, Updating the database that already added, with column  in csv earlier
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    In this problem set you work with another type of infobox data, audit it, clean it, 
    come up with a data model, insert it into a MongoDB and then run some queries against your database.
    The set contains data about Arachnid class.
    
    The data is already in the database. But you have been given a task to also include 'binomialAuthority'
    information in the data, so you have to go through the data and update the existing entries.
    
    The following things should be done in the function add_field:
    - process the csv file and extract 2 fields - 'rdf-schema#label' and 'binomialAuthority_label'
    - clean up the 'rdf-schema#label' same way as in the first exercise - removing redundant "(spider)" suffixes
    - return a dictionary, with 'label' being the key, and 'binomialAuthority_label' the value
    - if 'binomialAuthority_label' is "NULL", skip the item
    
    The following should be done in the function update_db:
    - query the database by using the field 'label'
    - update the data, by adding a new item under 'classification' with a key 'binomialAuthority'
    
    
    The resulting data should look like this:
    - the output structure should be as follows:
    { 'label': 'Argiope',
      'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
      'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
      'name': 'Argiope',
      'synonym': ["One", "Two"],
      'classification': {
                        'binomialAuthority': None,
                        'family': 'Orb-weaver spider',
                        'class': 'Arachnid',
                        'phylum': 'Arthropod',
                        'order': 'Spider',
                        'kingdom': 'Animal',
                        'genus': None
                        }
    }
    """
    import codecs
    import csv
    import json
    import pprint
    
    DATAFILE = 'arachnid.csv'
    FIELDS ={'rdf-schema#label': 'label',
             'binomialAuthority_label': 'binomialAuthority'}
    
    
    def add_field(filename, fields):
    
        process_fields = fields.keys()
        data = {}
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            reader = list(reader)[3:]
            for row in reader:
                k = row['rdf-schema#label']
                v = row['binomialAuthority_label']
                if v == 'NULL':
                        continue
                k = k.replace(' (spider)','')
                data[k] = v
                       
        return data
    
    
    def update_db(data, db):
        for key in data:
            db.arachnid.update({'label': key},
                                {'$set' : {'classification.binomialAuthority':data[key] }})
    
    
    
    def test():
        # Please change only the add_field and update_db functions!
        # Changes done to this function will not be taken into account
        # when doing a Test Run or Submit, they are just for your own reference
        # and as an example for running this code locally!
        
        data = add_field(DATAFILE, FIELDS)
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017")
        db = client.examples
    
        update_db(data, db)
    
        updated = db.arachnid.find_one({'label': 'Opisthoncana'})
        assert updated['classification']['binomialAuthority'] == 'Embrik Strand'
        pprint.pprint(data)
    
    
    
    if __name__ == "__main__":
        test()

    Writing update.py



    
