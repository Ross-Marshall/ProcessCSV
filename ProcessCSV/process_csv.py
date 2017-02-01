import sys

class ProcessCSV:


    def read_file( self, filename ):
        test_file = open( filename )
        lines = test_file.readlines()
        print lines
        print len(lines)
        text_file.close()

if __name__ == '__main__':

    if len( sys.argv ) == 1:
         print "USAGE: ProcessCSV <filename>\n"
         sys.exit(-1)


    filename = sys.argv[1] 

    pcsv = ProcessCSV()
    pcsv.read_file( filename )  
