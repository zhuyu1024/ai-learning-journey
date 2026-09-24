# -*- coding: utf-8 -*-
"""练习 2：装饰器（decorator）

学习目标：会写、会读装饰器。pytest 的 @pytest.fixture、很多框架的 @app.get
本质都是装饰器，做测试的你其实天天在用它的语法。

参考文档：
- 廖雪峰 Python 教程（搜索"廖雪峰 装饰器"）

任务：
1. 先直接运行本文件，观察输出，理解"函数可以被当参数传来传去"
2. 补全 timer 装饰器：让它打印出被装饰函数的执行耗时
3. 给 slow_add 和 slow_search 都加上 @timer，运行验证
"""
import time
import functools


# ===== 任务：补全这个装饰器 =====
def timer(func):
    @functools.wraps(func)  # 保持原函数名不变，固定写法
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # 调用原函数
        # TODO 1：在这里计算耗时（提示：time.time() - start），用 print 打印
        # 打印格式建议：f"{func.__name__} 耗时 {耗时:.3f} 秒"
        # TODO 2：把 result 返回出去（提示：return result）
        return result

    return wrapper


# ===== 加上 @timer 后，运行时应该自动打印耗时 =====
@timer
def slow_add(a, b):
    time.sleep(0.5)  # 假装在干活
    return a + b


@timer
def slow_search(keyword, items):
    time.sleep(1.0)
    return [i for i in items if keyword in i]


if __name__ == "__main__":
    print(slow_add(1, 2))
    print(slow_search("test", ["unit test", "integration test", "docs"]))
