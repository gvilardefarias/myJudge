import os, filecmp

results = {1:'success', 2:'file not found', 3:'error', 4:'timeout'}

fileName = 'brute.py'
language = 'py'
testin = 'entrada.txt'
outCorrect = 'saida.txt'
timeout = '1'

def compileFile(fileName, language):
    if (os.path.isfile(fileName)):
        if language == 'py':
            name = fileName
        elif language == 'py3':
            name = fileName
        elif language == 'cpp':
            os.system('g++ ' + fileName + ' -o ' + './' + fileName[:-4])
            name = fileName[:-4]
        elif language == 'c':
            os.system('gcc ' + fileName + ' -o ' + './' + fileName[:-2])
            name = fileName[:-2]

        if (os.path.isfile(name)):
            return 1
        else:
            return 3
    else:
        return 2

def run(fileName, input, timeout, language):
    if language == 'py':
        terminal = 'python ' + fileName
        name = fileName[:-3]
    elif language == 'py3':
        terminal = 'python3 ' + fileName
        name = fileName[:-3]
    elif language=='c':
        terminal = './' + fileName[:-2]
        name = fileName[:-2]
    elif language=='cpp':
        terminal = './' + fileName[:-4]
        name = fileName[:-4]

    r = os.system('timeout ' + timeout + ' ' + terminal + ' < ' + input + ' > out' + name + '.txt')

    if language=='c':
        os.remove('./' + fileName[:-2])
    elif language=='cpp':
        os.remove('./' + fileName[:-4])

    if r==1792:
        return 1
    elif r==31744:
        return 4
    else:
        return 3

def compare(output):
    if language == 'py':
        name = fileName[:-3]
    elif language == 'py3':
        name = fileName[:-3]
    elif language=='c':
        name = fileName[:-2]
    elif language=='cpp':
        name = fileName[:-4]

    if os.path.isfile('out' + name + '.txt') and os.path.isfile(output):
        b = filecmp.cmp('out' + name + '.txt', output)
        return b
    else:
        return 2

print(results[compileFile(fileName, language)])
print (results[run(fileName, testin, timeout, language)])
print (compare(outCorrect))

#Gustavo Vilar
#Julgador Simples