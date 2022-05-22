import time
import datetime
from playwright.sync_api import Playwright, sync_playwright
from scrapy import Selector

def login(context):
    # 打开新页面
    page = context.new_page()

    # 转到目标页面
    page.goto("https://www.cambly.com/english?lang=zh_CN")

    # 等待导航栏的下一步行动
    with page.expect_navigation():
        # 点击登录按钮，先找到登录的文本，然后，再点击登录
        page.click("text=登录")

    # 调用方法打开弹出窗口
    # 因为点击apple按钮之后进入弹出页面，因此，为了确保弹出的窗口能加载到正常的状态，故使用此方法
    with page.expect_popup() as popup_info:
        # 点击Apple按钮
        page.click("button:has-text(\"Apple\")")

    # 获取弹出窗口的浏览器对象
    page1 = popup_info.value

    # 输出弹出式窗口的URL
    print('page1: ' + page1.url)

    # 找到用户名input输入框，输入用户名
    page1.fill("input[type=\"text\"]", "1339732832@qq.com")

    # 点击继续
    page1.click("[aria-label=\"继续\"]")

    # 找到密码input输入框，输入密码
    page1.fill("input[type=\"password\"]", "371324neT")

    # 点击登录
    page1.click("[aria-label=\"登录\"]")

    # 点击继续
    page1.click("button:has-text(\"继续\")")

    # 关闭弹出式窗口
    page1.close()

    # 停顿3s，其原因是有网络延迟，如果太快的话，还没有反应过来，就接着点击下一个页面，自然会出错误
    time.sleep(3)

    # 进入登录后的页面
    page.goto("https://www.cambly.com/en/student?lang=zh_CN")

    # 进入页面，停顿2s
    time.sleep(2)
    return page

def find_teacher(page, teacher_name):
    # 点击私人教师
    page.click("text=私人教师")

    # 点击收藏
    page.click("text=收藏")

    # 点击需要预定的老师姓名
    # 获取弹出窗口的浏览器对象
    with page.expect_popup() as popup_info:
        page.click(f"text={teacher_name}")
    teacher_page = popup_info.value
    print("教师界面: " + teacher_page.url)
    return teacher_page

def choose_time_lesson(page, day) -> None:
    # 休眠1s
    time.sleep(1)
    print('正在预约的课程日期: ' + day)
    # 1. 点击预约日期
    page.click(f"button:has-text(\"{day}\")")
    # 2. 选择空闲时间
    # 找到当天所有的空闲时间

    # 3. 返回日期界面
    page.click("text=返回")

def book_lesson(page) -> None:
    # 1. 抓取网页源代码，找出所有的空闲日期
    time.sleep(5)
    schedule = page.query_selector('#schedule-section')
    # 获取js渲染后的网页源代码
    # html = page.query_selector('*').inner_html()
    # print(schedule.inner_html())
    response = Selector(text = schedule.inner_html())
    # 获取所有的日期信息
    date = response.css('h4::text').getall()[-1]
    year = date.split(' ')[-1]
    month = date.split(' ')[0]
    months = {
        '一月': '1', '二月': '2', '三月': '3', '四月': '4', '五月': '5', '六月': '6',
        '七月': '7', '八月': '8', '九月': '9', '十月': '10', '十一月': '11', '十二月': '12'
    }
    month = months[month]
    date_button = response.xpath('descendant-or-self::button')[0]
    keys = date_button.xpath('//button/span/text()').getall()
    values = date_button.xpath('//button/@title').getall()
    date_info = dict(zip(keys, values))
    # print(date_info)
    # 获取所有的有空日期
    free_date = []
    book_date = []
    for [k, v] in date_info.items():
        if v == '有空':
            free_date.append('%04d-%02d-%02d' % (int(year), int(month), int(k)))
        elif v == '已预订':
            book_date.append('%04d-%02d-%02d' % (int(year), int(month), int(k)))
    print("空闲日期: ", free_date)
    print('共有%d天空闲日期' % len(free_date))
    # print("已预定日期: ", book_date)
    # print('共有%d天已经预订' % len(book_date))
    # 2. 预定课程
    # 确定哪天位于哪周
    print("开始预定课程")
    week_list = []
    k = -1
    for i in free_date:
        d = int(datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%W')) - int(datetime.datetime.strptime(free_date[0], '%Y-%m-%d').strftime('%W'))
        if d == k:
            week_list[k].append(i)
        else:
            k = d
            week_list.append([])
            week_list[k].append(i)
    if week_list is None:
        print('该教师已经没有空闲的时间可供预约')
    else:
        print(week_list)
        # 循环每一周
        for each_week in week_list:
            # 循环每一周当中的可用日期
            for i in range(0, len(each_week), 2):
                # print('正在预定上课日期: ' + each_week[i] + ', 请稍后')
                try:
                    # 选择上课时间
                    choose_time_lesson(page, each_week[i].split('-')[-1])
                except Exception as e:
                    print(e)
                    print('上课日期: ' + each_week[i] + ',预约失败')
        print('全部预定成功')

def order_time(end_time):
    print('等待预定时间 ', end_time)
    start_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    seconds = (end_time - start_time).seconds
    while seconds > 0:
        print('还剩%d秒开始预定' % seconds)
        time.sleep(1)
        seconds -= 1
    print('准备预定', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def run(pw: Playwright) -> None:
    # 使用playwright启动chromium浏览器内核
    browser = pw.chromium.launch(headless = False)
    # 根据浏览器内核创建浏览器
    context = browser.new_context()
    # ---------- 函数开始------------
    # 传入浏览器权柄，实现登录过程
    index_page = login(context)
    # 进入教师界面
    teacher_page = find_teacher(index_page, 'Craig D\'Aurizio')
    # 定时
    order_time('2022-02-19 16:44:30')
    # 预定课程
    book_lesson(teacher_page)
    # ---------- 函数结束 -----------
    # 关闭浏览器
    context.close()
    # 关闭浏览器内核
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)