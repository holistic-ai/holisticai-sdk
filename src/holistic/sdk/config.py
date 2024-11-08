class Config:
    """
    Create a config using this class
    Attributes
    ----------
    config : dict -> {
        clientId: '',
        api_key: '',
        projectId: '',
        solutionId: ''
    }
    """

    mandatory_config_fields = ["clientId", "key", "api", "projectId", "solutionId", "moduleId"]  # noqa: RUF012

    def validate_config(self):
        for mandatory_config in self.mandatory_config_fields:
            if mandatory_config not in self.config:
                msg = f"{mandatory_config} field is missing from the config"
                raise Exception(msg)  # noqa: TRY002

    def __init__(self, config):
        self.config = config
        self.validate_config()
        self.session = {"config": self.config}
