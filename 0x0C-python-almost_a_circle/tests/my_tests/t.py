#!/usr/bin/python3
with open("mwass.txt", 'w') as f:
    for i in range(4, 21):
        string = "suite.addTest(self.test_{}-rectangle())\n".format(i)
        f.write(string)

