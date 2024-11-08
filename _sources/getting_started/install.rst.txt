============
Installation
============


Installation Guide

Step 1: Ensure you have Python 3.8+ installed. 

.. code-block::

  python --version

Step 2: Install the library with `pip` using the following command:

.. code-block::

  # Basic installation of the library, enough for SDK usage
  pip install holistic
  
  # bias mitigation support
  pip install holistic[bias] 

  # additional packages for explainability metrics and plots
  pip install holistic[explainability]

  # install all packages for security strategies
  pip install holistic[security]


Step 3: Verify installation by importing the package in a Python shell

.. code-block::

  import holistic

  holistic.__version__