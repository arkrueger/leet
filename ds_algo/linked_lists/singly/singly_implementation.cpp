// passes all tests

// https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
// Made while working through Leetcode's data structures curriculum

#include <iostream>
using namespace std;

class MyListNode {
 private:
  int val;
  MyListNode *next;

 public:
  MyListNode(int _val, MyListNode *_next = nullptr) {
    val = _val;
    next = _next;
  }

  void setVal(int _val) {
    val = _val;
  }

  int getVal() {
    return val;
  }

  void setNext(MyListNode *_next) {
    next = _next;
  }
  MyListNode *getNext() {
    return next;
  }
};

class MyLinkedList {
 private:
  MyListNode *head;

  MyListNode *getNodeAtIndex(int index) {
    MyListNode *currentNode = head;
    for (int i = 0; i < index; i++) {
      currentNode = currentNode->getNext();
    }
    return currentNode;
  }

 public:
  // If we want to initialize from an existing node
  MyLinkedList(MyListNode *_head = nullptr) {
    head = _head;
  }

  int get(int index) {
    // using indexIsValidToDelete because it checks if a node exists at that index
    if (indexIsValidToDelete(index)) {
      int val = getNodeAtIndex(index)->getVal();
      cout << to_string(val) + "\n";
      return val;
    } else {
      return -1;
    }
  }

  void addAtHead(int val) {
    // create the new node
    MyListNode *node = new MyListNode(val);
    // if head doesn't exist yet, then point head to the node
    if (!head) {
      head = new MyListNode(val);
      // cout << "head didn't exist, creating a new head. Head is " + to_string(head->getVal()) + "\n";
    } else {
      // if head does exist, then point the new node to head, and set the new node as head
      MyListNode *newHead = new MyListNode(val, head);
      head = newHead;
    }
  }

  MyListNode *getTail() {
    // if head doesn't exist yet, return nullptr
    if (!head) {
      return nullptr;
    }
    MyListNode *currentNode = head;
    while (currentNode->getNext()) {
      currentNode = currentNode->getNext();
    }
    return currentNode;
  }

  int getLength() {
    MyListNode *currentNode = head;
    int length = 1;  // length will be at least 1, unless current node is empty
    // if head is empty, our length is zero and we return early
    if (!currentNode) {
      return 0;
    }

    while (currentNode->getNext()) {
      currentNode = currentNode->getNext();
      length++;
    }
    return length;
  }

  bool indexIsValidToAdd(int index) {
    int length = getLength();
    bool isValid = ((index >= 0) && (index <= length));
    cout << "The index " + to_string(index) + " is " + (isValid ? "valid" : "out of bounds") + ". The length is " + to_string(length) + "\n";
    return isValid;
  }
  bool indexIsValidToDelete(int index) {
    int length = getLength();
    bool isValid = ((index >= 0) && (index < length));
    cout << "The index " + to_string(index) + " is " + (isValid ? "valid" : "out of bounds") + ". The length is " + to_string(length) + "\n";
    return isValid;
  }

  void addAtTail(int val) {
    // create new node, find tail, point tail to new node
    MyListNode *node = new MyListNode(val);
    MyListNode *tail = getTail();
    // if tail is empty, then head is empty, so just add at head and return
    if (!tail) {
      addAtHead(val);
      return;
    }
    // otherwise, add at tail
    tail->setNext(node);
  }

  void addAtIndex(int index, int val) {
    // find prev and next, point prev to new node, point new node to next
    // check if the index is valid, if not, return
    if (!indexIsValidToAdd(index)) {
      return;
    }
    // if head doesn't exist yet, just add it at head and return
    if (!head) {
      addAtHead(val);
      return;
    }
    // if the length is less than two, we don't want to mess around with "prev" and "next"
    if (getLength() < 2) {
      if (index == 0) {
        addAtHead(val);
        return;
      } else {  // if the index is valid, not 0, and the length is under 2, then the index is 1
        MyListNode *node = new MyListNode(val);
        head->setNext(node);
        return;
      }
    }
    // if none of the corner cases are true:
    // find prev and next
    MyListNode *prev = getNodeAtIndex(index - 1);
    MyListNode *next = prev->getNext();
    // make the new node
    MyListNode *node = new MyListNode(val, next);
    // point prev to the new node
    prev->setNext(node);
  }

