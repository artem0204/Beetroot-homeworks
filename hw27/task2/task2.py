import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    p_stack = Stack()
    e_tree = BinaryTree("")
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fplist:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i.isdigit():
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ["+", "-", "/", "*", "and", "or"]:
            current_tree.set_root_val(i)
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i in ["not"]:
            current_tree.set_root_val(None)
            current_tree = p_stack.pop()
            current_tree.set_root_val(i)
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError("Invalid expression given ")
    return e_tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, 'and': operator.and_,
                'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    elif left_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ')'
    return s_val


if __name__ == "__main__":
    pt1 = build_parse_tree(" ( 0 and 888 )")
    pt2 = build_parse_tree(" ( 233 and 888 )")
    print(evaluate(pt1))
    print(evaluate(pt2))
    pt3 = build_parse_tree(" ( 0 or 0 )")
    pt4 = build_parse_tree(" ( 0 or 888 ) or ( 0 or 901 )")
    pt5 = build_parse_tree(" ( 233 or 888 )")
    print(evaluate(pt3))
    print(evaluate(pt4))
    print(evaluate(pt5))

