# 功能：删除[[Category:已逝世超過一個月的人物]]中的页面death模板
# 计划：
# 版本：beta
# 最后修改日期：2022-02-28
import pywikibot,time,re
from pywikibot import pagegenerators
from datetime import datetime

site = pywikibot.Site('zh', 'wikipedia')
cat = pywikibot.Category(site,'Category:已逝世超過一個月的人物')
gen = pagegenerators.CategorizedPageGenerator(cat)
localday = time.strftime("%Y-%m-%d", time.localtime())
localday = datetime.strptime(localday,'%Y-%m-%d')
pagetext = ""
# 创建list以便匹配到模板中的各种情况，需要添加更多种情况
# 日期只有年月日，或日期包括具体时间。下面是几个例子：
    # {{Recent death|time=2021-12-15}}
    # {{最近逝世|time=2021-06-16T13:57:52+00:00}}
    # {{Recent Death|time=2021-06-20T05:12:50+00:00}}
# \d 匹配任意数字，等价于 [0-9].
# re.I 忽略大小写
# re0 = re.search('\{\{Recent death\|time=\d+-\d+-\d+T\d+:\d+:\d+\+\d+:\d+\}\}',page.text,re.I) 
# re.sub(pattern, repl, string, count=0, flags=0) 可以考虑使用这个直接进行替换
listRe = ["\{\{Recent death\|time=\d+-\d+-\d+T\d+:\d+:\d+\+\d+:\d+\}\}",
          "\{\{Recent death\|time=\d\d\d\d-\d\d-\d\d\}\}",
          "\{\{Recent death\|\d\d\d\d-\d\d-\d\d\}\}",
          "\{\{Recent death\|time=\d\d\d\d-\d\d\}\}",
          "\{\{最近逝世\|\d\d\d\d-\d\d-\d\d\}\}",
          "\{\{最近逝世\|time=\d\d\d\d-\d\d-\d\d\}\}"]
# 遍历页面
for page in gen:
    for countRegex in range(len(listRe)):
        re0 = re.search(listRe[countRegex],page.text,re.I)
        if re0 == None:# 没有搜索到 continue
            continue
        else:# 搜索到则 break
            break
    if re0 == None:# 没有任何一个正则表达式匹配到 continue
        continue
    re0 = re0.group()
    print(re0)
    print(page.title())
    page.text = page.text.replace(re0,"")
    # print(page.text)
    page.save("逝世超过一个月 Wikipedia:机器人/申请/Air7538-bot/4 测试")
    