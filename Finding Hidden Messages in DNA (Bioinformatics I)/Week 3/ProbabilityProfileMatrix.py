def Pr(Text, Profile):
    p = 1
    # loop through each index(char) in text
    for index,char in enumerate(Text):
        for key, profile_lists in sorted(Profile.items()):
            if char == key:
                p *= profile_lists[index]
    return p

profile = {'A': [0.4,  0.3,  0.0,  0.1,  0.0,  0.9],
           'T': [0.3,  0.1,  0.0,  0.4,  0.5,  0.0],
           'G': [0.1,  0.3,  1.0,  0.1,  0.5,  0.0],
           'C': [0.2,  0.3,  0.0,  0.4,  0.0,  0.1]}
text = "TCGGTA"

print(Pr(text, profile))