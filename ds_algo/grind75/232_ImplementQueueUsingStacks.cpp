/*
stack flushing approach:
    have two stacks
    one "input" and one "output"
    all pushing is done on the input stack
    but what happens when we need to pop or peek the queue?
        the output queue has the opposite order of the input stack 
            (therefore popping the output stack obeys FIFO)
        -> if the output stack has elements, pop or peek the output stack
        -> if the output stack is empty, then transfer the whole input stack into the output stack
                this will put that part of the queue in FIFO order in the output stack
                nothing will be pushed onto the output stack until it is empty (this prevents
                    it from going out of order)
*/


class MyQueue {
public:
    stack<int> in;
    stack<int> out;
    
    MyQueue() {
        
    }
    
    void push(int x) {
        // push into the FIFO queue -> push onto input stack
        in.push(x);
    }
    
    int pop() {
        // use output stack
        // peek already does the needful when the output stack is empty, so use peek before popping
        int top = peek();
        // now that peek has filled the output stack if applicable, pop the output stack
        out.pop();
        return top;
    }
    
    int peek() {
        // use output stack
        // if output stack is empty, move input stack over
        if(out.empty()) {
            while(!in.empty()) {
                out.push(in.top()); // push top of input stack onto output stack
                in.pop(); // shave off the top of input stack
            }
        }
        return out.top();
    }
    
    bool empty() {
        return in.empty() && out.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */