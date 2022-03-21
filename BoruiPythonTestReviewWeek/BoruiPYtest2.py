import string

# 1.get a list of documents from file
def getDocuments()->list:
    try:
        file = open("ap_docs.txt","r")
    except IOError:
        print("Can't read file movie_list.txt in current directory")
    documents = list()
    # create tmp to collect string 
    tmp = ""
    for line in file:
        # stop collecting and append if new document
        if(line == "<NEW DOCUMENT>\n"):
            if(tmp != ""):
                documents.append(tmp)
                tmp = ""
            continue
        # collecting lines
        else:
            tmp += line
    # for last document which isn't followed by new document
    if tmp != "":
        documents.append(tmp)        
    file.close()
    return documents
# 2.construct the dict from the list of documents
def getDict( documents:list )->dict:
    # create dict 
    wordDict = dict()
    for index, doc in enumerate(documents):
        # get raw wordlist from each document
        wordlist = doc.split()
        # process wordlist
        for word in wordlist:
            # process each word to be lower and stripped
            wp = word.strip(string.punctuation).lower()
            # store set of doc_numbers and if not in dict create new set
            if wp in wordDict:
                #use index as doc_number and store in set
                wordDict[wp].add(index + 1)
            else:
                wordDict[wp] = set()
                wordDict[wp].add(index + 1)
    return wordDict

# DEBUG print(getDict(getDocuments()))

#3.using input words to find sets(doc_numbers..) from the dict and get intersection of sets
def findWordsIntersect( db:dict, words:string )->string:
    # get input words
    wordlist = words.strip().lower().split()
    wordset = set()
    for word in wordlist:
        # search in dict, if no matching then set tmpset to false
        # therefore no documents since word not exist in any document
        tmpset = db.get(word, False)
        if tmpset == False:
            return "No satisfying documents."
        # if the first set assgin directly
        elif len(wordset) == 0:
            wordset = tmpset
        #if not the first intersect with current wordset for doc numbers
        else:
            wordset = wordset & tmpset
    # if empty set then no satisfying document as well
    if len(wordset) == 0:
        return "No satisfying documents."
    # construct result string
    res = "Documents fiiting search: \n"
    for doc in wordset:
        res = res + str(doc) + " "
    return res

# DEBUG print(findWordsIntersect(getDict(getDocuments()), "side Of"))

documents = getDocuments()
db = getDict(documents)
# 4.Menu 
while True:
    choice = input("What would you like to do?\n1. Search for documents\n2. Read Document\n3. Quit Program\n>")
    if choice == "1":
        words = input("Enter search words: ")
        print(findWordsIntersect(db, words))
    elif choice == "2":
        docNumStr = input("Enter document number: ")
        try:
            docNum = int(docNumStr)
            doc = documents[docNum-1]
            print("Document #" + docNumStr + "\n-----------\n" + doc)
        except ValueError:
            print("illegal input, pls enter an inteager")
    elif choice == "3":
        print("<program exited>")
        break
