import time as t
class MyTimer():
    def __init__(self):
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.borrow = [9999, 12, 30, 24, 60, 60]
        self.unit = ['年', '月', '日', '时', '分', '秒']

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.prompt

    def start(self):
        if not self.begin:
            self.begin = t.localtime()
            self.prompt = '请先执行stop操作'
            print('计时开始')
        else:
            print('计时已经开始')

    def stop(self):
        if self.begin:
            self.end = t.localtime()
            self.calc()
            print('计时结束')
        else:
            print('请先执行start操作')

    def calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for i in range(6):
            temp = self.end[i]-self.begin[i]
            if temp < 0:
                x = 1
                while self.lasted[i - x] < 1:
                    self.lasted[i - x] = self.borrow[i - x] - 1
                    x += 1
                self.lasted[i - x] -= 1
                temp += self.borrow[i]
            self.lasted.append(temp)
        for i in range(6):
            if self.lasted[i]:
                self.prompt += str(self.lasted[i]) + self.unit[i]
        self.begin = 0
        self.end = 0
    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for i in range(6):
            temp = self.lasted[i] + other.lasted[i]
            if temp >= self.borrow[i]:
                x =1
                while result[i - x] == self.borrow[i] - 1:
                    result[i - x] = 0
                result[i - x] += 1
                temp -= self.borrow[i]
            result.append(temp)
        for i in range(6):
            if result[i]:
                prompt += str(result[i]) + self.unit[i]
        return prompt
