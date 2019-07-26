"""

@Author:jyang
@Date:6/10/2019
"""
from bs4 import BeautifulSoup
import sys
import os


def compare_ignore_diff_rp(p_path, s_path, **kwargs):
    try:
        p_content = open(p_path, 'r', encoding='utf-8').read()
        s_content = open(s_path, 'r', encoding='utf-8').read()
        p_soup = BeautifulSoup(p_content, 'html.parser')
        s_soup = BeautifulSoup(s_content, 'html.parser')
        p_e = p_soup.find(attrs={'name': 'display_local_currency_to_buyer'})
        s_e = s_soup.find(attrs={'name': 'display_local_currency_to_buyer'})
        p_diff = p_e.next.string.strip()
        s_diff = s_e.next.string.strip()
        if p_diff != kwargs['p_diff']:
            print('Compare Failed for prod')
        if s_diff != kwargs['s_diff']:
            print('Compare Failed for stag')

        p_e.next.replace_with(s_e.next)
        with open(kwargs['new_file_path']+os.sep+p_path.split(os.sep)[-1], 'w', encoding='utf-8') as f:
            f.write(p_soup.prettify())

    except IOError as e:
        print(e)


def compare_ignore_diff_sb(p_path, s_path, **kwargs):
    try:
        p_content = open(p_path, 'r', encoding='utf-8').read()
        s_content = open(s_path, 'r', encoding='utf-8').read()
        p_soup = BeautifulSoup(p_content, 'html.parser')
        s_soup = BeautifulSoup(s_content, 'html.parser')
        # p_e = p_soup.find(attrs={'name': 'categorydetail1'})
        # s_e = s_soup.find(attrs={'name': 'categorydetail1'})
        #
        # p_e.replace_with(s_e)
        p_soup.find(attrs={'name': 'category'}).replace_with(s_soup.find(attrs={'name': 'category'}))
        if not os.path.exists(kwargs['new_file_path']):
            os.mkdir(kwargs['new_file_path'])
        with open(kwargs['new_file_path']+os.sep+p_path.split(os.sep)[-1], 'w', encoding='utf-8') as f:
            f.write(p_soup.prettify())

    except IOError as e:
        print(e)
    except AttributeError as e:
        print(e)
        print(p_path)


def compare_ignore_diff_sg(p_path, s_path, **kwargs):
    try:
        p_content = open(p_path, 'r', encoding='utf-8').read()
        s_content = open(s_path, 'r', encoding='utf-8').read()
        p_soup = BeautifulSoup(p_content, 'html.parser')
        s_soup = BeautifulSoup(s_content, 'html.parser')
        p_e = p_soup.find(attrs={'id': 'enablelcforstyleprice'})
        s_e = s_soup.find(attrs={'id': 'enablelcforstyleprice'})
        p_e.replace_with(s_e)

        p_e = p_soup.find(attrs={'id': 'labelforlocalcurrency'})
        s_e = s_soup.find(attrs={'id': 'labelforlocalcurrency'})
        p_e.replace_with(s_e)

        with open(kwargs['new_file_path']+os.sep+p_path.split(os.sep)[-1], 'w', encoding='utf-8') as f:
            f.write(p_soup.prettify())

    except IOError as e:
        print(e)


def compare_ignore_diff_ca_addRm(p_path, s_path, **kwargs):
    try:
        p_content = open(p_path, 'r', encoding='utf-8').read()
        s_content = open(s_path, 'r', encoding='utf-8').read()
        p_soup = BeautifulSoup(p_content, 'html.parser')
        s_soup = BeautifulSoup(s_content, 'html.parser')
        p_e = p_soup.find(attrs={'id': 'enablelcforstyleprice'})
        s_e = s_soup.find(attrs={'id': 'enablelcforstyleprice'})
        p_e.replace_with(s_e)

        p_e = p_soup.find(attrs={'id': 'labelforlocalcurrency'})
        s_e = s_soup.find(attrs={'id': 'labelforlocalcurrency'})
        p_e.replace_with(s_e)

        with open(kwargs['new_file_path']+os.sep+p_path.split(os.sep)[-1], 'w', encoding='utf-8') as f:
            f.write(p_soup.prettify())

    except IOError as e:
        print(e)


