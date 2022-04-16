# -*- coding: UTF-8 -*-
import os, sys, glob, shutil

abspath = os.path.dirname(__file__)
sys.path.append(abspath)

#切换到工作目录
if abspath == '':
    os.chdir(sys.path[0])
else:
    os.chdir(abspath)

search_str = 'client_email'
i = 0
emails_list = []

if __name__ == '__main__':
    All_in_File = glob.glob(r'*.json')
    if len(All_in_File) > 0:
        for infile in All_in_File:
            read_all_lines_list = open(infile, 'r').readlines()
            one_fetch_line_list = [j for j in read_all_lines_list if j.find(search_str) > 0]
            #去垃圾字符
            one_fetch_line_str = ''.join(one_fetch_line_list)
            emails_str = one_fetch_line_str.replace('  "client_email": "', '').replace('",', '')
            emails_list.append(emails_str)
            #进度
            i += 1
            print('Extracting: %d/%d\r' %(i,len(All_in_File)), end='')
            # 逢10插入空行并标记
            if i % 10 == 0:
                emails_list.append('(' + str(i) + '/' + str(len(All_in_File)) + ')')
                emails_list.append('\n''\n')

    #写入
    out_txt = open('email.txt', 'w')
    out_txt.writelines(emails_list)
    out_txt.close()

    #移动文件至email目录
    os.mkdir(abspath + './email')
    shutil.move(''.join(glob.glob(r'*.txt')), os.getcwd() + '/email')
    print('\nAll done.')
    print('email.txt is right here: \n' + os.getcwd() + '\email')