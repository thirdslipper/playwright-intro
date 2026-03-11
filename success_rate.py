import sys


def get_numbers():
    args = sys.argv[1:]
    if len(args) >= 5:
        try:
            return [float(a) for a in args[:5]]
        except ValueError:
            pass
    nums = []
    for i in range(1, 6):
        while True:
            try:
                n = float(input(f"Enter number {i}: "))
                nums.append(n)
                break
            except ValueError:
                print("Invalid number, try again.")
    return nums


numbers = get_numbers()
average = sum(numbers) / 5
print(f"Average: {average:.4f}")
