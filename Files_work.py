name_file = input('Введите название файла ')
All_str_arr = []
file_str_arr = []
while name_file != 'quit':
    name_file += '.txt'
    f_s = open(name_file,'r')
    p = f_s.readlines()
    All_str_arr += p
    file_str_arr.append(p)
    f_s.close()
    name_file = input('Введите название файла ')

alpha_arr = set()
n = 0
for i in range(len(All_str_arr)):
    if '\n' in All_str_arr[i]:
        All_str_arr[i] = All_str_arr[i][:-1]
print(All_str_arr)

for i in All_str_arr:
    for j in i:
        alpha_arr.add(j.lower())
n = 0
print(alpha_arr)
alpha_finish = set()
for i in alpha_arr:
    for j in file_str_arr:
        j = ''.join(j)
        if i in j:
            n += 1
            continue
    if n == len(file_str_arr):
        alpha_finish.add(i)
        n = 0
    else:
        n = 0

f_s_n = open('new_f.txt', 'w')
for i in alpha_finish:
    f_s_n.write(i+' ')
