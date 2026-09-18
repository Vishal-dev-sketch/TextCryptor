encode_sysmbol={"a":"☺", "b":"☻", "c":"♥", "d":"♦", "e":"♣", "f":"♠", "g":"•", "h":"◘", "i":"○", "j":"◙", "k":"♂", "l":"♀", "m":"♪", "n":"♫", "o":"☼", "p":"►", "q":"◄", "r":"↕", "s":"‼", "t":"¶", "u":"§", "v":"▬", "w":"↨", "x":"↑", "y":"↓", "z":"→", "A" : "F", "B" : "M", "C" : "V", "D" : "J", "E" : "X", "F" : "H", "G" : "B", "H" : "O", "I" : "T", "J" : "G", "K" : "C", "L" : "Q", "M" : "E", "N" : "R", "O" : "K", "P" : "Y", "Q" : "P", "R" : "L", "S" : "N", "T" : "U", "U" : "W", "V" : "D", "W" : "Z", "X" : "A", "Y" : "S", "Z" : "I", '0': '7', '1': '9', '2': '8', '3': '3', '4': '0', '5': '2', '6': '6', '7': '5', '8': '4', '9': '1'}
decoded_sysmbol={'☺': 'a', '☻': 'b', '♥': 'c', '♦': 'd', '♣': 'e', '♠': 'f', '•': 'g', '◘': 'h', '○': 'i', '◙': 'j', '♂': 'k', '♀': 'l', '♪': 'm', '♫': 'n', '☼': 'o', '►': 'p', '◄': 'q', '↕': 'r', '‼': 's', '¶': 't', '§': 'u', '▬': 'v', '↨': 'w', '↑': 'x', '↓': 'y', '→': 'z', "F" : "A", "M" : "B", "V" : "C", "J" : "D", "X" : "E", "H" : "F", "B" : "G", "O" : "H", "T" : "I", "G" : "J", "C" : "K", "Q" : "L", "E" : "M", "R" : "N", "K" : "O", "Y" : "P", "P" : "Q", "L" : "R", "N" : "S", "U" : "T", "W" : "U", "D" : "V", "Z" : "W", "A" : "X", "S" : "Y", "I" : "Z", '7': '0', '9': '1', '8': '2', '3': '3', '0': '4', '2': '5', '6': '6', '5': '7', '4': '8', '1': '9'}

decoded_text_list=[] #empty list that will store the decoded text
encoded_text_list=[] #empty list that will store the encoded text

#Method for decoding
def decoded(word):
    decoded_word=" " #fun() var to store the decoded word in the func

    for l in word:
        if l in decoded_sysmbol.keys():
            decoded_word+=decoded_sysmbol[l] #decoding the word
        else:
            decoded_word+=l

    global decoded_text_list 
    decoded_text_list.append(decoded_word) #adding the decoded word into the decoded text list

#Method for encoding
def encode(word):
    encoded_word=" " #fun() var to store the encoded word in the func

    for l in word:
        if l in encode_sysmbol.keys():
            encoded_word+=encode_sysmbol[l] #assigning the corresponding value of letter l with it's encoded code from  encode_symbol 
        else:
            encoded_word+=l
            
    global encoded_text_list 
    encoded_text_list.append(encoded_word) #adding the encoded word into the encoded text list

#----------------------------------------------------------------------------------------------

option=input("Enter your choice:-\n1. for Encoding\n2. for Decoding\n")

match option:
    case "1":
        text=input("Enter the text :- ")
        txt=text.split()

        for word in txt:
            encode(word)

        result="".join(encoded_text_list)
        print(result)

    case "2":
        text=input("Enter the text :- ")
        txt=text.split()

        for word in txt:
            decoded(word)

        result="".join(decoded_text_list)
        print(result)