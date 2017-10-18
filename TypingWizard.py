##program to caluclate the accuracy and wpm of a rewritten text

import time

ogStr = "My name is Piyush Agrawal"
print("This is the original text:")
print(ogStr,"\n")
length = len(ogStr)
ogTime = time.localtime(time.time())
ogTime = (time.localtime(time.time()).tm_min*60)+(time.localtime(time.time()).tm_sec)

reStr = input("Enter your rewritten text here:\n")
wordList = reStr.split(' ')
len1 = len(wordList) ##length of the list containing words of the original text

reTime = (time.localtime(time.time()).tm_min*60)+(time.localtime(time.time()).tm_sec)
wrong = 0
right = 0
for i, j in zip(ogStr, reStr):
    if(i!=j):
        wrong+=1
    else:
        right+=1
        
diff = reTime - ogTime ##this is  in seconds 

##print("right:",right)
##print("wrong:", wrong)
##print("length:",length)
##print("ogTime:", ogTime)
##print("reTime:", reTime)

print("Accuracy = ", ((right/length)*100))
print("Estimated words per minute = ", (len1/diff)*60)
        
