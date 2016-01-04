import os   # Interact with windows files and folders
from pprint import pprint as pp
from esri_files import esri

class fFinder(object):

    def __init__(self,drive,directory,fileExtensions,output=False,verbose=False):
        ''' Initialize the object with the variables passed. Default walkreturn is an empty dict as there is no data return from walk'''

        self.drive=drive
        self.directory=directory
        self.ext=fileExtensions
        self.out=output
        self.verbose=verbose
        self.results={"results":{}}


    def createDataObject(self):
        ''' Create a dictionairy with the path to be used for the initial walk'''
        dataObject = {}
        pathToStrWindows ="{drive}:\{directory}".format( drive=self.drive, directory=self.directory ) 
        if self.verbose:
            print pathToStr
        os.chdir(pathToStrWindows)
        if self.verbose:
            print os.getcwd()
        self.results['INIT_PATH'] = pathToStrWindows


    def walk(self):
        ''' 
        Perform Walk from (A) Drive and (B) Directory to look for (C) Files. The return value from walk is a 
        3 tuple that contains dirpath[0], dirnames[1], and filenames[2].
        The self.results object is updated to have:
            - The key INIT_PATH which is the start path
            - A key for each folder walked containg a list comprehension of matching files to extensions. 
        '''

        if self.verbose:
            print "Starting Walk"

        dirWalk = os.walk(self.results['INIT_PATH'])

        for tupData in dirWalk:
            for fName in tupData[2]: # For Each string in the tuple for filenames
                if self.ext in fName.lower(): #If the file extension has a match in the lowercase version of the file listed in the tuple for files
                    self.results["results"][str(tupData[0])] = [fName for fName in tupData[2] if self.ext.lower() in fName.lower() ]   
                    if self.verbose:
                        print "{path}:{fileName}".format( path=tupData[0],fileName=fName.lower() )


    def returnResults(self):
        ''' Choice of output is currently prettyprint, shelve, or dictionairy. Dictionairy is default'''
        if self.results:
            if self.out == 'pp':
                pp(self.results)

            else:
                return self.results
        else:
            return self.results
            
    def fDelete(self, fPath):
        ''' File remover function for search and remove. Not fully automated, this requires user input to ensure no mistakes are made. Called by fRemoval'''
        print "File Path to be deleted: {fpath}".format(fpath=fpath)
        confirm=raw_input('Are you sure you want to delete this path? (y|n)')
        while(confirm.lower() != 'y' or confirm.lower() != 'n'):
            confirm=raw_input('Are you sure you want to delete this path? (y|n)')
        if confirm.lower() == 'y':
            os.remove(fpath)
            return True
        elif confirm.lower() == 'n':
            return False

    def fRemoval(self):
        '''The removal process using the self.results object'''
        #for pathFile in self.results['results']:
            # self.fDelete()

        pass
