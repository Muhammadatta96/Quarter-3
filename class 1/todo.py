import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    return json.load(open(TODO_FILE)) if os.path.exists(TODO_FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(TODO_FILE, "w"), indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""

@click.command()
@click.argument("task")
def add(task):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added: {task}")

@click.command()
def list():
    """List tasks"""
    tasks = load_tasks()
    if not tasks:
        return click.echo("No tasks found.")
    for i, t in enumerate(tasks, 1):
        click.echo(f"{i}. {t['task']} [{'✅' if ['done'] else '❌'}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark task as done"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} completed")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        click.echo(f"Removed: {tasks.pop(task_number - 1)['task']}")
        save_tasks(tasks)
    else:
        click.echo(f"Invalid task number: {task_number}")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
