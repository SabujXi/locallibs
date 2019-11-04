# Local/Under Development Library Management Tool for Python Developers
Often it happens that pip and requirements.txt is not enough for Python developers to automate importing and deployment tasks. The problem is more severe when you yourself is a library/framework developer. And here is a tool for you that will help you mitigate the pains.

## When you are a Python library/framework/module developer.
Being a Python library/framework developer myself - some of which are public and some of which are private - I never feel it good to deploy it to PyPi and reinstall that using pip for using in other projects I am working on that need that library. Also, I cannot just add that to external-library-list in my IDEs in every single project or in different IDEs I use.

So, I needed a system that would help me import (and/or deploy with respective project) all the local modules under development, in private projects or modules that I did not put on version control or on PyPi. I was planning a simple solution.

## When you just need to add modules from local file system
It is not the case that only those library/framework/module developers need such system. Many other type of Python developers also need this. For example, you colleague has sent you a module that you won't add into version control and that might be updated later - so you will copy-paste that module in a folder. Or, you are using an old library or a library that does not exist in PyPi or you are using your own module that you use personally. There are a lot of other possibilities.

## Design/Planning of the system.
1. A plain text file named `.locallibs` will be placed in the project root or under `src` directory.
2. `.locallibs` would contain absolute and relative paths to the module root dir. For example, let's say, you have a library called `awesome` and you put project codes under `src` directory. So, you have a directory called `awesome` under `src`. Now, you will add it like this on a line in `.locallibs` file: `/absolute-path-to-project-root/awesome-project/src`.
2. At the beginning of your project code execution you will import locallibs module and execute function `add_locallibs(BASE_DIR)` where `BASE_DIR` is the directory where `.locallibs` file lives. This base dir can be relative path, absolute path, a path inside the project or anywhere else.
4. In `.locallibs` file empty lines will be ignored, lines starting with `#` will be considered comments. Lines starting with `:an_identifier` and before any path is added will be considered as options. 
5. When you need to ship those modules/code with your project but do not want that to be checked into the version control you just run a command `locallibs collect` and it will copy everything from those base paths to `_locallibs` directory inside the directory where `.locallibs` lives.
6. When using `locallibs` you should add `.locallibs` and `_locallibs` to your version control ignore configs, e.g. `.gitignore`

## About the developer
Md. Sabuj Sarker
md.sabuj.sarker@gmail.com
+8801868363600
A Software Engineer, Project Manager, Trainer, Author.
