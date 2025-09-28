// dumped by shxdows dumper (csdump)
# dumped by shxdows dumper (csdump) 

from enum import Enum

class CVSoundFormat_t(Enum):
    ADPCM = 3
    MP3 = 2
    PCM16 = 0
    PCM8 = 1

class EMidiNote(Enum):
    A = 9
    A_Sharp = 10
    B = 11
    C = 0
    C_Sharp = 1
    Count = 12
    D = 2
    D_Sharp = 3
    E = 4
    F = 5
    F_Sharp = 6
    G = 7
    G_Sharp = 8

class EMode_t(Enum):
    Peak = 0
    RMS = 1

class EWaveform(Enum):
    Noise = 4
    Saw = 2
    Sine = 0
    Square = 1
    Triangle = 3

class PlayBackMode_t(Enum):
    Random = 0
    RandomAvoidLast = 2
    RandomNoRepeats = 1
    RandomWeights = 4
    Sequential = 3

class SosActionSortType_t(Enum):
    SOS_SORTTYPE_HIGHEST = 0
    SOS_SORTTYPE_LOWEST = 1

class SosActionStopType_t(Enum):
    SOS_STOPTYPE_NONE = 0
    SOS_STOPTYPE_OPVAR = 2
    SOS_STOPTYPE_TIME = 1

class SosEditItemType_t(Enum):
    SOS_EDIT_ITEM_TYPE_FIELD = 5
    SOS_EDIT_ITEM_TYPE_LIBRARYSTACKS = 2
    SOS_EDIT_ITEM_TYPE_OPERATOR = 4
    SOS_EDIT_ITEM_TYPE_SOUNDEVENT = 1
    SOS_EDIT_ITEM_TYPE_SOUNDEVENTS = 0
    SOS_EDIT_ITEM_TYPE_STACK = 3

class SosGroupFieldBehavior_t(Enum):
    kBranch = 1
    kIgnore = 0
    kMatch = 2

class SosGroupType_t(Enum):
    SOS_GROUPTYPE_DYNAMIC = 0
    SOS_GROUPTYPE_STATIC = 1

class VMixChannelOperation_t(Enum):
    VMIX_CHAN_LEFT = 1
    VMIX_CHAN_MID_SIDE = 5
    VMIX_CHAN_MONO = 4
    VMIX_CHAN_RIGHT = 2
    VMIX_CHAN_STEREO = 0
    VMIX_CHAN_SWAP = 3

class VMixFilterSlope_t(Enum):
    FILTER_SLOPE_12dB = 4
    FILTER_SLOPE_1POLE_12dB = 1
    FILTER_SLOPE_1POLE_18dB = 2
    FILTER_SLOPE_1POLE_24dB = 3
    FILTER_SLOPE_1POLE_6dB = 0
    FILTER_SLOPE_24dB = 5
    FILTER_SLOPE_36dB = 6
    FILTER_SLOPE_48dB = 7
    FILTER_SLOPE_MAX = 7

class VMixFilterType_t(Enum):
    FILTER_ALLPASS = 7
    FILTER_BANDPASS = 2
    FILTER_HIGHPASS = 1
    FILTER_HIGH_SHELF = 6
    FILTER_LOWPASS = 0
    FILTER_LOW_SHELF = 5
    FILTER_NOTCH = 3
    FILTER_PASSTHROUGH = 8
    FILTER_PEAKING_EQ = 4
    FILTER_UNKNOWN = -1

