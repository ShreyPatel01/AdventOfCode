sum = 0
numDictionary = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "oneight" : "18",
    "twone" : "21",
    "threeight" : "38",
    "fiveight" : "58",
    "sevenine" : "79",
    "eightwo" : "82",
    "eighthree" : "83",
    "nineight" : "98"
}

def dictionarySwitch(stringInput):
    result = ""
    index = 0 

    #Looks for match to dictionary
    while index < len(stringInput):
        match = False

        #Loops through each key in dictionary
        for word in numDictionary:
            #Matches characters to key in dictionary
            if stringInput[index:].startswith(word):
                #replaces characters with value to matched key
                result += numDictionary[word]
                #Move the index by the length of the matched word
                index += len(word)  
                match = True

        #If no match is found, keep the character unchanged
        if match == False:
            result += stringInput[index]
            index += 1

    return result

#Parsing input file to inputLines
with open ("input.txt","r") as input:
    inputLines = []
    for line in input:
        inputLines.append(line.strip())
input.close()

#Goes through each line in inputLines
for string in inputLines:
    #Replaces alphanumeric numbers with digits
    newString = dictionarySwitch(string)
    #Checks for digits in newString and assigns digits to list
    numbers = [char for char in newString if char.isdigit()]

    if len(numbers) == 1:
        fullNo = numbers[0] + numbers[0]
        sum += int(fullNo)
    else:
        fullNo = numbers[0] + numbers[-1]
        sum += int(fullNo)

print(sum)