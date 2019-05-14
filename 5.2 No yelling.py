'''
Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. 
String should be capitalized and properly spaced. Using re and string is not allowed.
'''

def filter_words(st):
  return(" ".join(str(st[0].upper()+st[1:len(st)+1].lower()).split()))
  
def filter_words(st):
    return ' '.join(st.capitalize().split())
