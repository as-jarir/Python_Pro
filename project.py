print('')#space
print('    //\\\     ||||||||                ')
print('   //  \\\    ||                      ')
print('  //    \\\   ||||||||                ')
print(' //      \\\        ||                ')
print('//        \\\ |||||||| Projects...    ')
print('')#space
print("Basic Python Problem-Solving project. A individual Project Of AS Roots.")
print('')#space
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print('')#space

print('Here are 17 projects on Python. Execute them, take a look at the script and try at your own...')
print('')#space
print('[ 1] Sum of two numbers.')
print('[ 2] Pass-Fail identifier.')
print('[ 3] Age identifier.')
print('[ 4] Odd-Even Numbers identifier.')
print('[ 5] Leap year indentifier.')
print('[ 6] Meter to Feet and Feet to Meter converter.')
print('[ 7] Positive, negative and zero identifier.')
print('[ 8] Vowel and Consonant identifier.')
print('[ 9] Largest number identifier.')
print('[10] Multiple presentesion writer.')
print('[11] Word writer multiple time.')
print('[12] Odd-Even Number identifier between selected number.')
print('[13] 1'       )
print('     1,2     ')
print('     1,2,3   ')
print("     1,2,3,4...  ")
print("     this type of thing maker, don't know what it is :(")
print('[14] Multiplication table writer.')
print('[15] Multiple writer using while loop.')
print('[16] 1+2+3+.....+100 ,Sum counter.')
print('[17] leaving number writer.')
print('')#space
print('[18] Show script of this code.')
print('')#space
print('')#space

proj = input('Enter Selection : ')
print("")#space

