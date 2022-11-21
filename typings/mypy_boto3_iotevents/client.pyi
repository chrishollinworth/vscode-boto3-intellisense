"""
Type annotations for iotevents service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents import IoTEventsClient

    client: IoTEventsClient = boto3.client("iotevents")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import EvaluationMethodType
from .type_defs import (
    AlarmCapabilitiesTypeDef,
    AlarmEventActionsTypeDef,
    AlarmNotificationTypeDef,
    AlarmRuleTypeDef,
    CreateAlarmModelResponseTypeDef,
    CreateDetectorModelResponseTypeDef,
    CreateInputResponseTypeDef,
    DescribeAlarmModelResponseTypeDef,
    DescribeDetectorModelAnalysisResponseTypeDef,
    DescribeDetectorModelResponseTypeDef,
    DescribeInputResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DetectorModelDefinitionTypeDef,
    GetDetectorModelAnalysisResultsResponseTypeDef,
    InputDefinitionTypeDef,
    InputIdentifierTypeDef,
    ListAlarmModelsResponseTypeDef,
    ListAlarmModelVersionsResponseTypeDef,
    ListDetectorModelsResponseTypeDef,
    ListDetectorModelVersionsResponseTypeDef,
    ListInputRoutingsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    StartDetectorModelAnalysisResponseTypeDef,
    TagTypeDef,
    UpdateAlarmModelResponseTypeDef,
    UpdateDetectorModelResponseTypeDef,
    UpdateInputResponseTypeDef,
)

__all__ = ("IoTEventsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class IoTEventsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTEventsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#close)
        """
    def create_alarm_model(
        self,
        *,
        alarmModelName: str,
        roleArn: str,
        alarmRule: "AlarmRuleTypeDef",
        alarmModelDescription: str = None,
        tags: List["TagTypeDef"] = None,
        key: str = None,
        severity: int = None,
        alarmNotification: "AlarmNotificationTypeDef" = None,
        alarmEventActions: "AlarmEventActionsTypeDef" = None,
        alarmCapabilities: "AlarmCapabilitiesTypeDef" = None
    ) -> CreateAlarmModelResponseTypeDef:
        """
        Creates an alarm model to monitor an AWS IoT Events input attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.create_alarm_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#create_alarm_model)
        """
    def create_detector_model(
        self,
        *,
        detectorModelName: str,
        detectorModelDefinition: "DetectorModelDefinitionTypeDef",
        roleArn: str,
        detectorModelDescription: str = None,
        key: str = None,
        tags: List["TagTypeDef"] = None,
        evaluationMethod: EvaluationMethodType = None
    ) -> CreateDetectorModelResponseTypeDef:
        """
        Creates a detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.create_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#create_detector_model)
        """
    def create_input(
        self,
        *,
        inputName: str,
        inputDefinition: "InputDefinitionTypeDef",
        inputDescription: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateInputResponseTypeDef:
        """
        Creates an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.create_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#create_input)
        """
    def delete_alarm_model(self, *, alarmModelName: str) -> Dict[str, Any]:
        """
        Deletes an alarm model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.delete_alarm_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#delete_alarm_model)
        """
    def delete_detector_model(self, *, detectorModelName: str) -> Dict[str, Any]:
        """
        Deletes a detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.delete_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#delete_detector_model)
        """
    def delete_input(self, *, inputName: str) -> Dict[str, Any]:
        """
        Deletes an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.delete_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#delete_input)
        """
    def describe_alarm_model(
        self, *, alarmModelName: str, alarmModelVersion: str = None
    ) -> DescribeAlarmModelResponseTypeDef:
        """
        Retrieves information about an alarm model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.describe_alarm_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe_alarm_model)
        """
    def describe_detector_model(
        self, *, detectorModelName: str, detectorModelVersion: str = None
    ) -> DescribeDetectorModelResponseTypeDef:
        """
        Describes a detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe_detector_model)
        """
    def describe_detector_model_analysis(
        self, *, analysisId: str
    ) -> DescribeDetectorModelAnalysisResponseTypeDef:
        """
        Retrieves runtime information about a detector model analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe_detector_model_analysis)
        """
    def describe_input(self, *, inputName: str) -> DescribeInputResponseTypeDef:
        """
        Describes an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.describe_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe_input)
        """
    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current settings of the AWS IoT Events logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.describe_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe_logging_options)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#generate_presigned_url)
        """
    def get_detector_model_analysis_results(
        self, *, analysisId: str, nextToken: str = None, maxResults: int = None
    ) -> GetDetectorModelAnalysisResultsResponseTypeDef:
        """
        Retrieves one or more analysis results of the detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.get_detector_model_analysis_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#get_detector_model_analysis_results)
        """
    def list_alarm_model_versions(
        self, *, alarmModelName: str, nextToken: str = None, maxResults: int = None
    ) -> ListAlarmModelVersionsResponseTypeDef:
        """
        Lists all the versions of an alarm model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_alarm_model_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_alarm_model_versions)
        """
    def list_alarm_models(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAlarmModelsResponseTypeDef:
        """
        Lists the alarm models that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_alarm_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_alarm_models)
        """
    def list_detector_model_versions(
        self, *, detectorModelName: str, nextToken: str = None, maxResults: int = None
    ) -> ListDetectorModelVersionsResponseTypeDef:
        """
        Lists all the versions of a detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_detector_model_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_detector_model_versions)
        """
    def list_detector_models(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDetectorModelsResponseTypeDef:
        """
        Lists the detector models you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_detector_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_detector_models)
        """
    def list_input_routings(
        self,
        *,
        inputIdentifier: "InputIdentifierTypeDef",
        maxResults: int = None,
        nextToken: str = None
    ) -> ListInputRoutingsResponseTypeDef:
        """
        Lists one or more input routings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_input_routings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_input_routings)
        """
    def list_inputs(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListInputsResponseTypeDef:
        """
        Lists the inputs you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_inputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_inputs)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list_tags_for_resource)
        """
    def put_logging_options(self, *, loggingOptions: "LoggingOptionsTypeDef") -> None:
        """
        Sets or updates the AWS IoT Events logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.put_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#put_logging_options)
        """
    def start_detector_model_analysis(
        self, *, detectorModelDefinition: "DetectorModelDefinitionTypeDef"
    ) -> StartDetectorModelAnalysisResponseTypeDef:
        """
        Performs an analysis of your detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.start_detector_model_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#start_detector_model_analysis)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#untag_resource)
        """
    def update_alarm_model(
        self,
        *,
        alarmModelName: str,
        roleArn: str,
        alarmRule: "AlarmRuleTypeDef",
        alarmModelDescription: str = None,
        severity: int = None,
        alarmNotification: "AlarmNotificationTypeDef" = None,
        alarmEventActions: "AlarmEventActionsTypeDef" = None,
        alarmCapabilities: "AlarmCapabilitiesTypeDef" = None
    ) -> UpdateAlarmModelResponseTypeDef:
        """
        Updates an alarm model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.update_alarm_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#update_alarm_model)
        """
    def update_detector_model(
        self,
        *,
        detectorModelName: str,
        detectorModelDefinition: "DetectorModelDefinitionTypeDef",
        roleArn: str,
        detectorModelDescription: str = None,
        evaluationMethod: EvaluationMethodType = None
    ) -> UpdateDetectorModelResponseTypeDef:
        """
        Updates a detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.update_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#update_detector_model)
        """
    def update_input(
        self,
        *,
        inputName: str,
        inputDefinition: "InputDefinitionTypeDef",
        inputDescription: str = None
    ) -> UpdateInputResponseTypeDef:
        """
        Updates an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/iotevents.html#IoTEvents.Client.update_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#update_input)
        """
