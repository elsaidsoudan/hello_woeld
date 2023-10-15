tasks= input(" enter your tasks for today separated by a comma ").split(', ')
don_taskes=[ ]
ongoing_tasks=[ ]
for task in tasks:
    chicout=input(f"{task} \n did you finish it alredy ?(yes/no):")
    if chicout=="yes":
        print("good job \n " + "-"*150)
        don_taskes.append(task)
    else:
        print("try not to put it off\n "+"-"*150)
        ongoing_tasks.append(task)
progress=input(" do you want to see today's progress")
if progress:
    print("*"*20+"don_taskes"+"*"*20 +" \n", don_taskes)
    print("+"*20+"on going taskes"+"+"*20+ "\n",ongoing_tasks)








