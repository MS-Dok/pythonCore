'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
'''
def areYouPlayingBanjo(name):
    return (name+" plays banjo" if name[0].lower()=="r" else name+" does not play banjo")
