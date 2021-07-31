def main():
    #write your code below this line
    numbers = []

    while True:
        number = input()

        if number == "-1":
            break

        numbers.append(number)

    start = int(input("From where?"))
    end = int(input("To where?"))

    for i in range(start, end+1):
        print(numbers[i])

if __name__ == '__main__':
    main()
