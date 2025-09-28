// dumped by shxdows dumper (csdump)
# dumped by shxdows dumper (csdump) 

from enum import Enum

class CompMatPropertyMutatorConditionType_t(Enum):
    COMP_MAT_MUTATOR_CONDITION_INPUT_CONTAINER_EXISTS = 0
    COMP_MAT_MUTATOR_CONDITION_INPUT_CONTAINER_VALUE_EQUALS = 2
    COMP_MAT_MUTATOR_CONDITION_INPUT_CONTAINER_VALUE_EXISTS = 1

class CompMatPropertyMutatorType_t(Enum):
    COMP_MAT_PROPERTY_MUTATOR_CONDITIONAL_MUTATORS = 6
    COMP_MAT_PROPERTY_MUTATOR_COPY_KEYS_WITH_SUFFIX = 2
    COMP_MAT_PROPERTY_MUTATOR_COPY_MATCHING_KEYS = 1
    COMP_MAT_PROPERTY_MUTATOR_COPY_PROPERTY = 3
    COMP_MAT_PROPERTY_MUTATOR_DRAW_TEXT = 8
    COMP_MAT_PROPERTY_MUTATOR_GENERATE_TEXTURE = 5
    COMP_MAT_PROPERTY_MUTATOR_INIT = 0
    COMP_MAT_PROPERTY_MUTATOR_POP_INPUT_QUEUE = 7
    COMP_MAT_PROPERTY_MUTATOR_RANDOM_ROLL_INPUT_VARIABLES = 9
    COMP_MAT_PROPERTY_MUTATOR_SET_VALUE = 4

class CompositeMaterialInputContainerSourceType_t(Enum):
    CONTAINER_SOURCE_TYPE_LOOSE_VARIABLES = 3
    CONTAINER_SOURCE_TYPE_MATERIAL_FROM_TARGET_ATTR = 1
    CONTAINER_SOURCE_TYPE_SPECIFIC_MATERIAL = 2
    CONTAINER_SOURCE_TYPE_TARGET_INSTANCE_MATERIAL = 5
    CONTAINER_SOURCE_TYPE_TARGET_MATERIAL = 0
    CONTAINER_SOURCE_TYPE_VARIABLE_FROM_TARGET_ATTR = 4

class CompositeMaterialInputLooseVariableType_t(Enum):
    LOOSE_VARIABLE_TYPE_BOOLEAN = 0
    LOOSE_VARIABLE_TYPE_COLOR4 = 9
    LOOSE_VARIABLE_TYPE_FLOAT1 = 5
    LOOSE_VARIABLE_TYPE_FLOAT2 = 6
    LOOSE_VARIABLE_TYPE_FLOAT3 = 7
    LOOSE_VARIABLE_TYPE_FLOAT4 = 8
    LOOSE_VARIABLE_TYPE_INTEGER1 = 1
    LOOSE_VARIABLE_TYPE_INTEGER2 = 2
    LOOSE_VARIABLE_TYPE_INTEGER3 = 3
    LOOSE_VARIABLE_TYPE_INTEGER4 = 4
    LOOSE_VARIABLE_TYPE_PANORAMA_RENDER = 14
    LOOSE_VARIABLE_TYPE_RESOURCE_MATERIAL = 12
    LOOSE_VARIABLE_TYPE_RESOURCE_TEXTURE = 13
    LOOSE_VARIABLE_TYPE_STRING = 10
    LOOSE_VARIABLE_TYPE_SYSTEMVAR = 11

class CompositeMaterialInputTextureType_t(Enum):
    INPUT_TEXTURE_TYPE_AO = 6
    INPUT_TEXTURE_TYPE_COLOR = 2
    INPUT_TEXTURE_TYPE_DEFAULT = 0
    INPUT_TEXTURE_TYPE_MASKS = 3
    INPUT_TEXTURE_TYPE_NORMALMAP = 1
    INPUT_TEXTURE_TYPE_PEARLESCENCE_MASK = 5
    INPUT_TEXTURE_TYPE_POSITION = 7
    INPUT_TEXTURE_TYPE_ROUGHNESS = 4

class CompositeMaterialMatchFilterType_t(Enum):
    MATCH_FILTER_MATERIAL_ATTRIBUTE_EQUALS = 3
    MATCH_FILTER_MATERIAL_ATTRIBUTE_EXISTS = 0
    MATCH_FILTER_MATERIAL_NAME_SUBSTR = 2
    MATCH_FILTER_MATERIAL_PROPERTY_EQUALS = 5
    MATCH_FILTER_MATERIAL_PROPERTY_EXISTS = 4
    MATCH_FILTER_MATERIAL_SHADER = 1

class CompositeMaterialVarSystemVar_t(Enum):
    COMPMATSYSVAR_COMPOSITETIME = 0
    COMPMATSYSVAR_EMPTY_RESOURCE_SPACER = 1

class InventoryNodeType_t(Enum):
    CONCRETE_NODE_SCHEMA_ITEMDEF = 6
    CONCRETE_NODE_SCHEMA_KEYCHAIN = 8
    CONCRETE_NODE_SCHEMA_PREFAB = 5
    CONCRETE_NODE_SCHEMA_STICKER = 7
    NODE_TYPE_INVALID = 0
    VIRTUAL_NODE_SCHEMA_ITEMDEF = 2
    VIRTUAL_NODE_SCHEMA_KEYCHAIN = 4
    VIRTUAL_NODE_SCHEMA_PREFAB = 1
    VIRTUAL_NODE_SCHEMA_STICKER = 3

