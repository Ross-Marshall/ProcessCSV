import sys

class ProcessCSV:

#['', '', 'name9', '', 'name0', '', '']

    def is_number(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def check_for_glaz( self, tokens ):
        if len( tokens ) >= 4 and \
           self.is_number( tokens[4] ):
            print 'check_for_glaz: ',tokens[4],' is a glaz'

    def check_for_header( self, tokens ):
        print 'tokens length = ', len( tokens )
        if len( tokens ) >= 7 and \
           len( tokens[0] ) == 0 and \
           len( tokens[1] ) == 0 and \
           len( tokens[2] ) == 0 and \
           len( tokens[3] ) > 0  and \
           len( tokens[4] ) == 0 and \
           len( tokens[5] ) > 0  and \
           len( tokens[6] ) == 0 and \
           len( tokens[7] ) == 0:
            print 'check_for_header: tokens ===> ' , str( tokens ), ' is a header...'

    def read_file( self, filename ):
        test_file = open( filename )
        lines = test_file.readlines()
        print lines
        print len(lines)
        for line in lines:
            tokens = line.strip().split(",")
            self.check_for_header( tokens )
            self.check_for_glaz( tokens )
            print tokens
            ls = tokens[1]
            if len( ls ) > 0:
                if self.is_number( ls ):
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
