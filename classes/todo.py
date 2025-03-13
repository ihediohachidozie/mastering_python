from tabulate import tabulate

def main():
    
  pass

action = []
todo_list = {}
activity = input('What activity do you want to do today? ')
deadline = input("What's the deadline date: ")


todo_list['Activity'] = activity
todo_list['Date'] = deadline
action.append(todo_list)

table = tabulate(action, headers='keys', tablefmt='grid')
print(table)


