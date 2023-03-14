#function to conver string to binary
while True:
    x=int(input("enter 1 for envrypt 2 for decrypt: "))
    if x==1:
        def string_to_64bit():
            string1 = input("enter string: ")
            string = string1.encode('utf-8')
            # Using the hex method to convert the bytes into hexadecimal format
            l = string.hex()
            n = int(l, 16)

            bStr = ''
            while n > 0:
                bStr = str(n % 2) + bStr
                n = n >> 1
            res = bStr
            x = str(res)
            print(x)
            z = list(x.strip(""))
            a = len(z)
            b = a // 64
            d = (b + 1) * 64

            if b == 0:
                c = 64 - a
                for i in range(c):
                    z.append(0)

            else:
                c = d - a
                for i in range(c):
                    z.append(0)

            l1 = "".join(str(x) for x in z)
            substring_length = 64
            substrings = [l1[i:i + substring_length] for i in range(0, len(l1), substring_length)]
            print("string in 64  block: ", substrings)


        string_to_64bit()
    elif x==2:
        def binary_to_string():
            binary=bin(input("enter encrypted binary"))
            
