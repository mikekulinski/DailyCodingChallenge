#include <cassert>
#include <iostream>

using namespace std;

typedef struct XOR_Node {
  XOR_Node *both_;
  int value_;

  XOR_Node(int value) : value_(value) { both_ = NULL; }

  ~XOR_Node() {}

} XOR_Node;

XOR_Node *XOR(XOR_Node *prev, XOR_Node *next) {
  return (XOR_Node *)((intptr_t)prev ^ (intptr_t)next);
}

class XOR_List {
 public:
  XOR_Node *head;
  XOR_Node *tail;
  int length;

  XOR_List() {
    head = NULL;
    tail = NULL;
    length = 0;
  }

  ~XOR_List() {
    XOR_Node *current = head;
    XOR_Node *prev = NULL;
    XOR_Node *next;
    while (current != NULL) {
      next = XOR(current->both_, prev);
      prev = current;
      delete current;
      current = (XOR_Node *)next;
    }
  }

  void add(int value) {
    XOR_Node *node = new XOR_Node(value);

    if (length == 0) {
      node->both_ = NULL;
      head = node;
      tail = node;
    } else {
      tail->both_ = XOR(tail->both_, node);
      node->both_ = XOR(tail, NULL);
      tail = node;
    }
    length++;
  }

  XOR_Node *get(int index) {
    if (index >= length) {
      return NULL;
    }

    XOR_Node *current = head;
    XOR_Node *prev = NULL;
    XOR_Node *next;
    int i = 0;
    while (i < index) {
      next = XOR(current->both_, prev);
      prev = current;
      current = (XOR_Node *)next;
      i++;
    }

    return current;
  }
};

int main(int argc, char const *argv[]) {
  XOR_List *list = new XOR_List();

  list->add(1);
  list->add(2);
  list->add(3);

  XOR_Node *node = list->get(1);
  cout << node->value_ << endl;

  delete list;

  return 0;
}
