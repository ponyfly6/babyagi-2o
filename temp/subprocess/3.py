import subprocess


# 最灵活，可实时交互
# Popen （Process Open）是subprocess 模块中最基础和最灵活的接口，它允许你创建并管理子进程，提供了对子进程的输入、输出和错误流进行精细控制的能力，并且可以实现非阻塞的交互（即你的 Python 程序可以在子进程运行时继续做其他事情）。

# stdin: 允许我们向子进程的标准输入写入数据
# stdout: 允许我们从子进程的标准输出读取数据


proc = subprocess.Popen(['grep', 'hello'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

# proc.communicate() 会发送数据，然后等待命令结束，并返回标准输出和标准错误
# _ 用作占位符，因为我们这里不关心标准错误输出
out, _ = proc.communicate("hello world\nhello python\n")

print("匹配结果:", out)








