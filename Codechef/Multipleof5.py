def is_multiple_of_5(D, N):
    # Count the frequency of each digit
    digit_counts = [0] * 10
    for digit in N:
        digit_counts[int(digit)] += 1

    # Check if the last digit is 0 or 5
    if N[-1] not in {'0', '5'}:
        return "No"

    # Check if the sum of digits is divisible by 3
    if sum(int(digit) for digit in N) % 3 != 0:
        return "No"

    # Check if there is at least one even digit
    if digit_counts[0] + digit_counts[2] + digit_counts[4] + digit_counts[6] + digit_counts[8] == 0:
        return "No"

    return "Yes"

def main():
    T = int(input())
    for _ in range(T):
        D = int(input())
        N = input().strip()
        result = is_multiple_of_5(D, N)
        print(result)

if __name__ == "__main__":
    main()
