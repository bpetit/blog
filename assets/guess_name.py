#!/usr/bin/env python3

def main():
    with open("initiatives.csv", 'r') as fd:
        for l in fd.readlines():
            prefix = ""
            parts = l.split(',')
            if parts[0].startswith("http"):
                name = parts[0].split('/')[2].split('.')[0] 
                if name == 'www':
                    name = parts[0].split('/')[2].split('.')[1] 
                prefix = "{},".format(name)
            print("{}{}".format(prefix, l).strip())

if __name__ == '__main__':
    main()
