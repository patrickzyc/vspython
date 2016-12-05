# coding: utf-8
# input:
# 刘备 23 35 44 47 51
# 关羽 60 77 68
# 张飞 97 99 89 91
# 诸葛亮 100
# expected output:
# 刘备 200
# 关羽 205
# 张飞 376
# 诸葛亮 100
output = file('result.txt', 'a')
for i in file('write_to_file.txt'):
    data = i.split()
    # sum_score=0
    # for j in data[1:]:
    #     sum_score+=int(j)
    output.writelines(data[0]+'\t:'+str(sum([int(x) for x in data[1:]]))+'\n')  # 制表符\t
    print data[0], sum([int(x) for x in data[1:]])
output.close()


