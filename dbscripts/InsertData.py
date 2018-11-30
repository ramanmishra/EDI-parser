from pymongo import MongoClient

# read json from the db

client = MongoClient()
db = client.makeathon
post = {
    "name": "HealthCare",
    "active_template": "HealthCareTemplate",
    "active_version": "v1",
    "templates": [{"name": "hippa",
                   "version": "v1",
                   "config": {
                       "header_0": {"before": "Hippa"},
                       "isa": {
                           "0": "InterchangeControlHeader2",
                           "1": "AuthorizationInformationQualifier",
                           "2": "AuthorizationInformation",
                           "3": "SecurityInformationQualifier",
                           "4": "SecurityInformation",
                           "5": "InterchangeIdQualifier",
                           "6": "InterchangeSenderId",
                           "7": "InterchangeIdQualifier",
                           "8": "InterchangeReceiverId",
                           "10": "RepetitionSeparator",
                           "11": "InterchangeTime",
                           "12": "InterchangeControlVersionNumber",
                           "13": "InterchangeControlNumber",
                           "14": "AcknowledgementRequired",
                           "15": "UsageIndicator",
                           "16": "ComponentElementSeparator"
                       },
                       "header_1": {"before": "Group"},
                       "gs": {
                           "0": "FunctionalGroupHeader",
                           "1": "FunctionalIdentifierCode",
                           "2": "ApplicationSenderCode",
                           "3": "ApplicationReceivercode",
                           "4": "Date",
                           "5": "Time",
                           "6": "GroupControlNumber",
                           "7": "ResponsibleAgencyCode",
                           "8": "VersionReleaseNo"
                       },
                       "header_2": {"before": "Transaction"},
                       "st": {
                           "0": "TransactionSetHeader",
                           "1": "TransactionSetIdentifier",
                           "2": "TransactionSetControlNumber",
                           "3": "ImplementationConventionReference"
                       },
                       "header_3": {"before": "Segment"},
                       "bht": {
                           "0": "BeginningOfHierarchicalSegment",
                           "1": "HierarchicalStructureCode", "2": "TransactionSetPurposeCode",
                           "3": "ReferenceIdentification",
                           "4": "Date",
                           "5": "InterchangeIdQualifier",
                           "6": "TransactionTypeCode"
                       },
                       "nm1": {
                           "0": [
                               "SubmitterName",
                               "ReceiverName",
                               "BillingProviderName",
                               "SubscriberName",
                               "PayerName",
                               "ReferringProviderName",
                               "RenderingProviderName",
                               "ServiceFacilityLocation",
                               "OtherSubscriberName",
                               "OtherPayerName"
                           ],
                           "1": "EntityIdentifierCode",
                           "2": "EntityTypeQualifier",
                           "3": [
                               "NameLast",
                               "OrganizationName"
                           ],
                           "4": "NameFirst",
                           "5": "NameMiddle",
                           "6": "NamePrefix",
                           "7": "NameSuffix",
                           "8": "IdentificationCodeQualifier",
                           "9": "IdentificationCode"
                       },
                       "n3": {
                           "0": "SubscriberAddress",
                           "1": "AddressLine1",
                           "2": "AddressLine2"
                       },
                       "n4": {
                           "0": "SubscriberCityStateZipCode",
                           "1": "CityName",
                           "2": "StateOrProvinceCode",
                           "3": "PostalCode"
                       },
                       "hl": {
                           "0": ["BillingHierarchicalLevel", "SubscriberHierarchicalLevel", "PatientHierarchicalLevel"],
                           "1": ["HierarchicalIdNumber", "SubscriberIDNumber"],
                           "2": "HierarchicalParentIdNumber",
                           "3": "HierarchicalLevelCode",
                           "4": "HierarchicalChildCode"
                       },
                       "clm": {
                           "0": "ClaimInformation",
                           "1": "ClaimSubmitterIdentifier",
                           "2": "MonetaryAmount",
                           "3": "ClaimFillingIndicator",
                           "4": "NonInstitutionalClaimType",
                           "5": "FacilityCodeValue",
                           "6": "FacilityCodeQualifier",
                           "7": "ClaimFrequencyTypeCode",
                           "8": "YesNoProviderSignatureonFile",
                           "9": "ProviderAcceptAssignmentCode",
                           "10": "YesNoAssignmentsofBenefit",
                           "11": "YesNoReleaseofInformation",
                           "12": "PatientSignatureSourceCode"
                       },
                       "dtp": {
                           "0": [
                               "DateOnsetOfCurrentIllnessSymptom",
                               "DateInitialTreatment",
                               "DateLastSeen",
                               "DateAcuteManifestation",
                               "DateAccident",
                               "DateInitialMenstrual",
                               "DateLastXRayMenstrual",
                               "DateHearingAndVisionPrescriptionDate",
                               "DateLastWorked",
                               "ServiceDate",
                               "LineAdjudicationDate"
                           ],
                           "1": "DateTimeQualifier",
                           "2": "DateTimePeriodFormatQualifier",
                           "3": "DateTimePeriod"
                       },
                       "ref": {
                           "0": [
                               "CLIANumber",
                               "PriorAuthorizationOrReferralNumber"
                           ],
                           "1": "ReferenceIdentificationQualifier",
                           "2": "ReferenceIdentification"
                       },
                       "k3": {
                           "0": "ClaimInformation",
                           "1": "FixedFormatInformation"
                       },
                       "hi": {
                           "0": "HealthCareDiagnosisCode",
                           "1": "CodeListQualifierCode",
                           "2": "IndustryCode"
                       },
                       "sbr": {
                           "0": "SubscriberInformation",
                           "1": "PayerResponsibilityCode",
                           "2": "IndividualRelationshipCode",
                           "3": "ReferenceIdentification",
                           "4": "Name",
                           "5": "InsuranceTypeCode",
                           "6": "CoordinationOfBenefitCode",
                           "7": "YesNoCondition",
                           "8": "EmploymentStatusCode",
                           "9": "ClaimFillingIndicatorCode"
                       },
                       "lx": {
                           "0": "ServiceLine",
                           "1": "AssignedNumber"
                       },
                       "sv1": {
                           "0": "ProfessionalService",
                           "1": "ProductServiceIdQualifier : ProductServiceID : ProcedureModifier : ProcedureModifier : ProcedureModifier : ProcedureModifier",
                           "2": "MonetaryAmount",
                           "3": "Unit",
                           "4": "Quantity",
                           "5": "FacilityCodeValue",
                           "6": "ServiceTypeCode",
                           "7": "DiagnosisCodePointer : DiagnosisCodePointer : DiagnosisCodePointer : DiagnosisCodePointer : MonetaryAmount : YesNoEmergencyIndicator: MultipleProcedureCode : YesNoEPSDTIndicator : YesNoFamilyPlanningIndicator : ReviewCode : NationalOrLocalAssignedReviewValue : CopayStatusCode"
                       },
                       "svd": {
                           "0": "LineAdjudicationInformation",
                           "1": "IdentificationCode",
                           "2": "MonetaryAmount",
                           "3": "ProductServiceIDQualifier",
                           "4": "Description",
                           "5": "Quantity"
                       },
                       "cas": {
                           "0": "LineAdjustment",
                           "1": "ClaimAdjustmentGroupCode",
                           "2": "ClaimAdjustmentReasonCode",
                           "3": "MonetaryAmount"
                       },
                       "trailer_3": {"after": "/Segment"},
                       "se": {
                           "0": [
                               "TransactionSetTrailer",
                               "TransactionSetHeader"
                           ],
                           "1": "NumberofIncludedSegments",
                           "2": "TransactionSetControlNumber"
                       },
                       "trailer_2": {"after": "/Transaction"},
                       "ge": {
                           "0": [
                               "FunctionalGroupTrailer",
                               "FunctionalGroupHeader"
                           ],
                           "1": "NumberOfTransactionsSetsIncluded",
                           "2": "GroupControlNumber"
                       },
                       "trailer_1": {"after": "/Group"},
                       "iea": {
                           "0": "InterchangeControlTrailer",
                           "1": "NumberOfIncludedFunctionalGroups",
                           "2": "InterchangeControlNumber"
                       },
                       "trailer_0": {"after": "/Hippa"}
                   },
                   }, {"name": "hippa",
                       "version": "v2",
                       "config": {
                           "header_0": {"before": "Hippa"},
                           "isa": {
                               "0": "InterchangeControlHeader2"
                           },
                           "header_1": {"before": "Group"},
                           "gs": {
                               "0": "FunctionalGroupHeader",
                               "1": "FunctionalIdentifierCode",
                               "2": "ApplicationSenderCode",
                               "3": "ApplicationReceivercode",
                               "4": "Date",
                               "5": "Time",
                               "6": "GroupControlNumber",
                               "7": "ResponsibleAgencyCode",
                               "8": "VersionReleaseNo"
                           },
                           "header_2": {"before": "Transaction"},
                           "st": {
                               "0": "TransactionSetHeader",
                               "1": "TransactionSetIdentifier",
                               "2": "TransactionSetControlNumber",
                               "3": "ImplementationConventionReference"
                           },
                           "header_3": {"before": "Segment"},
                           "bht": {
                               "0": "BeginningOfHierarchicalSegment",
                               "1": "HierarchicalStructureCode", "2": "TransactionSetPurposeCode",
                               "3": "ReferenceIdentification",
                               "4": "Date",
                               "5": "InterchangeIdQualifier",
                               "6": "TransactionTypeCode"
                           },
                           "nm1": {
                               "0": [
                                   "SubmitterName",
                                   "ReceiverName",
                                   "BillingProviderName",
                                   "SubscriberName",
                                   "PayerName",
                                   "ReferringProviderName",
                                   "RenderingProviderName",
                                   "ServiceFacilityLocation",
                                   "OtherSubscriberName",
                                   "OtherPayerName"
                               ],
                               "1": "EntityIdentifierCode",
                               "2": "EntityTypeQualifier",
                               "3": [
                                   "NameLast",
                                   "OrganizationName"
                               ],
                               "4": "NameFirst",
                               "5": "NameMiddle",
                               "6": "NamePrefix",
                               "7": "NameSuffix",
                               "8": "IdentificationCodeQualifier",
                               "9": "IdentificationCode"
                           },
                           "n3": {
                               "0": "SubscriberAddress",
                               "1": "AddressLine1",
                               "2": "AddressLine2"
                           },
                           "n4": {
                               "0": "SubscriberCityStateZipCode",
                               "1": "CityName",
                               "2": "StateOrProvinceCode",
                               "3": "PostalCode"
                           },
                           "hl": {
                               "0": ["BillingHierarchicalLevel", "SubscriberHierarchicalLevel", "PatientHierarchicalLevel"],
                               "1": ["HierarchicalIdNumber", "SubscriberIDNumber"],
                               "2": "HierarchicalParentIdNumber",
                               "3": "HierarchicalLevelCode",
                               "4": "HierarchicalChildCode"
                           },
                           "clm": {
                               "0": "ClaimInformation",
                               "1": "ClaimSubmitterIdentifier",
                               "2": "MonetaryAmount",
                               "3": "ClaimFillingIndicator",
                               "4": "NonInstitutionalClaimType",
                               "5": "FacilityCodeValue",
                               "6": "FacilityCodeQualifier",
                               "7": "ClaimFrequencyTypeCode",
                               "8": "YesNoProviderSignatureonFile",
                               "9": "ProviderAcceptAssignmentCode",
                               "10": "YesNoAssignmentsofBenefit",
                               "11": "YesNoReleaseofInformation",
                               "12": "PatientSignatureSourceCode"
                           },
                           "dtp": {
                               "0": [
                                   "DateOnsetOfCurrentIllnessSymptom",
                                   "DateInitialTreatment",
                                   "DateLastSeen",
                                   "DateAcuteManifestation",
                                   "DateAccident",
                                   "DateInitialMenstrual",
                                   "DateLastXRayMenstrual",
                                   "DateHearingAndVisionPrescriptionDate",
                                   "DateLastWorked",
                                   "ServiceDate",
                                   "LineAdjudicationDate"
                               ],
                               "1": "DateTimeQualifier",
                               "2": "DateTimePeriodFormatQualifier",
                               "3": "DateTimePeriod"
                           },
                           "ref": {
                               "0": [
                                   "CLIANumber",
                                   "PriorAuthorizationOrReferralNumber"
                               ],
                               "1": "ReferenceIdentificationQualifier",
                               "2": "ReferenceIdentification"
                           },
                           "k3": {
                               "0": "ClaimInformation",
                               "1": "FixedFormatInformation"
                           },
                           "hi": {
                               "0": "HealthCareDiagnosisCode",
                               "1": "CodeListQualifierCode",
                               "2": "IndustryCode"
                           },
                           "sbr": {
                               "0": "SubscriberInformation",
                               "1": "PayerResponsibilityCode",
                               "2": "IndividualRelationshipCode",
                               "3": "ReferenceIdentification",
                               "4": "Name",
                               "5": "InsuranceTypeCode",
                               "6": "CoordinationOfBenefitCode",
                               "7": "YesNoCondition",
                               "8": "EmploymentStatusCode",
                               "9": "ClaimFillingIndicatorCode"
                           },
                           "lx": {
                               "0": "ServiceLine",
                               "1": "AssignedNumber"
                           },
                           "sv1": {
                               "0": "ProfessionalService",
                               "1": "ProductServiceIdQualifier : ProductServiceID : ProcedureModifier : ProcedureModifier : ProcedureModifier : ProcedureModifier",
                               "2": "MonetaryAmount",
                               "3": "Unit",
                               "4": "Quantity",
                               "5": "FacilityCodeValue",
                               "6": "ServiceTypeCode",
                               "7": "DiagnosisCodePointer : DiagnosisCodePointer : DiagnosisCodePointer : DiagnosisCodePointer : MonetaryAmount : YesNoEmergencyIndicator: MultipleProcedureCode : YesNoEPSDTIndicator : YesNoFamilyPlanningIndicator : ReviewCode : NationalOrLocalAssignedReviewValue : CopayStatusCode"
                           },
                           "svd": {
                               "0": "LineAdjudicationInformation",
                               "1": "IdentificationCode",
                               "2": "MonetaryAmount",
                               "3": "ProductServiceIDQualifier",
                               "4": "Description",
                               "5": "Quantity"
                           },
                           "cas": {
                               "0": "LineAdjustment",
                               "1": "ClaimAdjustmentGroupCode",
                               "2": "ClaimAdjustmentReasonCode",
                               "3": "MonetaryAmount"
                           },
                           "trailer_3": {"after": "/Segment"},
                           "se": {
                               "0": [
                                   "TransactionSetTrailer",
                                   "TransactionSetHeader"
                               ],
                               "1": "NumberofIncludedSegments",
                               "2": "TransactionSetControlNumber"
                           },
                           "trailer_2": {"after": "/Transaction"},
                           "ge": {
                               "0": [
                                   "FunctionalGroupTrailer",
                                   "FunctionalGroupHeader"
                               ],
                               "1": "NumberOfTransactionsSetsIncluded",
                               "2": "GroupControlNumber"
                           },
                           "trailer_1": {"after": "/Group"},
                           "iea": {
                               "0": "InterchangeControlTrailer",
                               "1": "NumberOfIncludedFunctionalGroups",
                               "2": "InterchangeControlNumber"
                           },
                           "trailer_0": {"after": "/Hippa"}
                       },
                       }],
    "delimiter": "*",
    "content_separator": ":",
    "output_format": ".xml"
}

post1 = {
    "name": "PurchaseOrder",
    "active_template": "PurchaseOrderTemplate",
    "active_version": "v1",
    "templates": [{"name": "retail",
                   "version":"v1",
                   "config": {
                       "header_0": {"before": "UNB"},
                       "bgm": {
                           "2": "PO_NUMBER"
                       },
                       "dtm": {
                           "1": " : PO_DATE : "
                       },
                       "nad": {
                           "2": "CUSTOMER_NUMBER : : ",
                           "4": "CUSTOMER_NAME",
                           "5": "ADDRESS",
                           "6": "CITY",
                           "7": "STATE",
                           "8": "POSTAL_CODE"
                       },
                       "lin": {
                           "1": "LINE_NUMBER",
                           "3": "UPC_NUMBER"
                       },
                       "qty": {
                           "1": " : QUANTITY : UOM"
                       },
                       "pri": {
                           "1": " : PRICE"
                       },
                       "trailer_0": {"after": "/UNB"}}
                   }],
    "delimiter": "+",
    "content_separator": ":",
    "output_format": ".csv"
}

db.agents.save(post1)
