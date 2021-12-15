from typing import List
import re, collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split()
        if word not in banned]
    print(words)

    counts = collections.Counter(words)
    print(counts)
    print(counts.most_common())
    return counts.most_common(1)[0][0]

print(mostCommonWord(paragraph, banned))

