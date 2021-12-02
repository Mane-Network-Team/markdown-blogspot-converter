# markdown-blogspot-converter

A Plug-in allow you to convert markdown code to html code for your google blogspot.

## Install

Download [releases](https://github.com/Mane-Network-Team/typora-blogspot-converter/releases) on your file system.

```bash
git clone https://github.com/Mane-Network-Team/markdown-blogspot-converter.git .
```

Install `Python3` and those modules.

```bash
pip3 install markdown
pip3 install beautifulsoup4
pip3 install requests
pip3 install pymdown-extensions
```

## How to use ?

Drop the markdown file to `dropTohere.py` or using the terminal with `mdToHtml.py`, it will generate html code in markdown file directory.

## About the file system and command

`mdToHtml.py` 

- `-i` : (required) input file
- `-t` : (required) using the template in `template` directory .
- `-v` : (optional) show versions
- `-m` : (optional) using module

Multiple use `,` to split it, like `-m img2base64,code4ace`

The `template` directory will be save the template files.

## Example command line

```bash
<your_patch>\mdToHtml.py -i "${currentPath}" -t default [-m "<module name>"]
```

**Example like this one:**

```bash
<your_patch>\mdToHtml.py -i "${currentPath}" -t default -m img2base64,mathjax,codeace
```

### Option template (-t)

Version 1.0 only have default template.

- `default` 

If you like to change the theme, just copy it.

### Option module (-m) (optional)

- `img2base64`
  - All the image will be convert Base64 format, If your image file is very large, the output file size will also be very large.
- `codeace`
  - Code highlight by [ACE Editor](https://ace.c9.io/).
- `codeprettify`
  - Code highlight by [Google Code Prettify](https://github.com/googlearchive/code-prettify).
- `mathjax`
  - Parse math formula (Like LaTeX) to image via [MathJax](https://www.mathjax.org/).

## Depend on

+ [markdown](https://github.com/Python-Markdown/markdown)
+ [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
+ [ACE Editor](https://ace.c9.io/)
+ [MathJax](https://www.mathjax.org/)
+ [Google Code Prettify](https://github.com/googlearchive/code-prettify)

## Developer

by Mane.
