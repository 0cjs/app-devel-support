from    bash import bash, CalledProcessError, joinlines
from    os.path  import dirname, join as joinpath
import  pytest

MYDIR = dirname(__file__)

def test_ok():
    r = bash('echo hello')
    assert 0 == r.returncode
    assert 'hello\n' == r.stdout

def test_fail():
    with pytest.raises(CalledProcessError) as ex:
        bash('f() { return 33; }; f')
    assert ex.match('exit status 33')

def test_failok():
    r = bash(failok=True, script='echo goodbye; false')
    assert 1 == r.returncode
    assert 'goodbye\n' == r.stdout

def test_set():
    r = bash(failok=True, script='echo start; false; echo nope')
    assert 1 == r.returncode
    assert 'start\n' == r.stdout
    assert '' == r.stderr

def test_set_u():
    r = bash(failok=True, script='echo $this_is_not_set; echo nope')
    assert 1 == r.returncode
    assert '' == r.stdout
    assert 'unbound variable' in r.stderr

def test_set_pipefail():
    r = bash(failok=True, script='false | cat')
    assert 1 == r.returncode
    assert '' == r.stdout
    assert '' == r.stderr

def test_presource():
    prescript = joinpath(MYDIR, 'bash_test.bash')
    print('prescript: ', prescript)     # debug on test failure
    script = '''
        echo a_var="'""$a_var""'"
        a_func 'an arg'
    '''
    r = bash(presource=prescript, script=script)
    expected = joinlines(
        "a_var='a value'",
        'a_func: arg=an arg',
    )
    assert expected == r.stdout
