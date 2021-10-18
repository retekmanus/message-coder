key = input("Input the key here: ")
inp = input("Input your message here: ")

inpU = inp.upper()
inpS = [] #input split into letters
inpN = [] #input converted to numbers that will be used to find the pair letter for encoding
inpN2 = [] #input converted to numbers a second time
keyS = [] #key split into characters
keySN = [] #split key converted to int
outlist = []
counter = 0

abc = {
    "A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": "6", "H": "7", "I": "8", "J": "9", "K": "10",
    "L": "11", "M": "12", "N": "13", "O": "14", "P": "15", "Q": "16", "R": "17", "S": "18", "T": "19", "U": "20", "V": "21",
    "W": "22", "X": "23", "Y": "24", "Z": "25", ".": "26", ",": "27", ";": "28", ":": "29", "?": "30", "-": "31", "_": "32", 
    "<": "33", ">": "34", "(": "35", ")": "36", "!": "37", "%": "38", "/": "39", "=": "40", "+": "41", "'": "42", '"': "43",
    "÷": "44", "×": "45", "[": "46", "]": "47", "{": "48", "}": "49", "#": "50", "&": "51", "@": "52", "*": "53", "0": "54",
    "1": "55", "2": "56", "3": "57", "4": "58", "5": "59", "6": "60", "7": "61", "8": "62", "9": "63"
}

xyz = {
    "0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", "7": "H", "8": "I", "9": "J", "10": "K",
    "11": "L", "12": "M", "13": "N", "14": "O", "15": "P", "16": "Q", "17": "R", "18": "S", "19": "T", "20": "U", "21": "V",
    "22": "W", "23": "X", "24": "Y", "25": "Z",  "26": ".", "27": ",", "28": ";", "29": ":", "30": "?", "31": "-", "32": "_", 
    "33": "<", "34": ">", "35": "(", "36": ")", "37": "!", "38": "%", "39": "/", "40": "=", "41": "+", "42": "'", "43": '"',
    "44": "÷", "45": "×", "46": "[", "47": "]", "48": "{", "49": "}", "50": "#", "51": "&", "52": "@", "53": "*", "54": "0",
    "55": "1", "56": "2", "57": "3", "58": "4", "59": "5", "60": "6", "61": "7", "62": "8", "63": "9"
}

for char in key: #digits of key added to keyS one by one
    keyS.append(char)

for char in inpU: #letters of uppercase input added to inpS one by one
    if char == " ":
        char = " "
        inpS.append(char)
    else:
        inpS.append(char)

for char in keyS: #digits of the key converted to be of int type
    num = int(char)
    keySN.append(num)

for char in inpS: #input message converted to numbers
    if char == " ":
        char = " "
        inpN.append(char)
    else:
        char = abc[char]
        num = int(char)
        inpN.append(num)

for char in inpN: #input message numbers added to matching digit of key
    if char == " ":
        char = " "
        inpN2.append(char) 
    else:
        try:
            char -= keySN[counter]
            inpN2.append(char)
            counter += 1
        except:
            counter = 0
            char -= keySN[counter]
            inpN2.append(char)
            counter += 1


for char in inpN2: #modified input numbers converted to letters
    if char == " ":
        char = " "
        outlist.append(char)
    elif char > 63:
        re = char % 63
        re -= 1
        char = re 
        char = xyz[f"{char}"]
        outlist.append(char)  
    elif char < 0:
        char = char + 64
        char = xyz[f"{char}"]
        outlist.append(char)
    else:
        char = xyz[f"{char}"]
        outlist.append(char)

output = ''.join(outlist) #converted message joined into text
print(output)