

    # %%writefile find_author_data.py
    
    #!/usr/bin/env python
    # Your task here is to extract data from xml on authors of an article
    # and add it to a list, one item for an author.
    # See the provided data structure for the expected format.
    # The tags for first name, surname and email should map directly
    # to the dictionary keys
    import xml.etree.ElementTree as ET
    
    article_file = "exampleResearchArticle.xml"
    
    
    def get_root(fname):
        tree = ET.parse(fname)
        return tree.getroot()
    
    
    def get_authors(root):
        authors = []
        for author in root.findall('./fm/bibl/aug/au'):
            data = {
                    "fnm": None,
                    "snm": None,
                    "email": None
            }
            
    
            # YOUR CODE HERE
            for key in data:
                data[key] = author.find(key).text
                
            data['insr'] = [e.attrib['iid'] for e in author.findall('insr')]
            authors.append(data)
    
        return authors
    
    
    def test():
        #withour insr
        solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}, {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'}, {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'}, {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'}, {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'}, {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'}, {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'}, {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
        
        root = get_root(article_file)
        data = get_authors(root)
        assert data[0] == solution[0]
        assert data[1]["fnm"] == solution[1]["fnm"]
        
        
        #with insr
        solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                    {'insr': ['I2'], 'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                    {'insr': ['I3', 'I4'], 'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                    {'insr': ['I3'], 'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                    {'insr': ['I8'], 'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                    {'insr': ['I3', 'I5'], 'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                    {'insr': ['I6'], 'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                    {'insr': ['I7'], 'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    
        root = get_root(article_file)
        data = get_authors(root)
    
        assert data[0] == solution[0]
        assert data[1]["insr"] == solution[1]["insr"]
    
    
    test()

    Overwriting find_author_data.py



    # %%writefile post_html_form.py
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # Please note that the function 'make_request' is provided for your reference only.
    # You will not be able to to actually use it from within the Udacity web UI.
    # Your task is to process the HTML using BeautifulSoup, extract the hidden
    # form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the approprate
    # values in the data dictionary.
    # All your changes should be in the 'extract_data' function
    from bs4 import BeautifulSoup
    import requests
    import json
    
    html_page = "page_source.html"
    
    
    def extract_data(page):
        data = {"eventvalidation": "",
                "viewstate": ""}
        with open(page, "r") as html:
            soup = BeautifulSoup(html)
            data['eventvalidation'] = soup.find(id='__EVENTVALIDATION')['value']
            data['viewstate']  = soup.find(id='__VIEWSTATE')['value']
            
            
    
        return data
    
    
    def make_request(data):
        eventvalidation = data["eventvalidation"]
        viewstate = data["viewstate"]
    
        #for managed session, use s instead of r
    #     s = requests.Session()
        r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                        data={'AirportList': "BOS",
                              'CarrierList': "VX",
                              'Submit': 'Submit',
                              "__EVENTTARGET": "",
                              "__EVENTARGUMENT": "",
                              "__EVENTVALIDATION": eventvalidation,
                              "__VIEWSTATE": viewstate
                        })
    
        return r.text
    
    
    def test():
        data = extract_data(html_page)
        assert data["eventvalidation"] != ""
        assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
        assert data["viewstate"].startswith("/wEPDwUKLTI")
    
        
    test()


    %%writefile process_all.py
    
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # Let's assume that you combined the code from the previous 2 exercises
    # with code from the lesson on how to build requests, and downloaded all the data locally.
    # The files are in a directory "data", named after the carrier and airport:
    # "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
    # The table with flight info has a table class="dataTDRight".
    # There are couple of helper functions to deal with the data files.
    # Please do not change them for grading purposes.
    # All your changes should be in the 'process_file' function
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    from bs4 import BeautifulSoup
    from zipfile import ZipFile
    import os
    
    datadir = "data"
    
    
    def open_zip(datadir):
        with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
            myzip.extractall()
    
    
    def process_all(datadir):
        files = os.listdir(datadir)
        return files
    
    
    def process_file(f):
        # This is example of the datastructure you should return
        # Each item in the list should be a dictionary containing all the relevant data
        # Note - year, month, and the flight data should be integers
        # You should skip the rows that contain the TOTAL data for a year
        # data = [{"courier": "FL",
        #         "airport": "ATL",
        #         "year": 2012,
        #         "month": 12,
        #         "flights": {"domestic": 100,
        #                     "international": 100}
        #         },
        #         {"courier": "..."}
        # ]
        data = []
        info = {}
        info["courier"], info["airport"] = f[:6].split("-")
        #print info
        with open("{}/{}".format(datadir, f), "r") as html:
            soup = BeautifulSoup(html)
            table = soup.find('table', {'class':'dataTDRight'})
            for row in table.findAll('tr')[1:]:
                fields = row.findAll('td')
                fields = [e.text.replace(',','') for e in fields]
                try:
                    fields.index('TOTAL')
                except ValueError:
                    fields = [int(float(e)) for e in fields ]
                    info['year'] = fields[0]
                    info['month'] = fields[1]
                    info['flights'] = {
                                    'domestic':fields[2],
                                    'international':fields[3],
                                    }
                    data.append(info)
                    
                    
            
    
        return data
    
    
    def test():
        print "Running a simple test..."
        open_zip(datadir)
        files = process_all(datadir)
        data = []
        for f in files:
            data += process_file(f)
        #print data
        assert len(data) == 399
        for entry in data[:3]:
            assert type(entry["year"]) == int
            assert type(entry["flights"]["domestic"]) == int
            assert len(entry["airport"]) == 3
            assert len(entry["courier"]) == 2
        assert data[-1]["airport"] == "ATL"
        assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
        
        print "... success!"
    
    if __name__ == "__main__":
        test()

    Writing process_all.py



    
