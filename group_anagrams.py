from typing import List

import collections

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs: List[str])->List[List[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        #print(sorted(word))
        #print(''.join(sorted(word)))
        anagrams[''.join(sorted(word))].append(word)
        #print(anagrams)
        #print(anagrams.values())
    return list(anagrams.values())

print(groupAnagrams(strs))