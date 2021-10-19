
def run(input_file,html):
    html += """
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
    <script async="" id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    """
    return html