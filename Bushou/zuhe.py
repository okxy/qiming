with open('cao.txt', 'r', encoding='utf-8') as fcao, \
     open('shui.txt', 'r', encoding='utf-8') as fshui, \
     open('zuhe.txt', 'w', encoding='utf-8') as fw:
    scao = fcao.readlines()
    sshui = fshui.readlines()
    zcao = []
    zshui = []
    for i in scao:
        zcao += i.strip().split()
        fw.write(i)

    for i in sshui:
        zshui += i.strip().split()
        fw.write(i)
        
    zuhe = []
    for i in zshui:
        x = []
        for j in zcao:
            x.append(i+j)        
        zuhe.append(x)        
        fw.write(' '.join(x))
        fw.write('\n\n')
        
    print('finished.')
