import subprocess
import os
import re
import shutil

STATSMODELSDIR = "C:\Users\skipper\statsmodels\statsmodels-skipper"

def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(" ".join(cmd), stdout = subprocess.PIPE, env=env,
                               shell=True).communicate()[0]
        return out
    os.chdir(STATSMODELSDIR)
    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        raise

    return GIT_REVISION

def rename_files():
    binaries = os.listdir(os.path.join(STATSMODELSDIR, "dist"))
    git_rev = git_version()[:7]
    for name in binaries:
        newname = re.sub("(?<=statsmodels-\d\.\d\.\d)", "-"+git_rev, name)
        shutil.move(os.path.join(STATSMODELSDIR, "dist", name),
                    os.path.join(STATSMODELSDIR, "dist", newname))

if __name__ == "__main__":
    rename_files()
