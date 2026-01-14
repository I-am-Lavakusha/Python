def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

string_a = "Listen"
string_b = "Silent"

if are_anagrams(string_a, string_b):
    print(f"'{string_a}' and '{string_b}' are anagrams.")
else:
    print(f"'{string_a}' and '{string_b}' are not anagrams.")