
def read_input():
    with open('d1000000_sample_ts1_input.txt') as f:
        lines = f.readlines()

    cont = 0
    listas = []
    for i in range(int(lines[0].split("\n")[0])):
        listas.append([int(j) for j in lines[2+cont*2].split("\n")[0].split(" ")])
        cont += 1

    return listas

def read_input2():
    listas = []
    #q = input()
    for i in range(int(input())):
        _ = int(input())
        q = input().split("\n")[0]
        listas.append([int(x) for x in q.split(" ")])

    return listas

def write_output(text):
    with open('Test output.txt', 'w') as f:
        f.write(text)

if __name__ == '__main__':
    listas = read_input2()
    text = ""
    for case, lista in enumerate(listas):
        lista.sort()
        count = 1
        if lista[0] < 1:
            #Case #1:
            text = text + "Case #" + str(case+1) + ": 0\n"
            break
        for i in lista[1:]:
            if i > count:
                count += 1
        text = text + "Case #" + str(case+1) + ": " + str(count) + "\n"

    text = text[0:-1]
    print(text)