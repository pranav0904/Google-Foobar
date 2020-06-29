'''
print the 1st 5 digit starting from the entered number from the string of prime numbers 
'''
def solution(n):
    prime_list = [2]
    num = 3
    while num < 100000:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    ls=''.join(str(i) for i in prime_list)
    print(ls[n:n+5])

solution(0)