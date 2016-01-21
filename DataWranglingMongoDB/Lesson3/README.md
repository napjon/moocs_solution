

    # %%writefile blueprint_planning.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import xml.etree.cElementTree as ET
    from collections import defaultdict
    import re
    
    osm_file = open("chicago.osm", "r")
    
    #The regex takes only last word that possibly include .
    street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
    street_types = defaultdict(int)
    
    def audit_street_type(street_types, street_name):
        m = street_type_re.search(street_name)
        if m:
            street_type = m.group()
    
            street_types[street_type] += 1
    
    def print_sorted_dict(d):
        keys = d.keys()
        keys = sorted(keys, key=lambda s: s.lower())
        for k in keys:
            v = d[k]
            print "%s: %d" % (k, v) 
    
    def is_street_name(elem):
        return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")
    
    def audit():
        for event, elem in ET.iterparse(osm_file):
            if is_street_name(elem):
                #keep track by inserting the value to dict, and increment everytime found
                audit_street_type(street_types, elem.attrib['v'])
        #print all keys and value  of a dict sorted
        print_sorted_dict(street_types) 
    
    if __name__ == '__main__':
        audit()


    blueprint_planning.py


    # %%writefile validity.py
    
    """
    Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
    The following things should be done:
    - check if the field "productionStartYear" contains a year
    - check if the year is in range 1886-2014
    - convert the value of the field to be just a year (not full datetime)
    - the rest of the fields and values should stay the same
    - if the value of the field is a valid year in range, as described above,
      write that line to the output_good file
    - if the value of the field is not a valid year, 
      write that line to the output_bad file
    - discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
    - you should use the provided way of reading and writing data (DictReader and DictWriter)
      They will take care of dealing with the header.
    
    You can write helper functions for checking the data and writing the files, but we will call only the 
    'process_file' with 3 arguments (inputfile, output_good, output_bad).
    """
    import csv
    import pprint
    import re
    INPUT_FILE = 'autos.csv'
    OUTPUT_GOOD = 'autos-valid.csv'
    OUTPUT_BAD = 'FIXME-autos.csv'
    
    # def year_checked(str_year):
    
    
    def process_file(input_file, output_good, output_bad):
    
        with open(input_file, "r") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
            
            fg = open(output_good,'w')
            fb = open(output_bad, 'w')
            
            wg = csv.DictWriter(fg, delimiter=",", fieldnames= header)
            wb = csv.DictWriter(fb, delimiter=",", fieldnames= header)
            
            wg.writeheader()
            wb.writeheader()
     
            year_re = re.compile(r'^[0-9]{4}')
            for row in reader:
                if not row['URI'].find('dbpedia') == -1:
                    
                    str_year = year_re.search(row['productionStartYear'][:4])
                    if str_year and 1886<int(str_year.group())<2014:
                        row['productionStartYear'] = str_year.group()
                        wg.writerow(row)
                    else:
                        wb.writerow(row)
            fg.close()
            fb.close()
    
    
    def test():
    
        process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)
    
    test()
    if __name__ == "__main__":
        test()
        
        
        # This is just an example on how you can use csv.DictWriter
        # Remember that you have to output 2 files
    #     with open(output_good, "w") as g:
    #         writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
    #         writer.writeheader()
    #         for row in YOURDATA:
    #             writer.writerow(row)



    


    
    """
    Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
    The following things should be done:
    - check if the field "productionStartYear" contains a year
    - check if the year is in range 1886-2014
    - convert the value of the field to be just a year (not full datetime)
    - the rest of the fields and values should stay the same
    - if the value of the field is a valid year in range, as described above,
      write that line to the output_good file
    - if the value of the field is not a valid year, 
      write that line to the output_bad file
    - discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
    - you should use the provided way of reading and writing data (DictReader and DictWriter)
      They will take care of dealing with the header.
    
    You can write helper functions for checking the data and writing the files, but we will call only the 
    'process_file' with 3 arguments (inputfile, output_good, output_bad).
    """
    import csv
    import pprint
    import re
    INPUT_FILE = 'autos.csv'
    OUTPUT_GOOD = 'autos-valid.csv'
    OUTPUT_BAD = 'FIXME-autos.csv'
    
    # def year_checked(str_year):
    
    
    def process_file(input_file, output_good, output_bad):
    
        with open(input_file, "r") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
            
            fg = open(output_good,'w')
            fb = open(output_bad, 'w')
            
            wg = csv.DictWriter(fg, delimiter=",", fieldnames= header)
            wb = csv.DictWriter(fb, delimiter=",", fieldnames= header)
            
            wg.writeheader()
            wb.writeheader()
    #         print header
            #COMPLETE THIS FUNCTION
            year_re = re.compile('[0-9]')
            #print [e['URI'] for e in reader]
            for row in reader:
                if not row['URI'].find('dbpedia') == -1:
                    
                    str_year = row['productionStartYear'][:4]
                    if year_re.search(str_year) and 1886<type(int(str_year))<2014:
                        row['productionStartYear'] = str_year
                        wg.writerow(row)
                    else:
                        wb.writerow(row)
            fg.close()
            fb.close()
    
    
    def test():
    
        process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)
    
    
    if __name__ == "__main__":
        test()
        
        
        # This is just an example on how you can use csv.DictWriter
        # Remember that you have to output 2 files
    #     with open(output_good, "w") as g:
    #         writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
    #         writer.writeheader()
    #         for row in YOURDATA:
    #             writer.writerow(row)


    # %%writefile audit.py
    
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
    clean it up. In the first exercise we want you to audit the datatypes that can be found in some 
    particular fields in the dataset.
    The possible types of values can be:
    - 'NoneType' if the value is a string "NULL" or an empty string ""
    - 'list', if the value starts with "{"
    - 'int', if the value can be cast to int
    - 'float', if the value can be cast to float, but is not an int
    - 'str', for all other values
    
    The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
    that can be found in the field.
    All the data initially is a string, so you have to do some checks on the values first.
    
    """
    import codecs
    import csv
    import json
    import pprint
    
    CITIES = 'cities.csv'
    
    FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
              "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
              "areaLand", "areaMetro", "areaUrban"]
    
    def audit_file(filename, fields):
        fieldtypes = {}
        
        # YOUR CODE HERE
        reader  =csv.DictReader(open(filename))
        
        fieldtypes = dict(zip(fields,[[]]*len(fields)))
        list_reader = list(reader)
        #pprint.pprint(fieldtypes)
        #print list_reader[3]['areaMetro']
        #print ex_1['areaLand']
        #pprint.pprint(list_reader)
        #pprint.pprint(list_reader[4])
    #     for key in fieldtypes:
    #         possible_type = []
    #     print list_reader[35]['areaMetro']
    #     print list_reader[36]['areaMetro']
    #     print list_reader[37]['areaMetro']
    #     print list_reader[38]['areaMetro']
    #     print list_reader[39]['areaMetro']
    #     print list_reader[40]['areaMetro']
        
        for row in list_reader:
            #print row['areaMetro']
            for key in fieldtypes:
    #             print row[key]
                if row[key] == 'NULL' or row[key] == '':
                    fieldtypes[key].append(type(None))
                elif row[key].startswith('{'):
                    fieldtypes[key].append(list)
                    print 
                    if list in fieldtypes['areaMetro']:
                        print fieldtypes['areaMetro']
                    #print row[key], key
                else:
    #                 try:
    #                     tipe = type(eval(row[key]))
    #                     if tipe == int and key == 'areaLand':
    #                         print tipe
    #                     fieldtypes[key].append(tipe)
    #                 except NameError:
    #                     pass
    #                 except SyntaxError:
    #                     pass
        #fieldtypes = [fieldtypes[key].remove(str) for key in fieldtypes]
        #for key in fieldtypes:
        #    print set(fieldtypes[key])
                    try:
                        fieldtypes[key].append(float)
    #                     fval = float(row[key])
    #                     if (fval - int(fval) > 0.0):
    #                         fieldtypes[key].append(float)
    #                     else:
    #                         fieldtypes[key].append(int)
                    except ValueError:
                        pass
        pprint.pprint(set(fieldtypes['areaMetro']))
        for key in fieldtypes:
            fieldtypes[key] = set(fieldtypes[key])
        
        return fieldtypes
    
    
    def test():
        fieldtypes = audit_file(CITIES, FIELDS)
    
        #pprint.pprint(fieldtypes)
        print fieldtypes["areaMetro"]
        #print set(fieldtypes['areaMetro'])
        assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
        assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
        
    if __name__ == "__main__":
        test()



    !python audit.py


    %%writefile area.py
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
    
    Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
    you now know what has to be done.
    
    Finish the function fix_area(). It will receive a string as an input, and it has to return a float
    representing the value of the area or None.
    You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
    will not be taken into account.
    The rest of the code is just an example on how this function can be used.
    """
    import codecs
    import csv
    import json
    import pprint
    import pandas
    CITIES = 'cities.csv'
    
    
    def fix_area(area):
        if area == 'NULL':
            area = None
            return area
        area = area[1:-1]
        area = area.split('|')
        strarea = [e[:-4] for e in area]
        idxmax= strarea.index(max(strarea, key = len))
        area = float(area[idxmax])
        return area
    
    
    
    def process_file(filename):
        # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
        data = []
    
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
    
            #skipping the extra matadata
            for i in range(3):
                l = reader.next()
            #reader = list(reader)
            #print reader[9]["areaLand"]
            # processing file
            for line in reader:
                # calling your function to fix the area value
                if "areaLand" in line:
                    line["areaLand"] = fix_area(line["areaLand"])
                data.append(line)
    
        return data
    
    
    def test():
        data = process_file(CITIES)
    
        print "Printing three example results:"
        for n in range(8,9):
            pprint.pprint(data[n]["areaLand"])
            
        #print data[8]["areaLand"]
        
        assert data[8]["areaLand"] == 55166700.0
        assert data[3]["areaLand"] == None
    
    
    if __name__ == "__main__":
        test()

    Writing area.py



    %%writefile name.py
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
    
    In the previous quiz you recognized that the "name" value can be an array (or list in Python terms).
    It would make it easier to process and query the data later, if all values for the name 
    would be in a Python list, instead of being just a string separated with special characters, like now.
    
    Finish the function fix_name(). It will recieve a string as an input, and it has to return a list
    of all the names. If there is only one name, the list with have only one item in it, if the name is "NULL",
    the list should be empty.
    The rest of the code is just an example on how this function can be used
    """
    import codecs
    import csv
    import pprint
    
    CITIES = 'cities.csv'
    
    
    def fix_name(name):
    
        if name == 'NULL':
            return []
        elif name.startswith('{'):
            name = name[1:-1]
            return name.split('|')
        return [name]
    
    
    def process_file(filename):
        data = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            #skipping the extra matadata
            for i in range(3):
                l = reader.next()
            # processing file
            for line in reader:
                # calling your function to fix the area value
                if "name" in line:
                    line["name"] = fix_name(line["name"])
                data.append(line)
        return data
    
    
    def test():
        data = process_file(CITIES)
    
        print "Printing 20 results:"
        for n in range(3,4):
            pprint.pprint(data[n]["name"])
    
        assert data[14]["name"] == ['Negtemiut', 'Nightmute']
        assert data[3]["name"] == ['Kumhari']
    
    if __name__ == "__main__":
        test()

    Writing name.py



    %%writefile location.py
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
    
    If you look at the full city data, you will notice that there are couple of values that seem to provide
    the same information in different formats: "point" seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long".
    However we do not know if that is the case and should check if they are equivalent.
    
    Finish the function check_loc(). It will recieve 3 strings, first will be the combined value of "point" and then the
    "wgs84_pos#" values separately. You have to extract the lat and long values from the "point" and compare
    to the "wgs84_pos# values and return True or False.
    
    Note that you do not have to fix the values, just determine if they are consistent. To fix them in this case
    you would need more information. Feel free to discuss possible strategies for fixing this on the discussion forum.
    
    The rest of the code is just an example on how this function can be used.
    Changes to "process_file" function will not be take into account.
    """
    import csv
    import pprint
    
    CITIES = 'cities.csv'
    
    
    def check_loc(point, lat, longi):
        # YOUR CODE HERE
        points = point.split(' ')
        return points[0] == lat and points[1] == longi
    
    
    def process_file(filename):
        data = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            #skipping the extra matadata
            for i in range(3):
                l = reader.next()
            # processing file
            for line in reader:
                # calling your function to check the location
                result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
                if not result:
                    print "{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
                data.append(line)
    
        return data
    
    
    def test():
        assert check_loc("33.08 75.28", "33.08", "75.28") == True
        assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") == False
    
    if __name__ == "__main__":
        test()

    Writing location.py



    