class VMixGraphCommandID_t(Enum):
    CMD_BLEND_VSNDS_TO_IMPULSERESPONSE = 37
    CMD_CONTROL_COND_COPY_IF_NEGATIVE = 8
    CMD_CONTROL_COPY = 7
    CMD_CONTROL_EVALUATE_CURVE = 6
    CMD_CONTROL_EVAL_ENVELOPE = 15
    CMD_CONTROL_INCREMENT_TIMER = 14
    CMD_CONTROL_INPUT_STORE = 1
    CMD_CONTROL_INPUT_STORE_DB = 2
    CMD_CONTROL_MAX = 12
    CMD_CONTROL_OUTPUT_STORE = 5
    CMD_CONTROL_REMAP_LINEAR = 9
    CMD_CONTROL_REMAP_LOGLINEAR = 11
    CMD_CONTROL_REMAP_SINE = 10
    CMD_CONTROL_RESET_TIMER = 13
    CMD_CONTROL_SINE_BLEND = 16
    CMD_CONTROL_TRANSIENT_INPUT_RESET = 4
    CMD_CONTROL_TRANSIENT_INPUT_STORE = 3
    CMD_IMPULSERESPONSE_DELAY = 38
    CMD_IMPULSERESPONSE_INPUT_STORE = 33
    CMD_IMPULSERESPONSE_RESET = 36
    CMD_INVALID = -1
    CMD_PROCESSOR_SET_CONTROL_ARRAYVALUE = 19
    CMD_PROCESSOR_SET_CONTROL_VALUE = 17
    CMD_PROCESSOR_SET_IMPULSERESPONSE_VALUE = 34
    CMD_PROCESSOR_SET_NAME_INPUT = 18
    CMD_PROCESSOR_SET_VSND_VALUE = 21
    CMD_PROCESSOR_STORE_CONTROL_VALUE = 20
    CMD_REMAP_VSND_TO_IMPULSERESPONSE = 35
    CMD_SUBMIX_ACCUMULATE = 30
    CMD_SUBMIX_COPY = 29
    CMD_SUBMIX_DEBUG = 25
    CMD_SUBMIX_GENERATE = 23
    CMD_SUBMIX_GENERATE_SIDECHAIN = 24
    CMD_SUBMIX_METER = 31
    CMD_SUBMIX_METER_SPECTRUM = 32
    CMD_SUBMIX_MIX2x1 = 26
    CMD_SUBMIX_OUTPUT = 27
    CMD_SUBMIX_OUTPUTx2 = 28
    CMD_SUBMIX_PROCESS = 22

class VMixLFOShape_t(Enum):
    LFO_SHAPE_NOISE = 4
    LFO_SHAPE_SAW = 3
    LFO_SHAPE_SINE = 0
    LFO_SHAPE_SQUARE = 1
    LFO_SHAPE_TRI = 2

class VMixPannerType_t(Enum):
    PANNER_TYPE_EQUAL_POWER = 1
    PANNER_TYPE_LINEAR = 0

class VMixProcessorType_t(Enum):
    VPROCESSOR_AUTOFILTER = 25
    VPROCESSOR_BOXVERB = 8
    VPROCESSOR_BOXVERB2 = 9
    VPROCESSOR_CONVOLUTION = 18
    VPROCESSOR_DELAY = 5
    VPROCESSOR_DIFFUSOR = 7
    VPROCESSOR_DUAL_COMPRESSOR = 19
    VPROCESSOR_DYNAMICS = 3
    VPROCESSOR_DYNAMICS_3BAND = 20
    VPROCESSOR_DYNAMICS_COMPRESSOR = 21
    VPROCESSOR_EFFECT_CHAIN = 28
    VPROCESSOR_ENVELOPE = 16
    VPROCESSOR_EQ8 = 15
    VPROCESSOR_FILTER = 13
    VPROCESSOR_FREEVERB = 10
    VPROCESSOR_FULLWAVE_INTEGRATOR = 12
    VPROCESSOR_MOD_DELAY = 6
    VPROCESSOR_OSC = 26
    VPROCESSOR_PANNER = 23
    VPROCESSOR_PLATEVERB = 11
    VPROCESSOR_PRESETDSP = 4
    VPROCESSOR_RT_PITCH = 1
    VPROCESSOR_SHAPER = 22
    VPROCESSOR_STEAMAUDIO_DIRECT = 30
    VPROCESSOR_STEAMAUDIO_HRTF = 2
    VPROCESSOR_STEAMAUDIO_HYBRIDREVERB = 31
    VPROCESSOR_STEAMAUDIO_PATHING = 14
    VPROCESSOR_STEREODELAY = 27
    VPROCESSOR_SUBGRAPH_SWITCH = 29
    VPROCESSOR_UNKNOWN = 0
    VPROCESSOR_UTILITY = 24
    VPROCESSOR_VOCODER = 17

