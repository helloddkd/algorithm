
def reverse_string(string):
    string = list(string)
    for i in range(len(string)//2):
        string[i], string[-i-1] = string[-i-1], string[i]
    return "".join(string)
print(reverse_string('strrt'))