"""
Type annotations for fis service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_fis import FISClient

    client: FISClient = boto3.client("fis")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CreateExperimentTemplateActionInputTypeDef,
    CreateExperimentTemplateResponseTypeDef,
    CreateExperimentTemplateStopConditionInputTypeDef,
    CreateExperimentTemplateTargetInputTypeDef,
    DeleteExperimentTemplateResponseTypeDef,
    GetActionResponseTypeDef,
    GetExperimentResponseTypeDef,
    GetExperimentTemplateResponseTypeDef,
    ListActionsResponseTypeDef,
    ListExperimentsResponseTypeDef,
    ListExperimentTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartExperimentResponseTypeDef,
    StopExperimentResponseTypeDef,
    UpdateExperimentTemplateActionInputItemTypeDef,
    UpdateExperimentTemplateResponseTypeDef,
    UpdateExperimentTemplateStopConditionInputTypeDef,
    UpdateExperimentTemplateTargetInputTypeDef,
)

__all__ = ("FISClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FISClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        FISClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#can_paginate)
        """
    def create_experiment_template(
        self,
        *,
        clientToken: str,
        description: str,
        stopConditions: List["CreateExperimentTemplateStopConditionInputTypeDef"],
        actions: Dict[str, "CreateExperimentTemplateActionInputTypeDef"],
        roleArn: str,
        targets: Dict[str, "CreateExperimentTemplateTargetInputTypeDef"] = None,
        tags: Dict[str, str] = None
    ) -> CreateExperimentTemplateResponseTypeDef:
        """
        Creates an experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.create_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#create_experiment_template)
        """
    def delete_experiment_template(self, *, id: str) -> DeleteExperimentTemplateResponseTypeDef:
        """
        Deletes the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.delete_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#delete_experiment_template)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#generate_presigned_url)
        """
    def get_action(self, *, id: str) -> GetActionResponseTypeDef:
        """
        Gets information about the specified AWS FIS action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.get_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_action)
        """
    def get_experiment(self, *, id: str) -> GetExperimentResponseTypeDef:
        """
        Gets information about the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.get_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_experiment)
        """
    def get_experiment_template(self, *, id: str) -> GetExperimentTemplateResponseTypeDef:
        """
        Gets information about the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.get_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_experiment_template)
        """
    def list_actions(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListActionsResponseTypeDef:
        """
        Lists the available AWS FIS actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.list_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_actions)
        """
    def list_experiment_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListExperimentTemplatesResponseTypeDef:
        """
        Lists your experiment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.list_experiment_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_experiment_templates)
        """
    def list_experiments(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists your experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.list_experiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_experiments)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_tags_for_resource)
        """
    def start_experiment(
        self, *, clientToken: str, experimentTemplateId: str, tags: Dict[str, str] = None
    ) -> StartExperimentResponseTypeDef:
        """
        Starts running an experiment from the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.start_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#start_experiment)
        """
    def stop_experiment(self, *, id: str) -> StopExperimentResponseTypeDef:
        """
        Stops the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.stop_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#stop_experiment)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str] = None) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#untag_resource)
        """
    def update_experiment_template(
        self,
        *,
        id: str,
        description: str = None,
        stopConditions: List["UpdateExperimentTemplateStopConditionInputTypeDef"] = None,
        targets: Dict[str, "UpdateExperimentTemplateTargetInputTypeDef"] = None,
        actions: Dict[str, "UpdateExperimentTemplateActionInputItemTypeDef"] = None,
        roleArn: str = None
    ) -> UpdateExperimentTemplateResponseTypeDef:
        """
        Updates the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/fis.html#FIS.Client.update_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#update_experiment_template)
        """
