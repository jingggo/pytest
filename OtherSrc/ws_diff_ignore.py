"""

@Author:jyang
@Date:6/19/2019
"""
import os,xlrd,xlwt,openpyxl,types
import math,string,time,sys,zipfile
import sys
from win32com.client import Dispatch

def one_ws(path):
    flag = True
    newlines = []
    ignores = [
        '[199.0,200.0]',
        '[203.0,204.0]',
        '[191.0,192.0]',
        '[190.0,197.0]',
        '[192.0,193.0]',
        '[193.0,194.0]',
    ]
    with open(path, 'r') as f5:
        for line in f5.readlines():
            if line.find('row')!=-1:
                l = line[line.find('row'):]
                ls = l.split('---')[1:]
                for i in ls:
                    if ignores.count(i[i.index('['):i.index(']')+1])==0:
                        flag = False
                        newlines.append(line)
                        break
            else:
                newlines.append(line)

    with open(path[:path.index('.')]+'_new.txt','w') as f1:
        f1.writelines(newlines)


def compareXLSX(prodf,stagef,diff_dir=None):
    '''

    :param prodf:
    :param stagef:
    :param diff_dir: the path to store diff file if exist, notice: extension is .xlsx
    :return:
    '''
    error_flag = False
    if diff_dir is None:
        diff_dir = stagef
    dir = diff_dir.replace(".xlsx",".txt")
    error_info=""
    if(prodf == None or stagef == None ):
        error_flag = True
        error_info="Report isn't generated!"
    elif (prodf.find("xlsx") == -1 or stagef.find("xlsx") == -1 ) :
        error_flag = True
        error_info="Report isn't XLSX!"
    else:
        pbook= openpyxl.load_workbook(prodf, data_only=True)
        sbook= openpyxl.load_workbook(stagef, data_only=True)
        if (len(pbook.get_sheet_names()) != len(sbook.get_sheet_names()) ):
            error_flag = True
            error_info = error_info+ "tabs count diff \n"
        else:
            for i in range(0,len(sbook.get_sheet_names())):
                psh = pbook.worksheets[i]
                ssh = sbook.worksheets[i]
                maxrows = max(psh.max_row, ssh.max_row)
                maxcols = max(psh.max_column, ssh.max_column)
                if (psh.title == ssh.title):
                    for j in range(1, maxrows+1):
                        row_diffCount = 0
                        for k in range(1, maxcols+1):
                            if (psh.cell(row=j, column=k).value != ssh.cell(row=j, column=k).value ):
                                error_flag = True
                                row_diffCount +=1
                                if(row_diffCount == 1):
                                    error_info = error_info+("\n diff---%s---row%d" %(psh.title,j))
                                error_info = error_info+("---col%d[%s,%s]" %(k,ssh.cell(row=j, column=k).value,psh.cell(row=j, column=k).value ))
                else:
                    error_flag = True
                    error_info = error_info+("diff ---  %s\ %s; ---- rows:\  %s\%s;---- cols:\  %s\%s.\n" %(ssh.title, psh.title ,ssh.max_row,psh.max_row,ssh.max_column,psh.max_column))
                    for m in range(1, maxrows+1):
                        row_diffCount = 0
                        for n in range(1, maxcols+1):
                            if (psh.cell(row=m, column=n).value != ssh.cell(row=m, column=n).value ):
                                row_diffCount +=1;
                                if(row_diffCount == 1):
                                    error_info = error_info+("\n diff---row%d" %(m))
                                error_info = error_info+("---col%d[%s,%s]" %(n,ssh.cell(row=m, column=n).value ,psh.cell(row=m, column=n).value))
    if(error_flag):
        diff_file = open(dir,"w")
        diff_file.write(error_info)
        diff_file.close()
        raise Exception("Excels are diff or not generated!")
    else:
        print("Same excels!")


def just_open(filename):
    '''
    Before compare xlsx with data-only, need to save the file first, or else, value with formula would be None.
    :param filename:
    :return:
    '''
    xlApp = Dispatch("Excel.Application")
    xlApp.Visible = False
    xlBook = xlApp.Workbooks.Open(filename)
    xlBook.Save()
    xlBook.Close()

if __name__ == '__main__':
    # path = r'Z:\QA\QA Material\TD\TD comparison\20190619\TD_WS\original diff'
    # for i in os.listdir(path):
    #     if (path+os.sep+i).find('.txt')!=-1:
    #         one_ws(path+os.sep+i)
    # p = r'Z:\QA\QA Material\TD\TD comparison\20190620\download_prod\20056666asung_JPN WH_p.xlsx'
    # s = r'Z:\QA\QA Material\TD\TD comparison\20190620\download_stag\20056666asung_JPN WH_s.xlsx'
    # just_open(s)
    # just_open(p)
    # compareXLSX(p,s,s)

    parent_path = r'Z:\QA\QA Material\TD\TD comparison\20190619\TD_WS'
    p = parent_path + os.sep + 'download_prod'
    s = parent_path + os.sep + 'download_stag'
    ignores = [

    ]
    for i in os.listdir(p)[5:]:
        if i.count('.xlsx'):
            if not ignores.count(i):
                just_open(p+os.sep+i)
                just_open(s+os.sep+i)
                try:
                    compareXLSX(p+os.sep+i, s+os.sep+i, parent_path+os.sep+i)
                except Exception as e:
                    print(e)

