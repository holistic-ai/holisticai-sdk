====================================
Setting Up a Quantitative Assessment
====================================

This document provides guidance on how to use the Holistic AI Governance Platform’s SDK functionality to perform a quantitative assessment within a user’s development environment using Python. 

Navigating the Governance Platform
----------------------------------

Before using the library, you must be onboarded and given access to the platform. To get started:

1. Sign in to your instance of the Governance Platform.

2. Locate the Solution for which you would like to perform the Quantitative Assessment.

3. Find the Quantitative Assessment node in the Solution's Panel view.

In this guide, we will use the Efficacy Quantitative Assessment as an example. 

.. image:: ../../_static/sdk/qassess.png
   :align: center
   :width: 400px

In the Quantitative Assessment, click the 'SDK Access' button available at the top of the Quantitative Efficacy assessment page and copy the SDK Access Config information to the clipboard. 


.. image:: ../../_static/sdk/sdkbutton.png
   :align: center
   :width: 400px

.. image:: ../../_static/sdk/sdkconfig.png
   :align: center
   :width: 600px

Initialising a Quantitative Assessment
----------------------------------

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

- config – this instance of the Config class created earlier should be assigned to this key
- task– this the task being fulfilled by the model. The SDK accepts the tasks
- binary_classification, multi_classification, and simple_regression
- data_type – only ‘train-test’ is available
- target_columns – the is the Pandas DataFrame name for the data column that contains the ground-truth labels for the dataset
- model_class – available model classes are ‘sklearn’, ‘lightgbm’, ‘catboost’, ‘xgboost’, ‘tensorflow’, and ‘pytorch’

An instance of the Assess class can then be created thus and assigned to a variable called ‘assess’:

.. code-block::
  assess = Assess(session=session, settings=settings)


Running a Quantitative Assessment
---------------------------------

The assessment is run via the run method over the Assess instance, passing to the method the training data (as a Pandas DataFrame), the test data (also as a Pandas DataFrame), and either model predictions (if there are none, set y_pred=None) or the model itself that you want to test (if there is not model, set model=None):

.. code-block::
  res = assess.run(X=df_train, y=df_test, y_pred=None, model=model)

By assigning the result of the run method to a variable, the results of the assessment can be printed to the console.

The results can be viewed in the console (if sent to the console via print()or otherwise):

.. code-block::
  {
      "results": [
          {"baseline": 0.64835, "metric": "Accuracy", "model": 0.531325, "pass": False},
          {
              "baseline": 0.7431195127924269,
              "metric": "Precision",
              "model": 0.8514885837315943,
              "pass": True,
          },
          {"baseline": 0.45365, "metric": "Recall", "model": 0.0758, "pass": False},
          {"baseline": 0.758657, "metric": "AUC", "model": 0.5891555, "pass": False},
          {
              "baseline": 0.6633033574180155,
              "metric": "Log Loss",
              "model": 0.7470556015829998,
              "pass": False,
          },
      ]
  }

The results can also be viewed on the Solution’s Quantitative Efficacy Assessment page in the Governance Platform:

.. image:: ../../_static/sdk/panel.png
   :align: center
   :width: 600px