class VMixSubgraphSwitchInterpolationType_t(Enum):
    SUBGRAPH_INTERPOLATION_KEEP_LAST_SUBGRAPH_RUNNING = 2
    SUBGRAPH_INTERPOLATION_TEMPORAL_CROSSFADE = 0
    SUBGRAPH_INTERPOLATION_TEMPORAL_FADE_OUT = 1

class soundlevel_t(Enum):
    SNDLVL_100dB = 100
    SNDLVL_105dB = 105
    SNDLVL_110dB = 110
    SNDLVL_120dB = 120
    SNDLVL_130dB = 130
    SNDLVL_140dB = 140
    SNDLVL_150dB = 150
    SNDLVL_180dB = 180
    SNDLVL_20dB = 20
    SNDLVL_25dB = 25
    SNDLVL_30dB = 30
    SNDLVL_35dB = 35
    SNDLVL_40dB = 40
    SNDLVL_45dB = 45
    SNDLVL_50dB = 50
    SNDLVL_55dB = 55
    SNDLVL_60dB = 60
    SNDLVL_65dB = 65
    SNDLVL_70dB = 70
    SNDLVL_75dB = 75
    SNDLVL_80dB = 80
    SNDLVL_85dB = 85
    SNDLVL_90dB = 90
    SNDLVL_95dB = 95
    SNDLVL_GUNFIRE = 140
    SNDLVL_IDLE = 60
    SNDLVL_NONE = 0
    SNDLVL_NORM = 75
    SNDLVL_STATIC = 66
    SNDLVL_TALKING = 80

class CAudioEmphasisSample:
    m_flTime = 0  # offset
    m_flValue = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAudioMorphData:
    m_flEaseIn = 96  # offset
    m_flEaseOut = 100  # offset
    m_nameHashCodes = 24  # offset
    m_nameStrings = 48  # offset
    m_samples = 72  # offset
    m_times = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAudioPhonemeTag:
    m_flEndTime = 4  # offset
    m_flStartTime = 0  # offset
    m_nPhonemeCode = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAudioSentence:
    m_EmphasisSamples = 32  # offset
    m_RunTimePhonemes = 8  # offset
    m_bShouldVoiceDuck = 0  # offset
    m_morphData = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDSPMixgroupModifier:
    m_flListenerReverbModifierWhenSourceReverbIsActive = 24  # offset
    m_flModifier = 8  # offset
    m_flModifierMin = 12  # offset
    m_flSourceModifier = 16  # offset
    m_flSourceModifierMin = 20  # offset
    m_mixgroup = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDSPPresetMixgroupModifierTable:
    m_table = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MVDataNodeType",
            "type": "Unknown"
        }
    ]

