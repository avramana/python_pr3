import dicoper as do
import sys

dobj = do.Dicoper()
dataDicMain = {}
dataDicMain = dobj.readJson("data.json")

while True:
    print("\nType exit to terminate program")
    word = input("Enter word :\n")
    if(word == "exit"):
        sys.exit(1)
    else:
        result = dobj.findMeaning(dataDicMain,word)
        if type(result) == list:
            for item in result:
                print(item)
        else:
            print(result)