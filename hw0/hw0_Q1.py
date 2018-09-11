import numpy
import PIL
import os
#print(os.listdir())
os.chdir(r'C:\Users\M10609309\PYTHON_ALL\ML2017FALL_HomeWork\hw0')

def AllWord(text):
    all_text=[]
    for a in range(len(text)):
        exist=False
        for b in range(len(all_text)):
            if all_text[b]==text[a]:
                exist=True
        if exist==False:
            all_text.append(text[a])
    return all_text
            
def CountWord(all_text,text):
    text_count=[]
    for a in range(len(all_text)):
        text_count.append(0)
        for b in range(len(text)):
            if (all_text[a]==text[b]):
                text_count[a]+=1
    return text_count

def CountWord_2(all_text,text):
    text_count=[]
    for a in range(len(all_text)):
        text_count.append(text.count(all_text[a]))
    return text_count

f=open('words.txt','r', encoding = 'UTF-8')
text=f.read()
text_g=text.split(" ")
print("GET eords.txt: ",text)
all_text=AllWord(text_g)
text_count=CountWord_2(all_text,text_g)

for i in range(len(all_text)):
    print(all_text[i],i,text_count[i]  ) 
