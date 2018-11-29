# DB connection
# read tamplate

from pymongo import MongoClient
import json
import re
from os import listdir
from os.path import isfile, join

template = """{
  "delimiter": "*",
  "header_0": {
    "before": "Hippa"
  },
  "isa": {
    "0": "InterchangeControlHeader2",
    "4": "SecurityInformation",
    "5": "InterchangeIdQualifier",
    "7": "InterchangeIdQualifier",
    "10": "RepetitionSeparator",
    "11": "InterchangeTime",
    "12": "InterchangeControlVersionNumber",
    "13": "InterchangeControlNumber",
    "15": "UsageIndicator",
    "16": "ComponentElementSeparator"
  },
  "header_1": {
    "before": "Group"
  },
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
  "header_2": {
    "before": "Transaction"
  },
  "st": {
    "0": "TransactionSetHeader",
    "1": "TransactionSetIdentifier",
    "2": "TransactionSetControlNumber",
    "3": "ImplementationConventionReference"
  },
  "header_3": {
    "before": "Segment"
  },
  "bht": {
    "0": "BeginningOfHierarchicalSegment",
    "1": "HierarchicalStructureCode",
    "2": "TransactionSetPurposeCode",
    "3": "ReferenceIdentification",
    "4": "Date",
    "5": "InterchangeIdQualifier",
    "6": "TransactionTypeCode"
  },
  "nm1": {
    "1": "EntityIdentifierCode",
    "2": "EntityTypeQualifier",
    "4": "NameFirst",
    "5": "NameMiddle",
    "6": "NamePrefix",
    "7": "NameSuffix",
    "8": "IdentificationCodeQualifier",
    "9": "IdentificationCode",
    "0": ["ReceiverName", "BillingProviderName", "SubscriberName", "PayerName", "ReferringProviderName", "RenderingProviderName", "ServiceFacilityLocation", "OtherSubscriberName", "OtherPayerName"],
    "3": ["NameLast", "OrganizationName"]
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
    "2": "HierarchicalParentIdNumber",
    "3": "HierarchicalLevelCode",
    "4": "HierarchicalChildCode",
    "0": ["BillingHierarchicalLevel", "SubscriberHierarchicalLevel", "PatientHierarchicalLevel"],
    "1" :["HierarchicalIdNumber", "SubscriberIDNumber"]
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
    "1": "DateTimeQualifier",
    "2": "DateTimePeriodFormatQualifier",
    "3": "DateTimePeriod",
    "0": ["DateOnsetOfCurrentIllnessSymptom", "DateInitialTreatment", "DateLastSeen", "DateAcuteManifestation", "DateAccident", "DateInitialMenstrual", "DateLastXRayMenstrual", "DateHearingAndVisionPrescriptionDate", "DateLastWorked"]
  },
  "ref": {
    "1": "ReferenceIdentificationQualifier",
    "2": "ReferenceIdentification",
    "0_0": "CLIANumber",
    "0_1": "PriorAuthorizationOrReferralNumber"
  },
  "k3": {
    "0": "ClaimInformation",
    "1": "FixedFormatInformation"
  },
  "hi": {
    "0": "HealthCareDiagnosisCode",
    "1": "CodeListQualifierCode : CodeNumber",
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
    "7": "DiagnosisCodePointer : DiagnosisCodePointer : DiagnosisCodePointer : DiagnosisCodePointer : MonetaryAmount : YesNoEmergency Indicator: MultipleProcedureCode : YesNoEPSDTIndicator : YesNoFamilyPlanningIndicator : ReviewCode : NationalOrLocalAssignedReviewValue : CopayStatusCode"
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
  "trailer_3": {
    "after": "/Segment"
  },
  "se": {
    "0": "TransactionSetTrailer",
    "1": "NumberofIncludedSegments",
    "2": "TransactionSetControlNumber"
  },
  "trailer_2": {
    "after": "/Transaction"
  },
  "ge": {
    "1": "NumberOfTransactionsSetsIncluded",
    "2": "GroupControlNumber",
    "0": ["FunctionalGroupTrailer", "FunctionalGroupHeader"]
  },
  "trailer_1": {
    "after": "/Group"
  },
  "iea": {
    "0": "InterchangeControlTrailer",
    "1": "NumberOfIncludedFunctionalGroups",
    "2": "InterchangeControlNumber20"
  },
  "trailer_0": {
    "after": "/Hippa"
  }
}"""

