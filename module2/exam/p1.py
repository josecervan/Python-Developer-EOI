def is_anagram(s1, s2):
    """
    :param s1: string 1
    :param s2: string 2
    :return: boolean value (are they anagrams?)
    """
    return ''.join(sorted(s1.lower())) == ''.join(sorted(s2.lower()))


print(is_anagram('tea', 'eat'))
print(is_anagram('tea', 'treat'))
print(is_anagram('sinks', 'skin'))
print(is_anagram('Listen', 'silent'))
