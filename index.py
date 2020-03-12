'''
Only can run in local
base on python 3.6
please cheack updata from Tymon42's github
'''
import time
global now_subject

now_subject = ''

trueList = []
for name in open('trueList.txt',"r", encoding='UTF-8'):
    trueList.append(name[:-1])

todayList = []
for line in open('todayList.txt',"r", encoding='UTF-8'):
    if line in ['#接龙物理\n', '#接龙化学\n', '#接龙生物\n', '#接龙语文\n', '#接龙数学\n', '#接龙英语\n', '#接龙历史\n', '#接龙地理\n', '#接龙政治\n']:
        now_subject = line[:-1]
    for dd in range(0,100):
        line = line.lstrip()
        if line in ['物理\n', '化学\n', '生物\n', '语文\n', '数学\n', '英语\n', '历史\n', '地理\n', '政治\n']:
            now_subject = line[:-1]
    for a in range(0,100):
        for i in range(0,100):
            line = line.lstrip(str(i))
    for b in range(0,100):
        line = line.lstrip('.')
        line = line.lstrip()
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            line = line.lstrip(c)
            line = line.lstrip('.')
            line = line.lstrip()
    todayList.append(line[:-1])

for i in trueList:
    if i not in todayList:
        print(i + " 未填写考勤接龙")

print('——————\n以上为' + now_subject + '截至'+ time.strftime("%Y-%m-%d %H:%M", time.localtime()) +'考勤接龙情况')
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
