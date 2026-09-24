# -*- coding: utf-8 -*-
"""练习 3：asyncio 异步基础

学习目标：会看懂 async/await 代码，理解"并发请求 LLM 时为什么快"。
这周只需要会"用"，事件循环原理等 Week 4 用到再回来补。

参考文档：
- 廖雪峰 Python 教程（搜索"廖雪峰 asyncio"）

任务：
1. 直接运行本文件，对比"串行版"和"异步版"的总耗时（应该差 3 倍左右）
2. 思考题（写在文件末尾注释里）：如果要把并发数从 3 提到 50，
   串行版和异步版分别会发生什么？
"""
import asyncio
import time


# 假装这是一个调用 LLM API 的函数（真实场景就是 openai/deepseek SDK 的异步客户端）
async def fake_llm_call(prompt: str) -> str:
    print(f"  开始处理: {prompt}")
    await asyncio.sleep(1)  # 假设 API 要 1 秒才返回
    return f"{prompt} -> 已生成"


# ========== 串行版：一个一个等 ==========
async def run_serial():
    results = []
    for p in ["用例1", "用例2", "用例3"]:
        results.append(await fake_llm_call(p))  # 每个都要等上一个完成
    return results


# ========== 异步版：三个一起发出去 ==========
async def run_parallel():
    results = await asyncio.gather(  # gather = 同时跑多个协程
        fake_llm_call("用例1"),
        fake_llm_call("用例2"),
        fake_llm_call("用例3"),
    )
    return results


if __name__ == "__main__":
    print("== 串行版 ==")
    t0 = time.time()
    asyncio.run(run_serial())
    print(f"总耗时: {time.time() - t0:.2f} 秒\n")

    print("== 异步版 ==")
    t0 = time.time()
    asyncio.run(run_parallel())
    print(f"总耗时: {time.time() - t0:.2f} 秒")
