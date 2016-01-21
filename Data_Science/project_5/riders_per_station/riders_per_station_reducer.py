import sys

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should return one row
    per unit, along with the total number of ENTRIESn_hourly over the course of may. 
    
    You can assume that the input to the reducer is sorted by UNIT, such that all rows 
    corresponding to a particular UNIT are group together.

    '''
    old_unit = None
    en_hour = 0
    for line in sys.stdin:
        
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        
        this_unit, this_count = data
        if old_unit and old_unit != this_unit:
            print "{0}\t{1}".format(old_unit, en_hour)
            en_hour = 0
        old_unit = this_unit
        en_hour+= float(this_count)
        
        if old_unit != None:
            print "{0}\t{1}".format(old_unit, en_hour)


reducer()
