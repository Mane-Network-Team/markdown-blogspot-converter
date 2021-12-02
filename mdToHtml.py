import getopt,sys
import importlib

version = "1.0.5"

if __name__ == "__main__":
    print("Mane mdTohtml Version %s" % (version))
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:t:vm:")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    input_file = ""
    template = "default"
    moudles = []

    for o, a in opts:
        if o == "-v":
            print(version)
            sys.exit()
        elif o in ("-i"):
            input_file = a
        elif o in ("-t"):
            template = a
        elif o in ("-m"):
            if (a.find(",")!=-1):
                moudles = a.strip().split(",")
            else:
                moudles.append(a)
    
    if (input_file.strip() == "" or template.strip() == ""):
        print("[Error] Missing -i or -t")

    print("* Using template: %s ..." % (template))

    lib = importlib.import_module('template.%s.run' % (template))
    getattr(lib,'run')(input_file,moudles)
