from distutils.core import setup

setup(
  name = 'isOdd',        
  packages = ['isOdd'],  
  version = '0.1',     
  license='MIT',        
  description = 'Simple library to check if a number is odd',  
  author = 'Juan Benitez',                  
  author_email = 'juanbenitezdev@gmail.com',     
  url = 'https://github.com/juanbenitezdev/isOdd',   
  download_url = 'https://github.com/JuanBenitezDev/isOdd/archive/v0.1.0.tar.gz',    
  keywords = ['Odd', 'Integer', 'Math'],  
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
  ],
)