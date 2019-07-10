import json as js
from difflib import get_close_matches

class Dicoper:
    def __init__(self):
        print("Init Class")

    def readJson(self,filename):
        dataDic = {}
        dataDic = js.load(open(filename))
        return dataDic

    def findMeaning(self,dataDic,word):
        w = word.lower()
        ret = []
        if w in dataDic:
            ret.append("Meaning of given word \'"+w+ "\' is :")
            ret += dataDic[w]
            return ret
        elif w.title() in dataDic:
            ret.append("Meaning of given word \'" + w.title() + "\' is :")
            ret += dataDic[w.title()]
            return ret
        else:
            matches = get_close_matches(word, dataDic.keys())
            if (len(matches)>0):
                print("Do you mean, ",matches[0]+"? (Y/N) : ")
                option=input()
                if(option == "Y" or option == "y"):
                    ret.append("Meaning of given word \'"+matches[0]+"\' is : ")
                    ret += dataDic[matches[0]]
                    return ret
                elif(option == "N" or option == "n"):
                    return "Then word Not Found!!!"
                else:
                    return "Not understood your option!!!"
            else:
                return "Word Not Found!!!"
