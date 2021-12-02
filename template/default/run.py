import markdown
import importlib

def run(input_file,modules):
    reader = open(input_file,'r',encoding='utf-8')
    # https://python-markdown.github.io/extensions/
    extens = ['toc','extra','sane_lists',
        "pymdownx.tasklist",
        "pymdownx.critic",
        "pymdownx.tilde",'nl2br',
    ]

    html = markdown.markdown(reader.read(),extensions=extens)
    writer = open(input_file+".html",'w',encoding='utf-8')

    # sample replace
    html = html.replace('<blockquote','<blockquote class="maneblockquote"')
    html = html.replace('<code>','<code class="manecode">')

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
                transition:0.5s;
            }
            .manearc a:hover{
                color:#69ad4b
            }
            .manearc .maneblockquote{
                color: #777777; 
                margin-inline-start: 0px;
                margin-inline-end: 0px;
                padding-left:15px;
                border-left: 5px solid #dfe2e5;
                font-size:15px;
                text-align: inherit;
                font-style:normal;
                line-height: 20px;
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

            .manearc .manecode{
                background: rgb(245 245 245);
                padding: 2px 2px 2px 2px;
                border-radius: 3px;
                transition: 0.5s;
            }     
            .manearc .manecode:hover{
                background: #757575;
                color: whitesmoke;
            } 
            .manearc p {
                transition: 0.5s;
            }
            .manearc p:hover{color:#000}
        </style>


    """)
   

    # close files
    writer.close()
    reader.close()