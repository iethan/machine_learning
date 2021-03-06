from distutils.core import setup

setup(name='MachineLearning',
      version='0.0.1',
      description='Utils for machine learning',
      author='Ethan Lyon',
      author_email='ethanyon@gmail.com',
      url='https://github.com/iethan/MachineLearning/',
      packages=['MachineLearning',
      			'MachineLearning.get_data',
      			"MachineLearning.pre_processing",
      			"MachineLearning.train_test_optimize"],
     )
