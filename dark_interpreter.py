# -*- coding: UTF-8 -*-
from sys import argv, exit, stderr
import re


def printerr(string):
    print >> stderr, (string)


def interprete_command(string):
    args = re.findall(r'("\.*?"|\'.*?\'|\S+)', string)

    if args[0] == "그만두게":
        exit(0)
    elif ' '.join(args[:3]) == "나의 부름에 응하라":
        message = ' '.join(args[3:])
        if message == "세카이여":
            print("Hello, World!")
        else:
            print(message)

if __name__ == '__main__':
    if len(argv) <= 1:
        while True:
            line = raw_input("黑>>>")
            line = line.strip()
            interprete_command(line)
    else:
        try:
            with open(argv[1]) as fp:
                while True:
                    line = fp.readline()
                    if not line:
                        break
                    line = line.strip()
                    interprete_command(line)
        except IOError as e:
            printerr("암흑의 에너지를 찾을 수 없다네: {0}".format(e))
