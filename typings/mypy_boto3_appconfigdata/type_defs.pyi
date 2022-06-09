"""
Type annotations for appconfigdata service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appconfigdata.type_defs import GetLatestConfigurationRequestRequestTypeDef

    data: GetLatestConfigurationRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetLatestConfigurationRequestRequestTypeDef",
    "GetLatestConfigurationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartConfigurationSessionRequestRequestTypeDef",
    "StartConfigurationSessionResponseTypeDef",
)

GetLatestConfigurationRequestRequestTypeDef = TypedDict(
    "GetLatestConfigurationRequestRequestTypeDef",
    {
        "ConfigurationToken": str,
    },
)

GetLatestConfigurationResponseTypeDef = TypedDict(
    "GetLatestConfigurationResponseTypeDef",
    {
        "NextPollConfigurationToken": str,
        "NextPollIntervalInSeconds": int,
        "ContentType": str,
        "Configuration": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStartConfigurationSessionRequestRequestTypeDef = TypedDict(
    "_RequiredStartConfigurationSessionRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ConfigurationProfileIdentifier": str,
    },
)
_OptionalStartConfigurationSessionRequestRequestTypeDef = TypedDict(
    "_OptionalStartConfigurationSessionRequestRequestTypeDef",
    {
        "RequiredMinimumPollIntervalInSeconds": int,
    },
    total=False,
)

class StartConfigurationSessionRequestRequestTypeDef(
    _RequiredStartConfigurationSessionRequestRequestTypeDef,
    _OptionalStartConfigurationSessionRequestRequestTypeDef,
):
    pass

StartConfigurationSessionResponseTypeDef = TypedDict(
    "StartConfigurationSessionResponseTypeDef",
    {
        "InitialConfigurationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
