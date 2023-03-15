import sys

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
    NUP = "~"
    ENT = "`"
    FIL = "load"
    IF = "if"
    while True:
        if tokens[pc] == "pendp":
            break
        else:
            if tokens[pc].isdecimal():
                try:
                    stack.append(int(tokens[pc]))
                    pc += 1
                except:
                    print(f"Error:{tokens[pc]}")
                    sys.exit(0)
            elif tokens[pc] == OUT:
                # output
                try:
                    print(stack.pop())
                    pc += 1
                except:
                    print(f"Error:@:{tokens[pc]}")
                    sys.exit(0)
            elif tokens[pc] == NPO:
                # out without popping from the stack
                try:
                    print(stack[len(stack)-1])
                    pc += 1
                except:
                    print(f"Error:.:{tokens[pc]}")
            elif tokens[pc] == ADD:
                # ADD
                try:
                    stack.append(stack.pop()+stack.pop())
                    pc += 1
                except:
                    print(f"Error:+:{tokens[pc]}")
            elif tokens[pc] == SUB:
                # SUB
                try:
                    stack.append(stack.pop()-stack.pop())
                    pc += 1
                except:
                    print(f"Error:-;{tokens[pc]}")
            elif tokens[pc] == MUL:
                # MUL
                try:
                    stack.append(stack.pop()*stack.pop())
                    pc += 1
                except:
                    print(f"Error:*:{tokens[pc]}")
            elif tokens[pc] == DIV:
                # DIV
                try:
                    stack.append(stack.pop() / stack.pop())
                    pc += 1
                except  ZeroDivisionError:
                    print(f"Error:/:{tokens[pc]}")
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
            elif tokens[pc] == NUP:
                # 数を指定してポップ
                pc += 1
                if tokens[pc].isdecimal():
                    try:
                        ran = int(tokens[pc])
                        for i in range(ran):
                            print(stack.pop(),end="")
                    except:
                        print(f"Error:{tokens[pc]}")
                        sys.exit(0)
                else:
                    print(f"Error:{tokens[pc]}")
                    sys.exit(0)
            elif tokens[pc] == ENT:
                # 改行
                print()
                pc += 1
            elif tokens[pc] == FIL:
                # file load
                pc += 1
                try:
                    f = open(tokens[pc],"r")
                    text = f.read()
                    f.close()
                except:
                    print(f"Error:load:{tokens[pc]}")
                    sys.exit(0)
                stack.append(text)
                pc += 1
            elif tokens[pc] == IF:
                pc += 1
                if tokens[pc].isdecimal():
                    num = int(tokens[pc])
                    pc += 1
                    if tokens[pc] == "=":
                        pc += 1
                        if tokens[pc].isdecimal():
                            num2 = int(tokens[pc])
                            if num == num2:
                                # true
                                pc += 1
                            else:
                                # false:
                                while True:
                                    if tokens[pc] == ";":
                                        pc += 1
                                        break
                                    else:
                                        pc += 1
                        else:
                            # 数字と文字が一緒なわけないのでfalse
                            while True:
                                if tokens[pc] == ";":
                                    pc += 1
                                    break
                                else:
                                    pc += 1
                    else:
                        print(f"Error:if:{tokens[pc]}")
                        sys.exit(0)
                else:
                    print(f"Error:if:{tokens[pc]}")
                    sys.exit(0)
            elif tokens[pc] == ";":
                pc += 1
            elif tokens[pc] == "?":
                # comment
                while True:
                    if tokens[pc] == ";":
                        pc += 1
                        break
                    else:
                        pc += 1
            else:
                print(f"Error: {tokens[pc]}: No such instruction. Are you stupid?")
                sys.exit(0)

