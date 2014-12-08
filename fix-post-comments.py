import sys

print "fixing comments tag..."

if len(sys.argv) < 2:
    print "wrong args"
    exit(0)
else:
    for fileName in sys.argv[1:]:
        # read
        f = open(fileName)
        print "reading %s" % sys.argv[1]
        str = f.read()
        f.close()
        # replace
        str = str.replace("meta:", "comments: true\nmeta:")
        # write
        print "writing %s" % sys.argv[1]
        f = open(fileName, 'w')
        f.write(str)
        f.close()

    
