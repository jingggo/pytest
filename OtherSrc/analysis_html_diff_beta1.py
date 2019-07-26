import difflib
import bs4
from bs4 import BeautifulSoup
import re


def compare_html(prod, stag):
    if (isinstance(prod, str)):
        diffs = difflib.ndiff(prod.splitlines(), stag.splitlines())
    else:
        diffs = difflib.ndiff(prod.readlines(), stag.readlines())
    return list(diffs)


def get_prod_diffs(diffs):
    """return is list, return is list of strings"""
    prod_diffs = []
    for prod_diff in diffs:
        if (prod_diff[0:2] == '- '):
            prod_diffs.append(prod_diff[2:])
    return prod_diffs


def get_stag_diffs(diffs):
    stag_diffs = []
    for stag_diff in diffs:
        if (stag_diff[:2] == '+ '):
            stag_diffs.append(stag_diff[2:])
    return stag_diffs


def add_diff_class(tag):
    for t in tag.descendants:
        if (isinstance(t, bs4.element.Tag)):
            if (t.has_attr('class')):
                t['class'].append('diff')
            else:
                #        print(tag)
                t['class'] = ['diff']


# print(str(tag))

def make_class_diff_tags(diffs):
    '''the argument is the prod_diffs or stage_diffs in list, and return is list of strings'''
    prods = []
    for diff in diffs[:5]:
        div_diff = '<div>' + diff + '</div>'

        div_soup = BeautifulSoup(div_diff, 'html.parser')
        src_soup = BeautifulSoup(diff, 'html.parser')
        #        soup.new_tag('div')
        tar_tag = src_soup

        if (isinstance(tar_tag, bs4.element.NavigableString)):
            '''This includes string with no tag and comment'''
            tar_tag = div_soup
        # print('string')
        #        print(tar_tag)
        add_diff_class(tar_tag)
        #        print(tar_tag)
        prod_diff_str = str(tar_tag)
        #        print(soup.prettify())
        prods.append(prod_diff_str)
    # prods.remove('''<div class="diff">'\n'</div>''')
    return prods


def make_html_diffs(html_lines, diffs, class_diffs):
    html_class_diff = ''
    #    for html_line in html_lines:
    #        if(html_line in diffs):
    #            index = diffs.index(html_line)
    #            html_class_diff += class_diffs[index]
    #        else:
    #            html_class_diff += html_line

    for diff, class_diff in zip(diffs, class_diffs):
        #        print(diff,class_diff)
        if diff in html_lines:
            index = html_lines.index(diff)
            html_lines.pop(index)
            '''&nbsp to transfer to space'''
            class_diff_re = class_diff.replace('\xa0', ' ')
            html_lines.insert(index, class_diff_re)
        html_class_diff = ''.join(html_lines)
    return html_class_diff

def comlete_html_div(html_prod_part, html_stag_html):
    html_pre = '''<html><head><style>
.wrap{display: flex;}
.prod{width: 50%;}
.stag{width: 50%;}
.diff{color: #000000; background-color: #FFE3E3;}
</style></head>
<body>
'''
    html_end = '''</body></html>'''
    html_part = '''<div class="wrap"><div class="prod">Prod</div><div class="stag">Stag</div></div><div class="wrap"><div class="prod">{}</div><div class="stag">{}</div></div>'''.format(
        html_prod_part, html_stag_html)
    html = html_pre + html_part + html_end
    #    html.replace('<div class="diff">\n</div>','')

    return html


def process_to_compare(prod, stag, output):
    html_prod = open(prod, "r+", encoding='utf-8')
    html_stag = open(stag, "r+", encoding='utf-8')
    html_prod_lines = html_prod.readlines()
    html_stag_lines = html_stag.readlines()

    diffs = list(difflib.ndiff(html_prod_lines, html_stag_lines))
    prod_diffs = get_prod_diffs(diffs)
    prod_class_diffs = make_class_diff_tags(prod_diffs)
    prod_html_diff = make_html_diffs(html_prod_lines, prod_diffs, prod_class_diffs)

    stag_diffs = get_stag_diffs(diffs)
    stag_class_diffs = make_class_diff_tags(stag_diffs)
    stag_html_diff = make_html_diffs(html_stag_lines, stag_diffs, stag_class_diffs)

    complete_ht = comlete_html_div(prod_html_diff, stag_html_diff)

    diff_tags = r'E:\CompareFiles\analysis\stag_prod_diff__per_tags1.htm'
    with open(diff_tags, 'w+') as dt:
        dt.write(str(prod_class_diffs))

    diff_tags = r'E:\CompareFiles\analysis\stag_stag_diff_per_tags1.htm'
    with open(diff_tags, 'w+') as dt:
        dt.write(str(stag_class_diffs))

    with open(output, 'w+', encoding='utf-8') as op:
        op.write(complete_ht)

    html_prod.close()
    html_stag.close()

prod_dir = r'Z:\QA\QA Material\TD\TD comparison\test\prod'
stag_dir = r'Z:\QA\QA Material\TD\TD comparison\test\stag'
diff_dir = r'Z:\QA\QA Material\TD\TD comparison\test\diff_html'
file_name = "seasonal notes_pcheng.htm"

prod = prod_dir + '\\' + file_name
stag = stag_dir + '\\' + file_name
prod_temp_output = diff_dir + '\\' + file_name

process_to_compare(prod, stag, prod_temp_output)
# html_prod=open(prod,"r+")
# html_stag=open(stag,"r+")
# html_prod_lines = list(html_prod.readlines())
# html_stag_lines = list(html_stag.readlines())
# diffs = list(difflib.ndiff(html_prod_lines,html_stag_lines))
#
# stag_diffs = get_stag_diffs(diffs)
# stag_class_diffs = make_class_diff_tags(stag_diffs)
# stag_html_diff = make_html_diffs(html_stag_lines,stag_diffs,stag_class_diffs)
def ono():
    if(True):
        print("ha")
