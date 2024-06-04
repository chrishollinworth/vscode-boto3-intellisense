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
    CreateExperimentTemplateExperimentOptionsInputTypeDef,
    CreateExperimentTemplateLogConfigurationInputTypeDef,
    CreateExperimentTemplateResponseTypeDef,
    CreateExperimentTemplateStopConditionInputTypeDef,
    CreateExperimentTemplateTargetInputTypeDef,
    CreateTargetAccountConfigurationResponseTypeDef,
    DeleteExperimentTemplateResponseTypeDef,
    DeleteTargetAccountConfigurationResponseTypeDef,
    GetActionResponseTypeDef,
    GetExperimentResponseTypeDef,
    GetExperimentTargetAccountConfigurationResponseTypeDef,
    GetExperimentTemplateResponseTypeDef,
    GetTargetAccountConfigurationResponseTypeDef,
    GetTargetResourceTypeResponseTypeDef,
    ListActionsResponseTypeDef,
    ListExperimentResolvedTargetsResponseTypeDef,
    ListExperimentsResponseTypeDef,
    ListExperimentTargetAccountConfigurationsResponseTypeDef,
    ListExperimentTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetAccountConfigurationsResponseTypeDef,
    ListTargetResourceTypesResponseTypeDef,
    StartExperimentExperimentOptionsInputTypeDef,
    StartExperimentResponseTypeDef,
    StopExperimentResponseTypeDef,
    UpdateExperimentTemplateActionInputItemTypeDef,
    UpdateExperimentTemplateExperimentOptionsInputTypeDef,
    UpdateExperimentTemplateLogConfigurationInputTypeDef,
    UpdateExperimentTemplateResponseTypeDef,
    UpdateExperimentTemplateStopConditionInputTypeDef,
    UpdateExperimentTemplateTargetInputTypeDef,
    UpdateTargetAccountConfigurationResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#close)
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
        tags: Dict[str, str] = None,
        logConfiguration: "CreateExperimentTemplateLogConfigurationInputTypeDef" = None,
        experimentOptions: "CreateExperimentTemplateExperimentOptionsInputTypeDef" = None
    ) -> CreateExperimentTemplateResponseTypeDef:
        """
        Creates an experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.create_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#create_experiment_template)
        """

    def create_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
        roleArn: str,
        clientToken: str = None,
        description: str = None
    ) -> CreateTargetAccountConfigurationResponseTypeDef:
        """
        Creates a target account configuration for the experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.create_target_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#create_target_account_configuration)
        """

    def delete_experiment_template(self, *, id: str) -> DeleteExperimentTemplateResponseTypeDef:
        """
        Deletes the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.delete_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#delete_experiment_template)
        """

    def delete_target_account_configuration(
        self, *, experimentTemplateId: str, accountId: str
    ) -> DeleteTargetAccountConfigurationResponseTypeDef:
        """
        Deletes the specified target account configuration of the experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.delete_target_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#delete_target_account_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#generate_presigned_url)
        """

    def get_action(self, *, id: str) -> GetActionResponseTypeDef:
        """
        Gets information about the specified FIS action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.get_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_action)
        """

    def get_experiment(self, *, id: str) -> GetExperimentResponseTypeDef:
        """
        Gets information about the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.get_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_experiment)
        """

    def get_experiment_target_account_configuration(
        self, *, experimentId: str, accountId: str
    ) -> GetExperimentTargetAccountConfigurationResponseTypeDef:
        """
        Gets information about the specified target account configuration of the
        experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.get_experiment_target_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_experiment_target_account_configuration)
        """

    def get_experiment_template(self, *, id: str) -> GetExperimentTemplateResponseTypeDef:
        """
        Gets information about the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.get_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_experiment_template)
        """

    def get_target_account_configuration(
        self, *, experimentTemplateId: str, accountId: str
    ) -> GetTargetAccountConfigurationResponseTypeDef:
        """
        Gets information about the specified target account configuration of the
        experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.get_target_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_target_account_configuration)
        """

    def get_target_resource_type(
        self, *, resourceType: str
    ) -> GetTargetResourceTypeResponseTypeDef:
        """
        Gets information about the specified resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.get_target_resource_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#get_target_resource_type)
        """

    def list_actions(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListActionsResponseTypeDef:
        """
        Lists the available FIS actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_actions)
        """

    def list_experiment_resolved_targets(
        self,
        *,
        experimentId: str,
        maxResults: int = None,
        nextToken: str = None,
        targetName: str = None
    ) -> ListExperimentResolvedTargetsResponseTypeDef:
        """
        Lists the resolved targets information of the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_experiment_resolved_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_experiment_resolved_targets)
        """

    def list_experiment_target_account_configurations(
        self, *, experimentId: str, nextToken: str = None
    ) -> ListExperimentTargetAccountConfigurationsResponseTypeDef:
        """
        Lists the target account configurations of the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_experiment_target_account_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_experiment_target_account_configurations)
        """

    def list_experiment_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListExperimentTemplatesResponseTypeDef:
        """
        Lists your experiment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_experiment_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_experiment_templates)
        """

    def list_experiments(
        self, *, maxResults: int = None, nextToken: str = None, experimentTemplateId: str = None
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists your experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_experiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_experiments)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_tags_for_resource)
        """

    def list_target_account_configurations(
        self, *, experimentTemplateId: str, maxResults: int = None, nextToken: str = None
    ) -> ListTargetAccountConfigurationsResponseTypeDef:
        """
        Lists the target account configurations of the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_target_account_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_target_account_configurations)
        """

    def list_target_resource_types(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListTargetResourceTypesResponseTypeDef:
        """
        Lists the target resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.list_target_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#list_target_resource_types)
        """

    def start_experiment(
        self,
        *,
        clientToken: str,
        experimentTemplateId: str,
        experimentOptions: "StartExperimentExperimentOptionsInputTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> StartExperimentResponseTypeDef:
        """
        Starts running an experiment from the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.start_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#start_experiment)
        """

    def stop_experiment(self, *, id: str) -> StopExperimentResponseTypeDef:
        """
        Stops the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.stop_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#stop_experiment)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str] = None) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.untag_resource)
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
        roleArn: str = None,
        logConfiguration: "UpdateExperimentTemplateLogConfigurationInputTypeDef" = None,
        experimentOptions: "UpdateExperimentTemplateExperimentOptionsInputTypeDef" = None
    ) -> UpdateExperimentTemplateResponseTypeDef:
        """
        Updates the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.update_experiment_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#update_experiment_template)
        """

    def update_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
        roleArn: str = None,
        description: str = None
    ) -> UpdateTargetAccountConfigurationResponseTypeDef:
        """
        Updates the target account configuration for the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/fis.html#FIS.Client.update_target_account_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/client.html#update_target_account_configuration)
        """
