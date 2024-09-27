# 这是一个示例 Python 脚本。
from datetime import datetime


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name, day=None):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

    # 获取当前日期
    current_date = datetime.now()

    # 打印当前日期
    print("当前日期是:", current_date.strftime("%Y-%m-%d"))

    # 如果需要获取当前日期的年、月、日
    year = current_date.year
    month = current_date.month
    day = str(current_date.day)

    print("年:", year)
    print("月:", month)
    print("日:", day)


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
