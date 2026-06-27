"""
- Given a string, return the characters sorted by highest frequency.
- In case characters have same frequcny, sort them in alphabetic order
- Letters will be lower case alphabets

Approach:
    - Build a frequency hash map for lower case case letters
    - Update the frequencies
    - Sort the hashmap based on frequencies highest to lowest.
        - But if they are sorted, we cannot find for which alphabet they are the counts
        - So in hash map, instead of counts store [count, 'alphabet']
        - So even after sorting we still can access the alphabet
        - Sort comparator
            - We need to ensure we write the sort comparatpr logic properly
                - Sort first by counts
                - If counts equal, by alphabetic order
    - Now traverse the sorted hashmap and put the characters in array (Until o count elements)

    - TC
        - O(26) + O(len(string)) + O(nlogn) -> Sort
    - SC -> O(26) + O(len(string))
"""


def sorted_by_frequency(s):
    freq_map = [[0, chr(ord('a')+i)] for i in range(0, ord('z')-ord('a')+1)]

    for i in range(0, len(s)):
        freq_map[ord(s[i]) - ord('a')][0] += 1

    
    # Sorts first by count x[0] in ascending
    # If x[0] equal, sorts by character x[1] ascending -> Alphabetically
    # sorted_freq_map = sorted(freq_map,key=lambda x: (x[0], x[1]))

    # If we need to sort by count in descending, but if qual, by character, alphabetically
    sorted_freq_map = sorted(freq_map,key=lambda x: (-x[0], x[1]))

    sorted_chars = [char[1] for char in sorted_freq_map if char[0] != 0]

    return sorted_chars


print(sorted_by_frequency("tree"))
print(sorted_by_frequency("raaaji"))
print(sorted_by_frequency("bbccddaaa"))