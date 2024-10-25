
def fizzbuzz (count):
    for i in range(1, count+1):
        if i % 3 == 0:
           print(f'{i} - fizz')
        else:
            print(i)

def main():
    fizzbuzz(15)

if __name__ == "__main__":
    main()
