from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as _build_ext
import os
import glob
import shutil

hvc_module = Extension('hypervolume',
                        sources = ['hvc.c', 'hv.c', 'timer.c', 'avl.c'],
                        extra_compile_args=['-std=c99'])

class build_ext(_build_ext):
    def run(self):
        _build_ext.run(self)
        builded_lib = glob.glob("build/lib*/h*")
        if len(builded_lib) == 0:
            raise Exception('Build failed')

        lib = builded_lib[0]
        print(lib)
        os.rename(builded_lib[0] , 'libhvci.so')
        try:
            shutil.rmtree('build')
            shutil.rmtree('dist')
        except Exception:
            pass


setup(name = 'hypervolume',
        version = '1.0',
        cmdclass={'build_ext': build_ext},
        description = 'Computation of the Hypervolume by Carlos M. Fonseca, Manuel Lopez-Ibanez and Luis Paquete.',
        author = 'Benjamin Manns',
        author_email = 'beesforever@gmx.de',
        ext_modules = [hvc_module])