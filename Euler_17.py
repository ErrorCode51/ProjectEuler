# this is the code for problem 17 of project euler

# this funtion returns the writen out number (single digit only)
def writeOutSingleDitgit(number):
    number = int(number)
    if number >= 10 or number < 0:
        print('The number is not single digit or is negative')
        return None
    if number == 0:
        return ''
    if number == 1:
        return 'one'
    if number == 2:
        return 'two'
    if number == 3:
        return 'three'
    if number == 4:
        return 'four'
    if number == 5:
        return 'five'
    if number == 6:
        return 'six'
    if number == 7:
        return 'seven'
    if number == 8:
        return 'eight'
    if number == 9:
        return 'nine'
    return None



# this function writes a number out in words
def writeOut(number):
     if number > 10000:
         print('The number is too high')
         return None
     textNumber = '' # create a string to put the text in
     if number >= 1000:
         textNumber += writeOutSingleDitgit(number/1000)
         textNumber += ' thousand and '
         while number >= 1000:
             number -= 1000
     if number >= 100:
         textNumber += writeOutSingleDitgit(number/100)
         textNumber += ' hundred and '
         while number >= 100:
             number -= 100
     if number >= 10:
        if number >= 90:
            textNumber += 'ninety-'
            number -= 90
        if number >= 80:
            textNumber += 'eighty-'
            number -= 80
        if number >= 70:
             textNumber += 'seventy-'
             number -= 70
        if number >= 60:
            textNumber += 'sixty-'
            number -= 60
        if number >= 50:
            textNumber += 'fifty-'
            number -= 50
        if number >= 40:
            textNumber += 'forty-'
            number -= 40
        if number >= 30:
            textNumber += 'thirty-'
            number -= 30
        if number >= 20:
            textNumber += 'twenty-'
            number -= 20
        if number == 19:
            textNumber += 'nineteen'
            number -= 19
        if number == 18:
            textNumber += 'eighteen'
            number -= 18
        if number == 17:
            textNumber += 'seventeen'
            number -= 17
        if number == 16:
            textNumber += 'sixteen'
            number -= 16
        if number == 15:
            textNumber += 'fifteen'
            number -= 15
        if number == 14:
            textNumber += 'fourteen'
            number -= 14
        if number == 13:
            textNumber += 'thirteen'
            number -= 13
        if number == 12:
            textNumber += 'twelve'
            number -= 12
        if number == 11:
            textNumber += 'eleven'
            number -= 11
        if number == 10:
            textNumber += 'ten'
            number -= 10
     if number != 0:
        textNumber += writeOutSingleDitgit(number)

     textNumber = textNumber.strip(' ')
     if textNumber.endswith('-'):
         textNumber = textNumber.strip('-')
     if textNumber.endswith('and'):
         textNumber = textNumber[0:-3]
     textNumber = textNumber.strip(' ')

     return textNumber

total = 0

for i in range(1, 1001):
    textNumber = writeOut(i)
    textNumber = textNumber.replace(' ', '')
    textNumber = textNumber.replace('-', '')
    print(textNumber)
    total += len(textNumber)

print('Total:', total)




