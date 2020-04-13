from collections import defaultdict

def groupAnagrams( strs):
    out = defaultdict(list)
    for x in strs:
        so = ''.join(sorted(x))
        out[so].append(x)
    return list(out.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))