import subprocess
import sys


def generate_playwright_code(url, output_file, browser_name):
    """
    使用 Playwright Codegen 生成自动化测试代码。

    :param url: 要测试的网页URL。
    :param output_file: 输出的Python文件名。
    :param browser_name: 浏览器名称，例如 "chromium" 或 "firefox"。
    :return: None
    """
    # 检查 Playwright 是否安装
    try:
        subprocess.run(['playwright', 'codegen', '--help'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       text=True)
    except FileNotFoundError:
        sys.exit("Playwright Codegen命令未找到，请确保Playwright已经安装并添加到PATH中。")

    # 构建命令行参数
    # "--viewport-size=1920,882"  窗口大小
    command = ['playwright', 'codegen', '--target', 'python', '-o', output_file, '-b', browser_name, url]

    # 运行命令并捕获输出
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("代码生成成功。")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        sys.exit(f"代码生成失败：{e.stderr}")


# 使用示例
if __name__ == "__main__":
    generate_playwright_code("http://192.168.10.230:30510/login", "example_test.py", "chromium")
