import wordcloud
file = open('words.txt', encoding='utf-8')
text = file.read()
stopwords = {"野生技术协会", "编程", "教育", "讲座", "变成技术宅", "教学", "电脑", "技术", "编程教育", "编程入门",
             "开发", "科学", "演示", "软件", "编程视频教程", "编程课程", "教学视频", "经验分享", "IT", "编程语言", "编程学习",
             "互联网", "考试", "考研", "科技", "语言", "技术宅", "面试", "自学", "原创", "公开课", "程序员", "学习", "课程",
             "教程", "计算机", "线上课堂", "视频教程", "数码", "科普", "生活", "全能打卡挑战", "DIY", "机械",
             "趣味", "人文", "趣味科普人文", "自制", "搞笑", "制作", "设计", "学习心得", "加工中心", "校园", "代码",
             "黑科技", "制造", "bilibili新星计划", "码农"}
wc = wordcloud.WordCloud(font_path="SIMYOU.TTF", stopwords=stopwords)
wc.generate(text)
image = wc.to_image()
image.show()
