from __future__ import absolute_import
from os import getenv
from os.path import join, exists
from sh import mkdir, cp
from pythonforandroid.recipe import PythonRecipe, current_directory


class LocalIPV8Recipe(PythonRecipe):
    """
    Python-for-Android IPV8 recipe
    """

    url = 'git+https://github.com/Tribler/py-ipv8.git'

    depends = ['cryptography', 'libsodium', 'netifaces', 'pyasn1',
               'python3', 'setuptools', 'twisted', 'lib2to3', 'libnacl', 'sqlite3', 'decorator', 'libnacl', 'six'
              ]

    patches = ["no_bootstrap.patch", "port_change.patch"]

    python_depends = ['hyperlink']

    site_packages_name = 'ipv8'

    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(LocalIPV8Recipe, self).postbuild_arch(arch)

        # Install twistd plugins
        cp('-rf', join(self.get_build_dir(arch.arch), 'twisted', 'plugins'), join(self.ctx.get_python_install_dir(), 'twisted'))
        
        # Copy ipv8_service.py
        cp('-rf', join(self.get_build_dir(arch.arch), 'ipv8_service.py'), self.ctx.get_python_install_dir())

recipe = LocalIPV8Recipe()
