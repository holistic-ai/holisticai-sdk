==================================
Setting Up a GitHub CI/CD Pipeline
==================================

This document provides guidance on how to use the Holistic AI Governance Platform’s SDK functionality to perform a Continuous Integration / Continuous Delivery (CI/CD) pipeline over your model development using GitHub. 

.. note::
  This guidance relies on your model development being undertaken within a repository managed using Github.

Some sections of this guidance replicate those of the Setting Up a Quantitative Assessment guidance.  


Creating the Github Workflow
----------------------------

To use the CI/CD Pipeline functionality in GitHub, a workflow needs to be created for your repository:

1. Navigate to your repository in Github.
2. Open the 'Actions' tab in the repository's top navigation bar. |action|
3. Click the 'New workflow' button in the top left corner of the Actions tab |newworkflow|. 
4. You will be presented with a page which provides a selection of potential workflows that you might use. For this guidance, however, simply click through on the hyperlink towards the top of the 'Choose a workflow' page labeled 'set up a workflow yourself'.
5. This will give you a page where you can enter your test script using the markup language YAML:

.. |action| image:: ../../_static/sdk/action.avif
   :width: 80px 

.. |newworkflow| image:: ../../_static/sdk/newworkflow.avif
   :width: 80px 

.. image:: ../../_static/sdk/console.png
   :align: center
   :width: 400px


The following workflow script can be used to test Python development (specifically Python 3.9 in the below):

.. code-block:: yaml

  name: Test pipeline
  on: pull_request

  jobs:
    integration-test-pipeline:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
          with:
            fetch-depth: 0
        - uses: actions/setup-python@v4
          with:
            python-version: 3.9

        - name: Install Poetry
          run: |
            python -m pip install --upgrade pip
            python -m pip install poetry
        - name: Install dependencies
          env:
            pypi_token: ${{ secrets.PYPI_TEST_TOKEN }}
            pypi_user: ${{ secrets.PYPI_TEST_USER }}
          run: |
            pip install -r requirements.txt
            pip install -i https://test.pypi.org/simple/ haisdk
        - name: Run tests
          run: |
            pytest -s

The YAML script then needs to be deployed via a change commit.

Navigating the Governance Platform
----------------------------------

Before using the library, you must be onboarded and given access to the platform. To get started:

1. Sign in to your instance of the Governance Platform.
2. Locate the Solution for which you would like to perform the CI/CD pipeline.
3. Find the Quantitative Assessment node in the Solution's Panel view.

In this guide, we will use the Efficacy Quantitative Assessment as an example. 

.. image:: ../../_static/sdk/qassess.png
   :align: center
   :width: 400px

In the Quantitative Assessment, click the 'SDK Access' button available at the top of the Quantitative Efficacy assessment page and copy the SDK Access Config information to the clipboard. 


.. image:: ../../_static/sdk/sdkbutton.png
   :align: center
   :width: 300px

.. raw:: html
   <br><br>

.. image:: ../../_static/sdk/sdkconfig.png
   :align: center
   :width: 600px

Initialising a Quantitative Assessment
--------------------------------------

In your Python code, import the Holistic AI SDK library together with Pandas as a necessary prerequisite: 

.. code-block::

  from holistic import Assess, Config
  import pandas as pd


The data from the SDK Access Config, as copied to your clipboard above, should then be assigned to a variable named ‘config’ and then an instance of the Config class should be created and assigned to a variable named ‘session’ – for example:

.. code-block::

  config = {
    "projectId": "cc5a543d-418b-4da4-b21f-24b201456b16",
    "solutionId": "9a9c0092-7e70-4d7b-9d67-e3064a745041",
    "moduleId": "EfficacyAssessment",
    "clientId": "none",
    "key": "oooWEAuZYV5NPEHYhje2YVrZYFQznmgC",
    "api": "api-sdk-demo.holisticai.io"
  }

  session = Config(config=config)


The settings for the assessment then need to be defined, and assigned to the ‘settings’ variable – for example:


.. code-block::

  settings = {
      'config': config,
      'task': 'binary_classification',
      'data_type': 'train-test',
      'target_columns': ['default'],
      'prediction_columns': [],
      'model_class': 'sklearn'
  }

- ```config``` – this instance of the Config class created earlier should be assigned to this key
- ```task```– this the task being fulfilled by the model. The SDK accepts the tasks
- ```binary_classification```, ```multi_classification```, and ```simple_regression```
- ```data_type``` – only ‘train-test’ is available
- ```target_columns``` – the is the Pandas DataFrame name for the data column that contains the ground-truth labels for the dataset
- ```model_class``` – available model classes are ‘sklearn’, ‘lightgbm’, ‘catboost’, ‘xgboost’, ‘tensorflow’, and ‘pytorch’

An instance of the Assess class can then be created thus and assigned to a variable called ‘assess’:


.. code-block::

  assess = Assess(session=session, settings=settings)


Results over your model can then be generated using the ```run``` method over the Assess instance, passing to the method the training data (as a Pandas DataFrame), the test data (also as a Pandas DataFrame), and either model predictions (if there are none, set ```y_pred=None```) or the model itself that you want to test (if there is not model, set ```model=None```):

.. code-block::

  res = assess.run(X=df_train, y=df_test, y_pred=None, model=model)

Specific tests can then be built which can flag whether the an iteration of your model passes or fails the workflow. For example, the metrics can be extracted from the generated results via


.. code-block::
  
  metrics = res.json()['results']

and then, using Python's ```assert``` method, a specific test can be built around the Precision metric:

.. code-block::
  for metric in metrics:
        if metric['metric'] == 'Precision':
           assert metric['pass'] is True

Running the Pipeline
--------------------

Whenever your model is updated, and the code is pushed to Github, the workflow will automatically run. This will perform the specific tests that have been put in place for the workflow, and generate Github alerts as to whether the current version of the model is passing the tests that have been put in place.
