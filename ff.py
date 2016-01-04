import argparse
from file_finder import fFinder

def main(drive, directory, fileExt, output, verbose):
    ''' Create a data object, pass it and the file extention to perform a walk and send to the output function'''
    if verbose:
        print "Starting Main"
    finder=fFinder(drive, directory, fileExt, output, verbose)
    dataObj = finder.createDataObject()
    walkResults = finder.walk() 
    finder.returnResults()
    


if __name__ == '__main__':

    ''' 
    ArgParse Setup:
    You must give a drive (i.e. C) followed by a directory (i.e. 'MyFolder') to construct a valid path (C:\Myfolder)
    Example usage:
        python ff Z /directories/path/to/my/file -f .lock -v 

    '''

    parser = argparse.ArgumentParser(description="A File Finding Script!")

    parser.add_argument('drive', 
                        action='store', 
                        help="Choose the Drive to use; MANDATORY")

    parser.add_argument('directory', 
                        action='store', 
                        help="Which Directory to start performing walk; MANDATORY")

    parser.add_argument('-o',
                        action='store',
                        default='pp', 
                        help='Output file name. Default to STDOUT' )

    parser.add_argument('-f',
                        action='store',
                        help='''String to find in file name. Easiest to just use file extensions without the period. (i.e. if you\'re looking
                        for max.png, just use png as the file ''')

    parser.add_argument('-v',
                        action="store_true",
                        #type=bool,
                        #default=False,
                        help="Output misc for debugging")

    parser.add_argument('-d',
                        action='store_true',
                        help="Invoke the deleter function and manually go through a list of values to remove")


    args = parser.parse_args()
    drive=args.drive


    main(args.drive, args.directory, args.f, args.o, args.v)