def get_header_or_trailer(header_trailer):
    return header_trailer[1][:-1].strip().replace("\'", "")


mypath = "./unprocessed_files"

fileNames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
template_map = json.loads(template)
delimiter = template_map["delimiter"]
number_of_failed_file = 0
for file in fileNames:
    outputXml = ""
    fields = []
    path = "C:/Users/Raman/Desktop/parser/unprocessed_files/"
    after = ""

    with open(path + file) as f:
        is_processed = True
        text = f.read().replace("~", "")
        lines = text.split("\n")
        for line in lines:
            fields += [(line.split(delimiter))]
        nmc = 0
        ces_delimiter = str(fields[0][-1])
        is_end = True
        for field in fields:
            try:
                input_header = str(field[0]).lower()
                template_value = template_map[input_header]
                rowFields = json.loads(str(template_value).replace("\'", "\""))
                template_keys = list(template_map.keys())
                header_idx_value = str(template_keys[template_keys.index(input_header) - 1])
                trailer_idx_value_f = str(template_keys[template_keys.index(input_header) + 1])
                trailer_idx_value_p = str(template_keys[template_keys.index(input_header) - 1])

                if re.match("header_", header_idx_value):
                    header_value = str(template_map[header_idx_value]).split(":")
                    header = get_header_or_trailer(header_value)
                    outputXml += "<" + header + ">" + "\n"
                    is_end = True

                if re.match("trailer_", trailer_idx_value_p) and is_end:
                    trailer_value_p = str(template_map[trailer_idx_value_p]).split(":")
                    trailer_p = get_header_or_trailer(trailer_value_p)
                    outputXml += "<" + trailer_p + ">" + "\n"
                    is_end = False

                if re.match("trailer_", trailer_idx_value_f) and not is_end and template_keys.index(
                        input_header) != len(template_map) - 2:
                    trailer_value_f = str(template_map[trailer_idx_value_f]).split(":")
                    trailer_f = get_header_or_trailer(trailer_value_f)
                    outputXml += "<" + trailer_f + ">" + "\n"
                else:
                    trailer_value_f = str(template_map[trailer_idx_value_f]).split(":")
                    trailer_f = get_header_or_trailer(trailer_value_f)
                    after = "<" + trailer_f + ">"

                for rowK, rowV in rowFields.items():
                    if str(rowK).isdigit() and len(re.split(r",", str(rowV))) > 1 or \
                            len(re.split(ces_delimiter, str(rowV))) > 1:
                        lenOfPossibleValues = nmc % len(rowV)
                        if (len(str(rowV).split(ces_delimiter))) > 1:
                            ces_value = list(
                                zip(list(field[int(rowK)].split(ces_delimiter)),
                                    str(rowV).split(ces_delimiter)))
                            for elem in ces_value:
                                if elem[1] != " ":
                                    outputXml += "<" + elem[1].strip() + ">" + elem[0] + "</" + elem[
                                        1].strip() + ">\n"
                        else:
                            outputXml += "<" + list(rowV)[lenOfPossibleValues] + ">" + field[int(rowK)] \
                                         + "</" + list(rowV)[lenOfPossibleValues] + ">\n"
                        nmc += 1
                    else:
                        if str(rowK).isdigit():
                            keyNumber = int(str(rowK))
                            valueIdx = 0
                            if keyNumber >= len(field):
                                valueIdx = keyNumber % len(field)
                            else:
                                valueIdx = int(rowK)
                            outputXml += "<" + rowFields[rowK] + ">" + field[valueIdx] + "</" + rowFields[rowK] + ">\n"

            except Exception as e:
                number_of_failed_file += 1
                failed_file = open("C:/Users/Raman/Desktop/parser/failed_files/" + file, "w")
                msg = "file unprocessed : {}".format(file)
                failed_file.write(str(msg))

        outputXml += after
        output_file = open(
            "C:/Users/Raman/Desktop/parser/processed_files/" + file.replace(".txt", "") + ".xml", "w")
        output_file.write(outputXml)
        print("file Processed {}".format(file))
print("number of failed files : {}".format(number_of_failed_file))
