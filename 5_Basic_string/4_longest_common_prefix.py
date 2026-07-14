"""
- Given an array of string, find the longest common prefix.
- Ex -> ["flower","flow","flaw","flute"]
- Longest common prefix is "fl"

Approach 1:
    - Keep at string as base.
    - Compare it element by element with other strings (also element by element)
    - Keep building common prefix
    - Stop when it breaks

    - TC
        - Outer loop -> len of 1st string times (say m chars)
            - Inner loop, remaining strings (say n strings -> n-1)
        -> O(mx(n-1)) ~ O(mxn)

Approach 2:
    - Here we take analogy of dictionary.
    - All words appear in a sorted fashion.
    - So once sorted, we can say longest prefix, just by comparing, 1st and last string/word
    - All those in between are bound to have the same longest prefix

    - How long does sorting take ?
        - Considering we use the best sorting technique, its going to take O(nlog(n))

    - And comparing the 1st and last string, char by char
        - Worst case, m chars where m is number of chars in the smallest of the 2 strings.
    - O(m)
    - TC -> O(nlog(n)) + O(m)

    - Is this less than the TC of aproach 1 ?
        - Not always.
        - Because sorting involes a lot of comparisons, at character level
        - Imagine to get the dictionary level sorting, we need to sort at character level
        - Costly operation
        - Usuallly the horizontal scanning/brute force is more efficient in this case!
"""


def brute_force_approach(strs):
    if len(strs) == 1:
        return strs[0]
    prefix = ""
    initial = strs[0]
    for j in range(0, len(initial)):
        for i in range(1, len(strs)):
            if j >= len(strs[i]) or strs[i][j] != initial[j]:
                return prefix

        prefix += initial[j]

    return prefix


def sorted_longest_prefix(strs):
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    first = strs[0]
    last = strs[len(strs) - 1]

    i = 0
    prefix = ""
    while i < min(len(first), len(last)):
        if first[i] == last[i]:
            prefix += first[i]
            i += 1
        else:
            break
    return prefix


print(brute_force_approach(["flower", "flow", "flaw", "flute"]))
print(brute_force_approach(["dog", "cat", "animal", "monkey"]))

print(sorted_longest_prefix(["flower", "flow", "flaw", "flute"]))
print(sorted_longest_prefix(["dog", "cat", "animal", "monkey"]))
