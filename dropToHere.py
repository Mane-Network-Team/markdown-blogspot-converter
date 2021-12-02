import sys,os

if (len(sys.argv) == 1) or ((sys.argv[1]).strip() == "") :
    print("Error: Please DROP markdown file into this file.")
    sys.exit(1)

if not (os.path.exists(sys.argv[1])):
    print("Error: No such file.")
    sys.exit(1)

## Lists module
modules = []
for dirpath, dirnames, filenames in os.walk('module'):
    for filename in (filenames):
        modules.append([filename.split(".py")[0],False])
    break

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Input Markdown File:")
    print("  " + sys.argv[1])

    print("Support Modules:")
    count = 0
    for module,enable in modules:
        print(" %s [%s] %s" % ( ">" if enable else " ",count,module))
        count += 1


    # read input
    print()
    print("Input number will be select (0,1,2), 's' will be start.")
    input_str = input()
    if (input_str.strip().lower() == "s"):
        break

    if (input_str.find(",") !=-1):
        for number in input_str.split(","):
            try:
                modules[int(number)][1] = not modules[int(number)][1]
            except :
                pass
    else:
        try:
            modules[int(input_str)][1] = not modules[int(input_str)][1]
        except :
            pass

enable_module = []
for module,enable in modules:
    if (enable):
        enable_module.append(module)

print("Execute Command: ")
exec_command = ('python mdTohtml.py -i "%s" -t default -m %s' % (sys.argv[1] , ','.join(enable_module)))
os.system(exec_command)

