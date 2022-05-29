class __Solution:
    def maxProduct(self, words: List[str]) -> int:
        # identify pairs that do not share letters
        hash = {} # dict of sets
        pairs = []
        for w in words:
            chars = set()
            for c in w:
                chars.add(c)
            hash[w] = chars
        for w1 in words:
            for w2 in words: 
                if w1 == w2: break
                for c in hash[w1]:
                    goodPair = True
                    if c in hash[w2]:
                        goodPair = False
                        break
                if goodPair:
                    pairs.append([len(w1),len(w2)]) # if the pair was compatible then add it
        product = 0
        for p in pairs:
            product = max(product, p[0]*p[1])
        
        return product

# found this one in the forum:
# BINARY MASK SOLUTION
""" 
it relies on casting the words to sets (note that "abc" and "aabbcc" produce the same set)
for each set, we can create a binary mask
    store this mask in a dict, using the mask as the *key* and the word length as the *value*
        again, abc and aabbcc appear identical here (same set -> same mask) so check if the key already exists in the dict and only store the longer length (since words are compatible based on their characters, if we can use abc then we can also use aabbcc, and aabbcc is longer so we'd rather use that to get a higher product)
    to reiterate, the process above took the words, generated sets, generated binary masks from those sets, and where the sets were identical, recorded only the longest word length for that set
    now that the dict is filled, two nested loops around the dict elements: (d[x] and d[y])
        if the masks evaluate to bitwise False (x & y):
            that means that the sets that produced the masks shared *no* letters in common -> they're compatible
            multiply the word lengths (d[x] * d[y]) and store in max if it is bigger than last recorded max
        the conditional above skips where x == y because their bitwise and will evaluate to True
    return the largest word length product
"""
class __Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - ord('a'))) # binary mask
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x]*d[y] for x in d for y in d if not x & y] or [0])
# again, but annotated:
class __Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {} # store key:value mask:wordlength here
        for w in words: # examine each word
            mask = 0 # reset the binary mask
            for c in set(w): # reduce the word to its unique components
                mask |= (1 << (ord(c) - ord('a'))) # binary mask
                # more on the binary mask:
                # mask |= means mask = mask | (etc), important: this is a bitwise or
                # (1 << x) means shift 1 bitwise left by x (and ord(c)-ord('a') turns char into a number)
                # mask will allow us to BOTH identify AND make a logical determination about the word's unique components
                # that is, two words that share NO characters will produce masks that evaluate to FALSE when compared by bitwise or -> mask1 ^ mask2 will be False (which indicates words we are allowed to pair)
            d[mask] = max(d.get(mask, 0), len(w)) # if the mask already exists, only update if current word is longer
        return max([d[x]*d[y] for x in d for y in d if not x & y] or [0]) # explanation below:
            # multiply the word lengths for every combination in the dict
            # but only if their hashes are compatible (x & y bitwise or is False)
            # return the max of the array, OR if the array is [empty], max of [0] -> 0

# again, but rewritten for readability        
class __Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                charval = ord(c) - ord('a') # convert char into a number
                shift = 1 << charval # use charval to shift 1 (i.e. convert its effect to binary)
                mask = mask ^ shift # add the new character to the mask
            if mask in d: # if mask is already in d, only overwrite if we found a longer word with that mask
                d[mask] = max(d[mask], len(w))
            else: # if mask isn't in d yet, add it with the value as word length
                d[mask] = len(w)
        # find the max
        maxProd = 0
        for x in d:
            for y in d:
                if x & y: # if the words share any letters
                    continue
                else:
                    maxProd = max(maxProd, d[x]*d[y])     
        if maxProd:
            return maxProd
        else:
            return 0
                
                
                
