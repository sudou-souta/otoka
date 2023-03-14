import sys

def loader():
    try:
        filename = sys.argv[1]
        f = open(filename,"r")
        src = f.read()
        f.close()
    except:
        print("Yu: open file error")
        sys.exit(0)
    tokens = src.split()
    tokens.append("pendp")
    return tokens

def parser(tokens):
    pc = 0
    stack = []
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    OUT = "@"
    NPO = "."
    STR = '"'
    while True:
        if tokens[pc] == "pendp":
            break
        else:
            if tokens[pc].isdecimal():
                stack.append(int(tokens[pc]))
                pc += 1
            elif tokens[pc] == OUT:
                # output
                print(stack.pop())
                pc += 1
            elif tokens[pc] == NPO:
                # out without popping from the stack
                print(stack[len(stack)-1])
                pc += 1
            elif tokens[pc] == ADD:
                # ADD
                stack.append(stack.pop()+stack.pop())
                pc += 1
            elif tokens[pc] == SUB:
                # SUB
                stack.append(stack.pop()-stack.pop())
                pc += 1
            elif tokens[pc] == MUL:
                # MUL
                stack.append(stack.pop()*stack.pop())
                pc += 1
            elif tokens[pc] == DIV:
                # DIV
                try:
                    stack.append(stack.pop() / stack.pop())
                    pc += 1
                except  ZeroDivisionError:
                    print(f"ZeroDivisionError:{tokens[pc]}")
                    sys.exit(0)
            elif tokens[pc] ==  STR:
                pc += 1
                if type(tokens[pc]) is str:
                    # string
                    string = tokens[pc]
                    pc += 1
                    if tokens[pc] == STR:
                        stack.append(string)
                        pc += 1
                    else:
                        print("error:The end of str must be closed with double quotes")
                        sys.exit(0)
            else:
                print(f"Error: {tokens[pc]}: No such instruction. Are you stupid?")
                sys.exit(0)
tokens = loader()
print("fileload: OK")
parser(tokens)
