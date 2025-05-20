import subprocess

# 运行一个命令并等待其完成的首选且最直接的方法
# 参数：
#  capture_output=True 这个参数告诉subprocess.run() 函数捕获子进程的标准输出stdout和stderr，捕获的内容会存放在CompleteProces 对象的stdout和stderr属性中
#  text=True 告诉subprocess.run() 函数将输出转换为字符串

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print(result.stdout)
