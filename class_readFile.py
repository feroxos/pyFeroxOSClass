import json
import os
def readFile_andParseJson(filePath):
    file_content="";
    with open(filePath, 'r') as file:
        file_content+=file.read()
    return json.loads(file_content)
def readFile_NoParseJson(filePath):
    file_content="";
    with open(filePath, 'r') as file:
        file_content+=file.read()
    return file_content
def countFile_row(filePath):
    try:
        with open(filePath, 'r') as file:
            num_lines = sum(1 for line in file)
    except:
        return -1
    return num_lines

def listFile_with_prefix(oDir,prefisso):
    files = os.listdir(oDir)
    file_con_prefisso = [file for file in files if file.startswith(prefisso)]    
    return file_con_prefisso

