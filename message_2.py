def show_magicians(printed_names):
    for printed_name in printed_names:
        print(printed_name.title())

def make_great(changed_lists):
    for i in range(4):
#####先用变量i来作为一个标志，然后用range()函数创建0、1、2、3四个数字，
#####用来对应魔术师姓名列表的四个姓名，最后用for循环将姓名之前加上”The Great”,循环结束后返回
        changed_lists[i] = 'the Great ' + changed_lists[i]
    return changed_lists

magicians = ['job', 'jane', 'stand', 'smile']
magicians_2=magicians[:]######创建副本
make_great(magicians_2)
show_magicians(magicians_2)
	
	
	
