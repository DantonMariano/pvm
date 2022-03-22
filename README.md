# PVM
## _PHP Version Manager!_
- As simple as it gets
- Never use update-alternatives again! (at least with php)
    
## Features

- Install and manage different PHP versions
- Shorthand command for Changing Versions -cv

I was running into the issue of doing the same old boring repetitive task of googling "how to change php versions on linux/ubuntu/debian etc... the list goes on." So I Had the idea of simply creating a tool that automates this! for now it only works with Debian/Ubuntu derivative distros. But I'm pretty sure that's the most of you out there anyways (hats off to Fedora/CentOS users btw)

> Couldn't there be just a simple package for PHP version management that worked a bit like nvm (node version manager)?

## Installation

PVM requires Python to run, but it will be installed
as soon as you make the install.sh script executable,
the alias will also be created!

Also, be sure to clone the repo on your ~/ (user) folder!

```sh
cd ~/pvm
chmod a+x install.sh
./install.sh
```

And there you go! now you have PVM Installed!

You can simply use it via the shorthand which is

```sh
pvm -cv (desired version) [ex: 7.4, 8.1, 5.6]
```

or use the User Interface! by executing:
```sh
pvm
```

Thanks a ton for your attention! I hope this helps you save time and effort! :)
