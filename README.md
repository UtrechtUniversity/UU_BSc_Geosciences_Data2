# Data2 exercises (GEO2-1231)

Welcome to the repository for the development of course materials for the Bachelor's course *Data analyse en statistiek 2 (GEO2-1231)*. This repository is dedicated to creating and refining the computer exercises of the course that will help students gain essential skills in data cleaning, statistical methods, trend and pattern discovery using Python.

This repository contains all the resources, code, and documentation needed for these exercises. Our goal is to ensure that the course materials are comprehensive, engaging, and effective.

## Structure and development of the computer exercises

-   Optimal schedule/setup
    -   Tuesday
        -   Remindo 9:00-9:30 about topic of week prior + break
        -   2 hour lecture on that week's topic + breaks
        -   45 minute (guided introduction) to exercise of Thursday
    -   Thursday
        -   Full 4h exercise with implementation of topic and skills learned on Tuesday
        -   Largely independent work
        -   Students work in couples
        -   Hand in answers for exercise assignment on Blackboard. Not graded (random check for quality?).
-   Computer exercise manual will be a webpage hosted as Github pages, with a separate sub page for the assignment of every week. An example of how that could look like: <https://mountainhydrology.github.io/hccc/introduction.html>
-   Computer exercises for the course will be developed using Quarto, which is very similar to RMarkdown but better. It will allow us to run Python code and render it to HTML using the Jupyter/IPython kernel from a specific virtual/conda environment directly. This will keep the dependencies etc properly in check. Quarto markdown documents can, among other ways, be rendered from the command line directly, straight from RStudio (also providing a visual editor), or using the VS code plugin.
-   We develop everything in this Github repository to keep everything synced properly.
-   Every week of the course should get its own sub directory.
-   For an example of a possible structure and use of Quarto, see [Regression example](/40_Linear_regression/) made by Emilia.

## Developing computer exercises on Windows

To develop the computer exercises on Windows, it is easiest to use a combination of Conda environments and RStudio. To get everything ready for development from scratch:

1.  **Install Git** for Windows from:\
    <https://www.git-scm.com/download/win>
2.  **Enable OpenSSH** and set the service to auto start**\
    **See [this guide](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows).
3.  **Generate ssh key** in command line\
    See [this guide](https://www.howtogeek.com/762863/how-to-generate-ssh-keys-in-windows-10-and-windows-11#option-1-generate-keys-in-the-command-line).
4.  **Add public ssh key** to your Github account\
    Create new entry at <https://github.com/settings/keys>, copy over the contents of the following text file on your computer `%userprofile%\.ssh\id_rsa.pub`
5.  **Enable UU Single Sign On** for the added ssh key\
    For the new key entry on Github, enable access to the Utrecht University organisation by going to the "Configure SSO" dropdown at <https://github.com/settings/keys>
6.  **Install miniconda3** from:\
    <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>
7.  **Install both R and RStudio** from:\
    <https://posit.co/download/rstudio-desktop/>
8.  **Install Quarto** from: <https://quarto.org/docs/get-started/>
9.  Open command line or anaconda prompt and **create a new conda environment** that has all the necessary dependencies by running the following line in the anaconda prompt (open via start menu):\
    `conda create -n data2 -c conda-forge jupyter numpy pandas statsmodels matplotlib`
10. Open RStudio and **set the Python interpreter** to created data2 environment (*Tools / Global options / Python / Select / Conda environments*)
11. **Clone this repository**. Using SSH connection while cloning is required by UU. Develop your material locally using Git version control (save and commit changes frequently). For more information on using Git, refer to online sources (e.g. <https://rogerdudler.github.io/git-guide/>).
12. **Copy the `.qmd` template** regression exercise of Emilia to work with **or create your own** Quarto document in RStudio (*File / New File / Quarto Document*). In RStudio you can toggle between the source and a visual editor for Quarto markdown.
13. When finished **push your local changes** to the git repo back to the origin (i.e. the repository on Github).

## Running instructions without Spyder

To make sure the dependencies are in place, use a virtual environment. First install the dependencies (needed only once or after changing them):

```         
poetry install
```

Then enter the venv using:

```         
poetry shell
```

After this you can run the script, either directly in a Python REPL or in an IDE, e.g. by starting VS Code from inside the venv:

```         
code .
```

To publish the script, run:

```         
quarto render $FILENAME
```
