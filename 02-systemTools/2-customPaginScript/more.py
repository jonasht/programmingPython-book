def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chuck = lines[:numlines]
        lines = lines[numlines:]
        for line in chuck: 
            print(line)
        if lines and input('more/mais?') not in ['y', 'Y', 's', 'S']:
            break
        
if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(), 10)
