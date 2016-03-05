import os, filecmp

results = {1:'success', 2:'file not found', 3:'error', 4:'timeout'}

fileName = 'codigo.cpp'
language = 'cpp'
folderInputs = '/inputs'
folderOutputs = '/outputs'
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

def run(fileName, input, timeout, language, name):
    if language == 'py':
        terminal = 'python ' + fileName        
    elif language == 'py3':
        terminal = 'python3 ' + fileName        
    elif language=='c':
        terminal = './' + fileName[:-2]        
    elif language=='cpp':
        terminal = './' + fileName[:-4]        

    r = os.system('timeout ' + timeout + ' ' + terminal + ' < ' + input + ' > out' + name + '.txt')

    if r==1792:
        return 1
    elif r==31744:
        return 4
    else:
        return 3

def compare(output, name):
    if os.path.isfile('out' + name + '.txt') and os.path.isfile(output):
        b = filecmp.cmp('out' + name + '.txt', output)
        return b
    else:
        return 2

result = compileFile(fileName, language)
print(results[result])

if result==1:

    folder = os.path.dirname(os.path.realpath(__file__)) + folderInputs
    files = os.listdir(folder)

    for i in files:
        run(fileName, folder + '/' + i, timeout, language, i[:-4])

    folder = os.path.dirname(os.path.realpath(__file__)) + folderOutputs
    files = os.listdir(folder)

    acc = 0
    for i in files:
        comp = compare(folder + '/' + i, i[:-4])
        if comp!=2 and comp:
            acc += 1

    print (str(acc) + '/' + str(len(files)))
    
#Gustavo Vilar
#Julgador Simples