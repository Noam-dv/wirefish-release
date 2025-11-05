from collections import deque
# file for publically acsesing the list of packets type shit
# made this when starting project, thought it would be way more complex so i thought this could help organization
# but ill just leaev it cuz it works
ls = deque(maxlen=1000)

def cap_list():
    return ls