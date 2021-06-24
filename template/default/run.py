from os import read
import markdown
def run(output_file):
    reader = open(output_file,'r',encoding='utf-8')
    # https://python-markdown.github.io/extensions/
    html = markdown.markdown(reader.read(),extensions=['extra'])
    writer = open(output_file+".html",'w',encoding='utf-8')

    # inject
    html = html.replace('<code>','<code class="manecode">')
    html = html.replace('<pre','<pre class="prettyprint" ')
    html = html.replace('<blockquote','<blockquote class="maneblockquote"')
    
    writer.write('<div class="manearc">')
    writer.write(html)
    writer.write('\n</div>')

    # inject class / js
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
        }
    </style>
    """)
    writer.write('<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?lang=vb&amp;skin=sunburst"></script>' + '\n')

    # close files
    writer.close()
    reader.close()