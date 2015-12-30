'''
A script to identify all lock files and their paths. Currently this is optimized for:
1) Python 2.7 (print statements will break in 3)
2) Windows. No unix/mac functionality is exclusive but pathing and interpretation of path is explicitly windows
3) To only use python 2.7 standard library
To be Added: 
    - Options for file metrics
    -CSV Output
    -More generalization with esri specific class
'''
import os   # Interact with windows files and folders
import argparse
import shelve
from pprint import pprint as pp

def createDataObject(drive, directory):
    ''' Create a dictionairy with the path to be used for the initial walk'''
    dataObject = {}  
    pathToStr ="{drive}:\{directory}".format(drive=drive, directory=directory) 
    if verbose:
        print pathToStr
    os.chdir(pathToStr)
    if verbose:
        print os.getcwd()
    return dataObject['INIT_PATH']=pathToStr


def walk(dataStore, fileExt, verbose=False):
    ''' Perform Walk from (A) Drive and (B) Directory to look for (C) Files. The return value from walk is a 
    3 tuple that contains dirpath[0], dirnames[1], and filenames[2].
    The return object will have:
        -The key INIT_PATH whcih is the start path
        - A key for each folder walked containg a list comprehension of matching files to extensions. '''
    if verbose:
        print "Starting Walk"

    dirWalk = os.walk(dataStore['INIT_PATH'])

    for tupData in dirWalk:
        for fname in tupData[2]: # For Each string in the tuple for filenames
            if fileExt in fname.lower(): #If the file extension
                dataStore[str(tupData[0])] = [fname for fname in tupData[2] if fileExt.lower() in fname.lower() ]
                if verbose:
                    print "{path}:{fileName}".format(path=tupData[0],fileName=fname.lower())

    return walkData

def outputfunction(walkResults, out):
    ''' Choice of output is currently prettyprint, shelve, or dictionairy. Dictionairy is default'''
    if walkResults:
        if out == 'pp':
            pp(walkResults)

        elif out == 'shelve':
            db = shelve.open('lock_out')
            db['data'] = walkResults
            print 'Saving to Disk as a shelve file'
            db.close()

        else:
            return walkResults
    else:
        return walkResults
        
def fRemover(fPath):
    ''' File remover function for search and remove. Not fully automated, this requires user input to ensure no mistakes are made'''
    print "File Path to be deleted: {fpath}".format(fpath=fpath)
    confirm=raw_input('Are you sure you want to delete this path? (y|n)')

    while(confirm.lower() != 'y' or confirm.lower() != 'n'):
        confirm=raw_input('Are you sure you want to delete this path? (y|n)')
    if confirm.lower() == 'y':
        os.remove(fpath)
        return True
    elif confirm.lower() == 'n':
        return False



def main(drive, directory, fileExt, output, verbose):
    ''' Create a data object, pass it and the file extention to perform a walk and send to the output function'''
    if verbose:
        print "Starting Main"
    dataObj = dataStore(drive,directory)
    walkResults = walk(dataObj, fileExt, verbose) 
    outputfunction(walkResults, output)
    #Output function should be fixed as an object that returns dict or something



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

    parser.add_argument('-d',
                        action='store_true',
                        help="Invoke the deleter function and manually go through a list of values to remove")


    args = parser.parse_args()
    print args

    main(args.drive, args.directory, args.f, args.o, args.v)
