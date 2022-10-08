def d1p2():
    input = open('d1p1_data', 'r')
    input = input.read()
    input = input.split()
    input = [int(i) for i in input]

    val = 0
    for i in range(0, len(input) - 3):
        if (input[i + 1] + input[i + 2] + input[i + 3]) > (input[i] + input[i + 1] + input[i + 2]):
            val += 1


    print(val)


d1p2()
