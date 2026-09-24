# -*- coding: utf-8 -*-
"""本周产出：测试用例生成器（命令行版）

用法（Week 1 周三之前逐步实现）：
    python gen_cases.py 需求文档.txt

实现步骤（按顺序做，每完成一步 commit 一次）：
    第 1 步：读取 txt 文件内容（明天做：周五注册完 API Key 后）
    第 2 步：调用 LLM API（DeepSeek 或智谱），system prompt 写死为
            "你是资深测试工程师，根据需求输出测试用例，JSON 格式"
    第 3 步：解析返回的 JSON，格式化打印到控制台
    第 4 步：支持 --output 参数，把结果存成 JSON 文件

前置准备（周五做）：
    1. 注册 https://platform.deepseek.com ，充值 10 元
    2. 创建 API Key
    3. 在本文件同目录建一个 .env 文件，内容一行：
       DEEPSEEK_API_KEY=sk-xxxxx
    （.env 已被 .gitignore 排除，Key 不会被提交到 GitHub）
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="测试用例生成器")
    parser.add_argument("requirement_file", help="需求文档 txt 路径")
    args = parser.parse_args()

    print(f"TODO：读取 {args.requirement_file} 并调用 LLM 生成测试用例")
    # TODO 第 1 步（周五开始）：with open(args.requirement_file, encoding="utf-8") as f: ...


if __name__ == "__main__":
    main()
