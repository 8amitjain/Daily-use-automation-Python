import os

os.chdir(r'E:\some-folder\some-folder')   # path of folder
print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('.'))
    try:
        t1, t2, t3 = file_name.split('.')   # add or delete number of variable according to requirement
        new_name = '{}-{}{}'.format(t1, t2, file_ext)   # change name according to requirement
        print(new_name)    # printing  new name
        # os.rename(f, new_name)  # changing file name non reversible proceed with caution
    except ValueError:
        pass
