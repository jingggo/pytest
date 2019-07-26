from bs4 import BeautifulSoup

def soup_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_zsrows_tags(soup):
    div_rows=list(soup.find_all("div",attrs={"zs.t":"SRow"}))
    return div_rows

def get_zscells_string(zsrow):
    zscells_data = []
    zscells = zsrow.find_all(class_="zscelltxt-real")
    for zscell in zscells:
        zscell_str = zscell.string
        zscells_data.append(zscell_str)
    return zscells_data

def get_zs_table_from_html(html):
    '''Input is the html format content in door info zsscroll div, and return is the list of the real datas in each zk cell'''
    rows_str = []
    #f = open(r'C:\Users\jyang\Desktop\doordatas.txt','r+')
    soup = soup_html(html)

    zsrows = get_zsrows_tags(soup)

    for row in zsrows:
        cells = get_zscells_string(row)
        rows_str.append(cells)
    return rows_str

if __name__ == '__main__':
    get_zs_table_from_html(html)