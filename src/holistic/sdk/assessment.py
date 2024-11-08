import codecs
import os
import pickle

import pandas as pd
import requests


class Assess:
    """
    Assess class is used to create an assessment

    Attributes
    ----------
    session : dict
    settings : dict -> {
        task: 'binary-classification' | 'clustering-efficacy' | 'simple-regression'
        target_column: '',
        prediction_column: '',
        prediction_proba_column: ''
    }
    """

    mandatory_settings_fields = ["task", "target_column"]  # noqa: RUF012
    mandatory_settings_tasks = {  # noqa: RUF012
        # target column or target columns
        "binary-classification": ["prediction_column", "prediction_proba_column"],
        "simple-regression": ["prediction_column"],
    }

    def __init__(self, session, settings):
        self.settings = settings
        self.session = session

    @staticmethod
    def _with_source():
        return (
            f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
            if "GITHUB_ACTIONS" in os.environ and os.environ["GITHUB_ACTIONS"] == "true"
            else "python-sdk"
        )

    def run(self, X: pd.DataFrame, y, y_pred, model):  # noqa: N803
        either_model_or_predictions = (model is None) ^ (y_pred is None)
        if either_model_or_predictions is False:
            raise Exception("Either the model or y_pred should be present")  # noqa: TRY003, TRY002, EM101
        config = self.session.config
        url = f"https://{config['api']}/sdk-assessment"
        headers = {
            "x-api-key": config["key"],
        }

        data = {
            "projectId": config["projectId"],
            "solutionId": config["solutionId"],
            "moduleId": config["moduleId"],
            "problemType": self.settings["task"],
            "dataType": self.settings["data_type"],
            "predictionColumns": self.settings["prediction_columns"],
            "targetColumn": self.settings["target_column"],
            "modelClass": self.settings["model_class"],
            "train": X.to_dict(orient="list"),
            "test": y.to_dict(orient="list"),
            "model": codecs.encode(pickle.dumps(model), "base64").decode(),
            "platformEndpoint": config["api"],
            "key": config["key"],
            "source": self._with_source(),
        }

        return requests.post(url=url, json=data, headers=headers)  # noqa: S113
