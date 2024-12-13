
import os 
import requests
import time

loopVariable = 0
countdownVariable = 5

customSites = {
    'github': 'https://github.com/',
    'youtube': 'https://youtube.com/@',
    'custom': 'customsite'
}

def inputFunction():
    os.system('cls')
    print("1 - A github user profile - github.com/------\n"
          "2 - A youtube channel's profile - youtube.com/@------\n"
          "3 - A custom URL - https://example.com/example\n")
    chooseInput = int(input("Please type the number of the site you want to scrape:  "))
    if (chooseInput == 1):
        githubFunction()
    elif (chooseInput == 2):
        youtubeFunction()
    elif (chooseInput == 3):
        customFunction()
    else:
        print("Please type a valid option")
        inputFunction()


def customFunction():
    os.system('cls')
    global customInput
    customInput = input("What URL would you like to scrape?  ex. https://example.com/example\n - ")
    customSites['custom'] = customInput 
    os.system('cls')
    print("Would you like to scrape the following URL? -", customInput)
    global loopVariable
    while (loopVariable == 0):
        yOrN = input("Type Y or N: ")
        if (yOrN == "y") or (yOrN == "Y"):
            customProcess()
            loopVariable=loopVariable+1
        elif (yOrN == "n") or (yOrN == "N"):
            customFunction()
            loopVariable=loopVariable+1
        else:
            print("Please type Y or N")

def youtubeFunction():
    os.system('cls')
    global youtubeInput
    youtubeInput = input("What is the username of the channel you'd like to scrape?\n - @")
    os.system('cls')
    print("Would you like to scrape the following channel? -", "https://youtube.com/@"+youtubeInput)
    global loopVariable
    while (loopVariable == 0):
        yOrN = input("Type Y or N: ")
        if (yOrN == "y") or (yOrN == "Y"):
            os.system('cls')
            youtubeProcess()
            loopVariable=loopVariable+1
        elif (yOrN == "n") or (yOrN == "N"):
            os.system('cls')
            youtubeFunction()
            loopVariable=loopVariable+1
        else:
            os.system('cls')
            print("Please type Y or N")

def githubFunction():
    os.system('cls')
    global githubInput
    githubInput = input("What is the username of the profile you'd like to scrape?\n - @")
    os.system('cls')
    print("Would you like to scrape the following user? -", customSites['github']+githubInput)
    global loopVariable
    while (loopVariable == 0):
        yOrN = input("Type Y or N: ")
        if (yOrN == "y") or (yOrN == "Y"):
            os.system('cls')
            githubProcess()
            loopVariable=loopVariable+1
        elif (yOrN == "n") or (yOrN == "N"):
            os.system('cls')
            githubFunction()
            loopVariable=loopVariable+1
        else:
            os.system('cls')
            print("Please type Y or N")

def customProcess():
    global customInput
    countdownVariable = 5
    requestOutput = requests.get(customInput)
    fileOpen = open("htmlOutput.txt", "w")
    fileOpen.write(str(requestOutput.content))
    fileOpen.close()
    os.system('cls')
    while (countdownVariable > 0):
        print("The scraped HTML has been dumped into htmlOutput.txt!")
        print(customInput, "was the target.")
        print("Going back to main menu in", countdownVariable, "seconds.")
        time.sleep(1)
        countdownVariable=countdownVariable-1
        os.system('cls')
    inputFunction()


def youtubeProcess():
    global youtubeInput
    countdownVariable = 5
    requestInput = (customSites['youtube']+youtubeInput)
    requestOutput = requests.get(requestInput)
    fileOpen = open("htmlOutput.txt", "w")
    fileOpen.write(str(requestOutput.content))
    fileOpen.close()
    os.system('cls')
    while (countdownVariable > 0):
        print("The scraped HTML has been dumped into htmlOutput.txt!")
        print(requestInput, "was the target.")
        print("Going back to main menu in", countdownVariable, "seconds.")
        time.sleep(1)
        countdownVariable=countdownVariable-1
        os.system('cls')
    inputFunction()

    
def githubProcess():
    global githubInput
    countdownVariable = 5
    requestInput = (customSites['github']+githubInput)
    requestOutput = requests.get(requestInput)
    fileOpen = open("htmlOutput.txt", "w")
    fileOpen.write(str(requestOutput.content))
    fileOpen.close()
    os.system('cls')
    while (countdownVariable > 0):
        print("The scraped HTML has been dumped into htmlOutput.txt!")
        print(requestInput, "was the target.")
        print("Going back to main menu in", countdownVariable, "seconds.")
        time.sleep(1)
        countdownVariable=countdownVariable-1
        os.system('cls')
    inputFunction()


    
inputFunction()