
def run(input_file,html):

    html = html.replace('<code>','<code class="manecode">')
    html = html.replace('<pre','<pre class="prettyprint" ')

    html += """
        <style>
            .manearc .manecode{
                background: rgb(246,248,250);
                padding: 3px 3px 3px 3px;
                border-radius: 3px;
            }            
        </style>
        <script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?lang=vb&amp;skin=sunburst"></script>
    """
    return html