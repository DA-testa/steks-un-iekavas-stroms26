# python3
## Haralds Strombergs 221RDB307


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top.char, next):
                    return i + 1
                
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1

    return "Success"


def main():
    
    user_input = input().strip()

    
    if user_input == "I":
        brackets_input = input().strip()
        print(find_mismatch(brackets_input))
    elif user_input == "F":
        

        file_path = input().strip()
        with open(file_path, "r") as f:
            brackets_input = f.read().strip()
        print(find_mismatch(brackets_input))
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()


