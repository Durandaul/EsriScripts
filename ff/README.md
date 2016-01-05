# FF
A script for creating 

How to use:
    python ff.py {drive} {directory_path} -f {file_extension} [-v] [-d]
Example:

    python ff.py C \Users\Durandaul -f .xls 
    
  This will return all xls files within all folders/subdirectories of durandal and return the result as a dictionairy

    python ff.py C \Users\Durandaul -f .xls -d
    
  This will do the same but invoke the delete function and go through each file listed to see if you want to delete it.
  Once it's done, it will ask if you want to re-run the program to confirm it's gone.
  
Feedback greatly appreciated :)
