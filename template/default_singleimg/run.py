import markdown
import core.ProcessImg as ProcessImg

def run(input_file):
    reader = open(input_file,'r',encoding='utf-8')
    # https://python-markdown.github.io/extensions/
    html = markdown.markdown(reader.read(),extensions=['extra','nl2br','sane_lists'])
    writer = open(input_file+".html",'w',encoding='utf-8')

    # sample replace
    html = html.replace('<code>','<code class="manecode">')
    html = html.replace('<pre','<pre class="prettyprint" ')
    html = html.replace('<blockquote','<blockquote class="maneblockquote"')
    
    writer.write('<div class="manearc">')

    # process stream
    for x in html.split('\n'):
        # process image
        if (x.find("<img") !=-1):
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(x, 'html.parser')
            for aimg in soup.find_all('img'):
                aimg['src'] = ProcessImg.UrlToBase64(input_file,aimg['src'])
            writer.write(str(soup) + '\n')
            continue
        writer.write(x + '\n')
    writer.write('\n</div>')

    # add class / js
    writer.write("""
    <style>
        .manearc h1,h2{
            padding-bottom: 0px;
            border-bottom: 1px solid rgba(204, 204, 204, 0.281);
            line-height: 200%;
        }
        .manearc a{
            text-decoration: none;
            color: rgb(147, 196, 125);
        }
        .manearc .manecode{
            background: rgb(246,248,250);
            padding: 3px 3px 3px 3px;
            border-radius: 3px;
        }
        .manearc .maneblockquote{
			color: #777777; 
			margin-inline-start: 0px;
			margin-inline-end: 0px;
			padding-left:15px;
            border-left: 5px solid #dfe2e5;
            font-size:15px;
            text-align: inherit;
        }
    </style>

    <script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?lang=vb&amp;skin=sunburst"></script>
    """)

    # close files
    writer.close()
    reader.close()