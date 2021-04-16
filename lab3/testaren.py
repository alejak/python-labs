from bintreeFile import Bintree

testlist = Bintree()
testlist.put("apa")
testlist.put("banan")
testlist.put("alex")
if "apa" in testlist:
    print("Finns")
else:
    print("Finns ej")
testlist.put(input())
testlist.write()