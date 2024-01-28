from setuptools import setup, find_packages

setup(
  name = 'AMIE-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'AMIE',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/AMIE-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'differential diagnosis'
  ],
  install_requires=[
    'accelerate',
    'beartype',
    'einops>=0.7.0',
    'einx>=0.1.2',
    'torch>=2.0',
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
