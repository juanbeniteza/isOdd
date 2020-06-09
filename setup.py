from setuptools import setup



setup(
  name = 'isOdd',        
  packages = ['isOdd'],  
  version = '0.1.2',     
  description = 'Simple library to check if a number is odd',  
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = "Juan Benitez",
  license="MIT",        
  author_email = 'juanbenitezdev@gmail.com',     
  url = 'https://github.com/juanbenitezdev/isOdd',   
  download_url = 'https://github.com/JuanBenitezDev/isOdd/archive/v0.1.2.tar.gz',    
  keywords = ['Odd', 'Integer', 'Math'],  
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
  ],
)