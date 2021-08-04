"""
Type annotations for lexv2-models service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/literals.html)

Usage::

    ```python
    from mypy_boto3_lexv2_models.literals import BotAliasAvailableWaiterName

    data: BotAliasAvailableWaiterName = "bot_alias_available"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BotAliasAvailableWaiterName",
    "BotAliasStatusType",
    "BotAvailableWaiterName",
    "BotExportCompletedWaiterName",
    "BotFilterNameType",
    "BotFilterOperatorType",
    "BotImportCompletedWaiterName",
    "BotLocaleBuiltWaiterName",
    "BotLocaleCreatedWaiterName",
    "BotLocaleExpressTestingAvailableWaiterName",
    "BotLocaleFilterNameType",
    "BotLocaleFilterOperatorType",
    "BotLocaleSortAttributeType",
    "BotLocaleStatusType",
    "BotSortAttributeType",
    "BotStatusType",
    "BotVersionAvailableWaiterName",
    "BotVersionSortAttributeType",
    "BuiltInIntentSortAttributeType",
    "BuiltInSlotTypeSortAttributeType",
    "EffectType",
    "ExportFilterNameType",
    "ExportFilterOperatorType",
    "ExportSortAttributeType",
    "ExportStatusType",
    "ImportExportFileFormatType",
    "ImportFilterNameType",
    "ImportFilterOperatorType",
    "ImportSortAttributeType",
    "ImportStatusType",
    "IntentFilterNameType",
    "IntentFilterOperatorType",
    "IntentSortAttributeType",
    "MergeStrategyType",
    "ObfuscationSettingTypeType",
    "SlotConstraintType",
    "SlotFilterNameType",
    "SlotFilterOperatorType",
    "SlotSortAttributeType",
    "SlotTypeFilterNameType",
    "SlotTypeFilterOperatorType",
    "SlotTypeSortAttributeType",
    "SlotValueResolutionStrategyType",
    "SortOrderType",
)

BotAliasAvailableWaiterName = Literal["bot_alias_available"]
BotAliasStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotAvailableWaiterName = Literal["bot_available"]
BotExportCompletedWaiterName = Literal["bot_export_completed"]
BotFilterNameType = Literal["BotName"]
BotFilterOperatorType = Literal["CO", "EQ"]
BotImportCompletedWaiterName = Literal["bot_import_completed"]
BotLocaleBuiltWaiterName = Literal["bot_locale_built"]
BotLocaleCreatedWaiterName = Literal["bot_locale_created"]
BotLocaleExpressTestingAvailableWaiterName = Literal["bot_locale_express_testing_available"]
BotLocaleFilterNameType = Literal["BotLocaleName"]
BotLocaleFilterOperatorType = Literal["CO", "EQ"]
BotLocaleSortAttributeType = Literal["BotLocaleName"]
BotLocaleStatusType = Literal[
    "Building",
    "Built",
    "Creating",
    "Deleting",
    "Failed",
    "Importing",
    "NotBuilt",
    "ReadyExpressTesting",
]
BotSortAttributeType = Literal["BotName"]
BotStatusType = Literal[
    "Available", "Creating", "Deleting", "Failed", "Importing", "Inactive", "Versioning"
]
BotVersionAvailableWaiterName = Literal["bot_version_available"]
BotVersionSortAttributeType = Literal["BotVersion"]
BuiltInIntentSortAttributeType = Literal["IntentSignature"]
BuiltInSlotTypeSortAttributeType = Literal["SlotTypeSignature"]
EffectType = Literal["Allow", "Deny"]
ExportFilterNameType = Literal["ExportResourceType"]
ExportFilterOperatorType = Literal["CO", "EQ"]
ExportSortAttributeType = Literal["LastUpdatedDateTime"]
ExportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
ImportExportFileFormatType = Literal["LexJson"]
ImportFilterNameType = Literal["ImportResourceType"]
ImportFilterOperatorType = Literal["CO", "EQ"]
ImportSortAttributeType = Literal["LastUpdatedDateTime"]
ImportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
IntentFilterNameType = Literal["IntentName"]
IntentFilterOperatorType = Literal["CO", "EQ"]
IntentSortAttributeType = Literal["IntentName", "LastUpdatedDateTime"]
MergeStrategyType = Literal["FailOnConflict", "Overwrite"]
ObfuscationSettingTypeType = Literal["DefaultObfuscation", "None"]
SlotConstraintType = Literal["Optional", "Required"]
SlotFilterNameType = Literal["SlotName"]
SlotFilterOperatorType = Literal["CO", "EQ"]
SlotSortAttributeType = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeFilterNameType = Literal["SlotTypeName"]
SlotTypeFilterOperatorType = Literal["CO", "EQ"]
SlotTypeSortAttributeType = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategyType = Literal["OriginalValue", "TopResolution"]
SortOrderType = Literal["Ascending", "Descending"]