class CDspPresetModifierList:
    m_dspName = 0  # offset
    m_modifiers = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSosGroupActionLimitSchema:
    m_bCountStopped = 21  # offset
    m_bStopImmediate = 20  # offset
    m_nMaxCount = 8  # offset
    m_nSortType = 16  # offset
    m_nStopType = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionMemberCountEnvelopeSchema:
    m_bSaveToGroup = 40  # offset
    m_flAttack = 24  # offset
    m_flBaseValue = 16  # offset
    m_flDecay = 28  # offset
    m_flTargetValue = 20  # offset
    m_nBaseCount = 8  # offset
    m_nTargetCount = 12  # offset
    m_resultVarName = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionSchema:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSosGroupActionSetSoundeventParameterSchema:
    m_flMaxValue = 16  # offset
    m_flMinValue = 12  # offset
    m_nMaxCount = 8  # offset
    m_nSortType = 32  # offset
    m_opvarName = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionSoundeventClusterSchema:
    m_clusterSizeOpvar = 32  # offset
    m_flClusterEpsilon = 12  # offset
    m_groupBoundingBoxMaxsOpvar = 48  # offset
    m_groupBoundingBoxMinsOpvar = 40  # offset
    m_nMinNearby = 8  # offset
    m_shouldPlayClusterChild = 24  # offset
    m_shouldPlayOpvar = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionSoundeventCountSchema:
    m_bExcludeStoppedSounds = 8  # offset
    m_strCountKeyName = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionSoundeventMinMaxValuesSchema:
    m_bExcludSoundsAboveThreshold = 32  # offset
    m_bExcludeDelayedSounds = 25  # offset
    m_bExcludeSoundsBelowThreshold = 26  # offset
    m_bExcludeStoppedSounds = 24  # offset
    m_flExcludeSoundsMaxThresholdValue = 36  # offset
    m_flExcludeSoundsMinThresholdValue = 28  # offset
    m_strDelayPublicFieldName = 16  # offset
    m_strMaxValueName = 48  # offset
    m_strMinValueName = 40  # offset
    m_strQueryPublicFieldName = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionSoundeventPrioritySchema:
    m_bPriorityReadButDontContribute = 32  # offset
    m_priorityContributeButDontRead = 24  # offset
    m_priorityValue = 8  # offset
    m_priorityVolumeScalar = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionTimeBlockLimitSchema:
    m_flMaxDuration = 12  # offset
    m_nMaxCount = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosGroupActionTimeLimitSchema:
    m_flMaxDuration = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CSosSoundEventGroupSchema:
    m_Behavior_EntIndex = 56  # offset
    m_Behavior_EventName = 28  # offset
    m_Behavior_Opvar = 64  # offset
    m_Behavior_String = 72  # offset
    m_bBlocksEvents = 12  # offset
    m_bInvertMatch = 24  # offset
    m_bMatchEventSubString = 40  # offset
    m_flEntIndex = 60  # offset
    m_flMemberLifespanTime = 20  # offset
    m_flOpvar = 68  # offset
    m_matchSoundEventName = 32  # offset
    m_matchSoundEventSubString = 48  # offset
    m_nBlockMaxCount = 16  # offset
    m_nGroupType = 8  # offset
    m_opvarString = 80  # offset
    m_vActions = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSoundContainerReference:
    m_bUseReference = 0  # offset
    m_pSound = 16  # offset
    m_sound = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CSoundContainerReferenceArray:
    m_bUseReference = 0  # offset
    m_pSounds = 32  # offset
    m_sounds = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CSoundEventMetaData:
    m_soundEventVMix = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSoundInfoHeader:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTestBlendContainer:
    m_firstSound = 184  # offset
    m_secondSound = 192  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVSound:
    m_Sentences = 24  # offset
    m_encodedHeader = 88  # offset
    m_flDuration = 20  # offset
    m_nChannels = 8  # offset
    m_nFormat = 4  # offset
    m_nLoopEnd = 80  # offset
    m_nLoopStart = 12  # offset
    m_nRate = 0  # offset
    m_nSampleCount = 16  # offset
    m_nSeekTable = 56  # offset
    m_nStreamingSize = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVoiceContainerAmpedDecayingSineWave:
    m_flGainAmount = 192  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerAnalysisBase:
    m_bRegenerateCurveOnCompile = 8  # offset
    m_curve = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MVDataNodeType",
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

