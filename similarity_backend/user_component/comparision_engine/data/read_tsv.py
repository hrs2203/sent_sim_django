def read_file(fileName: str, sep: str = "\t"):
    fileContent = None
    with open(fileName, 'r') as fileObject:
        fileContent = fileObject.read().split("\n")
        fileParsedContent = [item.split(sep) for item in fileContent]
    return fileParsedContent

def read_quora_data(fileName: str, sep: str = " \",\" "):
    fileContent = None
    with open(fileName, 'r') as fileObject:
        fileContent = fileObject.read().split("\n")
        fileParsedContent = []
        for item in fileContent:
            temp = item.split(sep) 
            if len(temp) == 6:
                fileContent.append( fileContent[-1][1:-1], fileContent[-3][1:-1], fileContent[-2][1:-1] )
    return fileParsedContent[1:]