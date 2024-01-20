def wordcount():
    input_file = open("input.txt", "r")
    data = input_file.readlines()
    output_file = open("output.txt", "w")
    output_file.writelines(data)
    output_file.write("\n Word_Count : ")

    dict = {}
    for line in data:
        word = line.strip().split(" ")
        for w in word:
            s = "\n" + w + " " + str(word.count(w))
            output_file.write(s)

wordcount()