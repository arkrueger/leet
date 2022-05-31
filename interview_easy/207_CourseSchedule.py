"""
thinking:
    on the surface from the two test cases,
        it looks like prereqs are incompatible when order is not preserved
        since we could have a large number of prereq pairs, it might be useful to construct a "main schedule" that produces a timeline of courses to be taken
        we can return True if we are able to construct this timeline successfully
        we can return False if we are unable to place a course
        how will we know if a course placement breaks the rules?
            let's say we have placement [ [0, 3], [3, 5], [5, 0] ]
            we would construct the timeline like this:
                0, 3
                0, 3, 5 (we know 5 has to come after 3 and 5 does not already exist in the list)
                0, 3, -> we found 5 in the list, which is after 0, but the current prereqs say it must come before 0
                so we'll make the determination by asking for each placement (in this case 5),
                    is 5 in a similar position (before or after) relative to its prereq (0) in the timeline as it is in the placement array? in this case, we see that 5 comes after 0 in the constructed timeline, but our current prereq says it should be before 5, so we know that this course set is impossible
        
approach:
    this doesn't work because it doesn't account for unconnected (e.g. [9, 10], [1, 2]) courses
        construct timeline:
            for each in placements, place the two courses in the timeline
                if a course doesn't exist yet, then place it in a location that preserves its prereq order
                if both courses are already in the timeline, check if the relative order in the timeline matches the prereq order 
                    if it doesn't, return False
            if we are able to complete the timeline-building loop and its length is < numCourses, return True

    post-order DFS:
        official leetcode solution
        
        
"""

# postorder dfs - leetcode solution
# T: O()
# S: O()
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        courseDict = defaultdict(list)
        for req in prerequisites:
            nextCourse, prevCourse = req[0], req[1]
            courseDict[prevCourse].append(nextCourse)
        # set up our breadcrumb lists
        checked = [False] * numCourses
        visited = [False] * numCourses
        # check each node
        for currCourse in range(numCourses):
            if self.hasCycle(currCourse, courseDict, checked, visited):
                return False
        return True
    
    def hasCycle(self, currCourse, courseDict, checked, visited):
        if checked[currCourse]:
            return False
        if visited[currCourse]:
            return True
        visited[currCourse] = True # mark current node as visited
        res = False # innocent until proven guilty
        for nxt in courseDict[currCourse]: # loop over courses that can be taken after current
            res = self.hasCycle(nxt, courseDict, checked, visited)
            if res: break
        visited[currCourse] = False # clear current "cycle check" breadcrumbs
        checked[currCourse] = True # leave a breadcrumb so we know if we checked this (if we did check it and we didn't already return false, then we know that there cannot be a cycle off of currCourse so we don't need to check a second time)
        return res


# backtracking (if directed acyclic graph good, if cycles bad)
# recreated official leetcode solution
# T: O(e + v^2) where e is number of dependencies, v is numCourses
# S: O(e + v)
class __Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        courseDict = defaultdict(list)
        # build the adjacency list
        for req in prerequisites:
            nextCourse, prevCourse = req[0], req[1]
            courseDict[prevCourse].append(nextCourse)
        
        visited = [False] * numCourses # track which nodes were visited while searching for cycles
        # check each course for prereq cycles
        for currCourse in range(numCourses):
            if self.hasCycle(currCourse, courseDict, visited):
                return False
        return True # good to go if we didn't find any cycles
    
    # helper to detect a cycle from currentCourse
    # relies on the adjacency list contained in courseDict
    # uses visited to breadcrumb visited courses (DP?)
    def hasCycle(self, currCourse, courseDict, visited):
        if visited[currCourse]: # return True if we already visited this course
            return True
        visited[currCourse] = True # mark the course visited
        # backtracking
        res = False
        for nxt in courseDict[currCourse]: # loop over the list of next courses that can be taken after this course
            res = self.hasCycle(nxt, courseDict, visited)
            if res:
                break
        # now that we're done backtracking (the recursive calls branching out from here have returned)
        # -> we can remove the breadcrumb (we don't want to interfere with the next "hasCycle" call)
        visited[currCourse] = False
        return res



# bad solution, didn't finish
"""
class __Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        timeline = []
        for p in prerequisites:
            f, s = p[0], p[1] # course to take first, course to take second
            if f in timeline and s in timeline:
                if timeline.index(f) > timeline.index(s):
                    # if the existing timeline disagrees with the current prereq rules, game over
                    return False
            if f in timeline and s not in timeline:
                pass # we'll need to break at the end of this
            if s in timeline and f not in timeline:
"""
