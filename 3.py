# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''
with open('3.txt','r') as file:
    a = file.read()
count = 1
res = ''
for i in range(0,len(a)-1):
    if a[i]==a[i+1]:
        count+=1
    else:
        res = res +str(count)+a[i]
        count=1
res = res +str(count)+a[i]
print(res)


