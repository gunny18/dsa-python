"""
- Given 2 string s and t, t is a valid anagram of s if t can be created by rearranging letters of s, each letter axactly
once and all letters must be used
- It will be lowercase english letters

Ex - eat, tea -> True
    dog, cat -> False

Approach 1:
    - sort s and t
    - Check of they are same
        - Yes -> anagram, else not
    - If t has n chars and s has m chars
        - Sort -> nlogn
    TC -> O(nlogn) + O(mlogm)

Approach 2:
    - Store frequency maps for each char of s and t
    - Compare the frequency maps
    - TC -> O(25) + O(25) + O(len(s)) + O(len(t)) + O(26)
        ~ O(len(s)) + O(len(t))
    - SC -> O(25) + O(25)
        ~ O(1)

Approach 3: [APPROACH ASSUMPTION WRONG]
    - We know its going to be english lower case chars
    - If its a anagram
        - Sum of ASCII of s = Sum of ASCII of t
    - If its not same length it cannot be anagram
    - So we need to iterate only for O(len(s) or len(t))

    TC -> O(n) + O(m) [Checking length]
        -> O(len(s) or len(t))
        ~ 2xO(n)
    SC -> O(1)
    - Arguably better right ?

    WILL NOT WORK
        - I assumed every unique ascii sum will lead to unique values
        - Assumption is false
        Simple case, say sum is 300
            - 100 + 100 + 100
            - 99 + 102 + 99
            - Analogy is even diff chars can combine to for same ascii sums
            - IT IS NOT UNIQUE
"""

def frequency_map(s, t):
    freq_s = [0 for _ in range(ord('z')-ord('a')+1)]
    freq_t = [0 for _ in range(ord('z')-ord('a')+1)]

    for i in range(0, len(s)):
        freq_s[ord(s[i])-ord('a')] += 1

    for i in range(0, len(t)):
        freq_t[ord(t[i])-ord('a')] += 1
    
    for i in range(0, ord('z')-ord('a')+1):
        if freq_t[i] != freq_s[i]:
            return False
    
    return True

def ascii_sum(s,t):
    if len(s) != len(t):
        return False
    ascii_sum_s = 0
    ascii_sum_t = 0
    for i in range(0, len(s)):
        ascii_sum_s += ord(s[i])
        ascii_sum_t += ord(t[i])
    return ascii_sum_t == ascii_sum_s


print(frequency_map("anagram","nagaram"))
print(frequency_map("cat","dog"))

print(ascii_sum("anagram","nagaram"))
print(ascii_sum("cat","dog"))
print(ascii_sum("bdf","cde"))