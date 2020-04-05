import os
import json
from shutil import which
from time import sleep as slp

mark = """
  _____     _______
 / ___/_ __/ ___/ /__  ___  ___
/ /__/ // / /__/ / _ \/ _ \/ -_)
\___/\_, /\___/_/\___/_//_/\__/
    /___/ V E R S I O N - 1 . 0

 This repository uses the CyClone to update its components.
 You can also make one for your own using CyClone.
 For more information, check the link below..
 https://github.com/lnxpy/cyclone
"""

is_permitted = True if os.getenv("SUDO_USER") else False

steps = ['add -A ',
         'commit -m \'CyClone-Updater Commited\'']

def main():
    print(mark)

    if not is_permitted:
        printer('Permission denied', 'ERROR')
        return

    if os.path.isfile('conf.json'):
        printer('Configs found')
    else:
        printer('Configuration could not be found', 'ERROR')
        return

    try:
        with open('conf.json') as json_file:
            configs = json.load(json_file)
    except Exception as e:
        printer('Configuration file has been currepted', 'ERROR')

    repo, source = configs['repository'], configs['source']

    if which('git'):
        update(repo, source)
    else:
        printer('be sure that the git software has been already installed', 'ERROR')
        return

def update(repo, source):
    printer('running the Git\n')
    #slp(2)

    for step in steps:
        os.system('git %s'%step)

    printer('Git is pulling from the cloud\n')
    slp(2)

    try:
        os.system('git pull')
    except Exception as e:
        printer('an error occurred for pulling %s'%s, 'ERROR')
        return

    printer('%s updated successfully'%repo.split('/')[1])

def printer(text, stat='CHECK'):
    print(' [%s] %s'%(stat, text))

if __name__ == '__main__':
    main()
