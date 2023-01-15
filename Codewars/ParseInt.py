def parse_int(string):
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen"
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    string = string.replace('-', ' ')
    string = string.replace(' and ', ' ')
    words = string.split()
    ans = 0
    final_ans = 0

    for word in words:
        if word in units:
            ans += units.index(word)
        elif word in tens:
            ans += tens.index(word) * 10
        elif word == 'hundred':
            ans *= 100
        elif word == 'thousand':
            final_ans, ans = ans * 1000, 0
        elif word == 'million':
            return 1000000
    final_ans += ans
    return final_ans