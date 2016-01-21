
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