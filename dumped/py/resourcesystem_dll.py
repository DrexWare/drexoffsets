# dumped by shxdows dumper (csdump)

from enum import Enum

class FuseVariableAccess_t(Enum):
    READ_ONLY = 1
    WRITABLE = 0

class FuseVariableType_t(Enum):
    BOOL = 1
    FLOAT32 = 8
    INT16 = 3
    INT32 = 4
    INT8 = 2
    INVALID = 0
    UINT16 = 6
    UINT32 = 7
    UINT8 = 5

class AABB_t:
    m_vMaxBounds = 12  # offset
    m_vMinBounds = 0  # offset

class CFuseProgram:
    m_nMaxTempVarsUsed = 72  # offset
    m_programBuffer = 0  # offset
    m_variablesRead = 24  # offset
    m_variablesWritten = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFuseSymbolTable:
    m_constantMap = 72  # offset
    m_constants = 0  # offset
    m_functionMap = 136  # offset
    m_functions = 48  # offset
    m_variableMap = 104  # offset
    m_variables = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ConstantInfo_t:
    m_flValue = 12  # offset
    m_name = 0  # offset
    m_nameToken = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FourQuaternions:
    w = 48  # offset
    x = 0  # offset
    y = 16  # offset
    z = 32  # offset

class FunctionInfo_t:
    m_bIsPure = 26  # offset
    m_nIndex = 24  # offset
    m_nParamCount = 20  # offset
    m_name = 8  # offset
    m_nameToken = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FuseFunctionIndex_t:
    m_Value = 0  # offset

class FuseVariableIndex_t:
    m_Value = 0  # offset

class InfoForResourceTypeCAnimData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCAnimationGroup:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCCSGOEconItem:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCChoreoSceneFileData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCCompositeMaterialKit:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCDOTANovelsList:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCDOTAPatchNotesList:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCDotaItemDefinitionResource:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCEntityLump:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCGcExportableExternalData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCJavaScriptResource:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCModel:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCMorphSetData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCNmClip:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCNmGraphDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCNmIKRig:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCNmSkeleton:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCPanoramaDynamicImages:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCPanoramaLayout:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCPanoramaStyle:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCPhysAggregateData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCPostProcessingResource:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCRenderMesh:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCResponseRulesList:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCSequenceGroupData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCSmartProp:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCSurfaceGraph:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCTestResourceData:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCTextureBase:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCTypeScriptResource:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVDataResource:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVMixListResource:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVPhysXSurfacePropertiesList:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVSoundEventScriptList:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVSoundStackScriptList:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVoiceContainerBase:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCVoxelVisibility:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeCWorldNode:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeIAnimGraphModelBinding:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeIMaterial2:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeIParticleSnapshot:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeIParticleSystemDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeIPulseGraphDef:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeIVectorGraphic:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeManifestTestResource_t:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeProceduralTestResource_t:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeWorld_t:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class ManifestTestResource_t:
    m_child = 8  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PackedAABB_t:
    m_nPackedMax = 4  # offset
    m_nPackedMin = 0  # offset

class VariableInfo_t:
    m_eAccess = 16  # offset
    m_eVarType = 15  # offset
    m_nIndex = 12  # offset
    m_nNumComponents = 14  # offset
    m_name = 0  # offset
    m_nameToken = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]