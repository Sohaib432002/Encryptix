#Encriptx internship

#Task No 1


"""#A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing

users to create, update, and track their to-do lists"""

class ToDoList:
    def __init__(self):
        self.list_high = []
        self.list_medium = []
        self.list_low = []

    def add_task(self):
        print('You want to add a task')
        print('Which task do you want to add? high_level(press 1)/medium level(press 2)/low level(press 3)')
        task_type = int(input())
        if task_type == 1:
            task = input('Enter a high level task:')
            self.list_high.append(task)
        elif task_type == 2:
            task = input('Enter a medium level task:')
            self.list_medium.append(task)
        elif task_type == 3:
            task = input('Enter a low level task:')
            self.list_low.append(task)

    def view_task(self):
        print('You want to view the task')
        print('Which task do you want to view? high_level(press 1)/medium level(press 2)/low level(press 3)')
        task_type = int(input())
        if task_type == 1:
            print('Your high level tasks are:')
            for i in self.list_high:
                print(i)
        elif task_type == 2:
            print('Your medium level tasks are:')
            for i in self.list_medium:
                print(i)
        elif task_type == 3:
            print('Your low level tasks are:')
            for i in self.list_low:
                print(i)

    def delete_task(self):
        print('You want to delete the task')
        print('Which task do you want to delete? high_level(press 1)/medium level(press 2)/low level(press 3)')
        task_type = int(input())
        if task_type == 1:
            print('Which high level task do you want to delete?')
            for i, task in enumerate(self.list_high, start=1):
                print(f"{i}. {task}")
            del_task_no = int(input('Enter the task number:'))
            if 0 < del_task_no <= len(self.list_high):
                self.list_high.pop(del_task_no - 1)
        elif task_type == 2:
            print('Which medium level task do you want to delete?')
            for i, task in enumerate(self.list_medium, start=1):
                print(f"{i}. {task}")
            del_task_no = int(input('Enter the task number:'))
            if 0 < del_task_no <= len(self.list_medium):
                self.list_medium.pop(del_task_no - 1)
        elif task_type == 3:
            print('Which low level task do you want to delete?')
            for i, task in enumerate(self.list_low, start=1):
                print(f"{i}. {task}")
            del_task_no = int(input('Enter the task number:'))
            if 0 < del_task_no <= len(self.list_low):
                self.list_low.pop(del_task_no - 1)

    def complete_task(self):
        list_high_task_completed = []
        list_medium_task_completed = []
        list_low_task_completed = []
        print('You want to complete the task')
        print('Which task do you want to complete? high_level(press 1)/medium level(press 2)/low level(press 3)')
        task_type = int(input())
        if task_type == 1:
            print('Which high level task did you complete?')
            for i, task in enumerate(self.list_high, start=1):
                print(f"{i}. {task}")
            complete_task_no = int(input('Enter the task number:'))
            if 0 < complete_task_no <= len(self.list_high):
                list_high_task_completed.append(self.list_high.pop(complete_task_no - 1))
        elif task_type == 2:
            print('Which medium level task did you complete?')
            for i, task in enumerate(self.list_medium, start=1):
                print(f"{i}. {task}")
            complete_task_no = int(input('Enter the task number:'))
            if 0 < complete_task_no <= len(self.list_medium):
                list_medium_task_completed.append(self.list_medium.pop(complete_task_no - 1))
        elif task_type == 3:
            print('Which low level task did you complete?')
            for i, task in enumerate(self.list_low, start=1):
                print(f"{i}. {task}")
            complete_task_no = int(input('Enter the task number:'))
            if 0 < complete_task_no <= len(self.list_low):
                list_low_task_completed.append(self.list_low.pop(complete_task_no - 1))
        return list_high_task_completed, list_medium_task_completed, list_low_task_completed

    def update_task(self):
        print('You want to update a task')
        print('Which task do you want to update? high_level(press 1)/medium level(press 2)/low level(press 3)')
        task_type = int(input())
        if task_type == 1:
            print('Which high level task do you want to update?')
            for i, task in enumerate(self.list_high, start=1):
                print(f"{i}. {task}")
            update_task_no = int(input('Enter the task number:'))
            if 0 < update_task_no <= len(self.list_high):
                new_task = input('Enter the new task: ')
                self.list_high[update_task_no - 1] = new_task
        elif task_type == 2:
            print('Which medium level task do you want to update?')
            for i, task in enumerate(self.list_medium, start=1):
                print(f"{i}. {task}")
            update_task_no = int(input('Enter the task number:'))
            if 0 < update_task_no <= len(self.list_medium):
                new_task = input('Enter the new task: ')
                self.list_medium[update_task_no - 1] = new_task
        elif task_type == 3:
            print('Which low level task do you want to update?')
            for i, task in enumerate(self.list_low, start=1):
                print(f"{i}. {task}")
            update_task_no = int(input('Enter the task number:'))
            if 0 < update_task_no <= len(self.list_low):
                new_task = input('Enter the new task: ')
                self.list_low[update_task_no - 1] = new_task

    def __str__(self):
        return f"ToDoList(high={self.list_high}, medium={self.list_medium}, low={self.list_low})"


if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print('''What do you want to do?
        ADD (press 1)
        View (press 2)
        Update (press 3)
        Complete (press 4)
        Remove (press 5)
        Exit (press 6)''')
        task = int(input())
        if task == 1:
            todo_list.add_task()
        elif task == 2:
            todo_list.view_task()
        elif task == 3:
            todo_list.update_task()
        elif task == 4:
            print(todo_list.complete_task())
        elif task == 5:
            todo_list.delete_task()
        elif task == 6:
            print('Exiting the program.')
            break
        else:
            print('Invalid option. Please try again.')

    print(todo_list)