match proj:
    case "1":
        print('Sum of two numbers.')
        print("")
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos1 = input('Insert your Option : ')
        print('')

        match chos1:
            case "1":
                print('Sum of two numbers.')
                print('')
                num1 = int(input('Insert first number = '))
                num2 = int(input('Insert second number = '))
                print('')#space
                result = num1 + num2

                print('The sum of',num1,'and',num2,'is',result)
            case "2":
                code1 = """
                num1 = int(input('Insert first number = '))
                num2 = int(input('Insert second number = '))
                print('')#space
                result = num1 + num2

                print('The sum of',num1,'and',num2,'is',result)
                """
                print(code1)
    case "2":

        print('Pass-Fail identifier.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos2 = input('Insert your Option : ')
        print('')

        match chos2:
            case "1":
                print("Pass-Fail identifier")
                print('')#space
                mark = int(input('Enter your mark here = '))
                
                if mark >= 40:
                    print('')#space
                    print('You have passed.')
                if mark < 40:
                    print('')#space
                    print('You have failed.')
            case "2":
                code2 = """
                    mark = int(input('Enter your mark here = '))
                
                if mark >= 40:
                    print('')#space
                    print('You have passed.')
                if mark < 40:
                    print('')#space
                    print('You have failed.')
                    """
                print(code2)

    case "3":
        print('Age identifier.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos3 = input('Insert your Option : ')
        print('')

        match chos3:
            case "1":
                print("Age identifier.3")
                print('')#space

                age = int(input('Insert your age here = '))
                print('')#space
                if age >= 18:
                    print('You are eligible for voting.')
                else:
                    print('You are not eligible for voting.')

            case "2":
                code3 = """
                    age = int(input('Insert your age here = '))
                print('')#space
                if age >= 18:
                    print('You are eligible for voting.')
                else:
                    print('You are not eligible for voting.')
                    """
                print(code3)
    case "4":
        print('Odd-Even Numbers identifier.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos4 = input('Insert your Option : ')
        print('')

        match chos4:
            case "1":
                print('Odd-Even Numbers identifier.')
                print('')#space

                num = int(input('Insert your number here = '))
                print('')#space
                if num%2!= 0:
                    print("It's an odd number.")  #You can use double cout ("") inside print syntax. if you use single cout (') in sentence.
                else:
                    print("It's and Even numbeer.")
            case "2":
                code4 = """
                    num = int(input('Insert your number here = '))
                print('')#space
                if num%2!= 0:
                    print("It's an odd number.")  #You can use double cout ("").
                else:
                    print("It's and Even numbeer.")
                    """
                print(code4)
    case "5":
        print('Leap year indentifier.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos5 = input('Insert your Option : ')
        print('')

        match chos5:
            case "1":
                print('Leap year identifier.')
                print('')#space

                year = int(input('Insert the year : '))
                print('')#space

                if (year%400 == 0 or (year%100 != 0 and year%4 == 0)):
                    print("It's a leap year.")
                else :
                    print("It's not a leap year")

            case "2":
                code5 = """
                    year = int(input('Insert the year : '))
                print('')#space

                if (year%400 == 0 or (year%100 != 0 and year%4 == 0)):
                    print("It's a leap year.")
                else :
                    print("It's not a leap year")
                    """
                print(code5)

    case "6":
        print('Meter to Feet and Feet to Meter converter.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos6 = input('Insert your Option : ')
        print('')

        match chos6:
            case "1":
                print("Meter to Feet and Feet to Meter converter.")
                print('')#space

                print('Insert 1 for Feet to Meter.')
                print('Insert 2 for Meter to feet')
                print('')#space

                choice = int(input('insert your option = '))
                print('')#space

                if choice == 1:
                    feet = float(input('Enter your feet = '))
                    result1 = feet/3.281
                    print(result1)
                elif choice == 2:
                    meter = float(input('Enter your meter = '))
                    result2 = meter*3.281
                    print(result2)

            case "2":
                code6 = """
                    print('Insert 1 for Feet to Meter.')
                print('Insert 2 for Meter to feet')
                print('')#space

                choice = int(input('insert your option = '))
                print('')#space

                if choice == 1:
                    feet = float(input('Enter your feet = '))
                    result1 = feet/0.3048
                    print(result1)
                elif choice == 2:
                    meter = float(input('Enter your meter = '))
                    result2 = meter*3.281
                    print(result2)
                    """
                print(code6)
                print('')#space
                print('You can also code the book script. Just open book.')

    case "7":
        print('Positive, negative and zero identifier.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos7 = input('Insert your Option : ')
        print('')

        match chos7:
            case "1":
                print('Positive, negative and zero identifier.')
                print('')#space

                num = int(input('Insert your number = '))
                print('')#space
                if num < 0:
                    print("It's a negative number.")
                elif num == 0 :
                    print("It's a zero")
                else:
                    print("It's a Positive number")  

            case "2":
                code7 = """
                    num = int(input('Insert your number = '))
                print('')#space
                if num < 0:
                    print("It's a negative number.")
                elif num == 0 :
                    print("It's a zero")
                else:
                    print("It's a Positive number")
                    """
                print(code7)
                print('You can also us ethe book code.')

    case "8":
        print('Vowel and Consonant identifier.')
        print('')#space
        print('1. Execute the code. (option 1)')
        print('2. Execute the code. (Option 2)')
        print('3. Show the script.')
        print()
        print('')#space
        chos8 = input('Insert your Option : ')
        print('')

        match chos8:
            case "1":
                print('Vowel and Consonant identifier. (Option 1)')
                print('')#space

                char = input("Enter alphabet : ")
                print('')#space

                match char:
                    case "a,A":
                        print(char,' is a vowel.')
                    case "e":
                        print(char,' is a vowel.')
                    case "i":
                        print(char,' is a vowel.')
                    case "o":
                        print(char,' is a vowel.')
                    case "u":
                        print(char,' is a vowel.')
                    case _:
                        print(char,' is a consonant.')
            case "2":
                print('Vowel and Consonant identifier. (Option 2)')
                print('')#space

                char = input("Enter alphabet : ")
                print('')#space
                 
                vowel = ['a','e','i','o','u','A','E','I','O','U']

                if char in vowel:
                    print(char," is a vowel.")
                else:
                    print(char," is a consonant.")
            case "3":
                
                
                code8_1 = """
                    char = input("Enter alphabet : ")
                print('')#space

                match char:
                    case "a,A":
                        print(char,' is a vowel.')
                    case "e":
                        print(char,' is a vowel.')
                    case "i":
                        print(char,' is a vowel.')
                    case "o":
                        print(char,' is a vowel.')
                    case "u":
                        print(char,' is a vowel.')
                    case _:
                        print(char,' is a consonant.')
                        """
                
                code8_2 = """
                    char = input("Enter alphabet : ")
                print('')#space
                 
                vowel = ['a','e','i','o','u','A','E','I','O','U']

                if char in vowel:
                    print(char," is a vowel.")
                else:
                    print(char," is a consonant.")
                    """
                print('Option 1 :')
                print('')#space
                print(code8_1)
                print('')#space
                print('option 2 :')
                print('')#space
                print(code8_2)

    case "9":
        print('Largest number identifier.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos9 = input('Insert your Option : ')
        print('')

        match chos9:
            case "1":
                print('Largest number identifier.')
                print('')#space

                num1 = float(input('Insert number 1 = '))
                num2 = float(input('Insert number 2 = '))
                num3 = float(input('Insert number 3 = '))
                print('')#space

                if (num1 >= num2) and (num1 >= num3):
                    print(num1,'is largest.')
                elif (num2 >= num1) and (num2 >= num3):
                    print(num2,'is largest.')
                else:
                    print(num3,'is largest.')
            case "2":
                code9 = """
                num1 = float(input('Insert number 1 = '))
                num2 = float(input('Insert number 2 = '))
                num3 = float(input('Insert number 3 = '))
                print('')#space

                if (num1 >= num2) and (num1 >= num3):
                    print(num1,'is largest.')
                elif (num2 >= num1) and (num2 >= num3):
                    print(num2,'is largest.')
                else:
                    print(num3,'is largest.')
                    """
                print(code9)
    case "10":
        print('Multiple presentesion writer.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos10 = input('Insert your Option : ')
        print('')#space

        match chos10:
            case "1":
                print('Multiple presentesion writer.')
                print('')#space
                
                word = str(input('Enter anything to write : '))
                print('')#space
                times = int(input("How many times you wanna write = "))
                print('')#space
                for i in range(times):
                    print(word)

            case "2":
                code10 = """
                    word = str(input('Enter anything to write : '))
                print('')#space
                times = int(input("How many times you wanna write = "))
                print('')#space
                for i in range(times):
                    print(word)
                    """
                print(code10)
                print('You can also use the book code.')
    case "11":
        print('Word writer multiple time.')
        print('')#space
        print('This problem and the previous problem are same.')

    case "12":
        print('Odd-Even Number identifier between selected number.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos12 = input('Insert your Option : ')
        print('')#space

        match chos12:
            case "1":
                print('Odd-Even Number identifier between selected number.')
                print('')#space

                print('Press 1 to find Even Number.')
                print('press 2 to find Odd Number.')
                print('')#space'

                chos = input('Insert your option = ')
                print('')#space

                match chos:
                    case "1":
                        print('Even number finder.')
                        print("")#space

                        here = int(input('From = '))
                        to = int(input('To = '))
                        to += 1
                        print('')#space

                        for i in range(here,to):
                            if (i % 2 == 0):
                                print(i)
                    
                    case "2":
                        print('Odd number finder.')
                        print("")#space

                        here = int(input('From = '))
                        to = int(input('To = '))
                        to += 1
                        print('')#space

                        for i in range(here,to):
                            if (i % 2 != 0):
                                print(i)
            case "2":
                code12 = """
                    case "1":
                        print('Even number finder.')
                        print("")#space

                        here = int(input('From = '))
                        to = int(input('To = '))
                        to += 1
                        print('')#space

                        for i in range(here,to):
                            if (i % 2 == 0):
                                print(i)
                    
                    case "2":
                        print('Odd number finder.')
                        print("")#space

                        here = int(input('From = '))
                        to = int(input('To = '))
                        to += 1
                        print('')#space

                        for i in range(here,to):
                            if (i % 2 != 0):
                                print(i)
                        """
                print(code12)
    case "13":
        print('    1       ')
        print('    1,2     ')
        print('    1,2,3   ')
        print("    1,2,3,4... this type of thing maker, don't know what it is :( ")
        print('')#space
        print('1. Execute the code. (Book code)')
        print('2. Execute the code. (Optional code)')
        print('3. Show the script.')
        print('')#space
        chos13 = input('Insert your Option : ')
        print('')#space

        match chos13:
            case "1":
                print('Here is the Book Code.')
                print('')#space
                
                for i in range(1,10):
                    for j in range(1,i+1):
                        print(j,end="")
                    print()
            case "2":
                print('Here is the Optional Code.')
                print('')#space

                rows = int(input('Rows = '))
                rows += 1
                print('')#space

                for i in range(rows):
                    for j in range(1,i+1):
                        print(j,end="")
                    print()
            case "3":
                code13_1 = """for i in range(1,10):
                    for j in range(1,i+1):
                        print(j,end="")
                    print()
                    """
                code13_2 = """rows = int(input('Rows = '))
                rows += 1
                print('')#space

                for i in range(rows):
                    for j in range(1,i+1):
                        print(j,end="")
                    print()
                    """
                
                print('Book Code :')
                print('')#space
                print(code13_1)
                print('')#space
                print('Optional Code :')
                print('')#space
                print(code13_2)

    case "14":
        print('Multiplication table writer.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos14 = input('Insert your Option : ')
        print('')

        match chos14:
            case "1":
                print('Multiplication table writer.')
                print('')#Space

                num = int(input('Multiplication table of which number = '))
                print('')#space
                tim = int(input('Up to which number = '))
                tim += 1
                print('')#space

                for i in range(1,tim):
                    result = num*i
                    print(num,"*",i," = ",result)
            case "2":
                code14 = """
                    print('Multiplication table writer.')
                print('')#Space

                num = int(input('Multiplication table of which number = '))
                print('')#space
                tim = int(input('Up to which number = '))
                tim += 1
                print('')#space

                for i in range(1,tim):
                    result = num*i
                    print(num,"*",i," = ",result)
                    """
                print(code14)
                
    case "15":
        print('Multiple writer using while loop.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos15 = input('Insert your Option : ')
        print('')

        match chos15:
            case "1":
                print('Multiple writer using while loop.')
                print('')#space

                txt = str(input('What to write : '))
                cnt = int(input('How many times = '))
                print('')#space

                i = 1
                while i <= cnt:
                    print(txt)
                    cnt -= 1

            case "2":
                code15 = """
                
                print('Multiple writer using while loop.')
                print('')#space

                txt = str(input('What to write : '))
                cnt = int(input('How many times = '))
                print('')#space

                i = 1
                while i <= cnt:
                    print(txt)
                    cnt -= 1
                    """
                print(code15)

    case "16":
        print('1+2+3+.....+100 ,Sum counter.')
        print('')#space
        print('1. Execute the code.')
        print('2. Show the script.')
        print('')#space
        chos16 = input('Insert your Option : ')
        print('')

        match chos16:
            case "1":
                print('1+2+3+.....+100 ,Sum counter.')
                print('')#space

                str = int(input('Start = '))
                end = int(input('Stop = '))
                print('')#space

                sum = 0
                while str <= end:
                    sum += str
                    str += 1
                print('The sum of the value is',sum)

            case "2":
                code16 = """
                
                print('1+2+3+.....+100 ,Sum counter.')
                print('')#space

                str = int(input('Start = '))
                end = int(input('Stop = '))
                print('')#space

                sum = 0
                while str <= end:
                    sum += str
                    str += 1
                print('The sum of the value is',sum)
                """
                print(code16)