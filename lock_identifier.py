'''
A script to identify all lock files and their paths.
'''
import os   # Interact with windows files and folders
import csv
import argparse
from pprint import pprint as pp

def walk(drive, directory, fileExt, verbose=False):
    ''' Perform Walk from (A) Drive and (B) Directory to look for (C) Files '''
    if verbose:
        print "Starting Walk"
    walkData = {}  # Data Object to return

    pathToStr ="{drive}:\{dir}".format(drive=drive, dir=directory)   #Create formatted string
 
    if verbose== True:
        print pathToStr

    os.chdir(pathToStr)    #Create a Windows specific directory string 

    walk = os.walk(pathToStr)
    for tupData in walk: #Tuple tupData :0 == dirpath ; 1 == dirnames ; 2 == filenames
        
        for fname in tupData[2]: # For Each string in the tuple for filenames
            if fileExt in fname.lower():
                walkData[str(tupData[0])] = [fname for fname in tupData[2] if fileExt.lower() in fname.lower() ] 

    return walkData

def outputfunction(walkResults, out):
    if out == 'pp':
        pp(walkResults) #Fix to be pretty print
    elif out =='dict':
        print walkResults
    else:
        pass


def main(drive, directory, fileExt, output, verbose):
    if verbose:
        print "Starting Main"
    walkResults=walk(drive, directory, fileExt, output)
    outputfunction(walkResults, output)



if __name__ == '__main__':

    ''' 
    ArgParse Setup:
    You must give a drive (i.e. C) followed by a directory (i.e. 'MyFolder') to construct a valid path (C:\Myfolder)
    '''

    parser = argparse.ArgumentParser(description="A File Finding Script!")

    parser.add_argument('drive', 
                        action='store', 
                        help="Choose the Drive to use MANDATORY")

    parser.add_argument('directory', 
                        action='store', 
                        help="Which Directory to start performing walk MANDATORY")

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


    args = parser.parse_args()
    print args

    main(args.drive, args.directory, args.f, args.o, args.v)
