
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
    