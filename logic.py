
def word_counter(inputs,target):
    input1 = inputs.split("\n")
    splited = []
    word_present = []

    # for i in range(len(input1)): # line no.
    #     if(len(input1[i]) < len(target)):
    #         continue
    #     else:
    #         splited.append(input1[i].split(target[0]))

    # for i in range(len(splited)):
    #     print(splited[i])
    # print(input1)
    # print(splited)

    # for i in range(len(splited)):
    #     for j in range(len(splited[i])):
    #         # print(splited[i][j][0:len(target)-1])
    #         # print(target[1:])
    #         if(splited[i][j][0:len(target)-1] == target[1:]):
    #             word_present.append(i+1) # line no


    for idx,line in enumerate(input1):
        if target in line:
            word_present.append(idx+1)


    return word_present

    



# word_line = word_counter(inputs=inp,target=target)
def print_lineno(word_line):
    for i in range(len(word_line)):
        print("Your target word present in line no :- ",word_line[i])