class ActiveModelConfig_t:
    m_AssociatedEntities = 64  # offset
    m_AssociatedEntityNames = 88  # offset
    m_Handle = 48  # offset
    m_Name = 56  # offset

    __metadata__ =     [
        {
            "name": "m_Handle",
            "type": "NetworkVarNames",
            "type_name": "ModelConfigHandle_t"
        },
        {
            "name": "m_Name",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_AssociatedEntities",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseModelEntity>"
        },
        {
            "name": "m_AssociatedEntityNames",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class CAnimGraphNetworkedVariables:
    m_OwnerOnlyPredNetBoolVariables = 248  # offset
    m_OwnerOnlyPredNetByteVariables = 272  # offset
    m_OwnerOnlyPredNetFloatVariables = 392  # offset
    m_OwnerOnlyPredNetGlobalSymbolVariables = 464  # offset
    m_OwnerOnlyPredNetIntVariables = 320  # offset
    m_OwnerOnlyPredNetQuaternionVariables = 440  # offset
    m_OwnerOnlyPredNetUInt16Variables = 296  # offset
    m_OwnerOnlyPredNetUInt32Variables = 344  # offset
    m_OwnerOnlyPredNetUInt64Variables = 368  # offset
    m_OwnerOnlyPredNetVectorVariables = 416  # offset
    m_PredNetBoolVariables = 8  # offset
    m_PredNetByteVariables = 32  # offset
    m_PredNetFloatVariables = 152  # offset
    m_PredNetGlobalSymbolVariables = 224  # offset
    m_PredNetIntVariables = 80  # offset
    m_PredNetQuaternionVariables = 200  # offset
    m_PredNetUInt16Variables = 56  # offset
    m_PredNetUInt32Variables = 104  # offset
    m_PredNetUInt64Variables = 128  # offset
    m_PredNetVectorVariables = 176  # offset
    m_flLastTeleportTime = 500  # offset
    m_nBoolVariablesCount = 488  # offset
    m_nOwnerOnlyBoolVariablesCount = 492  # offset
    m_nRandomSeedOffset = 496  # offset

    __metadata__ =     [
        {
            "name": "m_PredNetBoolVariables",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_PredNetByteVariables",
            "type": "NetworkVarNames",
            "type_name": "byte"
        },
        {
            "name": "m_PredNetUInt16Variables",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_PredNetIntVariables",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_PredNetUInt32Variables",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_PredNetUInt64Variables",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_PredNetFloatVariables",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_PredNetVectorVariables",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_PredNetQuaternionVariables",
            "type": "NetworkVarNames",
            "type_name": "Quaternion"
        },
        {
            "name": "m_PredNetGlobalSymbolVariables",
            "type": "NetworkVarNames",
            "type_name": "CGlobalSymbol"
        },
        {
            "name": "m_OwnerOnlyPredNetBoolVariables",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_OwnerOnlyPredNetByteVariables",
            "type": "NetworkVarNames",
            "type_name": "byte"
        },
        {
            "name": "m_OwnerOnlyPredNetUInt16Variables",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_OwnerOnlyPredNetIntVariables",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_OwnerOnlyPredNetUInt32Variables",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_OwnerOnlyPredNetUInt64Variables",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_OwnerOnlyPredNetFloatVariables",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_OwnerOnlyPredNetVectorVariables",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_OwnerOnlyPredNetQuaternionVariables",
            "type": "NetworkVarNames",
            "type_name": "Quaternion"
        },
        {
            "name": "m_OwnerOnlyPredNetGlobalSymbolVariables",
            "type": "NetworkVarNames",
            "type_name": "CGlobalSymbol"
        },
        {
            "name": "m_nBoolVariablesCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nOwnerOnlyBoolVariablesCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nRandomSeedOffset",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flLastTeleportTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CAttributeList:
    m_Attributes = 8  # offset
    m_pManager = 112  # offset

    __metadata__ =     [
        {
            "name": "m_Attributes",
            "type": "NetworkVarNames",
            "type_name": "CEconItemAttribute"
        }
    ]

class CAttributeManager:
    m_CachedResults = 48  # offset
    m_ProviderType = 44  # offset
    m_Providers = 8  # offset
    m_bPreventLoopback = 40  # offset
    m_hOuter = 36  # offset
    m_iReapplyProvisionParity = 32  # offset

    __metadata__ =     [
        {
            "name": "m_iReapplyProvisionParity",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_hOuter",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        },
        {
            "name": "m_ProviderType",
            "type": "NetworkVarNames",
            "type_name": "attributeprovidertypes_t"
        }
    ]

class CAttributeManager__cached_attribute_float_t:
    flIn = 0  # offset
    flOut = 16  # offset
    iAttribHook = 8  # offset

class CBaseAnimGraph(C_BaseModelEntity):
    m_RagdollPose = 4000  # offset
    m_bAnimGraphUpdateEnabled = 3928  # offset
    m_bAnimationUpdateScheduled = 3948  # offset
    m_bBuiltRagdoll = 3976  # offset
    m_bHasAnimatedMaterialAttributes = 4088  # offset
    m_bInitiallyPopulateInterpHistory = 3912  # offset
    m_bRagdollClientSide = 4073  # offset
    m_bRagdollEnabled = 4072  # offset
    m_bSuppressAnimEventSounds = 3914  # offset
    m_flMaxSlopeDistance = 3932  # offset
    m_nForceBone = 3964  # offset
    m_pClientsideRagdoll = 3968  # offset
    m_vLastSlopeCheckPos = 3936  # offset
    m_vecForce = 3952  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_bInitiallyPopulateInterpHistory",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bAnimGraphUpdateEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vecForce",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nForceBone",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_RagdollPose",
            "type": "NetworkVarNames",
            "type_name": "PhysicsRagdollPose_t"
        },
        {
            "name": "m_bRagdollEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bRagdollClientSide",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CBaseAnimGraphController(CSkeletonAnimationController):
    m_animGraphNetworkedVars = 24  # offset
    m_bIsUsingAG2 = 6248  # offset
    m_bLastUpdateSkipped = 5332  # offset
    m_bNetworkedAnimationInputsChanged = 5330  # offset
    m_bNetworkedSequenceChanged = 5331  # offset
    m_bSequenceFinished = 5288  # offset
    m_flPlaybackRate = 5316  # offset
    m_flPrevAnimUpdateTime = 5336  # offset
    m_flSeqFixedCycle = 5308  # offset
    m_flSeqStartTime = 5304  # offset
    m_flSoundSyncTime = 5292  # offset
    m_hGraphDefinitionAG2 = 6240  # offset
    m_hSequence = 5300  # offset
    m_nActiveIKChainMask = 5296  # offset
    m_nAnimLoopMode = 5312  # offset
    m_nGraphCreationFlagsAG2 = 6288  # offset
    m_nNotifyState = 5328  # offset
    m_nSerializePoseRecipeSizeAG2 = 6280  # offset
    m_nSerializePoseRecipeVersionAG2 = 6284  # offset
    m_nServerGraphDefReloadCountAG2 = 6356  # offset
    m_serializedPoseRecipeAG2 = 6256  # offset

    __metadata__ =     [
        {
            "name": "m_animGraphNetworkedVars",
            "type": "NetworkVarNames",
            "type_name": "CAnimGraphNetworkedVariables"
        },
        {
            "name": "m_hSequence",
            "type": "NetworkVarNames",
            "type_name": "HSequence"
        },
        {
            "name": "m_flSeqStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flSeqFixedCycle",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nAnimLoopMode",
            "type": "NetworkVarNames",
            "type_name": "AnimLoopMode_t"
        },
        {
            "name": "m_hGraphDefinitionAG2",
            "type": "NetworkVarNames",
            "type_name": "HNmGraphDefinitionStrong"
        },
        {
            "name": "m_bIsUsingAG2",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_serializedPoseRecipeAG2",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nSerializePoseRecipeSizeAG2",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nSerializePoseRecipeVersionAG2",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nGraphCreationFlagsAG2",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nServerGraphDefReloadCountAG2",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class CBaseFilter(CLogicalEntity):
    m_OnFail = 1576  # offset
    m_OnPass = 1536  # offset
    m_bNegated = 1528  # offset

class CBasePlayerController(C_BaseEntity):
    m_CommandContext = 1536  # offset
    m_bIsHLTV = 1760  # offset
    m_bIsLocalPlayerController = 1912  # offset
    m_bKnownTeamMismatch = 1720  # offset
    m_bNoClipEnabled = 1913  # offset
    m_hPawn = 1716  # offset
    m_hPredictedPawn = 1724  # offset
    m_hSplitOwner = 1732  # offset
    m_hSplitScreenPlayers = 1736  # offset
    m_iConnected = 1764  # offset
    m_iDesiredFOV = 1916  # offset
    m_iszPlayerName = 1768  # offset
    m_nInButtonsWhichAreToggles = 1704  # offset
    m_nSplitScreenSlot = 1728  # offset
    m_nTickBase = 1712  # offset
    m_steamID = 1904  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "m_nTickBase",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_hPawn",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerPawn>"
        },
        {
            "name": "m_bKnownTeamMismatch",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iConnected",
            "type": "NetworkVarNames",
            "type_name": "PlayerConnectedState"
        },
        {
            "name": "m_iszPlayerName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_steamID",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_bNoClipEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iDesiredFOV",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "MNetworkReplayCompatField",
            "type": "Unknown"
        }
    ]

class CBasePlayerControllerAPI:
    pass

class CBasePlayerVData:
    m_flArmDamageMultiplier = 312  # offset
    m_flChestDamageMultiplier = 280  # offset
    m_flCrouchTime = 372  # offset
    m_flDrowningDamageInterval = 348  # offset
    m_flHeadDamageMultiplier = 264  # offset
    m_flHoldBreathTime = 344  # offset
    m_flLegDamageMultiplier = 328  # offset
    m_flStomachDamageMultiplier = 296  # offset
    m_flUseAngleTolerance = 368  # offset
    m_flUseRange = 364  # offset
    m_nDrowningDamageInitial = 352  # offset
    m_nDrowningDamageMax = 356  # offset
    m_nWaterSpeed = 360  # offset
    m_sModelName = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBasePlayerWeaponVData:
    m_aShootSounds = 1048  # offset
    m_bAllowFlipping = 489  # offset
    m_bAutoSwitchFrom = 1025  # offset
    m_bAutoSwitchTo = 1024  # offset
    m_bBuiltRightHanded = 488  # offset
    m_bLinkedCooldowns = 996  # offset
    m_bReserveAmmoAsClips = 1016  # offset
    m_bTreatAsSingleClip = 1017  # offset
    m_flDropSpeed = 1032  # offset
    m_flMuzzleSmokeDecrementRate = 992  # offset
    m_flMuzzleSmokeTimeout = 988  # offset
    m_iDefaultClip1 = 1008  # offset
    m_iDefaultClip2 = 1012  # offset
    m_iFlags = 997  # offset
    m_iMaxClip1 = 1000  # offset
    m_iMaxClip2 = 1004  # offset
    m_iPosition = 1040  # offset
    m_iRumbleEffect = 1028  # offset
    m_iSlot = 1036  # offset
    m_iWeight = 1020  # offset
    m_nMuzzleSmokeShotThreshold = 984  # offset
    m_nPrimaryAmmoType = 998  # offset
    m_nSecondaryAmmoType = 999  # offset
    m_sMuzzleAttachment = 496  # offset
    m_sToolsOnlyOwnerModelName = 264  # offset
    m_szBarrelSmokeParticle = 760  # offset
    m_szMuzzleFlashParticle = 528  # offset
    m_szMuzzleFlashParticleConfig = 752  # offset
    m_szWorldModel = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBaseProp(CBaseAnimGraph):
    m_bConformToCollisionBounds = 4472  # offset
    m_bModelOverrodeBlockLOS = 4464  # offset
    m_iShapeType = 4468  # offset
    m_mPreferredCatchTransform = 4480  # offset

class CBasePulseGraphInstance:
    pass

class CBaseTriggerAPI:
    pass

class CBodyComponent(CEntityComponent):
    __m_pChainEntity = 72  # offset
    m_pSceneNode = 8  # offset

class CBodyComponentBaseAnimGraph(CBodyComponentSkeletonInstance):
    m_animationController = 1456  # offset

    __metadata__ =     [
        {
            "name": "m_animationController",
            "type": "NetworkVarNames",
            "type_name": "CBaseAnimGraphController"
        }
    ]

class CBodyComponentBaseModelEntity(CBodyComponentSkeletonInstance):
    pass

class CBodyComponentPoint(CBodyComponent):
    m_sceneNode = 128  # offset

    __metadata__ =     [
        {
            "name": "m_sceneNode",
            "type": "NetworkVarNames",
            "type_name": "CGameSceneNode"
        }
    ]

class CBodyComponentSkeletonInstance(CBodyComponent):
    m_skeletonInstance = 128  # offset

    __metadata__ =     [
        {
            "name": "m_skeletonInstance",
            "type": "NetworkVarNames",
            "type_name": "CSkeletonInstance"
        }
    ]

class CBombTarget(C_BaseTrigger):
    m_bBombPlantedHere = 4104  # offset

    __metadata__ =     [
        {
            "name": "m_bBombPlantedHere",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CBuoyancyHelper:
    m_bNeutrallyBuoyant = 44  # offset
    m_flFluidDensity = 28  # offset
    m_flNeutrallyBuoyantAngularDamping = 40  # offset
    m_flNeutrallyBuoyantGravity = 32  # offset
    m_flNeutrallyBuoyantLinearDamping = 36  # offset
    m_nFluidType = 24  # offset
    m_vecFractionOfWheelSubmergedForWheelDrag = 96  # offset
    m_vecFractionOfWheelSubmergedForWheelFriction = 48  # offset
    m_vecWheelDrag = 120  # offset
    m_vecWheelFrictionScales = 72  # offset

class CCSGO_WingmanIntroCharacterPosition(C_CSGO_TeamIntroCharacterPosition):
    pass

class CCSGO_WingmanIntroCounterTerroristPosition(CCSGO_WingmanIntroCharacterPosition):
    pass

class CCSGO_WingmanIntroTerroristPosition(CCSGO_WingmanIntroCharacterPosition):
    pass

class CCSGameModeRules:
    __m_pChainEntity = 8  # offset

class CCSGameModeRules_ArmsRace:
    m_WeaponSequence = 48  # offset

    __metadata__ =     [
        {
            "name": "m_WeaponSequence",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        }
    ]

class CCSGameModeRules_Deathmatch:
    m_flDMBonusStartTime = 48  # offset
    m_flDMBonusTimeLength = 52  # offset
    m_sDMBonusWeapon = 56  # offset

    __metadata__ =     [
        {
            "name": "m_flDMBonusStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flDMBonusTimeLength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_sDMBonusWeapon",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        }
    ]

class CCSGameModeRules_Noop:
    pass

class CCSObserver_CameraServices(CCSPlayerBase_CameraServices):
    pass

class CCSObserver_MovementServices(CPlayer_MovementServices):
    pass

class CCSObserver_ObserverServices(CPlayer_ObserverServices):
    m_obsInterpState = 92  # offset

class CCSObserver_UseServices(CPlayer_UseServices):
    pass

class CCSPlayerBase_CameraServices(CPlayer_CameraServices):
    m_flFOVRate = 660  # offset
    m_flFOVTime = 656  # offset
    m_flLastShotFOV = 668  # offset
    m_hZoomOwner = 664  # offset
    m_iFOV = 648  # offset
    m_iFOVStart = 652  # offset

    __metadata__ =     [
        {
            "name": "m_iFOV",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iFOVStart",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_flFOVTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flFOVRate",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_hZoomOwner",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        }
    ]

class CCSPlayerController(CBasePlayerController):
    m_bAbandonAllowsSurrender = 2266  # offset
    m_bAbandonOffersInstantSurrender = 2267  # offset
    m_bCanControlObservedBot = 2296  # offset
    m_bCannotBeKicked = 2264  # offset
    m_bControllingBot = 2288  # offset
    m_bDisconnection1MinWarningPrinted = 2268  # offset
    m_bEverFullyConnected = 2265  # offset
    m_bEverPlayedOnTeam = 2108  # offset
    m_bFireBulletsSeedSynchronized = 2373  # offset
    m_bHasBeenControlledByPlayerThisRound = 2290  # offset
    m_bHasCommunicationAbuseMute = 2076  # offset
    m_bHasControlledBotThisRound = 2289  # offset
    m_bIsPlayerNameDirty = 2372  # offset
    m_bMvpNoMusic = 2354  # offset
    m_bPawnHasDefuser = 2320  # offset
    m_bPawnHasHelmet = 2321  # offset
    m_bPawnIsAlive = 2308  # offset
    m_bScoreReported = 2269  # offset
    m_eMvpReason = 2356  # offset
    m_eNetworkDisconnectionReason = 2260  # offset
    m_flForceTeamTime = 2100  # offset
    m_flPreviousForceJoinTeamTime = 2112  # offset
    m_hObserverPawn = 2304  # offset
    m_hOriginalControllerOfCurrentPawn = 2336  # offset
    m_hPlayerPawn = 2300  # offset
    m_iCoachingTeam = 2136  # offset
    m_iCompTeammateColor = 2104  # offset
    m_iCompetitiveRankType = 2168  # offset
    m_iCompetitiveRanking = 2160  # offset
    m_iCompetitiveRankingPredicted_Loss = 2176  # offset
    m_iCompetitiveRankingPredicted_Tie = 2180  # offset
    m_iCompetitiveRankingPredicted_Win = 2172  # offset
    m_iCompetitiveWins = 2164  # offset
    m_iDraftIndex = 2248  # offset
    m_iMVPs = 2368  # offset
    m_iMusicKitID = 2360  # offset
    m_iMusicKitMVPs = 2364  # offset
    m_iPawnArmor = 2316  # offset
    m_iPawnBotDifficulty = 2332  # offset
    m_iPawnHealth = 2312  # offset
    m_iPawnLifetimeEnd = 2328  # offset
    m_iPawnLifetimeStart = 2324  # offset
    m_iPendingTeamNum = 2096  # offset
    m_iPing = 2072  # offset
    m_iScore = 2340  # offset
    m_msQueuedModeDisconnectionTimestamp = 2252  # offset
    m_nBotsControlledThisRound = 2292  # offset
    m_nDisconnectionTick = 2272  # offset
    m_nEndMatchNextMapVote = 2184  # offset
    m_nFirstKill = 2352  # offset
    m_nKillCount = 2353  # offset
    m_nPawnCharacterDefIndex = 2322  # offset
    m_nPlayerDominated = 2144  # offset
    m_nPlayerDominatingMe = 2152  # offset
    m_nQuestProgressReason = 2196  # offset
    m_pActionTrackingServices = 2056  # offset
    m_pDamageServices = 2064  # offset
    m_pInGameMoneyServices = 2040  # offset
    m_pInventoryServices = 2048  # offset
    m_recentKillQueue = 2344  # offset
    m_rtActiveMissionPeriod = 2192  # offset
    m_sSanitizedPlayerName = 2128  # offset
    m_szClan = 2120  # offset
    m_szCrosshairCodes = 2088  # offset
    m_uiAbandonRecordedReason = 2256  # offset
    m_uiCommunicationMuteFlags = 2080  # offset
    m_unActiveQuestId = 2188  # offset
    m_unPlayerTvControlFlags = 2200  # offset

    __metadata__ =     [
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "m_pInGameMoneyServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayerController_InGameMoneyServices*"
        },
        {
            "name": "m_pInventoryServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayerController_InventoryServices*"
        },
        {
            "name": "m_pActionTrackingServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayerController_ActionTrackingServices*"
        },
        {
            "name": "m_pDamageServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayerController_DamageServices*"
        },
        {
            "name": "m_iPing",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_bHasCommunicationAbuseMute",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_uiCommunicationMuteFlags",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_szCrosshairCodes",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iPendingTeamNum",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_flForceTeamTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_iCompTeammateColor",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bEverPlayedOnTeam",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_szClan",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iCoachingTeam",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPlayerDominated",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_nPlayerDominatingMe",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_iCompetitiveRanking",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iCompetitiveWins",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iCompetitiveRankType",
            "type": "NetworkVarNames",
            "type_name": "int8"
        },
        {
            "name": "m_iCompetitiveRankingPredicted_Win",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iCompetitiveRankingPredicted_Loss",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iCompetitiveRankingPredicted_Tie",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nEndMatchNextMapVote",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_unActiveQuestId",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_rtActiveMissionPeriod",
            "type": "NetworkVarNames",
            "type_name": "RTime32"
        },
        {
            "name": "m_nQuestProgressReason",
            "type": "NetworkVarNames",
            "type_name": "QuestProgress::Reason"
        },
        {
            "name": "m_unPlayerTvControlFlags",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nDisconnectionTick",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bControllingBot",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bHasControlledBotThisRound",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bCanControlObservedBot",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_hPlayerPawn",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_hObserverPawn",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSObserverPawn>"
        },
        {
            "name": "m_bPawnIsAlive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iPawnHealth",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iPawnArmor",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bPawnHasDefuser",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bPawnHasHelmet",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nPawnCharacterDefIndex",
            "type": "NetworkVarNames",
            "type_name": "item_definition_index_t"
        },
        {
            "name": "m_iPawnLifetimeStart",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iPawnLifetimeEnd",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iPawnBotDifficulty",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_hOriginalControllerOfCurrentPawn",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerController>"
        },
        {
            "name": "m_iScore",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_recentKillQueue",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nFirstKill",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nKillCount",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_bMvpNoMusic",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_eMvpReason",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMusicKitID",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMusicKitMVPs",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMVPs",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bFireBulletsSeedSynchronized",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CCSPlayerController_ActionTrackingServices(CPlayerControllerComponent):
    m_flTotalRoundDamageDealt = 304  # offset
    m_iNumRoundKills = 296  # offset
    m_iNumRoundKillsHeadshots = 300  # offset
    m_matchStats = 168  # offset
    m_perRoundStats = 64  # offset

    __metadata__ =     [
        {
            "name": "m_perRoundStats",
            "type": "NetworkVarNames",
            "type_name": "CSPerRoundStats_t"
        },
        {
            "name": "m_matchStats",
            "type": "NetworkVarNames",
            "type_name": "CSMatchStats_t"
        },
        {
            "name": "m_iNumRoundKills",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iNumRoundKillsHeadshots",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flTotalRoundDamageDealt",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CCSPlayerController_DamageServices(CPlayerControllerComponent):
    m_DamageList = 72  # offset
    m_nSendUpdate = 64  # offset

    __metadata__ =     [
        {
            "name": "m_nSendUpdate",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_DamageList",
            "type": "NetworkVarNames",
            "type_name": "CDamageRecord"
        },
        {
            "name": "MNetworkReplayCompatField",
            "type": "Unknown"
        }
    ]

class CCSPlayerController_InGameMoneyServices(CPlayerControllerComponent):
    m_iAccount = 64  # offset
    m_iCashSpentThisRound = 76  # offset
    m_iStartAccount = 68  # offset
    m_iTotalCashSpent = 72  # offset

    __metadata__ =     [
        {
            "name": "m_iAccount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iStartAccount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iTotalCashSpent",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iCashSpentThisRound",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class CCSPlayerController_InventoryServices(CPlayerControllerComponent):
    m_nPersonaDataPublicCommendsFriendly = 128  # offset
    m_nPersonaDataPublicCommendsLeader = 120  # offset
    m_nPersonaDataPublicCommendsTeacher = 124  # offset
    m_nPersonaDataPublicLevel = 116  # offset
    m_nPersonaDataXpTrailLevel = 132  # offset
    m_rank = 92  # offset
    m_unMusicID = 88  # offset
    m_vecNetworkableLoadout = 64  # offset
    m_vecServerAuthoritativeWeaponSlots = 136  # offset

    __metadata__ =     [
        {
            "name": "m_unMusicID",
            "type": "NetworkVarNames",
            "type_name": "item_definition_index_t"
        },
        {
            "name": "m_rank",
            "type": "NetworkVarNames",
            "type_name": "MedalRank_t"
        },
        {
            "name": "m_nPersonaDataPublicLevel",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPersonaDataPublicCommendsLeader",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPersonaDataPublicCommendsTeacher",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPersonaDataPublicCommendsFriendly",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPersonaDataXpTrailLevel",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vecServerAuthoritativeWeaponSlots",
            "type": "NetworkVarNames",
            "type_name": "ServerAuthoritativeWeaponSlot_t"
        }
    ]

class CCSPlayerController_InventoryServices__NetworkedLoadoutSlot_t:
    pItem = 0  # offset
    slot = 10  # offset
    team = 8  # offset

class CCSPlayer_ActionTrackingServices(CPlayerPawnComponent):
    m_bIsRescuing = 68  # offset
    m_hLastWeaponBeforeC4AutoSwitch = 64  # offset
    m_weaponPurchasesThisMatch = 72  # offset
    m_weaponPurchasesThisRound = 184  # offset

    __metadata__ =     [
        {
            "name": "m_bIsRescuing",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_weaponPurchasesThisMatch",
            "type": "NetworkVarNames",
            "type_name": "WeaponPurchaseTracker_t"
        },
        {
            "name": "m_weaponPurchasesThisRound",
            "type": "NetworkVarNames",
            "type_name": "WeaponPurchaseTracker_t"
        }
    ]

class CCSPlayer_BulletServices(CPlayerPawnComponent):
    m_totalHitsOnServer = 64  # offset

    __metadata__ =     [
        {
            "name": "m_totalHitsOnServer",
            "type": "NetworkVarNames",
            "type_name": "int32"
        }
    ]

class CCSPlayer_BuyServices(CPlayerPawnComponent):
    m_vecSellbackPurchaseEntries = 64  # offset

    __metadata__ =     [
        {
            "name": "m_vecSellbackPurchaseEntries",
            "type": "NetworkVarNames",
            "type_name": "SellbackPurchaseEntry_t"
        }
    ]

class CCSPlayer_CameraServices(CCSPlayerBase_CameraServices):
    m_flDeathCamTilt = 672  # offset
    m_vClientScopeInaccuracy = 680  # offset

class CCSPlayer_DamageReactServices(CPlayerPawnComponent):
    pass

class CCSPlayer_GlowServices(CPlayerPawnComponent):
    pass

class CCSPlayer_HostageServices(CPlayerPawnComponent):
    m_hCarriedHostage = 64  # offset
    m_hCarriedHostageProp = 68  # offset

    __metadata__ =     [
        {
            "name": "m_hCarriedHostage",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_hCarriedHostageProp",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        }
    ]

class CCSPlayer_ItemServices(CPlayer_ItemServices):
    m_bHasDefuser = 64  # offset
    m_bHasHelmet = 65  # offset

    __metadata__ =     [
        {
            "name": "m_bHasDefuser",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bHasHelmet",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CCSPlayer_MovementServices(CPlayer_MovementServices_Humanoid):
    m_StuckLast = 1228  # offset
    m_bDesiresDuck = 657  # offset
    m_bDuckOverride = 656  # offset
    m_bHasWalkMovedSinceLastJump = 697  # offset
    m_bInStuckTest = 698  # offset
    m_bOldJumpPressed = 1284  # offset
    m_bSpeedCropped = 1232  # offset
    m_bWasSurfing = 1340  # offset
    m_duckUntilOnGround = 696  # offset
    m_fStashGrenadeParameterWhen = 1292  # offset
    m_flAccumulatedJumpError = 1332  # offset
    m_flDuckAmount = 648  # offset
    m_flDuckOffset = 660  # offset
    m_flDuckSpeed = 652  # offset
    m_flHeightAtJumpStart = 1316  # offset
    m_flJumpPressedTime = 1288  # offset
    m_flLastDuckTime = 676  # offset
    m_flMaxJumpHeightLastJump = 1324  # offset
    m_flMaxJumpHeightThisJump = 1320  # offset
    m_flOffsetTickCompleteTime = 1304  # offset
    m_flOffsetTickStashedSpeed = 1308  # offset
    m_flStamina = 1312  # offset
    m_flStaminaAtJumpStart = 1328  # offset
    m_flTicksSinceLastSurfingDetected = 1336  # offset
    m_flWaterEntryTime = 1240  # offset
    m_nButtonDownMaskPrev = 1296  # offset
    m_nDuckJumpTimeMsecs = 668  # offset
    m_nDuckTimeMsecs = 664  # offset
    m_nGameCodeHasMovedPlayerAfterCommand = 1280  # offset
    m_nJumpTimeMsecs = 672  # offset
    m_nLadderSurfacePropIndex = 644  # offset
    m_nOldWaterLevel = 1236  # offset
    m_nTraceCount = 1224  # offset
    m_vecForward = 1244  # offset
    m_vecInputRotated = 1484  # offset
    m_vecLadderNormal = 632  # offset
    m_vecLastPositionAtFullCrouchSpeed = 688  # offset
    m_vecLeft = 1256  # offset
    m_vecUp = 1268  # offset

    __metadata__ =     [
        {
            "name": "m_vecLadderNormal",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nLadderSurfacePropIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flDuckAmount",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDuckSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bDuckOverride",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bDesiresDuck",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flDuckOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nDuckTimeMsecs",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nDuckJumpTimeMsecs",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nJumpTimeMsecs",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_flLastDuckTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nGameCodeHasMovedPlayerAfterCommand",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bOldJumpPressed",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fStashGrenadeParameterWhen",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_nButtonDownMaskPrev",
            "type": "NetworkVarNames",
            "type_name": "ButtonBitMask_t"
        },
        {
            "name": "m_flOffsetTickCompleteTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flOffsetTickStashedSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flStamina",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bWasSurfing",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CCSPlayer_PingServices(CPlayerPawnComponent):
    m_hPlayerPing = 64  # offset

    __metadata__ =     [
        {
            "name": "m_hPlayerPing",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        }
    ]

class CCSPlayer_UseServices(CPlayer_UseServices):
    pass

class CCSPlayer_WaterServices(CPlayer_WaterServices):
    m_flSwimSoundTime = 80  # offset
    m_flWaterJumpTime = 64  # offset
    m_vecWaterJumpVel = 68  # offset

class CCSPlayer_WeaponServices(CPlayer_WeaponServices):
    m_bBlockInspectUntilNextGraphUpdate = 6368  # offset
    m_bIsHoldingLookAtWeapon = 205  # offset
    m_bIsLookingAtWeapon = 204  # offset
    m_flNextAttack = 200  # offset
    m_nOldTotalInputHistoryCount = 872  # offset
    m_nOldTotalShootPositionHistoryCount = 208  # offset
    m_networkAnimTiming = 6344  # offset

    __metadata__ =     [
        {
            "name": "m_flNextAttack",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bIsLookingAtWeapon",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsHoldingLookAtWeapon",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_networkAnimTiming",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_bBlockInspectUntilNextGraphUpdate",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CCSPointScriptEntity(C_BaseEntity):
    pass

class CCSWeaponBaseVData:
    m_DefaultLoadoutSlot = 1800  # offset
    m_GearSlot = 1792  # offset
    m_GearSlotPosition = 1796  # offset
    m_WeaponCategory = 1092  # offset
    m_WeaponType = 1088  # offset
    m_bCannotShootUnderwater = 1823  # offset
    m_bHasBurstMode = 1821  # offset
    m_bHideViewModelWhenZoomed = 2025  # offset
    m_bIsFullAuto = 1844  # offset
    m_bIsRevolver = 1822  # offset
    m_bMeleeWeapon = 1820  # offset
    m_bReloadsSingleShells = 1852  # offset
    m_bUnzoomsAfterShot = 2024  # offset
    m_eSilencerType = 1832  # offset
    m_flArmorRatio = 2080  # offset
    m_flAttackMovespeedFactor = 2004  # offset
    m_flCycleTime = 1856  # offset
    m_flDeployDuration = 1988  # offset
    m_flDisallowAttackAfterReloadStartDuration = 1992  # offset
    m_flFlinchVelocityModifierLarge = 2096  # offset
    m_flFlinchVelocityModifierSmall = 2100  # offset
    m_flHeadshotMultiplier = 2076  # offset
    m_flInaccuracyAltSoundThreshold = 2012  # offset
    m_flInaccuracyCrouch = 1880  # offset
    m_flInaccuracyFire = 1920  # offset
    m_flInaccuracyJump = 1896  # offset
    m_flInaccuracyJumpApex = 1980  # offset
    m_flInaccuracyJumpInitial = 1976  # offset
    m_flInaccuracyLadder = 1912  # offset
    m_flInaccuracyLand = 1904  # offset
    m_flInaccuracyMove = 1928  # offset
    m_flInaccuracyPitchShift = 2008  # offset
    m_flInaccuracyReload = 1984  # offset
    m_flInaccuracyStand = 1888  # offset
    m_flIronSightFOV = 2060  # offset
    m_flIronSightLooseness = 2068  # offset
    m_flIronSightPivotForward = 2064  # offset
    m_flIronSightPullUpSpeed = 2052  # offset
    m_flIronSightPutDownSpeed = 2056  # offset
    m_flMaxSpeed = 1864  # offset
    m_flPenetration = 2084  # offset
    m_flRange = 2088  # offset
    m_flRangeModifier = 2092  # offset
    m_flRecoilAngle = 1936  # offset
    m_flRecoilAngleVariance = 1944  # offset
    m_flRecoilMagnitude = 1952  # offset
    m_flRecoilMagnitudeVariance = 1960  # offset
    m_flRecoveryTimeCrouch = 2104  # offset
    m_flRecoveryTimeCrouchFinal = 2112  # offset
    m_flRecoveryTimeStand = 2108  # offset
    m_flRecoveryTimeStandFinal = 2116  # offset
    m_flSpread = 1872  # offset
    m_flThrowVelocity = 2128  # offset
    m_flZoomTime0 = 2040  # offset
    m_flZoomTime1 = 2044  # offset
    m_flZoomTime2 = 2048  # offset
    m_nCrosshairDeltaDistance = 1840  # offset
    m_nCrosshairMinDistance = 1836  # offset
    m_nDamage = 2072  # offset
    m_nKillAward = 1808  # offset
    m_nNumBullets = 1848  # offset
    m_nPrice = 1804  # offset
    m_nPrimaryReserveAmmoMax = 1812  # offset
    m_nRecoilSeed = 1996  # offset
    m_nRecoveryTransitionEndBullet = 2124  # offset
    m_nRecoveryTransitionStartBullet = 2120  # offset
    m_nSecondaryReserveAmmoMax = 1816  # offset
    m_nSpreadSeed = 2000  # offset
    m_nTracerFrequency = 1968  # offset
    m_nZoomFOV1 = 2032  # offset
    m_nZoomFOV2 = 2036  # offset
    m_nZoomLevels = 2028  # offset
    m_szAnimClass = 2144  # offset
    m_szAnimSkeleton = 1320  # offset
    m_szModel_AG2 = 1096  # offset
    m_szName = 1824  # offset
    m_szTracerParticle = 1568  # offset
    m_szUseRadioSubtitle = 2016  # offset
    m_vSmokeColor = 2132  # offset
    m_vecMuzzlePos0 = 1544  # offset
    m_vecMuzzlePos1 = 1556  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertySuppressBaseClassField",
            "type": "Unknown"
        },
        {
            "name": "MPropertySuppressBaseClassField",
            "type": "Unknown"
        }
    ]

class CCS_PortraitWorldCallbackHandler(C_BaseEntity):
    pass

class CCitadelSoundOpvarSetOBB(C_BaseEntity):
    m_iszOperatorName = 1560  # offset
    m_iszOpvarName = 1568  # offset
    m_iszStackName = 1552  # offset
    m_nAABBDirection = 1624  # offset
    m_vDistanceInnerMaxs = 1588  # offset
    m_vDistanceInnerMins = 1576  # offset
    m_vDistanceOuterMaxs = 1612  # offset
    m_vDistanceOuterMins = 1600  # offset

    __metadata__ =     [
        {
            "name": "m_iszStackName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iszOperatorName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iszOpvarName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_vDistanceInnerMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vDistanceInnerMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vDistanceOuterMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vDistanceOuterMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nAABBDirection",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class CCollisionProperty:
    m_CollisionGroup = 94  # offset
    m_collisionAttribute = 16  # offset
    m_flBoundingRadius = 96  # offset
    m_flCapsuleRadius = 172  # offset
    m_nEnablePhysics = 95  # offset
    m_nSolidType = 91  # offset
    m_nSurroundType = 93  # offset
    m_triggerBloat = 92  # offset
    m_usSolidFlags = 90  # offset
    m_vCapsuleCenter1 = 148  # offset
    m_vCapsuleCenter2 = 160  # offset
    m_vecMaxs = 76  # offset
    m_vecMins = 64  # offset
    m_vecSpecifiedSurroundingMaxs = 112  # offset
    m_vecSpecifiedSurroundingMins = 100  # offset
    m_vecSurroundingMaxs = 124  # offset
    m_vecSurroundingMins = 136  # offset

    __metadata__ =     [
        {
            "name": "m_collisionAttribute",
            "type": "NetworkVarNames",
            "type_name": "VPhysicsCollisionAttribute_t"
        },
        {
            "name": "m_vecMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_usSolidFlags",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nSolidType",
            "type": "NetworkVarNames",
            "type_name": "SolidType_t"
        },
        {
            "name": "m_triggerBloat",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nSurroundType",
            "type": "NetworkVarNames",
            "type_name": "SurroundingBoundsType_t"
        },
        {
            "name": "m_CollisionGroup",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nEnablePhysics",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_vecSpecifiedSurroundingMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecSpecifiedSurroundingMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vCapsuleCenter1",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vCapsuleCenter2",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_flCapsuleRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CDamageRecord:
    m_DamagerXuid = 80  # offset
    m_PlayerDamager = 48  # offset
    m_PlayerRecipient = 52  # offset
    m_RecipientXuid = 88  # offset
    m_bIsOtherEnemy = 116  # offset
    m_flActualHealthRemoved = 104  # offset
    m_flBulletsDamage = 96  # offset
    m_flDamage = 100  # offset
    m_hPlayerControllerDamager = 56  # offset
    m_hPlayerControllerRecipient = 60  # offset
    m_iLastBulletUpdate = 112  # offset
    m_iNumHits = 108  # offset
    m_killType = 117  # offset
    m_szPlayerDamagerName = 64  # offset
    m_szPlayerRecipientName = 72  # offset

    __metadata__ =     [
        {
            "name": "m_PlayerDamager",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_PlayerRecipient",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_hPlayerControllerDamager",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerController>"
        },
        {
            "name": "m_hPlayerControllerRecipient",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerController>"
        },
        {
            "name": "m_szPlayerDamagerName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_szPlayerRecipientName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_DamagerXuid",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_RecipientXuid",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "MNetworkReplayCompatField",
            "type": "Unknown"
        },
        {
            "name": "m_flDamage",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "MNetworkReplayCompatField",
            "type": "Unknown"
        },
        {
            "name": "m_flActualHealthRemoved",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_iNumHits",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iLastBulletUpdate",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bIsOtherEnemy",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_killType",
            "type": "NetworkVarNames",
            "type_name": "EKillTypes_t"
        }
    ]

class CDestructiblePartsComponent:
    __m_pChainEntity = 0  # offset
    m_hOwner = 96  # offset
    m_nLastHitDamageLevel = 100  # offset
    m_vecDamageTakenByHitGroup = 72  # offset

    __metadata__ =     [
        {
            "name": "m_hOwner",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseModelEntity>"
        },
        {
            "name": "m_nLastHitDamageLevel",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class CEconItemAttribute:
    m_bSetBonus = 64  # offset
    m_flInitialValue = 56  # offset
    m_flValue = 52  # offset
    m_iAttributeDefinitionIndex = 48  # offset
    m_nRefundableCurrency = 60  # offset

    __metadata__ =     [
        {
            "name": "m_iAttributeDefinitionIndex",
            "type": "NetworkVarNames",
            "type_name": "attrib_definition_index_t"
        },
        {
            "name": "m_flValue",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flInitialValue",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nRefundableCurrency",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bSetBonus",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CEffectData:
    m_fFlags = 99  # offset
    m_flMagnitude = 68  # offset
    m_flRadius = 72  # offset
    m_flScale = 64  # offset
    m_hEntity = 56  # offset
    m_hOtherEntity = 60  # offset
    m_iEffectName = 108  # offset
    m_nAttachmentIndex = 100  # offset
    m_nAttachmentName = 104  # offset
    m_nColor = 98  # offset
    m_nDamageType = 88  # offset
    m_nEffectIndex = 80  # offset
    m_nExplosionType = 110  # offset
    m_nHitBox = 96  # offset
    m_nMaterial = 94  # offset
    m_nPenetrate = 92  # offset
    m_nSurfaceProp = 76  # offset
    m_vAngles = 44  # offset
    m_vNormal = 32  # offset
    m_vOrigin = 8  # offset
    m_vStart = 20  # offset

    __metadata__ =     [
        {
            "name": "m_vOrigin",
            "type": "NetworkVarNames",
            "type_name": "VectorWS"
        },
        {
            "name": "m_vStart",
            "type": "NetworkVarNames",
            "type_name": "VectorWS"
        },
        {
            "name": "m_vNormal",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_hEntity",
            "type": "NetworkVarNames",
            "type_name": "CEntityHandle"
        },
        {
            "name": "m_hOtherEntity",
            "type": "NetworkVarNames",
            "type_name": "CEntityHandle"
        },
        {
            "name": "m_flScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flMagnitude",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flRadius",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nSurfaceProp",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        },
        {
            "name": "m_nEffectIndex",
            "type": "NetworkVarNames",
            "type_name": "HParticleSystemDefinition"
        },
        {
            "name": "m_nDamageType",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nPenetrate",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nMaterial",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_nHitBox",
            "type": "NetworkVarNames",
            "type_name": "int16"
        },
        {
            "name": "m_nColor",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_fFlags",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nAttachmentIndex",
            "type": "NetworkVarNames",
            "type_name": "AttachmentHandle_t"
        },
        {
            "name": "m_nAttachmentName",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        },
        {
            "name": "m_iEffectName",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_nExplosionType",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        }
    ]

class CEntityComponent:
    pass

class CEntityIdentity:
    m_PathIndex = 64  # offset
    m_designerName = 32  # offset
    m_fDataObjectTypes = 60  # offset
    m_flags = 48  # offset
    m_name = 24  # offset
    m_nameStringableIndex = 20  # offset
    m_pNext = 96  # offset
    m_pNextByClass = 112  # offset
    m_pPrev = 88  # offset
    m_pPrevByClass = 104  # offset
    m_worldGroupId = 56  # offset

    __metadata__ =     [
        {
            "name": "m_nameStringableIndex",
            "type": "NetworkVarNames",
            "type_name": "int32"
        }
    ]

class CEntityInstance:
    m_CScriptComponent = 48  # offset
    m_iszPrivateVScripts = 8  # offset
    m_pEntity = 16  # offset

    __metadata__ =     [
        {
            "name": "m_pEntity",
            "type": "NetworkVarNames",
            "type_name": "CEntityIdentity*"
        },
        {
            "name": "m_CScriptComponent",
            "type": "NetworkVarNames",
            "type_name": "CScriptComponent::Storage_t"
        }
    ]

class CEnvSoundscape(C_BaseEntity):
    m_OnPlay = 1528  # offset
    m_bDisabled = 1668  # offset
    m_bOverrideWithEvent = 1584  # offset
    m_flRadius = 1568  # offset
    m_hProxySoundscape = 1664  # offset
    m_positionNames = 1600  # offset
    m_soundEventHash = 1680  # offset
    m_soundEventName = 1576  # offset
    m_soundscapeEntityListId = 1592  # offset
    m_soundscapeIndex = 1588  # offset
    m_soundscapeName = 1672  # offset

class CEnvSoundscapeAlias_snd_soundscape(CEnvSoundscape):
    pass

class CEnvSoundscapeProxy(CEnvSoundscape):
    m_MainSoundscapeName = 1688  # offset

class CEnvSoundscapeProxyAlias_snd_soundscape_proxy(CEnvSoundscapeProxy):
    pass

class CEnvSoundscapeTriggerable(CEnvSoundscape):
    pass

class CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable(CEnvSoundscapeTriggerable):
    pass

class CFilterAttributeInt(CBaseFilter):
    m_sAttributeName = 1616  # offset

class CFilterClass(CBaseFilter):
    m_iFilterClass = 1616  # offset

class CFilterLOS(CBaseFilter):
    pass

class CFilterMassGreater(CBaseFilter):
    m_fFilterMass = 1616  # offset

class CFilterModel(CBaseFilter):
    m_iFilterModel = 1616  # offset

class CFilterMultiple(CBaseFilter):
    m_hFilter = 1704  # offset
    m_iFilterName = 1624  # offset
    m_nFilterType = 1616  # offset

class CFilterMultipleAPI:
    pass

class CFilterName(CBaseFilter):
    m_iFilterName = 1616  # offset

class CFilterProximity(CBaseFilter):
    m_flRadius = 1616  # offset

class CFilterTeam(CBaseFilter):
    m_iFilterTeam = 1616  # offset

class CFuncWater(C_BaseModelEntity):
    m_BuoyancyHelper = 3784  # offset

class CGameSceneNode:
    m_angAbsRotation = 220  # offset
    m_angRotation = 192  # offset
    m_angWrappedLocalRotation = 248  # offset
    m_bBoneMergeFlex = 0  # offset
    m_bDebugAbsOriginChanges = 266  # offset
    m_bDirtyBoneMergeBoneToRoot = 0  # offset
    m_bDirtyBoneMergeInfo = 0  # offset
    m_bDirtyHierarchy = 0  # offset
    m_bDormant = 267  # offset
    m_bForceParentToBeNetworked = 268  # offset
    m_bNetworkedAnglesChanged = 0  # offset
    m_bNetworkedPositionChanged = 0  # offset
    m_bNetworkedScaleChanged = 0  # offset
    m_bWillBeCallingPostDataUpdate = 0  # offset
    m_flAbsScale = 232  # offset
    m_flClientLocalScale = 352  # offset
    m_flScale = 204  # offset
    m_flWrappedScale = 260  # offset
    m_flZOffset = 348  # offset
    m_hParent = 120  # offset
    m_hierarchyAttachName = 344  # offset
    m_nDoNotSetAnimTimeInInvalidatePhysicsCount = 273  # offset
    m_nHierarchicalDepth = 271  # offset
    m_nHierarchyType = 272  # offset
    m_nLatchAbsOrigin = 0  # offset
    m_nParentAttachmentOrBone = 264  # offset
    m_name = 276  # offset
    m_nodeToWorld = 16  # offset
    m_pChild = 64  # offset
    m_pNextSibling = 72  # offset
    m_pOwner = 48  # offset
    m_pParent = 56  # offset
    m_vRenderOrigin = 356  # offset
    m_vecAbsOrigin = 208  # offset
    m_vecOrigin = 136  # offset
    m_vecWrappedLocalOrigin = 236  # offset

    __metadata__ =     [
        {
            "name": "m_hParent",
            "type": "NetworkVarNames",
            "type_name": "CGameSceneNodeHandle"
        },
        {
            "name": "m_vecOrigin",
            "type": "NetworkVarNames",
            "type_name": "CNetworkOriginCellCoordQuantizedVector"
        },
        {
            "name": "m_angRotation",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_flScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_name",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        },
        {
            "name": "m_hierarchyAttachName",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        }
    ]

class CGameSceneNodeHandle:
    m_hOwner = 8  # offset
    m_name = 12  # offset

    __metadata__ =     [
        {
            "name": "m_hOwner",
            "type": "NetworkVarNames",
            "type_name": "CEntityHandle"
        },
        {
            "name": "m_name",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        }
    ]

class CGlowProperty:
    m_bEligibleForScreenHighlight = 80  # offset
    m_bFlashing = 68  # offset
    m_bGlowing = 81  # offset
    m_fGlowColor = 8  # offset
    m_flGlowStartTime = 76  # offset
    m_flGlowTime = 72  # offset
    m_glowColorOverride = 64  # offset
    m_iGlowTeam = 52  # offset
    m_iGlowType = 48  # offset
    m_nGlowRange = 56  # offset
    m_nGlowRangeMin = 60  # offset

    __metadata__ =     [
        {
            "name": "m_iGlowType",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_iGlowTeam",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_nGlowRange",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_nGlowRangeMin",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_glowColorOverride",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_bFlashing",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flGlowTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flGlowStartTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bEligibleForScreenHighlight",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CGrenadeTracer(C_BaseModelEntity):
    m_flTracerDuration = 3808  # offset
    m_nType = 3812  # offset

class CHitboxComponent(CEntityComponent):
    m_flBoundsExpandRadius = 32  # offset

class CHostageRescueZone(CHostageRescueZoneShim):
    pass

class CHostageRescueZoneShim(C_BaseTrigger):
    pass

class CInfoDynamicShadowHint(C_PointEntity):
    m_bDisabled = 1528  # offset
    m_flRange = 1532  # offset
    m_hLight = 1544  # offset
    m_nImportance = 1536  # offset
    m_nLightChoice = 1540  # offset

class CInfoDynamicShadowHintBox(CInfoDynamicShadowHint):
    m_vBoxMaxs = 1564  # offset
    m_vBoxMins = 1552  # offset

class CInfoFan(C_PointEntity):
    m_FanForceCurveString = 1608  # offset
    m_fFanForceMaxRadius = 1592  # offset
    m_fFanForceMinRadius = 1596  # offset
    m_flCurveDistRange = 1600  # offset

    __metadata__ =     [
        {
            "name": "m_fFanForceMaxRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fFanForceMinRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flCurveDistRange",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_FanForceCurveString",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class CInfoOffscreenPanoramaTexture(C_PointEntity):
    m_RenderAttrName = 1552  # offset
    m_TargetEntities = 1560  # offset
    m_bCheckCSSClasses = 1976  # offset
    m_bDisabled = 1528  # offset
    m_nResolutionX = 1532  # offset
    m_nResolutionY = 1536  # offset
    m_nTargetChangeCount = 1584  # offset
    m_szLayoutFileName = 1544  # offset
    m_vecCSSClasses = 1592  # offset

    __metadata__ =     [
        {
            "name": "m_bDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nResolutionX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nResolutionY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_szLayoutFileName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_RenderAttrName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_TargetEntities",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseModelEntity>"
        },
        {
            "name": "m_nTargetChangeCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vecCSSClasses",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class CInfoParticleTarget(C_PointEntity):
    pass

class CInfoTarget(C_PointEntity):
    pass

class CInfoWorldLayer(C_BaseEntity):
    m_bCreateAsChildSpawnGroup = 1586  # offset
    m_bEntitiesSpawned = 1585  # offset
    m_bWorldLayerActuallyVisible = 1592  # offset
    m_bWorldLayerVisible = 1584  # offset
    m_hLayerSpawnGroup = 1588  # offset
    m_layerName = 1576  # offset
    m_pOutputOnEntitiesSpawned = 1528  # offset
    m_worldName = 1568  # offset

    __metadata__ =     [
        {
            "name": "m_worldName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_layerName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_bWorldLayerVisible",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bEntitiesSpawned",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CLightComponent(CEntityComponent):
    __m_pChainEntity = 48  # offset
    m_Color = 109  # offset
    m_Pattern = 208  # offset
    m_SecondaryColor = 113  # offset
    m_SkyAmbientBounce = 396  # offset
    m_SkyColor = 388  # offset
    m_bAllowSSTGeneration = 281  # offset
    m_bEnabled = 308  # offset
    m_bFlicker = 309  # offset
    m_bMixedShadows = 401  # offset
    m_bPrecomputedFieldsValid = 310  # offset
    m_bRenderDiffuse = 184  # offset
    m_bRenderToCubemaps = 280  # offset
    m_bRenderTransmissive = 192  # offset
    m_bUseSecondaryColor = 400  # offset
    m_bUsesBakedShadowing = 260  # offset
    m_flAttenuation0 = 140  # offset
    m_flAttenuation1 = 144  # offset
    m_flAttenuation2 = 148  # offset
    m_flBrightness = 120  # offset
    m_flBrightnessMult = 128  # offset
    m_flBrightnessScale = 124  # offset
    m_flCapsuleLength = 408  # offset
    m_flFadeMaxDist = 296  # offset
    m_flFadeMinDist = 292  # offset
    m_flFalloff = 136  # offset
    m_flFogContributionStength = 380  # offset
    m_flLightStyleStartTime = 404  # offset
    m_flMinRoughness = 412  # offset
    m_flNearClipPlane = 384  # offset
    m_flOrthoLightHeight = 200  # offset
    m_flOrthoLightWidth = 196  # offset
    m_flPhi = 156  # offset
    m_flPrecomputedMaxRange = 372  # offset
    m_flRange = 132  # offset
    m_flShadowCascadeCrossFade = 220  # offset
    m_flShadowCascadeDistance0 = 228  # offset
    m_flShadowCascadeDistance1 = 232  # offset
    m_flShadowCascadeDistance2 = 236  # offset
    m_flShadowCascadeDistance3 = 240  # offset
    m_flShadowCascadeDistanceFade = 224  # offset
    m_flShadowFadeMaxDist = 304  # offset
    m_flShadowFadeMinDist = 300  # offset
    m_flSkyIntensity = 392  # offset
    m_flTheta = 152  # offset
    m_hLightCookie = 160  # offset
    m_nBakedShadowIndex = 268  # offset
    m_nCascadeRenderStaticObjects = 216  # offset
    m_nCascades = 168  # offset
    m_nCastShadows = 172  # offset
    m_nDirectLight = 284  # offset
    m_nFogLightingMode = 376  # offset
    m_nIndirectLight = 288  # offset
    m_nLightMapUniqueId = 276  # offset
    m_nLightPathUniqueId = 272  # offset
    m_nRenderSpecular = 188  # offset
    m_nShadowCascadeResolution0 = 244  # offset
    m_nShadowCascadeResolution1 = 248  # offset
    m_nShadowCascadeResolution2 = 252  # offset
    m_nShadowCascadeResolution3 = 256  # offset
    m_nShadowHeight = 180  # offset
    m_nShadowPriority = 264  # offset
    m_nShadowWidth = 176  # offset
    m_nStyle = 204  # offset
    m_vPrecomputedBoundsMaxs = 324  # offset
    m_vPrecomputedBoundsMins = 312  # offset
    m_vPrecomputedOBBAngles = 348  # offset
    m_vPrecomputedOBBExtent = 360  # offset
    m_vPrecomputedOBBOrigin = 336  # offset

    __metadata__ =     [
        {
            "name": "m_Color",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_SecondaryColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flBrightness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flBrightnessScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flBrightnessMult",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flRange",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFalloff",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flAttenuation0",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flAttenuation1",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flAttenuation2",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flTheta",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flPhi",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_hLightCookie",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_nCascades",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nCastShadows",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowWidth",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowHeight",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bRenderDiffuse",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nRenderSpecular",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bRenderTransmissive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flOrthoLightWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flOrthoLightHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nStyle",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Pattern",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_nCascadeRenderStaticObjects",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flShadowCascadeCrossFade",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowCascadeDistanceFade",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowCascadeDistance0",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowCascadeDistance1",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowCascadeDistance2",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowCascadeDistance3",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nShadowCascadeResolution0",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowCascadeResolution1",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowCascadeResolution2",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowCascadeResolution3",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bUsesBakedShadowing",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nShadowPriority",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nBakedShadowIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nLightPathUniqueId",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_nLightMapUniqueId",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_bRenderToCubemaps",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bAllowSSTGeneration",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nDirectLight",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nIndirectLight",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFadeMinDist",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeMaxDist",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowFadeMinDist",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowFadeMaxDist",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bFlicker",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bPrecomputedFieldsValid",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vPrecomputedBoundsMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedBoundsMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_flPrecomputedMaxRange",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nFogLightingMode",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFogContributionStength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flNearClipPlane",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_SkyColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flSkyIntensity",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_SkyAmbientBounce",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_bUseSecondaryColor",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMixedShadows",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flLightStyleStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flCapsuleLength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flMinRoughness",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CLogicRelay(CLogicalEntity):
    m_bDisabled = 1528  # offset
    m_bFastRetrigger = 1531  # offset
    m_bPassthoughCaller = 1532  # offset
    m_bTriggerOnce = 1530  # offset
    m_bWaitForRefire = 1529  # offset

class CLogicRelayAPI:
    pass

class CLogicalEntity(C_BaseEntity):
    pass

class CMapInfo(C_PointEntity):
    m_bDisableAutoGeneratedDMSpawns = 1541  # offset
    m_bFadePlayerVisibilityFarZ = 1552  # offset
    m_bRainTraceToSkyEnabled = 1553  # offset
    m_bUseNormalSpawnsForDM = 1540  # offset
    m_flBombRadius = 1532  # offset
    m_flBotMaxVisionDistance = 1544  # offset
    m_flEnvPuddleRippleDirection = 1564  # offset
    m_flEnvPuddleRippleStrength = 1560  # offset
    m_flEnvRainStrength = 1556  # offset
    m_flEnvWetnessCoverage = 1568  # offset
    m_flEnvWetnessDryingAmount = 1572  # offset
    m_iBuyingStatus = 1528  # offset
    m_iHostageCount = 1548  # offset
    m_iPetPopulation = 1536  # offset

class CModelState:
    m_MeshGroupMask = 592  # offset
    m_ModelName = 216  # offset
    m_bClientClothCreationSuppressed = 425  # offset
    m_hModel = 208  # offset
    m_nBodyGroupChoices = 672  # offset
    m_nClothUpdateFlags = 748  # offset
    m_nForceLOD = 747  # offset
    m_nIdealMotionType = 746  # offset

    __metadata__ =     [
        {
            "name": "m_hModel",
            "type": "NetworkVarNames",
            "type_name": "HModelStrong"
        },
        {
            "name": "m_bClientClothCreationSuppressed",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_MeshGroupMask",
            "type": "NetworkVarNames",
            "type_name": "MeshGroupMask_t"
        },
        {
            "name": "m_nBodyGroupChoices",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_nIdealMotionType",
            "type": "NetworkVarNames",
            "type_name": "int8"
        }
    ]

class CNetworkedSequenceOperation:
    m_bDiscontinuity = 29  # offset
    m_bSequenceChangeNetworked = 28  # offset
    m_flCycle = 16  # offset
    m_flPrevCycle = 12  # offset
    m_flPrevCycleForAnimEventDetection = 36  # offset
    m_flPrevCycleFromDiscontinuity = 32  # offset
    m_flWeight = 20  # offset
    m_hSequence = 8  # offset

    __metadata__ =     [
        {
            "name": "m_hSequence",
            "type": "NetworkVarNames",
            "type_name": "HSequence"
        },
        {
            "name": "m_flPrevCycle",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flCycle",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class CPathQueryComponent(CEntityComponent):
    pass

class CPathSimple(C_BaseEntity):
    m_CPathQueryComponent = 1536  # offset
    m_bClosedLoop = 1784  # offset
    m_pathString = 1776  # offset

    __metadata__ =     [
        {
            "name": "m_CPathQueryComponent",
            "type": "NetworkVarNames",
            "type_name": "CPathQueryComponent::Storage_t"
        },
        {
            "name": "m_pathString",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        }
    ]

class CPathSimpleAPI:
    pass

class CPlayer_AutoaimServices(CPlayerPawnComponent):
    pass

class CPlayer_CameraServices(CPlayerPawnComponent):
    m_CurrentFog = 320  # offset
    m_OverrideFogColor = 433  # offset
    m_PlayerFog = 88  # offset
    m_PostProcessingVolumes = 288  # offset
    m_angDemoViewAngles = 504  # offset
    m_audio = 168  # offset
    m_bOverrideFogColor = 428  # offset
    m_bOverrideFogStartEnd = 453  # offset
    m_fOverrideFogEnd = 480  # offset
    m_fOverrideFogStart = 460  # offset
    m_flCsViewPunchAngleTickRatio = 80  # offset
    m_flOldPlayerViewOffsetZ = 316  # offset
    m_flOldPlayerZ = 312  # offset
    m_hActivePostProcessingVolume = 500  # offset
    m_hColorCorrectionCtrl = 152  # offset
    m_hOldFogController = 424  # offset
    m_hTonemapController = 160  # offset
    m_hViewEntity = 156  # offset
    m_nCsViewPunchAngleTick = 76  # offset
    m_vecCsViewPunchAngle = 64  # offset

    __metadata__ =     [
        {
            "name": "m_vecCsViewPunchAngle",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_nCsViewPunchAngleTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_flCsViewPunchAngleTickRatio",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_PlayerFog",
            "type": "NetworkVarNames",
            "type_name": "fogplayerparams_t"
        },
        {
            "name": "m_hColorCorrectionCtrl",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CColorCorrection>"
        },
        {
            "name": "m_hViewEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_hTonemapController",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CTonemapController2>"
        },
        {
            "name": "m_audio",
            "type": "NetworkVarNames",
            "type_name": "audioparams_t"
        },
        {
            "name": "m_PostProcessingVolumes",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_PostProcessingVolume>"
        }
    ]

class CPlayer_FlashlightServices(CPlayerPawnComponent):
    pass

class CPlayer_ItemServices(CPlayerPawnComponent):
    pass

class CPlayer_MovementServices(CPlayerPawnComponent):
    m_arrForceSubtickMoveWhen = 412  # offset
    m_flForwardMove = 428  # offset
    m_flLeftMove = 432  # offset
    m_flMaxspeed = 408  # offset
    m_flUpMove = 436  # offset
    m_nButtonDoublePressed = 120  # offset
    m_nButtons = 72  # offset
    m_nImpulse = 64  # offset
    m_nLastCommandNumberProcessed = 384  # offset
    m_nQueuedButtonChangeMask = 112  # offset
    m_nQueuedButtonDownMask = 104  # offset
    m_nToggleButtonDownMask = 392  # offset
    m_pButtonPressedCmdNumber = 128  # offset
    m_vecLastMovementImpulses = 440  # offset
    m_vecOldViewAngles = 544  # offset

    __metadata__ =     [
        {
            "name": "m_nToggleButtonDownMask",
            "type": "NetworkVarNames",
            "type_name": "ButtonBitMask_t"
        },
        {
            "name": "m_flMaxspeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_arrForceSubtickMoveWhen",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class CPlayer_MovementServices_Humanoid(CPlayer_MovementServices):
    m_bDucked = 588  # offset
    m_bDucking = 589  # offset
    m_bInCrouch = 576  # offset
    m_bInDuckJump = 590  # offset
    m_flCrouchTransitionStartTime = 584  # offset
    m_flFallVelocity = 572  # offset
    m_flStepSoundTime = 568  # offset
    m_flSurfaceFriction = 604  # offset
    m_groundNormal = 592  # offset
    m_nCrouchState = 580  # offset
    m_nStepside = 624  # offset
    m_surfaceProps = 608  # offset

    __metadata__ =     [
        {
            "name": "m_flFallVelocity",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_bInCrouch",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nCrouchState",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_flCrouchTransitionStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bDucked",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bDucking",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bInDuckJump",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CPlayer_ObserverServices(CPlayerPawnComponent):
    m_bForcedObserverMode = 76  # offset
    m_flObserverChaseDistance = 80  # offset
    m_flObserverChaseDistanceCalcTime = 84  # offset
    m_hObserverTarget = 68  # offset
    m_iObserverLastMode = 72  # offset
    m_iObserverMode = 64  # offset

    __metadata__ =     [
        {
            "name": "m_iObserverMode",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_hObserverTarget",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        }
    ]

class CPlayer_UseServices(CPlayerPawnComponent):
    pass

class CPlayer_WaterServices(CPlayerPawnComponent):
    pass

class CPlayer_WeaponServices(CPlayerPawnComponent):
    m_hActiveWeapon = 88  # offset
    m_hLastWeapon = 92  # offset
    m_hMyWeapons = 64  # offset
    m_iAmmo = 96  # offset

    __metadata__ =     [
        {
            "name": "m_hMyWeapons",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BasePlayerWeapon>"
        },
        {
            "name": "m_hActiveWeapon",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerWeapon>"
        },
        {
            "name": "m_hLastWeapon",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerWeapon>"
        },
        {
            "name": "m_iAmmo",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        }
    ]

class CPointChildModifier(C_PointEntity):
    m_bOrphanInsteadOfDeletingChildrenOnRemove = 1528  # offset

class CPointOffScreenIndicatorUi(C_PointClientUIWorldPanel):
    m_bBeenEnabled = 4400  # offset
    m_bHide = 4401  # offset
    m_flSeenTargetTime = 4404  # offset
    m_pTargetPanel = 4408  # offset

class CPointOrient(C_BaseEntity):
    m_bActive = 1540  # offset
    m_flLastGameTime = 1556  # offset
    m_flMaxTurnRate = 1552  # offset
    m_hTarget = 1536  # offset
    m_iszSpawnTargetName = 1528  # offset
    m_nConstraint = 1548  # offset
    m_nGoalDirection = 1544  # offset

class CPointTemplate(CLogicalEntity):
    m_ScriptCallbackScope = 1624  # offset
    m_ScriptSpawnCallback = 1616  # offset
    m_SpawnedEntityHandles = 1592  # offset
    m_bAsynchronouslySpawnEntities = 1556  # offset
    m_clientOnlyEntityBehavior = 1560  # offset
    m_createdSpawnGroupHandles = 1568  # offset
    m_flTimeoutInterval = 1552  # offset
    m_iszEntityFilterName = 1544  # offset
    m_iszSource2EntityLumpName = 1536  # offset
    m_iszWorldName = 1528  # offset
    m_ownerSpawnGroupType = 1564  # offset

class CPointTemplateAPI:
    pass

class CPrecipitationVData:
    m_bBatchSameVolumeType = 272  # offset
    m_flInnerDistance = 264  # offset
    m_nAttachType = 268  # offset
    m_nRTEnvCP = 276  # offset
    m_nRTEnvCPComponent = 280  # offset
    m_szModifier = 288  # offset
    m_szParticlePrecipitationEffect = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPropDataComponent(CEntityComponent):
    m_bSpawnMotionDisabled = 52  # offset
    m_flDmgModBullet = 16  # offset
    m_flDmgModClub = 20  # offset
    m_flDmgModExplosive = 24  # offset
    m_flDmgModFire = 28  # offset
    m_iszBasePropData = 40  # offset
    m_iszPhysicsDamageTableName = 32  # offset
    m_nDisableTakePhysicsDamageSpawnFlag = 56  # offset
    m_nInteractions = 48  # offset
    m_nMotionDisabledSpawnFlag = 60  # offset

class CPulseAnimFuncs:
    pass

class CPulseArraylib:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseCell_Base:
    m_nEditorNodeID = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseFlow:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseLerp:
    m_WakeResume = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseLerp__CursorState_t:
    m_EndTime = 4  # offset
    m_StartTime = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseRequirement:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseState:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseValue:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BaseYieldingInflow:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_BooleanSwitchState:
    m_Condition = 72  # offset
    m_SubGraph = 192  # offset
    m_WhenFalse = 336  # offset
    m_WhenTrue = 264  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorCanvasItemSpecKV3",
            "type": "Unknown"
        }
    ]

class CPulseCell_CursorQueue:
    m_nCursorsAllowedToRunParallel = 152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_FireCursors:
    m_OnCanceled = 176  # offset
    m_OnFinished = 104  # offset
    m_Outflows = 72  # offset
    m_bWaitForChildOutflows = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_BaseEntrypoint:
    m_EntryChunk = 72  # offset
    m_RegisterMap = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_EntOutputHandler:
    m_ExpectedParamType = 160  # offset
    m_SourceEntity = 128  # offset
    m_SourceOutput = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_EventHandler:
    m_EventName = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_GraphHook:
    m_HookName = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_Method:
    m_Args = 184  # offset
    m_Description = 144  # offset
    m_MethodName = 128  # offset
    m_ReturnType = 160  # offset
    m_bIsPublic = 152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_ObservableVariableListener:
    m_bSelfReference = 130  # offset
    m_nBlackboardReference = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_Wait:
    m_WakeResume = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorCanvasItemSpecKV3",
            "type": "Unknown"
        }
    ]

class CPulseCell_Inflow_Yield:
    m_UnyieldResume = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_InlineNodeSkipSelector:
    m_FailOutflow = 104  # offset
    m_PassOutflow = 80  # offset
    m_bAnd = 76  # offset
    m_nFlowNodeID = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_IntervalTimer:
    m_Completed = 72  # offset
    m_OnInterval = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_IntervalTimer__CursorState_t:
    m_EndTime = 4  # offset
    m_StartTime = 0  # offset
    m_bCompleteOnNextWake = 16  # offset
    m_flWaitInterval = 8  # offset
    m_flWaitIntervalHigh = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_IsRequirementValid:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_IsRequirementValid__Criteria_t:
    m_bIsValid = 0  # offset

class CPulseCell_LerpCameraSettings:
    m_End = 164  # offset
    m_Start = 148  # offset
    m_flSeconds = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_LerpCameraSettings__CursorState_t:
    m_OverlaidEnd = 28  # offset
    m_OverlaidStart = 12  # offset
    m_hCamera = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_LimitCount:
    m_nLimitCount = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseCell_LimitCount__Criteria_t:
    m_bLimitCountPasses = 0  # offset

class CPulseCell_LimitCount__InstanceState_t:
    m_nCurrentCount = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_CycleOrdered:
    m_Outputs = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_CycleOrdered__InstanceState_t:
    m_nNextIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_CycleRandom:
    m_Outputs = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_CycleShuffled:
    m_Outputs = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_CycleShuffled__InstanceState_t:
    m_Shuffle = 0  # offset
    m_nNextShuffle = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_PickBestOutflowSelector:
    m_OutflowList = 80  # offset
    m_nCheckType = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorCanvasItemSpecKV3",
            "type": "Unknown"
        }
    ]

class CPulseCell_PlaySequence:
    m_OnCanceled = 176  # offset
    m_OnFinished = 104  # offset
    m_PulseAnimEvents = 80  # offset
    m_SequenceName = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseCell_PlaySequence__CursorState_t:
    m_hTarget = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Step_CallExternalMethod:
    m_ExpectedArgs = 104  # offset
    m_GameBlackboard = 88  # offset
    m_MethodName = 72  # offset
    m_OnFinished = 128  # offset
    m_nAsyncCallMode = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Step_DebugLog:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Step_EntFire:
    m_Input = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Step_PublicOutput:
    m_OutputIndex = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Timeline:
    m_OnCanceled = 176  # offset
    m_OnFinished = 104  # offset
    m_TimelineEvents = 72  # offset
    m_bWaitForChildOutflows = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        }
    ]

class CPulseCell_Timeline__TimelineEvent_t:
    m_EventOutflow = 8  # offset
    m_flTimeFromPrevious = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Unknown:
    m_UnknownKeys = 72  # offset

class CPulseCell_Value_Curve:
    m_Curve = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CPulseCell_Value_Gradient:
    m_Gradient = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CPulseCell_Value_RandomFloat:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_Value_RandomInt:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_WaitForCursorsWithTag:
    m_bTagSelfWhenComplete = 152  # offset
    m_nDesiredKillPriority = 156  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_WaitForCursorsWithTagBase:
    m_WaitComplete = 80  # offset
    m_nCursorsAllowedToWait = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorCanvasItemSpecKV3",
            "type": "Unknown"
        }
    ]

class CPulseCell_WaitForCursorsWithTagBase__CursorState_t:
    m_TagName = 0  # offset

class CPulseCell_WaitForObservable:
    m_Condition = 72  # offset
    m_OnTrue = 192  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPulseCellMethodBindings",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CPulseCursorFuncs:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseExecCursor:
    pass

class CPulseGameBlackboard(C_BaseEntity):
    m_strGraphName = 1528  # offset
    m_strStateBlob = 1536  # offset

    __metadata__ =     [
        {
            "name": "m_strGraphName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_strStateBlob",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        }
    ]

class CPulseGraphDef:
    m_BlackboardReferences = 272  # offset
    m_CallInfos = 200  # offset
    m_Cells = 104  # offset
    m_Chunks = 80  # offset
    m_Constants = 224  # offset
    m_DomainIdentifier = 8  # offset
    m_DomainSubType = 24  # offset
    m_DomainValues = 248  # offset
    m_InvokeBindings = 176  # offset
    m_OutputConnections = 296  # offset
    m_ParentMapName = 48  # offset
    m_ParentXmlName = 64  # offset
    m_PublicOutputs = 152  # offset
    m_Vars = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseMathlib:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseTestScriptLib:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulse_BlackboardReference:
    m_BlackboardResource = 8  # offset
    m_NodeName = 32  # offset
    m_hBlackboardResource = 0  # offset
    m_nNodeID = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_CallInfo:
    m_CallMethodID = 72  # offset
    m_PortName = 0  # offset
    m_RegisterMap = 24  # offset
    m_nEditorNodeID = 16  # offset
    m_nSrcChunk = 76  # offset
    m_nSrcInstruction = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_InvokeBinding:
    m_FuncName = 48  # offset
    m_RegisterMap = 0  # offset
    m_nCellIndex = 64  # offset
    m_nSrcChunk = 68  # offset
    m_nSrcInstruction = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_OutflowConnection:
    m_OutflowRegisterMap = 24  # offset
    m_SourceOutflowName = 0  # offset
    m_nDestChunk = 16  # offset
    m_nInstruction = 20  # offset

class CPulse_ResumePoint:
    pass

class CRagdollManager(C_BaseEntity):
    m_iCurrentMaxRagdollCount = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_iCurrentMaxRagdollCount",
            "type": "NetworkVarNames",
            "type_name": "int8"
        }
    ]

class CRenderComponent(CEntityComponent):
    __m_pChainEntity = 16  # offset
    m_bEnableRendering = 88  # offset
    m_bInterpolationReadyToDraw = 168  # offset
    m_bIsRenderingWithViewModels = 80  # offset
    m_nSplitscreenFlags = 84  # offset

class CSMatchStats_t:
    m_iEnemy3Ks = 112  # offset
    m_iEnemy4Ks = 108  # offset
    m_iEnemy5Ks = 104  # offset
    m_iEnemyKnifeKills = 116  # offset
    m_iEnemyTaserKills = 120  # offset

    __metadata__ =     [
        {
            "name": "m_iEnemy5Ks",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEnemy4Ks",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEnemy3Ks",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEnemyKnifeKills",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEnemyTaserKills",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class CSPerRoundStats_t:
    m_iAssists = 56  # offset
    m_iCashEarned = 88  # offset
    m_iDamage = 60  # offset
    m_iDeaths = 52  # offset
    m_iEnemiesFlashed = 96  # offset
    m_iEquipmentValue = 64  # offset
    m_iHeadShotKills = 80  # offset
    m_iKillReward = 72  # offset
    m_iKills = 48  # offset
    m_iLiveTime = 76  # offset
    m_iMoneySaved = 68  # offset
    m_iObjective = 84  # offset
    m_iUtilityDamage = 92  # offset

    __metadata__ =     [
        {
            "name": "m_iKills",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iDeaths",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iAssists",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iDamage",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEquipmentValue",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMoneySaved",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iKillReward",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iLiveTime",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iHeadShotKills",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iObjective",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iCashEarned",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iUtilityDamage",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEnemiesFlashed",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class CScriptComponent(CEntityComponent):
    m_scriptClassName = 48  # offset

class CServerOnlyModelEntity(C_BaseModelEntity):
    pass

class CSkeletonInstance(CGameSceneNode):
    m_bDirtyMotionType = 0  # offset
    m_bDisableSolidCollisionsForHierarchy = 1170  # offset
    m_bIsAnimationEnabled = 1168  # offset
    m_bIsGeneratingLatchedParentSpaceState = 0  # offset
    m_bUseParentRenderBounds = 1169  # offset
    m_materialGroup = 1172  # offset
    m_modelState = 400  # offset
    m_nHitboxSet = 1176  # offset

    __metadata__ =     [
        {
            "name": "m_modelState",
            "type": "NetworkVarNames",
            "type_name": "CModelState"
        },
        {
            "name": "m_bIsAnimationEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bUseParentRenderBounds",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_materialGroup",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        },
        {
            "name": "m_nHitboxSet",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        }
    ]

class CSkyboxReference(C_BaseEntity):
    m_hSkyCamera = 1532  # offset
    m_worldGroupId = 1528  # offset

class CSpriteOriented(C_Sprite):
    pass

class CTakeDamageInfoAPI:
    pass

class CTimeline:
    m_bStopped = 544  # offset
    m_flFinalValue = 536  # offset
    m_flInterval = 532  # offset
    m_flValues = 16  # offset
    m_nBucketCount = 528  # offset
    m_nCompressionType = 540  # offset
    m_nValueCounts = 272  # offset

    __metadata__ =     [
        {
            "name": "m_flValues",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nValueCounts",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nBucketCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flInterval",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFinalValue",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nCompressionType",
            "type": "NetworkVarNames",
            "type_name": "TimelineCompression_t"
        },
        {
            "name": "m_bStopped",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CTriggerFan(C_BaseTrigger):
    m_RampTimer = 4208  # offset
    m_bFalloff = 4200  # offset
    m_bPushAwayFromInfoTarget = 4165  # offset
    m_bPushTowardsInfoTarget = 4164  # offset
    m_flForce = 4196  # offset
    m_hInfoFan = 4192  # offset
    m_qNoiseDelta = 4176  # offset
    m_vDirection = 4152  # offset
    m_vFanEnd = 4128  # offset
    m_vFanOrigin = 4104  # offset
    m_vFanOriginOffset = 4116  # offset
    m_vNoiseDirectionTarget = 4140  # offset

    __metadata__ =     [
        {
            "name": "m_vFanOrigin",
            "type": "NetworkVarNames",
            "type_name": "VectorWS"
        },
        {
            "name": "m_vFanOriginOffset",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vFanEnd",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vNoiseDirectionTarget",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vDirection",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bPushTowardsInfoTarget",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bPushAwayFromInfoTarget",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_qNoiseDelta",
            "type": "NetworkVarNames",
            "type_name": "Quaternion"
        },
        {
            "name": "m_hInfoFan",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CInfoFan>"
        },
        {
            "name": "m_flForce",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bFalloff",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_RampTimer",
            "type": "NetworkVarNames",
            "type_name": "CountdownTimer"
        }
    ]

class CWaterSplasher(C_BaseModelEntity):
    pass

class C_AK47(C_CSWeaponBaseGun):
    pass

class C_AttributeContainer(CAttributeManager):
    m_Item = 80  # offset
    m_iExternalItemProviderRegisteredToken = 1224  # offset
    m_ullRegisteredAsItemID = 1232  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_Item",
            "type": "NetworkVarNames",
            "type_name": "CEconItemView"
        }
    ]

class C_BarnLight(C_BaseModelEntity):
    m_Color = 3792  # offset
    m_LightStyleEvents = 3880  # offset
    m_LightStyleString = 3840  # offset
    m_LightStyleTargets = 3904  # offset
    m_QueuedLightStyleStrings = 3856  # offset
    m_StyleEvent = 3928  # offset
    m_VisClusters = 4600  # offset
    m_bContactShadow = 4172  # offset
    m_bEnabled = 3784  # offset
    m_bFogMixedShadows = 4220  # offset
    m_bForceShadowsEnabled = 4173  # offset
    m_bInitialBoneSetup = 4592  # offset
    m_bPrecomputedFieldsValid = 4240  # offset
    m_fAlternateColorBrightness = 4200  # offset
    m_flBounceScale = 4180  # offset
    m_flBrightness = 3800  # offset
    m_flBrightnessScale = 3804  # offset
    m_flColorTemperature = 3796  # offset
    m_flFadeSizeEnd = 4228  # offset
    m_flFadeSizeStart = 4224  # offset
    m_flFogScale = 4216  # offset
    m_flFogStrength = 4208  # offset
    m_flLightStyleStartTime = 3848  # offset
    m_flLuminaireAnisotropy = 3832  # offset
    m_flLuminaireSize = 3828  # offset
    m_flMinRoughness = 4184  # offset
    m_flRange = 4128  # offset
    m_flShadowFadeSizeEnd = 4236  # offset
    m_flShadowFadeSizeStart = 4232  # offset
    m_flShape = 4096  # offset
    m_flSkirt = 4108  # offset
    m_flSkirtNear = 4112  # offset
    m_flSoftX = 4100  # offset
    m_flSoftY = 4104  # offset
    m_hLightCookie = 4088  # offset
    m_nBakeSpecularToCubemaps = 4144  # offset
    m_nBakedShadowIndex = 3812  # offset
    m_nBounceLight = 4176  # offset
    m_nCastShadows = 4160  # offset
    m_nColorMode = 3788  # offset
    m_nDirectLight = 3808  # offset
    m_nFog = 4204  # offset
    m_nFogShadows = 4212  # offset
    m_nLightMapUniqueId = 3820  # offset
    m_nLightPathUniqueId = 3816  # offset
    m_nLuminaireShape = 3824  # offset
    m_nPrecomputedSubFrusta = 4304  # offset
    m_nShadowMapSize = 4164  # offset
    m_nShadowPriority = 4168  # offset
    m_vAlternateColor = 4188  # offset
    m_vBakeSpecularToCubemapsSize = 4148  # offset
    m_vPrecomputedBoundsMaxs = 4256  # offset
    m_vPrecomputedBoundsMins = 4244  # offset
    m_vPrecomputedOBBAngles = 4280  # offset
    m_vPrecomputedOBBAngles0 = 4320  # offset
    m_vPrecomputedOBBAngles1 = 4356  # offset
    m_vPrecomputedOBBAngles2 = 4392  # offset
    m_vPrecomputedOBBAngles3 = 4428  # offset
    m_vPrecomputedOBBAngles4 = 4464  # offset
    m_vPrecomputedOBBAngles5 = 4500  # offset
    m_vPrecomputedOBBExtent = 4292  # offset
    m_vPrecomputedOBBExtent0 = 4332  # offset
    m_vPrecomputedOBBExtent1 = 4368  # offset
    m_vPrecomputedOBBExtent2 = 4404  # offset
    m_vPrecomputedOBBExtent3 = 4440  # offset
    m_vPrecomputedOBBExtent4 = 4476  # offset
    m_vPrecomputedOBBExtent5 = 4512  # offset
    m_vPrecomputedOBBOrigin = 4268  # offset
    m_vPrecomputedOBBOrigin0 = 4308  # offset
    m_vPrecomputedOBBOrigin1 = 4344  # offset
    m_vPrecomputedOBBOrigin2 = 4380  # offset
    m_vPrecomputedOBBOrigin3 = 4416  # offset
    m_vPrecomputedOBBOrigin4 = 4452  # offset
    m_vPrecomputedOBBOrigin5 = 4488  # offset
    m_vShear = 4132  # offset
    m_vSizeParams = 4116  # offset

    __metadata__ =     [
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nColorMode",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Color",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flColorTemperature",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flBrightness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flBrightnessScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nDirectLight",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nBakedShadowIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nLightPathUniqueId",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_nLightMapUniqueId",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_nLuminaireShape",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flLuminaireSize",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flLuminaireAnisotropy",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_LightStyleString",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_flLightStyleStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_QueuedLightStyleStrings",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_LightStyleEvents",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_LightStyleTargets",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseModelEntity>"
        },
        {
            "name": "m_hLightCookie",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_flShape",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSoftX",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSoftY",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSkirt",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSkirtNear",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vSizeParams",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_flRange",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vShear",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nBakeSpecularToCubemaps",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vBakeSpecularToCubemapsSize",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nCastShadows",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowMapSize",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nShadowPriority",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bContactShadow",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bForceShadowsEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nBounceLight",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flBounceScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flMinRoughness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vAlternateColor",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_fAlternateColorBrightness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nFog",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFogStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nFogShadows",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFogScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bFogMixedShadows",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flFadeSizeStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeSizeEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowFadeSizeStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flShadowFadeSizeEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bPrecomputedFieldsValid",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vPrecomputedBoundsMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedBoundsMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nPrecomputedSubFrusta",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vPrecomputedOBBOrigin0",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles0",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent0",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin1",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles1",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent1",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin2",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles2",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent2",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin3",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles3",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent3",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin4",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles4",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent4",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBOrigin5",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vPrecomputedOBBAngles5",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_vPrecomputedOBBExtent5",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_VisClusters",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        }
    ]

class C_BaseButton(C_BaseToggle):
    m_glowEntity = 3784  # offset
    m_szDisplayText = 3792  # offset
    m_usable = 3788  # offset

    __metadata__ =     [
        {
            "name": "m_glowEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseModelEntity>"
        },
        {
            "name": "m_usable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_szDisplayText",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class C_BaseCSGrenade(C_CSWeaponBase):
    m_bClientPredictDelete = 8080  # offset
    m_bIsHeldByPlayer = 8082  # offset
    m_bJumpThrow = 8084  # offset
    m_bJustPulledPin = 8224  # offset
    m_bPinPulled = 8083  # offset
    m_bRedraw = 8081  # offset
    m_bThrowAnimating = 8085  # offset
    m_fDropTime = 8216  # offset
    m_fPinPullTime = 8220  # offset
    m_fThrowTime = 8088  # offset
    m_flNextHoldFrac = 8232  # offset
    m_flThrowStrength = 8096  # offset
    m_hSwitchToWeaponAfterThrow = 8236  # offset
    m_nNextHoldTick = 8228  # offset

    __metadata__ =     [
        {
            "name": "m_bRedraw",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsHeldByPlayer",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bPinPulled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bJumpThrow",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bThrowAnimating",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fThrowTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_fDropTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_fPinPullTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bJustPulledPin",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nNextHoldTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_flNextHoldFrac",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_hSwitchToWeaponAfterThrow",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSWeaponBase>"
        }
    ]

class C_BaseCSGrenadeProjectile(C_BaseGrenade):
    flNextTrailLineTime = 5144  # offset
    m_arrTrajectoryTrailPointCreationTimes = 5192  # offset
    m_arrTrajectoryTrailPoints = 5168  # offset
    m_bCanCreateGrenadeTrail = 5149  # offset
    m_bExplodeEffectBegan = 5148  # offset
    m_flSpawnTime = 5128  # offset
    m_flTrajectoryTrailEffectCreationTime = 5216  # offset
    m_hSnapshotTrajectoryParticleSnapshot = 5160  # offset
    m_nBounces = 5096  # offset
    m_nExplodeEffectIndex = 5104  # offset
    m_nExplodeEffectTickBegin = 5112  # offset
    m_nSnapshotTrajectoryEffectIndex = 5152  # offset
    m_vInitialPosition = 5072  # offset
    m_vInitialVelocity = 5084  # offset
    m_vecExplodeEffectOrigin = 5116  # offset
    vecLastTrailLinePos = 5132  # offset

    __metadata__ =     [
        {
            "name": "m_vInitialPosition",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vInitialVelocity",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nBounces",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nExplodeEffectIndex",
            "type": "NetworkVarNames",
            "type_name": "HParticleSystemDefinitionStrong"
        },
        {
            "name": "m_nExplodeEffectTickBegin",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vecExplodeEffectOrigin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_BaseClientUIEntity(C_BaseModelEntity):
    m_DialogXMLName = 3800  # offset
    m_PanelClassName = 3808  # offset
    m_PanelID = 3816  # offset
    m_bEnabled = 3792  # offset

    __metadata__ =     [
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_DialogXMLName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_PanelClassName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_PanelID",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class C_BaseCombatCharacter(C_BaseFlex):
    m_flWaterNextTraceTime = 5028  # offset
    m_flWaterWorldZ = 5024  # offset
    m_hMyWearables = 4992  # offset
    m_leftFootAttachment = 5016  # offset
    m_nWaterWakeMode = 5020  # offset
    m_rightFootAttachment = 5017  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "m_hMyWearables",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_EconWearable>"
        }
    ]

class C_BaseDoor(C_BaseToggle):
    m_bIsUsable = 3784  # offset

    __metadata__ =     [
        {
            "name": "m_bIsUsable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_BaseEntity:
    m_CBodyComponent = 56  # offset
    m_DataChangeEventRef = 1460  # offset
    m_EntClientFlags = 1000  # offset
    m_ListEntry = 968  # offset
    m_MoveCollide = 1316  # offset
    m_MoveType = 1317  # offset
    m_NetworkTransmitComponent = 64  # offset
    m_Particles = 1400  # offset
    m_aThinkFunctions = 920  # offset
    m_bAnimTimeChanged = 1501  # offset
    m_bAnimatedEveryTick = 1352  # offset
    m_bApplyLayerMatchIDToModel = 891  # offset
    m_bClientSideRagdoll = 1002  # offset
    m_bDisabledContextThinks = 944  # offset
    m_bGravityActuallyDisabled = 1384  # offset
    m_bGravityDisabled = 1353  # offset
    m_bHasAddedVarsToInterpolation = 958  # offset
    m_bHasSuccessfullyInterpolated = 957  # offset
    m_bInterpolateEvenWithNoModel = 889  # offset
    m_bPredictable = 1385  # offset
    m_bPredictionEligible = 890  # offset
    m_bRenderEvenWhenNotSuccessfullyInterpolated = 959  # offset
    m_bRenderWithViewModels = 1386  # offset
    m_bSimulationTimeChanged = 1502  # offset
    m_bTakesDamage = 849  # offset
    m_dependencies = 1464  # offset
    m_fBBoxVisFlags = 1376  # offset
    m_fEffects = 1324  # offset
    m_fFlags = 1016  # offset
    m_flActualGravityScale = 1380  # offset
    m_flAnimTime = 948  # offset
    m_flCreateTime = 992  # offset
    m_flElasticity = 1340  # offset
    m_flFriction = 1336  # offset
    m_flGravityScale = 1344  # offset
    m_flNavIgnoreUntilTime = 1356  # offset
    m_flProxyRandomValue = 880  # offset
    m_flSimulationTime = 952  # offset
    m_flSpeed = 996  # offset
    m_flTimeScale = 1348  # offset
    m_flWaterLevel = 1320  # offset
    m_hEffectEntity = 1308  # offset
    m_hGroundEntity = 1328  # offset
    m_hOldMoveParent = 1396  # offset
    m_hOwnerEntity = 1312  # offset
    m_hSceneObjectController = 868  # offset
    m_hThink = 1360  # offset
    m_iCurrentThinkContext = 916  # offset
    m_iEFlags = 884  # offset
    m_iHealth = 844  # offset
    m_iMaxHealth = 840  # offset
    m_iTeamNum = 1003  # offset
    m_lifeState = 848  # offset
    m_nActualMoveType = 1318  # offset
    m_nBloodType = 1520  # offset
    m_nCreationTick = 1488  # offset
    m_nFirstPredictableCommand = 1388  # offset
    m_nGroundBodyIndex = 1332  # offset
    m_nInterpolationLatchDirtyFlags = 960  # offset
    m_nLastPredictableCommand = 1392  # offset
    m_nLastThinkTick = 808  # offset
    m_nNextThinkTick = 1008  # offset
    m_nNoInterpolationTick = 872  # offset
    m_nPlatformType = 864  # offset
    m_nSceneObjectOverrideFlags = 956  # offset
    m_nSimulationTick = 912  # offset
    m_nSubclassID = 896  # offset
    m_nTakeDamageFlags = 856  # offset
    m_nVisibilityNoInterpolationTick = 876  # offset
    m_nWaterType = 888  # offset
    m_pCollision = 832  # offset
    m_pGameSceneNode = 816  # offset
    m_pRenderComponent = 824  # offset
    m_sUniqueHammerID = 1512  # offset
    m_spawnflags = 1004  # offset
    m_tokLayerMatchID = 892  # offset
    m_ubInterpolationFrame = 865  # offset
    m_vecAbsVelocity = 1020  # offset
    m_vecAngVelocity = 1448  # offset
    m_vecBaseVelocity = 1296  # offset
    m_vecServerVelocity = 1032  # offset
    m_vecVelocity = 1072  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_CBodyComponent",
            "type": "NetworkVarNames",
            "type_name": "CBodyComponent::Storage_t"
        },
        {
            "name": "m_iMaxHealth",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_iHealth",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_lifeState",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_bTakesDamage",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nTakeDamageFlags",
            "type": "NetworkVarNames",
            "type_name": "TakeDamageFlags_t"
        },
        {
            "name": "m_nPlatformType",
            "type": "NetworkVarNames",
            "type_name": "EntityPlatformTypes_t"
        },
        {
            "name": "m_ubInterpolationFrame",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nSubclassID",
            "type": "NetworkVarNames",
            "type_name": "EntitySubclassID_t"
        },
        {
            "name": "m_flAnimTime",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flSimulationTime",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flCreateTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bClientSideRagdoll",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iTeamNum",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_spawnflags",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nNextThinkTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_fFlags",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_vecBaseVelocity",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_hEffectEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_hOwnerEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_MoveCollide",
            "type": "NetworkVarNames",
            "type_name": "MoveCollide_t"
        },
        {
            "name": "m_MoveType",
            "type": "NetworkVarNames",
            "type_name": "MoveType_t"
        },
        {
            "name": "m_flWaterLevel",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fEffects",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_hGroundEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_nGroundBodyIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFriction",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flElasticity",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flGravityScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flTimeScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_bAnimatedEveryTick",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bGravityDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flNavIgnoreUntilTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_nBloodType",
            "type": "NetworkVarNames",
            "type_name": "BloodType"
        }
    ]

class C_BaseEntityAPI:
    pass

class C_BaseFlex(CBaseAnimGraph):
    m_CachedViewTarget = 4748  # offset
    m_PhonemeClasses = 4896  # offset
    m_bResetFlexWeightsOnModelChange = 4790  # offset
    m_blinktime = 4768  # offset
    m_blinktoggle = 4648  # offset
    m_flBlinkAmount = 4784  # offset
    m_flJawOpenAmount = 4780  # offset
    m_flexWeight = 4480  # offset
    m_iBlink = 4764  # offset
    m_iEyeAttachment = 4789  # offset
    m_iJawOpen = 4776  # offset
    m_iMouthAttachment = 4788  # offset
    m_mEyeOcclusionRendererCameraToBoneTransform = 4820  # offset
    m_nEyeOcclusionRendererBone = 4816  # offset
    m_nLastFlexUpdateFrameCount = 4744  # offset
    m_nNextSceneEventId = 4760  # offset
    m_prevblinktoggle = 4772  # offset
    m_vEyeOcclusionRendererHalfExtent = 4868  # offset
    m_vLookTargetPosition = 4504  # offset

    __metadata__ =     [
        {
            "name": "m_flexWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_blinktoggle",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_BaseFlex__Emphasized_Phoneme:
    m_bBasechecked = 29  # offset
    m_bRequired = 28  # offset
    m_bValid = 30  # offset
    m_flAmount = 24  # offset
    m_sClassName = 0  # offset

class C_BaseGrenade(C_BaseFlex):
    m_DmgRadius = 4996  # offset
    m_ExplosionSound = 5024  # offset
    m_bHasWarnedAI = 4992  # offset
    m_bIsLive = 4994  # offset
    m_bIsSmokeGrenade = 4993  # offset
    m_flDamage = 5008  # offset
    m_flDetonateTime = 5000  # offset
    m_flNextAttack = 5060  # offset
    m_flWarnAITime = 5004  # offset
    m_hOriginalThrower = 5064  # offset
    m_hThrower = 5036  # offset
    m_iszBounceSound = 5016  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_bIsLive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_DmgRadius",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flDetonateTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flDamage",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_hThrower",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        }
    ]

class C_BaseModelEntity(C_BaseEntity):
    m_CHitboxComponent = 2792  # offset
    m_CRenderComponent = 2784  # offset
    m_ClientOverrideTint = 3712  # offset
    m_Collision = 3088  # offset
    m_ConfigEntitiesToPropagateMaterialDecalsTo = 3416  # offset
    m_Glow = 3264  # offset
    m_LastHitGroup = 2840  # offset
    m_bAllowFadeInView = 2914  # offset
    m_bInitModelEffects = 2896  # offset
    m_bIsStaticProp = 2897  # offset
    m_bNoInterpolate = 3081  # offset
    m_bRenderToCubemaps = 3080  # offset
    m_bUseClientOverrideTint = 3716  # offset
    m_bvDisabledHitGroups = 3776  # offset
    m_clrRender = 2944  # offset
    m_fadeMaxDist = 3360  # offset
    m_fadeMinDist = 3356  # offset
    m_flDecalHealBloodRate = 3404  # offset
    m_flDecalHealHeightRate = 3408  # offset
    m_flFadeScale = 3364  # offset
    m_flGlowBackfaceMult = 3352  # offset
    m_flShadowStrength = 3368  # offset
    m_iOldHealth = 2908  # offset
    m_nAddDecal = 3376  # offset
    m_nDecalMode = 3412  # offset
    m_nDecalsAdded = 2904  # offset
    m_nLastAddDecal = 2900  # offset
    m_nObjectCulling = 3372  # offset
    m_nRenderFX = 2913  # offset
    m_nRenderMode = 2912  # offset
    m_nRequiredDecalMode = 3413  # offset
    m_pClientAlphaProperty = 3704  # offset
    m_pDestructiblePartsSystemComponent = 2832  # offset
    m_sLastDamageSourceName = 2848  # offset
    m_vDecalForwardAxis = 3392  # offset
    m_vDecalPosition = 3380  # offset
    m_vLastDamagePosition = 2856  # offset
    m_vecRenderAttributes = 2952  # offset
    m_vecViewOffset = 3480  # offset

    __metadata__ =     [
        {
            "name": "m_CRenderComponent",
            "type": "NetworkVarNames",
            "type_name": "CRenderComponent::Storage_t"
        },
        {
            "name": "m_CHitboxComponent",
            "type": "NetworkVarNames",
            "type_name": "CHitboxComponent::Storage_t"
        },
        {
            "name": "m_pDestructiblePartsSystemComponent",
            "type": "NetworkVarNames",
            "type_name": "CDestructiblePartsComponent*"
        },
        {
            "name": "m_nRenderMode",
            "type": "NetworkVarNames",
            "type_name": "RenderMode_t"
        },
        {
            "name": "m_nRenderFX",
            "type": "NetworkVarNames",
            "type_name": "RenderFx_t"
        },
        {
            "name": "m_clrRender",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_vecRenderAttributes",
            "type": "NetworkVarNames",
            "type_name": "EntityRenderAttribute_t"
        },
        {
            "name": "m_bRenderToCubemaps",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bNoInterpolate",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Collision",
            "type": "NetworkVarNames",
            "type_name": "CCollisionProperty"
        },
        {
            "name": "m_Glow",
            "type": "NetworkVarNames",
            "type_name": "CGlowProperty"
        },
        {
            "name": "m_flGlowBackfaceMult",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fadeMinDist",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fadeMaxDist",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flShadowStrength",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nObjectCulling",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nAddDecal",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vDecalPosition",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vDecalForwardAxis",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_flDecalHealBloodRate",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDecalHealHeightRate",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nDecalMode",
            "type": "NetworkVarNames",
            "type_name": "DecalMode_t"
        },
        {
            "name": "m_nRequiredDecalMode",
            "type": "NetworkVarNames",
            "type_name": "DecalMode_t"
        },
        {
            "name": "m_ConfigEntitiesToPropagateMaterialDecalsTo",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseModelEntity>"
        },
        {
            "name": "m_bvDisabledHitGroups",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        }
    ]

class C_BasePlayerPawn(C_BaseCombatCharacter):
    m_ServerViewAngleChanges = 5208  # offset
    m_bIsSwappingToPredictableController = 5592  # offset
    m_flDeathTime = 5488  # offset
    m_flFOVSensitivityAdjust = 5552  # offset
    m_flLastCameraSetupTime = 5548  # offset
    m_flMouseSensitivity = 5556  # offset
    m_flOldSimulationTime = 5572  # offset
    m_flPredictionErrorTime = 5504  # offset
    m_hController = 5584  # offset
    m_hDefaultController = 5588  # offset
    m_iHideHUD = 5336  # offset
    m_nLastExecutedCommandNumber = 5576  # offset
    m_nLastExecutedCommandTick = 5580  # offset
    m_pAutoaimServices = 5144  # offset
    m_pCameraServices = 5184  # offset
    m_pFlashlightServices = 5176  # offset
    m_pItemServices = 5136  # offset
    m_pMovementServices = 5192  # offset
    m_pObserverServices = 5152  # offset
    m_pUseServices = 5168  # offset
    m_pWaterServices = 5160  # offset
    m_pWeaponServices = 5128  # offset
    m_skybox3d = 5344  # offset
    m_vOldOrigin = 5560  # offset
    m_vecLastCameraSetupLocalOrigin = 5536  # offset
    m_vecPredictionError = 5492  # offset
    v_angle = 5312  # offset
    v_anglePrevious = 5324  # offset

    __metadata__ =     [
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_pWeaponServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_WeaponServices*"
        },
        {
            "name": "m_pItemServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_ItemServices*"
        },
        {
            "name": "m_pAutoaimServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_AutoaimServices*"
        },
        {
            "name": "m_pObserverServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_ObserverServices*"
        },
        {
            "name": "m_pWaterServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_WaterServices*"
        },
        {
            "name": "m_pUseServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_UseServices*"
        },
        {
            "name": "m_pFlashlightServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_FlashlightServices*"
        },
        {
            "name": "m_pCameraServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_CameraServices*"
        },
        {
            "name": "m_pMovementServices",
            "type": "NetworkVarNames",
            "type_name": "CPlayer_MovementServices*"
        },
        {
            "name": "m_ServerViewAngleChanges",
            "type": "NetworkVarNames",
            "type_name": "ViewAngleServerChange_t"
        },
        {
            "name": "m_iHideHUD",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_skybox3d",
            "type": "NetworkVarNames",
            "type_name": "sky3dparams_t"
        },
        {
            "name": "m_flDeathTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_hController",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerController>"
        },
        {
            "name": "m_hDefaultController",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerController>"
        }
    ]

class C_BasePlayerWeapon(C_EconEntity):
    m_flNextPrimaryAttackTickRatio = 6396  # offset
    m_flNextSecondaryAttackTickRatio = 6404  # offset
    m_iClip1 = 6408  # offset
    m_iClip2 = 6412  # offset
    m_nNextPrimaryAttackTick = 6392  # offset
    m_nNextSecondaryAttackTick = 6400  # offset
    m_pReserveAmmo = 6416  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
        },
        {
            "name": "m_nNextPrimaryAttackTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_flNextPrimaryAttackTickRatio",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nNextSecondaryAttackTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_flNextSecondaryAttackTickRatio",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_iClip1",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_iClip2",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_pReserveAmmo",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_BasePropDoor(C_DynamicProp):
    m_bLocked = 5189  # offset
    m_bNoNPCs = 5190  # offset
    m_closedAngles = 5204  # offset
    m_closedPosition = 5192  # offset
    m_eDoorState = 5184  # offset
    m_hMaster = 5216  # offset
    m_modelChanged = 5188  # offset
    m_vWhereToSetLightingOrigin = 5220  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_eDoorState",
            "type": "NetworkVarNames",
            "type_name": "DoorState_t"
        },
        {
            "name": "m_bLocked",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bNoNPCs",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_closedPosition",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_closedAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_hMaster",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BasePropDoor>"
        }
    ]

class C_BaseToggle(C_BaseModelEntity):
    pass

class C_BaseTrigger(C_BaseToggle):
    m_OnEndTouch = 3864  # offset
    m_OnEndTouchAll = 3904  # offset
    m_OnNotTouching = 4024  # offset
    m_OnStartTouch = 3784  # offset
    m_OnStartTouchAll = 3824  # offset
    m_OnTouching = 3944  # offset
    m_OnTouchingEachEntity = 3984  # offset
    m_bDisabled = 4100  # offset
    m_hFilter = 4096  # offset
    m_hTouchingEntities = 4064  # offset
    m_iFilterName = 4088  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_bDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_Beam(C_BaseModelEntity):
    m_bTurnedOff = 3952  # offset
    m_fAmplitude = 3932  # offset
    m_fEndWidth = 3920  # offset
    m_fFadeLength = 3924  # offset
    m_fHaloScale = 3928  # offset
    m_fSpeed = 3940  # offset
    m_fStartFrame = 3936  # offset
    m_fWidth = 3916  # offset
    m_flDamage = 3796  # offset
    m_flFireTime = 3792  # offset
    m_flFrame = 3944  # offset
    m_flFrameRate = 3784  # offset
    m_flHDRColorScale = 3788  # offset
    m_hAttachEntity = 3864  # offset
    m_hBaseMaterial = 3840  # offset
    m_hEndEntity = 3968  # offset
    m_nAttachIndex = 3904  # offset
    m_nBeamFlags = 3860  # offset
    m_nBeamType = 3856  # offset
    m_nClipStyle = 3948  # offset
    m_nHaloIndex = 3848  # offset
    m_nNumBeamEnts = 3800  # offset
    m_queryHandleHalo = 3804  # offset
    m_vecEndPos = 3956  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "m_flFrameRate",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flHDRColorScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nNumBeamEnts",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_hBaseMaterial",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_nHaloIndex",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_nBeamType",
            "type": "NetworkVarNames",
            "type_name": "BeamType_t"
        },
        {
            "name": "m_nBeamFlags",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_hAttachEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_nAttachIndex",
            "type": "NetworkVarNames",
            "type_name": "AttachmentHandle_t"
        },
        {
            "name": "m_fWidth",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fEndWidth",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fFadeLength",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fHaloScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fAmplitude",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fStartFrame",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fSpeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFrame",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nClipStyle",
            "type": "NetworkVarNames",
            "type_name": "BeamClipStyle_t"
        },
        {
            "name": "m_bTurnedOff",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vecEndPos",
            "type": "NetworkVarNames",
            "type_name": "VectorWS"
        }
    ]

class C_Breakable(C_BaseModelEntity):
    pass

class C_BreakableProp(CBaseProp):
    m_BreakableContentsType = 4776  # offset
    m_CPropDataComponent = 4512  # offset
    m_OnBreak = 4616  # offset
    m_OnHealthChanged = 4656  # offset
    m_OnStartDeath = 4576  # offset
    m_OnTakeDamage = 4696  # offset
    m_PerformanceMode = 4768  # offset
    m_bHasBreakPiecesOrCommands = 4800  # offset
    m_explodeDamage = 4804  # offset
    m_explodeRadius = 4808  # offset
    m_explosionBuildupSound = 4824  # offset
    m_explosionCustomEffect = 4832  # offset
    m_explosionCustomSound = 4840  # offset
    m_explosionDelay = 4816  # offset
    m_explosionModifier = 4848  # offset
    m_flDefBurstScale = 4748  # offset
    m_flDefaultFadeScale = 4864  # offset
    m_flLastPhysicsInfluenceTime = 4860  # offset
    m_flPressureDelay = 4744  # offset
    m_flPreventDamageBeforeTime = 4772  # offset
    m_hBreaker = 4764  # offset
    m_hLastAttacker = 4868  # offset
    m_hPhysicsAttacker = 4856  # offset
    m_iMinHealthDmg = 4740  # offset
    m_impactEnergyScale = 4736  # offset
    m_strBreakableContentsParticleOverride = 4792  # offset
    m_strBreakableContentsPropGroupOverride = 4784  # offset
    m_vDefBurstOffset = 4752  # offset

    __metadata__ =     [
        {
            "name": "m_CPropDataComponent",
            "type": "NetworkVarNames",
            "type_name": "CPropDataComponent::Storage_t"
        }
    ]

class C_BulletHitModel:
    m_bIsHit = 4520  # offset
    m_flTimeCreated = 4524  # offset
    m_hPlayerParent = 4516  # offset
    m_iBoneIndex = 4512  # offset
    m_matLocal = 4464  # offset
    m_vecStartPos = 4528  # offset

class C_C4(C_CSWeaponBase):
    m_activeLightParticleIndex = 8080  # offset
    m_bBombPlacedAnimation = 8096  # offset
    m_bBombPlanted = 8139  # offset
    m_bIsPlantingViaUse = 8097  # offset
    m_bPlayedArmingBeeps = 8132  # offset
    m_bStartedArming = 8088  # offset
    m_eActiveLightEffect = 8084  # offset
    m_entitySpottedState = 8104  # offset
    m_fArmedTime = 8092  # offset
    m_nSpotRules = 8128  # offset

    __metadata__ =     [
        {
            "name": "m_bStartedArming",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fArmedTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bBombPlacedAnimation",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsPlantingViaUse",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_entitySpottedState",
            "type": "NetworkVarNames",
            "type_name": "EntitySpottedState_t"
        }
    ]

class C_CS2HudModelAddon(C_LateUpdatedAnimating):
    pass

class C_CS2HudModelArms(C_CS2HudModelBase):
    pass

class C_CS2HudModelBase(C_LateUpdatedAnimating):
    pass

class C_CS2HudModelWeapon(C_CS2HudModelBase):
    pass

class C_CS2WeaponModuleBase(CBaseAnimGraph):
    pass

class C_CSGO_CounterTerroristTeamIntroCamera(C_CSGO_TeamPreviewCamera):
    pass

class C_CSGO_CounterTerroristWingmanIntroCamera(C_CSGO_TeamPreviewCamera):
    pass

class C_CSGO_EndOfMatchCamera(C_CSGO_TeamPreviewCamera):
    pass

class C_CSGO_EndOfMatchCharacterPosition(C_CSGO_TeamPreviewCharacterPosition):
    pass

class C_CSGO_EndOfMatchLineupEnd(C_CSGO_EndOfMatchLineupEndpoint):
    pass

class C_CSGO_EndOfMatchLineupEndpoint(C_BaseEntity):
    pass

class C_CSGO_EndOfMatchLineupStart(C_CSGO_EndOfMatchLineupEndpoint):
    pass

class C_CSGO_MapPreviewCameraPath(C_BaseEntity):
    m_bConstantSpeed = 1538  # offset
    m_bDofEnabled = 1636  # offset
    m_bLoop = 1536  # offset
    m_bVerticalFOV = 1537  # offset
    m_flDofFarBlurry = 1652  # offset
    m_flDofFarCrisp = 1648  # offset
    m_flDofNearBlurry = 1640  # offset
    m_flDofNearCrisp = 1644  # offset
    m_flDofTiltToGround = 1656  # offset
    m_flDuration = 1540  # offset
    m_flPathDuration = 1612  # offset
    m_flPathLength = 1608  # offset
    m_flZFar = 1528  # offset
    m_flZNear = 1532  # offset

class C_CSGO_MapPreviewCameraPathNode(C_BaseEntity):
    m_flCameraSpeed = 1568  # offset
    m_flEaseIn = 1572  # offset
    m_flEaseOut = 1576  # offset
    m_flFOV = 1564  # offset
    m_nPathIndex = 1536  # offset
    m_szParentPathUniqueID = 1528  # offset
    m_vInTangentLocal = 1540  # offset
    m_vInTangentWorld = 1580  # offset
    m_vOutTangentLocal = 1552  # offset
    m_vOutTangentWorld = 1592  # offset

class C_CSGO_PreviewModel(C_BaseFlex):
    m_animgraph = 4992  # offset
    m_animgraphCharacterModeString = 5000  # offset
    m_defaultAnim = 5008  # offset
    m_flInitialModelScale = 5020  # offset
    m_nDefaultAnimLoopMode = 5016  # offset
    m_sInitialWeaponState = 5024  # offset

class C_CSGO_PreviewModelAlias_csgo_item_previewmodel(C_CSGO_PreviewModel):
    pass

class C_CSGO_PreviewPlayer(C_CSPlayerPawn):
    m_animgraph = 16160  # offset
    m_animgraphCharacterModeString = 16168  # offset
    m_flInitialModelScale = 16176  # offset

class C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel(C_CSGO_PreviewPlayer):
    pass

class C_CSGO_TeamIntroCharacterPosition(C_CSGO_TeamPreviewCharacterPosition):
    pass

class C_CSGO_TeamIntroCounterTerroristPosition(C_CSGO_TeamIntroCharacterPosition):
    pass

class C_CSGO_TeamIntroTerroristPosition(C_CSGO_TeamIntroCharacterPosition):
    pass

class C_CSGO_TeamPreviewCamera(C_CSGO_MapPreviewCameraPath):
    m_nVariant = 1664  # offset

class C_CSGO_TeamPreviewCharacterPosition(C_BaseEntity):
    m_agentItem = 1560  # offset
    m_glovesItem = 2704  # offset
    m_nOrdinal = 1536  # offset
    m_nRandom = 1532  # offset
    m_nVariant = 1528  # offset
    m_sWeaponName = 1544  # offset
    m_weaponItem = 3848  # offset
    m_xuid = 1552  # offset

    __metadata__ =     [
        {
            "name": "m_nVariant",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nRandom",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nOrdinal",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_sWeaponName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_xuid",
            "type": "NetworkVarNames",
            "type_name": "XUID"
        },
        {
            "name": "m_agentItem",
            "type": "NetworkVarNames",
            "type_name": "CEconItemView"
        },
        {
            "name": "m_glovesItem",
            "type": "NetworkVarNames",
            "type_name": "CEconItemView"
        },
        {
            "name": "m_weaponItem",
            "type": "NetworkVarNames",
            "type_name": "CEconItemView"
        }
    ]

class C_CSGO_TeamPreviewModel(C_CSGO_PreviewPlayer):
    pass

class C_CSGO_TeamSelectCamera(C_CSGO_TeamPreviewCamera):
    pass

class C_CSGO_TeamSelectCharacterPosition(C_CSGO_TeamPreviewCharacterPosition):
    pass

class C_CSGO_TeamSelectCounterTerroristPosition(C_CSGO_TeamSelectCharacterPosition):
    pass

class C_CSGO_TeamSelectTerroristPosition(C_CSGO_TeamSelectCharacterPosition):
    pass

class C_CSGO_TerroristTeamIntroCamera(C_CSGO_TeamPreviewCamera):
    pass

class C_CSGO_TerroristWingmanIntroCamera(C_CSGO_TeamPreviewCamera):
    pass

class C_CSGameRules:
    m_MatchDevice = 168  # offset
    m_MinimapVerticalSectionHeights = 3124  # offset
    m_RetakeRules = 3488  # offset
    m_TeamRespawnWaveTimes = 2844  # offset
    m_arrProhibitedItemIndices = 2244  # offset
    m_arrTournamentActiveCasterAccounts = 2444  # offset
    m_bAnyHostageReached = 148  # offset
    m_bBombDropped = 2468  # offset
    m_bBombPlanted = 2469  # offset
    m_bCTCantBuy = 2481  # offset
    m_bCTTimeOutActive = 77  # offset
    m_bFreezePeriod = 64  # offset
    m_bGameRestart = 116  # offset
    m_bHasMatchStarted = 172  # offset
    m_bHasTriggeredRoundStartMusic = 3452  # offset
    m_bIsDroppingItems = 2240  # offset
    m_bIsHltvActive = 2242  # offset
    m_bIsQuestEligible = 2241  # offset
    m_bIsQueuedMatchmaking = 152  # offset
    m_bIsValveDS = 160  # offset
    m_bLogoMap = 161  # offset
    m_bMapHasBombTarget = 149  # offset
    m_bMapHasBuyZone = 151  # offset
    m_bMapHasRescueZone = 150  # offset
    m_bMatchWaitingForResume = 97  # offset
    m_bPlayAllStepSoundsOnServer = 162  # offset
    m_bRoundEndNoMusic = 3836  # offset
    m_bRoundEndShowTimerDefend = 3792  # offset
    m_bSwitchingTeamsAtRoundReset = 3453  # offset
    m_bTCantBuy = 2480  # offset
    m_bTeamIntroPeriod = 3780  # offset
    m_bTechnicalTimeOut = 96  # offset
    m_bTerroristTimeOutActive = 76  # offset
    m_bWarmupPeriod = 65  # offset
    m_eRoundEndReason = 3788  # offset
    m_eRoundWinReason = 2476  # offset
    m_fMatchStartTime = 104  # offset
    m_fRoundStartTime = 108  # offset
    m_fWarmupPeriodEnd = 68  # offset
    m_fWarmupPeriodStart = 72  # offset
    m_flCMMItemDropRevealEndTime = 2236  # offset
    m_flCMMItemDropRevealStartTime = 2232  # offset
    m_flCTTimeOutRemaining = 84  # offset
    m_flGameStartTime = 120  # offset
    m_flLastPerfSampleTime = 20248  # offset
    m_flNextRespawnWave = 2972  # offset
    m_flRestartRoundTime = 112  # offset
    m_flTerroristTimeOutRemaining = 80  # offset
    m_gamePhase = 128  # offset
    m_iHostagesRemaining = 144  # offset
    m_iMatchStats_PlayersAlive_CT = 2604  # offset
    m_iMatchStats_PlayersAlive_T = 2724  # offset
    m_iMatchStats_RoundResults = 2484  # offset
    m_iNumConsecutiveCTLoses = 3252  # offset
    m_iNumConsecutiveTerroristLoses = 3256  # offset
    m_iRoundEndFunFactData1 = 3812  # offset
    m_iRoundEndFunFactData2 = 3816  # offset
    m_iRoundEndFunFactData3 = 3820  # offset
    m_iRoundEndFunFactPlayerSlot = 3808  # offset
    m_iRoundEndLegacy = 3840  # offset
    m_iRoundEndPlayerCount = 3832  # offset
    m_iRoundEndTimerTime = 3796  # offset
    m_iRoundEndWinnerTeam = 3784  # offset
    m_iRoundStartRoundNumber = 3848  # offset
    m_iRoundTime = 100  # offset
    m_iRoundWinStatus = 2472  # offset
    m_iSpectatorSlotCount = 164  # offset
    m_nCTTeamIntroVariant = 3776  # offset
    m_nCTTimeOuts = 92  # offset
    m_nEndMatchMapGroupVoteOptions = 3208  # offset
    m_nEndMatchMapGroupVoteTypes = 3168  # offset
    m_nEndMatchMapVoteWinner = 3248  # offset
    m_nHalloweenMaskListSeed = 2464  # offset
    m_nMatchAbortedEarlyReason = 3448  # offset
    m_nMatchEndCount = 3768  # offset
    m_nNextMapInMapgroup = 176  # offset
    m_nOvertimePlaying = 140  # offset
    m_nQueuedMatchmakingMode = 156  # offset
    m_nRoundEndCount = 3844  # offset
    m_nRoundStartCount = 3852  # offset
    m_nRoundsPlayedThisPhase = 136  # offset
    m_nTTeamIntroVariant = 3772  # offset
    m_nTerroristTimeOuts = 88  # offset
    m_nTournamentPredictionsPct = 2228  # offset
    m_numBestOfMaps = 2460  # offset
    m_pGameModeRules = 3480  # offset
    m_sRoundEndFunFactToken = 3800  # offset
    m_sRoundEndMessage = 3824  # offset
    m_szMatchStatTxt = 1204  # offset
    m_szTournamentEventName = 180  # offset
    m_szTournamentEventStage = 692  # offset
    m_szTournamentPredictionsTxt = 1716  # offset
    m_timeUntilNextPhaseStarts = 124  # offset
    m_totalRoundsPlayed = 132  # offset
    m_ullLocalMatchID = 3160  # offset
    m_vMinimapMaxs = 3112  # offset
    m_vMinimapMins = 3100  # offset

    __metadata__ =     [
        {
            "name": "m_bFreezePeriod",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bWarmupPeriod",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fWarmupPeriodEnd",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_fWarmupPeriodStart",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bTerroristTimeOutActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bCTTimeOutActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flTerroristTimeOutRemaining",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flCTTimeOutRemaining",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nTerroristTimeOuts",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nCTTimeOuts",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bTechnicalTimeOut",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMatchWaitingForResume",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRoundTime",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_fMatchStartTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fRoundStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flRestartRoundTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bGameRestart",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flGameStartTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_timeUntilNextPhaseStarts",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_gamePhase",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_totalRoundsPlayed",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nRoundsPlayedThisPhase",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nOvertimePlaying",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iHostagesRemaining",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bAnyHostageReached",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMapHasBombTarget",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMapHasRescueZone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMapHasBuyZone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsQueuedMatchmaking",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nQueuedMatchmakingMode",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bIsValveDS",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bLogoMap",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bPlayAllStepSoundsOnServer",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iSpectatorSlotCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_MatchDevice",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bHasMatchStarted",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nNextMapInMapgroup",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_szTournamentEventName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_szTournamentEventStage",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_szMatchStatTxt",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_szTournamentPredictionsTxt",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_nTournamentPredictionsPct",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flCMMItemDropRevealStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flCMMItemDropRevealEndTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bIsDroppingItems",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsQuestEligible",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsHltvActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_arrProhibitedItemIndices",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_arrTournamentActiveCasterAccounts",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_numBestOfMaps",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nHalloweenMaskListSeed",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bBombDropped",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bBombPlanted",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRoundWinStatus",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_eRoundWinReason",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bTCantBuy",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bCTCantBuy",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iMatchStats_RoundResults",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMatchStats_PlayersAlive_CT",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMatchStats_PlayersAlive_T",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_TeamRespawnWaveTimes",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flNextRespawnWave",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_vMinimapMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vMinimapMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_MinimapVerticalSectionHeights",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nEndMatchMapGroupVoteTypes",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nEndMatchMapGroupVoteOptions",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nEndMatchMapVoteWinner",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iNumConsecutiveCTLoses",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iNumConsecutiveTerroristLoses",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMatchAbortedEarlyReason",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_pGameModeRules",
            "type": "NetworkVarNames",
            "type_name": "CCSGameModeRules*"
        },
        {
            "name": "m_RetakeRules",
            "type": "NetworkVarNames",
            "type_name": "CRetakeGameRules"
        },
        {
            "name": "m_nMatchEndCount",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nTTeamIntroVariant",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nCTTeamIntroVariant",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bTeamIntroPeriod",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRoundEndWinnerTeam",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_eRoundEndReason",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bRoundEndShowTimerDefend",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRoundEndTimerTime",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_sRoundEndFunFactToken",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_iRoundEndFunFactPlayerSlot",
            "type": "NetworkVarNames",
            "type_name": "CPlayerSlot"
        },
        {
            "name": "m_iRoundEndFunFactData1",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iRoundEndFunFactData2",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iRoundEndFunFactData3",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_sRoundEndMessage",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_iRoundEndPlayerCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bRoundEndNoMusic",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRoundEndLegacy",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nRoundEndCount",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_iRoundStartRoundNumber",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nRoundStartCount",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        }
    ]

class C_CSGameRulesProxy(C_GameRulesProxy):
    m_pGameRules = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_pGameRules",
            "type": "NetworkVarNames",
            "type_name": "C_CSGameRules*"
        }
    ]

class C_CSMinimapBoundary(C_BaseEntity):
    pass

class C_CSObserverPawn(C_CSPlayerPawnBase):
    m_hDetectParentChange = 5760  # offset

    __metadata__ =     [
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        }
    ]

class C_CSPetPlacement(C_BaseEntity):
    pass

class C_CSPlayerPawn(C_CSPlayerPawnBase):
    m_ArmorValue = 10084  # offset
    m_EconGloves = 6336  # offset
    m_GunGameImmunityColor = 9368  # offset
    m_PredictedDamageTags = 10240  # offset
    m_RetakesMVPBoostExtraUtility = 6328  # offset
    m_aimPunchAngle = 5884  # offset
    m_aimPunchAngleVel = 5896  # offset
    m_aimPunchCache = 5920  # offset
    m_aimPunchTickBase = 5908  # offset
    m_aimPunchTickFraction = 5912  # offset
    m_angEyeAngles = 15872  # offset
    m_angEyeAnglesVelocity = 16080  # offset
    m_angShootAngleHistory = 10168  # offset
    m_angStashedShootAngles = 10132  # offset
    m_arrOldEyeAngles = 16032  # offset
    m_arrOldEyeAnglesTimes = 16016  # offset
    m_bCachedPlaneIsValid = 15853  # offset
    m_bClipHitStaticWorld = 15852  # offset
    m_bGrenadeParametersStashed = 10128  # offset
    m_bGunGameImmunity = 15780  # offset
    m_bHasDeathInfo = 10101  # offset
    m_bHasFemaleVoice = 5832  # offset
    m_bInBombZone = 5961  # offset
    m_bInBuyZone = 5880  # offset
    m_bInHostageRescueZone = 5960  # offset
    m_bInLanding = 5952  # offset
    m_bInNoDefuseArea = 10044  # offset
    m_bIsBuyMenuOpen = 5962  # offset
    m_bIsDefusing = 10034  # offset
    m_bIsGrabbingHostage = 10035  # offset
    m_bIsScoped = 10032  # offset
    m_bIsWalking = 9472  # offset
    m_bKilledByHeadshot = 10081  # offset
    m_bLastHeadBoneTransformIsValid = 9240  # offset
    m_bLeftHanded = 9293  # offset
    m_bMustSyncRagdollState = 7481  # offset
    m_bNeedToReApplyGloves = 6333  # offset
    m_bOldIsScoped = 10100  # offset
    m_bOnGroundLastTick = 9248  # offset
    m_bPrevDefuser = 5862  # offset
    m_bPrevHelmet = 5863  # offset
    m_bPreviouslyInBuyZone = 5881  # offset
    m_bRagdollDamageHeadshot = 7576  # offset
    m_bResumeZoom = 10033  # offset
    m_bRetakesHasDefuseKit = 6320  # offset
    m_bRetakesMVPLastRound = 6321  # offset
    m_bShouldAutobuyDMWeapons = 15772  # offset
    m_bSkipOneHeadConstraintUpdate = 9292  # offset
    m_bWaitForNoAttack = 10072  # offset
    m_delayTargetIDTimer = 16096  # offset
    m_entitySpottedState = 10008  # offset
    m_fImmuneToGunGameDamageTime = 15776  # offset
    m_fImmuneToGunGameDamageTimeLast = 15784  # offset
    m_fMolotovDamageTime = 15788  # offset
    m_fRenderingClipPlane = 15808  # offset
    m_fSwitchedHandednessTime = 9296  # offset
    m_flDeathInfoTime = 10104  # offset
    m_flEmitSoundTime = 10040  # offset
    m_flFlinchStack = 10056  # offset
    m_flHealthShotBoostExpirationTime = 5824  # offset
    m_flHitHeading = 10064  # offset
    m_flLandingStartTime = 5956  # offset
    m_flLandingTimeSeconds = 5836  # offset
    m_flLastFiredWeaponTime = 5828  # offset
    m_flNextSprayDecalTime = 5968  # offset
    m_flOldFallVelocity = 5840  # offset
    m_flSlopeDropHeight = 9744  # offset
    m_flSlopeDropOffset = 9624  # offset
    m_flTimeOfLastInjury = 5964  # offset
    m_flVelocityModifier = 10060  # offset
    m_flViewmodelFOV = 9312  # offset
    m_flViewmodelOffsetX = 9300  # offset
    m_flViewmodelOffsetY = 9304  # offset
    m_flViewmodelOffsetZ = 9308  # offset
    m_grenadeParameterStashTime = 10124  # offset
    m_hHudModelArms = 9276  # offset
    m_holdTargetIDTimer = 16128  # offset
    m_iBlockingUseActionInProgress = 10036  # offset
    m_iIDEntIndex = 16092  # offset
    m_iOldIDEntIndex = 16124  # offset
    m_iRetakesMVPBoostItem = 6324  # offset
    m_iRetakesOffering = 6312  # offset
    m_iRetakesOfferingCard = 6316  # offset
    m_iShotsFired = 10052  # offset
    m_iTargetItemEntIdx = 16120  # offset
    m_ignoreLadderJumpTime = 10076  # offset
    m_lastLandTime = 9244  # offset
    m_nEconGlovesChanged = 7480  # offset
    m_nHighestAppliedDamageTagTick = 10348  # offset
    m_nHitBodyPart = 10068  # offset
    m_nLastClipPlaneSetupFrame = 15824  # offset
    m_nLastKillerIndex = 10096  # offset
    m_nPlayerInfernoBodyFx = 15864  # offset
    m_nPrevArmorVal = 5864  # offset
    m_nPrevGrenadeAmmoCount = 5868  # offset
    m_nPrevHighestReceivedDamageTagTick = 10344  # offset
    m_nRagdollDamageBone = 7484  # offset
    m_nWhichBombZone = 10048  # offset
    m_pActionTrackingServices = 5808  # offset
    m_pBulletServices = 5776  # offset
    m_pBuyServices = 5792  # offset
    m_pClippingWeapon = 15856  # offset
    m_pDamageReactServices = 5816  # offset
    m_pGlowServices = 5800  # offset
    m_pHostageServices = 5784  # offset
    m_qDeathEyeAngles = 9280  # offset
    m_szLastPlaceName = 5844  # offset
    m_szRagdollDamageWeaponName = 7512  # offset
    m_thirdPersonHeading = 9480  # offset
    m_unCurrentEquipmentValue = 10088  # offset
    m_unFreezetimeEndEquipmentValue = 10092  # offset
    m_unPreviousWeaponHash = 5872  # offset
    m_unRoundStartEquipmentValue = 10090  # offset
    m_unWeaponHash = 5876  # offset
    m_vHeadConstraintOffset = 9864  # offset
    m_vRagdollDamageForce = 7488  # offset
    m_vRagdollDamagePosition = 7500  # offset
    m_vRagdollServerOrigin = 7580  # offset
    m_vecBulletHitModels = 9448  # offset
    m_vecDeathInfoOrigin = 10108  # offset
    m_vecLastAliveLocalVelocity = 15796  # offset
    m_vecLastClipCameraForward = 15840  # offset
    m_vecLastClipCameraPos = 15828  # offset
    m_vecPlayerPatchEconIndices = 9316  # offset
    m_vecStashedGrenadeThrowPosition = 10144  # offset
    m_vecStashedVelocity = 10156  # offset
    m_vecThrowPositionHistory = 10192  # offset
    m_vecVelocityHistory = 10216  # offset

    __metadata__ =     [
        {
            "name": "m_pBulletServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_BulletServices*"
        },
        {
            "name": "m_pHostageServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_HostageServices*"
        },
        {
            "name": "m_pBuyServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_BuyServices*"
        },
        {
            "name": "m_pGlowServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_GlowServices*"
        },
        {
            "name": "m_pActionTrackingServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_ActionTrackingServices*"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_flHealthShotBoostExpirationTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bHasFemaleVoice",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_szLastPlaceName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_bInBuyZone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_aimPunchAngle",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_aimPunchAngleVel",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_aimPunchTickBase",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_aimPunchTickFraction",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bInHostageRescueZone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bInBombZone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsBuyMenuOpen",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flTimeOfLastInjury",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flNextSprayDecalTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_iRetakesOffering",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iRetakesOfferingCard",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bRetakesHasDefuseKit",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bRetakesMVPLastRound",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRetakesMVPBoostItem",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_RetakesMVPBoostExtraUtility",
            "type": "NetworkVarNames",
            "type_name": "loadout_slot_t"
        },
        {
            "name": "m_EconGloves",
            "type": "NetworkVarNames",
            "type_name": "CEconItemView"
        },
        {
            "name": "m_nEconGlovesChanged",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nRagdollDamageBone",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vRagdollDamageForce",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vRagdollDamagePosition",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_szRagdollDamageWeaponName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_bRagdollDamageHeadshot",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vRagdollServerOrigin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "MNetworkReplayCompatField",
            "type": "Unknown"
        },
        {
            "name": "m_qDeathEyeAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_bLeftHanded",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fSwitchedHandednessTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flViewmodelOffsetX",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flViewmodelOffsetY",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flViewmodelOffsetZ",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flViewmodelFOV",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vecPlayerPatchEconIndices",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_GunGameImmunityColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_bIsWalking",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_entitySpottedState",
            "type": "NetworkVarNames",
            "type_name": "EntitySpottedState_t"
        },
        {
            "name": "m_bIsScoped",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bResumeZoom",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsDefusing",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsGrabbingHostage",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iBlockingUseActionInProgress",
            "type": "NetworkVarNames",
            "type_name": "CSPlayerBlockingUseAction_t"
        },
        {
            "name": "m_flEmitSoundTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bInNoDefuseArea",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nWhichBombZone",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iShotsFired",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFlinchStack",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flVelocityModifier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flHitHeading",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nHitBodyPart",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bWaitForNoAttack",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bKilledByHeadshot",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_ArmorValue",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_unCurrentEquipmentValue",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_unRoundStartEquipmentValue",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_unFreezetimeEndEquipmentValue",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_nLastKillerIndex",
            "type": "NetworkVarNames",
            "type_name": "CEntityIndex"
        },
        {
            "name": "m_PredictedDamageTags",
            "type": "NetworkVarNames",
            "type_name": "PredictedDamageTag_t"
        },
        {
            "name": "m_fImmuneToGunGameDamageTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bGunGameImmunity",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fMolotovDamageTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_CSPlayerPawnBase(C_BasePlayerPawn):
    m_bDeferStartMusicOnWarmup = 5700  # offset
    m_bFlashBuildUp = 5664  # offset
    m_bFlashDspHasBeenCleared = 5665  # offset
    m_bFlashScreenshotHasBeenGrabbed = 5666  # offset
    m_bHasMovedSinceSpawn = 5632  # offset
    m_fNextThinkPushAway = 5684  # offset
    m_flClientDeathTime = 5648  # offset
    m_flClientHealthFadeChangeTimestamp = 5676  # offset
    m_flCurrentMusicStartTime = 5692  # offset
    m_flFlashBangTime = 5652  # offset
    m_flFlashDuration = 5672  # offset
    m_flFlashMaxAlpha = 5668  # offset
    m_flFlashOverlayAlpha = 5660  # offset
    m_flFlashScreenshotAlpha = 5656  # offset
    m_flLastSmokeAge = 5708  # offset
    m_flLastSmokeOverlayAlpha = 5704  # offset
    m_flLastSpawnTimeIndex = 5636  # offset
    m_flMusicRoundStartTime = 5696  # offset
    m_flProgressBarStartTime = 5644  # offset
    m_hOriginalController = 5752  # offset
    m_iPlayerState = 5628  # offset
    m_iProgressBarDuration = 5640  # offset
    m_nClientHealthFadeParityValue = 5680  # offset
    m_pPingServices = 5616  # offset
    m_previousPlayerState = 5624  # offset
    m_vLastSmokeOverlayColor = 5712  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_pPingServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_PingServices*"
        },
        {
            "name": "m_iPlayerState",
            "type": "NetworkVarNames",
            "type_name": "CSPlayerState"
        },
        {
            "name": "m_bHasMovedSinceSpawn",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iProgressBarDuration",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flProgressBarStartTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFlashMaxAlpha",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFlashDuration",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_hOriginalController",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerController>"
        }
    ]

class C_CSPlayerResource(C_BaseEntity):
    m_bEndMatchNextMapAllVoted = 1672  # offset
    m_bHostageAlive = 1528  # offset
    m_bombsiteCenterA = 1600  # offset
    m_bombsiteCenterB = 1612  # offset
    m_foundGoalPositions = 1673  # offset
    m_hostageRescueX = 1624  # offset
    m_hostageRescueY = 1640  # offset
    m_hostageRescueZ = 1656  # offset
    m_iHostageEntityIDs = 1552  # offset
    m_isHostageFollowingSomeone = 1540  # offset

    __metadata__ =     [
        {
            "name": "m_bHostageAlive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_isHostageFollowingSomeone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iHostageEntityIDs",
            "type": "NetworkVarNames",
            "type_name": "CEntityIndex"
        },
        {
            "name": "m_bombsiteCenterA",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bombsiteCenterB",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_hostageRescueX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_hostageRescueY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_hostageRescueZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bEndMatchNextMapAllVoted",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_CSTeam(C_Team):
    m_bSurrendered = 2228  # offset
    m_iClanID = 2376  # offset
    m_numMapVictories = 2224  # offset
    m_scoreFirstHalf = 2232  # offset
    m_scoreOvertime = 2240  # offset
    m_scoreSecondHalf = 2236  # offset
    m_szClanTeamname = 2244  # offset
    m_szTeamFlagImage = 2380  # offset
    m_szTeamLogoImage = 2388  # offset
    m_szTeamMatchStat = 1712  # offset

    __metadata__ =     [
        {
            "name": "m_szTeamMatchStat",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_numMapVictories",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bSurrendered",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_scoreFirstHalf",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_scoreSecondHalf",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_scoreOvertime",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_szClanTeamname",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_iClanID",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_szTeamFlagImage",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_szTeamLogoImage",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class C_CSWeaponBase(C_BasePlayerWeapon):
    m_IronSightController = 7328  # offset
    m_OnPlayerPickup = 6600  # offset
    m_bBurstMode = 6684  # offset
    m_bClearWeaponIdentifyingUGC = 6888  # offset
    m_bDroppedNearBuyZone = 6724  # offset
    m_bFireOnEmpty = 6596  # offset
    m_bInReload = 6700  # offset
    m_bInspectPending = 6540  # offset
    m_bInspectShouldLoop = 6541  # offset
    m_bIsHauledBack = 6708  # offset
    m_bSilencerOn = 6709  # offset
    m_bUIWeapon = 6890  # offset
    m_bVisualsDataSet = 6889  # offset
    m_bWasActiveWeaponWhenDropped = 6916  # offset
    m_bWasOwnedByCT = 6956  # offset
    m_bWasOwnedByTerrorist = 6957  # offset
    m_donated = 6948  # offset
    m_fAccuracyPenalty = 6664  # offset
    m_fAccuracySmoothedForZoom = 6672  # offset
    m_fLastShotTime = 6952  # offset
    m_flCrosshairDistance = 6584  # offset
    m_flDroppedAtTime = 6704  # offset
    m_flInspectCancelCompleteTime = 6536  # offset
    m_flLastAccuracyUpdateTime = 6668  # offset
    m_flLastBurstModeChangeTime = 6688  # offset
    m_flLastLOSTraceFailureTime = 7528  # offset
    m_flLastShakeTime = 7644  # offset
    m_flNextAttackRenderTimeOffset = 6728  # offset
    m_flNextClientFireBulletTime = 6960  # offset
    m_flNextClientFireBulletTime_Repredict = 6964  # offset
    m_flPostponeFireReadyFrac = 6696  # offset
    m_flRecoilIndex = 6680  # offset
    m_flTimeSilencerSwitchComplete = 6712  # offset
    m_flTurningInaccuracy = 6660  # offset
    m_flTurningInaccuracyDelta = 6644  # offset
    m_flWatTickOffset = 7624  # offset
    m_flWeaponGameplayAnimStateTimestamp = 6532  # offset
    m_hPrevOwner = 6908  # offset
    m_iAmmoLastCheck = 6588  # offset
    m_iIronSightMode = 7504  # offset
    m_iMostRecentTeamNumber = 6720  # offset
    m_iOriginalTeamNumber = 6716  # offset
    m_iRecoilIndex = 6676  # offset
    m_iWeaponGameplayAnimState = 6528  # offset
    m_nCustomEconReloadEventId = 6892  # offset
    m_nDropTick = 6912  # offset
    m_nLastEmptySoundCmdNum = 6592  # offset
    m_nPostponeFireReadyTicks = 6692  # offset
    m_nextPrevOwnerUseTime = 6904  # offset
    m_vecTurningInaccuracyEyeDirLast = 6648  # offset
    m_weaponMode = 6640  # offset

    __metadata__ =     [
        {
            "name": "MNetworkOutOfPVSUpdates",
            "type": "Unknown"
        },
        {
            "name": "m_iWeaponGameplayAnimState",
            "type": "NetworkVarNames",
            "type_name": "WeaponGameplayAnimState"
        },
        {
            "name": "m_flWeaponGameplayAnimStateTimestamp",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flInspectCancelCompleteTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bInspectPending",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bInspectShouldLoop",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_weaponMode",
            "type": "NetworkVarNames",
            "type_name": "CSWeaponMode"
        },
        {
            "name": "m_fAccuracyPenalty",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_iRecoilIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flRecoilIndex",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bBurstMode",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nPostponeFireReadyTicks",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_flPostponeFireReadyFrac",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bInReload",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flDroppedAtTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bIsHauledBack",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bSilencerOn",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flTimeSilencerSwitchComplete",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_iOriginalTeamNumber",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iMostRecentTeamNumber",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bDroppedNearBuyZone",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nextPrevOwnerUseTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_hPrevOwner",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_nDropTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_bWasActiveWeaponWhenDropped",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fLastShotTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_iIronSightMode",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flWatTickOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flLastShakeTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        }
    ]

class C_CSWeaponBaseGun(C_CSWeaponBase):
    m_bNeedsBoltAction = 8109  # offset
    m_iBurstShotsRemaining = 8084  # offset
    m_iSilencerBodygroup = 8088  # offset
    m_inPrecache = 8108  # offset
    m_nRevolverCylinderIdx = 8112  # offset
    m_silencedModelIndex = 8104  # offset
    m_zoomLevel = 8080  # offset

    __metadata__ =     [
        {
            "name": "m_zoomLevel",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iBurstShotsRemaining",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bNeedsBoltAction",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nRevolverCylinderIdx",
            "type": "NetworkVarNames",
            "type_name": "int32"
        }
    ]

class C_Chicken(C_DynamicProp):
    m_AttributeManager = 5192  # offset
    m_bAttributesInitialized = 6432  # offset
    m_bIsPreviewModel = 6440  # offset
    m_hHolidayHatAddon = 5176  # offset
    m_hWaterWakeParticles = 6436  # offset
    m_jumpedThisFrame = 5180  # offset
    m_leader = 5184  # offset

    __metadata__ =     [
        {
            "name": "m_jumpedThisFrame",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_leader",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_AttributeManager",
            "type": "NetworkVarNames",
            "type_name": "CAttributeContainer"
        }
    ]

class C_ClientRagdoll(CBaseAnimGraph):
    m_bFadeOut = 4464  # offset
    m_bFadingOut = 4494  # offset
    m_bImportant = 4465  # offset
    m_bReleaseRagdoll = 4492  # offset
    m_flEffectTime = 4468  # offset
    m_flScaleEnd = 4496  # offset
    m_flScaleTimeEnd = 4576  # offset
    m_flScaleTimeStart = 4536  # offset
    m_gibDespawnTime = 4472  # offset
    m_iCurrentFriction = 4476  # offset
    m_iEyeAttachment = 4493  # offset
    m_iFrictionAnimState = 4488  # offset
    m_iMaxFriction = 4484  # offset
    m_iMinFriction = 4480  # offset

class C_ColorCorrection(C_BaseEntity):
    m_MaxFalloff = 1544  # offset
    m_MinFalloff = 1540  # offset
    m_bClientSide = 2078  # offset
    m_bEnabled = 2076  # offset
    m_bEnabledOnClient = 2080  # offset
    m_bExclusive = 2079  # offset
    m_bFadingIn = 2088  # offset
    m_bMaster = 2077  # offset
    m_flCurWeight = 1560  # offset
    m_flCurWeightOnClient = 2084  # offset
    m_flFadeDuration = 2100  # offset
    m_flFadeInDuration = 1548  # offset
    m_flFadeOutDuration = 1552  # offset
    m_flFadeStartTime = 2096  # offset
    m_flFadeStartWeight = 2092  # offset
    m_flMaxWeight = 1556  # offset
    m_netlookupFilename = 1564  # offset
    m_vecOrigin = 1528  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "m_MinFalloff",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_MaxFalloff",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeInDuration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeOutDuration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flMaxWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flCurWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_netlookupFilename",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMaster",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bClientSide",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bExclusive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_ColorCorrectionVolume(C_BaseTrigger):
    m_FadeDuration = 4128  # offset
    m_LastEnterTime = 4108  # offset
    m_LastEnterWeight = 4104  # offset
    m_LastExitTime = 4116  # offset
    m_LastExitWeight = 4112  # offset
    m_MaxWeight = 4124  # offset
    m_Weight = 4132  # offset
    m_bEnabled = 4120  # offset
    m_lookupFilename = 4136  # offset

    __metadata__ =     [
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_MaxWeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_FadeDuration",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Weight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_lookupFilename",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class C_CsmFovOverride(C_BaseEntity):
    m_cameraName = 1528  # offset
    m_flCsmFovOverrideValue = 1536  # offset

class C_DEagle(C_CSWeaponBaseGun):
    pass

class C_DecoyGrenade(C_BaseCSGrenade):
    pass

class C_DecoyProjectile(C_BaseCSGrenadeProjectile):
    m_flTimeParticleEffectSpawn = 5264  # offset
    m_nClientLastKnownDecoyShotTick = 5228  # offset
    m_nDecoyShotTick = 5224  # offset

    __metadata__ =     [
        {
            "name": "m_nDecoyShotTick",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_DynamicLight(C_BaseModelEntity):
    m_Exponent = 3792  # offset
    m_Flags = 3784  # offset
    m_InnerAngle = 3796  # offset
    m_LightStyle = 3785  # offset
    m_OuterAngle = 3800  # offset
    m_Radius = 3788  # offset
    m_SpotRadius = 3804  # offset

    __metadata__ =     [
        {
            "name": "m_Flags",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_LightStyle",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_Radius",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_Exponent",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_InnerAngle",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_OuterAngle",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_SpotRadius",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class C_DynamicProp(C_BreakableProp):
    m_OnAnimReachedEnd = 5048  # offset
    m_OnAnimReachedStart = 5008  # offset
    m_bCreateNonSolid = 5104  # offset
    m_bFiredStartEndOutput = 5102  # offset
    m_bForceNpcExclude = 5103  # offset
    m_bIsOverrideProp = 5105  # offset
    m_bRandomizeCycle = 5100  # offset
    m_bStartDisabled = 5101  # offset
    m_bUseAnimGraph = 4881  # offset
    m_bUseHitboxesForRenderBox = 4880  # offset
    m_glowColor = 5120  # offset
    m_iCachedFrameCount = 5128  # offset
    m_iInitialGlowState = 5108  # offset
    m_iszIdleAnim = 5088  # offset
    m_nGlowRange = 5112  # offset
    m_nGlowRangeMin = 5116  # offset
    m_nGlowTeam = 5124  # offset
    m_nIdleAnimLoopMode = 5096  # offset
    m_pOutputAnimBegun = 4888  # offset
    m_pOutputAnimLoopCycleOver = 4968  # offset
    m_pOutputAnimOver = 4928  # offset
    m_vecCachedRenderMaxs = 5144  # offset
    m_vecCachedRenderMins = 5132  # offset

    __metadata__ =     [
        {
            "name": "m_bUseHitboxesForRenderBox",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bUseAnimGraph",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_DynamicPropAlias_cable_dynamic(C_DynamicProp):
    pass

class C_DynamicPropAlias_dynamic_prop(C_DynamicProp):
    pass

class C_DynamicPropAlias_prop_dynamic_override(C_DynamicProp):
    pass

class C_EconEntity(C_BaseFlex):
    m_AttributeManager = 5032  # offset
    m_OriginalOwnerXuidHigh = 6276  # offset
    m_OriginalOwnerXuidLow = 6272  # offset
    m_bAttachmentDirty = 6336  # offset
    m_bAttributesInitialized = 5024  # offset
    m_bClientside = 6296  # offset
    m_bParticleSystemsCreated = 6297  # offset
    m_flFallbackWear = 6288  # offset
    m_flFlexDelayTime = 5008  # offset
    m_flFlexDelayedWeight = 5016  # offset
    m_hOldProvidee = 6360  # offset
    m_hViewmodelAttachment = 6328  # offset
    m_iNumOwnerValidationRetries = 6344  # offset
    m_iOldTeam = 6332  # offset
    m_nFallbackPaintKit = 6280  # offset
    m_nFallbackSeed = 6284  # offset
    m_nFallbackStatTrak = 6292  # offset
    m_nUnloadedModelIndex = 6340  # offset
    m_vecAttachedModels = 6368  # offset
    m_vecAttachedParticles = 6304  # offset

    __metadata__ =     [
        {
            "name": "m_AttributeManager",
            "type": "NetworkVarNames",
            "type_name": "CAttributeContainer"
        },
        {
            "name": "m_OriginalOwnerXuidLow",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_OriginalOwnerXuidHigh",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nFallbackPaintKit",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nFallbackSeed",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFallbackWear",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nFallbackStatTrak",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_EconEntity__AttachedModelData_t:
    m_iModelDisplayFlags = 0  # offset

class C_EconItemView:
    m_AttributeList = 528  # offset
    m_NetworkedDynamicAttributes = 648  # offset
    m_bDisallowSOC = 489  # offset
    m_bInitialized = 488  # offset
    m_bInitializedTags = 1136  # offset
    m_bInventoryImageRgbaRequested = 96  # offset
    m_bInventoryImageTriedCache = 97  # offset
    m_bIsStoreItem = 490  # offset
    m_bIsTradeItem = 491  # offset
    m_bRestoreCustomMaterialAfterPrecache = 440  # offset
    m_iAccountID = 472  # offset
    m_iEntityLevel = 448  # offset
    m_iEntityQuality = 444  # offset
    m_iEntityQuantity = 492  # offset
    m_iInventoryPosition = 476  # offset
    m_iItemDefinitionIndex = 442  # offset
    m_iItemID = 456  # offset
    m_iItemIDHigh = 464  # offset
    m_iItemIDLow = 468  # offset
    m_iOriginOverride = 504  # offset
    m_iQualityOverride = 500  # offset
    m_iRarityOverride = 496  # offset
    m_nInventoryImageRgbaHeight = 132  # offset
    m_nInventoryImageRgbaWidth = 128  # offset
    m_szCurrentLoadCachedFileName = 136  # offset
    m_szCustomName = 768  # offset
    m_szCustomNameOverride = 929  # offset
    m_ubStyleOverride = 508  # offset
    m_unClientFlags = 509  # offset

    __metadata__ =     [
        {
            "name": "m_iItemDefinitionIndex",
            "type": "NetworkVarNames",
            "type_name": "item_definition_index_t"
        },
        {
            "name": "m_iEntityQuality",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEntityLevel",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iItemIDHigh",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iItemIDLow",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iAccountID",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iInventoryPosition",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_bInitialized",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_AttributeList",
            "type": "NetworkVarNames",
            "type_name": "CAttributeList"
        },
        {
            "name": "m_NetworkedDynamicAttributes",
            "type": "NetworkVarNames",
            "type_name": "CAttributeList"
        },
        {
            "name": "m_szCustomName",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class C_EconWearable(C_EconEntity):
    m_bAlwaysAllow = 6396  # offset
    m_nForceSkin = 6392  # offset

class C_EntityDissolve(C_BaseModelEntity):
    m_bCoreExplode = 3844  # offset
    m_bLinkedToServerEnt = 3845  # offset
    m_flFadeInLength = 3800  # offset
    m_flFadeInStart = 3796  # offset
    m_flFadeOutLength = 3816  # offset
    m_flFadeOutModelLength = 3808  # offset
    m_flFadeOutModelStart = 3804  # offset
    m_flFadeOutStart = 3812  # offset
    m_flNextSparkTime = 3820  # offset
    m_flStartTime = 3792  # offset
    m_nDissolveType = 3824  # offset
    m_nMagnitude = 3840  # offset
    m_vDissolverOrigin = 3828  # offset

    __metadata__ =     [
        {
            "name": "m_flStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flFadeInStart",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeInLength",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeOutModelStart",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeOutModelLength",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeOutStart",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeOutLength",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nDissolveType",
            "type": "NetworkVarNames",
            "type_name": "EntityDisolveType_t"
        },
        {
            "name": "m_vDissolverOrigin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nMagnitude",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        }
    ]

class C_EntityFlame(C_BaseEntity):
    m_bCheapEffect = 1572  # offset
    m_hEntAttached = 1528  # offset
    m_hOldAttached = 1568  # offset

    __metadata__ =     [
        {
            "name": "m_hEntAttached",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseEntity>"
        },
        {
            "name": "m_bCheapEffect",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvCombinedLightProbeVolume(C_BaseEntity):
    m_Entity_Color = 5744  # offset
    m_Entity_bCustomCubemapTexture = 5760  # offset
    m_Entity_bEnabled = 5945  # offset
    m_Entity_bMoveable = 5864  # offset
    m_Entity_bStartDisabled = 5880  # offset
    m_Entity_flBrightness = 5748  # offset
    m_Entity_flEdgeFadeDist = 5884  # offset
    m_Entity_hCubemapTexture = 5752  # offset
    m_Entity_hLightProbeDirectLightIndicesTexture = 5816  # offset
    m_Entity_hLightProbeDirectLightScalarsTexture = 5824  # offset
    m_Entity_hLightProbeDirectLightShadowsTexture = 5832  # offset
    m_Entity_hLightProbeTexture_AmbientCube = 5768  # offset
    m_Entity_hLightProbeTexture_SDF = 5776  # offset
    m_Entity_hLightProbeTexture_SH2_B = 5808  # offset
    m_Entity_hLightProbeTexture_SH2_DC = 5784  # offset
    m_Entity_hLightProbeTexture_SH2_G = 5800  # offset
    m_Entity_hLightProbeTexture_SH2_R = 5792  # offset
    m_Entity_nEnvCubeMapArrayIndex = 5872  # offset
    m_Entity_nHandshake = 5868  # offset
    m_Entity_nLightProbeAtlasX = 5912  # offset
    m_Entity_nLightProbeAtlasY = 5916  # offset
    m_Entity_nLightProbeAtlasZ = 5920  # offset
    m_Entity_nLightProbeSizeX = 5900  # offset
    m_Entity_nLightProbeSizeY = 5904  # offset
    m_Entity_nLightProbeSizeZ = 5908  # offset
    m_Entity_nPriority = 5876  # offset
    m_Entity_vBoxMaxs = 5852  # offset
    m_Entity_vBoxMins = 5840  # offset
    m_Entity_vEdgeFadeDists = 5888  # offset

    __metadata__ =     [
        {
            "name": "m_Entity_Color",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_Entity_flBrightness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Entity_hCubemapTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_bCustomCubemapTexture",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_hLightProbeTexture_AmbientCube",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SDF",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_DC",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_R",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_G",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_B",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeDirectLightIndicesTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeDirectLightScalarsTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeDirectLightShadowsTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_vBoxMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_vBoxMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_bMoveable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_nHandshake",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nEnvCubeMapArrayIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nPriority",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_flEdgeFadeDist",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Entity_vEdgeFadeDists",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_nLightProbeSizeX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeSizeY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeSizeZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeAtlasX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeAtlasY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeAtlasZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume(C_EnvCombinedLightProbeVolume):
    pass

class C_EnvCubemap(C_BaseEntity):
    m_Entity_bCopyDiffuseFromDefaultCubemap = 1736  # offset
    m_Entity_bCustomCubemapTexture = 1664  # offset
    m_Entity_bDefaultEnvMap = 1733  # offset
    m_Entity_bDefaultSpecEnvMap = 1734  # offset
    m_Entity_bEnabled = 1752  # offset
    m_Entity_bIndoorCubeMap = 1735  # offset
    m_Entity_bMoveable = 1696  # offset
    m_Entity_bStartDisabled = 1732  # offset
    m_Entity_flDiffuseScale = 1728  # offset
    m_Entity_flEdgeFadeDist = 1712  # offset
    m_Entity_flInfluenceRadius = 1668  # offset
    m_Entity_hCubemapTexture = 1656  # offset
    m_Entity_nEnvCubeMapArrayIndex = 1704  # offset
    m_Entity_nHandshake = 1700  # offset
    m_Entity_nPriority = 1708  # offset
    m_Entity_vBoxProjectMaxs = 1684  # offset
    m_Entity_vBoxProjectMins = 1672  # offset
    m_Entity_vEdgeFadeDists = 1716  # offset

    __metadata__ =     [
        {
            "name": "m_Entity_hCubemapTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_bCustomCubemapTexture",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_flInfluenceRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Entity_vBoxProjectMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_vBoxProjectMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_bMoveable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_nHandshake",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nEnvCubeMapArrayIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nPriority",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_flEdgeFadeDist",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Entity_vEdgeFadeDists",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_flDiffuseScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Entity_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_bDefaultEnvMap",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_bDefaultSpecEnvMap",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_bIndoorCubeMap",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_bCopyDiffuseFromDefaultCubemap",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvCubemapBox(C_EnvCubemap):
    pass

class C_EnvCubemapFog(C_BaseEntity):
    m_bActive = 1564  # offset
    m_bFirstTime = 1601  # offset
    m_bHasHeightFogEnd = 1600  # offset
    m_bHeightFogEnabled = 1540  # offset
    m_bStartDisabled = 1565  # offset
    m_flEndDistance = 1528  # offset
    m_flFogFalloffExponent = 1536  # offset
    m_flFogHeightEnd = 1548  # offset
    m_flFogHeightExponent = 1556  # offset
    m_flFogHeightStart = 1552  # offset
    m_flFogHeightWidth = 1544  # offset
    m_flFogMaxOpacity = 1568  # offset
    m_flLODBias = 1560  # offset
    m_flStartDistance = 1532  # offset
    m_hFogCubemapTexture = 1592  # offset
    m_hSkyMaterial = 1576  # offset
    m_iszSkyEntity = 1584  # offset
    m_nCubemapSourceType = 1572  # offset

    __metadata__ =     [
        {
            "name": "m_flEndDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flStartDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogFalloffExponent",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bHeightFogEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flFogHeightWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogHeightEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogHeightStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogHeightExponent",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flLODBias",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flFogMaxOpacity",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nCubemapSourceType",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_hSkyMaterial",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_iszSkyEntity",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_hFogCubemapTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_bHasHeightFogEnd",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvDecal(C_BaseModelEntity):
    m_bProjectOnCharacters = 3809  # offset
    m_bProjectOnWater = 3810  # offset
    m_bProjectOnWorld = 3808  # offset
    m_flDepth = 3800  # offset
    m_flDepthSortBias = 3812  # offset
    m_flHeight = 3796  # offset
    m_flWidth = 3792  # offset
    m_hDecalMaterial = 3784  # offset
    m_nRenderOrder = 3804  # offset

    __metadata__ =     [
        {
            "name": "m_hDecalMaterial",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_flWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDepth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nRenderOrder",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_bProjectOnWorld",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bProjectOnCharacters",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bProjectOnWater",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flDepthSortBias",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_EnvDetailController(C_BaseEntity):
    m_flFadeEndDist = 1532  # offset
    m_flFadeStartDist = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_flFadeStartDist",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFadeEndDist",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class C_EnvLightProbeVolume(C_BaseEntity):
    m_Entity_bEnabled = 5761  # offset
    m_Entity_bMoveable = 5712  # offset
    m_Entity_bStartDisabled = 5724  # offset
    m_Entity_hLightProbeDirectLightIndicesTexture = 5664  # offset
    m_Entity_hLightProbeDirectLightScalarsTexture = 5672  # offset
    m_Entity_hLightProbeDirectLightShadowsTexture = 5680  # offset
    m_Entity_hLightProbeTexture_AmbientCube = 5616  # offset
    m_Entity_hLightProbeTexture_SDF = 5624  # offset
    m_Entity_hLightProbeTexture_SH2_B = 5656  # offset
    m_Entity_hLightProbeTexture_SH2_DC = 5632  # offset
    m_Entity_hLightProbeTexture_SH2_G = 5648  # offset
    m_Entity_hLightProbeTexture_SH2_R = 5640  # offset
    m_Entity_nHandshake = 5716  # offset
    m_Entity_nLightProbeAtlasX = 5740  # offset
    m_Entity_nLightProbeAtlasY = 5744  # offset
    m_Entity_nLightProbeAtlasZ = 5748  # offset
    m_Entity_nLightProbeSizeX = 5728  # offset
    m_Entity_nLightProbeSizeY = 5732  # offset
    m_Entity_nLightProbeSizeZ = 5736  # offset
    m_Entity_nPriority = 5720  # offset
    m_Entity_vBoxMaxs = 5700  # offset
    m_Entity_vBoxMins = 5688  # offset

    __metadata__ =     [
        {
            "name": "m_Entity_hLightProbeTexture_AmbientCube",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SDF",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_DC",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_R",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_G",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeTexture_SH2_B",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeDirectLightIndicesTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeDirectLightScalarsTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_hLightProbeDirectLightShadowsTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_Entity_vBoxMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_vBoxMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_Entity_bMoveable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_nHandshake",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nPriority",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_Entity_nLightProbeSizeX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeSizeY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeSizeZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeAtlasX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeAtlasY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_nLightProbeAtlasZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_Entity_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvParticleGlow(C_ParticleSystem):
    m_ColorTint = 5252  # offset
    m_flAlphaScale = 5240  # offset
    m_flRadiusScale = 5244  # offset
    m_flSelfIllumScale = 5248  # offset
    m_hTextureOverride = 5256  # offset

    __metadata__ =     [
        {
            "name": "m_flAlphaScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flRadiusScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flSelfIllumScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_ColorTint",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_hTextureOverride",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        }
    ]

class C_EnvSky(C_BaseModelEntity):
    m_bEnabled = 3836  # offset
    m_bStartDisabled = 3800  # offset
    m_flBrightnessScale = 3812  # offset
    m_flFogMaxEnd = 3832  # offset
    m_flFogMaxStart = 3828  # offset
    m_flFogMinEnd = 3824  # offset
    m_flFogMinStart = 3820  # offset
    m_hSkyMaterial = 3784  # offset
    m_hSkyMaterialLightingOnly = 3792  # offset
    m_nFogType = 3816  # offset
    m_vTintColor = 3801  # offset
    m_vTintColorLightingOnly = 3805  # offset

    __metadata__ =     [
        {
            "name": "m_hSkyMaterial",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_hSkyMaterialLightingOnly",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vTintColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_vTintColorLightingOnly",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flBrightnessScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nFogType",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFogMinStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogMinEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogMaxStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogMaxEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvVolumetricFogController(C_BaseEntity):
    m_TintColor = 1532  # offset
    m_bActive = 1604  # offset
    m_bEnableIndirect = 1645  # offset
    m_bFirstTime = 1696  # offset
    m_bIsMaster = 1646  # offset
    m_bStartDisabled = 1644  # offset
    m_fFirstVolumeSliceThickness = 1564  # offset
    m_fNoiseSpeed = 1660  # offset
    m_fNoiseStrength = 1664  # offset
    m_fWindSpeed = 1680  # offset
    m_flAnisotropy = 1536  # offset
    m_flDefaultAnisotropy = 1632  # offset
    m_flDefaultDrawDistance = 1640  # offset
    m_flDefaultScattering = 1636  # offset
    m_flDrawDistance = 1544  # offset
    m_flFadeInEnd = 1552  # offset
    m_flFadeInStart = 1548  # offset
    m_flFadeSpeed = 1540  # offset
    m_flIndirectStrength = 1556  # offset
    m_flScattering = 1528  # offset
    m_flStartAnisoTime = 1608  # offset
    m_flStartAnisotropy = 1620  # offset
    m_flStartDrawDistance = 1628  # offset
    m_flStartDrawDistanceTime = 1616  # offset
    m_flStartScatterTime = 1612  # offset
    m_flStartScattering = 1624  # offset
    m_hFogIndirectTexture = 1648  # offset
    m_nForceRefreshCount = 1656  # offset
    m_nIndirectTextureDimX = 1568  # offset
    m_nIndirectTextureDimY = 1572  # offset
    m_nIndirectTextureDimZ = 1576  # offset
    m_nVolumeDepth = 1560  # offset
    m_vBoxMaxs = 1592  # offset
    m_vBoxMins = 1580  # offset
    m_vNoiseScale = 1668  # offset
    m_vWindDirection = 1684  # offset

    __metadata__ =     [
        {
            "name": "m_flScattering",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_TintColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flAnisotropy",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDrawDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeInStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeInEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flIndirectStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nVolumeDepth",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_fFirstVolumeSliceThickness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nIndirectTextureDimX",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nIndirectTextureDimY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nIndirectTextureDimZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vBoxMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vBoxMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flStartAnisoTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flStartScatterTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flStartDrawDistanceTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flStartAnisotropy",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flStartScattering",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flStartDrawDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDefaultAnisotropy",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDefaultScattering",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDefaultDrawDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bEnableIndirect",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsMaster",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_hFogIndirectTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_nForceRefreshCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_fNoiseSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fNoiseStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vNoiseScale",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_fWindSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vWindDirection",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_EnvVolumetricFogVolume(C_BaseEntity):
    m_TintColor = 1592  # offset
    m_bActive = 1528  # offset
    m_bIndirectUseLPVs = 1557  # offset
    m_bOverrideIndirectLightStrength = 1597  # offset
    m_bOverrideNoiseStrength = 1599  # offset
    m_bOverrideSunLightStrength = 1598  # offset
    m_bOverrideTintColor = 1596  # offset
    m_bStartDisabled = 1556  # offset
    m_fHeightFogEdgeWidth = 1576  # offset
    m_fIndirectLightStrength = 1580  # offset
    m_fNoiseStrength = 1588  # offset
    m_fSunLightStrength = 1584  # offset
    m_flFalloffExponent = 1568  # offset
    m_flHeightFogDepth = 1572  # offset
    m_flStrength = 1560  # offset
    m_nFalloffShape = 1564  # offset
    m_vBoxMaxs = 1544  # offset
    m_vBoxMins = 1532  # offset

    __metadata__ =     [
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vBoxMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vBoxMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIndirectUseLPVs",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nFalloffShape",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flFalloffExponent",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flHeightFogDepth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fHeightFogEdgeWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fIndirectLightStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fSunLightStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fNoiseStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_TintColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_bOverrideTintColor",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bOverrideIndirectLightStrength",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bOverrideSunLightStrength",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bOverrideNoiseStrength",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvWind(C_BaseEntity):
    m_EnvWindShared = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_EnvWindShared",
            "type": "NetworkVarNames",
            "type_name": "CEnvWindShared"
        }
    ]

class C_EnvWindClientside(C_BaseEntity):
    m_EnvWindShared = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_EnvWindShared",
            "type": "NetworkVarNames",
            "type_name": "CEnvWindShared"
        }
    ]

class C_EnvWindController(C_BaseEntity):
    m_EnvWindShared = 1528  # offset
    m_bFirstTime = 1809  # offset
    m_bIsMaster = 1808  # offset
    m_fDirectionVariation = 1776  # offset
    m_fSpeedVariation = 1780  # offset
    m_fTurbulence = 1784  # offset
    m_fVolumeHalfExtentXY = 1788  # offset
    m_fVolumeHalfExtentZ = 1792  # offset
    m_nClipmapLevels = 1804  # offset
    m_nVolumeResolutionXY = 1796  # offset
    m_nVolumeResolutionZ = 1800  # offset

    __metadata__ =     [
        {
            "name": "m_EnvWindShared",
            "type": "NetworkVarNames",
            "type_name": "CEnvWindShared"
        },
        {
            "name": "m_fDirectionVariation",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fSpeedVariation",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fTurbulence",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fVolumeHalfExtentXY",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fVolumeHalfExtentZ",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nVolumeResolutionXY",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nVolumeResolutionZ",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nClipmapLevels",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bIsMaster",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_EnvWindShared:
    m_flGustDuration = 36  # offset
    m_flInitialWindSpeed = 44  # offset
    m_flMaxGustDelay = 32  # offset
    m_flMinGustDelay = 28  # offset
    m_flStartTime = 8  # offset
    m_hEntOwner = 60  # offset
    m_iGustDirChange = 40  # offset
    m_iInitialWindDir = 42  # offset
    m_iMaxGust = 26  # offset
    m_iMaxWind = 18  # offset
    m_iMinGust = 24  # offset
    m_iMinWind = 16  # offset
    m_iWindSeed = 12  # offset
    m_location = 48  # offset
    m_windRadius = 20  # offset

    __metadata__ =     [
        {
            "name": "m_flStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_iWindSeed",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_iMinWind",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_iMaxWind",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_windRadius",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_iMinGust",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_iMaxGust",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_flMinGustDelay",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flMaxGustDelay",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flGustDuration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_iGustDirChange",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_iInitialWindDir",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_flInitialWindSpeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_location",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_EnvWindVolume(C_BaseEntity):
    m_bActive = 1528  # offset
    m_bStartDisabled = 1556  # offset
    m_fWindDirectionVariationMultiplier = 1576  # offset
    m_fWindSpeedMultiplier = 1564  # offset
    m_fWindSpeedVariationMultiplier = 1572  # offset
    m_fWindTurbulenceMultiplier = 1568  # offset
    m_nShape = 1560  # offset
    m_vBoxMaxs = 1544  # offset
    m_vBoxMins = 1532  # offset

    __metadata__ =     [
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vBoxMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vBoxMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nShape",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_fWindSpeedMultiplier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fWindTurbulenceMultiplier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fWindSpeedVariationMultiplier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fWindDirectionVariationMultiplier",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_FireCrackerBlast(C_Inferno):
    pass

class C_Fish(CBaseAnimGraph):
    m_actualAngles = 4564  # offset
    m_actualPos = 4552  # offset
    m_angle = 4608  # offset
    m_angles = 4488  # offset
    m_averageError = 4700  # offset
    m_buoyancy = 4512  # offset
    m_deathAngle = 4508  # offset
    m_deathDepth = 4504  # offset
    m_errorHistory = 4612  # offset
    m_errorHistoryCount = 4696  # offset
    m_errorHistoryIndex = 4692  # offset
    m_gotUpdate = 4592  # offset
    m_localLifeState = 4500  # offset
    m_poolOrigin = 4576  # offset
    m_pos = 4464  # offset
    m_vel = 4476  # offset
    m_waterLevel = 4588  # offset
    m_wigglePhase = 4544  # offset
    m_wiggleRate = 4548  # offset
    m_wiggleTimer = 4520  # offset
    m_x = 4596  # offset
    m_y = 4600  # offset
    m_z = 4604  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_poolOrigin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_waterLevel",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_x",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_y",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_z",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_angle",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class C_Flashbang(C_BaseCSGrenade):
    pass

class C_FlashbangProjectile(C_BaseCSGrenadeProjectile):
    pass

class C_FogController(C_BaseEntity):
    m_bUseAngles = 1632  # offset
    m_fog = 1528  # offset
    m_iChangedVariables = 1636  # offset

    __metadata__ =     [
        {
            "name": "m_fog",
            "type": "NetworkVarNames",
            "type_name": "fogparams_t"
        }
    ]

class C_FootstepControl(C_BaseTrigger):
    m_destination = 4112  # offset
    m_source = 4104  # offset

    __metadata__ =     [
        {
            "name": "m_source",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_destination",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class C_FuncBrush(C_BaseModelEntity):
    pass

class C_FuncConveyor(C_BaseModelEntity):
    m_flCurrentConveyorOffset = 3848  # offset
    m_flCurrentConveyorSpeed = 3852  # offset
    m_flTargetSpeed = 3804  # offset
    m_flTransitionStartSpeed = 3816  # offset
    m_hConveyorModels = 3824  # offset
    m_nTransitionDurationTicks = 3812  # offset
    m_nTransitionStartTick = 3808  # offset
    m_vecMoveDirEntitySpace = 3792  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "m_vecMoveDirEntitySpace",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_flTargetSpeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nTransitionStartTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "m_nTransitionDurationTicks",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flTransitionStartSpeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_hConveyorModels",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        }
    ]

class C_FuncElectrifiedVolume(C_FuncBrush):
    m_EffectName = 3792  # offset
    m_bState = 3800  # offset
    m_nAmbientEffect = 3784  # offset

    __metadata__ =     [
        {
            "name": "m_EffectName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_bState",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_FuncLadder(C_BaseModelEntity):
    m_Dismounts = 3800  # offset
    m_bDisabled = 3864  # offset
    m_bFakeLadder = 3865  # offset
    m_bHasSlack = 3866  # offset
    m_flAutoRideSpeed = 3860  # offset
    m_vecLadderDir = 3784  # offset
    m_vecLocalTop = 3824  # offset
    m_vecPlayerMountPositionBottom = 3848  # offset
    m_vecPlayerMountPositionTop = 3836  # offset

    __metadata__ =     [
        {
            "name": "m_vecLadderDir",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecPlayerMountPositionTop",
            "type": "NetworkVarNames",
            "type_name": "VectorWS"
        },
        {
            "name": "m_vecPlayerMountPositionBottom",
            "type": "NetworkVarNames",
            "type_name": "VectorWS"
        },
        {
            "name": "m_flAutoRideSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bFakeLadder",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_FuncMonitor(C_FuncBrush):
    m_bDraw3DSkybox = 3813  # offset
    m_bEnabled = 3812  # offset
    m_bRenderShadows = 3796  # offset
    m_bUseUniqueColorTarget = 3797  # offset
    m_brushModelName = 3800  # offset
    m_hTargetCamera = 3808  # offset
    m_nResolutionEnum = 3792  # offset
    m_targetCamera = 3784  # offset

    __metadata__ =     [
        {
            "name": "m_targetCamera",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_nResolutionEnum",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bRenderShadows",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bUseUniqueColorTarget",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_brushModelName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_hTargetCamera",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        },
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bDraw3DSkybox",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_FuncMoveLinear(C_BaseToggle):
    pass

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        }
    ]

class C_FuncMover(C_BaseToggle):
    pass

class C_FuncRotating(C_BaseModelEntity):
    pass

    __metadata__ =     [
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        }
    ]

class C_FuncTrackTrain(C_BaseModelEntity):
    m_flLineLength = 3792  # offset
    m_flRadius = 3788  # offset
    m_nLongAxis = 3784  # offset

class C_GameRules:
    __m_pChainEntity = 8  # offset
    m_bGamePaused = 56  # offset
    m_nPauseStartTick = 52  # offset
    m_nTotalPausedTicks = 48  # offset

    __metadata__ =     [
        {
            "name": "m_nTotalPausedTicks",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPauseStartTick",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bGamePaused",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_GameRulesProxy(C_BaseEntity):
    pass

class C_GlobalLight(C_BaseEntity):
    m_WindClothForceHandle = 2752  # offset

class C_GradientFog(C_BaseEntity):
    m_bGradientFogNeedsTextures = 1586  # offset
    m_bHeightFogEnabled = 1544  # offset
    m_bIsEnabled = 1585  # offset
    m_bStartDisabled = 1584  # offset
    m_flFadeTime = 1580  # offset
    m_flFarZ = 1556  # offset
    m_flFogEndDistance = 1540  # offset
    m_flFogEndHeight = 1552  # offset
    m_flFogFalloffExponent = 1564  # offset
    m_flFogMaxOpacity = 1560  # offset
    m_flFogStartDistance = 1536  # offset
    m_flFogStartHeight = 1548  # offset
    m_flFogStrength = 1576  # offset
    m_flFogVerticalExponent = 1568  # offset
    m_fogColor = 1572  # offset
    m_hGradientFogTexture = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_hGradientFogTexture",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_flFogStartDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogEndDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bHeightFogEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flFogStartHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogEndHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFarZ",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogMaxOpacity",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogFalloffExponent",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogVerticalExponent",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_fogColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flFogStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_HEGrenade(C_BaseCSGrenade):
    pass

class C_HEGrenadeProjectile(C_BaseCSGrenadeProjectile):
    pass

class C_HandleTest(C_BaseEntity):
    m_Handle = 1528  # offset
    m_bSendHandle = 1532  # offset

    __metadata__ =     [
        {
            "name": "m_Handle",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_bSendHandle",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_Hostage(C_BaseCombatCharacter):
    m_bHandsHaveBeenCut = 5204  # offset
    m_blinkTimer = 5248  # offset
    m_chestAttachment = 5314  # offset
    m_entitySpottedState = 5128  # offset
    m_eyeAttachment = 5313  # offset
    m_fLastGrabTime = 5212  # offset
    m_fNewestAlphaThinkTime = 5328  # offset
    m_flDeadOrRescuedTime = 5240  # offset
    m_flDropStartTime = 5236  # offset
    m_flGrabSuccessTime = 5232  # offset
    m_flRescueStartTime = 5228  # offset
    m_hHostageGrabber = 5208  # offset
    m_isInit = 5312  # offset
    m_isRescued = 5196  # offset
    m_jumpedThisFrame = 5197  # offset
    m_leader = 5152  # offset
    m_lookAroundTimer = 5288  # offset
    m_lookAt = 5272  # offset
    m_nHostageState = 5200  # offset
    m_pPredictionOwner = 5320  # offset
    m_reuseTimer = 5160  # offset
    m_vecGrabbedPos = 5216  # offset
    m_vel = 5184  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkOverride",
            "type": "Unknown"
        },
        {
            "name": "m_entitySpottedState",
            "type": "NetworkVarNames",
            "type_name": "EntitySpottedState_t"
        },
        {
            "name": "m_leader",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_reuseTimer",
            "type": "NetworkVarNames",
            "type_name": "CountdownTimer"
        },
        {
            "name": "m_vel",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_isRescued",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_jumpedThisFrame",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nHostageState",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bHandsHaveBeenCut",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_hHostageGrabber",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_flRescueStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flGrabSuccessTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flDropStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        }
    ]

class C_HostageCarriableProp(CBaseAnimGraph):
    pass

class C_IncendiaryGrenade(C_MolotovGrenade):
    pass

class C_Inferno(C_BaseModelEntity):
    m_BurnNormal = 5496  # offset
    m_bFireIsBurning = 5432  # offset
    m_bInPostEffectTime = 6276  # offset
    m_blosCheck = 33940  # offset
    m_drawableCount = 33936  # offset
    m_fireCount = 6264  # offset
    m_fireParentPositions = 4664  # offset
    m_firePositions = 3896  # offset
    m_flLastGrassBurnThink = 33980  # offset
    m_hInfernoClimbingOutlinePointsSnapshot = 3880  # offset
    m_hInfernoDecalsSnapshot = 3888  # offset
    m_hInfernoFillerPointsSnapshot = 3864  # offset
    m_hInfernoOutlinePointsSnapshot = 3872  # offset
    m_hInfernoPointsSnapshot = 3856  # offset
    m_lastFireCount = 6280  # offset
    m_maxBounds = 33968  # offset
    m_maxFireHalfWidth = 33948  # offset
    m_maxFireHeight = 33952  # offset
    m_minBounds = 33956  # offset
    m_nFireEffectTickBegin = 6284  # offset
    m_nFireLifetime = 6272  # offset
    m_nInfernoType = 6268  # offset
    m_nfxFireDamageEffect = 3848  # offset
    m_nlosperiod = 33944  # offset

    __metadata__ =     [
        {
            "name": "m_firePositions",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_fireParentPositions",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bFireIsBurning",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_BurnNormal",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_fireCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nInfernoType",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nFireLifetime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bInPostEffectTime",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nFireEffectTickBegin",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_InfoInstructorHintHostageRescueZone(C_PointEntity):
    pass

class C_InfoLadderDismount(C_BaseEntity):
    pass

class C_InfoVisibilityBox(C_BaseEntity):
    m_bEnabled = 1548  # offset
    m_nMode = 1532  # offset
    m_vBoxSize = 1536  # offset

    __metadata__ =     [
        {
            "name": "m_nMode",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vBoxSize",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_Item(C_EconEntity):
    m_pReticleHintTextName = 6392  # offset

class C_ItemDogtags(C_Item):
    m_KillingPlayer = 6652  # offset
    m_OwningPlayer = 6648  # offset

    __metadata__ =     [
        {
            "name": "m_OwningPlayer",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_KillingPlayer",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        }
    ]

class C_Item_Healthshot(C_WeaponBaseItem):
    pass

class C_KeychainModule(C_CS2WeaponModuleBase):
    m_nKeychainDefID = 4472  # offset
    m_nKeychainSeed = 4476  # offset

class C_Knife(C_CSWeaponBase):
    m_bFirstAttack = 8080  # offset

    __metadata__ =     [
        {
            "name": "m_bFirstAttack",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_LateUpdatedAnimating(CBaseAnimGraph):
    pass

class C_LightDirectionalEntity(C_LightEntity):
    pass

class C_LightEntity(C_BaseModelEntity):
    m_CLightComponent = 3784  # offset

    __metadata__ =     [
        {
            "name": "m_CLightComponent",
            "type": "NetworkVarNames",
            "type_name": "CLightComponent::Storage_t"
        }
    ]

class C_LightEnvironmentEntity(C_LightDirectionalEntity):
    pass

class C_LightOrthoEntity(C_LightEntity):
    pass

class C_LightSpotEntity(C_LightEntity):
    pass

class C_LocalTempEntity(CBaseAnimGraph):
    bounceFactor = 4488  # offset
    die = 4468  # offset
    fadeSpeed = 4484  # offset
    flags = 4464  # offset
    hitSound = 4492  # offset
    m_bParticleCollision = 4576  # offset
    m_flFrame = 4552  # offset
    m_flFrameMax = 4472  # offset
    m_flFrameRate = 4548  # offset
    m_flSpriteScale = 4540  # offset
    m_iLastCollisionFrame = 4580  # offset
    m_nFlickerFrame = 4544  # offset
    m_pszImpactEffect = 4560  # offset
    m_pszParticleEffect = 4568  # offset
    m_vLastCollisionOrigin = 4584  # offset
    m_vecNormal = 4528  # offset
    m_vecPrevAbsOrigin = 4608  # offset
    m_vecTempEntAcceleration = 4620  # offset
    m_vecTempEntAngVelocity = 4512  # offset
    m_vecTempEntVelocity = 4596  # offset
    priority = 4496  # offset
    tempent_renderamt = 4524  # offset
    tentOffset = 4500  # offset
    x = 4476  # offset
    y = 4480  # offset

class C_MapPreviewParticleSystem(C_ParticleSystem):
    pass

class C_MapVetoPickController(C_BaseEntity):
    m_bDisabledHud = 3900  # offset
    m_nAccountIDs = 1836  # offset
    m_nCurrentPhase = 3884  # offset
    m_nDraftType = 1544  # offset
    m_nMapId0 = 2092  # offset
    m_nMapId1 = 2348  # offset
    m_nMapId2 = 2604  # offset
    m_nMapId3 = 2860  # offset
    m_nMapId4 = 3116  # offset
    m_nMapId5 = 3372  # offset
    m_nPhaseDurationTicks = 3892  # offset
    m_nPhaseStartTick = 3888  # offset
    m_nPostDataUpdateTick = 3896  # offset
    m_nStartingSide0 = 3628  # offset
    m_nTeamWinningCoinToss = 1548  # offset
    m_nTeamWithFirstChoice = 1552  # offset
    m_nVoteMapIdsList = 1808  # offset

    __metadata__ =     [
        {
            "name": "m_nDraftType",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nTeamWinningCoinToss",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nTeamWithFirstChoice",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nVoteMapIdsList",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nAccountIDs",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMapId0",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMapId1",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMapId2",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMapId3",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMapId4",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nMapId5",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nStartingSide0",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nCurrentPhase",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPhaseStartTick",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPhaseDurationTicks",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_ModelPointEntity(C_BaseModelEntity):
    pass

class C_MolotovGrenade(C_BaseCSGrenade):
    pass

class C_MolotovProjectile(C_BaseCSGrenadeProjectile):
    m_bIsIncGrenade = 5224  # offset

    __metadata__ =     [
        {
            "name": "m_bIsIncGrenade",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_Multimeter(CBaseAnimGraph):
    m_hTargetC4 = 4472  # offset

class C_MultiplayRules:
    pass

class C_NametagModule(C_CS2WeaponModuleBase):
    m_strNametagString = 4472  # offset

class C_NetTestBaseCombatCharacter(C_BaseCombatCharacter):
    pass

class C_OmniLight(C_BarnLight):
    m_bShowLight = 4640  # offset
    m_flInnerAngle = 4632  # offset
    m_flOuterAngle = 4636  # offset

    __metadata__ =     [
        {
            "name": "m_flInnerAngle",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flOuterAngle",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bShowLight",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_ParticleSystem(C_BaseModelEntity):
    m_bActive = 4296  # offset
    m_bAnimateDuringGameplayPause = 4308  # offset
    m_bFrozen = 4297  # offset
    m_bNoFreeze = 4637  # offset
    m_bNoRamp = 4638  # offset
    m_bNoSave = 4636  # offset
    m_bOldActive = 5216  # offset
    m_bOldFrozen = 5217  # offset
    m_bStartActive = 4639  # offset
    m_clrTint = 5180  # offset
    m_flFreezeTransitionDuration = 4300  # offset
    m_flPreSimTime = 4324  # offset
    m_flStartTime = 4320  # offset
    m_hControlPointEnts = 4380  # offset
    m_iEffectIndex = 4312  # offset
    m_iServerControlPointAssignments = 4376  # offset
    m_iszControlPointNames = 4648  # offset
    m_iszEffectName = 4640  # offset
    m_nDataCP = 5160  # offset
    m_nStopType = 4304  # offset
    m_nTintCP = 5176  # offset
    m_szSnapshotFileName = 3784  # offset
    m_vServerControlPoints = 4328  # offset
    m_vecDataCPValue = 5164  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_szSnapshotFileName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bFrozen",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flFreezeTransitionDuration",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nStopType",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bAnimateDuringGameplayPause",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iEffectIndex",
            "type": "NetworkVarNames",
            "type_name": "HParticleSystemDefinitionStrong"
        },
        {
            "name": "m_flStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flPreSimTime",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_vServerControlPoints",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_iServerControlPointAssignments",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_hControlPointEnts",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_bNoSave",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bNoFreeze",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bNoRamp",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_PathParticleRope(C_BaseEntity):
    m_ColorTint = 1588  # offset
    m_PathNodes_Color = 1680  # offset
    m_PathNodes_Name = 1552  # offset
    m_PathNodes_PinEnabled = 1704  # offset
    m_PathNodes_Position = 1608  # offset
    m_PathNodes_RadiusScale = 1728  # offset
    m_PathNodes_TangentIn = 1632  # offset
    m_PathNodes_TangentOut = 1656  # offset
    m_bStartActive = 1536  # offset
    m_flMaxSimulationTime = 1540  # offset
    m_flParticleSpacing = 1576  # offset
    m_flRadius = 1584  # offset
    m_flSlack = 1580  # offset
    m_iEffectIndex = 1600  # offset
    m_iszEffectName = 1544  # offset
    m_nEffectState = 1592  # offset

    __metadata__ =     [
        {
            "name": "m_flParticleSpacing",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSlack",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_ColorTint",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_nEffectState",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iEffectIndex",
            "type": "NetworkVarNames",
            "type_name": "HParticleSystemDefinitionStrong"
        },
        {
            "name": "m_PathNodes_Position",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_PathNodes_TangentIn",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_PathNodes_TangentOut",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_PathNodes_Color",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_PathNodes_PinEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_PathNodes_RadiusScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_PathParticleRopeAlias_path_particle_rope_clientside(C_PathParticleRope):
    pass

class C_PhysBox(C_Breakable):
    pass

class C_PhysMagnet(CBaseAnimGraph):
    m_aAttachedObjects = 4488  # offset
    m_aAttachedObjectsFromServer = 4464  # offset

class C_PhysPropClientside(C_BreakableProp):
    m_fDeathTime = 4884  # offset
    m_flTouchDelta = 4880  # offset
    m_nDamageType = 4912  # offset
    m_vecDamageDirection = 4900  # offset
    m_vecDamagePosition = 4888  # offset

class C_PhysicsProp(C_BreakableProp):
    m_bAwake = 4880  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_bAwake",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_PhysicsPropMultiplayer(C_PhysicsProp):
    pass

class C_PlantedC4(CBaseAnimGraph):
    m_AttributeManager = 4568  # offset
    m_bBeingDefused = 4532  # offset
    m_bBombDefused = 4556  # offset
    m_bBombTicking = 4472  # offset
    m_bC4Activated = 4544  # offset
    m_bCannotBeDefused = 4524  # offset
    m_bExplodeWarning = 4540  # offset
    m_bHasExploded = 4525  # offset
    m_bRadarFlash = 5816  # offset
    m_bTenSecWarning = 4545  # offset
    m_bTriggerWarning = 4536  # offset
    m_entitySpottedState = 4488  # offset
    m_fLastDefuseTime = 5824  # offset
    m_flC4Blow = 4520  # offset
    m_flC4ExplodeSpectateDuration = 5864  # offset
    m_flDefuseCountDown = 4552  # offset
    m_flDefuseLength = 4548  # offset
    m_flNextBeep = 4516  # offset
    m_flNextGlow = 4512  # offset
    m_flNextRadarFlashTime = 5812  # offset
    m_flTimerLength = 4528  # offset
    m_hBombDefuser = 4560  # offset
    m_hDefuserMultimeter = 5808  # offset
    m_nBombSite = 4476  # offset
    m_nSourceSoundscapeHash = 4480  # offset
    m_pBombDefuser = 5820  # offset
    m_pPredictionOwner = 5832  # offset
    m_vecC4ExplodeSpectateAng = 5852  # offset
    m_vecC4ExplodeSpectatePos = 5840  # offset

    __metadata__ =     [
        {
            "name": "m_bBombTicking",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nBombSite",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nSourceSoundscapeHash",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_entitySpottedState",
            "type": "NetworkVarNames",
            "type_name": "EntitySpottedState_t"
        },
        {
            "name": "m_flC4Blow",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bCannotBeDefused",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bHasExploded",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flTimerLength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bBeingDefused",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flDefuseLength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDefuseCountDown",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_bBombDefused",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_hBombDefuser",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_AttributeManager",
            "type": "NetworkVarNames",
            "type_name": "CAttributeContainer"
        }
    ]

class C_PlayerPing(C_BaseEntity):
    m_bUrgent = 1588  # offset
    m_hPingedEntity = 1580  # offset
    m_hPlayer = 1576  # offset
    m_iType = 1584  # offset
    m_szPlaceName = 1589  # offset

    __metadata__ =     [
        {
            "name": "m_hPlayer",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        },
        {
            "name": "m_hPingedEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_iType",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bUrgent",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_szPlaceName",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class C_PlayerSprayDecal(C_ModelPointEntity):
    m_SprayRenderHelper = 4008  # offset
    m_flCreationTime = 3860  # offset
    m_nEntity = 3852  # offset
    m_nHitbox = 3856  # offset
    m_nPlayer = 3848  # offset
    m_nTintID = 3864  # offset
    m_nUniqueID = 3784  # offset
    m_nVersion = 3868  # offset
    m_rtGcTime = 3796  # offset
    m_ubSignature = 3869  # offset
    m_unAccountID = 3788  # offset
    m_unTraceID = 3792  # offset
    m_vecEndPos = 3800  # offset
    m_vecLeft = 3824  # offset
    m_vecNormal = 3836  # offset
    m_vecStart = 3812  # offset

    __metadata__ =     [
        {
            "name": "m_nUniqueID",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_unAccountID",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unTraceID",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_rtGcTime",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_vecEndPos",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecStart",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecLeft",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecNormal",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_nPlayer",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nEntity",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nHitbox",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_flCreationTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nTintID",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nVersion",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_ubSignature",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        }
    ]

class C_PlayerVisibility(C_BaseEntity):
    m_bIsEnabled = 1545  # offset
    m_bStartDisabled = 1544  # offset
    m_flFadeTime = 1540  # offset
    m_flFogDistanceMultiplier = 1532  # offset
    m_flFogMaxDensityMultiplier = 1536  # offset
    m_flVisibilityStrength = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_flVisibilityStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogDistanceMultiplier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogMaxDensityMultiplier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFadeTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bStartDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bIsEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_PointCamera(C_BaseEntity):
    m_DegreesPerSecond = 1608  # offset
    m_FOV = 1528  # offset
    m_FogColor = 1537  # offset
    m_Resolution = 1532  # offset
    m_TargetFOV = 1604  # offset
    m_bActive = 1556  # offset
    m_bAlignWithParent = 1581  # offset
    m_bCanHLTVUse = 1580  # offset
    m_bDofEnabled = 1582  # offset
    m_bFogEnable = 1536  # offset
    m_bIsOn = 1612  # offset
    m_bNoSky = 1564  # offset
    m_bUseScreenAspectRatio = 1557  # offset
    m_fBrightness = 1568  # offset
    m_flAspectRatio = 1560  # offset
    m_flDofFarBlurry = 1596  # offset
    m_flDofFarCrisp = 1592  # offset
    m_flDofNearBlurry = 1584  # offset
    m_flDofNearCrisp = 1588  # offset
    m_flDofTiltToGround = 1600  # offset
    m_flFogEnd = 1548  # offset
    m_flFogMaxDensity = 1552  # offset
    m_flFogStart = 1544  # offset
    m_flZFar = 1572  # offset
    m_flZNear = 1576  # offset
    m_pNext = 1616  # offset

    __metadata__ =     [
        {
            "name": "m_FOV",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Resolution",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bFogEnable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_FogColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_flFogStart",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogEnd",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFogMaxDensity",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bUseScreenAspectRatio",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flAspectRatio",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bNoSky",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_fBrightness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flZFar",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flZNear",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bCanHLTVUse",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bAlignWithParent",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bDofEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flDofNearBlurry",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDofNearCrisp",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDofFarCrisp",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDofFarBlurry",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDofTiltToGround",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_PointCameraVFOV(C_PointCamera):
    m_flVerticalFOV = 1624  # offset

class C_PointClientUIDialog(C_BaseClientUIEntity):
    m_bStartEnabled = 3836  # offset
    m_hActivator = 3832  # offset

    __metadata__ =     [
        {
            "name": "m_hActivator",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        }
    ]

class C_PointClientUIHUD(C_BaseClientUIEntity):
    m_bAllowInteractionFromAllSceneWorlds = 4264  # offset
    m_bCheckCSSClasses = 3840  # offset
    m_bIgnoreInput = 4224  # offset
    m_flDPI = 4236  # offset
    m_flDepthOffset = 4244  # offset
    m_flHeight = 4232  # offset
    m_flInteractDistance = 4240  # offset
    m_flWidth = 4228  # offset
    m_unHorizontalAlign = 4252  # offset
    m_unOrientation = 4260  # offset
    m_unOwnerContext = 4248  # offset
    m_unVerticalAlign = 4256  # offset
    m_vecCSSClasses = 4272  # offset

    __metadata__ =     [
        {
            "name": "m_bIgnoreInput",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDPI",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flInteractDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDepthOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_unOwnerContext",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unHorizontalAlign",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unVerticalAlign",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unOrientation",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_bAllowInteractionFromAllSceneWorlds",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vecCSSClasses",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class C_PointClientUIWorldPanel(C_BaseClientUIEntity):
    m_anchorDeltaTransform = 3856  # offset
    m_bAllowInteractionFromAllSceneWorlds = 4344  # offset
    m_bCheckCSSClasses = 3842  # offset
    m_bDisableMipGen = 4384  # offset
    m_bExcludeFromSaveGames = 4381  # offset
    m_bFollowPlayerAcrossTeleport = 4306  # offset
    m_bForceRecreateNextUpdate = 3840  # offset
    m_bGrabbable = 4382  # offset
    m_bIgnoreInput = 4304  # offset
    m_bLit = 4305  # offset
    m_bMoveViewToPlayerNextThink = 3841  # offset
    m_bNoDepth = 4377  # offset
    m_bOnlyRenderToTexture = 4383  # offset
    m_bOpaque = 4376  # offset
    m_bRenderBackface = 4379  # offset
    m_bUseOffScreenIndicator = 4380  # offset
    m_bVisibleWhenParentNoDraw = 4378  # offset
    m_flDPI = 4316  # offset
    m_flDepthOffset = 4324  # offset
    m_flHeight = 4312  # offset
    m_flInteractDistance = 4320  # offset
    m_flWidth = 4308  # offset
    m_nExplicitImageLayout = 4388  # offset
    m_pOffScreenIndicator = 4264  # offset
    m_unHorizontalAlign = 4332  # offset
    m_unOrientation = 4340  # offset
    m_unOwnerContext = 4328  # offset
    m_unVerticalAlign = 4336  # offset
    m_vecCSSClasses = 4352  # offset

    __metadata__ =     [
        {
            "name": "m_bIgnoreInput",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bLit",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bFollowPlayerAcrossTeleport",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDPI",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flInteractDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDepthOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_unOwnerContext",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unHorizontalAlign",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unVerticalAlign",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_unOrientation",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_bAllowInteractionFromAllSceneWorlds",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vecCSSClasses",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_bOpaque",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bNoDepth",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bVisibleWhenParentNoDraw",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bRenderBackface",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bUseOffScreenIndicator",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bExcludeFromSaveGames",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bGrabbable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bOnlyRenderToTexture",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bDisableMipGen",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nExplicitImageLayout",
            "type": "NetworkVarNames",
            "type_name": "int32"
        }
    ]

class C_PointClientUIWorldTextPanel(C_PointClientUIWorldPanel):
    m_messageText = 4400  # offset

    __metadata__ =     [
        {
            "name": "m_messageText",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class C_PointCommentaryNode(CBaseAnimGraph):
    m_bActive = 4488  # offset
    m_bListenedTo = 4536  # offset
    m_bRestartAfterRestore = 4556  # offset
    m_bWasActive = 4489  # offset
    m_flEndTime = 4492  # offset
    m_flStartTime = 4496  # offset
    m_flStartTimeInCommentary = 4500  # offset
    m_hViewPosition = 4552  # offset
    m_iNodeNumber = 4528  # offset
    m_iNodeNumberMax = 4532  # offset
    m_iszCommentaryFile = 4504  # offset
    m_iszSpeakers = 4520  # offset
    m_iszTitle = 4512  # offset

    __metadata__ =     [
        {
            "name": "m_bActive",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_flStartTimeInCommentary",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_iszCommentaryFile",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iszTitle",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iszSpeakers",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iNodeNumber",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iNodeNumberMax",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bListenedTo",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_hViewPosition",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseEntity>"
        }
    ]

class C_PointEntity(C_BaseEntity):
    pass

class C_PointValueRemapper(C_BaseEntity):
    m_bDisabled = 1528  # offset
    m_bDisabledOld = 1529  # offset
    m_bEngaged = 1624  # offset
    m_bFirstUpdate = 1625  # offset
    m_bRequiresUseKey = 1556  # offset
    m_bUpdateOnClient = 1530  # offset
    m_flCurrentMomentum = 1608  # offset
    m_flDisengageDistance = 1548  # offset
    m_flEngageDistance = 1552  # offset
    m_flInputOffset = 1620  # offset
    m_flMaximumChangePerSecond = 1544  # offset
    m_flMomentumModifier = 1600  # offset
    m_flPreviousUpdateTickTime = 1632  # offset
    m_flPreviousValue = 1628  # offset
    m_flRatchetOffset = 1616  # offset
    m_flSnapValue = 1604  # offset
    m_hOutputEntities = 1568  # offset
    m_hRemapLineEnd = 1540  # offset
    m_hRemapLineStart = 1536  # offset
    m_nHapticsType = 1592  # offset
    m_nInputType = 1532  # offset
    m_nMomentumType = 1596  # offset
    m_nOutputType = 1560  # offset
    m_nRatchetType = 1612  # offset
    m_vecPreviousTestPoint = 1636  # offset

    __metadata__ =     [
        {
            "name": "m_bDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bUpdateOnClient",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nInputType",
            "type": "NetworkVarNames",
            "type_name": "ValueRemapperInputType_t"
        },
        {
            "name": "m_hRemapLineStart",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_hRemapLineEnd",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_flMaximumChangePerSecond",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDisengageDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flEngageDistance",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bRequiresUseKey",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nOutputType",
            "type": "NetworkVarNames",
            "type_name": "ValueRemapperOutputType_t"
        },
        {
            "name": "m_hOutputEntities",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseEntity>"
        },
        {
            "name": "m_nHapticsType",
            "type": "NetworkVarNames",
            "type_name": "ValueRemapperHapticsType_t"
        },
        {
            "name": "m_nMomentumType",
            "type": "NetworkVarNames",
            "type_name": "ValueRemapperMomentumType_t"
        },
        {
            "name": "m_flMomentumModifier",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSnapValue",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_nRatchetType",
            "type": "NetworkVarNames",
            "type_name": "ValueRemapperRatchetType_t"
        },
        {
            "name": "m_flInputOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_PointWorldText(C_ModelPointEntity):
    m_BackgroundMaterialName = 4392  # offset
    m_Color = 4488  # offset
    m_FontName = 4328  # offset
    m_bDrawBackground = 4472  # offset
    m_bEnabled = 4456  # offset
    m_bForceRecreateNextUpdate = 3792  # offset
    m_bFullbright = 4457  # offset
    m_flBackgroundBorderHeight = 4480  # offset
    m_flBackgroundBorderWidth = 4476  # offset
    m_flBackgroundWorldToUV = 4484  # offset
    m_flDepthOffset = 4468  # offset
    m_flFontSize = 4464  # offset
    m_flWorldUnitsPerPx = 4460  # offset
    m_messageText = 3816  # offset
    m_nJustifyHorizontal = 4492  # offset
    m_nJustifyVertical = 4496  # offset
    m_nReorientMode = 4500  # offset

    __metadata__ =     [
        {
            "name": "m_messageText",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_FontName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_BackgroundMaterialName",
            "type": "NetworkVarNames",
            "type_name": "char"
        },
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bFullbright",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flWorldUnitsPerPx",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFontSize",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDepthOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bDrawBackground",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flBackgroundBorderWidth",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flBackgroundBorderHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flBackgroundWorldToUV",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_Color",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "m_nJustifyHorizontal",
            "type": "NetworkVarNames",
            "type_name": "PointWorldTextJustifyHorizontal_t"
        },
        {
            "name": "m_nJustifyVertical",
            "type": "NetworkVarNames",
            "type_name": "PointWorldTextJustifyVertical_t"
        },
        {
            "name": "m_nReorientMode",
            "type": "NetworkVarNames",
            "type_name": "PointWorldTextReorientMode_t"
        }
    ]

class C_PortraitWorldCallbackHandler(C_BaseEntity):
    pass

class C_PostProcessingVolume(C_BaseTrigger):
    m_bExposureControl = 4165  # offset
    m_bMaster = 4164  # offset
    m_flExposureCompensation = 4148  # offset
    m_flExposureFadeSpeedDown = 4156  # offset
    m_flExposureFadeSpeedUp = 4152  # offset
    m_flFadeDuration = 4128  # offset
    m_flMaxExposure = 4144  # offset
    m_flMaxLogExposure = 4136  # offset
    m_flMinExposure = 4140  # offset
    m_flMinLogExposure = 4132  # offset
    m_flTonemapEVSmoothingRange = 4160  # offset
    m_hPostSettings = 4120  # offset

    __metadata__ =     [
        {
            "name": "m_hPostSettings",
            "type": "NetworkVarNames",
            "type_name": "HPostProcessingStrong"
        },
        {
            "name": "m_flFadeDuration",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flMinLogExposure",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flMaxLogExposure",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flMinExposure",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flMaxExposure",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flExposureCompensation",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flExposureFadeSpeedUp",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flExposureFadeSpeedDown",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flTonemapEVSmoothingRange",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bMaster",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bExposureControl",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_Precipitation(C_BaseTrigger):
    m_bActiveParticlePrecipEmitter = 4176  # offset
    m_bHasSimulatedSinceLastSceneObjectUpdate = 4178  # offset
    m_bParticlePrecipInitialized = 4177  # offset
    m_flDensity = 4104  # offset
    m_flParticleInnerDist = 4120  # offset
    m_nAvailableSheetSequencesMaxIndex = 4180  # offset
    m_pParticleDef = 4128  # offset
    m_tParticlePrecipTraceTimer = 4168  # offset

class C_PrecipitationBlocker(C_BaseModelEntity):
    pass

class C_PropDoorRotating(C_BasePropDoor):
    pass

class C_RagdollProp(CBaseAnimGraph):
    m_flBlendWeight = 4544  # offset
    m_flBlendWeightCurrent = 4556  # offset
    m_hRagdollSource = 4548  # offset
    m_iEyeAttachment = 4552  # offset
    m_parentPhysicsBoneIndices = 4560  # offset
    m_ragAngles = 4520  # offset
    m_ragEnabled = 4472  # offset
    m_ragPos = 4496  # offset
    m_worldSpaceBoneComputationOrder = 4584  # offset

    __metadata__ =     [
        {
            "name": "m_ragEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_ragPos",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_ragAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_flBlendWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_hRagdollSource",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        }
    ]

class C_RagdollPropAttached(C_RagdollProp):
    m_attachmentPointBoneSpace = 4616  # offset
    m_attachmentPointRagdollSpace = 4628  # offset
    m_bHasParent = 4656  # offset
    m_boneIndexAttached = 4608  # offset
    m_parentTime = 4652  # offset
    m_ragdollAttachedObjectIndex = 4612  # offset
    m_vecOffset = 4640  # offset

    __metadata__ =     [
        {
            "name": "m_boneIndexAttached",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_ragdollAttachedObjectIndex",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_attachmentPointBoneSpace",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_attachmentPointRagdollSpace",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_RectLight(C_BarnLight):
    m_bShowLight = 4632  # offset

    __metadata__ =     [
        {
            "name": "m_bShowLight",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_RetakeGameRules:
    m_bBlockersPresent = 252  # offset
    m_bRoundInProgress = 253  # offset
    m_iBombSite = 260  # offset
    m_iFirstSecondHalfRound = 256  # offset
    m_nMatchSeed = 248  # offset

    __metadata__ =     [
        {
            "name": "m_nMatchSeed",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bBlockersPresent",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bRoundInProgress",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iFirstSecondHalfRound",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iBombSite",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_RopeKeyframe(C_BaseModelEntity):
    m_LinksTouchingSomething = 3792  # offset
    m_PhysicsDelegate = 4520  # offset
    m_RopeFlags = 3848  # offset
    m_RopeLength = 4504  # offset
    m_Slack = 4506  # offset
    m_Subdiv = 4502  # offset
    m_TextureHeight = 4544  # offset
    m_TextureScale = 4508  # offset
    m_Width = 4516  # offset
    m_bApplyWind = 3800  # offset
    m_bConstrainBetweenEndpoints = 4656  # offset
    m_bEndPointAttachmentAnglesDirty = 0  # offset
    m_bEndPointAttachmentPositionsDirty = 0  # offset
    m_bNewDataThisFrame = 0  # offset
    m_bPhysicsInitted = 0  # offset
    m_bPrevEndPointPos = 3812  # offset
    m_fLockedPoints = 4512  # offset
    m_fPrevLockedPoints = 3804  # offset
    m_flCurScroll = 3840  # offset
    m_flCurrentGustLifetime = 4576  # offset
    m_flCurrentGustTimer = 4572  # offset
    m_flScrollSpeed = 3844  # offset
    m_flTimeToNextGust = 4580  # offset
    m_hEndPoint = 4496  # offset
    m_hMaterial = 4536  # offset
    m_hStartPoint = 4492  # offset
    m_iEndAttachment = 4501  # offset
    m_iForcePointMoveCounter = 3808  # offset
    m_iRopeMaterialModelIndex = 3856  # offset
    m_iStartAttachment = 4500  # offset
    m_nChangeCount = 4513  # offset
    m_nLinksTouchingSomething = 3796  # offset
    m_nSegments = 4488  # offset
    m_vCachedEndPointAttachmentAngle = 4632  # offset
    m_vCachedEndPointAttachmentPos = 4608  # offset
    m_vColorMod = 4596  # offset
    m_vPrevEndPointPos = 3816  # offset
    m_vWindDir = 4584  # offset
    m_vecImpulse = 4548  # offset
    m_vecPreviousImpulse = 4560  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_flScrollSpeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_RopeFlags",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_iRopeMaterialModelIndex",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_nSegments",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_hStartPoint",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseEntity>"
        },
        {
            "name": "m_hEndPoint",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseEntity>"
        },
        {
            "name": "m_iStartAttachment",
            "type": "NetworkVarNames",
            "type_name": "AttachmentHandle_t"
        },
        {
            "name": "m_iEndAttachment",
            "type": "NetworkVarNames",
            "type_name": "AttachmentHandle_t"
        },
        {
            "name": "m_Subdiv",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_RopeLength",
            "type": "NetworkVarNames",
            "type_name": "int16"
        },
        {
            "name": "m_Slack",
            "type": "NetworkVarNames",
            "type_name": "int16"
        },
        {
            "name": "m_TextureScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_fLockedPoints",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nChangeCount",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_Width",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_bConstrainBetweenEndpoints",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_RopeKeyframe__CPhysicsDelegate:
    m_pKeyframe = 8  # offset

class C_SceneEntity(C_PointEntity):
    m_QueuedEvents = 1592  # offset
    m_bAutogenerated = 1539  # offset
    m_bClientOnly = 1546  # offset
    m_bIsPlayingBack = 1536  # offset
    m_bMultiplayer = 1538  # offset
    m_bPaused = 1537  # offset
    m_bWasPlaying = 1576  # offset
    m_flCurrentTime = 1616  # offset
    m_flForceClientTime = 1540  # offset
    m_hActorList = 1552  # offset
    m_hOwner = 1548  # offset
    m_nSceneStringIndex = 1544  # offset

    __metadata__ =     [
        {
            "name": "m_bIsPlayingBack",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bPaused",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bMultiplayer",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bAutogenerated",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flForceClientTime",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nSceneStringIndex",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_hActorList",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BaseFlex>"
        }
    ]

class C_SceneEntity__QueuedEvents_t:
    starttime = 0  # offset

class C_ShatterGlassShardPhysics(C_PhysicsProp):
    m_ShardDesc = 4904  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_ShardDesc",
            "type": "NetworkVarNames",
            "type_name": "shard_model_desc_t"
        }
    ]

class C_SingleplayRules:
    pass

class C_SkyCamera(C_BaseEntity):
    m_bUseAngles = 1676  # offset
    m_pNext = 1680  # offset
    m_skyboxData = 1528  # offset
    m_skyboxSlotToken = 1672  # offset

    __metadata__ =     [
        {
            "name": "m_skyboxData",
            "type": "NetworkVarNames",
            "type_name": "sky3dparams_t"
        },
        {
            "name": "m_skyboxSlotToken",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        }
    ]

class C_SmokeGrenade(C_BaseCSGrenade):
    pass

class C_SmokeGrenadeProjectile(C_BaseCSGrenadeProjectile):
    m_VoxelFrameData = 5288  # offset
    m_bDidSmokeEffect = 5252  # offset
    m_bSmokeEffectSpawned = 5321  # offset
    m_bSmokeVolumeDataReceived = 5320  # offset
    m_nRandomSeed = 5256  # offset
    m_nSmokeEffectTickBegin = 5248  # offset
    m_nVoxelFrameDataSize = 5312  # offset
    m_nVoxelUpdate = 5316  # offset
    m_vSmokeColor = 5260  # offset
    m_vSmokeDetonationPos = 5272  # offset

    __metadata__ =     [
        {
            "name": "m_nSmokeEffectTickBegin",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bDidSmokeEffect",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nRandomSeed",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_vSmokeColor",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vSmokeDetonationPos",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_VoxelFrameData",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nVoxelFrameDataSize",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nVoxelUpdate",
            "type": "NetworkVarNames",
            "type_name": "int"
        }
    ]

class C_SoundAreaEntityBase(C_BaseEntity):
    m_bDisabled = 1528  # offset
    m_bWasEnabled = 1536  # offset
    m_iszSoundAreaType = 1544  # offset
    m_vPos = 1552  # offset

    __metadata__ =     [
        {
            "name": "m_bDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iszSoundAreaType",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_vPos",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_SoundAreaEntityOrientedBox(C_SoundAreaEntityBase):
    m_vMax = 1580  # offset
    m_vMin = 1568  # offset

    __metadata__ =     [
        {
            "name": "m_vMin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vMax",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_SoundAreaEntitySphere(C_SoundAreaEntityBase):
    m_flRadius = 1568  # offset

    __metadata__ =     [
        {
            "name": "m_flRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_SoundEventAABBEntity(C_SoundEventEntity):
    m_vMaxs = 1740  # offset
    m_vMins = 1728  # offset

    __metadata__ =     [
        {
            "name": "m_vMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_SoundEventEntity(C_BaseEntity):
    m_bClientSideOnly = 0  # offset
    m_bSaveRestore = 1531  # offset
    m_bSavedIsPlaying = 1532  # offset
    m_bStartOnSpawn = 1528  # offset
    m_bStopOnNew = 1530  # offset
    m_bToLocalPlayer = 1529  # offset
    m_flClientCullRadius = 1640  # offset
    m_flSavedElapsedTime = 1536  # offset
    m_hSource = 1716  # offset
    m_iszAttachmentName = 1552  # offset
    m_iszSoundName = 1688  # offset
    m_iszSourceEntityName = 1544  # offset
    m_nEntityIndexSelection = 1720  # offset
    m_onGUIDChanged = 1560  # offset
    m_onSoundFinished = 1600  # offset

class C_SoundEventEntityAlias_snd_event_point(C_SoundEventEntity):
    pass

class C_SoundEventOBBEntity(C_SoundEventEntity):
    m_vMaxs = 1740  # offset
    m_vMins = 1728  # offset

    __metadata__ =     [
        {
            "name": "m_vMins",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vMaxs",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        }
    ]

class C_SoundEventPathCornerEntity(C_SoundEventEntity):
    m_vecCornerPairsNetworked = 1728  # offset

    __metadata__ =     [
        {
            "name": "m_vecCornerPairsNetworked",
            "type": "NetworkVarNames",
            "type_name": "SoundeventPathCornerPairNetworked_t"
        }
    ]

class C_SoundEventSphereEntity(C_SoundEventEntity):
    m_flRadius = 1728  # offset

    __metadata__ =     [
        {
            "name": "m_flRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_SoundOpvarSetAABBEntity(C_SoundOpvarSetPointEntity):
    pass

class C_SoundOpvarSetAutoRoomEntity(C_SoundOpvarSetPointEntity):
    pass

class C_SoundOpvarSetOBBEntity(C_SoundOpvarSetAABBEntity):
    pass

class C_SoundOpvarSetOBBWindEntity(C_SoundOpvarSetPointBase):
    pass

class C_SoundOpvarSetPathCornerEntity(C_SoundOpvarSetPointEntity):
    pass

class C_SoundOpvarSetPointBase(C_BaseEntity):
    m_bUseAutoCompare = 1556  # offset
    m_iOpvarIndex = 1552  # offset
    m_iszOperatorName = 1536  # offset
    m_iszOpvarName = 1544  # offset
    m_iszStackName = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_iszStackName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iszOperatorName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iszOpvarName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_iOpvarIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bUseAutoCompare",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_SoundOpvarSetPointEntity(C_SoundOpvarSetPointBase):
    pass

class C_SpotlightEnd(C_BaseModelEntity):
    m_Radius = 3788  # offset
    m_flLightScale = 3784  # offset

    __metadata__ =     [
        {
            "name": "m_flLightScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_Radius",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class C_Sprite(C_BaseModelEntity):
    m_bWorldSpaceScale = 3840  # offset
    m_flBrightnessDuration = 3828  # offset
    m_flBrightnessTimeStart = 3880  # offset
    m_flDestScale = 3864  # offset
    m_flDieTime = 3808  # offset
    m_flFrame = 3804  # offset
    m_flGlowProxySize = 3844  # offset
    m_flHDRColorScale = 3848  # offset
    m_flLastTime = 3852  # offset
    m_flMaxFrame = 3856  # offset
    m_flScaleDuration = 3836  # offset
    m_flScaleTimeStart = 3868  # offset
    m_flSpriteFramerate = 3800  # offset
    m_flSpriteScale = 3832  # offset
    m_flStartScale = 3860  # offset
    m_hAttachedToEntity = 3792  # offset
    m_hSpriteMaterial = 3784  # offset
    m_nAttachment = 3796  # offset
    m_nBrightness = 3824  # offset
    m_nDestBrightness = 3876  # offset
    m_nSpriteHeight = 3900  # offset
    m_nSpriteWidth = 3896  # offset
    m_nStartBrightness = 3872  # offset

    __metadata__ =     [
        {
            "name": "m_hSpriteMaterial",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_hAttachedToEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_nAttachment",
            "type": "NetworkVarNames",
            "type_name": "AttachmentHandle_t"
        },
        {
            "name": "m_flSpriteFramerate",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flFrame",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nBrightness",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_flBrightnessDuration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flSpriteScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flScaleDuration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_bWorldSpaceScale",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flGlowProxySize",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_flHDRColorScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class C_StattrakModule(C_CS2WeaponModuleBase):
    m_bKnife = 4472  # offset

class C_Team(C_BaseEntity):
    m_aPlayerControllers = 1528  # offset
    m_aPlayers = 1552  # offset
    m_iScore = 1576  # offset
    m_szTeamname = 1580  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
        {
            "name": "m_aPlayerControllers",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerController>"
        },
        {
            "name": "m_aPlayers",
            "type": "NetworkVarNames",
            "type_name": "CHandle<C_BasePlayerPawn>"
        },
        {
            "name": "m_iScore",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_szTeamname",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class C_TeamplayRules:
    pass

class C_TextureBasedAnimatable(C_BaseModelEntity):
    m_bLoop = 3784  # offset
    m_flFPS = 3788  # offset
    m_flStartFrame = 3836  # offset
    m_flStartTime = 3832  # offset
    m_hPositionKeys = 3792  # offset
    m_hRotationKeys = 3800  # offset
    m_vAnimationBoundsMax = 3820  # offset
    m_vAnimationBoundsMin = 3808  # offset

    __metadata__ =     [
        {
            "name": "m_bLoop",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flFPS",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_hPositionKeys",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_hRotationKeys",
            "type": "NetworkVarNames",
            "type_name": "HRenderTextureStrong"
        },
        {
            "name": "m_vAnimationBoundsMin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vAnimationBoundsMax",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_flStartTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flStartFrame",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_TintController(C_BaseEntity):
    pass

class C_TonemapController2(C_BaseEntity):
    m_flAutoExposureMax = 1532  # offset
    m_flAutoExposureMin = 1528  # offset
    m_flExposureAdaptationSpeedDown = 1540  # offset
    m_flExposureAdaptationSpeedUp = 1536  # offset
    m_flTonemapEVSmoothingRange = 1544  # offset

    __metadata__ =     [
        {
            "name": "m_flAutoExposureMin",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flAutoExposureMax",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flExposureAdaptationSpeedUp",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flExposureAdaptationSpeedDown",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flTonemapEVSmoothingRange",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_TonemapController2Alias_env_tonemap_controller2(C_TonemapController2):
    pass

class C_TriggerBuoyancy(C_BaseTrigger):
    m_BuoyancyHelper = 4104  # offset
    m_flFluidDensity = 4384  # offset

    __metadata__ =     [
        {
            "name": "m_flFluidDensity",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class C_TriggerLerpObject(C_BaseTrigger):
    pass

class C_TriggerMultiple(C_BaseTrigger):
    pass

class C_TriggerPhysics(C_BaseTrigger):
    m_angularDamping = 4120  # offset
    m_angularLimit = 4116  # offset
    m_bCollapseToForcePoint = 4148  # offset
    m_bConvertToDebrisWhenPossible = 4176  # offset
    m_flDampingRatio = 4132  # offset
    m_flFrequency = 4128  # offset
    m_gravityScale = 4104  # offset
    m_linearDamping = 4112  # offset
    m_linearForce = 4124  # offset
    m_linearLimit = 4108  # offset
    m_vecLinearForceDirection = 4164  # offset
    m_vecLinearForcePointAt = 4136  # offset
    m_vecLinearForcePointAtWorld = 4152  # offset

    __metadata__ =     [
        {
            "name": "m_gravityScale",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_linearLimit",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_linearDamping",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_angularLimit",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_angularDamping",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_linearForce",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFrequency",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flDampingRatio",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vecLinearForcePointAt",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bCollapseToForcePoint",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_vecLinearForcePointAtWorld",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_vecLinearForceDirection",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_bConvertToDebrisWhenPossible",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_TriggerVolume(C_BaseModelEntity):
    pass

class C_VoteController(C_BaseEntity):
    m_bIsYesNoVote = 1578  # offset
    m_bTypeDirty = 1577  # offset
    m_bVotesDirty = 1576  # offset
    m_iActiveIssueIndex = 1544  # offset
    m_iOnlyTeamToVote = 1548  # offset
    m_nPotentialVotes = 1572  # offset
    m_nVoteOptionCount = 1552  # offset

    __metadata__ =     [
        {
            "name": "m_iActiveIssueIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_iOnlyTeamToVote",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nVoteOptionCount",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPotentialVotes",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bIsYesNoVote",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_WaterBullet(CBaseAnimGraph):
    pass

class C_WeaponAWP(C_CSWeaponBaseGun):
    pass

class C_WeaponAug(C_CSWeaponBaseGun):
    pass

class C_WeaponBaseItem(C_CSWeaponBase):
    m_bRedraw = 8081  # offset
    m_bSequenceInProgress = 8080  # offset

    __metadata__ =     [
        {
            "name": "m_bSequenceInProgress",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bRedraw",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_WeaponBizon(C_CSWeaponBaseGun):
    pass

class C_WeaponCZ75a(C_CSWeaponBaseGun):
    m_bMagazineRemoved = 8128  # offset

    __metadata__ =     [
        {
            "name": "m_bMagazineRemoved",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class C_WeaponElite(C_CSWeaponBaseGun):
    pass

class C_WeaponFamas(C_CSWeaponBaseGun):
    pass

class C_WeaponFiveSeven(C_CSWeaponBaseGun):
    pass

class C_WeaponG3SG1(C_CSWeaponBaseGun):
    pass

class C_WeaponGalilAR(C_CSWeaponBaseGun):
    pass

class C_WeaponGlock(C_CSWeaponBaseGun):
    pass

class C_WeaponHKP2000(C_CSWeaponBaseGun):
    pass

class C_WeaponM249(C_CSWeaponBaseGun):
    pass

class C_WeaponM4A1(C_CSWeaponBaseGun):
    pass

class C_WeaponM4A1Silencer(C_CSWeaponBaseGun):
    pass

class C_WeaponMAC10(C_CSWeaponBaseGun):
    pass

class C_WeaponMP5SD(C_CSWeaponBaseGun):
    pass

class C_WeaponMP7(C_CSWeaponBaseGun):
    pass

class C_WeaponMP9(C_CSWeaponBaseGun):
    pass

class C_WeaponMag7(C_CSWeaponBaseGun):
    pass

class C_WeaponNOVA(C_CSWeaponBase):
    pass

class C_WeaponNegev(C_CSWeaponBaseGun):
    pass

class C_WeaponP250(C_CSWeaponBaseGun):
    pass

class C_WeaponP90(C_CSWeaponBaseGun):
    pass

class C_WeaponRevolver(C_CSWeaponBaseGun):
    pass

class C_WeaponSCAR20(C_CSWeaponBaseGun):
    pass

class C_WeaponSG556(C_CSWeaponBaseGun):
    pass

class C_WeaponSSG08(C_CSWeaponBaseGun):
    pass

class C_WeaponSawedoff(C_CSWeaponBase):
    pass

class C_WeaponTaser(C_CSWeaponBaseGun):
    m_fFireTime = 8128  # offset
    m_nLastAttackTick = 8132  # offset

    __metadata__ =     [
        {
            "name": "m_fFireTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        }
    ]

class C_WeaponTec9(C_CSWeaponBaseGun):
    pass

class C_WeaponUMP45(C_CSWeaponBaseGun):
    pass

class C_WeaponUSPSilencer(C_CSWeaponBaseGun):
    pass

class C_WeaponXM1014(C_CSWeaponBase):
    pass

class C_World(C_BaseModelEntity):
    pass

class C_WorldModelGloves(CBaseAnimGraph):
    pass

class C_fogplayerparams_t:
    m_NewColor = 40  # offset
    m_OldColor = 16  # offset
    m_flNewEnd = 48  # offset
    m_flNewFarZ = 60  # offset
    m_flNewHDRColorScale = 56  # offset
    m_flNewMaxDensity = 52  # offset
    m_flNewStart = 44  # offset
    m_flOldEnd = 24  # offset
    m_flOldFarZ = 36  # offset
    m_flOldHDRColorScale = 32  # offset
    m_flOldMaxDensity = 28  # offset
    m_flOldStart = 20  # offset
    m_flTransitionTime = 12  # offset
    m_hCtrl = 8  # offset

    __metadata__ =     [
        {
            "name": "m_hCtrl",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CFogController>"
        }
    ]

class CountdownTimer:
    m_duration = 8  # offset
    m_nWorldGroupId = 20  # offset
    m_timescale = 16  # offset
    m_timestamp = 12  # offset

    __metadata__ =     [
        {
            "name": "m_duration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_timestamp",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_timescale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nWorldGroupId",
            "type": "NetworkVarNames",
            "type_name": "WorldGroupId_t"
        }
    ]

class EngineCountdownTimer:
    m_duration = 8  # offset
    m_timescale = 16  # offset
    m_timestamp = 12  # offset

    __metadata__ =     [
        {
            "name": "m_duration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_timestamp",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_timescale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class EntityRenderAttribute_t:
    m_ID = 48  # offset
    m_Values = 52  # offset

    __metadata__ =     [
        {
            "name": "m_ID",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        },
        {
            "name": "m_Values",
            "type": "NetworkVarNames",
            "type_name": "Vector4D"
        }
    ]

class EntitySpottedState_t:
    m_bSpotted = 8  # offset
    m_bSpottedByMask = 12  # offset

    __metadata__ =     [
        {
            "name": "m_bSpotted",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bSpottedByMask",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        }
    ]

class FilterDamageType(CBaseFilter):
    m_iDamageType = 1616  # offset

class FilterHealth(CBaseFilter):
    m_bAdrenalineActive = 1616  # offset
    m_iHealthMax = 1624  # offset
    m_iHealthMin = 1620  # offset

class IntervalTimer:
    m_nWorldGroupId = 12  # offset
    m_timestamp = 8  # offset

    __metadata__ =     [
        {
            "name": "m_timestamp",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "m_nWorldGroupId",
            "type": "NetworkVarNames",
            "type_name": "WorldGroupId_t"
        }
    ]

class OutflowWithRequirements_t:
    m_Connection = 0  # offset
    m_DestinationFlowNodeID = 72  # offset
    m_RequirementNodeIDs = 80  # offset
    m_nCursorStateBlockIndex = 104  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PhysicsRagdollPose_t:
    m_Transforms = 8  # offset
    m_bSetFromDebugHistory = 36  # offset
    m_hOwner = 32  # offset

    __metadata__ =     [
        {
            "name": "m_Transforms",
            "type": "NetworkVarNames",
            "type_name": "CTransform"
        },
        {
            "name": "m_hOwner",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        }
    ]

class PredictedDamageTag_t:
    flFlinchModLarge = 56  # offset
    flFlinchModSmall = 52  # offset
    flFriendlyFireDamageReductionRatio = 60  # offset
    nTagTick = 48  # offset

    __metadata__ =     [
        {
            "name": "nTagTick",
            "type": "NetworkVarNames",
            "type_name": "GameTick_t"
        },
        {
            "name": "flFlinchModSmall",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "flFlinchModLarge",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "flFriendlyFireDamageReductionRatio",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class PulseNodeDynamicOutflows_t:
    m_Outflows = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseNodeDynamicOutflows_t__DynamicOutflow_t:
    m_Connection = 8  # offset
    m_OutflowID = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseObservableBoolExpression_t:
    m_DependentObservableBlackboardReferences = 96  # offset
    m_DependentObservableVars = 72  # offset
    m_EvaluateConnection = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseSelectorOutflowList_t:
    m_Outflows = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SellbackPurchaseEntry_t:
    m_bPrevHelmet = 60  # offset
    m_hItem = 64  # offset
    m_nCost = 52  # offset
    m_nPrevArmor = 56  # offset
    m_unDefIdx = 48  # offset

    __metadata__ =     [
        {
            "name": "m_unDefIdx",
            "type": "NetworkVarNames",
            "type_name": "item_definition_index_t"
        },
        {
            "name": "m_nCost",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_nPrevArmor",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_bPrevHelmet",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_hItem",
            "type": "NetworkVarNames",
            "type_name": "CEntityHandle"
        }
    ]

class SequenceHistory_t:
    m_flCyclesPerSecond = 20  # offset
    m_flPlaybackRate = 16  # offset
    m_flSeqFixedCycle = 8  # offset
    m_flSeqStartTime = 4  # offset
    m_hSequence = 0  # offset
    m_nSeqLoopMode = 12  # offset

class SignatureOutflow_Continue:
    pass

class SignatureOutflow_Resume:
    pass

class VPhysicsCollisionAttribute_t:
    m_nCollisionFunctionMask = 43  # offset
    m_nCollisionGroup = 42  # offset
    m_nEntityId = 32  # offset
    m_nHierarchyId = 40  # offset
    m_nInteractsAs = 8  # offset
    m_nInteractsExclude = 24  # offset
    m_nInteractsWith = 16  # offset
    m_nOwnerId = 36  # offset

    __metadata__ =     [
        {
            "name": "m_nInteractsAs",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_nInteractsWith",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_nInteractsExclude",
            "type": "NetworkVarNames",
            "type_name": "uint64"
        },
        {
            "name": "m_nEntityId",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nOwnerId",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        },
        {
            "name": "m_nHierarchyId",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_nCollisionGroup",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nCollisionFunctionMask",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        }
    ]

class ViewAngleServerChange_t:
    nIndex = 64  # offset
    nType = 48  # offset
    qAngle = 52  # offset

    __metadata__ =     [
        {
            "name": "nType",
            "type": "NetworkVarNames",
            "type_name": "FixAngleSet_t"
        },
        {
            "name": "qAngle",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "nIndex",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        }
    ]

class WeaponPurchaseCount_t:
    m_nCount = 50  # offset
    m_nItemDefIndex = 48  # offset

    __metadata__ =     [
        {
            "name": "m_nItemDefIndex",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_nCount",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        }
    ]

class WeaponPurchaseTracker_t:
    m_weaponPurchases = 8  # offset

    __metadata__ =     [
        {
            "name": "m_weaponPurchases",
            "type": "NetworkVarNames",
            "type_name": "WeaponPurchaseCount_t"
        }
    ]

class audioparams_t:
    localBits = 108  # offset
    localSound = 8  # offset
    soundEventHash = 116  # offset
    soundscapeEntityListIndex = 112  # offset
    soundscapeIndex = 104  # offset

    __metadata__ =     [
        {
            "name": "localSound",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "soundscapeIndex",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "localBits",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "soundscapeEntityListIndex",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "soundEventHash",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        }
    ]

class fogparams_t:
    HDRColorScale = 56  # offset
    blend = 101  # offset
    blendtobackground = 88  # offset
    colorPrimary = 20  # offset
    colorPrimaryLerpTo = 28  # offset
    colorSecondary = 24  # offset
    colorSecondaryLerpTo = 32  # offset
    dirPrimary = 8  # offset
    duration = 84  # offset
    enable = 100  # offset
    end = 40  # offset
    endLerpTo = 72  # offset
    exponent = 52  # offset
    farz = 44  # offset
    lerptime = 80  # offset
    locallightscale = 96  # offset
    m_bPadding = 103  # offset
    m_bPadding2 = 102  # offset
    maxdensity = 48  # offset
    maxdensityLerpTo = 76  # offset
    scattering = 92  # offset
    skyboxFogFactor = 60  # offset
    skyboxFogFactorLerpTo = 64  # offset
    start = 36  # offset
    startLerpTo = 68  # offset

    __metadata__ =     [
        {
            "name": "dirPrimary",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "colorPrimary",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "colorSecondary",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "colorPrimaryLerpTo",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "colorSecondaryLerpTo",
            "type": "NetworkVarNames",
            "type_name": "Color"
        },
        {
            "name": "start",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "end",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "farz",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "maxdensity",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "exponent",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "HDRColorScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "skyboxFogFactor",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "skyboxFogFactorLerpTo",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "startLerpTo",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "endLerpTo",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "maxdensityLerpTo",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "lerptime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        },
        {
            "name": "duration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "blendtobackground",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "scattering",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "locallightscale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "enable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "blend",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class shard_model_desc_t:
    m_SurfacePropStringToken = 120  # offset
    m_bHasParent = 116  # offset
    m_bParentFrozen = 117  # offset
    m_flGlassHalfThickness = 112  # offset
    m_hMaterialBase = 16  # offset
    m_hMaterialDamageOverlay = 24  # offset
    m_nModelID = 8  # offset
    m_solid = 32  # offset
    m_vInitialPanelVertices = 88  # offset
    m_vecPanelSize = 36  # offset
    m_vecPanelVertices = 64  # offset
    m_vecStressPositionA = 44  # offset
    m_vecStressPositionB = 52  # offset

    __metadata__ =     [
        {
            "name": "m_nModelID",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_hMaterialBase",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_hMaterialDamageOverlay",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_solid",
            "type": "NetworkVarNames",
            "type_name": "ShardSolid_t"
        },
        {
            "name": "m_vecPanelSize",
            "type": "NetworkVarNames",
            "type_name": "Vector2D"
        },
        {
            "name": "m_vecStressPositionA",
            "type": "NetworkVarNames",
            "type_name": "Vector2D"
        },
        {
            "name": "m_vecStressPositionB",
            "type": "NetworkVarNames",
            "type_name": "Vector2D"
        },
        {
            "name": "m_vecPanelVertices",
            "type": "NetworkVarNames",
            "type_name": "Vector2D"
        },
        {
            "name": "m_vInitialPanelVertices",
            "type": "NetworkVarNames",
            "type_name": "Vector4D"
        },
        {
            "name": "m_flGlassHalfThickness",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bHasParent",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bParentFrozen",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_SurfacePropStringToken",
            "type": "NetworkVarNames",
            "type_name": "CUtlStringToken"
        }
    ]

class sky3dparams_t:
    bClip3DSkyBoxNearToWorldFar = 24  # offset
    flClip3DSkyBoxNearToWorldFarOffset = 28  # offset
    fog = 32  # offset
    m_nWorldGroupID = 136  # offset
    origin = 12  # offset
    scale = 8  # offset

    __metadata__ =     [
        {
            "name": "scale",
            "type": "NetworkVarNames",
            "type_name": "int16"
        },
        {
            "name": "origin",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "bClip3DSkyBoxNearToWorldFar",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "flClip3DSkyBoxNearToWorldFarOffset",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "fog",
            "type": "NetworkVarNames",
            "type_name": "fogparams_t"
        },
        {
            "name": "m_nWorldGroupID",
            "type": "NetworkVarNames",
            "type_name": "WorldGroupId_t"
        }
    ]