class CVoiceContainerBase:
    m_pEnvelopeAnalyzer = 176  # offset
    m_vSound = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MVDataNodeType",
            "type": "Unknown"
        },
        {
            "name": "MVDataFileExtension",
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

class CVoiceContainerBlender:
    m_firstSound = 184  # offset
    m_flBlendFactor = 232  # offset
    m_secondSound = 208  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerDecayingSineWave:
    m_flDecayTime = 188  # offset
    m_flFrequency = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerDefault:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerEnvelope:
    m_analysisContainer = 192  # offset
    m_sound = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerEnvelopeAnalyzer:
    m_fAnalysisWindowMs = 84  # offset
    m_flThreshold = 88  # offset
    m_mode = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerGranulator:
    m_bShouldWraparound = 200  # offset
    m_flGrainCrossfadeAmount = 188  # offset
    m_flGrainLength = 184  # offset
    m_flPlaybackJitter = 196  # offset
    m_flStartJitter = 192  # offset
    m_sourceAudio = 208  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CVoiceContainerLoopTrigger:
    m_bCrossFade = 220  # offset
    m_flFadeTime = 216  # offset
    m_flRetriggerTimeMax = 212  # offset
    m_flRetriggerTimeMin = 208  # offset
    m_sound = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerNull:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerParameterBlender:
    m_bEnableDistanceBlend = 368  # offset
    m_bEnableOcclusionBlend = 232  # offset
    m_curve1 = 240  # offset
    m_curve2 = 304  # offset
    m_curve3 = 376  # offset
    m_curve4 = 440  # offset
    m_firstSound = 184  # offset
    m_secondSound = 208  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerRandomSampler:
    m_flAmplitude = 184  # offset
    m_flAmplitudeJitter = 188  # offset
    m_flMaxLength = 196  # offset
    m_flTimeJitter = 192  # offset
    m_grainResources = 208  # offset
    m_nNumDelayVariations = 200  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerRealtimeFMSineWave:
    m_flCarrierFrequency = 184  # offset
    m_flModulatorAmount = 192  # offset
    m_flModulatorFrequency = 188  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerSelector:
    m_fProbabilityWeights = 248  # offset
    m_mode = 184  # offset
    m_soundsToPlay = 192  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerSet:
    m_soundsToPlay = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerSetElement:
    m_flVolumeDB = 24  # offset
    m_sound = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVoiceContainerShapedNoise:
    m_bUseCurveForAmplitude = 328  # offset
    m_bUseCurveForFrequency = 184  # offset
    m_bUseCurveForResonance = 256  # offset
    m_flFrequency = 188  # offset
    m_flGainInDecibels = 332  # offset
    m_flResonance = 260  # offset
    m_frequencySweep = 192  # offset
    m_gainSweep = 336  # offset
    m_resonanceSweep = 264  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerStaticAdditiveSynth:
    m_tones = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class CVoiceContainerStaticAdditiveSynth__CGainScalePerInstance:
    m_flMaxVolume = 8  # offset
    m_flMinVolume = 0  # offset
    m_nInstancesAtMaxVolume = 12  # offset
    m_nInstancesAtMinVolume = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVoiceContainerStaticAdditiveSynth__CHarmonic:
    m_curve = 16  # offset
    m_flCents = 8  # offset
    m_flPhase = 12  # offset
    m_nFundamental = 1  # offset
    m_nOctave = 4  # offset
    m_nWaveform = 0  # offset
    m_volumeScaling = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVoiceContainerStaticAdditiveSynth__CTone:
    m_bSyncInstances = 88  # offset
    m_curve = 24  # offset
    m_harmonics = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVoiceContainerSwitch:
    m_soundsToPlay = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
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

class SelectedEditItemInfo_t:
    m_EditItems = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SosEditItemInfo_t:
    itemKVString = 32  # offset
    itemName = 8  # offset
    itemPos = 40  # offset
    itemType = 0  # offset
    itemTypeName = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixAutoFilterDesc_t:
    m_filter = 12  # offset
    m_flAttackTimeMS = 4  # offset
    m_flEnvelopeAmount = 0  # offset
    m_flLFOAmount = 28  # offset
    m_flLFORate = 32  # offset
    m_flPhase = 36  # offset
    m_flReleaseTimeMS = 8  # offset
    m_nLFOShape = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixBoxverb2Desc_t:
    m_bParallel = 24  # offset
    m_filterType = 28  # offset
    m_flComplexity = 8  # offset
    m_flDepth = 52  # offset
    m_flDiffusion = 12  # offset
    m_flFeedbackDepth = 68  # offset
    m_flFeedbackHeight = 64  # offset
    m_flFeedbackScale = 56  # offset
    m_flFeedbackWidth = 60  # offset
    m_flHeight = 48  # offset
    m_flModDepth = 16  # offset
    m_flModRate = 20  # offset
    m_flOutputGain = 72  # offset
    m_flSizeMax = 0  # offset
    m_flSizeMin = 4  # offset
    m_flTaps = 76  # offset
    m_flWidth = 44  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixBoxverbDesc_t:
    m_bParallel = 24  # offset
    m_filterType = 28  # offset
    m_flComplexity = 8  # offset
    m_flDepth = 52  # offset
    m_flDiffusion = 12  # offset
    m_flFeedbackDepth = 68  # offset
    m_flFeedbackHeight = 64  # offset
    m_flFeedbackScale = 56  # offset
    m_flFeedbackWidth = 60  # offset
    m_flHeight = 48  # offset
    m_flModDepth = 16  # offset
    m_flModRate = 20  # offset
    m_flOutputGain = 72  # offset
    m_flSizeMax = 0  # offset
    m_flSizeMin = 4  # offset
    m_flTaps = 76  # offset
    m_flWidth = 44  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixConvolutionDesc_t:
    m_flHighCutoffFreq = 28  # offset
    m_flLowCutoffFreq = 24  # offset
    m_flPreDelayMS = 4  # offset
    m_flWetMix = 8  # offset
    m_fldbGain = 0  # offset
    m_fldbHigh = 20  # offset
    m_fldbLow = 12  # offset
    m_fldbMid = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDelayDesc_t:
    m_bEnableFilter = 16  # offset
    m_feedbackFilter = 0  # offset
    m_flDelay = 20  # offset
    m_flDelayGain = 28  # offset
    m_flDirectGain = 24  # offset
    m_flFeedbackGain = 32  # offset
    m_flWidth = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDiffusorDesc_t:
    m_flComplexity = 4  # offset
    m_flFeedback = 8  # offset
    m_flOutputGain = 12  # offset
    m_flSize = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDualCompressorDesc_t:
    m_bPeakMode = 12  # offset
    m_bandDesc = 16  # offset
    m_flRMSTimeMS = 0  # offset
    m_flWetMix = 8  # offset
    m_fldbKneeWidth = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDynamics3BandDesc_t:
    m_bPeakMode = 32  # offset
    m_bandDesc = 36  # offset
    m_flDepth = 12  # offset
    m_flHighCutoffFreq = 28  # offset
    m_flLowCutoffFreq = 24  # offset
    m_flRMSTimeMS = 4  # offset
    m_flTimeScale = 20  # offset
    m_flWetMix = 16  # offset
    m_fldbGainOutput = 0  # offset
    m_fldbKneeWidth = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDynamicsBand_t:
    m_bEnable = 32  # offset
    m_bSolo = 33  # offset
    m_flAttackTimeMS = 24  # offset
    m_flRatioAbove = 20  # offset
    m_flRatioBelow = 16  # offset
    m_flReleaseTimeMS = 28  # offset
    m_fldbGainInput = 0  # offset
    m_fldbGainOutput = 4  # offset
    m_fldbThresholdAbove = 12  # offset
    m_fldbThresholdBelow = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDynamicsCompressorDesc_t:
    m_bPeakMode = 32  # offset
    m_flAttackTimeMS = 16  # offset
    m_flCompressionRatio = 12  # offset
    m_flRMSTimeMS = 24  # offset
    m_flReleaseTimeMS = 20  # offset
    m_flWetMix = 28  # offset
    m_fldbCompressionThreshold = 4  # offset
    m_fldbKneeWidth = 8  # offset
    m_fldbOutputGain = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixDynamicsDesc_t:
    m_bPeakMode = 44  # offset
    m_flAttackTimeMS = 28  # offset
    m_flLimiterRatio = 24  # offset
    m_flRMSTimeMS = 36  # offset
    m_flRatio = 20  # offset
    m_flReleaseTimeMS = 32  # offset
    m_flWetMix = 40  # offset
    m_fldbCompressionThreshold = 8  # offset
    m_fldbGain = 0  # offset
    m_fldbKneeWidth = 16  # offset
    m_fldbLimiterThreshold = 12  # offset
    m_fldbNoiseGateThreshold = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixEQ8Desc_t:
    m_stages = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixEffectChainDesc_t:
    m_flCrossfadeTime = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixEnvelopeDesc_t:
    m_flAttackTimeMS = 0  # offset
    m_flHoldTimeMS = 4  # offset
    m_flReleaseTimeMS = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixFilterDesc_t:
    m_bEnabled = 3  # offset
    m_flCutoffFreq = 8  # offset
    m_flQ = 12  # offset
    m_fldbGain = 4  # offset
    m_nFilterSlope = 2  # offset
    m_nFilterType = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixFreeverbDesc_t:
    m_flDamp = 4  # offset
    m_flLateReflections = 12  # offset
    m_flRoomSize = 0  # offset
    m_flWidth = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixModDelayDesc_t:
    m_bApplyAntialiasing = 44  # offset
    m_bPhaseInvert = 16  # offset
    m_feedbackFilter = 0  # offset
    m_flDelay = 24  # offset
    m_flFeedbackGain = 32  # offset
    m_flGlideTime = 20  # offset
    m_flModDepth = 40  # offset
    m_flModRate = 36  # offset
    m_flOutputGain = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixOscDesc_t:
    m_flPhase = 8  # offset
    m_freq = 4  # offset
    oscType = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixPannerDesc_t:
    m_flStrength = 4  # offset
    m_type = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixPitchShiftDesc_t:
    m_flPitchShift = 4  # offset
    m_nGrainSampleCount = 0  # offset
    m_nProcType = 12  # offset
    m_nQuality = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixPlateverbDesc_t:
    m_flDamp = 16  # offset
    m_flDecay = 12  # offset
    m_flFeedbackDiffusion1 = 20  # offset
    m_flFeedbackDiffusion2 = 24  # offset
    m_flInputDiffusion1 = 4  # offset
    m_flInputDiffusion2 = 8  # offset
    m_flPrefilter = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixShaperDesc_t:
    m_flWetMix = 12  # offset
    m_fldbDrive = 4  # offset
    m_fldbOutputGain = 8  # offset
    m_nOversampleFactor = 16  # offset
    m_nShape = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixSubgraphSwitchDesc_t:
    m_bOnlyTailsOnFadeOut = 4  # offset
    m_flInterpolationTime = 8  # offset
    m_interpolationMode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixUtilityDesc_t:
    m_bBassMono = 16  # offset
    m_flBassFreq = 20  # offset
    m_flInputPan = 4  # offset
    m_flOutputBalance = 8  # offset
    m_fldbOutputGain = 12  # offset
    m_nOp = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMixVocoderDesc_t:
    m_bPeakMode = 36  # offset
    m_flAttackTimeMS = 24  # offset
    m_flBandwidth = 4  # offset
    m_flFreqRangeEnd = 16  # offset
    m_flFreqRangeStart = 12  # offset
    m_flReleaseTimeMS = 28  # offset
    m_fldBModGain = 8  # offset
    m_fldBUnvoicedGain = 20  # offset
    m_nBandCount = 0  # offset
    m_nDebugBand = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

