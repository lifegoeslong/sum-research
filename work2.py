import matplotlib.pyplot as plt

# 读取 strace 输出文件
with open('trace.txt', 'r') as file:
    data = file.read()

# 解析系统调用次数
syscall_counts = {'getuid': 0, 'rt_sigprocmask': 0}
lines = data.split('\n')
for line in lines:
    if '(' in line:
        syscall = line.split('(')[0]
        if syscall in syscall_counts:
            syscall_counts[syscall] += 1

# 提取系统调用和调用次数
syscalls = list(syscall_counts.keys())
counts = list(syscall_counts.values())

# 绘制柱状图
plt.bar(syscalls, counts)
plt.xlabel('system call 名字')
plt.ylabel('system call 数字')
plt.title('getuid() 和 rt_sigprocmask() system call ploting')

# 显示图表
plt.show()
