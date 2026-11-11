"""
todo-cli_14 —— 一个简洁的命令行待办事项管理工具
作者：周依诺  学号：2025131014
许可证：MIT License
"""
import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_task(text, priority="普通"):
    todos = load_todos()
    todos.append({
        "id": len(todos) + 1,
        "task": text,
        "done": False,
        "priority": priority,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_todos(todos)
    print(f"已添加：[{priority}] {text}")


def list_tasks():
    todos = load_todos()
    if not todos:
        print("暂无待办事项。")
        return
    print(f"{'编号':<4}{'状态':<6}{'优先级':<6}{'内容'}")
    for t in todos:
        status = "✓" if t["done"] else "✗"
        print(f"{t['id']:<4}{status:<6}{t['priority']:<6}{t['task']}")


def done_task(task_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == task_id:
            t["done"] = True
            save_todos(todos)
            print(f"已完成：{t['task']}")
            return
    print(f"未找到编号 {task_id} 的事项。")


def delete_task(task_id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != task_id]
    save_todos(todos)
    print(f"已删除编号 {task_id} 的事项。")


def clear_all():
    save_todos([])
    print("已清空所有待办事项。")


def main():
    import sys
    if len(sys.argv) < 2:
        print("用法: python todo.py <命令> [参数]")
        print("命令: add <内容> [优先级] | list | done <编号> | delete <编号> | clear")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print("请输入待办内容：python todo.py add <内容> [优先级]")
            return
        priority = sys.argv[3] if len(sys.argv) > 3 else "普通"
        add_task(sys.argv[2], priority)
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        done_task(int(sys.argv[2]))
    elif cmd == "delete":
        delete_task(int(sys.argv[2]))
    elif cmd == "clear":
        clear_all()
    else:
        print(f"未知命令：{cmd}")


if __name__ == "__main__":
    main()
