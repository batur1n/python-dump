def length(s):
    lw = s.split(' ')
    longest = ''
    for i in lw:
        if len(str(i)) > len(str(longest)):
           longest = str(i)
    return longest

print(length('afbaf adfbfdgadfg adfg adfg adfg fg'))
print(length('sdfsaf dfdsfe sdf sdf fdfd safsadfasf'))
print(length('sdafasfdasd dff dfsassa fdfd'))
