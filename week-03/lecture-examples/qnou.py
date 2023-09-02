#!/usr/bin/env python3

def qnou(s):
    s = s.replace("qu", "--")

#    if "q" in s:
#        return True
#    else:
#        return False

    return "q" in s # return whether q is in s


low = ["quiet", "quietq", "Quiet", "IRAQ"]

# first argument is what you want to add to the list, then the thing that you iterating through,
# then the condition for adding the element to the list.
qnous = [w for w in low if(qnou(w.lower()))]

print(qnous)
