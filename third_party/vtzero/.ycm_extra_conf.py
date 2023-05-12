#-----------------------------------------------------------------------------
#
#  Configuration for YouCompleteMe Vim plugin
#
#  http://valloric.github.io/YouCompleteMe/
#
#-----------------------------------------------------------------------------

from os.path import realpath, dirname

basedir = dirname(realpath(__file__))

# some default flags
# for more information install clang-3.2-doc package and
# check UsersManual.html
flags = [
    '-Werror',
    '-Wall',
    '-Wextra',
    '-pedantic',
    '-Wno-return-type',
    '-Wno-unused-parameter',
    '-Wno-unused-variable',
    '-std=c++11',
    '-x',
    'c++',
    '-isystem',
    '/usr/lib/ycmd/clang_includes/',
    f'-I{basedir}/../protozero/include',
    f'-I{basedir}/include',
    f'-I{basedir}/test/include',
    f'-I{basedir}/test/catch',
]

# youcompleteme is calling this function to get flags
# You can also set database for flags. Check: JSONCompilationDatabase.html in
# clang-3.2-doc package
def FlagsForFile( filename ):
  return {
    'flags': flags,
    'do_cache': True
  }
