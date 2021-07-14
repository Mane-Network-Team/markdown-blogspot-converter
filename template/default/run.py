import markdown
import importlib

def run(input_file,modules):
    reader = open(input_file,'r',encoding='utf-8')
    # https://python-markdown.github.io/extensions/
    html = markdown.markdown(reader.read(),extensions=['toc','extra','nl2br','sane_lists'])
    writer = open(input_file+".html",'w',encoding='utf-8')

    # sample replace
    html = html.replace('<code>','<code class="manecode">')
    html = html.replace('<pre','<pre class="prettyprint" ')
    html = html.replace('<blockquote','<blockquote class="maneblockquote"')
    
    writer.write('<div class="manearc">')

    for module in modules:
        print("* Using %s module ..." % (module))
        lib = importlib.import_module('module.%s' % (module))
        html = getattr(lib,'run')(input_file,html)
    writer.write(html + '\n')

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
                font-size:15px;
                text-align: inherit;
            }
            .manearc table{
                color: #75758b;
                border-collapse: collapse;
                border: 2px solid;
                padding: 10px;
                box-shadow: 0px 0px #888888;
                border-radius:2px;
                width:100%;
            }
            .manearc table td,.manearc table th {
            border: 1px solid #b3b3b3;
            padding: 8px;
            transition: all 0.3s ease;
            }
            .manearc table th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #494a4c;
            color: white;
            }
            .manearc table tr:nth-child(odd){background-color: #ffffff;}
            .manearc table tr:nth-child(even){background-color: #f2f2f2;}
            .manearc table tr{transition: all 0.3s ease;}
            .manearc table tr:hover {background-color: #ddd;}
            .manearc table td:hover {background-color: #d9d9d9}
        </style>

        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            enableMenu: false,
            extensions: ["tex2jax.js"],
            jax: ["input/TeX", "output/HTML-CSS"],
            tex2jax: {
            displayMath: [ ['$$','$$'] ],
            processEscapes: true
            },
            showMathMenu: false,
            "HTML-CSS": { availableFonts: ["TeX"] }
        });
        </script>

        <script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?lang=vb&amp;skin=sunburst"></script>
        <script async="" id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    """)
   

    # close files
    writer.close()
    reader.close()