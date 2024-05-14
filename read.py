import re
def resolveTime(regex, originalMessage):
    r = re.compile(regex)
    p = r.match(originalMessage)
    m = p.group().strip("#!")
    try:
        if m.endswith("d"):
            y = m.strip("d")
            #print(y)
            f = int(y) * 60 * 60 * 24
            return f
        if m.endswith("h"):
            y = m.strip("h")
            f = int(y) * 60 * 60
            return f
        if m.endswith("m"):
            y = m.strip("m")
            f = int(y) * 60
            return f
        if m.endswith("s"):
            y = m.strip("s")
            f = int(y)
            return f    
    except:
        print("An invalid type was entered.")
    
    

