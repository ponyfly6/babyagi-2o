class Colors:
    """
    各属性含义
        HEADER = '\033[95m'
        紫色（淡紫/洋红色），通常用作标题。

        OKBLUE = '\033[94m'
        蓝色，常用来表示一般信息。

        OKCYAN = '\033[96m'
        青色（蓝绿色），也是一般信息色。

        OKGREEN = '\033[92m'
        绿色，通常用来表示成功或通过。

        WARNING = '\033[93m'
        黄色，用于警告或提示。

        FAIL = '\033[91m'
        红色，表示失败或错误。

        ENDC = '\033[0m'
        重置所有样式（颜色和加粗等），一定要在你想“恢复正常显示”后加上。

        BOLD = '\033[1m'
        加粗。

        UNDERLINE = '\033[4m'
        下划线。
    
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{Colors.WARNING}警告：不要乱操作！{Colors.ENDC}")
print(f"{Colors.OKGREEN}操作成功！{Colors.ENDC}")
print(f"{Colors.FAIL}{Colors.BOLD}出错了！{Colors.ENDC}")
    
