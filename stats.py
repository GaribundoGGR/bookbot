def count_words(file_text):
    x = file_text.split()
    result = len(x)
    return result

def count_character(file_text):
    final_dict = {}
    char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lower_case = file_text.lower()
    y = lower_case.split()
    for i in y:
        for x in i:
            for h in range (len(char_list)):
                if x == char_list[h]:
                    count_list[h] += 1
    
    for h in range (len(char_list)):
        final_dict[char_list[h]] = count_list [h]
    
    return final_dict

def sort_greater(dict):
    return dict["num"]

def sorting(dict):
    sorted = []
    for i in dict:
        sorted.append({"char":i,"num":dict[i]})
    sorted.sort(key=sort_greater, reverse=True)
    return sorted

