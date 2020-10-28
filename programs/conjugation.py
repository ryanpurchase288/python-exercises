def dictionary():
    text_file = open("programs/words.txt", "r")
    words = text_file.read().split("\n")
    return words


def sub(word):
    sub_strings = [word[i: j] for i in range(len(word))
                   for j in range(i + 1, len(word) + 1)]
    return sub_strings


def main(string_):
    valid_subs = []
    all_subs = sub(string_)
    words = dictionary()

    for word in all_subs:
        if word.lower() in words and len(word.lower()) >=2:
            print(words)
    
            valid_subs.append(word)
            
            remove=word.lower()
          #  print(word.lower())
           # print(all_subs)
            #print('remove is',remove)
            for value in remove:
              string_=string_.replace(value,'')
              all_subs=sub(string_)
             # print('s is',string_)
    valid_subs = list(dict.fromkeys(valid_subs))
    
    return valid_subs


print(main('awesomeness'))