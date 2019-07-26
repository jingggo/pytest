"""

@Author:jyang
@Date:7/5/2019
"""


def get_casenames(path):
    casenames = []
    with open(path, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            if l.count('<casename>')==1:
                l = l.replace('<casename>', '')
                l = l.replace('</casename>', '')
                casenames.append(l.strip())
    return casenames


if __name__ == '__main__':
    path = r'E:\CMM\src\test\resources\CAPTYTest.xml'
    cases = get_casenames(path)
    print('There are {0} cases'.format(len(cases)))
    for c in cases:
        print(c)