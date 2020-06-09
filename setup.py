from distutils.core import setup


from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'isOdd',        
  packages = ['isOdd'],  
  version = '0.1.1',     
  license='MIT',        
  description = 'Simple library to check if a number is odd',  
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Juan Benitez',                  
  author_email = 'juanbenitezdev@gmail.com',     
  url = 'https://github.com/juanbenitezdev/isOdd',   
  download_url = 'https://github.com/JuanBenitezDev/isOdd/archive/v0.1.1.tar.gz',    
  keywords = ['Odd', 'Integer', 'Math'],  
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
  ],
)