def compare_ignore_diff_ca_addRm_difffile(diff_path, **kwargs):
    try:
        p_content = open(diff_path, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(p_content, 'html.parser')
        diffs = soup.find_all(class_='diff')
        flag = True
        for diff in diffs:
            if diff.name=='del':
                if len(list(diff.children))==0:
                    continue
                elif len(list(diff.children))==1:
                    if list(diff.children)[0].string is not None and list(diff.children)[0].string.strip()=='':
                        continue
                    else:
                        flag=False
                        break
                elif len(list(diff.children))==2:
                    if len(list(list(diff.children)[1].children))==6 and list(diff.children)[0].string.strip()=='':
                        print('ok')
                    elif len(list(list(diff.children)[0].children))==1:
                        print('ok')
                    else:
                        flag = False

                else:
                    flag = False
                    break
            else:
                flag=False
                break

        if flag:
           os.remove(diff_path)

    except IOError as e:
        print(e)


def compare_ignore_diff_ca_view(diff_path, **kwargs):
    try:
        p_content = open(diff_path, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(p_content, 'html.parser')
        diffs = soup.find_all(class_='diff')
        if len(soup.find_all(class_='diff'))==1 and len(soup.find_all('del'))==1:
            os.remove(diff_path)
        elif len(diffs)==3:
            if len(soup.find_all('del'))==1 and soup.find('del').next.string.strip()=='':
                if diffs[1].next.string.strip()=='# of Account Groups' and diffs[2].next.string.strip()=='# of Account Groups':
                    os.remove(diff_path)
            elif diffs[0].next.string.strip()=='TY Actual' and diffs[1].next.string.strip()=='TY' and diffs[2].next.string.strip()=='TY':
                os.remove(diff_path)
        elif len(diffs)==5:
            if diffs[0].next.string.strip()=='TY Actual' and diffs[1].next.string.strip()=='TY' and diffs[2].next.string.strip()=='# of Account Groups' and diffs[3].next.string.strip() == 'TY' and diffs[4].next.string.strip()=='# of Account Groups':
                os.remove(diff_path)
        elif len(diffs)==2:
            if diffs[0].next.string.strip()=='TY Actual' and diffs[1].next.string.strip()=='TY':
                os.remove(diff_path)

    except IOError as e:
        print(e)


def compare_ignore_diff_ca_cluser(diff_path, **kwargs):
    try:
        p_content = open(diff_path, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(p_content, 'html.parser')
        if len(soup.find_all(class_='diff'))==2 and len(soup.find_all('del'))==1 and len(soup.find_all('ins'))==1:
            if soup.find('del').find('a')!=None and soup.find('ins').find('a')!=None:
                os.remove(diff_path)
        else:
            diffs = soup.find_all(class_='diff')
            for d in diffs:
                if len(list(d.children))==2 and d.a is not None and d.a.get('title')=='Style Detail':
                    os.remove(diff_path)

    except IOError as e:
        print(e)


def compare_ignore_diff_ca_edit_sg(diff_path, **kwargs):
    try:
        p_content = open(diff_path, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(p_content, 'html.parser')
        if len(soup.find_all(class_='diff'))==2 and len(soup.find_all('del'))==1 and len(soup.find_all('ins'))==1:
            if soup.find('del').label is not None and soup.find('ins').label is not None:
                if soup.find('del').label.get('id')==soup.find('ins').label.get('id'): # 'labelforlocalcurrency'
                    os.remove(diff_path)

    except IOError as e:
        print(e)


def renamed(path):
    r = '_s'
    extension = '.xlsx'
    for i in os.listdir(path):
        if i.find(extension)!=-1:
            new_path = (path+os.sep+i).replace(extension, r + extension)
            os.rename(path+os.sep+i,new_path)


def compare_ignore_diff_others(diff_path, **kwargs):
    try:
        p_content = open(diff_path, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(p_content, 'html.parser')
        diffs = soup.find_all(class_='diff')
        if len(diffs)==2:
            if diffs[1].name=='ins' and list(diffs[1].children)[1].name=='script':
                if diffs[0].name == 'del':
                    if list(diffs[0].children)!=0 or diffs[0].next.string.strip() == '':
                        os.remove(diff_path)
            elif diffs[0].name=='del' and diffs[1].name=='del':
                if len(list(diffs[0].children))==0 and len(list(diffs[1].children))==0:
                    os.remove(diff_path)

    except IOError as e:
        print(e)


if __name__=='__main__':
    # renamed(r'Z:\QA\QA Material\TD\TD comparison\20190618\TD_WS\download_stag')
    p_path = os.sep.join(r'Z:\QA\QA Material\TD\TD comparison\20190617\TD_WS\CA\diff_html_result2'.split('\\'))
    s_path = os.sep.join(r'Z:\QA\QA Material\TD\TD comparison\20190604\TD_WS\SB\stag'.split('\\'))
    new_file_path = p_path + 'New'
    prod_new_path = r'Z:\QA\QA Material\TD\TD comparison\20190604\EF_Comparison\CA\prodNew'
    stag_new_path = r'Z:\QA\QA Material\TD\TD comparison\20190604\EF_Comparison\CA\stagNew'
    kwargs = {
        'p_diff': 'Use USD - US Dollar',
        's_diff': 'Use Default Currency',
        'new_file_path': new_file_path,
        'prod_new_path': prod_new_path,
        'stag_new_path': stag_new_path
    }
    for i in os.listdir(p_path):
        # if i.find('View')!=-1 or i.find('History')!=-1:
        #     compare_ignore_diff_ca_view(p_path + os.sep + i)
        # elif i.find('All Clusters')!=-1:
        #     compare_ignore_diff_ca_cluser(p_path + os.sep + i)
        # elif i.find('Edit Store Group')!=-1:
        #     compare_ignore_diff_ca_edit_sg(p_path + os.sep + i)
    #     # else:
    #     #     if p_path.index('RetailerProfile'):
    #     #         compare_ignore_diff_rp(p_path + os.sep + i, s_path + os.sep + i, **kwargs)
    #     #     elif p_path.index('StoreGroup'):
    #     #         compare_ignore_diff_sg(p_path + os.sep + i, s_path + os.sep + i, **kwargs)
    #
    #     compare_ignore_diff_sb(p_path + os.sep + i, s_path + os.sep + i, **kwargs)
    #     compare_ignore_diff_others(p_path + os.sep + i)
        if i.find('Add Remove ')!=-1:
            compare_ignore_diff_ca_addRm_difffile(p_path + os.sep + i)