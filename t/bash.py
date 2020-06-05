''' A module for testing Bash script.
'''

from    subprocess  import run      # ≥3.5
from    subprocess  import CalledProcessError

def bash(script=None, *, failok=False, presource=None):
    ''' Run the given bash script with extensive error checking.

        This runs the given bash script with the following options set:
        - ``-e``: Exit on any untested error.
        - ``-u``: Exit on reference to any unset variable.
        - ``-o pipefail``: Any command in a pipeline that fails will
          cause the entire pipeline to fail. (Normally the exit code
          of only the last command is checked.)

        If `presource` is given, that file will be sourced before running
        the given `script`.

        A `subprocess.CalledProcessError` exception will be raised if
        the process exit code is anything other than 0 unless the
        `failok` flag is set to `True`.

        This returns a `subprocess.CompletedProcess` object. The most
        common attributes you will use are `returncode` (the exit code
        of the process), `stdout` and `stderr`.

    '''

    #   Issues:
    #   * Perhaps we should be combining output: stdout=PIPE, stderr=STDOUT
    #   * capture_output requires ≥3.7.
    #   * encoding requires ≥3.6
    bash = ['bash', '-eu', '-o', 'pipefail', ]
    if presource:
        script = 'source "{}" && '.format(str(presource)) + script
    r = run(bash,
        input=script, encoding='UTF-8',
        capture_output=True,
        timeout=10,
        )
    if presource:
        print('----- Presource: {}'.format(presource))
    print(r.stderr)     # Debugging info when test fails.
    print('----- Exited with code {}'.format(r.returncode))
    if not failok:
        r.check_returncode()
    return r

def joinlines(*lines):
    ''' Join a list of lines, terminating each with a newline.

        This is useful for more easily expressing the expected output
        of a Bash script:

        >>> joinlines('hello', 'there')
        'hello\nthere\n'
    '''
    return '\n'.join(lines) + '\n'
