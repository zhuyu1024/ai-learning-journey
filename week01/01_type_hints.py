# -*- coding: utf-8 -*-
"""练习 1：类型注解（type hints）

学习目标：看懂并会写类型注解。AI 开源项目里到处都是，必须熟练。

参考文档：
- 廖雪峰 Python 教程（搜索"廖雪峰 类型注解"）
- 官方文档：https://docs.python.org/zh-cn/3/library/typing.html

任务：把下面所有函数的参数和返回值补上类型注解，然后运行确认无报错。
做完后 git add 一下这个文件，就是今天的一次 commit。
"""
from typing import Optional


# 任务 1：给参数 name 和返回值加注解（提示：name 是 str，返回值是 str）
def greet(name):
    return f"你好, {name}"


# 任务 2：times 有默认值，score 可能为 None（提示：用 Optional[float]）
def calc_average(times: int, score=None):
    if score is None:
        return None
    return score * times


# 任务 3：这个函数接收一个"字符串列表"，返回"排序后的字符串列表"（提示：list[str]）
def sort_names(names):
    return sorted(names)


if __name__ == "__main__":
    print(greet("zhuyu"))
    print(calc_average(3, 85.5))
    print(calc_average(3))
    print(sort_names(["pytest", "unittest", "robot"]))
