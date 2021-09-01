def read_file(fileName: str, sep: str = "\t"):
    fileContent = None
    with open(fileName, 'r') as fileObject:
        fileContent = fileObject.read().split("\n")
        fileParsedContent = [item.split(sep) for item in fileContent]
    return fileParsedContent
