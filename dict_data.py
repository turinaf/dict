'''
 Simple bilingual dictionary
 by Turi
 Github: https://github.com/turinaf
'''

'''
 This file the logic of dictionary behind the GUI.
 GUI is implemented in dict_gui.py file.
'''
with open("/home/turi/git/dict/words.txt", 'r', encoding="utf8") as fp:
    lines = fp.readlines()

wordlist = []
for line in lines:
    word = line.split() # delimiter is new line.
    wordlist.append(word) # Append each line wich countain a word & its chinese counterpart to word list. Basically it's list of lists.


# print(wordlist)
class Dict():
    # dict() prints all the dictionary
    def dict():
        print("Word   part of Speech\t Chinese meaning")
        for word in wordlist:
            print(word[0], "\t", word[1], "\t", word[2])
            

    def search(self, str):
        matched = []
        for item in wordlist:
            word = "".join(item[0])
            if word.startswith(str):
                matched.append(item)
        return matched

    def define1(self, key):
        for word in wordlist:
            if word[0] == key:
                # print(word[0]," ", word[1], "\t", word[2])
                return word
           

    def test(self):
        key = input("Enter you search key: ")
        result = self.search(key)
        if len(result) == 0:
            print("Nothing matched your search key")
        else:
            print("{} item(s) matched your search key".format(len(result)))
            for word in result:
                print(word[0])
                print(self.define1(word[0])) # calls define method to 
def main():
    myDict = Dict()
    myDict.test()

if __name__=="__main__":
    main()