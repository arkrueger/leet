/*
thoughts:
    push/pop/top in constant time is expected in a stack
        but getting the minimum element isn't as it would require searching
approach: (both of these are from the forum)
    two stacks:
        conceptual basis behind this approach is that you want two stacks of equal length
            one stores the stack values, the other stores the mins corresponding to each stack value
            it's important that that phrase is interpreted the right way
            if we have a stack that looks like
                top- 3, 1, 2, 5 -bottom  then our mins stack must make sense as we pop off the tops
                top- 1, 1, 2, 5 -bottom  would be our mins stack
            in other words, as we push values onto the actual stack, we check if they are < mins.top
            if they are, we push the value onto mins stack as well
            if they are not, we push the current min onto the mins stack
            this keeps the mins stack and values stack synced
            now whenever we pop the values stack, we also pop the mins stack to keep them in sync
    
    one stack:
        conceptual basis behind this approach is pretty similar to the two stack approach
            really it's the same as the two stack approach, but instead of having two stacks
            we have one stack with 2-d elements (each element is a pair of ints)
            this pair of its contains the value, and the min value in the stack when that pair is
            at the top of the stack
            
*/

// One stack approach
// this is actually slower than the two stack approach
class MinStack {
    public:
    stack<pair<int, int>> vals; // to access the pair, use .first and .second
    
    MinStack() {
        
    }
    
    void push(int val) {
        int min; // current min
        // if empty, set min to val. otherwise, check if val is less than top's min
        if(vals.empty()) {
            min = val;
        } else if(val < vals.top().second) {
            min = val;
        } else {
            min = vals.top().second;
        }
        
        vals.push({val, min}); // push val and its min onto the stack
    }
    
    void pop() {
        vals.pop();
    }
    
    int top() {
        return vals.top().first;
    }
    
    int getMin() {
        return vals.top().second;
    }
};

// Two stacks approach
/*
class MinStack {
public:
    stack<int> vals;
    stack<int> mins;
    
    MinStack() {
        
    }
    
    void push(int val) {
        // just push the value if mins is empty
        if(mins.empty()) { 
            mins.push(val);
        } else if(val < mins.top()) { // otherwise, check if the val is a new min
            mins.push(val);            
        } else {  // if neither, push current min
            mins.push(mins.top());
        }
        
        // always push the val onto vals
        vals.push(val);
        
    }
    
    void pop() {
        // vals and mins should be of equal length always so no need to check for empty
        vals.pop();
        mins.pop();
    }
    
    int top() {
        return vals.top();
    }
    
    int getMin() {
        return mins.top();
    }
};
*/


/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
