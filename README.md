# plcheatsheet - About this Project
**plcheatsheet** is a **command line tool** which is written in Python. With this tool you can **quickly** look up
several programming or scripting languages, more precisely you can search for the main syntax of a language or the usages of this language. 

## How to use plcheatsheet
To show the main help message for plcheatsheet, type:
```bash
plcs
# or
plcs --help
```
The newest version only include one subcommand lang with the two options -f and -s. The options don't require an argument but the subcommand lang requires this. To see all options and the helping message of the subcommand lang, please type:
```bash
plcs lang --help
```

### Example usage of plcheatsheet
When you want to look at the short summary of JavaScript, you can type:
```bash
plcs lang js -s
```
> [!IMPORTANT]
> To use plcheatsheet you have to type 'plcs' as you can see above, when you type 'plcheatsheet' to use it, it will not work!

## Programming Languages which will be included
For this information there is also the file [included_pl.md](docs/included_pl.md), which contains
more about the programing languages and also my ideas for features
in the future. 

## Installation
Firstly, please make sure that you have installed **python 3.12** or **higher**, **git** and **pipx** or **uv**.
To install this tool global, you can use **pipx**. To install plcheatsheet run the following code
```bash
pipx install git+https://github.com/xxsamiyaxx/plcheatsheet.git
```

**Alternatively**, you can installed it with **uv**, running:
```bash
uv tool install git+https://github.com/xxsamiyaxx/plcheatsheet.git
```
Now plcheatsheet should be **installed** and is **ready to use**.

> [!NOTE]
> Make sure that you use a terminal font which include a **normal**, **italic** and **bold** style, otherwise the italic style or bold style of words in the short summaries will not be showed. 
>Additionally, use a terminal font combined with **Symbols Nerd Font** or use a **Nerd Font** like JetBrainsMono Nerd Font to display the symbols correctly

## Notices
One kind of a problem is that when you use the fullscreen cheatsheets then your terminal has to be in fullscreen mode and you should have a terminal font size of **14.5 pt** or **lower** because if your font size is bigger than 14.5 pt then it is possible that not all of this cheatsheet will be correctly displayed.

## Contributing
Whenever you have an new idea for this project and maybe want to contribute, you can write this in the discussion or
if you find bugs or something else, you also can report this in the issues!

## License
Copyright (C) 2026 xxsamiyaxx

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Used sources
For the information of the short summaries I used sources to research and for fact-checking. You can find all sources in the file [SOURCES.md](docs/SOURCES.md).
The short summaries are written in my own words and also independently
