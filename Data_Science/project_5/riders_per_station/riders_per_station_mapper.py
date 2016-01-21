import sys
import string

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset.  This mapper 
    should return a line for each UNIT, along with the number of ENTRIESn_hourly for that row.
    
    An example input to the mapper may would look like this:
    R002    1050105.0
    
    The mapper should emit a key and value pair separated by a tab, for example:
    R002\t105105.0
    """
    
    i = 0;
    ##UNIT = 1
    ##ENTRIESn_hourly = 6
    for line in sys.stdin:
        i+=1
        logging.info(line)
        if i == 10:
           break
        
        data = line.strip().split(",")
        if data[1] == 'UNIT':
            continue
        print "{0}\t{1}".format(data[1],data[6])
                                    

mapper()