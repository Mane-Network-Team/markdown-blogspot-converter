# typora-blogspot-converter

A Plug-in allow you to convert markdown code to html code for your google blogspot.

## Install

Download [typora](https://typora.io/) and [releases](https://github.com/Mane-Network-Team/typora-blogspot-converter/releases) on your file system.

```bash
git clone https://github.com/Mane-Network-Team/typora-blogspot-converter.git .
```

Install `Python3` and `markdown` modules.

```bash
pip3 install markdown
pip3 install beautifulsoup4
pip3 install requests
```

## Add the Typora Export

1. Open `Typora`
2. Click `File` -> `Preferences` -> `Export`  -> `+`  to add one 
3. Type the name like `To Google Blogger`
4. Command line will be 

```bash
<your_patch>\mdToHtml.py -i "${currentPath}" -t default [-m "<module name>"]
```

**Example like this one:** 

```bash
<your_patch>\mdToHtml.py -i "${currentPath}" -t default -m img2base64,mathjax,codeace
```

Show Save File Dialog : "`Do not popup save file dialog`"

After Export : Disable the `show command output`

![Setting](https://raw.githubusercontent.com/Mane-Network-Team/typora-blogspot-converter/main/picture/setting.png)

## How to use ?

When you finished to config it, you just click `File` -> `Export` -> `Mane Blogger` . After that it will be generated `*.md.html` in the path where you open it.

Next, you **just copy the html code to google blogspot**.

## About the file system and command

`mdToHtml.py` 

- `-i` : (required) input file
- `-t` : (required) using the template in `template` directory .
- `-v` : (optional) show versions
- `-m` : (optional) using module
  - Multiple use `,` to split it, like `-m img2base64,code4ace`

The `template` directory will be save the template files.

## Template (-t)

Version 1.0 only have default template.

- `default` 

If you like to change the theme, just copy it.

## Module (-m) (optional)

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

