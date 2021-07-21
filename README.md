# typora-blogspot-converter

A Plug-in allow you to convert markdown code to html code for your google blogspot.

## Install

Download [typora](https://typora.io/) and [releases](https://github.com/Mane-Network-Team/typora-blogspot-converter/releases) on your file system.

Install `Python3` and `markdown` modules.

```bash
pip3 install markdown
pip3 install beautifulsoup4
pip3 install requests
```

## Add the Typora Export

1. Open `Typora`
2. Click `File` -> `Preferences` -> `Export`  -> `+`  to add one 
3. Type the name like `Mane Blogger`
4. Command line will be 

```bash
<your_patch>\mdToHtml.py -i "${currentPath}" -t default [-m "<module name>"]
```

Show Save File Dialog : "`Do not popup save file dialog`"

After Export : Disable the `show command output`

![Setting](https://raw.githubusercontent.com/Mane-Network-Team/typora-blogspot-converter/main/picture/setting.png)

## How to use ?

When you finished to config it, you just click `File` -> `Export` -> `Mane Blogger` . After that it will be generated `openfile.md.html` in the path where you open it.

Next, you just copy the html code to google blogspot.

## About the file system and command

`mdToHtml.py` 

- `-i` : (required) input file
- `-t` : (required) using the template in `template` directory .
- `-v` : (optional) show versions
- `-m` : (optional) using module

The `template` directory will be save the template files.

## Template (-t)

Version 1.0 only have default template.

- `default` 

## Module (-m) (optional)

- `img2base64`
  - All the image will be convert Base64 format, If your image file is very large, the output file size will also be very large.

## Depend on

+ [markdown](https://github.com/Python-Markdown/markdown)
+ [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
+ [code-prettify](https://github.com/googlearchive/code-prettify)
+ [MathJax](https://www.mathjax.org/)

## Developer

by Mane.

![visitors](https://visitor-badge.glitch.me/badge?page_id=https://github.com/Mane-Network-Team/typora-blogspot-converter)
