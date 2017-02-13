import sys

class ProcessCSV:

#['', '', 'name9', '', 'name0', '', '']

    def check_for_header( self, tokens ):
        print 'tokens length = ', len( tokens )
        if len( tokens ) >= 7 and \
           len( tokens[0] ) == 0 and \
           len( tokens[1] ) == 0 and \
           len( tokens[2] ) > 0  and \
           len( tokens[3] ) == 0 and \
           len( tokens[4] ) > 0  and \
           len( tokens[5] ) == 0 and \
           len( tokens[6] ) == 0:
            print 'check_for_header: tokens ===> ' , str( tokens ), ' is a header...'

    def read_file( self, filename ):
        test_file = open( filename )
        lines = test_file.readlines()
        print lines
        print len(lines)
        for line in lines:
            tokens = line.strip().split(",")
            self.check_for_header( tokens )
            print tokens
            ls = tokens[1]
            if len( ls ) > 0:
                num = int( ls )
                print num
        test_file.close()

if __name__ == '__main__':

    if len( sys.argv ) == 1:
         print "USAGE: ProcessCSV <filename>\n"
         sys.exit(-1)


    filename = sys.argv[1] 

    pcsv = ProcessCSV()
    pcsv.read_file( filename )  
