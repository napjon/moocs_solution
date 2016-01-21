import sys

def reducer():
    '''
    Given the output of the mapper for this assignment, simply print
    0 and then the average number of riders per day for the month of 05/2011,
    separated by a tab.
    
    There are 31 days in 05/2011.
    
    Example output might look like this:
    0   10501050.0
    '''

    riders = -1      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    for line in sys.stdin:
        # your code here
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        riders+=1
        #logging.info(riders)
        this_key, this_hours = data
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, num_hours/float(riders))
            num_hours = 0
            riders = 0
        
        old_key = this_key
        num_hours += float(this_hours)
        
        
        #if old_key != None and old_key == 'nofog-norain':
            #logging.info('last')
    print "{0}\t{1}".format(old_key, num_hours/(riders+1))

reducer()
