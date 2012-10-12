![](https://raw.github.com/crankyadmin/PigLint/master/piglint.png?login=crankyadmin&token=a33d4623f6ce1b98d5318f501c98a04c)
## An Apache Pig syntax checker

### Why?

During my day job (as a developer) I found myself writing loads of [Apache Pig](http://pig.apache.org/). Over time I became rather annoyed with the lack of development tools forgo PigLint and [pig-ctags](https://github.com/crankyadmin/pig-ctags) where born.
I'll be maintaining this code as an ongoing concern, I also fully welcome pull requests to make it even more awesome.

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

### Goodies

* [Syntastic](https://github.com/scrooloose/syntastic) support 
* It can tidy your pig script, use `--tidy`

### Whoa dude you have a bug

Open a issue and I'll do my best to fix it.
