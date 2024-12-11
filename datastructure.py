### String Operations

# 1. Reverse a String
def reverse_string(s):
    return s[::-1]

# 2. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 3. Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. Check Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 5. Find Substring Occurrences
def find_substring_occurrences(s, sub):
    return [i for i in range(len(s) - len(sub) + 1) if s[i:i+len(sub)] == sub]

# 6. Basic String Compression
def string_compression(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return ''.join(compressed)

# 7. Check Unique Characters
def has_all_unique_chars(s):
    return len(s) == len(set(s))

# 8. Case Conversion
def convert_case(s, to_upper=True):
    return s.upper() if to_upper else s.lower()

# 9. Count Words in a String
def count_words(s):
    return len(s.split())

# 10. Concatenate Strings Without + Operator
def concatenate_strings(s1, s2):
    return "".join([s1, s2])

### List Operations

# 11. Remove All Occurrences from List
def remove_all_occurrences(lst, element):
    return [x for x in lst if x != element]

# 12. Find Second Largest Number
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# 13. Count Element Occurrences
def count_elements(lst):
    from collections import Counter
    return dict(Counter(lst))

# 14. Reverse List In-Place
def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

# 15. Remove Duplicates While Preserving Order
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 16. Check Sorted List
def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

# 17. Merge Sorted Lists
def merge_sorted_lists(lst1, lst2):
    from heapq import merge
    return list(merge(lst1, lst2))

# 18. Find Intersection of Lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 19. Union of Lists Without Duplicates
def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

# 20. Shuffle a List Randomly
def shuffle_list(lst):
    import random
    shuffled = lst[:]
    for i in range(len(shuffled)):
        swap_idx = random.randint(0, i)
        shuffled[i], shuffled[swap_idx] = shuffled[swap_idx], shuffled[i]
    return shuffled

### Tuple Operations

# 21. Common Elements in Tuples
def common_elements_in_tuples(t1, t2):
    return tuple(set(t1) & set(t2))

# 22. Prompt for Sets and Find Intersection
def sets_intersection():
    set1 = set(map(int, input("Enter first set of integers, separated by commas: ").split(',')))
    set2 = set(map(int, input("Enter second set of integers, separated by commas: ").split(',')))
    return set1 & set2

# 23. Concatenate Tuples
def concatenate_tuples(t1, t2):
    return t1 + t2

# 24. Tuple Range Extraction
def tuple_range_extraction(t, start, end):
    return t[start:end]

# 25. Tuple Max and Min
def tuple_max_min(t):
    return max(t), min(t)

# 26. Count Tuple Element Occurrences
def count_tuple_element(t, element):
    return t.count(element)

### Set Operations

# 27. Set Difference
def set_difference(set1, set2):
    return set1 - set2

# 28. Set Union, Intersection, and Difference
def set_operations(set1, set2):
    return {
        'union': set1 | set2,
        'intersection': set1 & set2,
        'difference': set1 - set2
    }

# 29. Set Symmetric Difference
def symmetric_difference(set1, set2):
    return set1 ^ set2

# 30. Character Union in Sets
def char_union(set1, set2):
    return set1 | set2

### Dictionary Operations

# 31. Word Frequency Count
def word_frequency(words):
    from collections import Counter
    return dict(Counter(words))

# 32. Merge Dictionaries
def merge_dictionaries(d1, d2):
    from collections import Counter
    merged = Counter(d1) + Counter(d2)
    return dict(merged)

# 33. Access Nested Dictionary Value
def access_nested_dict(d, keys):
    for key in keys:
        d = d.get(key, None)
        if d is None:
            return None
    return d

# 34. Sort Dictionary by Values
def sort_dict_by_values(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# 35. Invert Dictionary
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted
