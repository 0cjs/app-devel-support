import bash

#   We must source xdg.bash with the full path to the one we're testing
#   because if we let Bash do a $PATH search it may pick up a different
#   version.
#
#   XXX These tests assume that CWD contains xdg.bash. Pass in $basedir
#   instead.
#
XDG_BASH_DIR = './'
