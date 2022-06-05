
# importing the sys module
from datetime import datetime
import sys       
# inserting the mod.py directory at
# position 1 in sys.path
sys.path.insert(1, 'C:\\MyProjects2\\PythonNusLib\\NusLib')       
# importing the module NusLibGeneric.py
import NusLibGeneric   

#test AppendToTextFile_ThreadSafe_v1 method
FilePath = "C:\\MyProjects2\\PythonNusLib\\NusLib\\tests\\logtest.txt"
data = str(datetime) +  " - hi this is a test"
NusLibGeneric.AppendToTextFile_ThreadSafe_v1(FilePath,data)
 