from setuptools import setup, find_packages

setup(
    name='akanda-rug',
    version='0.1.6',
    description='Akanda Router Update Generator manages tenant routers',
    author='DreamHost',
    author_email='dev-community@dreamhost.com',
    url='http://github.com/dreamhost/akanda-rug',
    license='BSD',
    install_requires=[
        'netaddr>=0.7.5',
        'httplib2>=0.7.2',
        'python-neutronclient>=2.1',
        'oslo.config',
        'kombu>=2.4.8',
        'webob',
        'python-novaclient',
        'cliff',
    ],
    namespace_packages=['akanda'],
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'akanda-rug-service=akanda.rug.main:main',
            'akanda-debug-router=akanda.rug.debug:debug_one_router',
            'rug-ctl=akanda.rug.cli.main:main',
        ],
        'akanda.rug.cli': [
            'router debug=akanda.rug.cli.router:RouterDebug',
            'router manage=akanda.rug.cli.router:RouterManage',
            'tenant debug=akanda.rug.cli.tenant:TenantDebug',
            'tenant manage=akanda.rug.cli.tenant:TenantManage',
            'workers debug=akanda.rug.cli.worker:WorkerDebug',
        ],
    },
)
