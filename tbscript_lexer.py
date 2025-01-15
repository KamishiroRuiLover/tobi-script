import sys


def main():
    fname = str(input("File path: "))

    file = ''
    if fname.endswith(".tobi"):
        file = open(fname)
    else:
        print("FILE NOT TOBI-SCRIPT!")
        sys.exit(1)

    for line in file:
        translate(line)


def fail(cont, code):
    print("TBSCRIPT LXR (PY) FAILED: Reason: " + '"' + cont + '"')
    sys.exit(code)


def translate(line):
    action = ""
    args = ("")
    index = 0

    check_init = False
    for i in line:
        if check_init:
            if i.isalnum():
                action += i
            else:
                check_init = False
                break
        else:
            if i.isalnum():
                check_init = True
                action += i
        
        index += 1

    failed = True
    func = ""
    argt = ""
    argscap = 0
    for act in actions:
        if act == action:
            temp = actions[act]
            failed = False
            func = temp["func"]
            argt = temp["argtype"]
            argscap = temp["argsnum"]
    if failed:
        fail("action tried to run, but didn't exist.", 2)
    
    if argt == "space":
        index += 1

    argsnum = 0
    while(True):
        if line[index].isalnum():
            args[argsnum] = args[argsnum] + line[index]
        elif line[index].isspace():
            argsnum += 1
            index += 1
        else:
            fail("Expected whitespace or alphanumeric, instead got different character.", 3)
        
        index += 1

        if index >= len(line) - 1:
            break
    
    if argsnum != argscap:
        fail("Function: " + action + " expected " + str(argscap) + " arguments.")


def native_import(args):
    print(args)


actions = {
    "import": {
        "func": native_import,
        "argtype": "space",
        "argsnum": 1
    }
}


main()