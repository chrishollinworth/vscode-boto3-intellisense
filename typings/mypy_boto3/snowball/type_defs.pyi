"""
Type annotations for snowball service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/type_defs.html)

Usage::

    ```python
    from mypy_boto3_snowball.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ClusterStateType,
    DeviceServiceNameType,
    JobStateType,
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ShipmentStateType,
    ShippingLabelStatusType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
    TransferOptionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddressTypeDef",
    "CancelClusterRequestRequestTypeDef",
    "CancelJobRequestRequestTypeDef",
    "ClusterListEntryTypeDef",
    "ClusterMetadataTypeDef",
    "CompatibleImageTypeDef",
    "CreateAddressRequestRequestTypeDef",
    "CreateAddressResultTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResultTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResultTypeDef",
    "CreateLongTermPricingRequestRequestTypeDef",
    "CreateLongTermPricingResultTypeDef",
    "CreateReturnShippingLabelRequestRequestTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DataTransferTypeDef",
    "DescribeAddressRequestRequestTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResultTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "DeviceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestRequestRequestTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeRequestRequestTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesRequestRequestTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobListEntryTypeDef",
    "JobLogsTypeDef",
    "JobMetadataTypeDef",
    "JobResourceTypeDef",
    "KeyRangeTypeDef",
    "LambdaResourceTypeDef",
    "ListClusterJobsRequestRequestTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesRequestRequestTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListLongTermPricingRequestRequestTypeDef",
    "ListLongTermPricingResultTypeDef",
    "LongTermPricingListEntryTypeDef",
    "NFSOnDeviceServiceConfigurationTypeDef",
    "NotificationTypeDef",
    "OnDeviceServiceConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ResourceTypeDef",
    "ShipmentTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "TargetOnDeviceServiceTypeDef",
    "TaxDocumentsTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateJobShipmentStateRequestRequestTypeDef",
    "UpdateLongTermPricingRequestRequestTypeDef",
    "WirelessConnectionTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

CancelClusterRequestRequestTypeDef = TypedDict(
    "CancelClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": str,
        "ClusterState": ClusterStateType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": ClusterStateType,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Resources": "JobResourceTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
    },
    total=False,
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef",
    {
        "AmiId": str,
        "Name": str,
    },
    total=False,
)

CreateAddressRequestRequestTypeDef = TypedDict(
    "CreateAddressRequestRequestTypeDef",
    {
        "Address": "AddressTypeDef",
    },
)

CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef",
    {
        "AddressId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Resources": "JobResourceTypeDef",
        "AddressId": str,
        "RoleARN": str,
        "SnowballType": SnowballTypeType,
        "ShippingOption": ShippingOptionType,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "Description": str,
        "KmsKeyARN": str,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "RemoteManagement": RemoteManagementType,
    },
    total=False,
)

class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "ClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Resources": "JobResourceTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "Description": str,
        "AddressId": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "SnowballCapacityPreference": SnowballCapacityType,
        "ShippingOption": ShippingOptionType,
        "Notification": "NotificationTypeDef",
        "ClusterId": str,
        "SnowballType": SnowballTypeType,
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "DeviceConfiguration": "DeviceConfigurationTypeDef",
        "RemoteManagement": RemoteManagementType,
        "LongTermPricingId": str,
    },
    total=False,
)

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingType": LongTermPricingTypeType,
    },
)
_OptionalCreateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLongTermPricingRequestRequestTypeDef",
    {
        "IsLongTermPricingAutoRenew": bool,
        "SnowballType": SnowballTypeType,
    },
    total=False,
)

class CreateLongTermPricingRequestRequestTypeDef(
    _RequiredCreateLongTermPricingRequestRequestTypeDef,
    _OptionalCreateLongTermPricingRequestRequestTypeDef,
):
    pass

CreateLongTermPricingResultTypeDef = TypedDict(
    "CreateLongTermPricingResultTypeDef",
    {
        "LongTermPricingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalCreateReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReturnShippingLabelRequestRequestTypeDef",
    {
        "ShippingOption": ShippingOptionType,
    },
    total=False,
)

class CreateReturnShippingLabelRequestRequestTypeDef(
    _RequiredCreateReturnShippingLabelRequestRequestTypeDef,
    _OptionalCreateReturnShippingLabelRequestRequestTypeDef,
):
    pass

CreateReturnShippingLabelResultTypeDef = TypedDict(
    "CreateReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {
        "BytesTransferred": int,
        "ObjectsTransferred": int,
        "TotalBytes": int,
        "TotalObjects": int,
    },
    total=False,
)

DescribeAddressRequestRequestTypeDef = TypedDict(
    "DescribeAddressRequestRequestTypeDef",
    {
        "AddressId": str,
    },
)

DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef",
    {
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef",
    {
        "ClusterMetadata": "ClusterMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "JobMetadata": "JobMetadataTypeDef",
        "SubJobMetadata": List["JobMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeReturnShippingLabelResultTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ExpirationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeDef = TypedDict(
    "DeviceConfigurationTypeDef",
    {
        "SnowconeDeviceConfiguration": "SnowconeDeviceConfigurationTypeDef",
    },
    total=False,
)

_RequiredEc2AmiResourceTypeDef = TypedDict(
    "_RequiredEc2AmiResourceTypeDef",
    {
        "AmiId": str,
    },
)
_OptionalEc2AmiResourceTypeDef = TypedDict(
    "_OptionalEc2AmiResourceTypeDef",
    {
        "SnowballAmiId": str,
    },
    total=False,
)

class Ec2AmiResourceTypeDef(_RequiredEc2AmiResourceTypeDef, _OptionalEc2AmiResourceTypeDef):
    pass

EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef",
    {
        "EventResourceARN": str,
    },
    total=False,
)

GetJobManifestRequestRequestTypeDef = TypedDict(
    "GetJobManifestRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef",
    {
        "ManifestURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobUnlockCodeRequestRequestTypeDef = TypedDict(
    "GetJobUnlockCodeRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef",
    {
        "UnlockCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef",
    {
        "SnowballLimit": int,
        "SnowballsInUse": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSoftwareUpdatesRequestRequestTypeDef = TypedDict(
    "GetSoftwareUpdatesRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef",
    {
        "UpdatesURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

INDTaxDocumentsTypeDef = TypedDict(
    "INDTaxDocumentsTypeDef",
    {
        "GSTIN": str,
    },
    total=False,
)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": str,
        "JobState": JobStateType,
        "IsMaster": bool,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {
        "JobCompletionReportURI": str,
        "JobSuccessLogURI": str,
        "JobFailureLogURI": str,
    },
    total=False,
)

JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": JobStateType,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Resources": "JobResourceTypeDef",
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": "ShippingDetailsTypeDef",
        "SnowballCapacityPreference": SnowballCapacityType,
        "Notification": "NotificationTypeDef",
        "DataTransferProgress": "DataTransferTypeDef",
        "JobLogInfo": "JobLogsTypeDef",
        "ClusterId": str,
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "DeviceConfiguration": "DeviceConfigurationTypeDef",
        "RemoteManagement": RemoteManagementType,
        "LongTermPricingId": str,
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
    },
    total=False,
)

JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": List["S3ResourceTypeDef"],
        "LambdaResources": List["LambdaResourceTypeDef"],
        "Ec2AmiResources": List["Ec2AmiResourceTypeDef"],
    },
    total=False,
)

KeyRangeTypeDef = TypedDict(
    "KeyRangeTypeDef",
    {
        "BeginMarker": str,
        "EndMarker": str,
    },
    total=False,
)

LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List["EventTriggerDefinitionTypeDef"],
    },
    total=False,
)

_RequiredListClusterJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListClusterJobsRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListClusterJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListClusterJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListClusterJobsRequestRequestTypeDef(
    _RequiredListClusterJobsRequestRequestTypeDef, _OptionalListClusterJobsRequestRequestTypeDef
):
    pass

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {
        "ClusterListEntries": List["ClusterListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCompatibleImagesRequestRequestTypeDef = TypedDict(
    "ListCompatibleImagesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {
        "CompatibleImages": List["CompatibleImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLongTermPricingRequestRequestTypeDef = TypedDict(
    "ListLongTermPricingRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLongTermPricingResultTypeDef = TypedDict(
    "ListLongTermPricingResultTypeDef",
    {
        "LongTermPricingEntries": List["LongTermPricingListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LongTermPricingListEntryTypeDef = TypedDict(
    "LongTermPricingListEntryTypeDef",
    {
        "LongTermPricingId": str,
        "LongTermPricingEndDate": datetime,
        "LongTermPricingStartDate": datetime,
        "LongTermPricingType": LongTermPricingTypeType,
        "CurrentActiveJob": str,
        "ReplacementJob": str,
        "IsLongTermPricingAutoRenew": bool,
        "LongTermPricingStatus": str,
        "SnowballType": SnowballTypeType,
        "JobIds": List[str],
    },
    total=False,
)

NFSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "NFSOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": int,
        "StorageUnit": Literal["TB"],
    },
    total=False,
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[JobStateType],
        "NotifyAll": bool,
    },
    total=False,
)

OnDeviceServiceConfigurationTypeDef = TypedDict(
    "OnDeviceServiceConfigurationTypeDef",
    {
        "NFSOnDeviceService": "NFSOnDeviceServiceConfigurationTypeDef",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "BucketArn": str,
        "KeyRange": "KeyRangeTypeDef",
        "TargetOnDeviceServices": List["TargetOnDeviceServiceTypeDef"],
    },
    total=False,
)

ShipmentTypeDef = TypedDict(
    "ShipmentTypeDef",
    {
        "Status": str,
        "TrackingNumber": str,
    },
    total=False,
)

ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": ShippingOptionType,
        "InboundShipment": "ShipmentTypeDef",
        "OutboundShipment": "ShipmentTypeDef",
    },
    total=False,
)

SnowconeDeviceConfigurationTypeDef = TypedDict(
    "SnowconeDeviceConfigurationTypeDef",
    {
        "WirelessConnection": "WirelessConnectionTypeDef",
    },
    total=False,
)

TargetOnDeviceServiceTypeDef = TypedDict(
    "TargetOnDeviceServiceTypeDef",
    {
        "ServiceName": DeviceServiceNameType,
        "TransferOption": TransferOptionType,
    },
    total=False,
)

TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef",
    {
        "IND": "INDTaxDocumentsTypeDef",
    },
    total=False,
)

_RequiredUpdateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalUpdateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestRequestTypeDef",
    {
        "RoleARN": str,
        "Description": str,
        "Resources": "JobResourceTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
    },
    total=False,
)

class UpdateClusterRequestRequestTypeDef(
    _RequiredUpdateClusterRequestRequestTypeDef, _OptionalUpdateClusterRequestRequestTypeDef
):
    pass

_RequiredUpdateJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalUpdateJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestRequestTypeDef",
    {
        "RoleARN": str,
        "Notification": "NotificationTypeDef",
        "Resources": "JobResourceTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Description": str,
        "SnowballCapacityPreference": SnowballCapacityType,
        "ForwardingAddressId": str,
    },
    total=False,
)

class UpdateJobRequestRequestTypeDef(
    _RequiredUpdateJobRequestRequestTypeDef, _OptionalUpdateJobRequestRequestTypeDef
):
    pass

UpdateJobShipmentStateRequestRequestTypeDef = TypedDict(
    "UpdateJobShipmentStateRequestRequestTypeDef",
    {
        "JobId": str,
        "ShipmentState": ShipmentStateType,
    },
)

_RequiredUpdateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingId": str,
    },
)
_OptionalUpdateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLongTermPricingRequestRequestTypeDef",
    {
        "ReplacementJob": str,
        "IsLongTermPricingAutoRenew": bool,
    },
    total=False,
)

class UpdateLongTermPricingRequestRequestTypeDef(
    _RequiredUpdateLongTermPricingRequestRequestTypeDef,
    _OptionalUpdateLongTermPricingRequestRequestTypeDef,
):
    pass

WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef",
    {
        "IsWifiEnabled": bool,
    },
    total=False,
)
