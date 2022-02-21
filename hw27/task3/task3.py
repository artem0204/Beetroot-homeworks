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


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = math_exp.split()
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    operators = ["+", "-", "*", "/", "(", ")"]
    splited_list = []
    temp = ""
    for index in range(len(math_exp)):
        if temp and not math_exp[index].isdigit():
            splited_list.append(temp)
            temp = ""
        if math_exp[index] in operators:
            splited_list.append(math_exp[index])
        elif math_exp[index].isdigit():
            temp += math_exp[index]
    for i in splited_list:
        if i == "(":
            current_tree.insert_left("")
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ["+", "-", "*", "/"]:
            current_tree.set_root_val(i)
            current_tree.insert_right("")
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = stack.pop()
        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))
    return tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ')'
    if s_val.__len__() > 10:
        temp = ""
        for i in range(len(s_val) - 1):
            if s_val[i + 1].isdigit():
                temp += s_val[i + 1]
                continue
            if not s_val[i].isdigit() and not s_val[i-1].isdigit():
                temp += s_val[i]
        print(temp[1:])

    return s_val


if __name__ == "__main__":
    print_exp(build_parse_tree("( ( 10 + 5 ) * 3 )"))
