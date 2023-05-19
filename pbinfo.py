# #861
# # def dublare():
# #     print(int(input))
# #     l = strlen(s)
# #     cnt = 0
# #     while(l % 2 == 0):
# #         bool(s)
# #         ok = true
# #         for i in range(int(s) == 0, i < l/2, 1):
# #             if(s[i]!=s[l-i-1]):
# #                 ok=false
# #         if(ok):
# #             cnt == 1
# #             l/=2
# #         else:
# #             break
# #
# # if __name__ == "__main__":
# #     print(dublare)
#
#
# if __name__ == "__main__":
#     citire_fisier = open("pozitiiconsecutive.in" , "r")
#     scriere_fisier = open("pozitiiconsecutive.out" , "w")
#     x = int(citire_fisier.readline().strip())
#     y = int(citire_fisier.readline().strip())
#     z = 9
#     scriere_fisier.write(str(y))
#     scriere_fisier.write(' ')
#     scriere_fisier.write(str(x))
#     scriere_fisier.write(' ')
#     while(z > 8):
#         z = 2 * x - y + 2
#         scriere_fisier.write(str(z))
#         scriere_fisier.write(' ')
#         y = x
#         x = z
#     scriere_fisier.write('3')
#     scriere_fisier.write(' ')
#     scriere_fisier.write('0')

# if __name__ == "main":
#     p = int(input())
#     s = 0
#     unsigned long long k
#     cin >> p >> k:
#     if(k % 2 == 0) :
#         cout << k / 2 + k - 2 << p
#     else:
#         cout << k / 2 + k - 1 << p
#     return 0


def fibonacci_decomposition(n):
    fib = [0, 1, 1]  # stocarea primei serii fibonacci
    i = 3
    while fib[i-1] <= n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    decomposition = []
    i -= 1
    while n > 0:
        while fib[i] > n:
            i -= 1
        decomposition.append(fib[i])
        n -= fib[i]
    return decomposition


print(fibonacci_decomposition(65))
