#include <cstddef>
namespace client_dll {
		namespace ActiveModelConfig_t {
			constexpr std::ptrdiff_t m_AssociatedEntities = 0x38; // ActiveModelConfig_t
			constexpr std::ptrdiff_t m_AssociatedEntityNames = 0x50; // ActiveModelConfig_t
			constexpr std::ptrdiff_t m_Handle = 0x28; // ActiveModelConfig_t
			constexpr std::ptrdiff_t m_Name = 0x30; // ActiveModelConfig_t
		}
		namespace CAnimGraphNetworkedVariables {
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetBoolVariables = 0xf8; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetByteVariables = 0x110; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetFloatVariables = 0x188; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetGlobalSymbolVariables = 0x1d0; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetIntVariables = 0x140; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetQuaternionVariables = 0x1b8; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetUInt16Variables = 0x128; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetUInt32Variables = 0x158; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetUInt64Variables = 0x170; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_OwnerOnlyPredNetVectorVariables = 0x1a0; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetBoolVariables = 0x8; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetByteVariables = 0x20; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetFloatVariables = 0x98; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetGlobalSymbolVariables = 0xe0; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetIntVariables = 0x50; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetQuaternionVariables = 0xc8; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetUInt16Variables = 0x38; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetUInt32Variables = 0x68; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetUInt64Variables = 0x80; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_PredNetVectorVariables = 0xb0; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_flLastTeleportTime = 0x1f4; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_nBoolVariablesCount = 0x1e8; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_nOwnerOnlyBoolVariablesCount = 0x1ec; // CAnimGraphNetworkedVariables
			constexpr std::ptrdiff_t m_nRandomSeedOffset = 0x1f0; // CAnimGraphNetworkedVariables
		}
		namespace CAttributeList {
			constexpr std::ptrdiff_t m_Attributes = 0x8; // CAttributeList
			constexpr std::ptrdiff_t m_pManager = 0x58; // CAttributeList
		}
		namespace CAttributeManager {
			constexpr std::ptrdiff_t m_CachedResults = 0x30; // CAttributeManager
			constexpr std::ptrdiff_t m_ProviderType = 0x2c; // CAttributeManager
			constexpr std::ptrdiff_t m_Providers = 0x8; // CAttributeManager
			constexpr std::ptrdiff_t m_bPreventLoopback = 0x28; // CAttributeManager
			constexpr std::ptrdiff_t m_hOuter = 0x24; // CAttributeManager
			constexpr std::ptrdiff_t m_iReapplyProvisionParity = 0x20; // CAttributeManager
		}
		namespace CAttributeManager__cached_attribute_float_t {
			constexpr std::ptrdiff_t flIn = 0x0; // CAttributeManager__cached_attribute_float_t
			constexpr std::ptrdiff_t flOut = 0x10; // CAttributeManager__cached_attribute_float_t
			constexpr std::ptrdiff_t iAttribHook = 0x8; // CAttributeManager__cached_attribute_float_t
		}
		namespace CBaseAnimGraph {
			constexpr std::ptrdiff_t m_RagdollPose = 0xdf8; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bAnimGraphUpdateEnabled = 0xdb0; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bAnimationUpdateScheduled = 0xdc4; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bBuiltRagdoll = 0xde0; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bHasAnimatedMaterialAttributes = 0xe50; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bInitiallyPopulateInterpHistory = 0xda0; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bRagdollClientSide = 0xe40; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_bSuppressAnimEventSounds = 0xda2; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_flMaxSlopeDistance = 0xdb4; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_nForceBone = 0xdd4; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_pClientsideRagdoll = 0xdd8; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_vLastSlopeCheckPos = 0xdb8; // CBaseAnimGraph
			constexpr std::ptrdiff_t m_vecForce = 0xdc8; // CBaseAnimGraph
		}
		namespace CBaseAnimGraphController {
			constexpr std::ptrdiff_t m_animGraphNetworkedVars = 0x18; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_bLastUpdateSkipped = 0x14d4; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_bNetworkedAnimationInputsChanged = 0x14d2; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_bNetworkedSequenceChanged = 0x14d3; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_bSequenceFinished = 0x14a8; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_flPlaybackRate = 0x14c4; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_flPrevAnimUpdateTime = 0x14d8; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_flSeqFixedCycle = 0x14bc; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_flSeqStartTime = 0x14b8; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_flSoundSyncTime = 0x14ac; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_hSequence = 0x14b4; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_nActiveIKChainMask = 0x14b0; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_nAnimLoopMode = 0x14c0; // CBaseAnimGraphController
			constexpr std::ptrdiff_t m_nNotifyState = 0x14d0; // CBaseAnimGraphController
		}
		namespace CBasePlayerController {
			constexpr std::ptrdiff_t m_CommandContext = 0x578; // CBasePlayerController
			constexpr std::ptrdiff_t m_bIsHLTV = 0x658; // CBasePlayerController
			constexpr std::ptrdiff_t m_bIsLocalPlayerController = 0x6f0; // CBasePlayerController
			constexpr std::ptrdiff_t m_bKnownTeamMismatch = 0x630; // CBasePlayerController
			constexpr std::ptrdiff_t m_hPawn = 0x62c; // CBasePlayerController
			constexpr std::ptrdiff_t m_hPredictedPawn = 0x634; // CBasePlayerController
			constexpr std::ptrdiff_t m_hSplitOwner = 0x63c; // CBasePlayerController
			constexpr std::ptrdiff_t m_hSplitScreenPlayers = 0x640; // CBasePlayerController
			constexpr std::ptrdiff_t m_iConnected = 0x65c; // CBasePlayerController
			constexpr std::ptrdiff_t m_iDesiredFOV = 0x6f4; // CBasePlayerController
			constexpr std::ptrdiff_t m_iszPlayerName = 0x660; // CBasePlayerController
			constexpr std::ptrdiff_t m_nFinalPredictedTick = 0x570; // CBasePlayerController
			constexpr std::ptrdiff_t m_nInButtonsWhichAreToggles = 0x620; // CBasePlayerController
			constexpr std::ptrdiff_t m_nSplitScreenSlot = 0x638; // CBasePlayerController
			constexpr std::ptrdiff_t m_nTickBase = 0x628; // CBasePlayerController
			constexpr std::ptrdiff_t m_steamID = 0x6e8; // CBasePlayerController
		}
		namespace CBasePlayerVData {
			constexpr std::ptrdiff_t m_flArmDamageMultiplier = 0x138; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flChestDamageMultiplier = 0x118; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flCrouchTime = 0x174; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flDrowningDamageInterval = 0x15c; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flHeadDamageMultiplier = 0x108; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flHoldBreathTime = 0x158; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flLegDamageMultiplier = 0x148; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flStomachDamageMultiplier = 0x128; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flUseAngleTolerance = 0x170; // CBasePlayerVData
			constexpr std::ptrdiff_t m_flUseRange = 0x16c; // CBasePlayerVData
			constexpr std::ptrdiff_t m_nDrowningDamageInitial = 0x160; // CBasePlayerVData
			constexpr std::ptrdiff_t m_nDrowningDamageMax = 0x164; // CBasePlayerVData
			constexpr std::ptrdiff_t m_nWaterSpeed = 0x168; // CBasePlayerVData
			constexpr std::ptrdiff_t m_sModelName = 0x28; // CBasePlayerVData
		}
		namespace CBasePlayerWeaponVData {
			constexpr std::ptrdiff_t m_aShootSounds = 0x320; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_bAllowFlipping = 0x1e9; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_bAutoSwitchFrom = 0x30d; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_bAutoSwitchTo = 0x30c; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_bBuiltRightHanded = 0x1e8; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_bLinkedCooldowns = 0x2f0; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_bReserveAmmoAsClips = 0x304; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iDefaultClip1 = 0x2fc; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iDefaultClip2 = 0x300; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iFlags = 0x2f1; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iMaxClip1 = 0x2f4; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iMaxClip2 = 0x2f8; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iPosition = 0x318; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iRumbleEffect = 0x310; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iSlot = 0x314; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_iWeight = 0x308; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_nPrimaryAmmoType = 0x2f2; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_nSecondaryAmmoType = 0x2f3; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_sMuzzleAttachment = 0x1f0; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_sToolsOnlyOwnerModelName = 0x108; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_szMuzzleFlashParticle = 0x210; // CBasePlayerWeaponVData
			constexpr std::ptrdiff_t m_szWorldModel = 0x28; // CBasePlayerWeaponVData
		}
		namespace CBaseProp {
			constexpr std::ptrdiff_t m_bConformToCollisionBounds = 0xf90; // CBaseProp
			constexpr std::ptrdiff_t m_bModelOverrodeBlockLOS = 0xf88; // CBaseProp
			constexpr std::ptrdiff_t m_iShapeType = 0xf8c; // CBaseProp
			constexpr std::ptrdiff_t m_mPreferredCatchTransform = 0xf94; // CBaseProp
		}
		namespace CBodyComponent {
			constexpr std::ptrdiff_t __m_pChainEntity = 0x20; // CBodyComponent
			constexpr std::ptrdiff_t m_pSceneNode = 0x8; // CBodyComponent
		}
		namespace CBodyComponentBaseAnimGraph {
			constexpr std::ptrdiff_t m_animationController = 0x490; // CBodyComponentBaseAnimGraph
		}
		namespace CBodyComponentPoint {
			constexpr std::ptrdiff_t m_sceneNode = 0x50; // CBodyComponentPoint
		}
		namespace CBodyComponentSkeletonInstance {
			constexpr std::ptrdiff_t m_skeletonInstance = 0x50; // CBodyComponentSkeletonInstance
		}
		namespace CBombTarget {
			constexpr std::ptrdiff_t m_bBombPlantedHere = 0xd30; // CBombTarget
		}
		namespace CBuoyancyHelper {
			constexpr std::ptrdiff_t m_flFluidDensity = 0x1c; // CBuoyancyHelper
			constexpr std::ptrdiff_t m_nFluidType = 0x18; // CBuoyancyHelper
			constexpr std::ptrdiff_t m_vecFractionOfWheelSubmergedForWheelDrag = 0x50; // CBuoyancyHelper
			constexpr std::ptrdiff_t m_vecFractionOfWheelSubmergedForWheelFriction = 0x20; // CBuoyancyHelper
			constexpr std::ptrdiff_t m_vecWheelDrag = 0x68; // CBuoyancyHelper
			constexpr std::ptrdiff_t m_vecWheelFrictionScales = 0x38; // CBuoyancyHelper
		}
		namespace CCSGameModeRules {
			constexpr std::ptrdiff_t __m_pChainEntity = 0x8; // CCSGameModeRules
		}
		namespace CCSGameModeRules_ArmsRace {
			constexpr std::ptrdiff_t m_WeaponSequence = 0x30; // CCSGameModeRules_ArmsRace
		}
		namespace CCSGameModeRules_Deathmatch {
			constexpr std::ptrdiff_t m_flDMBonusStartTime = 0x30; // CCSGameModeRules_Deathmatch
			constexpr std::ptrdiff_t m_flDMBonusTimeLength = 0x34; // CCSGameModeRules_Deathmatch
			constexpr std::ptrdiff_t m_sDMBonusWeapon = 0x38; // CCSGameModeRules_Deathmatch
		}
		namespace CCSObserver_ObserverServices {
			constexpr std::ptrdiff_t m_bObserverInterpolationNeedsDeferredSetup = 0xa4; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_flObsInterp_PathLength = 0x74; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_hLastObserverTarget = 0x58; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_obsInterpState = 0xa0; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_qObsInterp_OrientationStart = 0x80; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_qObsInterp_OrientationTravelDir = 0x90; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_vecObserverInterpStartPos = 0x68; // CCSObserver_ObserverServices
			constexpr std::ptrdiff_t m_vecObserverInterpolateOffset = 0x5c; // CCSObserver_ObserverServices
		}
		namespace CCSPlayerBase_CameraServices {
			constexpr std::ptrdiff_t m_flFOVRate = 0x21c; // CCSPlayerBase_CameraServices
			constexpr std::ptrdiff_t m_flFOVTime = 0x218; // CCSPlayerBase_CameraServices
			constexpr std::ptrdiff_t m_flLastShotFOV = 0x224; // CCSPlayerBase_CameraServices
			constexpr std::ptrdiff_t m_hZoomOwner = 0x220; // CCSPlayerBase_CameraServices
			constexpr std::ptrdiff_t m_iFOV = 0x210; // CCSPlayerBase_CameraServices
			constexpr std::ptrdiff_t m_iFOVStart = 0x214; // CCSPlayerBase_CameraServices
		}
		namespace CCSPlayerController {
			constexpr std::ptrdiff_t m_bAbandonAllowsSurrender = 0x7ee; // CCSPlayerController
			constexpr std::ptrdiff_t m_bAbandonOffersInstantSurrender = 0x7ef; // CCSPlayerController
			constexpr std::ptrdiff_t m_bCanControlObservedBot = 0x808; // CCSPlayerController
			constexpr std::ptrdiff_t m_bCannotBeKicked = 0x7ec; // CCSPlayerController
			constexpr std::ptrdiff_t m_bControllingBot = 0x800; // CCSPlayerController
			constexpr std::ptrdiff_t m_bDisconnection1MinWarningPrinted = 0x7f0; // CCSPlayerController
			constexpr std::ptrdiff_t m_bEverFullyConnected = 0x7ed; // CCSPlayerController
			constexpr std::ptrdiff_t m_bEverPlayedOnTeam = 0x75c; // CCSPlayerController
			constexpr std::ptrdiff_t m_bFireBulletsSeedSynchronized = 0x855; // CCSPlayerController
			constexpr std::ptrdiff_t m_bHasBeenControlledByPlayerThisRound = 0x802; // CCSPlayerController
			constexpr std::ptrdiff_t m_bHasCommunicationAbuseMute = 0x744; // CCSPlayerController
			constexpr std::ptrdiff_t m_bHasControlledBotThisRound = 0x801; // CCSPlayerController
			constexpr std::ptrdiff_t m_bIsPlayerNameDirty = 0x854; // CCSPlayerController
			constexpr std::ptrdiff_t m_bMvpNoMusic = 0x842; // CCSPlayerController
			constexpr std::ptrdiff_t m_bPawnHasDefuser = 0x820; // CCSPlayerController
			constexpr std::ptrdiff_t m_bPawnHasHelmet = 0x821; // CCSPlayerController
			constexpr std::ptrdiff_t m_bPawnIsAlive = 0x814; // CCSPlayerController
			constexpr std::ptrdiff_t m_bScoreReported = 0x7f1; // CCSPlayerController
			constexpr std::ptrdiff_t m_eMvpReason = 0x844; // CCSPlayerController
			constexpr std::ptrdiff_t m_flForceTeamTime = 0x754; // CCSPlayerController
			constexpr std::ptrdiff_t m_flPreviousForceJoinTeamTime = 0x760; // CCSPlayerController
			constexpr std::ptrdiff_t m_hObserverPawn = 0x810; // CCSPlayerController
			constexpr std::ptrdiff_t m_hOriginalControllerOfCurrentPawn = 0x830; // CCSPlayerController
			constexpr std::ptrdiff_t m_hPlayerPawn = 0x80c; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCoachingTeam = 0x778; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompTeammateColor = 0x758; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompetitiveRankType = 0x798; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompetitiveRanking = 0x790; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompetitiveRankingPredicted_Loss = 0x7a0; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompetitiveRankingPredicted_Tie = 0x7a4; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompetitiveRankingPredicted_Win = 0x79c; // CCSPlayerController
			constexpr std::ptrdiff_t m_iCompetitiveWins = 0x794; // CCSPlayerController
			constexpr std::ptrdiff_t m_iDraftIndex = 0x7e0; // CCSPlayerController
			constexpr std::ptrdiff_t m_iMVPs = 0x850; // CCSPlayerController
			constexpr std::ptrdiff_t m_iMusicKitID = 0x848; // CCSPlayerController
			constexpr std::ptrdiff_t m_iMusicKitMVPs = 0x84c; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPawnArmor = 0x81c; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPawnBotDifficulty = 0x82c; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPawnHealth = 0x818; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPawnLifetimeEnd = 0x828; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPawnLifetimeStart = 0x824; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPendingTeamNum = 0x750; // CCSPlayerController
			constexpr std::ptrdiff_t m_iPing = 0x740; // CCSPlayerController
			constexpr std::ptrdiff_t m_iScore = 0x834; // CCSPlayerController
			constexpr std::ptrdiff_t m_msQueuedModeDisconnectionTimestamp = 0x7e4; // CCSPlayerController
			constexpr std::ptrdiff_t m_nBotsControlledThisRound = 0x804; // CCSPlayerController
			constexpr std::ptrdiff_t m_nDisconnectionTick = 0x7f4; // CCSPlayerController
			constexpr std::ptrdiff_t m_nEndMatchNextMapVote = 0x7a8; // CCSPlayerController
			constexpr std::ptrdiff_t m_nFirstKill = 0x840; // CCSPlayerController
			constexpr std::ptrdiff_t m_nKillCount = 0x841; // CCSPlayerController
			constexpr std::ptrdiff_t m_nPawnCharacterDefIndex = 0x822; // CCSPlayerController
			constexpr std::ptrdiff_t m_nPlayerDominated = 0x780; // CCSPlayerController
			constexpr std::ptrdiff_t m_nPlayerDominatingMe = 0x788; // CCSPlayerController
			constexpr std::ptrdiff_t m_nQuestProgressReason = 0x7b0; // CCSPlayerController
			constexpr std::ptrdiff_t m_pActionTrackingServices = 0x730; // CCSPlayerController
			constexpr std::ptrdiff_t m_pDamageServices = 0x738; // CCSPlayerController
			constexpr std::ptrdiff_t m_pInGameMoneyServices = 0x720; // CCSPlayerController
			constexpr std::ptrdiff_t m_pInventoryServices = 0x728; // CCSPlayerController
			constexpr std::ptrdiff_t m_recentKillQueue = 0x838; // CCSPlayerController
			constexpr std::ptrdiff_t m_sSanitizedPlayerName = 0x770; // CCSPlayerController
			constexpr std::ptrdiff_t m_szClan = 0x768; // CCSPlayerController
			constexpr std::ptrdiff_t m_szCrosshairCodes = 0x748; // CCSPlayerController
			constexpr std::ptrdiff_t m_uiAbandonRecordedReason = 0x7e8; // CCSPlayerController
			constexpr std::ptrdiff_t m_unActiveQuestId = 0x7ac; // CCSPlayerController
			constexpr std::ptrdiff_t m_unPlayerTvControlFlags = 0x7b4; // CCSPlayerController
		}
		namespace CCSPlayerController_ActionTrackingServices {
			constexpr std::ptrdiff_t m_iNumRoundKills = 0x110; // CCSPlayerController_ActionTrackingServices
			constexpr std::ptrdiff_t m_iNumRoundKillsHeadshots = 0x114; // CCSPlayerController_ActionTrackingServices
			constexpr std::ptrdiff_t m_matchStats = 0x90; // CCSPlayerController_ActionTrackingServices
			constexpr std::ptrdiff_t m_perRoundStats = 0x40; // CCSPlayerController_ActionTrackingServices
			constexpr std::ptrdiff_t m_unTotalRoundDamageDealt = 0x118; // CCSPlayerController_ActionTrackingServices
		}
		namespace CCSPlayerController_DamageServices {
			constexpr std::ptrdiff_t m_DamageList = 0x48; // CCSPlayerController_DamageServices
			constexpr std::ptrdiff_t m_nSendUpdate = 0x40; // CCSPlayerController_DamageServices
		}
		namespace CCSPlayerController_InGameMoneyServices {
			constexpr std::ptrdiff_t m_iAccount = 0x40; // CCSPlayerController_InGameMoneyServices
			constexpr std::ptrdiff_t m_iCashSpentThisRound = 0x4c; // CCSPlayerController_InGameMoneyServices
			constexpr std::ptrdiff_t m_iStartAccount = 0x44; // CCSPlayerController_InGameMoneyServices
			constexpr std::ptrdiff_t m_iTotalCashSpent = 0x48; // CCSPlayerController_InGameMoneyServices
		}
		namespace CCSPlayerController_InventoryServices {
			constexpr std::ptrdiff_t m_nPersonaDataPublicCommendsFriendly = 0x68; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_nPersonaDataPublicCommendsLeader = 0x60; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_nPersonaDataPublicCommendsTeacher = 0x64; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_nPersonaDataPublicLevel = 0x5c; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_nPersonaDataXpTrailLevel = 0x6c; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_rank = 0x44; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_unMusicID = 0x40; // CCSPlayerController_InventoryServices
			constexpr std::ptrdiff_t m_vecServerAuthoritativeWeaponSlots = 0x70; // CCSPlayerController_InventoryServices
		}
		namespace CCSPlayer_ActionTrackingServices {
			constexpr std::ptrdiff_t m_bIsRescuing = 0x44; // CCSPlayer_ActionTrackingServices
			constexpr std::ptrdiff_t m_hLastWeaponBeforeC4AutoSwitch = 0x40; // CCSPlayer_ActionTrackingServices
			constexpr std::ptrdiff_t m_weaponPurchasesThisMatch = 0x48; // CCSPlayer_ActionTrackingServices
			constexpr std::ptrdiff_t m_weaponPurchasesThisRound = 0xa0; // CCSPlayer_ActionTrackingServices
		}
		namespace CCSPlayer_BulletServices {
			constexpr std::ptrdiff_t m_totalHitsOnServer = 0x40; // CCSPlayer_BulletServices
		}
		namespace CCSPlayer_BuyServices {
			constexpr std::ptrdiff_t m_vecSellbackPurchaseEntries = 0x40; // CCSPlayer_BuyServices
		}
		namespace CCSPlayer_CameraServices {
			constexpr std::ptrdiff_t m_flDeathCamTilt = 0x228; // CCSPlayer_CameraServices
			constexpr std::ptrdiff_t m_vClientScopeInaccuracy = 0x230; // CCSPlayer_CameraServices
		}
		namespace CCSPlayer_HostageServices {
			constexpr std::ptrdiff_t m_hCarriedHostage = 0x40; // CCSPlayer_HostageServices
			constexpr std::ptrdiff_t m_hCarriedHostageProp = 0x44; // CCSPlayer_HostageServices
		}
		namespace CCSPlayer_ItemServices {
			constexpr std::ptrdiff_t m_bHasDefuser = 0x40; // CCSPlayer_ItemServices
			constexpr std::ptrdiff_t m_bHasHeavyArmor = 0x42; // CCSPlayer_ItemServices
			constexpr std::ptrdiff_t m_bHasHelmet = 0x41; // CCSPlayer_ItemServices
		}
		namespace CCSPlayer_MovementServices {
			constexpr std::ptrdiff_t m_StuckLast = 0x46c; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_bDesiresDuck = 0x231; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_bDuckOverride = 0x230; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_bHasWalkMovedSinceLastJump = 0x259; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_bInStuckTest = 0x25a; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_bOldJumpPressed = 0x4a8; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_bSpeedCropped = 0x470; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_duckUntilOnGround = 0x258; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_fStashGrenadeParameterWhen = 0x4b0; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flAccumulatedJumpError = 0x4dc; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flDuckAmount = 0x228; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flDuckOffset = 0x234; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flDuckSpeed = 0x22c; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flGroundMoveEfficiency = 0x474; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flHeightAtJumpStart = 0x4cc; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flJumpPressedTime = 0x4ac; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flLastDuckTime = 0x244; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flMaxJumpHeightLastJump = 0x4d4; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flMaxJumpHeightThisJump = 0x4d0; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flOffsetTickCompleteTime = 0x4c0; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flOffsetTickStashedSpeed = 0x4c4; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flStamina = 0x4c8; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flStaminaAtJumpStart = 0x4d8; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flStuckCheckTime = 0x268; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_flWaterEntryTime = 0x47c; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nButtonDownMaskPrev = 0x4b8; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nDuckJumpTimeMsecs = 0x23c; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nDuckTimeMsecs = 0x238; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nGameCodeHasMovedPlayerAfterCommand = 0x4a4; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nJumpTimeMsecs = 0x240; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nLadderSurfacePropIndex = 0x224; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nOldWaterLevel = 0x478; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_nTraceCount = 0x468; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecForward = 0x480; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecLadderNormal = 0x218; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecLastPositionAtFullCrouchSpeed = 0x250; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecLeft = 0x48c; // CCSPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecUp = 0x498; // CCSPlayer_MovementServices
		}
		namespace CCSPlayer_PingServices {
			constexpr std::ptrdiff_t m_hPlayerPing = 0x40; // CCSPlayer_PingServices
		}
		namespace CCSPlayer_ViewModelServices {
			constexpr std::ptrdiff_t m_hViewModel = 0x40; // CCSPlayer_ViewModelServices
		}
		namespace CCSPlayer_WaterServices {
			constexpr std::ptrdiff_t m_flSwimSoundTime = 0x50; // CCSPlayer_WaterServices
			constexpr std::ptrdiff_t m_flWaterJumpTime = 0x40; // CCSPlayer_WaterServices
			constexpr std::ptrdiff_t m_vecWaterJumpVel = 0x44; // CCSPlayer_WaterServices
		}
		namespace CCSPlayer_WeaponServices {
			constexpr std::ptrdiff_t m_bIsHoldingLookAtWeapon = 0xbd; // CCSPlayer_WeaponServices
			constexpr std::ptrdiff_t m_bIsLookingAtWeapon = 0xbc; // CCSPlayer_WeaponServices
			constexpr std::ptrdiff_t m_flNextAttack = 0xb8; // CCSPlayer_WeaponServices
			constexpr std::ptrdiff_t m_nOldInputHistoryCount = 0x458; // CCSPlayer_WeaponServices
			constexpr std::ptrdiff_t m_nOldShootPositionHistoryCount = 0xc0; // CCSPlayer_WeaponServices
		}
		namespace CCSPointScript {
			constexpr std::ptrdiff_t m_pParent = 0xf8; // CCSPointScript
		}
		namespace CCSWeaponBaseVData {
			constexpr std::ptrdiff_t m_DefaultLoadoutSlot = 0xcf8; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_GearSlot = 0xcf0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_GearSlotPosition = 0xcf4; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_WeaponCategory = 0x34c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_WeaponType = 0x348; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_angPivotAngle = 0xe28; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bCannotShootUnderwater = 0xd1b; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bHasBurstMode = 0xd19; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bHideViewModelWhenZoomed = 0xdf9; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bIsFullAuto = 0xd3c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bIsRevolver = 0xd1a; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bMeleeWeapon = 0xd18; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_bUnzoomsAfterShot = 0xdf8; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_eSilencerType = 0xd30; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flArmorRatio = 0xe48; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flAttackMovespeedFactor = 0xdd8; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flBotAudibleRange = 0xde8; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flCycleTime = 0xd44; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flFlinchVelocityModifierLarge = 0xe58; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flFlinchVelocityModifierSmall = 0xe5c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flHeadshotMultiplier = 0xe44; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flHeatPerShot = 0xddc; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flIdleInterval = 0xdd4; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyAltSoundThreshold = 0xde4; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyCrouch = 0xd5c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyFire = 0xd84; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyJump = 0xd6c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyJumpApex = 0xdc0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyJumpInitial = 0xdbc; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyLadder = 0xd7c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyLand = 0xd74; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyMove = 0xd8c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyPitchShift = 0xde0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyReload = 0xdc4; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flInaccuracyStand = 0xd64; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flIronSightFOV = 0xe1c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flIronSightLooseness = 0xe24; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flIronSightPivotForward = 0xe20; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flIronSightPullUpSpeed = 0xe14; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flIronSightPutDownSpeed = 0xe18; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flMaxSpeed = 0xd4c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flPenetration = 0xe4c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRange = 0xe50; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRangeModifier = 0xe54; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoilAngle = 0xd94; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoilAngleVariance = 0xd9c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoilMagnitude = 0xda4; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoilMagnitudeVariance = 0xdac; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoveryTimeCrouch = 0xe60; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoveryTimeCrouchFinal = 0xe68; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoveryTimeStand = 0xe64; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flRecoveryTimeStandFinal = 0xe6c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flSpread = 0xd54; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flThrowVelocity = 0xe78; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flTimeToIdleAfterFire = 0xdd0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flZoomTime0 = 0xe08; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flZoomTime1 = 0xe0c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_flZoomTime2 = 0xe10; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nCrosshairDeltaDistance = 0xd38; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nCrosshairMinDistance = 0xd34; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nDamage = 0xe40; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nKillAward = 0xd0c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nNumBullets = 0xd40; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nPrice = 0xd08; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nPrimaryReserveAmmoMax = 0xd10; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nRecoilSeed = 0xdc8; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nRecoveryTransitionEndBullet = 0xe74; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nRecoveryTransitionStartBullet = 0xe70; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nSecondaryReserveAmmoMax = 0xd14; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nSpreadSeed = 0xdcc; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nTracerFrequency = 0xdb4; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nZoomFOV1 = 0xe00; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nZoomFOV2 = 0xe04; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_nZoomLevels = 0xdfc; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_sWrongTeamMsg = 0xd00; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szAimsightLensMaskModel = 0x5f0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szAnimClass = 0xe88; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szAnimExtension = 0xd28; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szEjectBrassEffect = 0x890; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szHeatEffect = 0x7b0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szMagazineModel = 0x6d0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szMuzzleFlashParticleAlt = 0x970; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szMuzzleFlashThirdPersonParticle = 0xa50; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szMuzzleFlashThirdPersonParticleAlt = 0xb30; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szName = 0xd20; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szPlayerModel = 0x430; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szTracerParticle = 0xc10; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szUseRadioSubtitle = 0xdf0; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szViewModel = 0x350; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_szWorldDroppedModel = 0x510; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_vSmokeColor = 0xe7c; // CCSWeaponBaseVData
			constexpr std::ptrdiff_t m_vecIronSightEyePos = 0xe34; // CCSWeaponBaseVData
		}
		namespace CCitadelSoundOpvarSetOBB {
			constexpr std::ptrdiff_t m_iszOperatorName = 0x588; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_iszOpvarName = 0x590; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_iszStackName = 0x580; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_nAABBDirection = 0x5c8; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_vDistanceInnerMaxs = 0x5a4; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_vDistanceInnerMins = 0x598; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_vDistanceOuterMaxs = 0x5bc; // CCitadelSoundOpvarSetOBB
			constexpr std::ptrdiff_t m_vDistanceOuterMins = 0x5b0; // CCitadelSoundOpvarSetOBB
		}
		namespace CCollisionProperty {
			constexpr std::ptrdiff_t m_CollisionGroup = 0x5e; // CCollisionProperty
			constexpr std::ptrdiff_t m_collisionAttribute = 0x10; // CCollisionProperty
			constexpr std::ptrdiff_t m_flBoundingRadius = 0x60; // CCollisionProperty
			constexpr std::ptrdiff_t m_flCapsuleRadius = 0xac; // CCollisionProperty
			constexpr std::ptrdiff_t m_nEnablePhysics = 0x5f; // CCollisionProperty
			constexpr std::ptrdiff_t m_nSolidType = 0x5b; // CCollisionProperty
			constexpr std::ptrdiff_t m_nSurroundType = 0x5d; // CCollisionProperty
			constexpr std::ptrdiff_t m_triggerBloat = 0x5c; // CCollisionProperty
			constexpr std::ptrdiff_t m_usSolidFlags = 0x5a; // CCollisionProperty
			constexpr std::ptrdiff_t m_vCapsuleCenter1 = 0x94; // CCollisionProperty
			constexpr std::ptrdiff_t m_vCapsuleCenter2 = 0xa0; // CCollisionProperty
			constexpr std::ptrdiff_t m_vecMaxs = 0x4c; // CCollisionProperty
			constexpr std::ptrdiff_t m_vecMins = 0x40; // CCollisionProperty
			constexpr std::ptrdiff_t m_vecSpecifiedSurroundingMaxs = 0x70; // CCollisionProperty
			constexpr std::ptrdiff_t m_vecSpecifiedSurroundingMins = 0x64; // CCollisionProperty
			constexpr std::ptrdiff_t m_vecSurroundingMaxs = 0x7c; // CCollisionProperty
			constexpr std::ptrdiff_t m_vecSurroundingMins = 0x88; // CCollisionProperty
		}
		namespace CDamageRecord {
			constexpr std::ptrdiff_t m_DamagerXuid = 0x48; // CDamageRecord
			constexpr std::ptrdiff_t m_PlayerDamager = 0x28; // CDamageRecord
			constexpr std::ptrdiff_t m_PlayerRecipient = 0x2c; // CDamageRecord
			constexpr std::ptrdiff_t m_RecipientXuid = 0x50; // CDamageRecord
			constexpr std::ptrdiff_t m_bIsOtherEnemy = 0x6c; // CDamageRecord
			constexpr std::ptrdiff_t m_hPlayerControllerDamager = 0x30; // CDamageRecord
			constexpr std::ptrdiff_t m_hPlayerControllerRecipient = 0x34; // CDamageRecord
			constexpr std::ptrdiff_t m_iActualHealthRemoved = 0x60; // CDamageRecord
			constexpr std::ptrdiff_t m_iBulletsDamage = 0x58; // CDamageRecord
			constexpr std::ptrdiff_t m_iDamage = 0x5c; // CDamageRecord
			constexpr std::ptrdiff_t m_iLastBulletUpdate = 0x68; // CDamageRecord
			constexpr std::ptrdiff_t m_iNumHits = 0x64; // CDamageRecord
			constexpr std::ptrdiff_t m_killType = 0x6d; // CDamageRecord
			constexpr std::ptrdiff_t m_szPlayerDamagerName = 0x38; // CDamageRecord
			constexpr std::ptrdiff_t m_szPlayerRecipientName = 0x40; // CDamageRecord
		}
		namespace CEconItemAttribute {
			constexpr std::ptrdiff_t m_bSetBonus = 0x40; // CEconItemAttribute
			constexpr std::ptrdiff_t m_flInitialValue = 0x38; // CEconItemAttribute
			constexpr std::ptrdiff_t m_flValue = 0x34; // CEconItemAttribute
			constexpr std::ptrdiff_t m_iAttributeDefinitionIndex = 0x30; // CEconItemAttribute
			constexpr std::ptrdiff_t m_nRefundableCurrency = 0x3c; // CEconItemAttribute
		}
		namespace CEffectData {
			constexpr std::ptrdiff_t m_fFlags = 0x63; // CEffectData
			constexpr std::ptrdiff_t m_flMagnitude = 0x44; // CEffectData
			constexpr std::ptrdiff_t m_flRadius = 0x48; // CEffectData
			constexpr std::ptrdiff_t m_flScale = 0x40; // CEffectData
			constexpr std::ptrdiff_t m_hEntity = 0x38; // CEffectData
			constexpr std::ptrdiff_t m_hOtherEntity = 0x3c; // CEffectData
			constexpr std::ptrdiff_t m_iEffectName = 0x6c; // CEffectData
			constexpr std::ptrdiff_t m_nAttachmentIndex = 0x64; // CEffectData
			constexpr std::ptrdiff_t m_nAttachmentName = 0x68; // CEffectData
			constexpr std::ptrdiff_t m_nColor = 0x62; // CEffectData
			constexpr std::ptrdiff_t m_nDamageType = 0x58; // CEffectData
			constexpr std::ptrdiff_t m_nEffectIndex = 0x50; // CEffectData
			constexpr std::ptrdiff_t m_nExplosionType = 0x6e; // CEffectData
			constexpr std::ptrdiff_t m_nHitBox = 0x60; // CEffectData
			constexpr std::ptrdiff_t m_nMaterial = 0x5e; // CEffectData
			constexpr std::ptrdiff_t m_nPenetrate = 0x5c; // CEffectData
			constexpr std::ptrdiff_t m_nSurfaceProp = 0x4c; // CEffectData
			constexpr std::ptrdiff_t m_vAngles = 0x2c; // CEffectData
			constexpr std::ptrdiff_t m_vNormal = 0x20; // CEffectData
			constexpr std::ptrdiff_t m_vOrigin = 0x8; // CEffectData
			constexpr std::ptrdiff_t m_vStart = 0x14; // CEffectData
		}
		namespace CEntityIdentity {
			constexpr std::ptrdiff_t m_PathIndex = 0x40; // CEntityIdentity
			constexpr std::ptrdiff_t m_designerName = 0x20; // CEntityIdentity
			constexpr std::ptrdiff_t m_fDataObjectTypes = 0x3c; // CEntityIdentity
			constexpr std::ptrdiff_t m_flags = 0x30; // CEntityIdentity
			constexpr std::ptrdiff_t m_name = 0x18; // CEntityIdentity
			constexpr std::ptrdiff_t m_nameStringableIndex = 0x14; // CEntityIdentity
			constexpr std::ptrdiff_t m_pNext = 0x60; // CEntityIdentity
			constexpr std::ptrdiff_t m_pNextByClass = 0x70; // CEntityIdentity
			constexpr std::ptrdiff_t m_pPrev = 0x58; // CEntityIdentity
			constexpr std::ptrdiff_t m_pPrevByClass = 0x68; // CEntityIdentity
			constexpr std::ptrdiff_t m_worldGroupId = 0x38; // CEntityIdentity
		}
		namespace CEntityInstance {
			constexpr std::ptrdiff_t m_CScriptComponent = 0x28; // CEntityInstance
			constexpr std::ptrdiff_t m_bVisibleinPVS = 0x30; // CEntityInstance
			constexpr std::ptrdiff_t m_iszPrivateVScripts = 0x8; // CEntityInstance
			constexpr std::ptrdiff_t m_pEntity = 0x10; // CEntityInstance
		}
		namespace CEnvSoundscape {
			constexpr std::ptrdiff_t m_OnPlay = 0x568; // CEnvSoundscape
			constexpr std::ptrdiff_t m_bDisabled = 0x5f4; // CEnvSoundscape
			constexpr std::ptrdiff_t m_bOverrideWithEvent = 0x5a0; // CEnvSoundscape
			constexpr std::ptrdiff_t m_flRadius = 0x590; // CEnvSoundscape
			constexpr std::ptrdiff_t m_hProxySoundscape = 0x5f0; // CEnvSoundscape
			constexpr std::ptrdiff_t m_positionNames = 0x5b0; // CEnvSoundscape
			constexpr std::ptrdiff_t m_soundEventHash = 0x600; // CEnvSoundscape
			constexpr std::ptrdiff_t m_soundEventName = 0x598; // CEnvSoundscape
			constexpr std::ptrdiff_t m_soundscapeEntityListId = 0x5a8; // CEnvSoundscape
			constexpr std::ptrdiff_t m_soundscapeIndex = 0x5a4; // CEnvSoundscape
			constexpr std::ptrdiff_t m_soundscapeName = 0x5f8; // CEnvSoundscape
		}
		namespace CEnvSoundscapeProxy {
			constexpr std::ptrdiff_t m_MainSoundscapeName = 0x608; // CEnvSoundscapeProxy
		}
		namespace CFuncWater {
			constexpr std::ptrdiff_t m_BuoyancyHelper = 0xd28; // CFuncWater
		}
		namespace CGameSceneNode {
			constexpr std::ptrdiff_t m_angAbsRotation = 0xdc; // CGameSceneNode
			constexpr std::ptrdiff_t m_angRotation = 0xc0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bBoneMergeFlex = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bDebugAbsOriginChanges = 0xee; // CGameSceneNode
			constexpr std::ptrdiff_t m_bDirtyBoneMergeBoneToRoot = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bDirtyBoneMergeInfo = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bDirtyHierarchy = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bDormant = 0xef; // CGameSceneNode
			constexpr std::ptrdiff_t m_bForceParentToBeNetworked = 0xf0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bNetworkedAnglesChanged = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bNetworkedPositionChanged = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bNetworkedScaleChanged = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_bWillBeCallingPostDataUpdate = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_flAbsScale = 0xe8; // CGameSceneNode
			constexpr std::ptrdiff_t m_flClientLocalScale = 0x140; // CGameSceneNode
			constexpr std::ptrdiff_t m_flScale = 0xcc; // CGameSceneNode
			constexpr std::ptrdiff_t m_flZOffset = 0x13c; // CGameSceneNode
			constexpr std::ptrdiff_t m_hParent = 0x78; // CGameSceneNode
			constexpr std::ptrdiff_t m_hierarchyAttachName = 0x138; // CGameSceneNode
			constexpr std::ptrdiff_t m_nDoNotSetAnimTimeInInvalidatePhysicsCount = 0xf5; // CGameSceneNode
			constexpr std::ptrdiff_t m_nHierarchicalDepth = 0xf3; // CGameSceneNode
			constexpr std::ptrdiff_t m_nHierarchyType = 0xf4; // CGameSceneNode
			constexpr std::ptrdiff_t m_nLatchAbsOrigin = 0x0; // CGameSceneNode
			constexpr std::ptrdiff_t m_nParentAttachmentOrBone = 0xec; // CGameSceneNode
			constexpr std::ptrdiff_t m_name = 0xf8; // CGameSceneNode
			constexpr std::ptrdiff_t m_nodeToWorld = 0x10; // CGameSceneNode
			constexpr std::ptrdiff_t m_pChild = 0x40; // CGameSceneNode
			constexpr std::ptrdiff_t m_pNextSibling = 0x48; // CGameSceneNode
			constexpr std::ptrdiff_t m_pOwner = 0x30; // CGameSceneNode
			constexpr std::ptrdiff_t m_pParent = 0x38; // CGameSceneNode
			constexpr std::ptrdiff_t m_vRenderOrigin = 0x144; // CGameSceneNode
			constexpr std::ptrdiff_t m_vecAbsOrigin = 0xd0; // CGameSceneNode
			constexpr std::ptrdiff_t m_vecOrigin = 0x88; // CGameSceneNode
		}
		namespace CGameSceneNodeHandle {
			constexpr std::ptrdiff_t m_hOwner = 0x8; // CGameSceneNodeHandle
			constexpr std::ptrdiff_t m_name = 0xc; // CGameSceneNodeHandle
		}
		namespace CGlowProperty {
			constexpr std::ptrdiff_t m_bEligibleForScreenHighlight = 0x50; // CGlowProperty
			constexpr std::ptrdiff_t m_bFlashing = 0x44; // CGlowProperty
			constexpr std::ptrdiff_t m_bGlowing = 0x51; // CGlowProperty
			constexpr std::ptrdiff_t m_fGlowColor = 0x8; // CGlowProperty
			constexpr std::ptrdiff_t m_flGlowStartTime = 0x4c; // CGlowProperty
			constexpr std::ptrdiff_t m_flGlowTime = 0x48; // CGlowProperty
			constexpr std::ptrdiff_t m_glowColorOverride = 0x40; // CGlowProperty
			constexpr std::ptrdiff_t m_iGlowTeam = 0x34; // CGlowProperty
			constexpr std::ptrdiff_t m_iGlowType = 0x30; // CGlowProperty
			constexpr std::ptrdiff_t m_nGlowRange = 0x38; // CGlowProperty
			constexpr std::ptrdiff_t m_nGlowRangeMin = 0x3c; // CGlowProperty
		}
		namespace CGrenadeTracer {
			constexpr std::ptrdiff_t m_flTracerDuration = 0xd40; // CGrenadeTracer
			constexpr std::ptrdiff_t m_nType = 0xd44; // CGrenadeTracer
		}
		namespace CHitboxComponent {
			constexpr std::ptrdiff_t m_bvDisabledHitGroups = 0x24; // CHitboxComponent
		}
		namespace CInfoDynamicShadowHint {
			constexpr std::ptrdiff_t m_bDisabled = 0x568; // CInfoDynamicShadowHint
			constexpr std::ptrdiff_t m_flRange = 0x56c; // CInfoDynamicShadowHint
			constexpr std::ptrdiff_t m_hLight = 0x578; // CInfoDynamicShadowHint
			constexpr std::ptrdiff_t m_nImportance = 0x570; // CInfoDynamicShadowHint
			constexpr std::ptrdiff_t m_nLightChoice = 0x574; // CInfoDynamicShadowHint
		}
		namespace CInfoDynamicShadowHintBox {
			constexpr std::ptrdiff_t m_vBoxMaxs = 0x58c; // CInfoDynamicShadowHintBox
			constexpr std::ptrdiff_t m_vBoxMins = 0x580; // CInfoDynamicShadowHintBox
		}
		namespace CInfoOffscreenPanoramaTexture {
			constexpr std::ptrdiff_t m_RenderAttrName = 0x580; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_TargetEntities = 0x588; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_bCheckCSSClasses = 0x720; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_bDisabled = 0x568; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_nResolutionX = 0x56c; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_nResolutionY = 0x570; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_nTargetChangeCount = 0x5a0; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_szLayoutFileName = 0x578; // CInfoOffscreenPanoramaTexture
			constexpr std::ptrdiff_t m_vecCSSClasses = 0x5a8; // CInfoOffscreenPanoramaTexture
		}
		namespace CInfoWorldLayer {
			constexpr std::ptrdiff_t m_bCreateAsChildSpawnGroup = 0x5a2; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_bEntitiesSpawned = 0x5a1; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_bWorldLayerActuallyVisible = 0x5a8; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_bWorldLayerVisible = 0x5a0; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_hLayerSpawnGroup = 0x5a4; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_layerName = 0x598; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_pOutputOnEntitiesSpawned = 0x568; // CInfoWorldLayer
			constexpr std::ptrdiff_t m_worldName = 0x590; // CInfoWorldLayer
		}
		namespace CLightComponent {
			constexpr std::ptrdiff_t __m_pChainEntity = 0x38; // CLightComponent
			constexpr std::ptrdiff_t m_Color = 0x75; // CLightComponent
			constexpr std::ptrdiff_t m_Pattern = 0xd8; // CLightComponent
			constexpr std::ptrdiff_t m_SecondaryColor = 0x79; // CLightComponent
			constexpr std::ptrdiff_t m_SkyAmbientBounce = 0x18c; // CLightComponent
			constexpr std::ptrdiff_t m_SkyColor = 0x184; // CLightComponent
			constexpr std::ptrdiff_t m_bEnabled = 0x134; // CLightComponent
			constexpr std::ptrdiff_t m_bFlicker = 0x135; // CLightComponent
			constexpr std::ptrdiff_t m_bMixedShadows = 0x191; // CLightComponent
			constexpr std::ptrdiff_t m_bPrecomputedFieldsValid = 0x136; // CLightComponent
			constexpr std::ptrdiff_t m_bRenderDiffuse = 0xc0; // CLightComponent
			constexpr std::ptrdiff_t m_bRenderToCubemaps = 0x118; // CLightComponent
			constexpr std::ptrdiff_t m_bRenderTransmissive = 0xc8; // CLightComponent
			constexpr std::ptrdiff_t m_bUseSecondaryColor = 0x190; // CLightComponent
			constexpr std::ptrdiff_t m_bUsesBakedShadowing = 0x10c; // CLightComponent
			constexpr std::ptrdiff_t m_flAttenuation0 = 0x94; // CLightComponent
			constexpr std::ptrdiff_t m_flAttenuation1 = 0x98; // CLightComponent
			constexpr std::ptrdiff_t m_flAttenuation2 = 0x9c; // CLightComponent
			constexpr std::ptrdiff_t m_flBrightness = 0x80; // CLightComponent
			constexpr std::ptrdiff_t m_flBrightnessMult = 0x88; // CLightComponent
			constexpr std::ptrdiff_t m_flBrightnessScale = 0x84; // CLightComponent
			constexpr std::ptrdiff_t m_flCapsuleLength = 0x198; // CLightComponent
			constexpr std::ptrdiff_t m_flFadeMaxDist = 0x128; // CLightComponent
			constexpr std::ptrdiff_t m_flFadeMinDist = 0x124; // CLightComponent
			constexpr std::ptrdiff_t m_flFalloff = 0x90; // CLightComponent
			constexpr std::ptrdiff_t m_flFogContributionStength = 0x17c; // CLightComponent
			constexpr std::ptrdiff_t m_flLightStyleStartTime = 0x194; // CLightComponent
			constexpr std::ptrdiff_t m_flMinRoughness = 0x19c; // CLightComponent
			constexpr std::ptrdiff_t m_flNearClipPlane = 0x180; // CLightComponent
			constexpr std::ptrdiff_t m_flOrthoLightHeight = 0xd0; // CLightComponent
			constexpr std::ptrdiff_t m_flOrthoLightWidth = 0xcc; // CLightComponent
			constexpr std::ptrdiff_t m_flPhi = 0xa4; // CLightComponent
			constexpr std::ptrdiff_t m_flPrecomputedMaxRange = 0x174; // CLightComponent
			constexpr std::ptrdiff_t m_flRange = 0x8c; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowCascadeCrossFade = 0xe4; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowCascadeDistance0 = 0xec; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowCascadeDistance1 = 0xf0; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowCascadeDistance2 = 0xf4; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowCascadeDistance3 = 0xf8; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowCascadeDistanceFade = 0xe8; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowFadeMaxDist = 0x130; // CLightComponent
			constexpr std::ptrdiff_t m_flShadowFadeMinDist = 0x12c; // CLightComponent
			constexpr std::ptrdiff_t m_flSkyIntensity = 0x188; // CLightComponent
			constexpr std::ptrdiff_t m_flTheta = 0xa0; // CLightComponent
			constexpr std::ptrdiff_t m_hLightCookie = 0xa8; // CLightComponent
			constexpr std::ptrdiff_t m_nBakedShadowIndex = 0x114; // CLightComponent
			constexpr std::ptrdiff_t m_nCascadeRenderStaticObjects = 0xe0; // CLightComponent
			constexpr std::ptrdiff_t m_nCascades = 0xb0; // CLightComponent
			constexpr std::ptrdiff_t m_nCastShadows = 0xb4; // CLightComponent
			constexpr std::ptrdiff_t m_nDirectLight = 0x11c; // CLightComponent
			constexpr std::ptrdiff_t m_nFogLightingMode = 0x178; // CLightComponent
			constexpr std::ptrdiff_t m_nIndirectLight = 0x120; // CLightComponent
			constexpr std::ptrdiff_t m_nRenderSpecular = 0xc4; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowCascadeResolution0 = 0xfc; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowCascadeResolution1 = 0x100; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowCascadeResolution2 = 0x104; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowCascadeResolution3 = 0x108; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowHeight = 0xbc; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowPriority = 0x110; // CLightComponent
			constexpr std::ptrdiff_t m_nShadowWidth = 0xb8; // CLightComponent
			constexpr std::ptrdiff_t m_nStyle = 0xd4; // CLightComponent
			constexpr std::ptrdiff_t m_vPrecomputedBoundsMaxs = 0x144; // CLightComponent
			constexpr std::ptrdiff_t m_vPrecomputedBoundsMins = 0x138; // CLightComponent
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles = 0x15c; // CLightComponent
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent = 0x168; // CLightComponent
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin = 0x150; // CLightComponent
		}
		namespace CLogicRelay {
			constexpr std::ptrdiff_t m_OnSpawn = 0x590; // CLogicRelay
			constexpr std::ptrdiff_t m_OnTrigger = 0x568; // CLogicRelay
			constexpr std::ptrdiff_t m_bDisabled = 0x5b8; // CLogicRelay
			constexpr std::ptrdiff_t m_bFastRetrigger = 0x5bb; // CLogicRelay
			constexpr std::ptrdiff_t m_bPassthoughCaller = 0x5bc; // CLogicRelay
			constexpr std::ptrdiff_t m_bTriggerOnce = 0x5ba; // CLogicRelay
			constexpr std::ptrdiff_t m_bWaitForRefire = 0x5b9; // CLogicRelay
		}
		namespace CMapInfo {
			constexpr std::ptrdiff_t m_bDisableAutoGeneratedDMSpawns = 0x575; // CMapInfo
			constexpr std::ptrdiff_t m_bFadePlayerVisibilityFarZ = 0x580; // CMapInfo
			constexpr std::ptrdiff_t m_bRainTraceToSkyEnabled = 0x581; // CMapInfo
			constexpr std::ptrdiff_t m_bUseNormalSpawnsForDM = 0x574; // CMapInfo
			constexpr std::ptrdiff_t m_flBombRadius = 0x56c; // CMapInfo
			constexpr std::ptrdiff_t m_flBotMaxVisionDistance = 0x578; // CMapInfo
			constexpr std::ptrdiff_t m_iBuyingStatus = 0x568; // CMapInfo
			constexpr std::ptrdiff_t m_iHostageCount = 0x57c; // CMapInfo
			constexpr std::ptrdiff_t m_iPetPopulation = 0x570; // CMapInfo
		}
		namespace CModelState {
			constexpr std::ptrdiff_t m_MeshGroupMask = 0x198; // CModelState
			constexpr std::ptrdiff_t m_ModelName = 0xa8; // CModelState
			constexpr std::ptrdiff_t m_bClientClothCreationSuppressed = 0xe8; // CModelState
			constexpr std::ptrdiff_t m_hModel = 0xa0; // CModelState
			constexpr std::ptrdiff_t m_nClothUpdateFlags = 0x21c; // CModelState
			constexpr std::ptrdiff_t m_nForceLOD = 0x21b; // CModelState
			constexpr std::ptrdiff_t m_nIdealMotionType = 0x21a; // CModelState
		}
		namespace CNetworkedSequenceOperation {
			constexpr std::ptrdiff_t m_bDiscontinuity = 0x1d; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_bSequenceChangeNetworked = 0x1c; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_flCycle = 0x10; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_flPrevCycle = 0xc; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_flPrevCycleForAnimEventDetection = 0x24; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_flPrevCycleFromDiscontinuity = 0x20; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_flWeight = 0x14; // CNetworkedSequenceOperation
			constexpr std::ptrdiff_t m_hSequence = 0x8; // CNetworkedSequenceOperation
		}
		namespace CPathSimple {
			constexpr std::ptrdiff_t m_pathString = 0x5c0; // CPathSimple
		}
		namespace CPlayer_CameraServices {
			constexpr std::ptrdiff_t m_CurrentFog = 0x140; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_OverrideFogColor = 0x1b1; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_PlayerFog = 0x58; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_PostProcessingVolumes = 0x120; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_angDemoViewAngles = 0x1f8; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_audio = 0xa8; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_bOverrideFogColor = 0x1ac; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_bOverrideFogStartEnd = 0x1c5; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_fOverrideFogEnd = 0x1e0; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_fOverrideFogStart = 0x1cc; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_flCsViewPunchAngleTickRatio = 0x50; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_flOldPlayerViewOffsetZ = 0x13c; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_flOldPlayerZ = 0x138; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_hActivePostProcessingVolume = 0x1f4; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_hColorCorrectionCtrl = 0x98; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_hOldFogController = 0x1a8; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_hTonemapController = 0xa0; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_hViewEntity = 0x9c; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_nCsViewPunchAngleTick = 0x4c; // CPlayer_CameraServices
			constexpr std::ptrdiff_t m_vecCsViewPunchAngle = 0x40; // CPlayer_CameraServices
		}
		namespace CPlayer_MovementServices {
			constexpr std::ptrdiff_t m_arrForceSubtickMoveWhen = 0x19c; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_flForwardMove = 0x1ac; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_flLeftMove = 0x1b0; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_flMaxspeed = 0x198; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_flUpMove = 0x1b4; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nButtonDoublePressed = 0x78; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nButtons = 0x48; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nImpulse = 0x40; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nLastCommandNumberProcessed = 0x180; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nQueuedButtonChangeMask = 0x70; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nQueuedButtonDownMask = 0x68; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_nToggleButtonDownMask = 0x188; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_pButtonPressedCmdNumber = 0x80; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecLastMovementImpulses = 0x1b8; // CPlayer_MovementServices
			constexpr std::ptrdiff_t m_vecOldViewAngles = 0x1c4; // CPlayer_MovementServices
		}
		namespace CPlayer_MovementServices_Humanoid {
			constexpr std::ptrdiff_t m_bDucked = 0x1ec; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_bDucking = 0x1ed; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_bInCrouch = 0x1e0; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_bInDuckJump = 0x1ee; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_flCrouchTransitionStartTime = 0x1e8; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_flFallVelocity = 0x1dc; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_flStepSoundTime = 0x1d8; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_flSurfaceFriction = 0x1fc; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_groundNormal = 0x1f0; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_nCrouchState = 0x1e4; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_nStepside = 0x210; // CPlayer_MovementServices_Humanoid
			constexpr std::ptrdiff_t m_surfaceProps = 0x200; // CPlayer_MovementServices_Humanoid
		}
		namespace CPlayer_ObserverServices {
			constexpr std::ptrdiff_t m_bForcedObserverMode = 0x4c; // CPlayer_ObserverServices
			constexpr std::ptrdiff_t m_flObserverChaseDistance = 0x50; // CPlayer_ObserverServices
			constexpr std::ptrdiff_t m_flObserverChaseDistanceCalcTime = 0x54; // CPlayer_ObserverServices
			constexpr std::ptrdiff_t m_hObserverTarget = 0x44; // CPlayer_ObserverServices
			constexpr std::ptrdiff_t m_iObserverLastMode = 0x48; // CPlayer_ObserverServices
			constexpr std::ptrdiff_t m_iObserverMode = 0x40; // CPlayer_ObserverServices
		}
		namespace CPlayer_WeaponServices {
			constexpr std::ptrdiff_t m_hActiveWeapon = 0x58; // CPlayer_WeaponServices
			constexpr std::ptrdiff_t m_hLastWeapon = 0x5c; // CPlayer_WeaponServices
			constexpr std::ptrdiff_t m_hMyWeapons = 0x40; // CPlayer_WeaponServices
			constexpr std::ptrdiff_t m_iAmmo = 0x60; // CPlayer_WeaponServices
		}
		namespace CPointChildModifier {
			constexpr std::ptrdiff_t m_bOrphanInsteadOfDeletingChildrenOnRemove = 0x568; // CPointChildModifier
		}
		namespace CPointOffScreenIndicatorUi {
			constexpr std::ptrdiff_t m_bBeenEnabled = 0xf90; // CPointOffScreenIndicatorUi
			constexpr std::ptrdiff_t m_bHide = 0xf91; // CPointOffScreenIndicatorUi
			constexpr std::ptrdiff_t m_flSeenTargetTime = 0xf94; // CPointOffScreenIndicatorUi
			constexpr std::ptrdiff_t m_pTargetPanel = 0xf98; // CPointOffScreenIndicatorUi
		}
		namespace CPointTemplate {
			constexpr std::ptrdiff_t m_ScriptCallbackScope = 0x5f0; // CPointTemplate
			constexpr std::ptrdiff_t m_ScriptSpawnCallback = 0x5e8; // CPointTemplate
			constexpr std::ptrdiff_t m_SpawnedEntityHandles = 0x5d0; // CPointTemplate
			constexpr std::ptrdiff_t m_bAsynchronouslySpawnEntities = 0x584; // CPointTemplate
			constexpr std::ptrdiff_t m_clientOnlyEntityBehavior = 0x5b0; // CPointTemplate
			constexpr std::ptrdiff_t m_createdSpawnGroupHandles = 0x5b8; // CPointTemplate
			constexpr std::ptrdiff_t m_flTimeoutInterval = 0x580; // CPointTemplate
			constexpr std::ptrdiff_t m_iszEntityFilterName = 0x578; // CPointTemplate
			constexpr std::ptrdiff_t m_iszSource2EntityLumpName = 0x570; // CPointTemplate
			constexpr std::ptrdiff_t m_iszWorldName = 0x568; // CPointTemplate
			constexpr std::ptrdiff_t m_ownerSpawnGroupType = 0x5b4; // CPointTemplate
			constexpr std::ptrdiff_t m_pOutputOnSpawned = 0x588; // CPointTemplate
		}
		namespace CPrecipitationVData {
			constexpr std::ptrdiff_t m_bBatchSameVolumeType = 0x110; // CPrecipitationVData
			constexpr std::ptrdiff_t m_flInnerDistance = 0x108; // CPrecipitationVData
			constexpr std::ptrdiff_t m_nAttachType = 0x10c; // CPrecipitationVData
			constexpr std::ptrdiff_t m_nRTEnvCP = 0x114; // CPrecipitationVData
			constexpr std::ptrdiff_t m_nRTEnvCPComponent = 0x118; // CPrecipitationVData
			constexpr std::ptrdiff_t m_szModifier = 0x120; // CPrecipitationVData
			constexpr std::ptrdiff_t m_szParticlePrecipitationEffect = 0x28; // CPrecipitationVData
		}
		namespace CProjectedTextureBase {
			constexpr std::ptrdiff_t m_LightColor = 0x24; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_SpotlightTextureName = 0x54; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bAlwaysUpdate = 0x11; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bCameraSpace = 0x1c; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bEnableShadows = 0x18; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bFlipHorizontal = 0x26c; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bLightOnlyTarget = 0x1a; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bLightWorld = 0x1b; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bSimpleProjection = 0x19; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bState = 0x10; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_bVolumetric = 0x34; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flAmbient = 0x50; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flBrightnessScale = 0x20; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flColorTransitionTime = 0x4c; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flFarZ = 0x260; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flFlashlightTime = 0x40; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flIntensity = 0x28; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flLightFOV = 0x14; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flLinearAttenuation = 0x2c; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flNearZ = 0x25c; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flNoiseStrength = 0x3c; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flPlaneOffset = 0x48; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flProjectionSize = 0x264; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flQuadraticAttenuation = 0x30; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flRotation = 0x268; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_flVolumetricIntensity = 0x38; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_hTargetEntity = 0xc; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_nNumPlanes = 0x44; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_nShadowQuality = 0x258; // CProjectedTextureBase
			constexpr std::ptrdiff_t m_nSpotlightTextureFrame = 0x254; // CProjectedTextureBase
		}
		namespace CPropDataComponent {
			constexpr std::ptrdiff_t m_bSpawnMotionDisabled = 0x34; // CPropDataComponent
			constexpr std::ptrdiff_t m_flDmgModBullet = 0x10; // CPropDataComponent
			constexpr std::ptrdiff_t m_flDmgModClub = 0x14; // CPropDataComponent
			constexpr std::ptrdiff_t m_flDmgModExplosive = 0x18; // CPropDataComponent
			constexpr std::ptrdiff_t m_flDmgModFire = 0x1c; // CPropDataComponent
			constexpr std::ptrdiff_t m_iszBasePropData = 0x28; // CPropDataComponent
			constexpr std::ptrdiff_t m_iszPhysicsDamageTableName = 0x20; // CPropDataComponent
			constexpr std::ptrdiff_t m_nDisableTakePhysicsDamageSpawnFlag = 0x38; // CPropDataComponent
			constexpr std::ptrdiff_t m_nInteractions = 0x30; // CPropDataComponent
			constexpr std::ptrdiff_t m_nMotionDisabledSpawnFlag = 0x3c; // CPropDataComponent
		}
		namespace CRagdollManager {
			constexpr std::ptrdiff_t m_iCurrentMaxRagdollCount = 0x568; // CRagdollManager
		}
		namespace CRenderComponent {
			constexpr std::ptrdiff_t __m_pChainEntity = 0x10; // CRenderComponent
			constexpr std::ptrdiff_t m_bEnableRendering = 0x60; // CRenderComponent
			constexpr std::ptrdiff_t m_bInterpolationReadyToDraw = 0xb0; // CRenderComponent
			constexpr std::ptrdiff_t m_bIsRenderingWithViewModels = 0x50; // CRenderComponent
			constexpr std::ptrdiff_t m_nSplitscreenFlags = 0x54; // CRenderComponent
		}
		namespace CSMatchStats_t {
			constexpr std::ptrdiff_t m_iEnemy3Ks = 0x70; // CSMatchStats_t
			constexpr std::ptrdiff_t m_iEnemy4Ks = 0x6c; // CSMatchStats_t
			constexpr std::ptrdiff_t m_iEnemy5Ks = 0x68; // CSMatchStats_t
			constexpr std::ptrdiff_t m_iEnemyKnifeKills = 0x74; // CSMatchStats_t
			constexpr std::ptrdiff_t m_iEnemyTaserKills = 0x78; // CSMatchStats_t
		}
		namespace CSPerRoundStats_t {
			constexpr std::ptrdiff_t m_iAssists = 0x38; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iCashEarned = 0x58; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iDamage = 0x3c; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iDeaths = 0x34; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iEnemiesFlashed = 0x60; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iEquipmentValue = 0x40; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iHeadShotKills = 0x50; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iKillReward = 0x48; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iKills = 0x30; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iLiveTime = 0x4c; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iMoneySaved = 0x44; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iObjective = 0x54; // CSPerRoundStats_t
			constexpr std::ptrdiff_t m_iUtilityDamage = 0x5c; // CSPerRoundStats_t
		}
		namespace CScriptComponent {
			constexpr std::ptrdiff_t m_scriptClassName = 0x30; // CScriptComponent
		}
		namespace CSkeletonInstance {
			constexpr std::ptrdiff_t m_bDirtyMotionType = 0x0; // CSkeletonInstance
			constexpr std::ptrdiff_t m_bDisableSolidCollisionsForHierarchy = 0x3a2; // CSkeletonInstance
			constexpr std::ptrdiff_t m_bIsAnimationEnabled = 0x3a0; // CSkeletonInstance
			constexpr std::ptrdiff_t m_bIsGeneratingLatchedParentSpaceState = 0x0; // CSkeletonInstance
			constexpr std::ptrdiff_t m_bUseParentRenderBounds = 0x3a1; // CSkeletonInstance
			constexpr std::ptrdiff_t m_materialGroup = 0x3a4; // CSkeletonInstance
			constexpr std::ptrdiff_t m_modelState = 0x170; // CSkeletonInstance
			constexpr std::ptrdiff_t m_nHitboxSet = 0x3a8; // CSkeletonInstance
		}
		namespace CSkyboxReference {
			constexpr std::ptrdiff_t m_hSkyCamera = 0x56c; // CSkyboxReference
			constexpr std::ptrdiff_t m_worldGroupId = 0x568; // CSkyboxReference
		}
		namespace CTimeline {
			constexpr std::ptrdiff_t m_bStopped = 0x220; // CTimeline
			constexpr std::ptrdiff_t m_flFinalValue = 0x218; // CTimeline
			constexpr std::ptrdiff_t m_flInterval = 0x214; // CTimeline
			constexpr std::ptrdiff_t m_flValues = 0x10; // CTimeline
			constexpr std::ptrdiff_t m_nBucketCount = 0x210; // CTimeline
			constexpr std::ptrdiff_t m_nCompressionType = 0x21c; // CTimeline
			constexpr std::ptrdiff_t m_nValueCounts = 0x110; // CTimeline
		}
		namespace C_AttributeContainer {
			constexpr std::ptrdiff_t m_Item = 0x50; // C_AttributeContainer
			constexpr std::ptrdiff_t m_iExternalItemProviderRegisteredToken = 0x498; // C_AttributeContainer
			constexpr std::ptrdiff_t m_ullRegisteredAsItemID = 0x4a0; // C_AttributeContainer
		}
		namespace C_BarnLight {
			constexpr std::ptrdiff_t m_Color = 0xd30; // C_BarnLight
			constexpr std::ptrdiff_t m_LightStyleEvents = 0xd80; // C_BarnLight
			constexpr std::ptrdiff_t m_LightStyleString = 0xd58; // C_BarnLight
			constexpr std::ptrdiff_t m_LightStyleTargets = 0xd98; // C_BarnLight
			constexpr std::ptrdiff_t m_QueuedLightStyleStrings = 0xd68; // C_BarnLight
			constexpr std::ptrdiff_t m_StyleEvent = 0xdb0; // C_BarnLight
			constexpr std::ptrdiff_t m_VisClusters = 0x1050; // C_BarnLight
			constexpr std::ptrdiff_t m_bContactShadow = 0xea4; // C_BarnLight
			constexpr std::ptrdiff_t m_bEnabled = 0xd28; // C_BarnLight
			constexpr std::ptrdiff_t m_bFogMixedShadows = 0xed4; // C_BarnLight
			constexpr std::ptrdiff_t m_bInitialBoneSetup = 0x1048; // C_BarnLight
			constexpr std::ptrdiff_t m_bPrecomputedFieldsValid = 0xee8; // C_BarnLight
			constexpr std::ptrdiff_t m_fAlternateColorBrightness = 0xec0; // C_BarnLight
			constexpr std::ptrdiff_t m_flBounceScale = 0xeac; // C_BarnLight
			constexpr std::ptrdiff_t m_flBrightness = 0xd38; // C_BarnLight
			constexpr std::ptrdiff_t m_flBrightnessScale = 0xd3c; // C_BarnLight
			constexpr std::ptrdiff_t m_flColorTemperature = 0xd34; // C_BarnLight
			constexpr std::ptrdiff_t m_flFadeSizeEnd = 0xedc; // C_BarnLight
			constexpr std::ptrdiff_t m_flFadeSizeStart = 0xed8; // C_BarnLight
			constexpr std::ptrdiff_t m_flFogScale = 0xed0; // C_BarnLight
			constexpr std::ptrdiff_t m_flFogStrength = 0xec8; // C_BarnLight
			constexpr std::ptrdiff_t m_flLightStyleStartTime = 0xd60; // C_BarnLight
			constexpr std::ptrdiff_t m_flLuminaireAnisotropy = 0xd50; // C_BarnLight
			constexpr std::ptrdiff_t m_flLuminaireSize = 0xd4c; // C_BarnLight
			constexpr std::ptrdiff_t m_flMinRoughness = 0xeb0; // C_BarnLight
			constexpr std::ptrdiff_t m_flRange = 0xe78; // C_BarnLight
			constexpr std::ptrdiff_t m_flShadowFadeSizeEnd = 0xee4; // C_BarnLight
			constexpr std::ptrdiff_t m_flShadowFadeSizeStart = 0xee0; // C_BarnLight
			constexpr std::ptrdiff_t m_flShape = 0xe58; // C_BarnLight
			constexpr std::ptrdiff_t m_flSkirt = 0xe64; // C_BarnLight
			constexpr std::ptrdiff_t m_flSkirtNear = 0xe68; // C_BarnLight
			constexpr std::ptrdiff_t m_flSoftX = 0xe5c; // C_BarnLight
			constexpr std::ptrdiff_t m_flSoftY = 0xe60; // C_BarnLight
			constexpr std::ptrdiff_t m_hLightCookie = 0xe50; // C_BarnLight
			constexpr std::ptrdiff_t m_nBakeSpecularToCubemaps = 0xe88; // C_BarnLight
			constexpr std::ptrdiff_t m_nBakedShadowIndex = 0xd44; // C_BarnLight
			constexpr std::ptrdiff_t m_nBounceLight = 0xea8; // C_BarnLight
			constexpr std::ptrdiff_t m_nCastShadows = 0xe98; // C_BarnLight
			constexpr std::ptrdiff_t m_nColorMode = 0xd2c; // C_BarnLight
			constexpr std::ptrdiff_t m_nDirectLight = 0xd40; // C_BarnLight
			constexpr std::ptrdiff_t m_nFog = 0xec4; // C_BarnLight
			constexpr std::ptrdiff_t m_nFogShadows = 0xecc; // C_BarnLight
			constexpr std::ptrdiff_t m_nLuminaireShape = 0xd48; // C_BarnLight
			constexpr std::ptrdiff_t m_nPrecomputedSubFrusta = 0xf28; // C_BarnLight
			constexpr std::ptrdiff_t m_nShadowMapSize = 0xe9c; // C_BarnLight
			constexpr std::ptrdiff_t m_nShadowPriority = 0xea0; // C_BarnLight
			constexpr std::ptrdiff_t m_vAlternateColor = 0xeb4; // C_BarnLight
			constexpr std::ptrdiff_t m_vBakeSpecularToCubemapsSize = 0xe8c; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedBoundsMaxs = 0xef8; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedBoundsMins = 0xeec; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles = 0xf10; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles0 = 0xf38; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles1 = 0xf5c; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles2 = 0xf80; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles3 = 0xfa4; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles4 = 0xfc8; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBAngles5 = 0xfec; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent = 0xf1c; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent0 = 0xf44; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent1 = 0xf68; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent2 = 0xf8c; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent3 = 0xfb0; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent4 = 0xfd4; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBExtent5 = 0xff8; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin = 0xf04; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin0 = 0xf2c; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin1 = 0xf50; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin2 = 0xf74; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin3 = 0xf98; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin4 = 0xfbc; // C_BarnLight
			constexpr std::ptrdiff_t m_vPrecomputedOBBOrigin5 = 0xfe0; // C_BarnLight
			constexpr std::ptrdiff_t m_vShear = 0xe7c; // C_BarnLight
			constexpr std::ptrdiff_t m_vSizeParams = 0xe6c; // C_BarnLight
		}
		namespace C_BaseButton {
			constexpr std::ptrdiff_t m_glowEntity = 0xd28; // C_BaseButton
			constexpr std::ptrdiff_t m_szDisplayText = 0xd30; // C_BaseButton
			constexpr std::ptrdiff_t m_usable = 0xd2c; // C_BaseButton
		}
		namespace C_BaseCSGrenade {
			constexpr std::ptrdiff_t m_bClientPredictDelete = 0x1b20; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_bIsHeldByPlayer = 0x1b22; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_bJumpThrow = 0x1b24; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_bJustPulledPin = 0x1b3c; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_bPinPulled = 0x1b23; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_bRedraw = 0x1b21; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_bThrowAnimating = 0x1b25; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_fDropTime = 0x1b34; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_fPinPullTime = 0x1b38; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_fThrowTime = 0x1b28; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_flNextHoldFrac = 0x1b44; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_flThrowStrength = 0x1b2c; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_flThrowStrengthApproach = 0x1b30; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_hSwitchToWeaponAfterThrow = 0x1b48; // C_BaseCSGrenade
			constexpr std::ptrdiff_t m_nNextHoldTick = 0x1b40; // C_BaseCSGrenade
		}
		namespace C_BaseCSGrenadeProjectile {
			constexpr std::ptrdiff_t flNextTrailLineTime = 0x11b8; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_arrTrajectoryTrailPointCreationTimes = 0x11e8; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_arrTrajectoryTrailPoints = 0x11d0; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_bCanCreateGrenadeTrail = 0x11bd; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_bExplodeEffectBegan = 0x11bc; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_flSpawnTime = 0x11a8; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_flTrajectoryTrailEffectCreationTime = 0x1200; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_hSnapshotTrajectoryParticleSnapshot = 0x11c8; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_nBounces = 0x1188; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_nExplodeEffectIndex = 0x1190; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_nExplodeEffectTickBegin = 0x1198; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_nSnapshotTrajectoryEffectIndex = 0x11c0; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_vInitialPosition = 0x1170; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_vInitialVelocity = 0x117c; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t m_vecExplodeEffectOrigin = 0x119c; // C_BaseCSGrenadeProjectile
			constexpr std::ptrdiff_t vecLastTrailLinePos = 0x11ac; // C_BaseCSGrenadeProjectile
		}
		namespace C_BaseClientUIEntity {
			constexpr std::ptrdiff_t m_DialogXMLName = 0xd38; // C_BaseClientUIEntity
			constexpr std::ptrdiff_t m_PanelClassName = 0xd40; // C_BaseClientUIEntity
			constexpr std::ptrdiff_t m_PanelID = 0xd48; // C_BaseClientUIEntity
			constexpr std::ptrdiff_t m_bEnabled = 0xd30; // C_BaseClientUIEntity
		}
		namespace C_BaseCombatCharacter {
			constexpr std::ptrdiff_t m_flWaterNextTraceTime = 0x1144; // C_BaseCombatCharacter
			constexpr std::ptrdiff_t m_flWaterWorldZ = 0x1140; // C_BaseCombatCharacter
			constexpr std::ptrdiff_t m_hMyWearables = 0x1120; // C_BaseCombatCharacter
			constexpr std::ptrdiff_t m_leftFootAttachment = 0x1138; // C_BaseCombatCharacter
			constexpr std::ptrdiff_t m_nWaterWakeMode = 0x113c; // C_BaseCombatCharacter
			constexpr std::ptrdiff_t m_rightFootAttachment = 0x1139; // C_BaseCombatCharacter
		}
		namespace C_BaseDoor {
			constexpr std::ptrdiff_t m_bIsUsable = 0xd28; // C_BaseDoor
		}
		namespace C_BaseEntity {
			constexpr std::ptrdiff_t m_CBodyComponent = 0x38; // C_BaseEntity
			constexpr std::ptrdiff_t m_DataChangeEventRef = 0x524; // C_BaseEntity
			constexpr std::ptrdiff_t m_EntClientFlags = 0x3e0; // C_BaseEntity
			constexpr std::ptrdiff_t m_ListEntry = 0x3c0; // C_BaseEntity
			constexpr std::ptrdiff_t m_MoveCollide = 0x444; // C_BaseEntity
			constexpr std::ptrdiff_t m_MoveType = 0x445; // C_BaseEntity
			constexpr std::ptrdiff_t m_NetworkTransmitComponent = 0x40; // C_BaseEntity
			constexpr std::ptrdiff_t m_Particles = 0x498; // C_BaseEntity
			constexpr std::ptrdiff_t m_aThinkFunctions = 0x390; // C_BaseEntity
			constexpr std::ptrdiff_t m_bAnimTimeChanged = 0x54d; // C_BaseEntity
			constexpr std::ptrdiff_t m_bAnimatedEveryTick = 0x468; // C_BaseEntity
			constexpr std::ptrdiff_t m_bApplyLayerMatchIDToModel = 0x373; // C_BaseEntity
			constexpr std::ptrdiff_t m_bClientSideRagdoll = 0x3e2; // C_BaseEntity
			constexpr std::ptrdiff_t m_bDisabledContextThinks = 0x3a8; // C_BaseEntity
			constexpr std::ptrdiff_t m_bHasAddedVarsToInterpolation = 0x3b6; // C_BaseEntity
			constexpr std::ptrdiff_t m_bHasSuccessfullyInterpolated = 0x3b5; // C_BaseEntity
			constexpr std::ptrdiff_t m_bInterpolateEvenWithNoModel = 0x371; // C_BaseEntity
			constexpr std::ptrdiff_t m_bPredictable = 0x481; // C_BaseEntity
			constexpr std::ptrdiff_t m_bPredictionEligible = 0x372; // C_BaseEntity
			constexpr std::ptrdiff_t m_bRenderEvenWhenNotSuccessfullyInterpolated = 0x3b7; // C_BaseEntity
			constexpr std::ptrdiff_t m_bRenderWithViewModels = 0x482; // C_BaseEntity
			constexpr std::ptrdiff_t m_bSimulationTimeChanged = 0x54e; // C_BaseEntity
			constexpr std::ptrdiff_t m_bTakesDamage = 0x349; // C_BaseEntity
			constexpr std::ptrdiff_t m_dependencies = 0x528; // C_BaseEntity
			constexpr std::ptrdiff_t m_fBBoxVisFlags = 0x480; // C_BaseEntity
			constexpr std::ptrdiff_t m_fEffects = 0x44c; // C_BaseEntity
			constexpr std::ptrdiff_t m_fFlags = 0x3ec; // C_BaseEntity
			constexpr std::ptrdiff_t m_flAnimTime = 0x3ac; // C_BaseEntity
			constexpr std::ptrdiff_t m_flCreateTime = 0x3d8; // C_BaseEntity
			constexpr std::ptrdiff_t m_flElasticity = 0x45c; // C_BaseEntity
			constexpr std::ptrdiff_t m_flFriction = 0x458; // C_BaseEntity
			constexpr std::ptrdiff_t m_flGravityScale = 0x460; // C_BaseEntity
			constexpr std::ptrdiff_t m_flNavIgnoreUntilTime = 0x46c; // C_BaseEntity
			constexpr std::ptrdiff_t m_flProxyRandomValue = 0x368; // C_BaseEntity
			constexpr std::ptrdiff_t m_flSimulationTime = 0x3b0; // C_BaseEntity
			constexpr std::ptrdiff_t m_flSpeed = 0x3dc; // C_BaseEntity
			constexpr std::ptrdiff_t m_flTimeScale = 0x464; // C_BaseEntity
			constexpr std::ptrdiff_t m_flWaterLevel = 0x448; // C_BaseEntity
			constexpr std::ptrdiff_t m_hEffectEntity = 0x43c; // C_BaseEntity
			constexpr std::ptrdiff_t m_hGroundEntity = 0x450; // C_BaseEntity
			constexpr std::ptrdiff_t m_hOldMoveParent = 0x490; // C_BaseEntity
			constexpr std::ptrdiff_t m_hOwnerEntity = 0x440; // C_BaseEntity
			constexpr std::ptrdiff_t m_hSceneObjectController = 0x35c; // C_BaseEntity
			constexpr std::ptrdiff_t m_hThink = 0x470; // C_BaseEntity
			constexpr std::ptrdiff_t m_iCurrentThinkContext = 0x38c; // C_BaseEntity
			constexpr std::ptrdiff_t m_iEFlags = 0x36c; // C_BaseEntity
			constexpr std::ptrdiff_t m_iHealth = 0x344; // C_BaseEntity
			constexpr std::ptrdiff_t m_iMaxHealth = 0x340; // C_BaseEntity
			constexpr std::ptrdiff_t m_iTeamNum = 0x3e3; // C_BaseEntity
			constexpr std::ptrdiff_t m_lifeState = 0x348; // C_BaseEntity
			constexpr std::ptrdiff_t m_nActualMoveType = 0x446; // C_BaseEntity
			constexpr std::ptrdiff_t m_nBloodType = 0x560; // C_BaseEntity
			constexpr std::ptrdiff_t m_nCreationTick = 0x540; // C_BaseEntity
			constexpr std::ptrdiff_t m_nFirstPredictableCommand = 0x488; // C_BaseEntity
			constexpr std::ptrdiff_t m_nGroundBodyIndex = 0x454; // C_BaseEntity
			constexpr std::ptrdiff_t m_nInterpolationLatchDirtyFlags = 0x3b8; // C_BaseEntity
			constexpr std::ptrdiff_t m_nLastPredictableCommand = 0x48c; // C_BaseEntity
			constexpr std::ptrdiff_t m_nLastThinkTick = 0x320; // C_BaseEntity
			constexpr std::ptrdiff_t m_nNextScriptVarRecordID = 0x508; // C_BaseEntity
			constexpr std::ptrdiff_t m_nNextThinkTick = 0x3e8; // C_BaseEntity
			constexpr std::ptrdiff_t m_nNoInterpolationTick = 0x360; // C_BaseEntity
			constexpr std::ptrdiff_t m_nPlatformType = 0x358; // C_BaseEntity
			constexpr std::ptrdiff_t m_nSceneObjectOverrideFlags = 0x3b4; // C_BaseEntity
			constexpr std::ptrdiff_t m_nSimulationTick = 0x388; // C_BaseEntity
			constexpr std::ptrdiff_t m_nSplitUserPlayerPredictionSlot = 0x484; // C_BaseEntity
			constexpr std::ptrdiff_t m_nSubclassID = 0x378; // C_BaseEntity
			constexpr std::ptrdiff_t m_nTakeDamageFlags = 0x350; // C_BaseEntity
			constexpr std::ptrdiff_t m_nVisibilityNoInterpolationTick = 0x364; // C_BaseEntity
			constexpr std::ptrdiff_t m_nWaterType = 0x370; // C_BaseEntity
			constexpr std::ptrdiff_t m_pCollision = 0x338; // C_BaseEntity
			constexpr std::ptrdiff_t m_pGameSceneNode = 0x328; // C_BaseEntity
			constexpr std::ptrdiff_t m_pRenderComponent = 0x330; // C_BaseEntity
			constexpr std::ptrdiff_t m_sUniqueHammerID = 0x558; // C_BaseEntity
			constexpr std::ptrdiff_t m_spawnflags = 0x3e4; // C_BaseEntity
			constexpr std::ptrdiff_t m_tokLayerMatchID = 0x374; // C_BaseEntity
			constexpr std::ptrdiff_t m_ubInterpolationFrame = 0x359; // C_BaseEntity
			constexpr std::ptrdiff_t m_vecAbsVelocity = 0x3f0; // C_BaseEntity
			constexpr std::ptrdiff_t m_vecAngVelocity = 0x518; // C_BaseEntity
			constexpr std::ptrdiff_t m_vecBaseVelocity = 0x430; // C_BaseEntity
			constexpr std::ptrdiff_t m_vecPredictedScriptFloatIDs = 0x4d8; // C_BaseEntity
			constexpr std::ptrdiff_t m_vecPredictedScriptFloats = 0x4c0; // C_BaseEntity
			constexpr std::ptrdiff_t m_vecVelocity = 0x400; // C_BaseEntity
		}
		namespace C_BaseFire {
			constexpr std::ptrdiff_t m_flScale = 0x568; // C_BaseFire
			constexpr std::ptrdiff_t m_flScaleTime = 0x570; // C_BaseFire
			constexpr std::ptrdiff_t m_flStartScale = 0x56c; // C_BaseFire
			constexpr std::ptrdiff_t m_nFlags = 0x574; // C_BaseFire
		}
		namespace C_BaseFlex {
			constexpr std::ptrdiff_t m_CachedViewTarget = 0x102c; // C_BaseFlex
			constexpr std::ptrdiff_t m_PhonemeClasses = 0x10c0; // C_BaseFlex
			constexpr std::ptrdiff_t m_bResetFlexWeightsOnModelChange = 0x1056; // C_BaseFlex
			constexpr std::ptrdiff_t m_blinktime = 0x1040; // C_BaseFlex
			constexpr std::ptrdiff_t m_blinktoggle = 0xfc8; // C_BaseFlex
			constexpr std::ptrdiff_t m_flBlinkAmount = 0x1050; // C_BaseFlex
			constexpr std::ptrdiff_t m_flJawOpenAmount = 0x104c; // C_BaseFlex
			constexpr std::ptrdiff_t m_flexWeight = 0xf98; // C_BaseFlex
			constexpr std::ptrdiff_t m_iBlink = 0x103c; // C_BaseFlex
			constexpr std::ptrdiff_t m_iEyeAttachment = 0x1055; // C_BaseFlex
			constexpr std::ptrdiff_t m_iJawOpen = 0x1048; // C_BaseFlex
			constexpr std::ptrdiff_t m_iMouthAttachment = 0x1054; // C_BaseFlex
			constexpr std::ptrdiff_t m_mEyeOcclusionRendererCameraToBoneTransform = 0x1074; // C_BaseFlex
			constexpr std::ptrdiff_t m_nEyeOcclusionRendererBone = 0x1070; // C_BaseFlex
			constexpr std::ptrdiff_t m_nLastFlexUpdateFrameCount = 0x1028; // C_BaseFlex
			constexpr std::ptrdiff_t m_nNextSceneEventId = 0x1038; // C_BaseFlex
			constexpr std::ptrdiff_t m_prevblinktoggle = 0x1044; // C_BaseFlex
			constexpr std::ptrdiff_t m_vEyeOcclusionRendererHalfExtent = 0x10a4; // C_BaseFlex
			constexpr std::ptrdiff_t m_vLookTargetPosition = 0xfb0; // C_BaseFlex
		}
		namespace C_BaseFlex__Emphasized_Phoneme {
			constexpr std::ptrdiff_t m_bBasechecked = 0x1d; // C_BaseFlex__Emphasized_Phoneme
			constexpr std::ptrdiff_t m_bRequired = 0x1c; // C_BaseFlex__Emphasized_Phoneme
			constexpr std::ptrdiff_t m_bValid = 0x1e; // C_BaseFlex__Emphasized_Phoneme
			constexpr std::ptrdiff_t m_flAmount = 0x18; // C_BaseFlex__Emphasized_Phoneme
			constexpr std::ptrdiff_t m_sClassName = 0x0; // C_BaseFlex__Emphasized_Phoneme
		}
		namespace C_BaseGrenade {
			constexpr std::ptrdiff_t m_DmgRadius = 0x1124; // C_BaseGrenade
			constexpr std::ptrdiff_t m_ExplosionSound = 0x1140; // C_BaseGrenade
			constexpr std::ptrdiff_t m_bHasWarnedAI = 0x1120; // C_BaseGrenade
			constexpr std::ptrdiff_t m_bIsLive = 0x1122; // C_BaseGrenade
			constexpr std::ptrdiff_t m_bIsSmokeGrenade = 0x1121; // C_BaseGrenade
			constexpr std::ptrdiff_t m_flDamage = 0x1130; // C_BaseGrenade
			constexpr std::ptrdiff_t m_flDetonateTime = 0x1128; // C_BaseGrenade
			constexpr std::ptrdiff_t m_flNextAttack = 0x1164; // C_BaseGrenade
			constexpr std::ptrdiff_t m_flWarnAITime = 0x112c; // C_BaseGrenade
			constexpr std::ptrdiff_t m_hOriginalThrower = 0x1168; // C_BaseGrenade
			constexpr std::ptrdiff_t m_hThrower = 0x114c; // C_BaseGrenade
			constexpr std::ptrdiff_t m_iszBounceSound = 0x1138; // C_BaseGrenade
		}
		namespace C_BaseModelEntity {
			constexpr std::ptrdiff_t m_CHitboxComponent = 0xa58; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_CRenderComponent = 0xa50; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_ClientOverrideTint = 0xce8; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_Collision = 0xb50; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_ConfigEntitiesToPropagateMaterialDecalsTo = 0xc98; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_Glow = 0xc00; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_LastHitGroup = 0xa80; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_bAllowFadeInView = 0xaba; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_bInitModelEffects = 0xaa8; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_bIsStaticProp = 0xaa9; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_bNoInterpolate = 0xb49; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_bRenderToCubemaps = 0xb48; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_bUseClientOverrideTint = 0xcec; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_clrRender = 0xad8; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_fadeMaxDist = 0xc60; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_fadeMinDist = 0xc5c; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_flDecalHealBloodRate = 0xc8c; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_flDecalHealHeightRate = 0xc90; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_flFadeScale = 0xc64; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_flGlowBackfaceMult = 0xc58; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_flShadowStrength = 0xc68; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_iOldHealth = 0xab4; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_nAddDecal = 0xc70; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_nDecalsAdded = 0xab0; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_nLastAddDecal = 0xaac; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_nObjectCulling = 0xc6c; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_nRenderFX = 0xab9; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_nRenderMode = 0xab8; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_pClientAlphaProperty = 0xce0; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_vDecalForwardAxis = 0xc80; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_vDecalPosition = 0xc74; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_vecRenderAttributes = 0xae0; // C_BaseModelEntity
			constexpr std::ptrdiff_t m_vecViewOffset = 0xcb0; // C_BaseModelEntity
		}
		namespace C_BasePlayerPawn {
			constexpr std::ptrdiff_t m_ServerViewAngleChanges = 0x11f8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_bIsSwappingToPredictableController = 0x1340; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_flDeathTime = 0x12f8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_flFOVSensitivityAdjust = 0x131c; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_flLastCameraSetupTime = 0x1318; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_flMouseSensitivity = 0x1320; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_flOldSimulationTime = 0x1330; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_flPredictionErrorTime = 0x1308; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_hController = 0x133c; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_iHideHUD = 0x1264; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_nHighestConsumedServerViewAngleChangeIndex = 0x1248; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_nLastExecutedCommandNumber = 0x1334; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_nLastExecutedCommandTick = 0x1338; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pAutoaimServices = 0x11b8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pCameraServices = 0x11e0; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pFlashlightServices = 0x11d8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pItemServices = 0x11b0; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pMovementServices = 0x11e8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pObserverServices = 0x11c0; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pUseServices = 0x11d0; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pWaterServices = 0x11c8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_pWeaponServices = 0x11a8; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_skybox3d = 0x1268; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_vOldOrigin = 0x1324; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_vecLastCameraSetupLocalOrigin = 0x130c; // C_BasePlayerPawn
			constexpr std::ptrdiff_t m_vecPredictionError = 0x12fc; // C_BasePlayerPawn
			constexpr std::ptrdiff_t v_angle = 0x124c; // C_BasePlayerPawn
			constexpr std::ptrdiff_t v_anglePrevious = 0x1258; // C_BasePlayerPawn
		}
		namespace C_BasePlayerWeapon {
			constexpr std::ptrdiff_t m_flNextPrimaryAttackTickRatio = 0x166c; // C_BasePlayerWeapon
			constexpr std::ptrdiff_t m_flNextSecondaryAttackTickRatio = 0x1674; // C_BasePlayerWeapon
			constexpr std::ptrdiff_t m_iClip1 = 0x1678; // C_BasePlayerWeapon
			constexpr std::ptrdiff_t m_iClip2 = 0x167c; // C_BasePlayerWeapon
			constexpr std::ptrdiff_t m_nNextPrimaryAttackTick = 0x1668; // C_BasePlayerWeapon
			constexpr std::ptrdiff_t m_nNextSecondaryAttackTick = 0x1670; // C_BasePlayerWeapon
			constexpr std::ptrdiff_t m_pReserveAmmo = 0x1680; // C_BasePlayerWeapon
		}
		namespace C_BasePropDoor {
			constexpr std::ptrdiff_t m_bLocked = 0x123d; // C_BasePropDoor
			constexpr std::ptrdiff_t m_closedAngles = 0x124c; // C_BasePropDoor
			constexpr std::ptrdiff_t m_closedPosition = 0x1240; // C_BasePropDoor
			constexpr std::ptrdiff_t m_eDoorState = 0x1238; // C_BasePropDoor
			constexpr std::ptrdiff_t m_hMaster = 0x1258; // C_BasePropDoor
			constexpr std::ptrdiff_t m_modelChanged = 0x123c; // C_BasePropDoor
			constexpr std::ptrdiff_t m_vWhereToSetLightingOrigin = 0x125c; // C_BasePropDoor
		}
		namespace C_BaseTrigger {
			constexpr std::ptrdiff_t m_bClientSidePredicted = 0xd29; // C_BaseTrigger
			constexpr std::ptrdiff_t m_bDisabled = 0xd28; // C_BaseTrigger
		}
		namespace C_BaseViewModel {
			constexpr std::ptrdiff_t m_flAnimationStartTime = 0xfa4; // C_BaseViewModel
			constexpr std::ptrdiff_t m_hControlPanel = 0xfe8; // C_BaseViewModel
			constexpr std::ptrdiff_t m_hOldLayerSequence = 0xfdc; // C_BaseViewModel
			constexpr std::ptrdiff_t m_hWeapon = 0xfa8; // C_BaseViewModel
			constexpr std::ptrdiff_t m_iCameraAttachment = 0xfc0; // C_BaseViewModel
			constexpr std::ptrdiff_t m_nAnimationParity = 0xfa0; // C_BaseViewModel
			constexpr std::ptrdiff_t m_nOldAnimationParity = 0xfd8; // C_BaseViewModel
			constexpr std::ptrdiff_t m_nViewModelIndex = 0xf9c; // C_BaseViewModel
			constexpr std::ptrdiff_t m_oldLayer = 0xfe0; // C_BaseViewModel
			constexpr std::ptrdiff_t m_oldLayerStartTime = 0xfe4; // C_BaseViewModel
			constexpr std::ptrdiff_t m_previousCycle = 0xfd4; // C_BaseViewModel
			constexpr std::ptrdiff_t m_previousElapsedDuration = 0xfd0; // C_BaseViewModel
			constexpr std::ptrdiff_t m_sAnimationPrefix = 0xfb8; // C_BaseViewModel
			constexpr std::ptrdiff_t m_sVMName = 0xfb0; // C_BaseViewModel
			constexpr std::ptrdiff_t m_vecLastCameraAngles = 0xfc4; // C_BaseViewModel
			constexpr std::ptrdiff_t m_vecLastFacing = 0xf90; // C_BaseViewModel
		}
		namespace C_Beam {
			constexpr std::ptrdiff_t m_bTurnedOff = 0xdd0; // C_Beam
			constexpr std::ptrdiff_t m_fAmplitude = 0xdbc; // C_Beam
			constexpr std::ptrdiff_t m_fEndWidth = 0xdb0; // C_Beam
			constexpr std::ptrdiff_t m_fFadeLength = 0xdb4; // C_Beam
			constexpr std::ptrdiff_t m_fHaloScale = 0xdb8; // C_Beam
			constexpr std::ptrdiff_t m_fSpeed = 0xdc4; // C_Beam
			constexpr std::ptrdiff_t m_fStartFrame = 0xdc0; // C_Beam
			constexpr std::ptrdiff_t m_fWidth = 0xdac; // C_Beam
			constexpr std::ptrdiff_t m_flDamage = 0xd34; // C_Beam
			constexpr std::ptrdiff_t m_flFireTime = 0xd30; // C_Beam
			constexpr std::ptrdiff_t m_flFrame = 0xdc8; // C_Beam
			constexpr std::ptrdiff_t m_flFrameRate = 0xd28; // C_Beam
			constexpr std::ptrdiff_t m_flHDRColorScale = 0xd2c; // C_Beam
			constexpr std::ptrdiff_t m_hAttachEntity = 0xd78; // C_Beam
			constexpr std::ptrdiff_t m_hBaseMaterial = 0xd60; // C_Beam
			constexpr std::ptrdiff_t m_hEndEntity = 0xde0; // C_Beam
			constexpr std::ptrdiff_t m_nAttachIndex = 0xda0; // C_Beam
			constexpr std::ptrdiff_t m_nBeamFlags = 0xd74; // C_Beam
			constexpr std::ptrdiff_t m_nBeamType = 0xd70; // C_Beam
			constexpr std::ptrdiff_t m_nClipStyle = 0xdcc; // C_Beam
			constexpr std::ptrdiff_t m_nHaloIndex = 0xd68; // C_Beam
			constexpr std::ptrdiff_t m_nNumBeamEnts = 0xd38; // C_Beam
			constexpr std::ptrdiff_t m_queryHandleHalo = 0xd3c; // C_Beam
			constexpr std::ptrdiff_t m_vecEndPos = 0xdd4; // C_Beam
		}
		namespace C_BreakableProp {
			constexpr std::ptrdiff_t m_BreakableContentsType = 0x10a8; // C_BreakableProp
			constexpr std::ptrdiff_t m_CPropDataComponent = 0xfc8; // C_BreakableProp
			constexpr std::ptrdiff_t m_OnBreak = 0x1008; // C_BreakableProp
			constexpr std::ptrdiff_t m_OnHealthChanged = 0x1030; // C_BreakableProp
			constexpr std::ptrdiff_t m_OnTakeDamage = 0x1058; // C_BreakableProp
			constexpr std::ptrdiff_t m_PerformanceMode = 0x10a0; // C_BreakableProp
			constexpr std::ptrdiff_t m_bHasBreakPiecesOrCommands = 0x10c0; // C_BreakableProp
			constexpr std::ptrdiff_t m_explodeDamage = 0x10c4; // C_BreakableProp
			constexpr std::ptrdiff_t m_explodeRadius = 0x10c8; // C_BreakableProp
			constexpr std::ptrdiff_t m_explosionBuildupSound = 0x10d8; // C_BreakableProp
			constexpr std::ptrdiff_t m_explosionCustomEffect = 0x10e0; // C_BreakableProp
			constexpr std::ptrdiff_t m_explosionCustomSound = 0x10e8; // C_BreakableProp
			constexpr std::ptrdiff_t m_explosionDelay = 0x10d0; // C_BreakableProp
			constexpr std::ptrdiff_t m_explosionModifier = 0x10f0; // C_BreakableProp
			constexpr std::ptrdiff_t m_flDefBurstScale = 0x108c; // C_BreakableProp
			constexpr std::ptrdiff_t m_flDefaultFadeScale = 0x1100; // C_BreakableProp
			constexpr std::ptrdiff_t m_flLastPhysicsInfluenceTime = 0x10fc; // C_BreakableProp
			constexpr std::ptrdiff_t m_flPressureDelay = 0x1088; // C_BreakableProp
			constexpr std::ptrdiff_t m_flPreventDamageBeforeTime = 0x10a4; // C_BreakableProp
			constexpr std::ptrdiff_t m_hBreaker = 0x109c; // C_BreakableProp
			constexpr std::ptrdiff_t m_hFlareEnt = 0x1108; // C_BreakableProp
			constexpr std::ptrdiff_t m_hLastAttacker = 0x1104; // C_BreakableProp
			constexpr std::ptrdiff_t m_hPhysicsAttacker = 0x10f8; // C_BreakableProp
			constexpr std::ptrdiff_t m_iMinHealthDmg = 0x1084; // C_BreakableProp
			constexpr std::ptrdiff_t m_impactEnergyScale = 0x1080; // C_BreakableProp
			constexpr std::ptrdiff_t m_noGhostCollision = 0x110c; // C_BreakableProp
			constexpr std::ptrdiff_t m_strBreakableContentsParticleOverride = 0x10b8; // C_BreakableProp
			constexpr std::ptrdiff_t m_strBreakableContentsPropGroupOverride = 0x10b0; // C_BreakableProp
			constexpr std::ptrdiff_t m_vDefBurstOffset = 0x1090; // C_BreakableProp
		}
		namespace C_BulletHitModel {
			constexpr std::ptrdiff_t m_bIsHit = 0xfc0; // C_BulletHitModel
			constexpr std::ptrdiff_t m_flTimeCreated = 0xfc4; // C_BulletHitModel
			constexpr std::ptrdiff_t m_hPlayerParent = 0xfbc; // C_BulletHitModel
			constexpr std::ptrdiff_t m_iBoneIndex = 0xfb8; // C_BulletHitModel
			constexpr std::ptrdiff_t m_matLocal = 0xf88; // C_BulletHitModel
			constexpr std::ptrdiff_t m_vecStartPos = 0xfc8; // C_BulletHitModel
		}
		namespace C_C4 {
			constexpr std::ptrdiff_t m_activeLightParticleIndex = 0x1b40; // C_C4
			constexpr std::ptrdiff_t m_bBombPlacedAnimation = 0x1b50; // C_C4
			constexpr std::ptrdiff_t m_bBombPlanted = 0x1b7b; // C_C4
			constexpr std::ptrdiff_t m_bIsPlantingViaUse = 0x1b51; // C_C4
			constexpr std::ptrdiff_t m_bPlayedArmingBeeps = 0x1b74; // C_C4
			constexpr std::ptrdiff_t m_bStartedArming = 0x1b48; // C_C4
			constexpr std::ptrdiff_t m_eActiveLightEffect = 0x1b44; // C_C4
			constexpr std::ptrdiff_t m_entitySpottedState = 0x1b58; // C_C4
			constexpr std::ptrdiff_t m_fArmedTime = 0x1b4c; // C_C4
			constexpr std::ptrdiff_t m_nSpotRules = 0x1b70; // C_C4
			constexpr std::ptrdiff_t m_szScreenText = 0x1b20; // C_C4
		}
		namespace C_CSGOViewModel {
			constexpr std::ptrdiff_t m_bNeedToQueueHighResComposite = 0x1028; // C_CSGOViewModel
			constexpr std::ptrdiff_t m_bShouldIgnoreOffsetAndAccuracy = 0x1021; // C_CSGOViewModel
			constexpr std::ptrdiff_t m_nLastKnownAssociatedWeaponEntIndex = 0x1024; // C_CSGOViewModel
			constexpr std::ptrdiff_t m_vLoweredWeaponOffset = 0x1078; // C_CSGOViewModel
		}
		namespace C_CSGO_MapPreviewCameraPath {
			constexpr std::ptrdiff_t m_bConstantSpeed = 0x572; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_bLoop = 0x570; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_bVerticalFOV = 0x571; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_flDuration = 0x574; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_flPathDuration = 0x5bc; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_flPathLength = 0x5b8; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_flZFar = 0x568; // C_CSGO_MapPreviewCameraPath
			constexpr std::ptrdiff_t m_flZNear = 0x56c; // C_CSGO_MapPreviewCameraPath
		}
		namespace C_CSGO_MapPreviewCameraPathNode {
			constexpr std::ptrdiff_t m_flCameraSpeed = 0x590; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_flEaseIn = 0x594; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_flEaseOut = 0x598; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_flFOV = 0x58c; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_nPathIndex = 0x570; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_szParentPathUniqueID = 0x568; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_vInTangentLocal = 0x574; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_vInTangentWorld = 0x59c; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_vOutTangentLocal = 0x580; // C_CSGO_MapPreviewCameraPathNode
			constexpr std::ptrdiff_t m_vOutTangentWorld = 0x5a8; // C_CSGO_MapPreviewCameraPathNode
		}
		namespace C_CSGO_PreviewModel {
			constexpr std::ptrdiff_t m_animgraph = 0x1120; // C_CSGO_PreviewModel
			constexpr std::ptrdiff_t m_animgraphCharacterModeString = 0x1128; // C_CSGO_PreviewModel
			constexpr std::ptrdiff_t m_defaultAnim = 0x1130; // C_CSGO_PreviewModel
			constexpr std::ptrdiff_t m_flInitialModelScale = 0x113c; // C_CSGO_PreviewModel
			constexpr std::ptrdiff_t m_nDefaultAnimLoopMode = 0x1138; // C_CSGO_PreviewModel
			constexpr std::ptrdiff_t m_sInitialWeaponState = 0x1140; // C_CSGO_PreviewModel
		}
		namespace C_CSGO_PreviewPlayer {
			constexpr std::ptrdiff_t m_animgraph = 0x3a40; // C_CSGO_PreviewPlayer
			constexpr std::ptrdiff_t m_animgraphCharacterModeString = 0x3a48; // C_CSGO_PreviewPlayer
			constexpr std::ptrdiff_t m_flInitialModelScale = 0x3a50; // C_CSGO_PreviewPlayer
		}
		namespace C_CSGO_TeamPreviewCamera {
			constexpr std::ptrdiff_t m_bDofEnabled = 0x5dc; // C_CSGO_TeamPreviewCamera
			constexpr std::ptrdiff_t m_flDofFarBlurry = 0x5ec; // C_CSGO_TeamPreviewCamera
			constexpr std::ptrdiff_t m_flDofFarCrisp = 0x5e8; // C_CSGO_TeamPreviewCamera
			constexpr std::ptrdiff_t m_flDofNearBlurry = 0x5e0; // C_CSGO_TeamPreviewCamera
			constexpr std::ptrdiff_t m_flDofNearCrisp = 0x5e4; // C_CSGO_TeamPreviewCamera
			constexpr std::ptrdiff_t m_flDofTiltToGround = 0x5f0; // C_CSGO_TeamPreviewCamera
			constexpr std::ptrdiff_t m_nVariant = 0x5d8; // C_CSGO_TeamPreviewCamera
		}
		namespace C_CSGO_TeamPreviewCharacterPosition {
			constexpr std::ptrdiff_t m_agentItem = 0x588; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_glovesItem = 0x9d0; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_nOrdinal = 0x570; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_nRandom = 0x56c; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_nVariant = 0x568; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_sWeaponName = 0x578; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_weaponItem = 0xe18; // C_CSGO_TeamPreviewCharacterPosition
			constexpr std::ptrdiff_t m_xuid = 0x580; // C_CSGO_TeamPreviewCharacterPosition
		}
		namespace C_CSGameRules {
			constexpr std::ptrdiff_t m_MatchDevice = 0xa8; // C_CSGameRules
			constexpr std::ptrdiff_t m_MinimapVerticalSectionHeights = 0xc38; // C_CSGameRules
			constexpr std::ptrdiff_t m_RetakeRules = 0xda0; // C_CSGameRules
			constexpr std::ptrdiff_t m_TeamRespawnWaveTimes = 0xb1c; // C_CSGameRules
			constexpr std::ptrdiff_t m_arrProhibitedItemIndices = 0x8c4; // C_CSGameRules
			constexpr std::ptrdiff_t m_arrTournamentActiveCasterAccounts = 0x98c; // C_CSGameRules
			constexpr std::ptrdiff_t m_bAnyHostageReached = 0x94; // C_CSGameRules
			constexpr std::ptrdiff_t m_bBombDropped = 0x9a4; // C_CSGameRules
			constexpr std::ptrdiff_t m_bBombPlanted = 0x9a5; // C_CSGameRules
			constexpr std::ptrdiff_t m_bCTCantBuy = 0x9b1; // C_CSGameRules
			constexpr std::ptrdiff_t m_bCTTimeOutActive = 0x4e; // C_CSGameRules
			constexpr std::ptrdiff_t m_bFreezePeriod = 0x40; // C_CSGameRules
			constexpr std::ptrdiff_t m_bGameRestart = 0x74; // C_CSGameRules
			constexpr std::ptrdiff_t m_bHasMatchStarted = 0xac; // C_CSGameRules
			constexpr std::ptrdiff_t m_bHasTriggeredRoundStartMusic = 0xd7c; // C_CSGameRules
			constexpr std::ptrdiff_t m_bIsDroppingItems = 0x8c0; // C_CSGameRules
			constexpr std::ptrdiff_t m_bIsHltvActive = 0x8c2; // C_CSGameRules
			constexpr std::ptrdiff_t m_bIsQuestEligible = 0x8c1; // C_CSGameRules
			constexpr std::ptrdiff_t m_bIsQueuedMatchmaking = 0x98; // C_CSGameRules
			constexpr std::ptrdiff_t m_bIsValveDS = 0xa0; // C_CSGameRules
			constexpr std::ptrdiff_t m_bLogoMap = 0xa1; // C_CSGameRules
			constexpr std::ptrdiff_t m_bMapHasBombTarget = 0x95; // C_CSGameRules
			constexpr std::ptrdiff_t m_bMapHasBuyZone = 0x97; // C_CSGameRules
			constexpr std::ptrdiff_t m_bMapHasRescueZone = 0x96; // C_CSGameRules
			constexpr std::ptrdiff_t m_bMarkClientStopRecordAtRoundEnd = 0xcd0; // C_CSGameRules
			constexpr std::ptrdiff_t m_bMatchWaitingForResume = 0x61; // C_CSGameRules
			constexpr std::ptrdiff_t m_bPlayAllStepSoundsOnServer = 0xa2; // C_CSGameRules
			constexpr std::ptrdiff_t m_bRoundEndNoMusic = 0xefc; // C_CSGameRules
			constexpr std::ptrdiff_t m_bRoundEndShowTimerDefend = 0xed0; // C_CSGameRules
			constexpr std::ptrdiff_t m_bServerPaused = 0x4c; // C_CSGameRules
			constexpr std::ptrdiff_t m_bSpawnedTerrorHuntHeavy = 0xc58; // C_CSGameRules
			constexpr std::ptrdiff_t m_bSwitchingTeamsAtRoundReset = 0xd7d; // C_CSGameRules
			constexpr std::ptrdiff_t m_bTCantBuy = 0x9b0; // C_CSGameRules
			constexpr std::ptrdiff_t m_bTeamIntroPeriod = 0xec4; // C_CSGameRules
			constexpr std::ptrdiff_t m_bTechnicalTimeOut = 0x60; // C_CSGameRules
			constexpr std::ptrdiff_t m_bTerroristTimeOutActive = 0x4d; // C_CSGameRules
			constexpr std::ptrdiff_t m_bWarmupPeriod = 0x41; // C_CSGameRules
			constexpr std::ptrdiff_t m_eRoundEndReason = 0xecc; // C_CSGameRules
			constexpr std::ptrdiff_t m_eRoundWinReason = 0x9ac; // C_CSGameRules
			constexpr std::ptrdiff_t m_fMatchStartTime = 0x68; // C_CSGameRules
			constexpr std::ptrdiff_t m_fRoundStartTime = 0x6c; // C_CSGameRules
			constexpr std::ptrdiff_t m_fWarmupPeriodEnd = 0x44; // C_CSGameRules
			constexpr std::ptrdiff_t m_fWarmupPeriodStart = 0x48; // C_CSGameRules
			constexpr std::ptrdiff_t m_flCMMItemDropRevealEndTime = 0x8bc; // C_CSGameRules
			constexpr std::ptrdiff_t m_flCMMItemDropRevealStartTime = 0x8b8; // C_CSGameRules
			constexpr std::ptrdiff_t m_flCTTimeOutRemaining = 0x54; // C_CSGameRules
			constexpr std::ptrdiff_t m_flGameStartTime = 0x78; // C_CSGameRules
			constexpr std::ptrdiff_t m_flLastPerfSampleTime = 0x4f18; // C_CSGameRules
			constexpr std::ptrdiff_t m_flNextRespawnWave = 0xb9c; // C_CSGameRules
			constexpr std::ptrdiff_t m_flRestartRoundTime = 0x70; // C_CSGameRules
			constexpr std::ptrdiff_t m_flTerroristTimeOutRemaining = 0x50; // C_CSGameRules
			constexpr std::ptrdiff_t m_gamePhase = 0x80; // C_CSGameRules
			constexpr std::ptrdiff_t m_iHostagesRemaining = 0x90; // C_CSGameRules
			constexpr std::ptrdiff_t m_iMatchStats_PlayersAlive_CT = 0xa2c; // C_CSGameRules
			constexpr std::ptrdiff_t m_iMatchStats_PlayersAlive_T = 0xaa4; // C_CSGameRules
			constexpr std::ptrdiff_t m_iMatchStats_RoundResults = 0x9b4; // C_CSGameRules
			constexpr std::ptrdiff_t m_iNumConsecutiveCTLoses = 0xcb0; // C_CSGameRules
			constexpr std::ptrdiff_t m_iNumConsecutiveTerroristLoses = 0xcb4; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndFunFactData1 = 0xee4; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndFunFactData2 = 0xee8; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndFunFactData3 = 0xeec; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndFunFactPlayerSlot = 0xee0; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndLegacy = 0xf00; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndPlayerCount = 0xef8; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndTimerTime = 0xed4; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundEndWinnerTeam = 0xec8; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundStartRoundNumber = 0xf08; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundTime = 0x64; // C_CSGameRules
			constexpr std::ptrdiff_t m_iRoundWinStatus = 0x9a8; // C_CSGameRules
			constexpr std::ptrdiff_t m_iSpectatorSlotCount = 0xa4; // C_CSGameRules
			constexpr std::ptrdiff_t m_nCTTeamIntroVariant = 0xec0; // C_CSGameRules
			constexpr std::ptrdiff_t m_nCTTimeOuts = 0x5c; // C_CSGameRules
			constexpr std::ptrdiff_t m_nEndMatchMapGroupVoteOptions = 0xc84; // C_CSGameRules
			constexpr std::ptrdiff_t m_nEndMatchMapGroupVoteTypes = 0xc5c; // C_CSGameRules
			constexpr std::ptrdiff_t m_nEndMatchMapVoteWinner = 0xcac; // C_CSGameRules
			constexpr std::ptrdiff_t m_nHalloweenMaskListSeed = 0x9a0; // C_CSGameRules
			constexpr std::ptrdiff_t m_nMatchAbortedEarlyReason = 0xd78; // C_CSGameRules
			constexpr std::ptrdiff_t m_nMatchEndCount = 0xeb8; // C_CSGameRules
			constexpr std::ptrdiff_t m_nNextMapInMapgroup = 0xb0; // C_CSGameRules
			constexpr std::ptrdiff_t m_nOvertimePlaying = 0x8c; // C_CSGameRules
			constexpr std::ptrdiff_t m_nQueuedMatchmakingMode = 0x9c; // C_CSGameRules
			constexpr std::ptrdiff_t m_nRoundEndCount = 0xf04; // C_CSGameRules
			constexpr std::ptrdiff_t m_nRoundStartCount = 0xf0c; // C_CSGameRules
			constexpr std::ptrdiff_t m_nRoundsPlayedThisPhase = 0x88; // C_CSGameRules
			constexpr std::ptrdiff_t m_nServerQuestID = 0xc1c; // C_CSGameRules
			constexpr std::ptrdiff_t m_nTTeamIntroVariant = 0xebc; // C_CSGameRules
			constexpr std::ptrdiff_t m_nTerroristTimeOuts = 0x58; // C_CSGameRules
			constexpr std::ptrdiff_t m_nTournamentPredictionsPct = 0x8b4; // C_CSGameRules
			constexpr std::ptrdiff_t m_numBestOfMaps = 0x99c; // C_CSGameRules
			constexpr std::ptrdiff_t m_pGameModeRules = 0xd98; // C_CSGameRules
			constexpr std::ptrdiff_t m_sRoundEndFunFactToken = 0xed8; // C_CSGameRules
			constexpr std::ptrdiff_t m_sRoundEndMessage = 0xef0; // C_CSGameRules
			constexpr std::ptrdiff_t m_szMatchStatTxt = 0x4b4; // C_CSGameRules
			constexpr std::ptrdiff_t m_szTournamentEventName = 0xb4; // C_CSGameRules
			constexpr std::ptrdiff_t m_szTournamentEventStage = 0x2b4; // C_CSGameRules
			constexpr std::ptrdiff_t m_szTournamentPredictionsTxt = 0x6b4; // C_CSGameRules
			constexpr std::ptrdiff_t m_timeUntilNextPhaseStarts = 0x7c; // C_CSGameRules
			constexpr std::ptrdiff_t m_totalRoundsPlayed = 0x84; // C_CSGameRules
			constexpr std::ptrdiff_t m_vMinimapMaxs = 0xc2c; // C_CSGameRules
			constexpr std::ptrdiff_t m_vMinimapMins = 0xc20; // C_CSGameRules
		}
		namespace C_CSGameRulesProxy {
			constexpr std::ptrdiff_t m_pGameRules = 0x568; // C_CSGameRulesProxy
		}
		namespace C_CSObserverPawn {
			constexpr std::ptrdiff_t m_hDetectParentChange = 0x1510; // C_CSObserverPawn
		}
		namespace C_CSPlayerPawn {
			constexpr std::ptrdiff_t m_ArmorValue = 0x241c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_EconGloves = 0x1768; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_GunGameImmunityColor = 0x2310; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_PredictedDamageTags = 0x24b8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_RetakesMVPBoostExtraUtility = 0x1740; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_aimPunchAngle = 0x1584; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_aimPunchAngleVel = 0x1590; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_aimPunchCache = 0x15a8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_aimPunchTickBase = 0x159c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_aimPunchTickFraction = 0x15a0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_angShootAngleHistory = 0x246c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_angStashedShootAngles = 0x2448; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bGrenadeParametersStashed = 0x2444; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bHasDeathInfo = 0x242d; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bHasFemaleVoice = 0x1550; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bInBombZone = 0x15d1; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bInBuyZone = 0x1580; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bInHostageRescueZone = 0x15d0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bInLanding = 0x15c8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bInNoDefuseArea = 0x23f4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bIsBuyMenuOpen = 0x15d2; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bIsDefusing = 0x23ea; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bIsGrabbingHostage = 0x23eb; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bIsScoped = 0x23e8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bIsWalking = 0x2378; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bKilledByHeadshot = 0x2419; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bLastHeadBoneTransformIsValid = 0x2290; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bLeftHanded = 0x22c1; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bMustSyncRagdollState = 0x1bb1; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bNeedToReApplyGloves = 0x1760; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bOldIsScoped = 0x242c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bOnGroundLastTick = 0x2298; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bPrevDefuser = 0x156e; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bPrevHelmet = 0x156f; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bPreviouslyInBuyZone = 0x1581; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bRagdollDamageHeadshot = 0x1c10; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bResumeZoom = 0x23e9; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bRetakesHasDefuseKit = 0x1738; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bRetakesMVPLastRound = 0x1739; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bSkipOneHeadConstraintUpdate = 0x22c0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_bWaitForNoAttack = 0x2410; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_entitySpottedState = 0x23d0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_fSwitchedHandednessTime = 0x22c4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flDeathInfoTime = 0x2430; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flEmitSoundTime = 0x23f0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flFlinchStack = 0x2400; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flHealthShotBoostExpirationTime = 0x1548; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flHitHeading = 0x2408; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flLandingStartTime = 0x15cc; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flLandingTimeSeconds = 0x1554; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flLastFiredWeaponTime = 0x154c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flNextSprayDecalTime = 0x15d8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flOldFallVelocity = 0x1558; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flSlopeDropHeight = 0x23a8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flSlopeDropOffset = 0x2398; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flTimeOfLastInjury = 0x15d4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flVelocityModifier = 0x2404; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flViewmodelFOV = 0x22d4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flViewmodelOffsetX = 0x22c8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flViewmodelOffsetY = 0x22cc; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_flViewmodelOffsetZ = 0x22d0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_grenadeParameterStashTime = 0x2440; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_iBlockingUseActionInProgress = 0x23ec; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_iRetakesMVPBoostItem = 0x173c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_iRetakesOffering = 0x1730; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_iRetakesOfferingCard = 0x1734; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_iShotsFired = 0x23fc; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_ignoreLadderJumpTime = 0x2414; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_lastLandTime = 0x2294; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nEconGlovesChanged = 0x1bb0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nHighestAppliedDamageTagTick = 0x250c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nHitBodyPart = 0x240c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nLastKillerIndex = 0x2428; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nPrevArmorVal = 0x1570; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nPrevGrenadeAmmoCount = 0x1574; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nPrevHighestReceivedDamageTagTick = 0x2508; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nRagdollDamageBone = 0x1bb4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_nWhichBombZone = 0x23f8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_pActionTrackingServices = 0x1538; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_pBulletServices = 0x1518; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_pBuyServices = 0x1528; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_pDamageReactServices = 0x1540; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_pGlowServices = 0x1530; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_pHostageServices = 0x1520; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_qDeathEyeAngles = 0x22b4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_szLastPlaceName = 0x155c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_szRagdollDamageWeaponName = 0x1bd0; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_thirdPersonHeading = 0x2380; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_unCurrentEquipmentValue = 0x2420; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_unFreezetimeEndEquipmentValue = 0x2424; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_unPreviousWeaponHash = 0x1578; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_unRoundStartEquipmentValue = 0x2422; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_unWeaponHash = 0x157c; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vHeadConstraintOffset = 0x23b8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vRagdollDamageForce = 0x1bb8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vRagdollDamagePosition = 0x1bc4; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vRagdollServerOrigin = 0x1c14; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecBulletHitModels = 0x2360; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecDeathInfoOrigin = 0x2434; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecPlayerPatchEconIndices = 0x22d8; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecStashedGrenadeThrowPosition = 0x2454; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecStashedVelocity = 0x2460; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecThrowPositionHistory = 0x2484; // C_CSPlayerPawn
			constexpr std::ptrdiff_t m_vecVelocityHistory = 0x249c; // C_CSPlayerPawn
		}
		namespace C_CSPlayerPawnBase {
			constexpr std::ptrdiff_t m_angEyeAngles = 0x1438; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bCachedPlaneIsValid = 0x139d; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bClipHitStaticWorld = 0x139c; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bDeferStartMusicOnWarmup = 0x14a4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bFlashBuildUp = 0x1404; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bFlashDspHasBeenCleared = 0x1405; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bFlashScreenshotHasBeenGrabbed = 0x1406; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bGuardianShouldSprayCustomXMark = 0x1500; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bGunGameImmunity = 0x13bc; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bHasMovedSinceSpawn = 0x13bd; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bIsRescuing = 0x13b0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bScreenTearFrameCaptured = 0x13f4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bShouldAutobuyDMWeapons = 0x1454; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_bShouldAutobuyNow = 0x1455; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_cycleLatch = 0x14a8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_delayTargetIDTimer = 0x1460; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_fImmuneToGunGameDamageTime = 0x13b4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_fImmuneToGunGameDamageTimeLast = 0x13b8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_fMolotovDamageTime = 0x13c4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_fMolotovUseTime = 0x13c0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_fNextThinkPushAway = 0x1450; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_fRenderingClipPlane = 0x1370; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flClientDeathTime = 0x13f0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flCurrentMusicStartTime = 0x149c; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flDeathCCWeight = 0x1428; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flFlashBangTime = 0x13f8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flFlashDuration = 0x140c; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flFlashMaxAlpha = 0x1408; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flFlashOverlayAlpha = 0x1400; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flFlashScreenshotAlpha = 0x13fc; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flHealthFadeAlpha = 0x1418; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flHealthFadeValue = 0x1414; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flLastSmokeAge = 0x14b4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flLastSmokeOverlayAlpha = 0x14b0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flLastSpawnTimeIndex = 0x13cc; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flMusicRoundStartTime = 0x14a0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flNextMagDropTime = 0x14d0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flPrevMatchEndTime = 0x1430; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flPrevRoundEndTime = 0x142c; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_flProgressBarStartTime = 0x13d4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_hOriginalController = 0x1508; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_holdTargetIDTimer = 0x1480; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iHealthBarRenderMaskIndex = 0x1410; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iIDEntIndex = 0x1458; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iOldIDEntIndex = 0x147c; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iPlayerState = 0x13ac; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iProgressBarDuration = 0x13d0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iTargetItemEntIdx = 0x1478; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_iThrowGrenadeCounter = 0x13c8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_nLastClipPlaneSetupFrame = 0x1380; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_nLastMagDropAttachmentIndex = 0x14d4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_nPlayerInfernoBodyFx = 0x14c8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_nPlayerInfernoFootFx = 0x14cc; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_nPlayerSmokedFx = 0x14c4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_pClippingWeapon = 0x13a0; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_pPingServices = 0x1360; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_pViewModelServices = 0x1368; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_previousPlayerState = 0x13a8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_serverIntendedCycle = 0x14ac; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_vLastSmokeOverlayColor = 0x14b8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_vecIntroStartEyePosition = 0x13d8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_vecIntroStartPlayerForward = 0x13e4; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_vecLastAliveLocalVelocity = 0x14d8; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_vecLastClipCameraForward = 0x1390; // C_CSPlayerPawnBase
			constexpr std::ptrdiff_t m_vecLastClipCameraPos = 0x1384; // C_CSPlayerPawnBase
		}
		namespace C_CSPlayerResource {
			constexpr std::ptrdiff_t m_bEndMatchNextMapAllVoted = 0x5f8; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_bHostageAlive = 0x568; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_bombsiteCenterA = 0x5b0; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_bombsiteCenterB = 0x5bc; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_foundGoalPositions = 0x5f9; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_hostageRescueX = 0x5c8; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_hostageRescueY = 0x5d8; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_hostageRescueZ = 0x5e8; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_iHostageEntityIDs = 0x580; // C_CSPlayerResource
			constexpr std::ptrdiff_t m_isHostageFollowingSomeone = 0x574; // C_CSPlayerResource
		}
		namespace C_CSTeam {
			constexpr std::ptrdiff_t m_bSurrendered = 0x824; // C_CSTeam
			constexpr std::ptrdiff_t m_iClanID = 0x8b8; // C_CSTeam
			constexpr std::ptrdiff_t m_numMapVictories = 0x820; // C_CSTeam
			constexpr std::ptrdiff_t m_scoreFirstHalf = 0x828; // C_CSTeam
			constexpr std::ptrdiff_t m_scoreOvertime = 0x830; // C_CSTeam
			constexpr std::ptrdiff_t m_scoreSecondHalf = 0x82c; // C_CSTeam
			constexpr std::ptrdiff_t m_szClanTeamname = 0x834; // C_CSTeam
			constexpr std::ptrdiff_t m_szTeamFlagImage = 0x8bc; // C_CSTeam
			constexpr std::ptrdiff_t m_szTeamLogoImage = 0x8c4; // C_CSTeam
			constexpr std::ptrdiff_t m_szTeamMatchStat = 0x620; // C_CSTeam
		}
		namespace C_CSWeaponBase {
			constexpr std::ptrdiff_t m_ClientPreviousWeaponState = 0x1758; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_IronSightController = 0x19e0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_OnPlayerPickup = 0x1790; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bBurstMode = 0x17e8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bClearWeaponIdentifyingUGC = 0x18b0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bDroppedNearBuyZone = 0x1810; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bFireOnEmpty = 0x1788; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bInReload = 0x17f8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bIsHauledBack = 0x1800; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bOldFirstPersonSpectatedState = 0x18b2; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bReloadVisuallyComplete = 0x17f9; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bReloadsWithClips = 0x1780; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bSilencerOn = 0x1801; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bUIWeapon = 0x18b3; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bVisualsDataSet = 0x18b1; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bWasOwnedByCT = 0x18f4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_bWasOwnedByTerrorist = 0x18f5; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_donated = 0x18ec; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_ePlayerFireEvent = 0x16e8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_ePlayerFireEventAttackType = 0x16ec; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_fAccuracyPenalty = 0x17d0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_fAccuracySmoothedForZoom = 0x17d8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_fLastShotTime = 0x18f0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_fScopeZoomEndTime = 0x17dc; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flCrosshairDistance = 0x1760; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flDroppedAtTime = 0x17fc; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flFireSequenceStartTime = 0x16dc; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flGunAccuracyPositionDeprecated = 0x1774; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flLastAccuracyUpdateTime = 0x17d4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flLastBurstModeChangeTime = 0x17ec; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flLastLOSTraceFailureTime = 0x1aa0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flLastMagDropRequestTime = 0x1b00; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flNextAttackRenderTimeOffset = 0x1814; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flNextClientFireBulletTime = 0x1904; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flNextClientFireBulletTime_Repredict = 0x1908; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flPostponeFireReadyFrac = 0x17f4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flRecoilIndex = 0x17e4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flTimeSilencerSwitchComplete = 0x1804; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flTimeWeaponIdle = 0x1784; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flTurningInaccuracy = 0x17cc; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flTurningInaccuracyDelta = 0x17bc; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_flWatTickOffset = 0x1b04; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_gunHeat = 0x18f8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_hCurrentThirdPersonSequence = 0x1718; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_hPrevOwner = 0x18c4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iAlpha = 0x1768; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iAmmoLastCheck = 0x1764; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iCrosshairTextureID = 0x1770; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iIronSightMode = 0x1a90; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iMostRecentTeamNumber = 0x180c; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iNumEmptyAttacks = 0x1aa4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iOriginalTeamNumber = 0x1808; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iRecoilIndex = 0x17e0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iScopeTextureID = 0x176c; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_iState = 0x175c; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_lastSmokeTime = 0x1900; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nCustomEconReloadEventId = 0x18b4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nDropTick = 0x18c8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nFireSequenceStartTimeAck = 0x16e4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nFireSequenceStartTimeChange = 0x16e0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nLastEmptySoundCmdNum = 0x1778; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nPostponeFireReadyTicks = 0x17f0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nSilencerBoneIndex = 0x171c; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nViewModelIndex = 0x177c; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_nextPrevOwnerUseTime = 0x18c0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_seqFirePrimary = 0x16f4; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_seqFireSecondary = 0x16f8; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_seqIdle = 0x16f0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_smokeAttachments = 0x18fc; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_thirdPersonFireSequences = 0x1700; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_thirdPersonSequences = 0x1720; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_vecTurningInaccuracyEyeDirLast = 0x17c0; // C_CSWeaponBase
			constexpr std::ptrdiff_t m_weaponMode = 0x17b8; // C_CSWeaponBase
		}
		namespace C_CSWeaponBaseGun {
			constexpr std::ptrdiff_t m_bNeedsBoltAction = 0x1b3d; // C_CSWeaponBaseGun
			constexpr std::ptrdiff_t m_iBurstShotsRemaining = 0x1b24; // C_CSWeaponBaseGun
			constexpr std::ptrdiff_t m_iSilencerBodygroup = 0x1b28; // C_CSWeaponBaseGun
			constexpr std::ptrdiff_t m_inPrecache = 0x1b3c; // C_CSWeaponBaseGun
			constexpr std::ptrdiff_t m_silencedModelIndex = 0x1b38; // C_CSWeaponBaseGun
			constexpr std::ptrdiff_t m_zoomLevel = 0x1b20; // C_CSWeaponBaseGun
		}
		namespace C_Chicken {
			constexpr std::ptrdiff_t m_AttributeManager = 0x1240; // C_Chicken
			constexpr std::ptrdiff_t m_bAttributesInitialized = 0x16e8; // C_Chicken
			constexpr std::ptrdiff_t m_bIsPreviewModel = 0x16f0; // C_Chicken
			constexpr std::ptrdiff_t m_hHolidayHatAddon = 0x1230; // C_Chicken
			constexpr std::ptrdiff_t m_hWaterWakeParticles = 0x16ec; // C_Chicken
			constexpr std::ptrdiff_t m_jumpedThisFrame = 0x1234; // C_Chicken
			constexpr std::ptrdiff_t m_leader = 0x1238; // C_Chicken
		}
		namespace C_ClientRagdoll {
			constexpr std::ptrdiff_t m_bFadeOut = 0xf88; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_bFadingOut = 0xfa6; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_bImportant = 0xf89; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_bReleaseRagdoll = 0xfa4; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_flEffectTime = 0xf8c; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_flScaleEnd = 0xfa8; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_flScaleTimeEnd = 0xff8; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_flScaleTimeStart = 0xfd0; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_gibDespawnTime = 0xf90; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_iCurrentFriction = 0xf94; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_iEyeAttachment = 0xfa5; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_iFrictionAnimState = 0xfa0; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_iMaxFriction = 0xf9c; // C_ClientRagdoll
			constexpr std::ptrdiff_t m_iMinFriction = 0xf98; // C_ClientRagdoll
		}
		namespace C_ColorCorrection {
			constexpr std::ptrdiff_t m_MaxFalloff = 0x578; // C_ColorCorrection
			constexpr std::ptrdiff_t m_MinFalloff = 0x574; // C_ColorCorrection
			constexpr std::ptrdiff_t m_bClientSide = 0x78e; // C_ColorCorrection
			constexpr std::ptrdiff_t m_bEnabled = 0x78c; // C_ColorCorrection
			constexpr std::ptrdiff_t m_bEnabledOnClient = 0x790; // C_ColorCorrection
			constexpr std::ptrdiff_t m_bExclusive = 0x78f; // C_ColorCorrection
			constexpr std::ptrdiff_t m_bFadingIn = 0x798; // C_ColorCorrection
			constexpr std::ptrdiff_t m_bMaster = 0x78d; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flCurWeight = 0x588; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flCurWeightOnClient = 0x794; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flFadeDuration = 0x7a4; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flFadeInDuration = 0x57c; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flFadeOutDuration = 0x580; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flFadeStartTime = 0x7a0; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flFadeStartWeight = 0x79c; // C_ColorCorrection
			constexpr std::ptrdiff_t m_flMaxWeight = 0x584; // C_ColorCorrection
			constexpr std::ptrdiff_t m_netlookupFilename = 0x58c; // C_ColorCorrection
			constexpr std::ptrdiff_t m_vecOrigin = 0x568; // C_ColorCorrection
		}
		namespace C_ColorCorrectionVolume {
			constexpr std::ptrdiff_t m_FadeDuration = 0xd48; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_LastEnterTime = 0xd34; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_LastEnterWeight = 0xd30; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_LastExitTime = 0xd3c; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_LastExitWeight = 0xd38; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_MaxWeight = 0xd44; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_Weight = 0xd4c; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_bEnabled = 0xd40; // C_ColorCorrectionVolume
			constexpr std::ptrdiff_t m_lookupFilename = 0xd50; // C_ColorCorrectionVolume
		}
		namespace C_CsmFovOverride {
			constexpr std::ptrdiff_t m_cameraName = 0x568; // C_CsmFovOverride
			constexpr std::ptrdiff_t m_flCsmFovOverrideValue = 0x570; // C_CsmFovOverride
		}
		namespace C_DecoyProjectile {
			constexpr std::ptrdiff_t m_flTimeParticleEffectSpawn = 0x1230; // C_DecoyProjectile
			constexpr std::ptrdiff_t m_nClientLastKnownDecoyShotTick = 0x120c; // C_DecoyProjectile
			constexpr std::ptrdiff_t m_nDecoyShotTick = 0x1208; // C_DecoyProjectile
		}
		namespace C_DynamicLight {
			constexpr std::ptrdiff_t m_Exponent = 0xd30; // C_DynamicLight
			constexpr std::ptrdiff_t m_Flags = 0xd28; // C_DynamicLight
			constexpr std::ptrdiff_t m_InnerAngle = 0xd34; // C_DynamicLight
			constexpr std::ptrdiff_t m_LightStyle = 0xd29; // C_DynamicLight
			constexpr std::ptrdiff_t m_OuterAngle = 0xd38; // C_DynamicLight
			constexpr std::ptrdiff_t m_Radius = 0xd2c; // C_DynamicLight
			constexpr std::ptrdiff_t m_SpotRadius = 0xd3c; // C_DynamicLight
		}
		namespace C_DynamicProp {
			constexpr std::ptrdiff_t m_OnAnimReachedEnd = 0x11b8; // C_DynamicProp
			constexpr std::ptrdiff_t m_OnAnimReachedStart = 0x1190; // C_DynamicProp
			constexpr std::ptrdiff_t m_bCreateNonSolid = 0x11f0; // C_DynamicProp
			constexpr std::ptrdiff_t m_bFiredStartEndOutput = 0x11ee; // C_DynamicProp
			constexpr std::ptrdiff_t m_bForceNpcExclude = 0x11ef; // C_DynamicProp
			constexpr std::ptrdiff_t m_bIsOverrideProp = 0x11f1; // C_DynamicProp
			constexpr std::ptrdiff_t m_bRandomizeCycle = 0x11ec; // C_DynamicProp
			constexpr std::ptrdiff_t m_bStartDisabled = 0x11ed; // C_DynamicProp
			constexpr std::ptrdiff_t m_bUseAnimGraph = 0x1111; // C_DynamicProp
			constexpr std::ptrdiff_t m_bUseHitboxesForRenderBox = 0x1110; // C_DynamicProp
			constexpr std::ptrdiff_t m_glowColor = 0x1200; // C_DynamicProp
			constexpr std::ptrdiff_t m_iCachedFrameCount = 0x1208; // C_DynamicProp
			constexpr std::ptrdiff_t m_iInitialGlowState = 0x11f4; // C_DynamicProp
			constexpr std::ptrdiff_t m_iszIdleAnim = 0x11e0; // C_DynamicProp
			constexpr std::ptrdiff_t m_nGlowRange = 0x11f8; // C_DynamicProp
			constexpr std::ptrdiff_t m_nGlowRangeMin = 0x11fc; // C_DynamicProp
			constexpr std::ptrdiff_t m_nGlowTeam = 0x1204; // C_DynamicProp
			constexpr std::ptrdiff_t m_nIdleAnimLoopMode = 0x11e8; // C_DynamicProp
			constexpr std::ptrdiff_t m_pOutputAnimBegun = 0x1118; // C_DynamicProp
			constexpr std::ptrdiff_t m_pOutputAnimLoopCycleOver = 0x1168; // C_DynamicProp
			constexpr std::ptrdiff_t m_pOutputAnimOver = 0x1140; // C_DynamicProp
			constexpr std::ptrdiff_t m_vecCachedRenderMaxs = 0x1218; // C_DynamicProp
			constexpr std::ptrdiff_t m_vecCachedRenderMins = 0x120c; // C_DynamicProp
		}
		namespace C_EconEntity {
			constexpr std::ptrdiff_t m_AttributeManager = 0x1148; // C_EconEntity
			constexpr std::ptrdiff_t m_OriginalOwnerXuidHigh = 0x15f4; // C_EconEntity
			constexpr std::ptrdiff_t m_OriginalOwnerXuidLow = 0x15f0; // C_EconEntity
			constexpr std::ptrdiff_t m_bAttachmentDirty = 0x1630; // C_EconEntity
			constexpr std::ptrdiff_t m_bAttributesInitialized = 0x1140; // C_EconEntity
			constexpr std::ptrdiff_t m_bClientside = 0x1608; // C_EconEntity
			constexpr std::ptrdiff_t m_bParticleSystemsCreated = 0x1609; // C_EconEntity
			constexpr std::ptrdiff_t m_flFallbackWear = 0x1600; // C_EconEntity
			constexpr std::ptrdiff_t m_flFlexDelayTime = 0x1130; // C_EconEntity
			constexpr std::ptrdiff_t m_flFlexDelayedWeight = 0x1138; // C_EconEntity
			constexpr std::ptrdiff_t m_hOldProvidee = 0x1648; // C_EconEntity
			constexpr std::ptrdiff_t m_hViewmodelAttachment = 0x1628; // C_EconEntity
			constexpr std::ptrdiff_t m_iNumOwnerValidationRetries = 0x1638; // C_EconEntity
			constexpr std::ptrdiff_t m_iOldTeam = 0x162c; // C_EconEntity
			constexpr std::ptrdiff_t m_nFallbackPaintKit = 0x15f8; // C_EconEntity
			constexpr std::ptrdiff_t m_nFallbackSeed = 0x15fc; // C_EconEntity
			constexpr std::ptrdiff_t m_nFallbackStatTrak = 0x1604; // C_EconEntity
			constexpr std::ptrdiff_t m_nUnloadedModelIndex = 0x1634; // C_EconEntity
			constexpr std::ptrdiff_t m_vecAttachedModels = 0x1650; // C_EconEntity
			constexpr std::ptrdiff_t m_vecAttachedParticles = 0x1610; // C_EconEntity
		}
		namespace C_EconEntity__AttachedModelData_t {
			constexpr std::ptrdiff_t m_iModelDisplayFlags = 0x0; // C_EconEntity__AttachedModelData_t
		}
		namespace C_EconItemView {
			constexpr std::ptrdiff_t m_AttributeList = 0x210; // C_EconItemView
			constexpr std::ptrdiff_t m_NetworkedDynamicAttributes = 0x270; // C_EconItemView
			constexpr std::ptrdiff_t m_bDisallowSOC = 0x1e9; // C_EconItemView
			constexpr std::ptrdiff_t m_bInitialized = 0x1e8; // C_EconItemView
			constexpr std::ptrdiff_t m_bInitializedTags = 0x440; // C_EconItemView
			constexpr std::ptrdiff_t m_bInventoryImageRgbaRequested = 0x60; // C_EconItemView
			constexpr std::ptrdiff_t m_bInventoryImageTriedCache = 0x61; // C_EconItemView
			constexpr std::ptrdiff_t m_bIsStoreItem = 0x1ea; // C_EconItemView
			constexpr std::ptrdiff_t m_bIsTradeItem = 0x1eb; // C_EconItemView
			constexpr std::ptrdiff_t m_bRestoreCustomMaterialAfterPrecache = 0x1b8; // C_EconItemView
			constexpr std::ptrdiff_t m_iAccountID = 0x1d8; // C_EconItemView
			constexpr std::ptrdiff_t m_iEntityLevel = 0x1c0; // C_EconItemView
			constexpr std::ptrdiff_t m_iEntityQuality = 0x1bc; // C_EconItemView
			constexpr std::ptrdiff_t m_iEntityQuantity = 0x1ec; // C_EconItemView
			constexpr std::ptrdiff_t m_iInventoryPosition = 0x1dc; // C_EconItemView
			constexpr std::ptrdiff_t m_iItemDefinitionIndex = 0x1ba; // C_EconItemView
			constexpr std::ptrdiff_t m_iItemID = 0x1c8; // C_EconItemView
			constexpr std::ptrdiff_t m_iItemIDHigh = 0x1d0; // C_EconItemView
			constexpr std::ptrdiff_t m_iItemIDLow = 0x1d4; // C_EconItemView
			constexpr std::ptrdiff_t m_iOriginOverride = 0x1f8; // C_EconItemView
			constexpr std::ptrdiff_t m_iQualityOverride = 0x1f4; // C_EconItemView
			constexpr std::ptrdiff_t m_iRarityOverride = 0x1f0; // C_EconItemView
			constexpr std::ptrdiff_t m_nInventoryImageRgbaHeight = 0x84; // C_EconItemView
			constexpr std::ptrdiff_t m_nInventoryImageRgbaWidth = 0x80; // C_EconItemView
			constexpr std::ptrdiff_t m_szCurrentLoadCachedFileName = 0x88; // C_EconItemView
			constexpr std::ptrdiff_t m_szCustomName = 0x2d0; // C_EconItemView
			constexpr std::ptrdiff_t m_szCustomNameOverride = 0x371; // C_EconItemView
			constexpr std::ptrdiff_t m_unClientFlags = 0x1fc; // C_EconItemView
			constexpr std::ptrdiff_t m_unOverrideStyle = 0x1fd; // C_EconItemView
		}
		namespace C_EconWearable {
			constexpr std::ptrdiff_t m_bAlwaysAllow = 0x166c; // C_EconWearable
			constexpr std::ptrdiff_t m_nForceSkin = 0x1668; // C_EconWearable
		}
		namespace C_EntityDissolve {
			constexpr std::ptrdiff_t m_bCoreExplode = 0xd64; // C_EntityDissolve
			constexpr std::ptrdiff_t m_bLinkedToServerEnt = 0xd65; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flFadeInLength = 0xd38; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flFadeInStart = 0xd34; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flFadeOutLength = 0xd48; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flFadeOutModelLength = 0xd40; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flFadeOutModelStart = 0xd3c; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flFadeOutStart = 0xd44; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flNextSparkTime = 0xd4c; // C_EntityDissolve
			constexpr std::ptrdiff_t m_flStartTime = 0xd30; // C_EntityDissolve
			constexpr std::ptrdiff_t m_nDissolveType = 0xd50; // C_EntityDissolve
			constexpr std::ptrdiff_t m_nMagnitude = 0xd60; // C_EntityDissolve
			constexpr std::ptrdiff_t m_vDissolverOrigin = 0xd54; // C_EntityDissolve
		}
		namespace C_EntityFlame {
			constexpr std::ptrdiff_t m_bCheapEffect = 0x594; // C_EntityFlame
			constexpr std::ptrdiff_t m_hEntAttached = 0x568; // C_EntityFlame
			constexpr std::ptrdiff_t m_hOldAttached = 0x590; // C_EntityFlame
		}
		namespace C_EnvCombinedLightProbeVolume {
			constexpr std::ptrdiff_t m_Entity_Color = 0x15c8; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_bCustomCubemapTexture = 0x15d8; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_bEnabled = 0x1669; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_bMoveable = 0x1618; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_bStartDisabled = 0x1628; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_flBrightness = 0x15cc; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_flEdgeFadeDist = 0x162c; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hCubemapTexture = 0x15d0; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeDirectLightIndicesTexture = 0x15e8; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeDirectLightScalarsTexture = 0x15f0; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeDirectLightShadowsTexture = 0x15f8; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeTexture = 0x15e0; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nEnvCubeMapArrayIndex = 0x1620; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nHandshake = 0x161c; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeAtlasX = 0x1648; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeAtlasY = 0x164c; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeAtlasZ = 0x1650; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeSizeX = 0x163c; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeSizeY = 0x1640; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeSizeZ = 0x1644; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nPriority = 0x1624; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_vBoxMaxs = 0x160c; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_vBoxMins = 0x1600; // C_EnvCombinedLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_vEdgeFadeDists = 0x1630; // C_EnvCombinedLightProbeVolume
		}
		namespace C_EnvCubemap {
			constexpr std::ptrdiff_t m_Entity_bCopyDiffuseFromDefaultCubemap = 0x638; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bCustomCubemapTexture = 0x5f0; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bDefaultEnvMap = 0x635; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bDefaultSpecEnvMap = 0x636; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bEnabled = 0x648; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bIndoorCubeMap = 0x637; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bMoveable = 0x610; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_bStartDisabled = 0x634; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_flDiffuseScale = 0x630; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_flEdgeFadeDist = 0x620; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_flInfluenceRadius = 0x5f4; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_hCubemapTexture = 0x5e8; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_nEnvCubeMapArrayIndex = 0x618; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_nHandshake = 0x614; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_nPriority = 0x61c; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_vBoxProjectMaxs = 0x604; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_vBoxProjectMins = 0x5f8; // C_EnvCubemap
			constexpr std::ptrdiff_t m_Entity_vEdgeFadeDists = 0x624; // C_EnvCubemap
		}
		namespace C_EnvCubemapFog {
			constexpr std::ptrdiff_t m_bActive = 0x58c; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_bFirstTime = 0x5b1; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_bHasHeightFogEnd = 0x5b0; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_bHeightFogEnabled = 0x574; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_bStartDisabled = 0x58d; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flEndDistance = 0x568; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flFogFalloffExponent = 0x570; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flFogHeightEnd = 0x57c; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flFogHeightExponent = 0x584; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flFogHeightStart = 0x580; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flFogHeightWidth = 0x578; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flFogMaxOpacity = 0x590; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flLODBias = 0x588; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_flStartDistance = 0x56c; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_hFogCubemapTexture = 0x5a8; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_hSkyMaterial = 0x598; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_iszSkyEntity = 0x5a0; // C_EnvCubemapFog
			constexpr std::ptrdiff_t m_nCubemapSourceType = 0x594; // C_EnvCubemapFog
		}
		namespace C_EnvDecal {
			constexpr std::ptrdiff_t m_bProjectOnCharacters = 0xd41; // C_EnvDecal
			constexpr std::ptrdiff_t m_bProjectOnWater = 0xd42; // C_EnvDecal
			constexpr std::ptrdiff_t m_bProjectOnWorld = 0xd40; // C_EnvDecal
			constexpr std::ptrdiff_t m_flDepth = 0xd38; // C_EnvDecal
			constexpr std::ptrdiff_t m_flDepthSortBias = 0xd44; // C_EnvDecal
			constexpr std::ptrdiff_t m_flHeight = 0xd34; // C_EnvDecal
			constexpr std::ptrdiff_t m_flWidth = 0xd30; // C_EnvDecal
			constexpr std::ptrdiff_t m_hDecalMaterial = 0xd28; // C_EnvDecal
			constexpr std::ptrdiff_t m_nRenderOrder = 0xd3c; // C_EnvDecal
		}
		namespace C_EnvDetailController {
			constexpr std::ptrdiff_t m_flFadeEndDist = 0x56c; // C_EnvDetailController
			constexpr std::ptrdiff_t m_flFadeStartDist = 0x568; // C_EnvDetailController
		}
		namespace C_EnvLightProbeVolume {
			constexpr std::ptrdiff_t m_Entity_bEnabled = 0x15b1; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_bMoveable = 0x1580; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_bStartDisabled = 0x158c; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeDirectLightIndicesTexture = 0x1550; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeDirectLightScalarsTexture = 0x1558; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeDirectLightShadowsTexture = 0x1560; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_hLightProbeTexture = 0x1548; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nHandshake = 0x1584; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeAtlasX = 0x159c; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeAtlasY = 0x15a0; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeAtlasZ = 0x15a4; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeSizeX = 0x1590; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeSizeY = 0x1594; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nLightProbeSizeZ = 0x1598; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_nPriority = 0x1588; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_vBoxMaxs = 0x1574; // C_EnvLightProbeVolume
			constexpr std::ptrdiff_t m_Entity_vBoxMins = 0x1568; // C_EnvLightProbeVolume
		}
		namespace C_EnvParticleGlow {
			constexpr std::ptrdiff_t m_ColorTint = 0x12e4; // C_EnvParticleGlow
			constexpr std::ptrdiff_t m_flAlphaScale = 0x12d8; // C_EnvParticleGlow
			constexpr std::ptrdiff_t m_flRadiusScale = 0x12dc; // C_EnvParticleGlow
			constexpr std::ptrdiff_t m_flSelfIllumScale = 0x12e0; // C_EnvParticleGlow
			constexpr std::ptrdiff_t m_hTextureOverride = 0x12e8; // C_EnvParticleGlow
		}
		namespace C_EnvScreenOverlay {
			constexpr std::ptrdiff_t m_bIsActive = 0x5e8; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_bWasActive = 0x5e9; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_flCurrentOverlayTime = 0x5f4; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_flOverlayTimes = 0x5b8; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_flStartTime = 0x5e0; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_iCachedDesiredOverlay = 0x5ec; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_iCurrentOverlay = 0x5f0; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_iDesiredOverlay = 0x5e4; // C_EnvScreenOverlay
			constexpr std::ptrdiff_t m_iszOverlayNames = 0x568; // C_EnvScreenOverlay
		}
		namespace C_EnvSky {
			constexpr std::ptrdiff_t m_bEnabled = 0xd5c; // C_EnvSky
			constexpr std::ptrdiff_t m_bStartDisabled = 0xd38; // C_EnvSky
			constexpr std::ptrdiff_t m_flBrightnessScale = 0xd44; // C_EnvSky
			constexpr std::ptrdiff_t m_flFogMaxEnd = 0xd58; // C_EnvSky
			constexpr std::ptrdiff_t m_flFogMaxStart = 0xd54; // C_EnvSky
			constexpr std::ptrdiff_t m_flFogMinEnd = 0xd50; // C_EnvSky
			constexpr std::ptrdiff_t m_flFogMinStart = 0xd4c; // C_EnvSky
			constexpr std::ptrdiff_t m_hSkyMaterial = 0xd28; // C_EnvSky
			constexpr std::ptrdiff_t m_hSkyMaterialLightingOnly = 0xd30; // C_EnvSky
			constexpr std::ptrdiff_t m_nFogType = 0xd48; // C_EnvSky
			constexpr std::ptrdiff_t m_vTintColor = 0xd39; // C_EnvSky
			constexpr std::ptrdiff_t m_vTintColorLightingOnly = 0xd3d; // C_EnvSky
		}
		namespace C_EnvVolumetricFogController {
			constexpr std::ptrdiff_t m_bActive = 0x5b0; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_bEnableIndirect = 0x5d9; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_bFirstTime = 0x600; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_bIndirectUseLPVs = 0x5da; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_bIsMaster = 0x5db; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_bStartDisabled = 0x5d8; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_fFirstVolumeSliceThickness = 0x588; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_fNoiseSpeed = 0x5ec; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_fNoiseStrength = 0x5f0; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flAnisotropy = 0x56c; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flDefaultAnisotropy = 0x5cc; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flDefaultDrawDistance = 0x5d4; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flDefaultScattering = 0x5d0; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flDrawDistance = 0x574; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flFadeInEnd = 0x57c; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flFadeInStart = 0x578; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flFadeSpeed = 0x570; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flIndirectStrength = 0x580; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flScattering = 0x568; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flStartAnisoTime = 0x5b4; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flStartAnisotropy = 0x5c0; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flStartDrawDistance = 0x5c8; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flStartDrawDistanceTime = 0x5bc; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flStartScatterTime = 0x5b8; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_flStartScattering = 0x5c4; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_hFogIndirectTexture = 0x5e0; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_nForceRefreshCount = 0x5e8; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_nIndirectTextureDimX = 0x58c; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_nIndirectTextureDimY = 0x590; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_nIndirectTextureDimZ = 0x594; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_nVolumeDepth = 0x584; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_vBoxMaxs = 0x5a4; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_vBoxMins = 0x598; // C_EnvVolumetricFogController
			constexpr std::ptrdiff_t m_vNoiseScale = 0x5f4; // C_EnvVolumetricFogController
		}
		namespace C_EnvVolumetricFogVolume {
			constexpr std::ptrdiff_t m_bActive = 0x568; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_bAllowLPVIndirect = 0x5ab; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_bOverrideIndirectLightStrength = 0x5a8; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_bOverrideNoiseStrength = 0x5aa; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_bOverrideSunLightStrength = 0x5a9; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_bStartDisabled = 0x584; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_fHeightFogEdgeWidth = 0x598; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_fIndirectLightStrength = 0x59c; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_fNoiseStrength = 0x5a4; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_fSunLightStrength = 0x5a0; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_flFalloffExponent = 0x590; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_flHeightFogDepth = 0x594; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_flStrength = 0x588; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_nFalloffShape = 0x58c; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_vBoxMaxs = 0x578; // C_EnvVolumetricFogVolume
			constexpr std::ptrdiff_t m_vBoxMins = 0x56c; // C_EnvVolumetricFogVolume
		}
		namespace C_EnvWind {
			constexpr std::ptrdiff_t m_EnvWindShared = 0x568; // C_EnvWind
		}
		namespace C_EnvWindClientside {
			constexpr std::ptrdiff_t m_EnvWindShared = 0x568; // C_EnvWindClientside
		}
		namespace C_EnvWindShared {
			constexpr std::ptrdiff_t m_CurrentSwayVector = 0x50; // C_EnvWindShared
			constexpr std::ptrdiff_t m_PrevSwayVector = 0x5c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_bGusting = 0x84; // C_EnvWindShared
			constexpr std::ptrdiff_t m_currentWindVector = 0x44; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flAveWindSpeed = 0x80; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flGustDuration = 0x24; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flInitialWindSpeed = 0x6c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flMaxGustDelay = 0x20; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flMinGustDelay = 0x1c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flSimTime = 0x78; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flStartTime = 0x8; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flSwayTime = 0x74; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flSwitchTime = 0x7c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flVariationTime = 0x70; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flWindAngleVariation = 0x88; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flWindSpeed = 0x40; // C_EnvWindShared
			constexpr std::ptrdiff_t m_flWindSpeedVariation = 0x8c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_hEntOwner = 0x90; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iGustDirChange = 0x28; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iInitialWindDir = 0x68; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iMaxGust = 0x1a; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iMaxWind = 0x12; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iMinGust = 0x18; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iMinWind = 0x10; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iWindDir = 0x3c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iWindSeed = 0xc; // C_EnvWindShared
			constexpr std::ptrdiff_t m_iszGustSound = 0x38; // C_EnvWindShared
			constexpr std::ptrdiff_t m_location = 0x2c; // C_EnvWindShared
			constexpr std::ptrdiff_t m_windRadius = 0x14; // C_EnvWindShared
		}
		namespace C_EnvWindShared__WindAveEvent_t {
			constexpr std::ptrdiff_t m_flAveWindSpeed = 0x4; // C_EnvWindShared__WindAveEvent_t
			constexpr std::ptrdiff_t m_flStartWindSpeed = 0x0; // C_EnvWindShared__WindAveEvent_t
		}
		namespace C_EnvWindShared__WindVariationEvent_t {
			constexpr std::ptrdiff_t m_flWindAngleVariation = 0x0; // C_EnvWindShared__WindVariationEvent_t
			constexpr std::ptrdiff_t m_flWindSpeedVariation = 0x4; // C_EnvWindShared__WindVariationEvent_t
		}
		namespace C_FireSmoke {
			constexpr std::ptrdiff_t m_bClipTested = 0x5ac; // C_FireSmoke
			constexpr std::ptrdiff_t m_bFadingOut = 0x5ad; // C_FireSmoke
			constexpr std::ptrdiff_t m_flChildFlameSpread = 0x594; // C_FireSmoke
			constexpr std::ptrdiff_t m_flClipPerc = 0x5a8; // C_FireSmoke
			constexpr std::ptrdiff_t m_flScaleEnd = 0x588; // C_FireSmoke
			constexpr std::ptrdiff_t m_flScaleRegister = 0x580; // C_FireSmoke
			constexpr std::ptrdiff_t m_flScaleStart = 0x584; // C_FireSmoke
			constexpr std::ptrdiff_t m_flScaleTimeEnd = 0x590; // C_FireSmoke
			constexpr std::ptrdiff_t m_flScaleTimeStart = 0x58c; // C_FireSmoke
			constexpr std::ptrdiff_t m_nFlameFromAboveModelIndex = 0x57c; // C_FireSmoke
			constexpr std::ptrdiff_t m_nFlameModelIndex = 0x578; // C_FireSmoke
			constexpr std::ptrdiff_t m_pFireOverlay = 0x5b8; // C_FireSmoke
			constexpr std::ptrdiff_t m_tParticleSpawn = 0x5b0; // C_FireSmoke
		}
		namespace C_FireSprite {
			constexpr std::ptrdiff_t m_bFadeFromAbove = 0xe44; // C_FireSprite
			constexpr std::ptrdiff_t m_vecMoveDir = 0xe38; // C_FireSprite
		}
		namespace C_Fish {
			constexpr std::ptrdiff_t m_actualAngles = 0xfec; // C_Fish
			constexpr std::ptrdiff_t m_actualPos = 0xfe0; // C_Fish
			constexpr std::ptrdiff_t m_angle = 0x1018; // C_Fish
			constexpr std::ptrdiff_t m_angles = 0xfa0; // C_Fish
			constexpr std::ptrdiff_t m_averageError = 0x1074; // C_Fish
			constexpr std::ptrdiff_t m_buoyancy = 0xfb8; // C_Fish
			constexpr std::ptrdiff_t m_deathAngle = 0xfb4; // C_Fish
			constexpr std::ptrdiff_t m_deathDepth = 0xfb0; // C_Fish
			constexpr std::ptrdiff_t m_errorHistory = 0x101c; // C_Fish
			constexpr std::ptrdiff_t m_errorHistoryCount = 0x1070; // C_Fish
			constexpr std::ptrdiff_t m_errorHistoryIndex = 0x106c; // C_Fish
			constexpr std::ptrdiff_t m_gotUpdate = 0x1008; // C_Fish
			constexpr std::ptrdiff_t m_localLifeState = 0xfac; // C_Fish
			constexpr std::ptrdiff_t m_poolOrigin = 0xff8; // C_Fish
			constexpr std::ptrdiff_t m_pos = 0xf88; // C_Fish
			constexpr std::ptrdiff_t m_vel = 0xf94; // C_Fish
			constexpr std::ptrdiff_t m_waterLevel = 0x1004; // C_Fish
			constexpr std::ptrdiff_t m_wigglePhase = 0xfd8; // C_Fish
			constexpr std::ptrdiff_t m_wiggleRate = 0xfdc; // C_Fish
			constexpr std::ptrdiff_t m_wiggleTimer = 0xfc0; // C_Fish
			constexpr std::ptrdiff_t m_x = 0x100c; // C_Fish
			constexpr std::ptrdiff_t m_y = 0x1010; // C_Fish
			constexpr std::ptrdiff_t m_z = 0x1014; // C_Fish
		}
		namespace C_Fists {
			constexpr std::ptrdiff_t m_bPlayingUninterruptableAct = 0x1b20; // C_Fists
			constexpr std::ptrdiff_t m_nUninterruptableActivity = 0x1b24; // C_Fists
		}
		namespace C_FogController {
			constexpr std::ptrdiff_t m_bUseAngles = 0x5d0; // C_FogController
			constexpr std::ptrdiff_t m_fog = 0x568; // C_FogController
			constexpr std::ptrdiff_t m_iChangedVariables = 0x5d4; // C_FogController
		}
		namespace C_FootstepControl {
			constexpr std::ptrdiff_t m_destination = 0xd38; // C_FootstepControl
			constexpr std::ptrdiff_t m_source = 0xd30; // C_FootstepControl
		}
		namespace C_FuncConveyor {
			constexpr std::ptrdiff_t m_flCurrentConveyorOffset = 0xd68; // C_FuncConveyor
			constexpr std::ptrdiff_t m_flCurrentConveyorSpeed = 0xd6c; // C_FuncConveyor
			constexpr std::ptrdiff_t m_flTargetSpeed = 0xd3c; // C_FuncConveyor
			constexpr std::ptrdiff_t m_flTransitionStartSpeed = 0xd48; // C_FuncConveyor
			constexpr std::ptrdiff_t m_hConveyorModels = 0xd50; // C_FuncConveyor
			constexpr std::ptrdiff_t m_nTransitionDurationTicks = 0xd44; // C_FuncConveyor
			constexpr std::ptrdiff_t m_nTransitionStartTick = 0xd40; // C_FuncConveyor
			constexpr std::ptrdiff_t m_vecMoveDirEntitySpace = 0xd30; // C_FuncConveyor
		}
		namespace C_FuncElectrifiedVolume {
			constexpr std::ptrdiff_t m_EffectName = 0xd30; // C_FuncElectrifiedVolume
			constexpr std::ptrdiff_t m_bState = 0xd38; // C_FuncElectrifiedVolume
			constexpr std::ptrdiff_t m_nAmbientEffect = 0xd28; // C_FuncElectrifiedVolume
		}
		namespace C_FuncLadder {
			constexpr std::ptrdiff_t m_Dismounts = 0xd38; // C_FuncLadder
			constexpr std::ptrdiff_t m_bDisabled = 0xd78; // C_FuncLadder
			constexpr std::ptrdiff_t m_bFakeLadder = 0xd79; // C_FuncLadder
			constexpr std::ptrdiff_t m_bHasSlack = 0xd7a; // C_FuncLadder
			constexpr std::ptrdiff_t m_flAutoRideSpeed = 0xd74; // C_FuncLadder
			constexpr std::ptrdiff_t m_vecLadderDir = 0xd28; // C_FuncLadder
			constexpr std::ptrdiff_t m_vecLocalTop = 0xd50; // C_FuncLadder
			constexpr std::ptrdiff_t m_vecPlayerMountPositionBottom = 0xd68; // C_FuncLadder
			constexpr std::ptrdiff_t m_vecPlayerMountPositionTop = 0xd5c; // C_FuncLadder
		}
		namespace C_FuncMonitor {
			constexpr std::ptrdiff_t m_bDraw3DSkybox = 0xd45; // C_FuncMonitor
			constexpr std::ptrdiff_t m_bEnabled = 0xd44; // C_FuncMonitor
			constexpr std::ptrdiff_t m_bRenderShadows = 0xd34; // C_FuncMonitor
			constexpr std::ptrdiff_t m_bUseUniqueColorTarget = 0xd35; // C_FuncMonitor
			constexpr std::ptrdiff_t m_brushModelName = 0xd38; // C_FuncMonitor
			constexpr std::ptrdiff_t m_hTargetCamera = 0xd40; // C_FuncMonitor
			constexpr std::ptrdiff_t m_nResolutionEnum = 0xd30; // C_FuncMonitor
			constexpr std::ptrdiff_t m_targetCamera = 0xd28; // C_FuncMonitor
		}
		namespace C_FuncTrackTrain {
			constexpr std::ptrdiff_t m_flLineLength = 0xd30; // C_FuncTrackTrain
			constexpr std::ptrdiff_t m_flRadius = 0xd2c; // C_FuncTrackTrain
			constexpr std::ptrdiff_t m_nLongAxis = 0xd28; // C_FuncTrackTrain
		}
		namespace C_GameRules {
			constexpr std::ptrdiff_t __m_pChainEntity = 0x8; // C_GameRules
			constexpr std::ptrdiff_t m_bGamePaused = 0x38; // C_GameRules
			constexpr std::ptrdiff_t m_nPauseStartTick = 0x34; // C_GameRules
			constexpr std::ptrdiff_t m_nTotalPausedTicks = 0x30; // C_GameRules
		}
		namespace C_GlobalLight {
			constexpr std::ptrdiff_t m_WindClothForceHandle = 0xa30; // C_GlobalLight
		}
		namespace C_GradientFog {
			constexpr std::ptrdiff_t m_bGradientFogNeedsTextures = 0x5a2; // C_GradientFog
			constexpr std::ptrdiff_t m_bHeightFogEnabled = 0x578; // C_GradientFog
			constexpr std::ptrdiff_t m_bIsEnabled = 0x5a1; // C_GradientFog
			constexpr std::ptrdiff_t m_bStartDisabled = 0x5a0; // C_GradientFog
			constexpr std::ptrdiff_t m_flFadeTime = 0x59c; // C_GradientFog
			constexpr std::ptrdiff_t m_flFarZ = 0x584; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogEndDistance = 0x574; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogEndHeight = 0x580; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogFalloffExponent = 0x58c; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogMaxOpacity = 0x588; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogStartDistance = 0x570; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogStartHeight = 0x57c; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogStrength = 0x598; // C_GradientFog
			constexpr std::ptrdiff_t m_flFogVerticalExponent = 0x590; // C_GradientFog
			constexpr std::ptrdiff_t m_fogColor = 0x594; // C_GradientFog
			constexpr std::ptrdiff_t m_hGradientFogTexture = 0x568; // C_GradientFog
		}
		namespace C_HandleTest {
			constexpr std::ptrdiff_t m_Handle = 0x568; // C_HandleTest
			constexpr std::ptrdiff_t m_bSendHandle = 0x56c; // C_HandleTest
		}
		namespace C_Hostage {
			constexpr std::ptrdiff_t m_bHandsHaveBeenCut = 0x11f4; // C_Hostage
			constexpr std::ptrdiff_t m_blinkTimer = 0x1220; // C_Hostage
			constexpr std::ptrdiff_t m_chestAttachment = 0x1262; // C_Hostage
			constexpr std::ptrdiff_t m_entitySpottedState = 0x11a8; // C_Hostage
			constexpr std::ptrdiff_t m_eyeAttachment = 0x1261; // C_Hostage
			constexpr std::ptrdiff_t m_fLastGrabTime = 0x11fc; // C_Hostage
			constexpr std::ptrdiff_t m_fNewestAlphaThinkTime = 0x1270; // C_Hostage
			constexpr std::ptrdiff_t m_flDeadOrRescuedTime = 0x1218; // C_Hostage
			constexpr std::ptrdiff_t m_flDropStartTime = 0x1214; // C_Hostage
			constexpr std::ptrdiff_t m_flGrabSuccessTime = 0x1210; // C_Hostage
			constexpr std::ptrdiff_t m_flRescueStartTime = 0x120c; // C_Hostage
			constexpr std::ptrdiff_t m_hHostageGrabber = 0x11f8; // C_Hostage
			constexpr std::ptrdiff_t m_isInit = 0x1260; // C_Hostage
			constexpr std::ptrdiff_t m_isRescued = 0x11ec; // C_Hostage
			constexpr std::ptrdiff_t m_jumpedThisFrame = 0x11ed; // C_Hostage
			constexpr std::ptrdiff_t m_leader = 0x11c0; // C_Hostage
			constexpr std::ptrdiff_t m_lookAroundTimer = 0x1248; // C_Hostage
			constexpr std::ptrdiff_t m_lookAt = 0x1238; // C_Hostage
			constexpr std::ptrdiff_t m_nHostageState = 0x11f0; // C_Hostage
			constexpr std::ptrdiff_t m_pPredictionOwner = 0x1268; // C_Hostage
			constexpr std::ptrdiff_t m_reuseTimer = 0x11c8; // C_Hostage
			constexpr std::ptrdiff_t m_vecGrabbedPos = 0x1200; // C_Hostage
			constexpr std::ptrdiff_t m_vel = 0x11e0; // C_Hostage
		}
		namespace C_Inferno {
			constexpr std::ptrdiff_t m_BurnNormal = 0x13d8; // C_Inferno
			constexpr std::ptrdiff_t m_bFireIsBurning = 0x1398; // C_Inferno
			constexpr std::ptrdiff_t m_bInPostEffectTime = 0x16e4; // C_Inferno
			constexpr std::ptrdiff_t m_blosCheck = 0x82f4; // C_Inferno
			constexpr std::ptrdiff_t m_drawableCount = 0x82f0; // C_Inferno
			constexpr std::ptrdiff_t m_fireCount = 0x16d8; // C_Inferno
			constexpr std::ptrdiff_t m_fireParentPositions = 0x1098; // C_Inferno
			constexpr std::ptrdiff_t m_firePositions = 0xd98; // C_Inferno
			constexpr std::ptrdiff_t m_flLastGrassBurnThink = 0x831c; // C_Inferno
			constexpr std::ptrdiff_t m_hInfernoClimbingOutlinePointsSnapshot = 0xd88; // C_Inferno
			constexpr std::ptrdiff_t m_hInfernoDecalsSnapshot = 0xd90; // C_Inferno
			constexpr std::ptrdiff_t m_hInfernoFillerPointsSnapshot = 0xd78; // C_Inferno
			constexpr std::ptrdiff_t m_hInfernoOutlinePointsSnapshot = 0xd80; // C_Inferno
			constexpr std::ptrdiff_t m_hInfernoPointsSnapshot = 0xd70; // C_Inferno
			constexpr std::ptrdiff_t m_lastFireCount = 0x16e8; // C_Inferno
			constexpr std::ptrdiff_t m_maxBounds = 0x8310; // C_Inferno
			constexpr std::ptrdiff_t m_maxFireHalfWidth = 0x82fc; // C_Inferno
			constexpr std::ptrdiff_t m_maxFireHeight = 0x8300; // C_Inferno
			constexpr std::ptrdiff_t m_minBounds = 0x8304; // C_Inferno
			constexpr std::ptrdiff_t m_nFireEffectTickBegin = 0x16ec; // C_Inferno
			constexpr std::ptrdiff_t m_nFireLifetime = 0x16e0; // C_Inferno
			constexpr std::ptrdiff_t m_nInfernoType = 0x16dc; // C_Inferno
			constexpr std::ptrdiff_t m_nfxFireDamageEffect = 0xd68; // C_Inferno
			constexpr std::ptrdiff_t m_nlosperiod = 0x82f8; // C_Inferno
		}
		namespace C_InfoVisibilityBox {
			constexpr std::ptrdiff_t m_bEnabled = 0x57c; // C_InfoVisibilityBox
			constexpr std::ptrdiff_t m_nMode = 0x56c; // C_InfoVisibilityBox
			constexpr std::ptrdiff_t m_vBoxSize = 0x570; // C_InfoVisibilityBox
		}
		namespace C_Item {
			constexpr std::ptrdiff_t m_pReticleHintTextName = 0x1668; // C_Item
		}
		namespace C_ItemDogtags {
			constexpr std::ptrdiff_t m_KillingPlayer = 0x176c; // C_ItemDogtags
			constexpr std::ptrdiff_t m_OwningPlayer = 0x1768; // C_ItemDogtags
		}
		namespace C_KeychainModule {
			constexpr std::ptrdiff_t m_nKeychainDefID = 0xf90; // C_KeychainModule
			constexpr std::ptrdiff_t m_nKeychainSeed = 0xf94; // C_KeychainModule
		}
		namespace C_Knife {
			constexpr std::ptrdiff_t m_bFirstAttack = 0x1b20; // C_Knife
		}
		namespace C_LightEntity {
			constexpr std::ptrdiff_t m_CLightComponent = 0xd28; // C_LightEntity
		}
		namespace C_LightGlow {
			constexpr std::ptrdiff_t m_GlowOverlay = 0xd48; // C_LightGlow
			constexpr std::ptrdiff_t m_flGlowProxySize = 0xd3c; // C_LightGlow
			constexpr std::ptrdiff_t m_flHDRColorScale = 0xd40; // C_LightGlow
			constexpr std::ptrdiff_t m_nHorizontalSize = 0xd28; // C_LightGlow
			constexpr std::ptrdiff_t m_nMaxDist = 0xd34; // C_LightGlow
			constexpr std::ptrdiff_t m_nMinDist = 0xd30; // C_LightGlow
			constexpr std::ptrdiff_t m_nOuterMaxDist = 0xd38; // C_LightGlow
			constexpr std::ptrdiff_t m_nVerticalSize = 0xd2c; // C_LightGlow
		}
		namespace C_LocalTempEntity {
			constexpr std::ptrdiff_t bounceFactor = 0xfa0; // C_LocalTempEntity
			constexpr std::ptrdiff_t die = 0xf8c; // C_LocalTempEntity
			constexpr std::ptrdiff_t fadeSpeed = 0xf9c; // C_LocalTempEntity
			constexpr std::ptrdiff_t flags = 0xf88; // C_LocalTempEntity
			constexpr std::ptrdiff_t hitSound = 0xfa4; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_bParticleCollision = 0xff8; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_flFrame = 0xfe0; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_flFrameMax = 0xf90; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_flFrameRate = 0xfdc; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_flSpriteScale = 0xfd4; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_iLastCollisionFrame = 0xffc; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_nFlickerFrame = 0xfd8; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_pszImpactEffect = 0xfe8; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_pszParticleEffect = 0xff0; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_vLastCollisionOrigin = 0x1000; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_vecNormal = 0xfc8; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_vecPrevAbsOrigin = 0x1018; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_vecTempEntAcceleration = 0x1024; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_vecTempEntAngVelocity = 0xfb8; // C_LocalTempEntity
			constexpr std::ptrdiff_t m_vecTempEntVelocity = 0x100c; // C_LocalTempEntity
			constexpr std::ptrdiff_t priority = 0xfa8; // C_LocalTempEntity
			constexpr std::ptrdiff_t tempent_renderamt = 0xfc4; // C_LocalTempEntity
			constexpr std::ptrdiff_t tentOffset = 0xfac; // C_LocalTempEntity
			constexpr std::ptrdiff_t x = 0xf94; // C_LocalTempEntity
			constexpr std::ptrdiff_t y = 0xf98; // C_LocalTempEntity
		}
		namespace C_MapVetoPickController {
			constexpr std::ptrdiff_t m_bDisabledHud = 0xeac; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nAccountIDs = 0x69c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nCurrentPhase = 0xe9c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nDraftType = 0x578; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nMapId0 = 0x79c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nMapId1 = 0x89c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nMapId2 = 0x99c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nMapId3 = 0xa9c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nMapId4 = 0xb9c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nMapId5 = 0xc9c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nPhaseDurationTicks = 0xea4; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nPhaseStartTick = 0xea0; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nPostDataUpdateTick = 0xea8; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nStartingSide0 = 0xd9c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nTeamWinningCoinToss = 0x57c; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nTeamWithFirstChoice = 0x580; // C_MapVetoPickController
			constexpr std::ptrdiff_t m_nVoteMapIdsList = 0x680; // C_MapVetoPickController
		}
		namespace C_MolotovProjectile {
			constexpr std::ptrdiff_t m_bIsIncGrenade = 0x1208; // C_MolotovProjectile
		}
		namespace C_Multimeter {
			constexpr std::ptrdiff_t m_hTargetC4 = 0xf90; // C_Multimeter
		}
		namespace C_NametagModule {
			constexpr std::ptrdiff_t m_strNametagString = 0xf90; // C_NametagModule
		}
		namespace C_OmniLight {
			constexpr std::ptrdiff_t m_bShowLight = 0x1078; // C_OmniLight
			constexpr std::ptrdiff_t m_flInnerAngle = 0x1070; // C_OmniLight
			constexpr std::ptrdiff_t m_flOuterAngle = 0x1074; // C_OmniLight
		}
		namespace C_ParticleSystem {
			constexpr std::ptrdiff_t m_bActive = 0xf28; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bAnimateDuringGameplayPause = 0xf34; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bFrozen = 0xf29; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bNoFreeze = 0x107d; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bNoRamp = 0x107e; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bNoSave = 0x107c; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bOldActive = 0x12c0; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bOldFrozen = 0x12c1; // C_ParticleSystem
			constexpr std::ptrdiff_t m_bStartActive = 0x107f; // C_ParticleSystem
			constexpr std::ptrdiff_t m_clrTint = 0x129c; // C_ParticleSystem
			constexpr std::ptrdiff_t m_flFreezeTransitionDuration = 0xf2c; // C_ParticleSystem
			constexpr std::ptrdiff_t m_flPreSimTime = 0xf44; // C_ParticleSystem
			constexpr std::ptrdiff_t m_flStartTime = 0xf40; // C_ParticleSystem
			constexpr std::ptrdiff_t m_hControlPointEnts = 0xf7c; // C_ParticleSystem
			constexpr std::ptrdiff_t m_iEffectIndex = 0xf38; // C_ParticleSystem
			constexpr std::ptrdiff_t m_iServerControlPointAssignments = 0xf78; // C_ParticleSystem
			constexpr std::ptrdiff_t m_iszControlPointNames = 0x1088; // C_ParticleSystem
			constexpr std::ptrdiff_t m_iszEffectName = 0x1080; // C_ParticleSystem
			constexpr std::ptrdiff_t m_nDataCP = 0x1288; // C_ParticleSystem
			constexpr std::ptrdiff_t m_nStopType = 0xf30; // C_ParticleSystem
			constexpr std::ptrdiff_t m_nTintCP = 0x1298; // C_ParticleSystem
			constexpr std::ptrdiff_t m_szSnapshotFileName = 0xd28; // C_ParticleSystem
			constexpr std::ptrdiff_t m_vServerControlPoints = 0xf48; // C_ParticleSystem
			constexpr std::ptrdiff_t m_vecDataCPValue = 0x128c; // C_ParticleSystem
		}
		namespace C_PathParticleRope {
			constexpr std::ptrdiff_t m_ColorTint = 0x5a4; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_Color = 0x600; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_Name = 0x580; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_PinEnabled = 0x618; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_Position = 0x5b8; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_RadiusScale = 0x630; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_TangentIn = 0x5d0; // C_PathParticleRope
			constexpr std::ptrdiff_t m_PathNodes_TangentOut = 0x5e8; // C_PathParticleRope
			constexpr std::ptrdiff_t m_bStartActive = 0x570; // C_PathParticleRope
			constexpr std::ptrdiff_t m_flMaxSimulationTime = 0x574; // C_PathParticleRope
			constexpr std::ptrdiff_t m_flParticleSpacing = 0x598; // C_PathParticleRope
			constexpr std::ptrdiff_t m_flRadius = 0x5a0; // C_PathParticleRope
			constexpr std::ptrdiff_t m_flSlack = 0x59c; // C_PathParticleRope
			constexpr std::ptrdiff_t m_iEffectIndex = 0x5b0; // C_PathParticleRope
			constexpr std::ptrdiff_t m_iszEffectName = 0x578; // C_PathParticleRope
			constexpr std::ptrdiff_t m_nEffectState = 0x5a8; // C_PathParticleRope
		}
		namespace C_PhysMagnet {
			constexpr std::ptrdiff_t m_aAttachedObjects = 0xfa0; // C_PhysMagnet
			constexpr std::ptrdiff_t m_aAttachedObjectsFromServer = 0xf88; // C_PhysMagnet
		}
		namespace C_PhysPropClientside {
			constexpr std::ptrdiff_t m_fDeathTime = 0x1114; // C_PhysPropClientside
			constexpr std::ptrdiff_t m_flTouchDelta = 0x1110; // C_PhysPropClientside
			constexpr std::ptrdiff_t m_inertiaScale = 0x1118; // C_PhysPropClientside
			constexpr std::ptrdiff_t m_nDamageType = 0x1134; // C_PhysPropClientside
			constexpr std::ptrdiff_t m_vecDamageDirection = 0x1128; // C_PhysPropClientside
			constexpr std::ptrdiff_t m_vecDamagePosition = 0x111c; // C_PhysPropClientside
		}
		namespace C_PhysicsProp {
			constexpr std::ptrdiff_t m_bAwake = 0x1110; // C_PhysicsProp
		}
		namespace C_PlantedC4 {
			constexpr std::ptrdiff_t m_AttributeManager = 0xff0; // C_PlantedC4
			constexpr std::ptrdiff_t m_bBeingDefused = 0xfcc; // C_PlantedC4
			constexpr std::ptrdiff_t m_bBombDefused = 0xfe4; // C_PlantedC4
			constexpr std::ptrdiff_t m_bBombTicking = 0xf90; // C_PlantedC4
			constexpr std::ptrdiff_t m_bC4Activated = 0xfd8; // C_PlantedC4
			constexpr std::ptrdiff_t m_bCannotBeDefused = 0xfc4; // C_PlantedC4
			constexpr std::ptrdiff_t m_bExplodeWarning = 0xfd4; // C_PlantedC4
			constexpr std::ptrdiff_t m_bHasExploded = 0xfc5; // C_PlantedC4
			constexpr std::ptrdiff_t m_bRadarFlash = 0x14a0; // C_PlantedC4
			constexpr std::ptrdiff_t m_bTenSecWarning = 0xfd9; // C_PlantedC4
			constexpr std::ptrdiff_t m_bTriggerWarning = 0xfd0; // C_PlantedC4
			constexpr std::ptrdiff_t m_entitySpottedState = 0xfa0; // C_PlantedC4
			constexpr std::ptrdiff_t m_fLastDefuseTime = 0x14a8; // C_PlantedC4
			constexpr std::ptrdiff_t m_flC4Blow = 0xfc0; // C_PlantedC4
			constexpr std::ptrdiff_t m_flC4ExplodeSpectateDuration = 0x14d0; // C_PlantedC4
			constexpr std::ptrdiff_t m_flDefuseCountDown = 0xfe0; // C_PlantedC4
			constexpr std::ptrdiff_t m_flDefuseLength = 0xfdc; // C_PlantedC4
			constexpr std::ptrdiff_t m_flNextBeep = 0xfbc; // C_PlantedC4
			constexpr std::ptrdiff_t m_flNextGlow = 0xfb8; // C_PlantedC4
			constexpr std::ptrdiff_t m_flNextRadarFlashTime = 0x149c; // C_PlantedC4
			constexpr std::ptrdiff_t m_flTimerLength = 0xfc8; // C_PlantedC4
			constexpr std::ptrdiff_t m_hBombDefuser = 0xfe8; // C_PlantedC4
			constexpr std::ptrdiff_t m_hControlPanel = 0xfec; // C_PlantedC4
			constexpr std::ptrdiff_t m_hDefuserMultimeter = 0x1498; // C_PlantedC4
			constexpr std::ptrdiff_t m_nBombSite = 0xf94; // C_PlantedC4
			constexpr std::ptrdiff_t m_nSourceSoundscapeHash = 0xf98; // C_PlantedC4
			constexpr std::ptrdiff_t m_pBombDefuser = 0x14a4; // C_PlantedC4
			constexpr std::ptrdiff_t m_pPredictionOwner = 0x14b0; // C_PlantedC4
			constexpr std::ptrdiff_t m_vecC4ExplodeSpectateAng = 0x14c4; // C_PlantedC4
			constexpr std::ptrdiff_t m_vecC4ExplodeSpectatePos = 0x14b8; // C_PlantedC4
		}
		namespace C_PlayerPing {
			constexpr std::ptrdiff_t m_bUrgent = 0x5a4; // C_PlayerPing
			constexpr std::ptrdiff_t m_hPingedEntity = 0x59c; // C_PlayerPing
			constexpr std::ptrdiff_t m_hPlayer = 0x598; // C_PlayerPing
			constexpr std::ptrdiff_t m_iType = 0x5a0; // C_PlayerPing
			constexpr std::ptrdiff_t m_szPlaceName = 0x5a5; // C_PlayerPing
		}
		namespace C_PlayerSprayDecal {
			constexpr std::ptrdiff_t m_SprayRenderHelper = 0xe08; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_flCreationTime = 0xd74; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_nEntity = 0xd6c; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_nHitbox = 0xd70; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_nPlayer = 0xd68; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_nTintID = 0xd78; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_nUniqueID = 0xd28; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_nVersion = 0xd7c; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_rtGcTime = 0xd34; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_ubSignature = 0xd7d; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_unAccountID = 0xd2c; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_unTraceID = 0xd30; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_vecEndPos = 0xd38; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_vecLeft = 0xd50; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_vecNormal = 0xd5c; // C_PlayerSprayDecal
			constexpr std::ptrdiff_t m_vecStart = 0xd44; // C_PlayerSprayDecal
		}
		namespace C_PlayerVisibility {
			constexpr std::ptrdiff_t m_bIsEnabled = 0x579; // C_PlayerVisibility
			constexpr std::ptrdiff_t m_bStartDisabled = 0x578; // C_PlayerVisibility
			constexpr std::ptrdiff_t m_flFadeTime = 0x574; // C_PlayerVisibility
			constexpr std::ptrdiff_t m_flFogDistanceMultiplier = 0x56c; // C_PlayerVisibility
			constexpr std::ptrdiff_t m_flFogMaxDensityMultiplier = 0x570; // C_PlayerVisibility
			constexpr std::ptrdiff_t m_flVisibilityStrength = 0x568; // C_PlayerVisibility
		}
		namespace C_PointCamera {
			constexpr std::ptrdiff_t m_DegreesPerSecond = 0x5b8; // C_PointCamera
			constexpr std::ptrdiff_t m_FOV = 0x568; // C_PointCamera
			constexpr std::ptrdiff_t m_FogColor = 0x571; // C_PointCamera
			constexpr std::ptrdiff_t m_Resolution = 0x56c; // C_PointCamera
			constexpr std::ptrdiff_t m_TargetFOV = 0x5b4; // C_PointCamera
			constexpr std::ptrdiff_t m_bActive = 0x584; // C_PointCamera
			constexpr std::ptrdiff_t m_bAlignWithParent = 0x59d; // C_PointCamera
			constexpr std::ptrdiff_t m_bCanHLTVUse = 0x59c; // C_PointCamera
			constexpr std::ptrdiff_t m_bDofEnabled = 0x59e; // C_PointCamera
			constexpr std::ptrdiff_t m_bFogEnable = 0x570; // C_PointCamera
			constexpr std::ptrdiff_t m_bIsOn = 0x5bc; // C_PointCamera
			constexpr std::ptrdiff_t m_bNoSky = 0x58c; // C_PointCamera
			constexpr std::ptrdiff_t m_bUseScreenAspectRatio = 0x585; // C_PointCamera
			constexpr std::ptrdiff_t m_fBrightness = 0x590; // C_PointCamera
			constexpr std::ptrdiff_t m_flAspectRatio = 0x588; // C_PointCamera
			constexpr std::ptrdiff_t m_flDofFarBlurry = 0x5ac; // C_PointCamera
			constexpr std::ptrdiff_t m_flDofFarCrisp = 0x5a8; // C_PointCamera
			constexpr std::ptrdiff_t m_flDofNearBlurry = 0x5a0; // C_PointCamera
			constexpr std::ptrdiff_t m_flDofNearCrisp = 0x5a4; // C_PointCamera
			constexpr std::ptrdiff_t m_flDofTiltToGround = 0x5b0; // C_PointCamera
			constexpr std::ptrdiff_t m_flFogEnd = 0x57c; // C_PointCamera
			constexpr std::ptrdiff_t m_flFogMaxDensity = 0x580; // C_PointCamera
			constexpr std::ptrdiff_t m_flFogStart = 0x578; // C_PointCamera
			constexpr std::ptrdiff_t m_flZFar = 0x594; // C_PointCamera
			constexpr std::ptrdiff_t m_flZNear = 0x598; // C_PointCamera
			constexpr std::ptrdiff_t m_pNext = 0x5c0; // C_PointCamera
		}
		namespace C_PointCameraVFOV {
			constexpr std::ptrdiff_t m_flVerticalFOV = 0x5c8; // C_PointCameraVFOV
		}
		namespace C_PointClientUIDialog {
			constexpr std::ptrdiff_t m_bStartEnabled = 0xd5c; // C_PointClientUIDialog
			constexpr std::ptrdiff_t m_hActivator = 0xd58; // C_PointClientUIDialog
		}
		namespace C_PointClientUIHUD {
			constexpr std::ptrdiff_t m_bAllowInteractionFromAllSceneWorlds = 0xf08; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_bCheckCSSClasses = 0xd60; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_bIgnoreInput = 0xee0; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_flDPI = 0xeec; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_flDepthOffset = 0xef4; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_flHeight = 0xee8; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_flInteractDistance = 0xef0; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_flWidth = 0xee4; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_unHorizontalAlign = 0xefc; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_unOrientation = 0xf04; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_unOwnerContext = 0xef8; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_unVerticalAlign = 0xf00; // C_PointClientUIHUD
			constexpr std::ptrdiff_t m_vecCSSClasses = 0xf10; // C_PointClientUIHUD
		}
		namespace C_PointClientUIWorldPanel {
			constexpr std::ptrdiff_t m_anchorDeltaTransform = 0xd70; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bAllowInteractionFromAllSceneWorlds = 0xf58; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bCheckCSSClasses = 0xd62; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bDisableMipGen = 0xf7f; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bExcludeFromSaveGames = 0xf7c; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bFollowPlayerAcrossTeleport = 0xf32; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bForceRecreateNextUpdate = 0xd60; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bGrabbable = 0xf7d; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bIgnoreInput = 0xf30; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bLit = 0xf31; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bMoveViewToPlayerNextThink = 0xd61; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bNoDepth = 0xf79; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bOnlyRenderToTexture = 0xf7e; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bOpaque = 0xf78; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bRenderBackface = 0xf7a; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_bUseOffScreenIndicator = 0xf7b; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_flDPI = 0xf3c; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_flDepthOffset = 0xf44; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_flHeight = 0xf38; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_flInteractDistance = 0xf40; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_flWidth = 0xf34; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_nExplicitImageLayout = 0xf80; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_pOffScreenIndicator = 0xf08; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_unHorizontalAlign = 0xf4c; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_unOrientation = 0xf54; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_unOwnerContext = 0xf48; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_unVerticalAlign = 0xf50; // C_PointClientUIWorldPanel
			constexpr std::ptrdiff_t m_vecCSSClasses = 0xf60; // C_PointClientUIWorldPanel
		}
		namespace C_PointClientUIWorldTextPanel {
			constexpr std::ptrdiff_t m_messageText = 0xf90; // C_PointClientUIWorldTextPanel
		}
		namespace C_PointCommentaryNode {
			constexpr std::ptrdiff_t m_bActive = 0xf90; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_bListenedTo = 0xfc0; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_bRestartAfterRestore = 0xfd4; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_bWasActive = 0xf91; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_flEndTime = 0xf94; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_flStartTime = 0xf98; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_flStartTimeInCommentary = 0xf9c; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_hViewPosition = 0xfd0; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_iNodeNumber = 0xfb8; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_iNodeNumberMax = 0xfbc; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_iszCommentaryFile = 0xfa0; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_iszSpeakers = 0xfb0; // C_PointCommentaryNode
			constexpr std::ptrdiff_t m_iszTitle = 0xfa8; // C_PointCommentaryNode
		}
		namespace C_PointValueRemapper {
			constexpr std::ptrdiff_t m_bDisabled = 0x568; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_bDisabledOld = 0x569; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_bEngaged = 0x5c8; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_bFirstUpdate = 0x5c9; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_bRequiresUseKey = 0x584; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_bUpdateOnClient = 0x56a; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flCurrentMomentum = 0x5b8; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flDisengageDistance = 0x57c; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flEngageDistance = 0x580; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flInputOffset = 0x5c4; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flMaximumChangePerSecond = 0x578; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flMomentumModifier = 0x5b0; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flPreviousUpdateTickTime = 0x5d0; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flPreviousValue = 0x5cc; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flRatchetOffset = 0x5c0; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_flSnapValue = 0x5b4; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_hOutputEntities = 0x590; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_hRemapLineEnd = 0x574; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_hRemapLineStart = 0x570; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_nHapticsType = 0x5a8; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_nInputType = 0x56c; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_nMomentumType = 0x5ac; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_nOutputType = 0x588; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_nRatchetType = 0x5bc; // C_PointValueRemapper
			constexpr std::ptrdiff_t m_vecPreviousTestPoint = 0x5d4; // C_PointValueRemapper
		}
		namespace C_PointWorldText {
			constexpr std::ptrdiff_t m_BackgroundMaterialName = 0xf88; // C_PointWorldText
			constexpr std::ptrdiff_t m_Color = 0xfe8; // C_PointWorldText
			constexpr std::ptrdiff_t m_FontName = 0xf48; // C_PointWorldText
			constexpr std::ptrdiff_t m_bDrawBackground = 0xfd8; // C_PointWorldText
			constexpr std::ptrdiff_t m_bEnabled = 0xfc8; // C_PointWorldText
			constexpr std::ptrdiff_t m_bForceRecreateNextUpdate = 0xd30; // C_PointWorldText
			constexpr std::ptrdiff_t m_bFullbright = 0xfc9; // C_PointWorldText
			constexpr std::ptrdiff_t m_flBackgroundBorderHeight = 0xfe0; // C_PointWorldText
			constexpr std::ptrdiff_t m_flBackgroundBorderWidth = 0xfdc; // C_PointWorldText
			constexpr std::ptrdiff_t m_flBackgroundWorldToUV = 0xfe4; // C_PointWorldText
			constexpr std::ptrdiff_t m_flDepthOffset = 0xfd4; // C_PointWorldText
			constexpr std::ptrdiff_t m_flFontSize = 0xfd0; // C_PointWorldText
			constexpr std::ptrdiff_t m_flWorldUnitsPerPx = 0xfcc; // C_PointWorldText
			constexpr std::ptrdiff_t m_messageText = 0xd48; // C_PointWorldText
			constexpr std::ptrdiff_t m_nJustifyHorizontal = 0xfec; // C_PointWorldText
			constexpr std::ptrdiff_t m_nJustifyVertical = 0xff0; // C_PointWorldText
			constexpr std::ptrdiff_t m_nReorientMode = 0xff4; // C_PointWorldText
		}
		namespace C_PostProcessingVolume {
			constexpr std::ptrdiff_t m_bExposureControl = 0xd6d; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_bMaster = 0xd6c; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flExposureCompensation = 0xd5c; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flExposureFadeSpeedDown = 0xd64; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flExposureFadeSpeedUp = 0xd60; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flFadeDuration = 0xd48; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flMaxExposure = 0xd58; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flMaxLogExposure = 0xd50; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flMinExposure = 0xd54; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flMinLogExposure = 0xd4c; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flRate = 0xd70; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flTonemapEVSmoothingRange = 0xd68; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flTonemapMinAvgLum = 0xd7c; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flTonemapPercentBrightPixels = 0xd78; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_flTonemapPercentTarget = 0xd74; // C_PostProcessingVolume
			constexpr std::ptrdiff_t m_hPostSettings = 0xd40; // C_PostProcessingVolume
		}
		namespace C_Precipitation {
			constexpr std::ptrdiff_t m_bActiveParticlePrecipEmitter = 0xd78; // C_Precipitation
			constexpr std::ptrdiff_t m_bHasSimulatedSinceLastSceneObjectUpdate = 0xd7a; // C_Precipitation
			constexpr std::ptrdiff_t m_bParticlePrecipInitialized = 0xd79; // C_Precipitation
			constexpr std::ptrdiff_t m_flDensity = 0xd30; // C_Precipitation
			constexpr std::ptrdiff_t m_flParticleInnerDist = 0xd40; // C_Precipitation
			constexpr std::ptrdiff_t m_nAvailableSheetSequencesMaxIndex = 0xd7c; // C_Precipitation
			constexpr std::ptrdiff_t m_pParticleDef = 0xd48; // C_Precipitation
			constexpr std::ptrdiff_t m_tParticlePrecipTraceTimer = 0xd70; // C_Precipitation
		}
		namespace C_PredictedViewModel {
			constexpr std::ptrdiff_t m_currentSpeed = 0x1008; // C_PredictedViewModel
			constexpr std::ptrdiff_t m_targetSpeed = 0xffc; // C_PredictedViewModel
			constexpr std::ptrdiff_t m_vPredictedLagOffset = 0xff0; // C_PredictedViewModel
		}
		namespace C_RagdollProp {
			constexpr std::ptrdiff_t m_flBlendWeight = 0xfc0; // C_RagdollProp
			constexpr std::ptrdiff_t m_flBlendWeightCurrent = 0xfcc; // C_RagdollProp
			constexpr std::ptrdiff_t m_hRagdollSource = 0xfc4; // C_RagdollProp
			constexpr std::ptrdiff_t m_iEyeAttachment = 0xfc8; // C_RagdollProp
			constexpr std::ptrdiff_t m_parentPhysicsBoneIndices = 0xfd0; // C_RagdollProp
			constexpr std::ptrdiff_t m_ragAngles = 0xfa8; // C_RagdollProp
			constexpr std::ptrdiff_t m_ragPos = 0xf90; // C_RagdollProp
			constexpr std::ptrdiff_t m_worldSpaceBoneComputationOrder = 0xfe8; // C_RagdollProp
		}
		namespace C_RagdollPropAttached {
			constexpr std::ptrdiff_t m_attachmentPointBoneSpace = 0x1008; // C_RagdollPropAttached
			constexpr std::ptrdiff_t m_attachmentPointRagdollSpace = 0x1014; // C_RagdollPropAttached
			constexpr std::ptrdiff_t m_bHasParent = 0x1030; // C_RagdollPropAttached
			constexpr std::ptrdiff_t m_boneIndexAttached = 0x1000; // C_RagdollPropAttached
			constexpr std::ptrdiff_t m_parentTime = 0x102c; // C_RagdollPropAttached
			constexpr std::ptrdiff_t m_ragdollAttachedObjectIndex = 0x1004; // C_RagdollPropAttached
			constexpr std::ptrdiff_t m_vecOffset = 0x1020; // C_RagdollPropAttached
		}
		namespace C_RectLight {
			constexpr std::ptrdiff_t m_bShowLight = 0x1070; // C_RectLight
		}
		namespace C_RetakeGameRules {
			constexpr std::ptrdiff_t m_bBlockersPresent = 0xfc; // C_RetakeGameRules
			constexpr std::ptrdiff_t m_bRoundInProgress = 0xfd; // C_RetakeGameRules
			constexpr std::ptrdiff_t m_iBombSite = 0x104; // C_RetakeGameRules
			constexpr std::ptrdiff_t m_iFirstSecondHalfRound = 0x100; // C_RetakeGameRules
			constexpr std::ptrdiff_t m_nMatchSeed = 0xf8; // C_RetakeGameRules
		}
		namespace C_RopeKeyframe {
			constexpr std::ptrdiff_t m_LightValues = 0xfe8; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_LinksTouchingSomething = 0xd30; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_PhysicsDelegate = 0x1080; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_RopeFlags = 0xd68; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_RopeLength = 0x1070; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_Slack = 0x1072; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_Subdiv = 0x106e; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_TextureHeight = 0x1098; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_TextureScale = 0x1074; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_Width = 0x107c; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bApplyWind = 0xd38; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bConstrainBetweenEndpoints = 0x1108; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bEndPointAttachmentAnglesDirty = 0x0; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bEndPointAttachmentPositionsDirty = 0x0; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bNewDataThisFrame = 0x0; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bPhysicsInitted = 0x0; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_bPrevEndPointPos = 0xd44; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_fLockedPoints = 0x1078; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_fPrevLockedPoints = 0xd3c; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_flCurScroll = 0xd60; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_flCurrentGustLifetime = 0x10b8; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_flCurrentGustTimer = 0x10b4; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_flScrollSpeed = 0xd64; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_flTimeToNextGust = 0x10bc; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_hEndPoint = 0x1068; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_hMaterial = 0x1090; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_hStartPoint = 0x1064; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_iEndAttachment = 0x106d; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_iForcePointMoveCounter = 0xd40; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_iRopeMaterialModelIndex = 0xd70; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_iStartAttachment = 0x106c; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_nChangeCount = 0x1079; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_nLinksTouchingSomething = 0xd34; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_nSegments = 0x1060; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vCachedEndPointAttachmentAngle = 0x10f0; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vCachedEndPointAttachmentPos = 0x10d8; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vColorMod = 0x10cc; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vPrevEndPointPos = 0xd48; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vWindDir = 0x10c0; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vecImpulse = 0x109c; // C_RopeKeyframe
			constexpr std::ptrdiff_t m_vecPreviousImpulse = 0x10a8; // C_RopeKeyframe
		}
		namespace C_RopeKeyframe__CPhysicsDelegate {
			constexpr std::ptrdiff_t m_pKeyframe = 0x8; // C_RopeKeyframe__CPhysicsDelegate
		}
		namespace C_SceneEntity {
			constexpr std::ptrdiff_t m_QueuedEvents = 0x5a8; // C_SceneEntity
			constexpr std::ptrdiff_t m_bAutogenerated = 0x573; // C_SceneEntity
			constexpr std::ptrdiff_t m_bClientOnly = 0x57a; // C_SceneEntity
			constexpr std::ptrdiff_t m_bIsPlayingBack = 0x570; // C_SceneEntity
			constexpr std::ptrdiff_t m_bMultiplayer = 0x572; // C_SceneEntity
			constexpr std::ptrdiff_t m_bPaused = 0x571; // C_SceneEntity
			constexpr std::ptrdiff_t m_bWasPlaying = 0x598; // C_SceneEntity
			constexpr std::ptrdiff_t m_flCurrentTime = 0x5c0; // C_SceneEntity
			constexpr std::ptrdiff_t m_flForceClientTime = 0x574; // C_SceneEntity
			constexpr std::ptrdiff_t m_hActorList = 0x580; // C_SceneEntity
			constexpr std::ptrdiff_t m_hOwner = 0x57c; // C_SceneEntity
			constexpr std::ptrdiff_t m_nSceneStringIndex = 0x578; // C_SceneEntity
		}
		namespace C_SceneEntity__QueuedEvents_t {
			constexpr std::ptrdiff_t starttime = 0x0; // C_SceneEntity__QueuedEvents_t
		}
		namespace C_ShatterGlassShardPhysics {
			constexpr std::ptrdiff_t m_ShardDesc = 0x1120; // C_ShatterGlassShardPhysics
		}
		namespace C_SkyCamera {
			constexpr std::ptrdiff_t m_bUseAngles = 0x5fc; // C_SkyCamera
			constexpr std::ptrdiff_t m_pNext = 0x600; // C_SkyCamera
			constexpr std::ptrdiff_t m_skyboxData = 0x568; // C_SkyCamera
			constexpr std::ptrdiff_t m_skyboxSlotToken = 0x5f8; // C_SkyCamera
		}
		namespace C_SmokeGrenadeProjectile {
			constexpr std::ptrdiff_t m_VoxelFrameData = 0x1238; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_bDidSmokeEffect = 0x1214; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_bSmokeEffectSpawned = 0x1259; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_bSmokeVolumeDataReceived = 0x1258; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_nRandomSeed = 0x1218; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_nSmokeEffectTickBegin = 0x1210; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_nVoxelFrameDataSize = 0x1250; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_nVoxelUpdate = 0x1254; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_vSmokeColor = 0x121c; // C_SmokeGrenadeProjectile
			constexpr std::ptrdiff_t m_vSmokeDetonationPos = 0x1228; // C_SmokeGrenadeProjectile
		}
		namespace C_SoundAreaEntityBase {
			constexpr std::ptrdiff_t m_bDisabled = 0x568; // C_SoundAreaEntityBase
			constexpr std::ptrdiff_t m_bWasEnabled = 0x570; // C_SoundAreaEntityBase
			constexpr std::ptrdiff_t m_iszSoundAreaType = 0x578; // C_SoundAreaEntityBase
			constexpr std::ptrdiff_t m_vPos = 0x580; // C_SoundAreaEntityBase
		}
		namespace C_SoundAreaEntityOrientedBox {
			constexpr std::ptrdiff_t m_vMax = 0x59c; // C_SoundAreaEntityOrientedBox
			constexpr std::ptrdiff_t m_vMin = 0x590; // C_SoundAreaEntityOrientedBox
		}
		namespace C_SoundAreaEntitySphere {
			constexpr std::ptrdiff_t m_flRadius = 0x590; // C_SoundAreaEntitySphere
		}
		namespace C_SoundEventAABBEntity {
			constexpr std::ptrdiff_t m_vMaxs = 0x634; // C_SoundEventAABBEntity
			constexpr std::ptrdiff_t m_vMins = 0x628; // C_SoundEventAABBEntity
		}
		namespace C_SoundEventEntity {
			constexpr std::ptrdiff_t m_bClientSideOnly = 0x0; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_bSaveRestore = 0x56b; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_bSavedIsPlaying = 0x56c; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_bStartOnSpawn = 0x568; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_bStopOnNew = 0x56a; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_bToLocalPlayer = 0x569; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_flClientCullRadius = 0x5d8; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_flSavedElapsedTime = 0x570; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_hSource = 0x618; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_iszAttachmentName = 0x580; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_iszSoundName = 0x608; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_iszSourceEntityName = 0x578; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_nEntityIndexSelection = 0x61c; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_onGUIDChanged = 0x588; // C_SoundEventEntity
			constexpr std::ptrdiff_t m_onSoundFinished = 0x5b0; // C_SoundEventEntity
		}
		namespace C_SoundEventOBBEntity {
			constexpr std::ptrdiff_t m_vMaxs = 0x634; // C_SoundEventOBBEntity
			constexpr std::ptrdiff_t m_vMins = 0x628; // C_SoundEventOBBEntity
		}
		namespace C_SoundEventPathCornerEntity {
			constexpr std::ptrdiff_t m_vecCornerPairsNetworked = 0x628; // C_SoundEventPathCornerEntity
		}
		namespace C_SoundEventSphereEntity {
			constexpr std::ptrdiff_t m_flRadius = 0x628; // C_SoundEventSphereEntity
		}
		namespace C_SoundOpvarSetPointBase {
			constexpr std::ptrdiff_t m_bUseAutoCompare = 0x584; // C_SoundOpvarSetPointBase
			constexpr std::ptrdiff_t m_iOpvarIndex = 0x580; // C_SoundOpvarSetPointBase
			constexpr std::ptrdiff_t m_iszOperatorName = 0x570; // C_SoundOpvarSetPointBase
			constexpr std::ptrdiff_t m_iszOpvarName = 0x578; // C_SoundOpvarSetPointBase
			constexpr std::ptrdiff_t m_iszStackName = 0x568; // C_SoundOpvarSetPointBase
		}
		namespace C_SpotlightEnd {
			constexpr std::ptrdiff_t m_Radius = 0xd2c; // C_SpotlightEnd
			constexpr std::ptrdiff_t m_flLightScale = 0xd28; // C_SpotlightEnd
		}
		namespace C_Sprite {
			constexpr std::ptrdiff_t m_bWorldSpaceScale = 0xd60; // C_Sprite
			constexpr std::ptrdiff_t m_flBrightnessDuration = 0xd54; // C_Sprite
			constexpr std::ptrdiff_t m_flBrightnessTimeStart = 0xd88; // C_Sprite
			constexpr std::ptrdiff_t m_flDestScale = 0xd78; // C_Sprite
			constexpr std::ptrdiff_t m_flDieTime = 0xd40; // C_Sprite
			constexpr std::ptrdiff_t m_flFrame = 0xd3c; // C_Sprite
			constexpr std::ptrdiff_t m_flGlowProxySize = 0xd64; // C_Sprite
			constexpr std::ptrdiff_t m_flHDRColorScale = 0xd68; // C_Sprite
			constexpr std::ptrdiff_t m_flLastTime = 0xd6c; // C_Sprite
			constexpr std::ptrdiff_t m_flMaxFrame = 0xd70; // C_Sprite
			constexpr std::ptrdiff_t m_flScaleDuration = 0xd5c; // C_Sprite
			constexpr std::ptrdiff_t m_flScaleTimeStart = 0xd7c; // C_Sprite
			constexpr std::ptrdiff_t m_flSpriteFramerate = 0xd38; // C_Sprite
			constexpr std::ptrdiff_t m_flSpriteScale = 0xd58; // C_Sprite
			constexpr std::ptrdiff_t m_flStartScale = 0xd74; // C_Sprite
			constexpr std::ptrdiff_t m_hAttachedToEntity = 0xd30; // C_Sprite
			constexpr std::ptrdiff_t m_hOldSpriteMaterial = 0xd90; // C_Sprite
			constexpr std::ptrdiff_t m_hSpriteMaterial = 0xd28; // C_Sprite
			constexpr std::ptrdiff_t m_nAttachment = 0xd34; // C_Sprite
			constexpr std::ptrdiff_t m_nBrightness = 0xd50; // C_Sprite
			constexpr std::ptrdiff_t m_nDestBrightness = 0xd84; // C_Sprite
			constexpr std::ptrdiff_t m_nSpriteHeight = 0xe34; // C_Sprite
			constexpr std::ptrdiff_t m_nSpriteWidth = 0xe30; // C_Sprite
			constexpr std::ptrdiff_t m_nStartBrightness = 0xd80; // C_Sprite
		}
		namespace C_StattrakModule {
			constexpr std::ptrdiff_t m_bKnife = 0xf90; // C_StattrakModule
		}
		namespace C_Sun {
			constexpr std::ptrdiff_t m_bOn = 0xd64; // C_Sun
			constexpr std::ptrdiff_t m_bmaxColor = 0xd65; // C_Sun
			constexpr std::ptrdiff_t m_clrOverlay = 0xd60; // C_Sun
			constexpr std::ptrdiff_t m_fdistNormalize = 0xd30; // C_Sun
			constexpr std::ptrdiff_t m_flAlphaHaze = 0xd78; // C_Sun
			constexpr std::ptrdiff_t m_flAlphaHdr = 0xd80; // C_Sun
			constexpr std::ptrdiff_t m_flAlphaScale = 0xd7c; // C_Sun
			constexpr std::ptrdiff_t m_flFarZScale = 0xd84; // C_Sun
			constexpr std::ptrdiff_t m_flHDRColorScale = 0xd74; // C_Sun
			constexpr std::ptrdiff_t m_flHazeScale = 0xd6c; // C_Sun
			constexpr std::ptrdiff_t m_flRotation = 0xd70; // C_Sun
			constexpr std::ptrdiff_t m_flSize = 0xd68; // C_Sun
			constexpr std::ptrdiff_t m_fxSSSunFlareEffectIndex = 0xd28; // C_Sun
			constexpr std::ptrdiff_t m_fxSunFlareEffectIndex = 0xd2c; // C_Sun
			constexpr std::ptrdiff_t m_iszEffectName = 0xd50; // C_Sun
			constexpr std::ptrdiff_t m_iszSSEffectName = 0xd58; // C_Sun
			constexpr std::ptrdiff_t m_vDirection = 0xd40; // C_Sun
			constexpr std::ptrdiff_t m_vSunPos = 0xd34; // C_Sun
		}
		namespace C_Team {
			constexpr std::ptrdiff_t m_aPlayerControllers = 0x568; // C_Team
			constexpr std::ptrdiff_t m_aPlayers = 0x580; // C_Team
			constexpr std::ptrdiff_t m_iScore = 0x598; // C_Team
			constexpr std::ptrdiff_t m_szTeamname = 0x59c; // C_Team
		}
		namespace C_TeamRoundTimer {
			constexpr std::ptrdiff_t m_bAutoCountdown = 0x584; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire10SecRemain = 0x5a0; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire1MinRemain = 0x59e; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire1SecRemain = 0x5a5; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire2MinRemain = 0x59d; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire2SecRemain = 0x5a4; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire30SecRemain = 0x59f; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire3MinRemain = 0x59c; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire3SecRemain = 0x5a3; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire4MinRemain = 0x59b; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire4SecRemain = 0x5a2; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire5MinRemain = 0x59a; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFire5SecRemain = 0x5a1; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bFireFinished = 0x599; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bInCaptureWatchState = 0x591; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bIsDisabled = 0x574; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bShowInHUD = 0x575; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bStartPaused = 0x590; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bStopWatchTimer = 0x598; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_bTimerPaused = 0x568; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_flTimeRemaining = 0x56c; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_flTimerEndTime = 0x570; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_flTotalTime = 0x594; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nOldTimerLength = 0x5a8; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nOldTimerState = 0x5ac; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nSetupTimeLength = 0x588; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nState = 0x58c; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nTimerInitialLength = 0x57c; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nTimerLength = 0x578; // C_TeamRoundTimer
			constexpr std::ptrdiff_t m_nTimerMaxLength = 0x580; // C_TeamRoundTimer
		}
		namespace C_TextureBasedAnimatable {
			constexpr std::ptrdiff_t m_bLoop = 0xd28; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_flFPS = 0xd2c; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_flStartFrame = 0xd5c; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_flStartTime = 0xd58; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_hPositionKeys = 0xd30; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_hRotationKeys = 0xd38; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_vAnimationBoundsMax = 0xd4c; // C_TextureBasedAnimatable
			constexpr std::ptrdiff_t m_vAnimationBoundsMin = 0xd40; // C_TextureBasedAnimatable
		}
		namespace C_TonemapController2 {
			constexpr std::ptrdiff_t m_flAutoExposureMax = 0x56c; // C_TonemapController2
			constexpr std::ptrdiff_t m_flAutoExposureMin = 0x568; // C_TonemapController2
			constexpr std::ptrdiff_t m_flExposureAdaptationSpeedDown = 0x580; // C_TonemapController2
			constexpr std::ptrdiff_t m_flExposureAdaptationSpeedUp = 0x57c; // C_TonemapController2
			constexpr std::ptrdiff_t m_flTonemapEVSmoothingRange = 0x584; // C_TonemapController2
			constexpr std::ptrdiff_t m_flTonemapMinAvgLum = 0x578; // C_TonemapController2
			constexpr std::ptrdiff_t m_flTonemapPercentBrightPixels = 0x574; // C_TonemapController2
			constexpr std::ptrdiff_t m_flTonemapPercentTarget = 0x570; // C_TonemapController2
		}
		namespace C_TriggerBuoyancy {
			constexpr std::ptrdiff_t m_BuoyancyHelper = 0xd30; // C_TriggerBuoyancy
			constexpr std::ptrdiff_t m_flFluidDensity = 0xdb0; // C_TriggerBuoyancy
		}
		namespace C_TriggerPhysics {
			constexpr std::ptrdiff_t m_angularDamping = 0xd40; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_angularLimit = 0xd3c; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_bCollapseToForcePoint = 0xd5c; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_bConvertToDebrisWhenPossible = 0xd78; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_flDampingRatio = 0xd4c; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_flFrequency = 0xd48; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_gravityScale = 0xd30; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_linearDamping = 0xd38; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_linearForce = 0xd44; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_linearLimit = 0xd34; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_vecLinearForceDirection = 0xd6c; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_vecLinearForcePointAt = 0xd50; // C_TriggerPhysics
			constexpr std::ptrdiff_t m_vecLinearForcePointAtWorld = 0xd60; // C_TriggerPhysics
		}
		namespace C_ViewmodelAttachmentModel {
			constexpr std::ptrdiff_t m_bCreatedLeftHanded = 0xf91; // C_ViewmodelAttachmentModel
			constexpr std::ptrdiff_t m_bShouldFrontFaceCullLeftHanded = 0xf90; // C_ViewmodelAttachmentModel
		}
		namespace C_VoteController {
			constexpr std::ptrdiff_t m_bIsYesNoVote = 0x59a; // C_VoteController
			constexpr std::ptrdiff_t m_bTypeDirty = 0x599; // C_VoteController
			constexpr std::ptrdiff_t m_bVotesDirty = 0x598; // C_VoteController
			constexpr std::ptrdiff_t m_iActiveIssueIndex = 0x578; // C_VoteController
			constexpr std::ptrdiff_t m_iOnlyTeamToVote = 0x57c; // C_VoteController
			constexpr std::ptrdiff_t m_nPotentialVotes = 0x594; // C_VoteController
			constexpr std::ptrdiff_t m_nVoteOptionCount = 0x580; // C_VoteController
		}
		namespace C_WeaponBaseItem {
			constexpr std::ptrdiff_t m_SequenceCompleteTimer = 0x1b20; // C_WeaponBaseItem
			constexpr std::ptrdiff_t m_bRedraw = 0x1b38; // C_WeaponBaseItem
		}
		namespace C_WeaponShield {
			constexpr std::ptrdiff_t m_flDisplayHealth = 0x1b40; // C_WeaponShield
		}
		namespace C_WeaponTaser {
			constexpr std::ptrdiff_t m_fFireTime = 0x1b40; // C_WeaponTaser
			constexpr std::ptrdiff_t m_nLastAttackTick = 0x1b44; // C_WeaponTaser
		}
		namespace C_fogplayerparams_t {
			constexpr std::ptrdiff_t m_NewColor = 0x28; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_OldColor = 0x10; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flNewEnd = 0x30; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flNewFarZ = 0x3c; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flNewHDRColorScale = 0x38; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flNewMaxDensity = 0x34; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flNewStart = 0x2c; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flOldEnd = 0x18; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flOldFarZ = 0x24; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flOldHDRColorScale = 0x20; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flOldMaxDensity = 0x1c; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flOldStart = 0x14; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_flTransitionTime = 0xc; // C_fogplayerparams_t
			constexpr std::ptrdiff_t m_hCtrl = 0x8; // C_fogplayerparams_t
		}
		namespace CountdownTimer {
			constexpr std::ptrdiff_t m_duration = 0x8; // CountdownTimer
			constexpr std::ptrdiff_t m_nWorldGroupId = 0x14; // CountdownTimer
			constexpr std::ptrdiff_t m_timescale = 0x10; // CountdownTimer
			constexpr std::ptrdiff_t m_timestamp = 0xc; // CountdownTimer
		}
		namespace EngineCountdownTimer {
			constexpr std::ptrdiff_t m_duration = 0x8; // EngineCountdownTimer
			constexpr std::ptrdiff_t m_timescale = 0x10; // EngineCountdownTimer
			constexpr std::ptrdiff_t m_timestamp = 0xc; // EngineCountdownTimer
		}
		namespace EntityRenderAttribute_t {
			constexpr std::ptrdiff_t m_ID = 0x30; // EntityRenderAttribute_t
			constexpr std::ptrdiff_t m_Values = 0x34; // EntityRenderAttribute_t
		}
		namespace EntitySpottedState_t {
			constexpr std::ptrdiff_t m_bSpotted = 0x8; // EntitySpottedState_t
			constexpr std::ptrdiff_t m_bSpottedByMask = 0xc; // EntitySpottedState_t
		}
		namespace IntervalTimer {
			constexpr std::ptrdiff_t m_nWorldGroupId = 0xc; // IntervalTimer
			constexpr std::ptrdiff_t m_timestamp = 0x8; // IntervalTimer
		}
		namespace PhysicsRagdollPose_t {
			constexpr std::ptrdiff_t m_Transforms = 0x8; // PhysicsRagdollPose_t
			constexpr std::ptrdiff_t m_hOwner = 0x20; // PhysicsRagdollPose_t
		}
		namespace PredictedDamageTag_t {
			constexpr std::ptrdiff_t flFlinchModLarge = 0x38; // PredictedDamageTag_t
			constexpr std::ptrdiff_t flFlinchModSmall = 0x34; // PredictedDamageTag_t
			constexpr std::ptrdiff_t flFriendlyFireDamageReductionRatio = 0x3c; // PredictedDamageTag_t
			constexpr std::ptrdiff_t nTagTick = 0x30; // PredictedDamageTag_t
		}
		namespace SellbackPurchaseEntry_t {
			constexpr std::ptrdiff_t m_bPrevHelmet = 0x3c; // SellbackPurchaseEntry_t
			constexpr std::ptrdiff_t m_hItem = 0x40; // SellbackPurchaseEntry_t
			constexpr std::ptrdiff_t m_nCost = 0x34; // SellbackPurchaseEntry_t
			constexpr std::ptrdiff_t m_nPrevArmor = 0x38; // SellbackPurchaseEntry_t
			constexpr std::ptrdiff_t m_unDefIdx = 0x30; // SellbackPurchaseEntry_t
		}
		namespace SequenceHistory_t {
			constexpr std::ptrdiff_t m_flCyclesPerSecond = 0x14; // SequenceHistory_t
			constexpr std::ptrdiff_t m_flPlaybackRate = 0x10; // SequenceHistory_t
			constexpr std::ptrdiff_t m_flSeqFixedCycle = 0x8; // SequenceHistory_t
			constexpr std::ptrdiff_t m_flSeqStartTime = 0x4; // SequenceHistory_t
			constexpr std::ptrdiff_t m_hSequence = 0x0; // SequenceHistory_t
			constexpr std::ptrdiff_t m_nSeqLoopMode = 0xc; // SequenceHistory_t
		}
		namespace ServerAuthoritativeWeaponSlot_t {
			constexpr std::ptrdiff_t unClass = 0x28; // ServerAuthoritativeWeaponSlot_t
			constexpr std::ptrdiff_t unItemDefIdx = 0x2c; // ServerAuthoritativeWeaponSlot_t
			constexpr std::ptrdiff_t unSlot = 0x2a; // ServerAuthoritativeWeaponSlot_t
		}
		namespace VPhysicsCollisionAttribute_t {
			constexpr std::ptrdiff_t m_nCollisionFunctionMask = 0x2b; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nCollisionGroup = 0x2a; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nEntityId = 0x20; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nHierarchyId = 0x28; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nInteractsAs = 0x8; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nInteractsExclude = 0x18; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nInteractsWith = 0x10; // VPhysicsCollisionAttribute_t
			constexpr std::ptrdiff_t m_nOwnerId = 0x24; // VPhysicsCollisionAttribute_t
		}
		namespace ViewAngleServerChange_t {
			constexpr std::ptrdiff_t nIndex = 0x40; // ViewAngleServerChange_t
			constexpr std::ptrdiff_t nType = 0x30; // ViewAngleServerChange_t
			constexpr std::ptrdiff_t qAngle = 0x34; // ViewAngleServerChange_t
		}
		namespace WeaponPurchaseCount_t {
			constexpr std::ptrdiff_t m_nCount = 0x32; // WeaponPurchaseCount_t
			constexpr std::ptrdiff_t m_nItemDefIndex = 0x30; // WeaponPurchaseCount_t
		}
		namespace WeaponPurchaseTracker_t {
			constexpr std::ptrdiff_t m_weaponPurchases = 0x8; // WeaponPurchaseTracker_t
		}
		namespace audioparams_t {
			constexpr std::ptrdiff_t localBits = 0x6c; // audioparams_t
			constexpr std::ptrdiff_t localSound = 0x8; // audioparams_t
			constexpr std::ptrdiff_t soundEventHash = 0x74; // audioparams_t
			constexpr std::ptrdiff_t soundscapeEntityListIndex = 0x70; // audioparams_t
			constexpr std::ptrdiff_t soundscapeIndex = 0x68; // audioparams_t
		}
		namespace fogparams_t {
			constexpr std::ptrdiff_t HDRColorScale = 0x38; // fogparams_t
			constexpr std::ptrdiff_t blend = 0x65; // fogparams_t
			constexpr std::ptrdiff_t blendtobackground = 0x58; // fogparams_t
			constexpr std::ptrdiff_t colorPrimary = 0x14; // fogparams_t
			constexpr std::ptrdiff_t colorPrimaryLerpTo = 0x1c; // fogparams_t
			constexpr std::ptrdiff_t colorSecondary = 0x18; // fogparams_t
			constexpr std::ptrdiff_t colorSecondaryLerpTo = 0x20; // fogparams_t
			constexpr std::ptrdiff_t dirPrimary = 0x8; // fogparams_t
			constexpr std::ptrdiff_t duration = 0x54; // fogparams_t
			constexpr std::ptrdiff_t enable = 0x64; // fogparams_t
			constexpr std::ptrdiff_t end = 0x28; // fogparams_t
			constexpr std::ptrdiff_t endLerpTo = 0x48; // fogparams_t
			constexpr std::ptrdiff_t exponent = 0x34; // fogparams_t
			constexpr std::ptrdiff_t farz = 0x2c; // fogparams_t
			constexpr std::ptrdiff_t lerptime = 0x50; // fogparams_t
			constexpr std::ptrdiff_t locallightscale = 0x60; // fogparams_t
			constexpr std::ptrdiff_t m_bNoReflectionFog = 0x66; // fogparams_t
			constexpr std::ptrdiff_t m_bPadding = 0x67; // fogparams_t
			constexpr std::ptrdiff_t maxdensity = 0x30; // fogparams_t
			constexpr std::ptrdiff_t maxdensityLerpTo = 0x4c; // fogparams_t
			constexpr std::ptrdiff_t scattering = 0x5c; // fogparams_t
			constexpr std::ptrdiff_t skyboxFogFactor = 0x3c; // fogparams_t
			constexpr std::ptrdiff_t skyboxFogFactorLerpTo = 0x40; // fogparams_t
			constexpr std::ptrdiff_t start = 0x24; // fogparams_t
			constexpr std::ptrdiff_t startLerpTo = 0x44; // fogparams_t
		}
		namespace shard_model_desc_t {
			constexpr std::ptrdiff_t m_SurfacePropStringToken = 0x78; // shard_model_desc_t
			constexpr std::ptrdiff_t m_bHasParent = 0x74; // shard_model_desc_t
			constexpr std::ptrdiff_t m_bParentFrozen = 0x75; // shard_model_desc_t
			constexpr std::ptrdiff_t m_flGlassHalfThickness = 0x70; // shard_model_desc_t
			constexpr std::ptrdiff_t m_hMaterialBase = 0x10; // shard_model_desc_t
			constexpr std::ptrdiff_t m_hMaterialDamageOverlay = 0x18; // shard_model_desc_t
			constexpr std::ptrdiff_t m_nModelID = 0x8; // shard_model_desc_t
			constexpr std::ptrdiff_t m_solid = 0x20; // shard_model_desc_t
			constexpr std::ptrdiff_t m_vInitialPanelVertices = 0x58; // shard_model_desc_t
			constexpr std::ptrdiff_t m_vecPanelSize = 0x24; // shard_model_desc_t
			constexpr std::ptrdiff_t m_vecPanelVertices = 0x40; // shard_model_desc_t
			constexpr std::ptrdiff_t m_vecStressPositionA = 0x2c; // shard_model_desc_t
			constexpr std::ptrdiff_t m_vecStressPositionB = 0x34; // shard_model_desc_t
		}
		namespace sky3dparams_t {
			constexpr std::ptrdiff_t bClip3DSkyBoxNearToWorldFar = 0x18; // sky3dparams_t
			constexpr std::ptrdiff_t flClip3DSkyBoxNearToWorldFarOffset = 0x1c; // sky3dparams_t
			constexpr std::ptrdiff_t fog = 0x20; // sky3dparams_t
			constexpr std::ptrdiff_t m_nWorldGroupID = 0x88; // sky3dparams_t
			constexpr std::ptrdiff_t origin = 0xc; // sky3dparams_t
			constexpr std::ptrdiff_t scale = 0x8; // sky3dparams_t
		}
}