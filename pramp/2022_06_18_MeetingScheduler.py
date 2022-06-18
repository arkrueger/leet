### Pramp practice interview ###

"""
timestamp

5 		understand problem and constraints
10 		pseudocode
15 		first implementation (first hint if unsuccessful)
20		if applicable, follow-up question (second hint otherwise)
30		if applicable, finished follow-up implementation
"""
"""
thinking:
  
  if any interval is shorter than the duration, then ignore than interval
  max(slotA start, slotB start) <= max(slotA start, slotB start) + dur <= min(slotA end, slotB end)
  
approach:
  
  iterative:
    
"""
# iterative brute force
# T: O(n^2)
# S: O(1)
def __meeting_planner(slotsA, slotsB, dur):
  for a in slotsA:
    for b in slotsB:
      laterStart = max(a[0], b[0])
      earlierEnd = min(a[1], b[1])
      compatible = laterStart <= laterStart + dur <= earlierEnd
      if compatible:
        return [laterStart, laterStart + dur]
  return []
  
# iterative, smarter
# T: O(n) because we only compare compatible slots, not n*n slots
# S: O(1)
def meeting_planner(slotsA, slotsB, dur):
  a = 0 # slotA index
  b = 0 # slotB index
  while a < len(slotsA) and b < len(slotsB):
    aEnd, bEnd = slotsA[a][1], slotsB[b][1]
    aStart, bStart = slotsA[a][0], slotsB[b][0]
    # make sure we have potentially compatible overlap
    if aEnd < bStart: # we need to move a forward
      a += 1
      continue
    if bEnd < aStart: # we need to move b forward
      b += 1
      continue
    # assess whether the current overlap satisfies the duration requirement
    laterStart = max(aStart, bStart)
    earlierEnd = min(aEnd, bEnd)
    compatible = laterStart <= laterStart + dur <= earlierEnd
    if compatible:
      return [laterStart, laterStart + dur]
    if bEnd < aEnd:
      b += 1
      continue
    if aEnd < bEnd:
      a += 1
      continue
  return []
