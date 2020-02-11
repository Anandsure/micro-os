import os
parent_dir = "/Users/anand/Desktop/new_os/os"
while True:
    cmd = input().lower()
    if 'create' in cmd:
        if 'folder' in cmd:
            c=0
            ind = -1
            for i in cmd:
                ind+=1
                if i == ' ':
                    c+=1
                if c==2:
                    directory = cmd[ind+1::]
                    break

            path = os.path.join(parent_dir, directory)
            print(path)
            os.mkdir(path,0o666)

        if 'file' in cmd:
            ta=[]
            c=0
            ind = -1
            for i in cmd:
                ind+=1
                if i == ' ':
                    c+=1
                if c==2:
                    f_name = cmd[ind+1::]
                    break
            #print(f_name)
            f_name="/"+f_name+".txt"
            #print(f_name)
            while True:
                n = input()
                if n == 'end':
                    break
                else:
                    ta.append(n+'\n')
            f = open(parent_dir+f_name, "w+")
            for i in ta:
                f.write(i)
            f.close()