  void deleteAtHead() {
    if (head) {
      MyListNode *next = head->getNext();
      MyListNode *oldHead = head;
      head = next;
      delete oldHead;
    }
  }
  void deleteAtIndex(int index) {
    // check if the index is valid, if not, return
    if (!indexIsValidToDelete(index)) {
      return;
    }
    // if there is only 1 node, don't bother getting the previous (it doesn't exist)
    // just delete the node and return
    if (getLength() < 2) {
      MyListNode *oldHead = head;
      head = nullptr;
      delete oldHead;
      return;
    }

    // if we're trying to delete at index 0, we can't get the previous
    if (index == 0) {
      deleteAtHead();
      return;
    }
    // if none of the corner cases were valid, then:
    // find prev and next, point prev to next
    MyListNode *prev = getNodeAtIndex(index - 1);
    MyListNode *deleted = prev->getNext();
    MyListNode *next = deleted->getNext();
    // point prev to next
    prev->setNext(next);
    // clean up deleted
    delete deleted;
  }

  void printNode(MyListNode *node) {
    cout << to_string(node->getVal()) + (node->getNext() ? " , " : " end");
  }

  void printList() {
    cout << "List: ";
    MyListNode *currentNode = head;
    if (head) {
      do {
        printNode(currentNode);
        currentNode = currentNode->getNext();
      } while (currentNode);
      cout << "\n";
    }
  }
};

int main() {
  MyLinkedList *myLinkedList = new MyLinkedList();
  cout << "head 5\n";
  myLinkedList->addAtHead(5);
  myLinkedList->printList();
  cout << "index 1,2\n";
  myLinkedList->addAtIndex(1, 2);
  myLinkedList->printList();
  cout << "get 1\n";
  myLinkedList->get(1);
  myLinkedList->printList();

  // cout << "index 0, 10\n";
  // myLinkedList->addAtIndex(0, 10);
  // myLinkedList->printList();
  // cout << "index 0, 20\n";
  // myLinkedList->addAtIndex(0, 20);
  // myLinkedList->printList();
  // cout << "index 1, 30\n";
  // myLinkedList->addAtIndex(1, 30);
  // myLinkedList->printList();
  // cout << "get 0\n";
  // myLinkedList->get(0);
  // myLinkedList->printList();

  // cout << "head 1\n";
  // myLinkedList->addAtHead(1);
  // myLinkedList->printList();
  // cout << "tail 3\n";
  // myLinkedList->addAtTail(3);
  // myLinkedList->printList();
  // cout << "index 1, 2\n";
  // myLinkedList->addAtIndex(1, 2);
  // myLinkedList->printList();
  // cout << "get 1\n";
  // myLinkedList->get(1);
  // myLinkedList->printList();
  // cout << "delindex 0\n";
  // myLinkedList->deleteAtIndex(0);
  // myLinkedList->printList();
  // cout << "get 0\n";
  // myLinkedList->get(0);
  // myLinkedList->printList();

  // cout << "head 7\n";
  // myLinkedList->addAtHead(7);
  // myLinkedList->printList();
  // cout << "head 2\n";
  // myLinkedList->addAtHead(2);
  // myLinkedList->printList();
  // cout << "head 1\n";
  // myLinkedList->addAtHead(1);
  // myLinkedList->printList();
  // cout << "index 3, 0\n";
  // myLinkedList->addAtIndex(3, 0);
  // myLinkedList->printList();
  // cout << "delindex 2\n";
  // myLinkedList->deleteAtIndex(2);
  // myLinkedList->printList();
  // cout << "head 6\n";
  // myLinkedList->addAtHead(6);
  // myLinkedList->printList();
  // cout << "tail 4\n";
  // myLinkedList->addAtTail(4);
  // myLinkedList->printList();
  // cout << "get\n";
  // myLinkedList->get(4);
  // myLinkedList->printList();
  // cout << "head 4\n";
  // myLinkedList->addAtHead(4);
  // myLinkedList->printList();
  // cout << "index 5, 0\n";
  // myLinkedList->addAtIndex(5, 0);
  // myLinkedList->printList();
  // cout << "head 6\n";
  // myLinkedList->addAtHead(6);
  // myLinkedList->printList();
  return 0;
}