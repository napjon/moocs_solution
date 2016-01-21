
###### Python Wrangling with MongoDB


    #%%writefile csv_to_dict.py
    
    # Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
    # split each line on "," and then for each line, create a dictionary
    # where the key is the header title of the field, and the value is the value of that field in the row.
    # The function parse_file should return a list of dictionaries,
    # each data line in the file being a single list entry.
    # Field names and values should not contain extra whitespace, like spaces or newline characters.
    # You can use the Python string method strip() to remove the extra whitespace.
    # You have to parse only the first 10 data lines in this exercise,
    # so the returned list should have 10 entries!
    import os
    import pprint
    
    DATADIR = ""
    DATAFILE = "beatles-diskography.csv"
    
    
    def parse_file(datafile):
        with open(datafile, "r") as f:
            items = [line.strip().split(',') for line in f]
            key_list = items[0]
            data = [dict(zip(key_list,items[i])) for i in range(1,11)]
        return data
    
    
    def test():
        # a simple test of your implemetation
        datafile = os.path.join(DATADIR, DATAFILE)
        d = parse_file(datafile)
        pprint.pprint(d)
        firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
        tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    
        assert d[0] == firstline
        assert d[9] == tenthline
    
        
    test()



    # %%writefile parse_excel.py
    
    import xlrd
    
    datafile = "2013_ERCOT_Hourly_Load_Data.xls"
    import pprint
    
    def parse_file(datafile):
        workbook = xlrd.open_workbook(datafile)
        sheet = workbook.sheet_by_index(0)
    
        data = [[sheet.cell_value(r, col) 
                    for col in range(sheet.ncols)] 
                        for r in range(sheet.nrows)]
    
        print "\nList Comprehension"
        print "data[3][2]:",
        print data[3][2]
    
        print "\nCells in a nested loop:"    
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                if row == 50:
                    print sheet.cell_value(row, col),
    
    
        ### other useful methods:
        print "\nROWS, COLUMNS, and CELLS:"
        print "Number of rows in the sheet:", 
        print sheet.nrows
        print "Type of data in cell (row 3, col 2):", 
        print sheet.cell_type(3, 2)
        print "Value in cell (row 3, col 2):", 
        print sheet.cell_value(3, 2)
        print "Get a slice of values in column 3, from rows 1-3:"
        print sheet.col_values(3, start_rowx=1, end_rowx=4)
    
        print "\nDATES:"
        print "Type of data in cell (row 1, col 0):", 
        print sheet.cell_type(1, 0)
        exceltime = sheet.cell_value(1, 0)
        print "Time in Excel format:",
        print exceltime
        print "Convert time to a Python datetime tuple, from the Excel float:",
        print xlrd.xldate_as_tuple(exceltime, 0)
        
        #pprint.pprint(data[1:10])
        task = """
        Your task is as follows:
        - read the provided Excel file
        - find and return the min, max and average values for the COAST region
        - find and return the time value for the min and max entries
        - the time values should be returned as Python tuples
    
        Please see the test function for the expected return format
        """
        list_coast = sheet.col_values(1,start_rowx=1)
        max_val =  max(list_coast)
        min_val = min(list_coast)
        d_data = {
                'maxtime': xlrd.xldate_as_tuple(data[list_coast.index(max_val)+1][0],0),
                'maxvalue':max_val,
                'mintime': xlrd.xldate_as_tuple(data[list_coast.index(min_val)+1][0],0),
                'minvalue': min_val,
                'avgcoast': sum(list_coast)/len(list_coast)
        }
        pprint.pprint(d_data)
        return data
    
    
    
    if __name__ == "__main__":
        data = parse_file(datafile)
        

    
    List Comprehension
    data[3][2]: 1036.088697
    
    Cells in a nested loop:
    41277.0833333 9238.73731 1438.20528 1565.442856 916.708348 14010.903488 3027.98334 6165.211119 1157.741663 37520.933404 
    ROWS, COLUMNS, and CELLS:
    Number of rows in the sheet: 7296
    Type of data in cell (row 3, col 2): 2
    Value in cell (row 3, col 2): 1036.088697
    Get a slice of values in column 3, from rows 1-3:
    [1411.7505669999982, 1403.4722870000019, 1395.053150000001]
    
    DATES:
    Type of data in cell (row 1, col 0): 3
    Time in Excel format: 41275.0416667
    Convert time to a Python datetime tuple, from the Excel float: (2013, 1, 1, 1, 0, 0)
    {'avgcoast': 10976.933460679751,
     'maxtime': (2013, 8, 13, 17, 0, 0),
     'maxvalue': 18779.025510000003,
     'mintime': (2013, 2, 3, 4, 0, 0),
     'minvalue': 6602.113898999982}



    # %%writefile ws_json_music_brain.py
    # To experiment with this code freely you will have to run this code locally.
    # We have provided an example json output here for you to look at,
    # but you will not be able to run any queries through our UI.
    import json
    import requests
    import pprint
    
    BASE_URL = "http://musicbrainz.org/ws/2/"
    ARTIST_URL = BASE_URL + "artist/"
    
    query_type = {  "simple": {},
                    "atr": {"inc": "aliases+tags+ratings"},
                    "aliases": {"inc": "aliases"},
                    "releases": {"inc": "releases"}}
    
    
    def query_site(url, params, uid="", fmt="json"):
        params["fmt"] = fmt
        r = requests.get(url + uid, params=params)
        print "requesting", r.url
    
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()
    
    
    def query_by_name(url, params, name):
        params["query"] = "artist:" + name
        return query_site(url, params)
    
    
    def pretty_print(data, indent=4):
        if type(data) == dict:
            print json.dumps(data, indent=indent, sort_keys=True)
        else:
            print data
    
    
    def main():
        results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
        aliases = results["artists"][0]["aliases"]
        for a in aliases:
            if a["locale"] == "es":
                pretty_print(a["name"])
    #     pretty_print(results['artists'][0]['aliases'])
    #     print(len(results['artists']))
    #     for e in results['artists']:
    #         try:
    #             pprint.pprint(e['aliases'])
    #         except KeyError:
    #             continue
    #     try:
    #         [e['aliases'] for e in results['artists']]
    #     except KeyError:
    #         continue
        artist_id = results["artists"][1]["id"]
    #     print len(results['artists'][1])
    #     print "\nARTIST:"
    #     pretty_print(results["artist"][1])
    
        artist_data = query_site(ARTIST_URL, query_type["aliases"], artist_id)
        pretty_print(artist_data,indent=10)
    #     releases = artist_data["aliases"]
    #     pretty_print(artist_data)
    #     print "\nONE RELEASE:"
    #     pretty_print(releases[0], indent=2)
    #     release_titles = [r["title"] for r in releases]
    
    #     print "\nALL TITLES:"
    #     for t in release_titles:
    #         print t
    
    #     q1 = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
    #     q1_count = 0
    #     for artist in q1["artists"]:
    #         if artist["score"] == "100":
    #             q1_count += 1
    #     print "Q1: Number of bands 'FIRST AID KIT' that had score == 100"
    #     print q1_count
    
    
    if __name__ == '__main__':
        main()



    %%writefile problem11.py
    
    #!/usr/bin/env python
    """
    Your task is to process the supplied file and use the csv module to extract data from it.
    The data comes from NREL (National Renewable Energy Laboratory) website. Each file
    contains information from one meteorological station, in particular - about amount of
    solar and wind energy for each hour of day.
    
    Note that the first line of the datafile is neither data entry, nor header. It is a line
    describing the data source. You should extract the name of the station from it.
    
    The data should be returned as a list of lists (not dictionaries).
    You can use the csv modules "reader" method to get data in such format.
    Another useful method is next() - to get the next line from the iterator.
    You should only change the parse_file function.
    """
    import csv
    import os
    import pandas
    
    DATADIR = ""
    DATAFILE = "745090.csv"
    
    
    def parse_file(datafile):
        name = ""
        data = []
        with open(datafile,'rb') as f:
            items = list(csv.reader(f))
            name = items[0][1]
            data = items[2:]
        # Do not change the line below
        return (name, data)
    
    def parse_file2(datafile):
        name = ""
        data = []
        with open(datafile,'rb') as f:
            r = csv.reader(f)
            name = r.next()[1]
            header = r.next()
            data = [row for row in r]
    
        return (name, data)
    
    def test():
        datafile = os.path.join(DATADIR, DATAFILE)
        name, data = parse_file(datafile)
        #print name
        assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
        assert data[0][1] == "01:00"
        assert data[2][0] == "01/01/2005"
        assert data[2][5] == "2"
    
    
    if __name__ == "__main__":
        test()


    %%writefile problem12.py
    # -*- coding: utf-8 -*-
    # Find the time and value of max load for each of the regions
    # COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
    # and write the result out in a csv file, using pipe character | as the delimiter.
    # An example output can be seen in the "example.csv" file.
    
    import xlrd
    import os
    import csv
    from zipfile import ZipFile
    import pandas
    datafile = "2013_ERCOT_Hourly_Load_Data.xls"
    outfile = "2013_Max_Loads.csv"
    
    
    def open_zip(datafile):
        with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
            myzip.extractall()
    
    
    def parse_file(datafile):
        workbook = xlrd.open_workbook(datafile)
        sheet = workbook.sheet_by_index(0)
        data = []
        # YOUR CODE HERE
        # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
        # Excel date to Python tuple of (year, month, day, hour, minute, second)
        xldata = [[str(sheet.cell_value(r,c)) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        headers = ["Station",'Year','Month','Day','Hour','Max Load']
        data.append(headers)
        for i in range(1,9):
            list_reg = sheet.col_values(i,start_rowx=1)
            max_val =  max(list_reg)
            
            exceltime = xldata[list_reg.index(max_val)+1][0]
            #print exceltime
            max_time = xlrd.xldate_as_tuple(float(exceltime),0)
            y,m,d,h,v1,v2 = max_time
            data.append([str(xldata[0][i]),str(y),str(m),str(d),str(h),repr(max_val)])
            
        return data
    
    def save_file(data, filename):
        # YOUR CODE HERE
        with open(filename, 'wb') as f:
            writercsv = csv.writer(f,delimiter='|')
            for row in data:
                writercsv.writerow(row)
        
    def test():
        #open_zip(datafile)
        data = parse_file(datafile)
        #print data
        save_file(data, outfile)
    
        number_of_rows = 0
        stations = []
    
        ans = {'FAR_WEST': {'Max Load': "2281.2722140000024",
                            'Year': "2013",
                            "Month": "6",
                            "Day": "26",
                            "Hour": "17"}}
        correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                            'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
        fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    
        with open(outfile) as of:
            csvfile = csv.DictReader(of, delimiter="|")
            for line in csvfile:
                station = line["Station"]
                if station == 'FAR_WEST':
                    for field in fields:
                        #print ans[station][field]
                        #print line[field]
                        assert ans[station][field] == line[field]
    
                number_of_rows += 1
                stations.append(station)
    
            # Check Station Names
            assert set(stations) == set(correct_stations)
            
            # Output should be 8 lines not including header
            assert number_of_rows == 8
            
        print "All tests passed"
    
    test()
    
    if __name__ == "__main__":
        test()


    Writing problem12.py



    %%writefile problem13.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    This exercise shows some important concepts that you should be aware about:
    - using codecs module to write unicode files
    - using authentication with web APIs
    - using offset when accessing web APIs
    
    To run this code locally you have to register at the NYTimes developer site 
    and get your own API key. You will be able to complete this exercise in our UI without doing so,
    as we have provided a sample result.
    
    Your task is to process the saved file that represents the most popular (by view count)
    articles in the last day, and return the following data:
    - list of dictionaries, where the dictionary key is "section" and value is "title"
    - list of URLs for all media entries with "format": "Standard Thumbnail"
    
    All your changes should be in the article_overview function.
    The rest of functions are provided for your convenience, if you want to access the API by yourself.
    """
    import json
    import codecs
    import requests
    
    URL_MAIN = "http://api.nytimes.com/svc/"
    URL_POPULAR = URL_MAIN + "mostpopular/v2/"
    API_KEY = { "popular": "",
                "article": ""}
    
    
    def get_from_file(kind, period):
        filename = "popular-{0}-{1}.json".format(kind, period)
        with open(filename, "r") as f:
            return json.loads(f.read())
    
    
    def article_overview(kind, period):
        data = get_from_file(kind, period)
        # YOUR CODE HERE
        titles = [{e['section']:e['title']} for e in data]
        urls=[]
        for js1 in data:
            for js2 in js1['media']:
                for js3 in js2['media-metadata']:
                    if js3['format'] == "Standard Thumbnail":
                        urls.append(js3['url'])
                
        return (titles, urls)
    
    
    def query_site(url, target, offset):
        # This will set up the query with the API key and offset
        # Web services often use offset paramter to return data in small chunks
        # NYTimes returns 20 articles per request, if you want the next 20
        # You have to provide the offset parameter
        if API_KEY["popular"] == "" or API_KEY["article"] == "":
            print "You need to register for NYTimes Developer account to run this program."
            print "See Intructor notes for information"
            return False
        params = {"api-key": API_KEY[target], "offset": offset}
        r = requests.get(url, params = params)
    
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()
    
    
    def get_popular(url, kind, days, section="all-sections", offset=0):
        # This function will construct the query according to the requirements of the site
        # and return the data, or print an error message if called incorrectly
        if days not in [1,7,30]:
            print "Time period can be 1,7, 30 days only"
            return False
        if kind not in ["viewed", "shared", "emailed"]:
            print "kind can be only one of viewed/shared/emailed"
            return False
    
        url = URL_POPULAR + "most{0}/{1}/{2}.json".format(kind, section, days)
        data = query_site(url, "popular", offset)
    
        return data
    
    
    def save_file(kind, period):
        # This will process all results, by calling the API repeatedly with supplied offset value,
        # combine the data and then write all results in a file.
        data = get_popular(URL_POPULAR, "viewed", 1)
        num_results = data["num_results"]
        full_data = []
        with codecs.open("popular-{0}-{1}-full.json".format(kind, period), encoding='utf-8', mode='w') as v:
            for offset in range(0, num_results, 20):        
                data = get_popular(URL_POPULAR, kind, period, offset=offset)
                full_data += data["results"]
            
            v.write(json.dumps(full_data, indent=2))
    
    
    def test():
        titles, urls = article_overview("viewed", 1)
        assert len(titles) == 20
        assert len(urls) == 30
        assert titles[2] == {'Opinion': 'Professors, We Need You!'}
        assert urls[20] == 'http://graphics8.nytimes.com/images/2014/02/17/sports/ICEDANCE/ICEDANCE-thumbStandard.jpg'
    
    
    if __name__ == "__main__":
        test()

    Overwriting problem13.py



    
