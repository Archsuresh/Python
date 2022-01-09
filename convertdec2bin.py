from stack import Stack

def dec_2bin(dec_num):
    s=Stack()

    while dec_num >0:
        remainder=dec_num %2
        s.push(remainder)
        dec_num=dec_num//2

    bin_num=""

    while not s.isempty():
        bin_num+=str(s.pop())

    return bin_num

n=int(input('Enter the number to convert to bin'))
print(dec_2bin(n))
