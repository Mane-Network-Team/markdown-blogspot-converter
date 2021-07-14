import core.ProcessImg as ProcessImg
def run(input_file,html):
    return_html = ""
    for x in html.split('\n'):
        if (x.find("<img") !=-1):
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(x, 'html.parser')
            for aimg in soup.find_all('img'):
                aimg['src'] = ProcessImg.UrlToBase64(input_file,aimg['src'])
            return_html+=(str(soup) + '\n')
            continue
        return_html+=(x + '\n')
    return return_html