from setuptools import setup

setup( 
    name = 'gerenciadorcs',
    version = '4.0',
    author = 'Junio da Silva Damasceno',
    author_email = 'juniowin@yahoo.com.br',
    packages = ['gerenciadorcs'],
    package_data={
        'gerenciadorcs': [
            'interface-en-US.glade',
            'interface-pt-BR.glade',
            'interface-ES.glade'
        ]
    },
    include_package_data=True,
    description = 'um gerenciador de contas, usuários e senhas',
    url = 'https://github.com/JunioDamasceno/gerenciadorcs',
    license = 'MIT',
    keywords = ['gerenciador de senhas', 'Key manager', 'keymanager'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Licence :: OSI Aproved :: MIT Licence',
        'Natural Language :: Portuguese (Brazilian)',
       ]
)

