# on https://haozi.moe/2019/08/28/hexo%E6%9B%BF%E6%8D%A2%E4%BB%A3%E7%A0%81%E9%AB%98%E4%BA%AE%E4%B8%BAace-js/

def run(input_file,html):
    html += """
<script src="https://code.jquery.com/jquery-3.6.0.min.js" type="text/javascript" charset="utf-8"></script>
<script src="https://pagecdn.io/lib/ace/1.4.12/ace.min.js" type="text/javascript" charset="utf-8"></script>
<script src="https://pagecdn.io/lib/ace/1.4.12/ext-static_highlight.min.js" type="text/javascript" charset="utf-8"></script>

<script>
    (async () => {

        if(document.getElementsByTagName('pre').length === 0) {
            console.log('Ace.js 未加载 -> 没有找到代码段');
            return;
        }

        const base_url = 'https://pagecdn.io/lib/ace/1.4.12/';

        const get_script = function (url) {
            return new Promise((s, j) => {
                $.getScript(url, s, j );
            })
        };

        // 这里设置ace加载解析器的基础地址, 自己部署的话设置为自己ace.js组件的地址, 这里使用的是CDN的
        ace.config.set('basePath', base_url);
        const highlight = ace.require("ace/ext/static_highlight");

        // 搜索 pre code 解构的块, 进行着色
        [].map.call(document.querySelectorAll('pre code'), ((el) => {
            // 如果已经被设置了ace-mode的话, 这个块已经是被高亮过了, 就不重复了
            if (el.getAttribute( 'ace-mode'))
            return;
            // 拆分class
            const p = el.className.split(' ').map(v => v.replace(/ /g,''));
            // Typora to know words
            // https://pagecdn.com/lib/ace

            var convert_keyword = {
                "c#":"csharp", "js":"javascript","c++":"c_cpp",
                "c":"c_cpp", "bash":"sh","shell":"sh"
            }
            
            var langu = p[0].replace("language-","")  || "plain_text"
            if (langu in convert_keyword){
                langu = convert_keyword[langu]
            }

            // 这里是设置着色的语言
            el.setAttribute('ace-mode', 'ace/mode/' + (langu));
            // 这里可以修改主题颜色
            el.setAttribute('ace-theme', 'ace/theme/crimson_editor');
            el.setAttribute('gutter',  p[3] || true);
            highlight(el, {
                mode: el.getAttribute("ace-mode"),
                theme: el.getAttribute("ace-theme"),
                startLineNumber: 1,
                trim: true,
                showGutter: el.getAttribute("gutter"),
            });
        }));
    })();
</script>
<style>
    .ace_line {transition: all 0.3s ease;}
    .ace_line:hover {background-color: #e8e8e8}
    .ace-crimson-editor{border: 1px rgb(202 202 202) solid;line-height: normal;}
</style>
    """
    return html