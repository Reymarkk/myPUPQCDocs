# University Online Document Request
It offers various submodules and functionalities that enable students, alumni, and other stakeholders to conveniently request documents such as transcripts, certificates, and letters online.

## Setup & Installation
(Example only, still not the proper way to setup & install)

Make sure you have the latest version of Python installed.

Setup & Installation

Clone the projectsssssssssssss
```bash
git clone <repo-url>
```

Install Django
```bash
pip install django
```

if doesn't work try:
```bash
pip3 install django
```
or
```bash
python -m pip install django
```
or 
```bash
python3 -m pip install django
```

Install bootstrap
```bash
pip install crispy-bootstrap5
```
and
```bash
pip install crispy-forms
```

Ctrl+c to quit the server
 

Example only:
Clone the project
```bash
git clone <repo-url>
```

Install python flask

```bash
pip install flask
```
Install postgres sql

```bash
pip install psycopg2
pip install psycopg2-binary
```

Run. (not literally)

```bash
python main.py
```
 
## Folder Structure
📦

├── 📂 assets                                       > Contain template static & generated assets

│   ├── 📂 audio

│   ├── 📂 css                                      > Demo & Example related styles only

│   ├── 📂 img                                      > Images (jpeg/png)

│   ├── 📂 js                                       > JS files i.e demos, pages & apps

│   │   ├── 📄 main.js                                > Template Main JS file (Init)

│   │   ├── 📄 config.js                              > Template config file for easy customization

│   │   ├── 📄 front-main.js                          > Front pages Main JS file (Init)

│   │   ├── 📄 front-config.js                        > Front pages config file for easy customization

│   │   └── 📄 ...

│   ├── 📂 json                                     > Search, Apps, Table & Translation fake data

│   ├── 📂 svg                                      > SVGs

│   └── 📂 vendor                                   > Generated assets i.e css, js, fonts & libs

├── 📂 build                                      > Generated build for Production 🚀

├── 📂 dist                                       > Generated dist 📦

├── 📂 fonts                                      > Template Font-icons

├── 📂 html                                       > Template HTML

│   ├── 📂 vertical-menu-template                   > With Customizer

│   ├── 📂 vertical-menu-template-no-customizer     > Without Customizer

│   ├── 📂 front-pages                              > Front pages for ex: landing payment, checkout, pricing etc...

│   └── ...

├── 📂 html-starter                               > Starter HTML files with least required libs

├── 📂 js                                         > Core JS(ES6) files

│   ├── 📄 menu.js                                  > Core Menu

│   ├── 📄 template-customizer.js                   > Customizer Plugin

│   └── 📄 ...

├── 📂 libs                                       > Third-party libs i.e datatable, full-calender etc...

├── 📂 scss                                       > Core SCSS

│   ├── 📂 _bootstrap-extended                      > Extended styles of bootstrap components

│   ├── 📂 _components                              > Contain custom components style

│   ├── 📂 _custom-variables                        > Custom variables files (bootstrap, custom compo., pages & libs) for customer to override

│   ├── 📂 _theme                                   > Custom themes mixin for bootstrap, libs & pages

│   ├── 📂 pages                                    > Pages, Apps & Front Pages styles

│   ├── 📂 rtl/                                     > RTL supported styles

│   ├── 📄 core.scss                                > Core (light) style file which includes bootstrap, bootstrap-extended, components & colors

│   ├── 📄 core-dark.scss                           > Core dark style file

│   ├── 📄 theme-default.scss                       > Default (light) theme style file

│   ├── 📄 theme-default-dark.scss                  > Default dark theme style file

│   └── 📄 ...

├── 📂 tasks                                      > Gulp tasks

├── 📄 .eslintignore                              > eslint ignore file

├── 📄 .eslintrc.json                             > eslint rc file

├── 📄 .npmrc                                     > To resolve peer dependency while using npm

├── 📄 .prettierignore                            > prettier ignore file

├── 📄 .prettierrc.json                           > prettier rc file

├── 📄 build-config.js                            > Template build config file

├── 📄 gulpfile.js                                > Gulpfile

├── 📄 index.html                                 > Index page to check all demos

├── 📄 package.json

└── 📄 webpack.config.js                          > Webpack file to transpile & bundle JS files.

<br />
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original-wordmark.svg" alt="python" width="40" height="40"/></a>
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-plain.svg" alt="css3" width="40" height="40"/></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg" alt="javascript" width="40" height="40"/> </a>
<a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://sass-lang.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg" alt="sass" width="40" height="40"/></a>
<a href="https://codeigniter.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-plain.svg" alt="html5" width="40" height="40"/> </a>
<a href="https://codeigniter.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a>
<a href="https://codeigniter.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/postgresql/postgresql-original-wordmark.svg" alt="Postgresql" width="40" height="40"/> </a>
