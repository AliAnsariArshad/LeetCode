def matchReplacement( mappings):

    newstr = ""
    dict = {}

    for elem in mappings:
            dict[elem[0]] = elem[1]
    print (dict)


matchReplacement([["e","3"],["t","7"],["t","8"]])


