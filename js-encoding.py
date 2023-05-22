from selenium import webdriver

def js_encoding():
    # 创建 ChromeOptions 对象，并设置启动参数
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # 设置为静默模式

    # 指定 chromedriver 及其路径
    executable_path = "your path \chromedriver.exe"

    # 创建浏览器对象
    browser = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    # 打开网页
    browser.get('http://www.example.com/login')

    # 调用 JavaScript 函数
    # 遍历读取文件中的每一行，并调用 JavaScript 函数
    with open('pass.txt', 'r') as f, open('result.txt', 'w') as r:
        lines = f.readlines()
        for line in lines:
            result = browser.execute_script(f"return hex_sha1('{line.strip()}')")
            print(result)
            r.write(result + '\n')

    # 输出结果
    print(result)

    # 关闭浏览器
    browser.quit()

if __name__ == '__main__':
    js_encoding()
