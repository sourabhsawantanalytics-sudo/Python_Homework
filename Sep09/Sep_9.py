# Can we change global variable value from local scope?
# Yes

count = 0
def increase():
    global count  # (Without global python assume any variable inside function is local)
    count+=1
increase()
print(count)