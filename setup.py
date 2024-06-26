import setuptools
from numpy.distutils.core import Extension

ext_cpwt = Extension(name='zxcpd.cpwt',
                     sources=['plateflex/src/cpwt/cpwt.f90', 'plateflex/src/cpwt/cpwt_sub.f90'])
ext_flex = Extension(name='zxcpd.flex',
                     sources=['plateflex/src/flex/flex.f90'])

setuptools.setup(
    name='zxcpd',
    version='0.1.0',  # Update version as needed
    description='Integrated package for Curie depth and lithospheric elastic thickness estimation',
    author='Meknit254',
    author_email='collinjuma2001@gmail.com',
    url='https://github.com/Meknit254/zxcpd',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'],
    install_requires=['numpy>=1.15', 'pymc3', 'matplotlib', 'seaborn'],
    python_requires='>=3.6',
    tests_require=['pytest'],
    ext_modules=[ext_cpwt, ext_flex],
    packages=['zxcpd'],
    package_data={
        'zxcpd': [
            'examples/data/*.txt',
            'examples/Notebooks/*.py',  # Adjust as necessary
            'plateflex/examples/data.zip',
            'plateflex/examples/Notebooks/*.ipynb']
    }
)
