# PigLint 
## (An Apache Pig syntax checker)

### Why?

During my day job (as a dev) I found myself writing loads of Pig. Over time I became rather annoyed with the lack of development tools forgo PigLint and pig-ctags where born.

### Installation
#### The easy way

    pip install piglint

#### The easyish way

    git clone git@github.com:crankyadmin/PigLint.git
    cd PigLint
    chmod +x piglint.py
    sudo cp piglint.py /usr/local/bin/piglint

### Usage

    piglint --file your_pig_script.py

### Whoa dude you have a bug

Open a issue and I'll do my best to fix it.
