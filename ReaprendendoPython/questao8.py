# #include <stdio.h>
# int main()
# {
#     char alfabeto[26] = "abcdefghijklmnopqrstuvwxyz";
#     int num  = 97, i;
#     for (i = 0; i < 26; i++)
#     {
#         printf("%d e %c\n", num, alfabeto[i]);
#         num++;
#     }
#     return 0;
# }

alfabeto = "abcdefghijklmnopqrstuvwxyz"
num = 97

for i in range(26):
    print(f"{num} e {alfabeto[i]}")
    num += 1
    