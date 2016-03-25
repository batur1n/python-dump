import sys
s = "Hot sUn BEATIng dOWN bURNINg mY FEet JuSt WalKIng arOUnD HOt suN mAkiNG me SWeat"
# s = "I canT DAnCE i CANt TAlK Hey"    #Input string
print "Input: ", s
s = ''.join(s.split(' '))
s = [s[i:i+5] for i in range(0, len(s), 5)]
j, new = 0, []
new2, new3 = '', ''

for x in s:
    if len(x) == 5:
       new.append(x)
s = ' '.join(new)

for y in s:
    if y.isupper() == True:
       new2 = new2 + 'b'
    elif y.islower() == True:
       new2 = new2 + 'a'
    else:
       new2 = new2 + ' '
s = new2.split(' ')
code = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for z in s:
    ind = code.index(z)  
    new3 = new3 + alphabet[ind]
print "Output: ", new3
