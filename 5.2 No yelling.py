def filter_words(st):
  return(" ".join(str(st[0].upper()+st[1:len(st)+1].lower()).split()))
  
def filter_words(st):
    return ' '.join(st.capitalize().split())