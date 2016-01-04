class esri(object):
    ''' A class for working with ESRI Files'''
    def __init__(self):
        pass

    def parseLock(self, fname):
        ''' Pass a lockfilename into the parser to seperate out into process, misc, file, directory, and computer'''
        lockParse=fname.split('.') 
        try:
            parsedLockFile=dict(computer=lockParse[1], processID=lockParse[3],fType=lockParse[5],fName=lockFile)
        except IndexError:
            parsedLockFile=dict(fName=lockFile)
        return parsedLockFile