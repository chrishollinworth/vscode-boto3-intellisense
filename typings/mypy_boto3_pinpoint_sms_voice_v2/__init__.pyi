"""
Main interface for pinpoint-sms-voice-v2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_sms_voice_v2 import (
        Client,
        DescribeAccountAttributesPaginator,
        DescribeAccountLimitsPaginator,
        DescribeConfigurationSetsPaginator,
        DescribeKeywordsPaginator,
        DescribeOptOutListsPaginator,
        DescribeOptedOutNumbersPaginator,
        DescribePhoneNumbersPaginator,
        DescribePoolsPaginator,
        DescribeRegistrationAttachmentsPaginator,
        DescribeRegistrationFieldDefinitionsPaginator,
        DescribeRegistrationFieldValuesPaginator,
        DescribeRegistrationSectionDefinitionsPaginator,
        DescribeRegistrationTypeDefinitionsPaginator,
        DescribeRegistrationVersionsPaginator,
        DescribeRegistrationsPaginator,
        DescribeSenderIdsPaginator,
        DescribeSpendLimitsPaginator,
        DescribeVerifiedDestinationNumbersPaginator,
        ListPoolOriginationIdentitiesPaginator,
        ListRegistrationAssociationsPaginator,
        PinpointSMSVoiceV2Client,
    )

    session = boto3.Session()

    client: PinpointSMSVoiceV2Client = boto3.client("pinpoint-sms-voice-v2")
    session_client: PinpointSMSVoiceV2Client = session.client("pinpoint-sms-voice-v2")

    describe_account_attributes_paginator: DescribeAccountAttributesPaginator = client.get_paginator("describe_account_attributes")
    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_configuration_sets_paginator: DescribeConfigurationSetsPaginator = client.get_paginator("describe_configuration_sets")
    describe_keywords_paginator: DescribeKeywordsPaginator = client.get_paginator("describe_keywords")
    describe_opt_out_lists_paginator: DescribeOptOutListsPaginator = client.get_paginator("describe_opt_out_lists")
    describe_opted_out_numbers_paginator: DescribeOptedOutNumbersPaginator = client.get_paginator("describe_opted_out_numbers")
    describe_phone_numbers_paginator: DescribePhoneNumbersPaginator = client.get_paginator("describe_phone_numbers")
    describe_pools_paginator: DescribePoolsPaginator = client.get_paginator("describe_pools")
    describe_registration_attachments_paginator: DescribeRegistrationAttachmentsPaginator = client.get_paginator("describe_registration_attachments")
    describe_registration_field_definitions_paginator: DescribeRegistrationFieldDefinitionsPaginator = client.get_paginator("describe_registration_field_definitions")
    describe_registration_field_values_paginator: DescribeRegistrationFieldValuesPaginator = client.get_paginator("describe_registration_field_values")
    describe_registration_section_definitions_paginator: DescribeRegistrationSectionDefinitionsPaginator = client.get_paginator("describe_registration_section_definitions")
    describe_registration_type_definitions_paginator: DescribeRegistrationTypeDefinitionsPaginator = client.get_paginator("describe_registration_type_definitions")
    describe_registration_versions_paginator: DescribeRegistrationVersionsPaginator = client.get_paginator("describe_registration_versions")
    describe_registrations_paginator: DescribeRegistrationsPaginator = client.get_paginator("describe_registrations")
    describe_sender_ids_paginator: DescribeSenderIdsPaginator = client.get_paginator("describe_sender_ids")
    describe_spend_limits_paginator: DescribeSpendLimitsPaginator = client.get_paginator("describe_spend_limits")
    describe_verified_destination_numbers_paginator: DescribeVerifiedDestinationNumbersPaginator = client.get_paginator("describe_verified_destination_numbers")
    list_pool_origination_identities_paginator: ListPoolOriginationIdentitiesPaginator = client.get_paginator("list_pool_origination_identities")
    list_registration_associations_paginator: ListRegistrationAssociationsPaginator = client.get_paginator("list_registration_associations")
    ```
"""
from .client import PinpointSMSVoiceV2Client
from .paginator import (
    DescribeAccountAttributesPaginator,
    DescribeAccountLimitsPaginator,
    DescribeConfigurationSetsPaginator,
    DescribeKeywordsPaginator,
    DescribeOptedOutNumbersPaginator,
    DescribeOptOutListsPaginator,
    DescribePhoneNumbersPaginator,
    DescribePoolsPaginator,
    DescribeRegistrationAttachmentsPaginator,
    DescribeRegistrationFieldDefinitionsPaginator,
    DescribeRegistrationFieldValuesPaginator,
    DescribeRegistrationSectionDefinitionsPaginator,
    DescribeRegistrationsPaginator,
    DescribeRegistrationTypeDefinitionsPaginator,
    DescribeRegistrationVersionsPaginator,
    DescribeSenderIdsPaginator,
    DescribeSpendLimitsPaginator,
    DescribeVerifiedDestinationNumbersPaginator,
    ListPoolOriginationIdentitiesPaginator,
    ListRegistrationAssociationsPaginator,
)

Client = PinpointSMSVoiceV2Client

__all__ = (
    "Client",
    "DescribeAccountAttributesPaginator",
    "DescribeAccountLimitsPaginator",
    "DescribeConfigurationSetsPaginator",
    "DescribeKeywordsPaginator",
    "DescribeOptOutListsPaginator",
    "DescribeOptedOutNumbersPaginator",
    "DescribePhoneNumbersPaginator",
    "DescribePoolsPaginator",
    "DescribeRegistrationAttachmentsPaginator",
    "DescribeRegistrationFieldDefinitionsPaginator",
    "DescribeRegistrationFieldValuesPaginator",
    "DescribeRegistrationSectionDefinitionsPaginator",
    "DescribeRegistrationTypeDefinitionsPaginator",
    "DescribeRegistrationVersionsPaginator",
    "DescribeRegistrationsPaginator",
    "DescribeSenderIdsPaginator",
    "DescribeSpendLimitsPaginator",
    "DescribeVerifiedDestinationNumbersPaginator",
    "ListPoolOriginationIdentitiesPaginator",
    "ListRegistrationAssociationsPaginator",
    "PinpointSMSVoiceV2Client",
)
