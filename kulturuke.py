import random as rd

def kult(word, n):
    list = [word]  #Legger til orginalordet i starten
    while n > 0:
        temp = word
        nword = ""  #Det neste ordet
        while len(temp)>0: 
            r = rd.randint(0,len(temp)-1) #Velger hvilken bokstav som skal velges
            nword += temp[r] #Legger bokstaven til neste ord
            temp = temp[0 : r : ] + temp[r+1 : : ] #Fjerner bokstaven fra orginalordet
        list.append(nword) #Legger til det nye ordet
        n -= 1
    return list

for c in kult("vitnemålet", 15):
    print(c)