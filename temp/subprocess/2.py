import subprocess


# 只关心命令的标准输出，并且希望在命令执行出错时（返回非零退出码）自动抛出异常，那么 check_output() 是一个便捷的选择。
output = subprocess.check_output(["ls"], text=True)


print(output)
