"""
- Given 2 strings (same length, only lowercase english letters), they are isomorphic if
    - We can get other word, using maps of characters of one word to another
- Example:
    s="egg", t="add"
        - e maps to a
        - g maps to d
        - g again maps to d
    - Using this we can get s from t and vice versa

    s="apple", t="bbnbm"
        - a->b
        - p->b - But b is already mapped to a
    So this is not isomorphic

Approach 1 - Using a hash map to store mappings
    - Hash indexes are what we will use to represent chars of t string
    - We will store what t string are mapped to
    Steps
        - Build hash map
            - Hash array from 97 to 122 (25 size array)
            - Empty "" initially
            - Iterate from 0 to len(s or t) [As len are same]
                - s[i] needs to be mapped to t[i]
                - Calc hash index using t[i]
                - If hashmap[hash index of t[i]] already has value, return false
                - If empty, put s[i]
            - Return true, in case loop already did not return false

            TC -> O(25) to build hashtable
                - O(len(s or t)) to iterate
                -> O(len(s or t)) + O(25)
            SC -> O(25)
    WHERE IT WENT WRONG ?
        - Above solution went wrong because we needed 2 hashmaps
        - One mapping s->t
        - Other mapping t->s
        - In above approach we used n=only t->s
Remember:
    - This works as problem clearly mentiones on lower case english letters
    - In case any character, logic remains sae, we just need a bigger hash table
    - Preferably a dictionary instead of an array as hashtable
"""

def compare_hashtable(s, t):
    s_to_t_hash_table = ["" for i in range(0, ord('z') - ord('a') + 1)]
    t_to_s_hash_table = ["" for i in range(0, ord('z') - ord('a') + 1)]
    
    for i in range(0, len(s)):
        hash_index_t = ord(t[i]) - ord('a')
        hash_index_s = ord(s[i]) - ord('a')

        # In case both hash maps are "", map them
        if (t_to_s_hash_table[hash_index_t] == "" and s_to_t_hash_table[hash_index_s] == ""):
            t_to_s_hash_table[hash_index_t] = s[i]
            s_to_t_hash_table[hash_index_s] = t[i]
        # If value exists and this time a diff value is trying to map
        elif (s_to_t_hash_table[hash_index_s] != t[i] or t_to_s_hash_table[hash_index_t] != s[i]):
            return False
        
    return True

print(compare_hashtable('egg','add'))
print(compare_hashtable('apple','bnbnm'))
print(compare_hashtable('paper','title'))
print(compare_hashtable('foo','bar'))

