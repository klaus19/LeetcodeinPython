def numbers_of_letters(n):
    names = { '0': 'zero' ,
              '1': 'one'  ,
              '2': 'two'  ,
              '3': 'three',
              '4': 'four' ,
              '5': 'five' ,
              '6': 'six'  ,
              '7': 'seven',
              '8': 'eight',
              '9': 'nine' }
    result = []
    while True:
        result.append(''.join(names[digit] for digit in str(n)))
        if result[-1]=='four':
            return result
        n = len(result[-1])