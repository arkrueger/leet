"""
clarify and understand problem
think about / write out constraints and edge cases
think about an approach, start with brute force
give s-t analysis
get interviewer buy-in
implement solution
run test cases/debug (without being prompted)
verify solution with interviewer

"""

"""
thinking:
  
  we don't know how many times 26 was subtracted
    -> we end up with a bunch of options, maybe a tree datastructure?
  
  for the first letter
    b - z
    z -> A subtract 26 -> a
    
  
  input will only be lowercase

approach:
  
  start with word[0]
  loop over word:
    word[i]
  
  
//
// d	n	o	t	q
  // 99  
 100   have 110
     need 114
  
// 110 - 100

110 - 100 gives us 10
add 26 until we are in the range of 97-122
10 -> 36 -> 62 -> 88 -> 114 bingo 
just to explore: 114 - 97 = 17
does 26 % 10 + 1 give us the offset? maybe. let's keep going
111 - 110 = 1
1 -> 27 -> etc -> 105 bingo
111 - 110
"""


# ord('a') -> ascii a

def decrypt(word):
  if not word:
    return ""
  decrypted = []
  firstChar = ord(word[0])-1 if ord(word[0]) <= ord("z") else ord("a") # wrap back around if the encryption pushed the first char beyond z
  decrypted.append(chr(firstChar))
  for i, c in enumerate(word[1:]):
    p = word[i]
    d = ord(c) - ord(p)
    while d < 97:
      d += 26
    decrypted.append(chr(d))
  return "".join(decrypted)
