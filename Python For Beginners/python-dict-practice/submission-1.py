from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    #char_count = 0
    my_dict = {}
    for c in word:
        if (c in my_dict) == False:
            my_dict[c] = 1
        else:
            my_dict[c] += 1
    
    return my_dict
    pass




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
