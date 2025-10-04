# dumped by shxdows dumper (csdump)

from enum import Enum

class AnimationType_t(Enum):
    ANIMATION_TYPE_FIT_LIFETIME = 1
    ANIMATION_TYPE_FIXED_RATE = 0
    ANIMATION_TYPE_MANUAL_FRAMES = 2

class BBoxVolumeType_t(Enum):
    BBOX_DIMENSIONS = 1
    BBOX_MINS_MAXS = 2
    BBOX_VOLUME = 0

class BlurFilterType_t(Enum):
    BLURFILTER_BOX = 1
    BLURFILTER_GAUSSIAN = 0

class ClosestPointTestType_t(Enum):
    PARTICLE_CLOSEST_TYPE_BOX = 0
    PARTICLE_CLOSEST_TYPE_CAPSULE = 1
    PARTICLE_CLOSEST_TYPE_HYBRID = 2

class Detail2Combo_t(Enum):
    DETAIL_2_COMBO_ADD = 1
    DETAIL_2_COMBO_ADD_SELF_ILLUM = 2
    DETAIL_2_COMBO_CROSSFADE = 5
    DETAIL_2_COMBO_MOD2X = 3
    DETAIL_2_COMBO_MUL = 4
    DETAIL_2_COMBO_OFF = 0
    DETAIL_2_COMBO_UNINITIALIZED = -1

class DetailCombo_t(Enum):
    DETAIL_COMBO_ADD = 1
    DETAIL_COMBO_ADD_SELF_ILLUM = 2
    DETAIL_COMBO_MOD2X = 3
    DETAIL_COMBO_OFF = 0

class EventTypeSelection_t(Enum):
    PARTICLE_EVENT_TYPE_MASK_COLLISION = 4
    PARTICLE_EVENT_TYPE_MASK_COLLISION_STOPPED = 16
    PARTICLE_EVENT_TYPE_MASK_FIRST_COLLISION = 8
    PARTICLE_EVENT_TYPE_MASK_KILLED = 2
    PARTICLE_EVENT_TYPE_MASK_KILLED_ON_COLLISION = 32
    PARTICLE_EVENT_TYPE_MASK_NONE = 0
    PARTICLE_EVENT_TYPE_MASK_SPAWNED = 1
    PARTICLE_EVENT_TYPE_MASK_USER_1 = 64
    PARTICLE_EVENT_TYPE_MASK_USER_2 = 128
    PARTICLE_EVENT_TYPE_MASK_USER_3 = 256
    PARTICLE_EVENT_TYPE_MASK_USER_4 = 512

class HitboxLerpType_t(Enum):
    HITBOX_LERP_CONSTANT = 1
    HITBOX_LERP_LIFETIME = 0

class InheritableBoolType_t(Enum):
    INHERITABLE_BOOL_FALSE = 1
    INHERITABLE_BOOL_INHERIT = 0
    INHERITABLE_BOOL_TRUE = 2

class MaterialProxyType_t(Enum):
    MATERIAL_PROXY_STATUS_EFFECT = 0
    MATERIAL_PROXY_TINT = 1

class MissingParentInheritBehavior_t(Enum):
    MISSING_PARENT_DO_NOTHING = -1
    MISSING_PARENT_FIND_NEW = 1
    MISSING_PARENT_KILL = 0
    MISSING_PARENT_SAME_INDEX = 2

class ModelHitboxType_t(Enum):
    MODEL_HITBOX_TYPE_RAW_BONES = 1
    MODEL_HITBOX_TYPE_RENDERBOUNDS = 2
    MODEL_HITBOX_TYPE_SNAPSHOT = 3
    MODEL_HITBOX_TYPE_STANDARD = 0

class PFuncVisualizationType_t(Enum):
    PFUNC_VISUALIZATION_BOX = 2
    PFUNC_VISUALIZATION_CYLINDER = 6
    PFUNC_VISUALIZATION_LINE = 5
    PFUNC_VISUALIZATION_PLANE = 4
    PFUNC_VISUALIZATION_RING = 3
    PFUNC_VISUALIZATION_SPHERE_SOLID = 1
    PFUNC_VISUALIZATION_SPHERE_WIREFRAME = 0

class ParticleAlphaReferenceType_t(Enum):
    PARTICLE_ALPHA_REFERENCE_ALPHA_ALPHA = 0
    PARTICLE_ALPHA_REFERENCE_ALPHA_OPAQUE = 2
    PARTICLE_ALPHA_REFERENCE_OPAQUE_ALPHA = 1
    PARTICLE_ALPHA_REFERENCE_OPAQUE_OPAQUE = 3

class ParticleAttrBoxFlags_t(Enum):
    PARTICLE_ATTR_BOX_FLAGS_ASLEEP = 8
    PARTICLE_ATTR_BOX_FLAGS_ELECTRIFIED = 4
    PARTICLE_ATTR_BOX_FLAGS_FROZEN = 16
    PARTICLE_ATTR_BOX_FLAGS_NONE = 0
    PARTICLE_ATTR_BOX_FLAGS_ON_FIRE = 2
    PARTICLE_ATTR_BOX_FLAGS_TIMED_DECAY = 32
    PARTICLE_ATTR_BOX_FLAGS_WATER = 1

class ParticleCollisionGroup_t(Enum):
    PARTICLE_COLLISION_GROUP_DEBRIS = 5
    PARTICLE_COLLISION_GROUP_DEFAULT = 4
    PARTICLE_COLLISION_GROUP_INTERACTIVE = 7
    PARTICLE_COLLISION_GROUP_NPC = 12
    PARTICLE_COLLISION_GROUP_PLAYER = 8
    PARTICLE_COLLISION_GROUP_PROPS = 24
    PARTICLE_COLLISION_GROUP_VEHICLE = 10

class ParticleCollisionMask_t(Enum):
    PARTICLE_MASK_ALL = -1
    PARTICLE_MASK_DEFAULTPLAYERSOLID = 798737
    PARTICLE_MASK_NPCSOLID = 798753
    PARTICLE_MASK_OPAQUE = 128
    PARTICLE_MASK_SHOT = 1839107
    PARTICLE_MASK_SHOT_BRUSHONLY = 1052673
    PARTICLE_MASK_SHOT_HULL = 1847297
    PARTICLE_MASK_SOLID = 798721
    PARTICLE_MASK_SOLID_WATER = 897025
    PARTICLE_MASK_WATER = 98304

class ParticleCollisionMode_t(Enum):
    COLLISION_MODE_DISABLED = -1
    COLLISION_MODE_INITIAL_TRACE_DOWN = 0
    COLLISION_MODE_PER_FRAME_PLANESET = 1
    COLLISION_MODE_PER_PARTICLE_TRACE = 3
    COLLISION_MODE_USE_NEAREST_TRACE = 2

class ParticleColorBlendMode_t(Enum):
    PARTICLEBLEND_DARKEN = 2
    PARTICLEBLEND_DEFAULT = 0
    PARTICLEBLEND_LIGHTEN = 3
    PARTICLEBLEND_MULTIPLY = 4
    PARTICLEBLEND_OVERLAY = 1

class ParticleColorBlendType_t(Enum):
    PARTICLE_COLOR_BLEND_ADD = 3
    PARTICLE_COLOR_BLEND_AVERAGE = 10
    PARTICLE_COLOR_BLEND_DIVIDE = 2
    PARTICLE_COLOR_BLEND_LUMINANCE = 12
    PARTICLE_COLOR_BLEND_MAX = 7
    PARTICLE_COLOR_BLEND_MIN = 8
    PARTICLE_COLOR_BLEND_MOD2X = 5
    PARTICLE_COLOR_BLEND_MULTIPLY = 0
    PARTICLE_COLOR_BLEND_MULTIPLY2X = 1
    PARTICLE_COLOR_BLEND_NEGATE = 11
    PARTICLE_COLOR_BLEND_REPLACE = 9
    PARTICLE_COLOR_BLEND_SCREEN = 6
    PARTICLE_COLOR_BLEND_SUBTRACT = 4

class ParticleControlPointAxis_t(Enum):
    PARTICLE_CP_AXIS_NEGATIVE_X = 3
    PARTICLE_CP_AXIS_NEGATIVE_Y = 4
    PARTICLE_CP_AXIS_NEGATIVE_Z = 5
    PARTICLE_CP_AXIS_X = 0
    PARTICLE_CP_AXIS_Y = 1
    PARTICLE_CP_AXIS_Z = 2

class ParticleDepthFeatheringMode_t(Enum):
    PARTICLE_DEPTH_FEATHERING_OFF = 0
    PARTICLE_DEPTH_FEATHERING_ON_OPTIONAL = 1
    PARTICLE_DEPTH_FEATHERING_ON_REQUIRED = 2

class ParticleDetailLevel_t(Enum):
    PARTICLEDETAIL_HIGH = 2
    PARTICLEDETAIL_LOW = 0
    PARTICLEDETAIL_MEDIUM = 1
    PARTICLEDETAIL_ULTRA = 3

class ParticleDirectionNoiseType_t(Enum):
    PARTICLE_DIR_NOISE_CURL = 1
    PARTICLE_DIR_NOISE_PERLIN = 0
    PARTICLE_DIR_NOISE_WORLEY_BASIC = 2

class ParticleEndcapMode_t(Enum):
    PARTICLE_ENDCAP_ALWAYS_ON = -1
    PARTICLE_ENDCAP_ENDCAP_OFF = 0
    PARTICLE_ENDCAP_ENDCAP_ON = 1

class ParticleFalloffFunction_t(Enum):
    PARTICLE_FALLOFF_CONSTANT = 0
    PARTICLE_FALLOFF_EXPONENTIAL = 2
    PARTICLE_FALLOFF_LINEAR = 1

class ParticleFanType_t(Enum):
    PARTICLE_FAN_TYPE_FAN = 0
    PARTICLE_FAN_TYPE_RADIAL = 2
    PARTICLE_FAN_TYPE_ROTOR_WASH = 1

class ParticleFogType_t(Enum):
    PARTICLE_FOG_DISABLED = 2
    PARTICLE_FOG_ENABLED = 1
    PARTICLE_FOG_GAME_DEFAULT = 0

class ParticleHitboxBiasType_t(Enum):
    PARTICLE_HITBOX_BIAS_ENTITY = 0
    PARTICLE_HITBOX_BIAS_HITBOX = 1

class ParticleHitboxDataSelection_t(Enum):
    PARTICLE_HITBOX_AVERAGE_SPEED = 0
    PARTICLE_HITBOX_COUNT = 1

class ParticleImpulseType_t(Enum):
    IMPULSE_TYPE_EXPLOSION = 4
    IMPULSE_TYPE_EXPLOSION_UNDERWATER = 8
    IMPULSE_TYPE_GENERIC = 1
    IMPULSE_TYPE_NONE = 0
    IMPULSE_TYPE_PARTICLE_SYSTEM = 16
    IMPULSE_TYPE_ROPE = 2

class ParticleLightBehaviorChoiceList_t(Enum):
    PARTICLE_LIGHT_BEHAVIOR_FOLLOW_DIRECTION = 0
    PARTICLE_LIGHT_BEHAVIOR_ROPE = 1
    PARTICLE_LIGHT_BEHAVIOR_TRAILS = 2

class ParticleLightFogLightingMode_t(Enum):
    PARTICLE_LIGHT_FOG_LIGHTING_MODE_DYNAMIC = 2
    PARTICLE_LIGHT_FOG_LIGHTING_MODE_DYNAMIC_NOSHADOWS = 4
    PARTICLE_LIGHT_FOG_LIGHTING_MODE_NONE = 0

class ParticleLightTypeChoiceList_t(Enum):
    PARTICLE_LIGHT_TYPE_CAPSULE = 3
    PARTICLE_LIGHT_TYPE_FX = 2
    PARTICLE_LIGHT_TYPE_POINT = 0
    PARTICLE_LIGHT_TYPE_SPOT = 1

class ParticleLightUnitChoiceList_t(Enum):
    PARTICLE_LIGHT_UNIT_CANDELAS = 0
    PARTICLE_LIGHT_UNIT_LUMENS = 1

class ParticleLightingQuality_t(Enum):
    PARTICLE_LIGHTING_PER_PARTICLE = 0
    PARTICLE_LIGHTING_PER_PIXEL = -1
    PARTICLE_LIGHTING_PER_VERTEX = 1

class ParticleLightnintBranchBehavior_t(Enum):
    PARTICLE_LIGHTNING_BRANCH_CURRENT_DIR = 0
    PARTICLE_LIGHTNING_BRANCH_ENDPOINT_DIR = 1

class ParticleLiquidContents_t(Enum):
    PARTICLE_LIQUID_NONE = 0
    PARTICLE_LIQUID_OIL = 1
    PARTICLE_LIQUID_WATER = 2

class ParticleMassMode_t(Enum):
    PARTICLE_MASSMODE_RADIUS_CUBED = 0
    PARTICLE_MASSMODE_RADIUS_SQUARED = 2

class ParticleOmni2LightTypeChoiceList_t(Enum):
    PARTICLE_OMNI2_LIGHT_TYPE_POINT = 0
    PARTICLE_OMNI2_LIGHT_TYPE_SPHERE = 1

class ParticleOrientationChoiceList_t(Enum):
    PARTICLE_ORIENTATION_ALIGN_TO_PARTICLE_NORMAL = 3
    PARTICLE_ORIENTATION_FULL_3AXIS_ROTATION = 5
    PARTICLE_ORIENTATION_SCREENALIGN_TO_PARTICLE_NORMAL = 4
    PARTICLE_ORIENTATION_SCREEN_ALIGNED = 0
    PARTICLE_ORIENTATION_SCREEN_Z_ALIGNED = 1
    PARTICLE_ORIENTATION_WORLD_Z_ALIGNED = 2

class ParticleOrientationSetMode_t(Enum):
    PARTICLE_ORIENTATION_SET_FROM_NORMAL = 1
    PARTICLE_ORIENTATION_SET_FROM_ROTATIONS = 2
    PARTICLE_ORIENTATION_SET_FROM_VELOCITY = 0
    PARTICLE_ORIENTATION_SET_NONE = -1

class ParticleOrientationType_t(Enum):
    PARTICLE_ORIENTATION_NONE = 0
    PARTICLE_ORIENTATION_NORMAL = 2
    PARTICLE_ORIENTATION_ROTATION = 4
    PARTICLE_ORIENTATION_VELOCITY = 1

class ParticleOutputBlendMode_t(Enum):
    PARTICLE_OUTPUT_BLEND_MODE_ADD = 1
    PARTICLE_OUTPUT_BLEND_MODE_ALPHA = 0
    PARTICLE_OUTPUT_BLEND_MODE_BLEND_ADD = 2
    PARTICLE_OUTPUT_BLEND_MODE_HALF_BLEND_ADD = 3
    PARTICLE_OUTPUT_BLEND_MODE_LIGHTEN = 6
    PARTICLE_OUTPUT_BLEND_MODE_MOD2X = 5
    PARTICLE_OUTPUT_BLEND_MODE_NEG_HALF_BLEND_ADD = 4

class ParticleParentSetMode_t(Enum):
    PARTICLE_SET_PARENT_IMMEDIATE = 1
    PARTICLE_SET_PARENT_NO = 0
    PARTICLE_SET_PARENT_ROOT = 1

class ParticlePinDistance_t(Enum):
    PARTICLE_PIN_COLLECTION_AGE = 10
    PARTICLE_PIN_DISTANCE_CENTER = 5
    PARTICLE_PIN_DISTANCE_CP = 6
    PARTICLE_PIN_DISTANCE_CP_PAIR_BOTH = 8
    PARTICLE_PIN_DISTANCE_CP_PAIR_EITHER = 7
    PARTICLE_PIN_DISTANCE_FARTHEST = 1
    PARTICLE_PIN_DISTANCE_FIRST = 2
    PARTICLE_PIN_DISTANCE_LAST = 3
    PARTICLE_PIN_DISTANCE_NEIGHBOR = 0
    PARTICLE_PIN_DISTANCE_NONE = -1
    PARTICLE_PIN_FLOAT_VALUE = 11
    PARTICLE_PIN_SPEED = 9

class ParticlePostProcessPriorityGroup_t(Enum):
    PARTICLE_POST_PROCESS_PRIORITY_GAMEPLAY_EFFECT = 2
    PARTICLE_POST_PROCESS_PRIORITY_GAMEPLAY_STATE_HIGH = 4
    PARTICLE_POST_PROCESS_PRIORITY_GAMEPLAY_STATE_LOW = 3
    PARTICLE_POST_PROCESS_PRIORITY_GLOBAL_UI = 5
    PARTICLE_POST_PROCESS_PRIORITY_LEVEL_OVERRIDE = 1
    PARTICLE_POST_PROCESS_PRIORITY_LEVEL_VOLUME = 0

class ParticleReplicationMode_t(Enum):
    PARTICLE_REPLICATIONMODE_NONE = 0
    PARTICLE_REPLICATIONMODE_REPLICATE_FOR_EACH_PARENT_PARTICLE = 1

class ParticleRotationLockType_t(Enum):
    PARTICLE_ROTATION_LOCK_NONE = 0
    PARTICLE_ROTATION_LOCK_NORMAL = 2
    PARTICLE_ROTATION_LOCK_ROTATIONS = 1

class ParticleSelection_t(Enum):
    PARTICLE_SELECTION_FIRST = 0
    PARTICLE_SELECTION_LAST = 1
    PARTICLE_SELECTION_NUMBER = 2

class ParticleSequenceCropOverride_t(Enum):
    PARTICLE_SEQUENCE_CROP_OVERRIDE_DEFAULT = -1
    PARTICLE_SEQUENCE_CROP_OVERRIDE_FORCE_OFF = 0
    PARTICLE_SEQUENCE_CROP_OVERRIDE_FORCE_ON = 1

class ParticleSetMethod_t(Enum):
    PARTICLE_SET_ADD_TO_CURRENT_VALUE = 5
    PARTICLE_SET_ADD_TO_INITIAL_VALUE = 2
    PARTICLE_SET_RAMP_CURRENT_VALUE = 3
    PARTICLE_SET_REPLACE_VALUE = 0
    PARTICLE_SET_SCALE_CURRENT_VALUE = 4
    PARTICLE_SET_SCALE_INITIAL_VALUE = 1

class ParticleSortingChoiceList_t(Enum):
    PARTICLE_SORTING_CREATION_TIME = 1
    PARTICLE_SORTING_NEAREST = 0

class ParticleTextureLayerBlendType_t(Enum):
    SPRITECARD_TEXTURE_BLEND_ADD = 3
    SPRITECARD_TEXTURE_BLEND_AVERAGE = 5
    SPRITECARD_TEXTURE_BLEND_LUMINANCE = 6
    SPRITECARD_TEXTURE_BLEND_MOD2X = 1
    SPRITECARD_TEXTURE_BLEND_MULTIPLY = 0
    SPRITECARD_TEXTURE_BLEND_REPLACE = 2
    SPRITECARD_TEXTURE_BLEND_SUBTRACT = 4

class ParticleTopology_t(Enum):
    PARTICLE_TOPOLOGY_CUBES = 4
    PARTICLE_TOPOLOGY_LINES = 1
    PARTICLE_TOPOLOGY_POINTS = 0
    PARTICLE_TOPOLOGY_QUADS = 3
    PARTICLE_TOPOLOGY_TRIS = 2

class ParticleTraceMissBehavior_t(Enum):
    PARTICLE_TRACE_MISS_BEHAVIOR_KILL = 1
    PARTICLE_TRACE_MISS_BEHAVIOR_NONE = 0
    PARTICLE_TRACE_MISS_BEHAVIOR_TRACE_END = 2

class ParticleTraceSet_t(Enum):
    PARTICLE_TRACE_SET_ALL = 0
    PARTICLE_TRACE_SET_DYNAMIC = 3
    PARTICLE_TRACE_SET_STATIC = 1
    PARTICLE_TRACE_SET_STATIC_AND_KEYFRAMED = 2

class ParticleVRHandChoiceList_t(Enum):
    PARTICLE_VRHAND_CP = 2
    PARTICLE_VRHAND_CP_OBJECT = 3
    PARTICLE_VRHAND_LEFT = 0
    PARTICLE_VRHAND_RIGHT = 1

class PetGroundType_t(Enum):
    PET_GROUND_GRID = 1
    PET_GROUND_NONE = 0
    PET_GROUND_PLANE = 2

class RenderModelSubModelFieldType_t(Enum):
    SUBMODEL_AS_BODYGROUP_SUBMODEL = 0
    SUBMODEL_AS_MESHGROUP_INDEX = 1
    SUBMODEL_AS_MESHGROUP_MASK = 2
    SUBMODEL_IGNORED_USE_MODEL_DEFAULT_MESHGROUP_MASK = 3

class ScalarExpressionType_t(Enum):
    SCALAR_EXPRESSION_ADD = 0
    SCALAR_EXPRESSION_DIVIDE = 3
    SCALAR_EXPRESSION_EQUAL = 8
    SCALAR_EXPRESSION_GT = 9
    SCALAR_EXPRESSION_INPUT_1 = 4
    SCALAR_EXPRESSION_LT = 10
    SCALAR_EXPRESSION_MAX = 6
    SCALAR_EXPRESSION_MIN = 5
    SCALAR_EXPRESSION_MOD = 7
    SCALAR_EXPRESSION_MUL = 2
    SCALAR_EXPRESSION_SUBTRACT = 1
    SCALAR_EXPRESSION_UNINITIALIZED = -1

class SetStatisticExpressionType_t(Enum):
    SET_EXPRESSION_MAX = 6
    SET_EXPRESSION_MEAN = 1
    SET_EXPRESSION_MEDIAN = 2
    SET_EXPRESSION_MIN = 5
    SET_EXPRESSION_MODE = 3
    SET_EXPRESSION_STANDARD_DEVIATION = 4
    SET_EXPRESSION_SUM = 0
    SET_EXPRESSION_UNINITIALIZED = -1

class SnapshotIndexType_t(Enum):
    SNAPSHOT_INDEX_DIRECT = 1
    SNAPSHOT_INDEX_INCREMENT = 0

class SpriteCardPerParticleScale_t(Enum):
    SPRITECARD_TEXTURE_PP_SCALE_ANIMATION_FRAME = 2
    SPRITECARD_TEXTURE_PP_SCALE_NEG_RANDOM = 11
    SPRITECARD_TEXTURE_PP_SCALE_NEG_RANDOM_TIME = 13
    SPRITECARD_TEXTURE_PP_SCALE_NONE = 0
    SPRITECARD_TEXTURE_PP_SCALE_PARTICLE_AGE = 1
    SPRITECARD_TEXTURE_PP_SCALE_PARTICLE_ALPHA = 5
    SPRITECARD_TEXTURE_PP_SCALE_PITCH = 9
    SPRITECARD_TEXTURE_PP_SCALE_RANDOM = 10
    SPRITECARD_TEXTURE_PP_SCALE_RANDOM_TIME = 12
    SPRITECARD_TEXTURE_PP_SCALE_ROLL = 7
    SPRITECARD_TEXTURE_PP_SCALE_SHADER_EXTRA_DATA1 = 3
    SPRITECARD_TEXTURE_PP_SCALE_SHADER_EXTRA_DATA2 = 4
    SPRITECARD_TEXTURE_PP_SCALE_SHADER_RADIUS = 6
    SPRITECARD_TEXTURE_PP_SCALE_YAW = 8

class SpriteCardShaderType_t(Enum):
    SPRITECARD_SHADER_BASE = 0
    SPRITECARD_SHADER_CUSTOM = 1

class SpriteCardTextureChannel_t(Enum):
    SPRITECARD_TEXTURE_CHANNEL_MIX_A = 2
    SPRITECARD_TEXTURE_CHANNEL_MIX_A_RGBALPHA = 7
    SPRITECARD_TEXTURE_CHANNEL_MIX_B = 11
    SPRITECARD_TEXTURE_CHANNEL_MIX_BALPHA = 14
    SPRITECARD_TEXTURE_CHANNEL_MIX_G = 10
    SPRITECARD_TEXTURE_CHANNEL_MIX_GALPHA = 13
    SPRITECARD_TEXTURE_CHANNEL_MIX_R = 9
    SPRITECARD_TEXTURE_CHANNEL_MIX_RALPHA = 12
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGB = 0
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGBA = 1
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGBA_RGBALPHA = 6
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGB_A = 3
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGB_ALPHAMASK = 4
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGB_A_RGBALPHA = 8
    SPRITECARD_TEXTURE_CHANNEL_MIX_RGB_RGBMASK = 5

class SpriteCardTextureType_t(Enum):
    SPRITECARD_TEXTURE_1D_COLOR_LOOKUP = 2
    SPRITECARD_TEXTURE_ANIMMOTIONVEC = 6
    SPRITECARD_TEXTURE_DEPTH = 10
    SPRITECARD_TEXTURE_DIFFUSE = 0
    SPRITECARD_TEXTURE_ILLUMINATION_GRADIENT = 11
    SPRITECARD_TEXTURE_NORMALMAP = 5
    SPRITECARD_TEXTURE_SPHERICAL_HARMONICS_A = 7
    SPRITECARD_TEXTURE_SPHERICAL_HARMONICS_B = 8
    SPRITECARD_TEXTURE_SPHERICAL_HARMONICS_C = 9
    SPRITECARD_TEXTURE_UVDISTORTION = 3
    SPRITECARD_TEXTURE_UVDISTORTION_ZOOM = 4
    SPRITECARD_TEXTURE_ZOOM = 1

class StandardLightingAttenuationStyle_t(Enum):
    LIGHT_STYLE_NEW = 1
    LIGHT_STYLE_OLD = 0

class TextureRepetitionMode_t(Enum):
    TEXTURE_REPETITION_PARTICLE = 0
    TEXTURE_REPETITION_PATH = 1

class VectorExpressionType_t(Enum):
    VECTOR_EXPRESSION_ADD = 0
    VECTOR_EXPRESSION_CROSSPRODUCT = 7
    VECTOR_EXPRESSION_DIVIDE = 3
    VECTOR_EXPRESSION_INPUT_1 = 4
    VECTOR_EXPRESSION_LERP = 8
    VECTOR_EXPRESSION_MAX = 6
    VECTOR_EXPRESSION_MIN = 5
    VECTOR_EXPRESSION_MUL = 2
    VECTOR_EXPRESSION_SUBTRACT = 1
    VECTOR_EXPRESSION_UNINITIALIZED = -1

class VectorFloatExpressionType_t(Enum):
    VECTOR_FLOAT_EXPRESSION_DISTANCE = 1
    VECTOR_FLOAT_EXPRESSION_DISTANCESQR = 2
    VECTOR_FLOAT_EXPRESSION_DOTPRODUCT = 0
    VECTOR_FLOAT_EXPRESSION_INPUT1_LENGTH = 3
    VECTOR_FLOAT_EXPRESSION_INPUT1_LENGTHSQR = 4
    VECTOR_FLOAT_EXPRESSION_INPUT1_NOISE = 5
    VECTOR_FLOAT_EXPRESSION_UNINITIALIZED = -1

class CBaseRendererSource2:
    m_bAnimateInFPS = 4000  # offset
    m_bBlendFramesSeq0 = 10676  # offset
    m_bDisableZBuffering = 8904  # offset
    m_bGammaCorrectVertexColors = 5780  # offset
    m_bMaxLuminanceBlendingSequence0 = 10677  # offset
    m_bOnlyRenderInEffecsGameOverlay = 8643  # offset
    m_bOnlyRenderInEffectsBloomPass = 8640  # offset
    m_bOnlyRenderInEffectsWaterPass = 8641  # offset
    m_bRefract = 8272  # offset
    m_bRefractSolid = 8273  # offset
    m_bReverseZBuffering = 8903  # offset
    m_bSaturateColorPreAlphaBlend = 5781  # offset
    m_bStencilTestExclude = 8772  # offset
    m_bTintByFOW = 7200  # offset
    m_bTintByGlobalLight = 7201  # offset
    m_bUseMixedResolutionRendering = 8642  # offset
    m_bWriteStencilOnDepthFail = 8902  # offset
    m_bWriteStencilOnDepthPass = 8901  # offset
    m_flAddSelfAmount = 5784  # offset
    m_flAlphaReferenceSoftness = 7216  # offset
    m_flAlphaScale = 880  # offset
    m_flAnimationRate = 3992  # offset
    m_flBumpStrength = 3968  # offset
    m_flCenterXOffset = 3264  # offset
    m_flCenterYOffset = 3616  # offset
    m_flDepthBias = 10320  # offset
    m_flDesaturation = 6136  # offset
    m_flDiffuseAmount = 5064  # offset
    m_flDiffuseClamp = 5416  # offset
    m_flFeatheringDepthMapFilter = 9968  # offset
    m_flFeatheringFilter = 9616  # offset
    m_flFeatheringMaxDist = 9264  # offset
    m_flFeatheringMinDist = 8912  # offset
    m_flFogAmount = 6848  # offset
    m_flMotionVectorScaleU = 4008  # offset
    m_flMotionVectorScaleV = 4360  # offset
    m_flOverbrightFactor = 6488  # offset
    m_flRadiusScale = 528  # offset
    m_flRefractAmount = 8280  # offset
    m_flRollScale = 1232  # offset
    m_flSelfIllumAmount = 4712  # offset
    m_flSourceAlphaValueToMapToOne = 7920  # offset
    m_flSourceAlphaValueToMapToZero = 7568  # offset
    m_nAlpha2Field = 1584  # offset
    m_nAlphaReferenceType = 7212  # offset
    m_nAnimationType = 3996  # offset
    m_nColorBlendType = 3248  # offset
    m_nCropTextureOverride = 3972  # offset
    m_nFeatheringMode = 8908  # offset
    m_nFogType = 6844  # offset
    m_nHSVShiftControlPoint = 6840  # offset
    m_nLightingControlPoint = 5768  # offset
    m_nOutputBlendMode = 5776  # offset
    m_nPerParticleAlphaRefWindow = 7208  # offset
    m_nPerParticleAlphaReference = 7204  # offset
    m_nRefractBlurRadius = 8632  # offset
    m_nRefractBlurType = 8636  # offset
    m_nSelfIllumPerParticle = 5772  # offset
    m_nShaderType = 3252  # offset
    m_nSortMethod = 10672  # offset
    m_stencilTestID = 8644  # offset
    m_stencilWriteID = 8773  # offset
    m_strShaderOverride = 3256  # offset
    m_vecColorScale = 1592  # offset
    m_vecTexturesInput = 3976  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBaseTrailRenderer:
    m_bClampV = 12008  # offset
    m_flEndFadeSize = 11656  # offset
    m_flMaxSize = 11300  # offset
    m_flMinSize = 11296  # offset
    m_flStartFadeSize = 11304  # offset
    m_nOrientationControlPoint = 11292  # offset
    m_nOrientationType = 11288  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CGeneralRandomRotation:
    m_bRandomlyFlipDirection = 476  # offset
    m_flDegrees = 460  # offset
    m_flDegreesMax = 468  # offset
    m_flDegreesMin = 464  # offset
    m_flRotationRandExponent = 472  # offset
    m_nFieldOutput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CGeneralSpin:
    m_fSpinRateStopTime = 460  # offset
    m_nSpinRateDegrees = 448  # offset
    m_nSpinRateMinDegrees = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPAssignment_t:
    m_Pos = 8  # offset
    m_nCPNumber = 0  # offset
    m_nOrientationMode = 1664  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunction:
    m_Notes = 416  # offset
    m_bDisableOperator = 414  # offset
    m_bNormalizeToStopTime = 384  # offset
    m_flOpEndFadeInTime = 368  # offset
    m_flOpEndFadeOutTime = 376  # offset
    m_flOpFadeOscillatePeriod = 380  # offset
    m_flOpStartFadeInTime = 364  # offset
    m_flOpStartFadeOutTime = 372  # offset
    m_flOpStrength = 8  # offset
    m_flOpTimeOffsetMax = 392  # offset
    m_flOpTimeOffsetMin = 388  # offset
    m_flOpTimeScaleMax = 408  # offset
    m_flOpTimeScaleMin = 404  # offset
    m_nOpEndCapState = 360  # offset
    m_nOpTimeOffsetSeed = 396  # offset
    m_nOpTimeScaleSeed = 400  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionConstraint:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionEmitter:
    m_nEmitterIndex = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionForce:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionInitializer:
    m_nAssociatedEmitterIndex = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionOperator:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionPreEmission:
    m_bRunOnce = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleFunctionRenderer:
    VisibilityInputs = 448  # offset
    m_bCannotBeRefracted = 520  # offset
    m_bSkipRenderingOnMobile = 521  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleMassCalculationParameters:
    m_flNominalRadius = 360  # offset
    m_flRadius = 8  # offset
    m_flScale = 712  # offset
    m_nMassMode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleSystemDefinition:
    m_BoundingBoxMax = 552  # offset
    m_BoundingBoxMin = 540  # offset
    m_Children = 184  # offset
    m_ConstantColor = 608  # offset
    m_ConstantNormal = 612  # offset
    m_Constraints = 136  # offset
    m_Emitters = 40  # offset
    m_ForceGenerators = 112  # offset
    m_Initializers = 64  # offset
    m_NamedValueDomain = 576  # offset
    m_NamedValueLocals = 584  # offset
    m_Operators = 88  # offset
    m_PreEmissionOperators = 16  # offset
    m_Renderers = 160  # offset
    m_bEnableNamedValues = 573  # offset
    m_bInfiniteBounds = 572  # offset
    m_bScreenSpaceEffect = 788  # offset
    m_bShouldBatch = 780  # offset
    m_bShouldHitboxesFallbackToCollisionHulls = 783  # offset
    m_bShouldHitboxesFallbackToRenderBounds = 781  # offset
    m_bShouldHitboxesFallbackToSnapshot = 782  # offset
    m_bShouldSort = 808  # offset
    m_controlPointConfigurations = 880  # offset
    m_flAggregateRadius = 776  # offset
    m_flConstantLifespan = 636  # offset
    m_flConstantRadius = 624  # offset
    m_flConstantRotation = 628  # offset
    m_flConstantRotationSpeed = 632  # offset
    m_flCullFillCost = 676  # offset
    m_flCullRadius = 672  # offset
    m_flDepthSortBias = 564  # offset
    m_flMaxCreationDistance = 768  # offset
    m_flMaxDrawDistance = 760  # offset
    m_flMaximumSimTime = 732  # offset
    m_flMaximumTimeStep = 728  # offset
    m_flMinimumSimTime = 736  # offset
    m_flMinimumTimeStep = 740  # offset
    m_flNoDrawTimeToGoToSleep = 756  # offset
    m_flPreSimulationTime = 720  # offset
    m_flStartFadeDistance = 764  # offset
    m_flStopSimulationAfterTime = 724  # offset
    m_hFallback = 688  # offset
    m_hLowViolenceDef = 704  # offset
    m_hReferenceReplacement = 712  # offset
    m_hSnapshot = 656  # offset
    m_nAggregationMinAvailableParticles = 772  # offset
    m_nAllowRenderControlPoint = 804  # offset
    m_nBehaviorVersion = 8  # offset
    m_nConstantSequenceNumber = 640  # offset
    m_nConstantSequenceNumber1 = 644  # offset
    m_nCullControlPoint = 680  # offset
    m_nFallbackMaxCount = 696  # offset
    m_nFirstMultipleOverride_BackwardCompat = 376  # offset
    m_nGroupID = 536  # offset
    m_nInitialParticles = 528  # offset
    m_nMaxParticles = 532  # offset
    m_nMinCPULevel = 748  # offset
    m_nMinGPULevel = 752  # offset
    m_nMinimumFrames = 744  # offset
    m_nSkipRenderControlPoint = 800  # offset
    m_nSnapshotControlPoint = 648  # offset
    m_nSortOverridePositionCP = 568  # offset
    m_nViewModelEffect = 784  # offset
    m_pszCullReplacementName = 664  # offset
    m_pszTargetLayerID = 792  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleVisibilityInputs:
    m_bDotCPAngles = 44  # offset
    m_bDotCameraAngles = 45  # offset
    m_bRightEye = 68  # offset
    m_flAlphaScaleMax = 52  # offset
    m_flAlphaScaleMin = 48  # offset
    m_flCameraBias = 0  # offset
    m_flDistanceInputMax = 32  # offset
    m_flDistanceInputMin = 28  # offset
    m_flDotInputMax = 40  # offset
    m_flDotInputMin = 36  # offset
    m_flInputMax = 16  # offset
    m_flInputMin = 12  # offset
    m_flInputPixelVisFade = 20  # offset
    m_flNoPixelVisibilityFallback = 24  # offset
    m_flProxyRadius = 8  # offset
    m_flRadiusScaleFOVBase = 64  # offset
    m_flRadiusScaleMax = 60  # offset
    m_flRadiusScaleMin = 56  # offset
    m_nCPin = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPathParameters:
    m_flBulge = 12  # offset
    m_flMidPoint = 16  # offset
    m_nBulgeControl = 8  # offset
    m_nEndControlPointNumber = 4  # offset
    m_nStartControlPointNumber = 0  # offset
    m_vEndOffset = 44  # offset
    m_vMidPointOffset = 32  # offset
    m_vStartPointOffset = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRandomNumberGeneratorParameters:
    m_bDistributeEvenly = 0  # offset
    m_nSeed = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CReplicationParameters:
    m_bScaleChildParticleRadii = 4  # offset
    m_flMaxRandomRadiusScale = 360  # offset
    m_flMinRandomRadiusScale = 8  # offset
    m_flModellingScale = 4024  # offset
    m_nReplicationMode = 0  # offset
    m_vMaxRandomDisplacement = 2368  # offset
    m_vMinRandomDisplacement = 712  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSpinUpdateBase:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_AddVectorToVector:
    m_nFieldInput = 472  # offset
    m_nFieldOutput = 468  # offset
    m_randomnessParameters = 500  # offset
    m_vOffsetMax = 488  # offset
    m_vOffsetMin = 476  # offset
    m_vecScale = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_AgeNoise:
    m_bAbsVal = 456  # offset
    m_bAbsValInv = 457  # offset
    m_flAgeMax = 468  # offset
    m_flAgeMin = 464  # offset
    m_flNoiseScale = 472  # offset
    m_flNoiseScaleLoc = 476  # offset
    m_flOffset = 460  # offset
    m_vecOffsetLoc = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_ChaoticAttractor:
    m_bUniformSpeed = 488  # offset
    m_flAParm = 456  # offset
    m_flBParm = 460  # offset
    m_flCParm = 464  # offset
    m_flDParm = 468  # offset
    m_flScale = 472  # offset
    m_flSpeedMax = 480  # offset
    m_flSpeedMin = 476  # offset
    m_nBaseCP = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CheckParticleForWater:
    m_flOutputRemap = 816  # offset
    m_flRadius = 456  # offset
    m_nFieldOutput = 808  # offset
    m_nSetMethod = 1168  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_ColorLitPerParticle:
    m_ColorMax = 484  # offset
    m_ColorMin = 480  # offset
    m_TintMax = 492  # offset
    m_TintMin = 488  # offset
    m_flLightAmplification = 504  # offset
    m_flTintPerc = 496  # offset
    m_nTintBlendMode = 500  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateAlongPath:
    m_PathParams = 464  # offset
    m_bSaveOffset = 544  # offset
    m_bUseRandomCPs = 528  # offset
    m_fMaxDistance = 456  # offset
    m_vEndOffset = 532  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateFromCPs:
    m_nDynamicCPCount = 472  # offset
    m_nIncrement = 456  # offset
    m_nMaxCP = 464  # offset
    m_nMinCP = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateFromParentParticles:
    m_bRandomDistribution = 464  # offset
    m_bSetRopeSegmentID = 473  # offset
    m_bSubFrame = 472  # offset
    m_flIncrement = 460  # offset
    m_flVelocityScale = 456  # offset
    m_nRandomSeed = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateFromPlaneCache:
    m_bUseNormal = 481  # offset
    m_vecOffsetMax = 468  # offset
    m_vecOffsetMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateInEpitrochoid:
    m_TransformInput = 464  # offset
    m_bOffsetExistingPos = 1978  # offset
    m_bUseCount = 1976  # offset
    m_bUseLocalCoords = 1977  # offset
    m_flOffset = 920  # offset
    m_flParticleDensity = 568  # offset
    m_flRadius1 = 1272  # offset
    m_flRadius2 = 1624  # offset
    m_nComponent1 = 456  # offset
    m_nComponent2 = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateOnGrid:
    m_bCenter = 2573  # offset
    m_bHollow = 2574  # offset
    m_bLocalSpace = 2572  # offset
    m_nControlPointNumber = 2568  # offset
    m_nXCount = 456  # offset
    m_nXSpacing = 1512  # offset
    m_nYCount = 808  # offset
    m_nYSpacing = 1864  # offset
    m_nZCount = 1160  # offset
    m_nZSpacing = 2216  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateOnModel:
    m_HitboxSetName = 4344  # offset
    m_bEvenDistribution = 661  # offset
    m_bLocalCoords = 4472  # offset
    m_bScaleToVolume = 660  # offset
    m_bUseBones = 4473  # offset
    m_bUseMesh = 4474  # offset
    m_flBoneVelocity = 2680  # offset
    m_flMaxBoneVelocity = 2684  # offset
    m_flShellSize = 4480  # offset
    m_modelInput = 456  # offset
    m_nDesiredHitbox = 664  # offset
    m_nForceInModel = 656  # offset
    m_nHitboxValueFromControlPointIndex = 1016  # offset
    m_transformInput = 552  # offset
    m_vecDirectionBias = 2688  # offset
    m_vecHitBoxScale = 1024  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateOnModelAtHeight:
    m_HitboxSetName = 4142  # offset
    m_bForceZ = 457  # offset
    m_bLocalCoords = 4140  # offset
    m_bPreferMovingBoxes = 4141  # offset
    m_bUseBones = 456  # offset
    m_bUseWaterHeight = 468  # offset
    m_flDesiredHeight = 472  # offset
    m_flHitboxVelocityScale = 4272  # offset
    m_flMaxBoneVelocity = 4624  # offset
    m_nBiasType = 4136  # offset
    m_nControlPointNumber = 460  # offset
    m_nHeightCP = 464  # offset
    m_vecDirectionBias = 2480  # offset
    m_vecHitBoxScale = 824  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateParticleImpulse:
    m_InputFalloffExp = 1168  # offset
    m_InputMagnitude = 808  # offset
    m_InputRadius = 456  # offset
    m_nFalloffFunction = 1160  # offset
    m_nImpulseType = 1520  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreatePhyllotaxis:
    m_bUseLocalCoords = 500  # offset
    m_bUseOrigRadius = 502  # offset
    m_bUseWithContEmit = 501  # offset
    m_fDistBias = 496  # offset
    m_fMinRad = 492  # offset
    m_fRadBias = 488  # offset
    m_fRadCentCore = 468  # offset
    m_fRadPerPoint = 472  # offset
    m_fRadPerPointTo = 476  # offset
    m_fpointAngle = 480  # offset
    m_fsizeOverall = 484  # offset
    m_nComponent = 464  # offset
    m_nControlPointNumber = 456  # offset
    m_nScaleCP = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateSequentialPath:
    m_PathParams = 480  # offset
    m_bCPPairs = 465  # offset
    m_bLoop = 464  # offset
    m_bSaveOffset = 466  # offset
    m_fMaxDistance = 456  # offset
    m_flNumToAssign = 460  # offset

    __metadata__ =     [
        {
            "name": "MParticleMaxVersion",
            "type": "Unknown"
        },
        {
            "name": "MParticleReplacementOp",
            "type": "Unknown"
        },
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateSequentialPathV2:
    m_PathParams = 1168  # offset
    m_bCPPairs = 1161  # offset
    m_bLoop = 1160  # offset
    m_bSaveOffset = 1162  # offset
    m_fMaxDistance = 456  # offset
    m_flNumToAssign = 808  # offset

    __metadata__ =     [
        {
            "name": "MParticleMinVersion",
            "type": "Unknown"
        },
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateSpiralSphere:
    m_bUseParticleCount = 480  # offset
    m_flInitialRadius = 468  # offset
    m_flInitialSpeedMax = 476  # offset
    m_flInitialSpeedMin = 472  # offset
    m_nControlPointNumber = 456  # offset
    m_nDensity = 464  # offset
    m_nOverrideCP = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateWithinBox:
    m_bLocalSpace = 3772  # offset
    m_bUseNewCode = 3784  # offset
    m_nControlPointNumber = 3768  # offset
    m_randomnessParameters = 3776  # offset
    m_vecMax = 2112  # offset
    m_vecMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateWithinCapsuleTransform:
    m_LocalCoordinateSystemSpeedMax = 3984  # offset
    m_LocalCoordinateSystemSpeedMin = 2328  # offset
    m_TransformInput = 1512  # offset
    m_fHeight = 1160  # offset
    m_fRadiusMax = 808  # offset
    m_fRadiusMin = 456  # offset
    m_fSpeedMax = 1968  # offset
    m_fSpeedMin = 1616  # offset
    m_fSpeedRandExp = 2320  # offset
    m_nFieldOutput = 5640  # offset
    m_nFieldVelocity = 5644  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreateWithinSphereTransform:
    m_LocalCoordinateSystemSpeedMax = 5304  # offset
    m_LocalCoordinateSystemSpeedMin = 3648  # offset
    m_TransformInput = 2832  # offset
    m_bLocalCoords = 3644  # offset
    m_fRadiusMax = 808  # offset
    m_fRadiusMin = 456  # offset
    m_fSpeedMax = 3288  # offset
    m_fSpeedMin = 2936  # offset
    m_fSpeedRandExp = 3640  # offset
    m_nFieldOutput = 6960  # offset
    m_nFieldVelocity = 6964  # offset
    m_vecDistanceBias = 1160  # offset
    m_vecDistanceBiasAbs = 2816  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_CreationNoise:
    m_bAbsVal = 460  # offset
    m_bAbsValInv = 461  # offset
    m_flNoiseScale = 476  # offset
    m_flNoiseScaleLoc = 480  # offset
    m_flOffset = 464  # offset
    m_flOutputMax = 472  # offset
    m_flOutputMin = 468  # offset
    m_flWorldTimeScale = 496  # offset
    m_nFieldOutput = 456  # offset
    m_vecOffsetLoc = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_DistanceCull:
    m_bCullInside = 816  # offset
    m_flDistance = 464  # offset
    m_nControlPoint = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_DistanceToCPInit:
    m_CollisionGroupName = 1877  # offset
    m_bActiveRange = 2376  # offset
    m_bLOS = 1876  # offset
    m_flInputMax = 816  # offset
    m_flInputMin = 464  # offset
    m_flLOSScale = 2368  # offset
    m_flMaxTraceLength = 2016  # offset
    m_flOutputMax = 1520  # offset
    m_flOutputMin = 1168  # offset
    m_flRemapBias = 2392  # offset
    m_nFieldOutput = 456  # offset
    m_nSetMethod = 2372  # offset
    m_nStartCP = 1872  # offset
    m_nTraceSet = 2008  # offset
    m_vecDistanceScale = 2380  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_DistanceToNeighborCull:
    m_bIncludeRadii = 808  # offset
    m_bUseNeighbor = 1532  # offset
    m_flDistance = 456  # offset
    m_flLifespanOverlap = 816  # offset
    m_flModify = 1176  # offset
    m_nFieldModify = 1168  # offset
    m_nSetMethod = 1528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_GlobalScale:
    m_bScalePosition = 469  # offset
    m_bScaleRadius = 468  # offset
    m_bScaleVelocity = 470  # offset
    m_flScale = 456  # offset
    m_nControlPointNumber = 464  # offset
    m_nScaleControlPointNumber = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InheritFromParentParticles:
    m_bRandomDistribution = 468  # offset
    m_flScale = 456  # offset
    m_nFieldOutput = 460  # offset
    m_nIncrement = 464  # offset
    m_nRandomSeed = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InheritVelocity:
    m_flVelocityScale = 460  # offset
    m_nControlPointNumber = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitFloat:
    m_InputStrength = 816  # offset
    m_InputValue = 456  # offset
    m_nOutputField = 808  # offset
    m_nSetMethod = 812  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitFloatCollection:
    m_InputValue = 456  # offset
    m_nOutputField = 808  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitFromCPSnapshot:
    m_bLocalSpaceAngles = 1196  # offset
    m_bRandom = 484  # offset
    m_bReverse = 485  # offset
    m_nAttributeToRead = 472  # offset
    m_nAttributeToWrite = 476  # offset
    m_nControlPointNumber = 456  # offset
    m_nLocalSpaceCP = 480  # offset
    m_nManualSnapshotIndex = 840  # offset
    m_nRandomSeed = 1192  # offset
    m_nSnapShotIncrement = 488  # offset
    m_strSnapshotSubset = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitFromParentKilled:
    m_nAttributeToCopy = 456  # offset
    m_nEventType = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitFromVectorFieldSnapshot:
    m_bUseVerticalVelocity = 468  # offset
    m_nControlPointNumber = 456  # offset
    m_nLocalSpaceCP = 460  # offset
    m_nWeightUpdateCP = 464  # offset
    m_vecScale = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitSkinnedPositionFromCPSnapshot:
    m_bCopyAlpha = 861  # offset
    m_bCopyColor = 860  # offset
    m_bIgnoreDt = 474  # offset
    m_bRandom = 464  # offset
    m_bRigid = 472  # offset
    m_bSetNormal = 473  # offset
    m_bSetRadius = 862  # offset
    m_flBoneVelocity = 852  # offset
    m_flBoneVelocityMax = 856  # offset
    m_flIncrement = 840  # offset
    m_flMaxNormalVelocity = 480  # offset
    m_flMinNormalVelocity = 476  # offset
    m_flReadIndex = 488  # offset
    m_nControlPointNumber = 460  # offset
    m_nFullLoopIncrement = 844  # offset
    m_nIndexType = 484  # offset
    m_nRandomSeed = 468  # offset
    m_nSnapShotStartPoint = 848  # offset
    m_nSnapshotControlPointNumber = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitVec:
    m_InputValue = 456  # offset
    m_bNormalizedOutput = 2120  # offset
    m_bWritePreviousPosition = 2121  # offset
    m_nOutputField = 2112  # offset
    m_nSetMethod = 2116  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitVecCollection:
    m_InputValue = 456  # offset
    m_nOutputField = 2112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitialRepulsionVelocity:
    m_CollisionGroupName = 456  # offset
    m_bInherit = 625  # offset
    m_bPerParticle = 616  # offset
    m_bPerParticleTR = 624  # offset
    m_bProportional = 618  # offset
    m_bTranslate = 617  # offset
    m_flTraceLength = 620  # offset
    m_nChildCP = 628  # offset
    m_nChildGroupID = 632  # offset
    m_nControlPointNumber = 612  # offset
    m_nTraceSet = 584  # offset
    m_vecOutputMax = 600  # offset
    m_vecOutputMin = 588  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitialSequenceFromModel:
    m_flInputMax = 472  # offset
    m_flInputMin = 468  # offset
    m_flOutputMax = 480  # offset
    m_flOutputMin = 476  # offset
    m_nControlPointNumber = 456  # offset
    m_nFieldOutput = 460  # offset
    m_nFieldOutputAnim = 464  # offset
    m_nSetMethod = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitialVelocityFromHitbox:
    m_HitboxSetName = 468  # offset
    m_bUseBones = 596  # offset
    m_flVelocityMax = 460  # offset
    m_flVelocityMin = 456  # offset
    m_nControlPointNumber = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_InitialVelocityNoise:
    m_TransformInput = 6504  # offset
    m_bIgnoreDt = 6608  # offset
    m_flNoiseScale = 5800  # offset
    m_flNoiseScaleLoc = 6152  # offset
    m_flOffset = 2136  # offset
    m_vecAbsVal = 456  # offset
    m_vecAbsValInv = 468  # offset
    m_vecOffsetLoc = 480  # offset
    m_vecOutputMax = 4144  # offset
    m_vecOutputMin = 2488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_LifespanFromVelocity:
    m_CollisionGroupName = 488  # offset
    m_bIncludeWater = 632  # offset
    m_flMaxTraceLength = 472  # offset
    m_flTraceOffset = 468  # offset
    m_flTraceTolerance = 476  # offset
    m_nMaxPlanes = 480  # offset
    m_nTraceSet = 616  # offset
    m_vecComponentScale = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_ModelCull:
    m_HitboxSetName = 463  # offset
    m_bBoundBox = 460  # offset
    m_bCullOutside = 461  # offset
    m_bUseBones = 462  # offset
    m_nControlPointNumber = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_MoveBetweenPoints:
    m_bTrailBias = 2220  # offset
    m_flEndOffset = 1864  # offset
    m_flEndSpread = 1160  # offset
    m_flSpeedMax = 808  # offset
    m_flSpeedMin = 456  # offset
    m_flStartOffset = 1512  # offset
    m_nEndControlPointNumber = 2216  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_NormalAlignToCP:
    m_nControlPointAxis = 560  # offset
    m_transformInput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_NormalOffset:
    m_OffsetMax = 468  # offset
    m_OffsetMin = 456  # offset
    m_bLocalCoords = 484  # offset
    m_bNormalize = 485  # offset
    m_nControlPointNumber = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_OffsetVectorToVector:
    m_nFieldInput = 456  # offset
    m_nFieldOutput = 460  # offset
    m_randomnessParameters = 488  # offset
    m_vecOutputMax = 476  # offset
    m_vecOutputMin = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_Orient2DRelToCP:
    m_flRotOffset = 464  # offset
    m_nCP = 456  # offset
    m_nFieldOutput = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PlaneCull:
    m_bCullInside = 816  # offset
    m_flDistance = 464  # offset
    m_nControlPoint = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PointList:
    m_bClosedLoop = 489  # offset
    m_bPlaceAlongPath = 488  # offset
    m_nFieldOutput = 456  # offset
    m_nNumPointsAlongPath = 492  # offset
    m_pointList = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PositionOffset:
    m_OffsetMax = 2112  # offset
    m_OffsetMin = 456  # offset
    m_TransformInput = 3768  # offset
    m_bLocalCoords = 3872  # offset
    m_bProportional = 3873  # offset
    m_randomnessParameters = 3876  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PositionOffsetToCP:
    m_bLocalCoords = 464  # offset
    m_nControlPointNumberEnd = 460  # offset
    m_nControlPointNumberStart = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PositionPlaceOnGround:
    m_CollisionGroupName = 1160  # offset
    m_bIncludeWater = 1308  # offset
    m_bOffsetonColOnly = 1324  # offset
    m_bSetNormal = 1309  # offset
    m_bSetPXYZOnly = 1316  # offset
    m_bTraceAlongNormal = 1317  # offset
    m_flMaxTraceLength = 808  # offset
    m_flOffset = 456  # offset
    m_flOffsetByRadiusFactor = 1328  # offset
    m_nAttribute = 1312  # offset
    m_nIgnoreCP = 1336  # offset
    m_nPreserveOffsetCP = 1332  # offset
    m_nTraceDirectionAttribute = 1320  # offset
    m_nTraceMissBehavior = 1304  # offset
    m_nTraceSet = 1288  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PositionWarp:
    m_bInvertWarp = 3792  # offset
    m_bUseCount = 3793  # offset
    m_flPrevPosScale = 3788  # offset
    m_flWarpStartTime = 3784  # offset
    m_flWarpTime = 3780  # offset
    m_nControlPointNumber = 3772  # offset
    m_nRadiusComponent = 3776  # offset
    m_nScaleControlPointNumber = 3768  # offset
    m_vecWarpMax = 2112  # offset
    m_vecWarpMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_PositionWarpScalar:
    m_InputValue = 480  # offset
    m_flPrevPosScale = 832  # offset
    m_nControlPointNumber = 840  # offset
    m_nScaleControlPointNumber = 836  # offset
    m_vecWarpMax = 468  # offset
    m_vecWarpMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_QuantizeFloat:
    m_InputValue = 456  # offset
    m_nOutputField = 808  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RadiusFromCPObject:
    m_nControlPoint = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomAlpha:
    m_flAlphaRandExponent = 476  # offset
    m_nAlphaMax = 464  # offset
    m_nAlphaMin = 460  # offset
    m_nFieldOutput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomAlphaWindowThreshold:
    m_flExponent = 464  # offset
    m_flMax = 460  # offset
    m_flMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomColor:
    m_ColorMax = 488  # offset
    m_ColorMin = 484  # offset
    m_TintMax = 496  # offset
    m_TintMin = 492  # offset
    m_flLightAmplification = 520  # offset
    m_flTintPerc = 500  # offset
    m_flUpdateThreshold = 504  # offset
    m_nFieldOutput = 512  # offset
    m_nTintBlendMode = 516  # offset
    m_nTintCP = 508  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomLifeTime:
    m_fLifetimeMax = 460  # offset
    m_fLifetimeMin = 456  # offset
    m_fLifetimeRandExponent = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomModelSequence:
    m_ActivityName = 456  # offset
    m_SequenceName = 712  # offset
    m_hModel = 968  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomNamedModelBodyPart:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomNamedModelElement:
    m_bLinear = 489  # offset
    m_bModelFromRenderer = 490  # offset
    m_bShuffle = 488  # offset
    m_hModel = 456  # offset
    m_nFieldOutput = 492  # offset
    m_names = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomNamedModelMeshGroup:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomNamedModelSequence:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomRadius:
    m_flRadiusMax = 460  # offset
    m_flRadiusMin = 456  # offset
    m_flRadiusRandExponent = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomRotation:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomRotationSpeed:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomScalar:
    m_flExponent = 464  # offset
    m_flMax = 460  # offset
    m_flMin = 456  # offset
    m_nFieldOutput = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomSecondSequence:
    m_nSequenceMax = 460  # offset
    m_nSequenceMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomSequence:
    m_WeightedList = 472  # offset
    m_bLinear = 465  # offset
    m_bShuffle = 464  # offset
    m_nSequenceMax = 460  # offset
    m_nSequenceMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomTrailLength:
    m_flLengthRandExponent = 464  # offset
    m_flMaxLength = 460  # offset
    m_flMinLength = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomVector:
    m_nFieldOutput = 480  # offset
    m_randomnessParameters = 484  # offset
    m_vecMax = 468  # offset
    m_vecMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomVectorComponent:
    m_flMax = 460  # offset
    m_flMin = 456  # offset
    m_nComponent = 468  # offset
    m_nFieldOutput = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomYaw:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RandomYawFlip:
    m_flPercent = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapCPtoScalar:
    m_flEndTime = 488  # offset
    m_flInputMax = 472  # offset
    m_flInputMin = 468  # offset
    m_flOutputMax = 480  # offset
    m_flOutputMin = 476  # offset
    m_flRemapBias = 496  # offset
    m_flStartTime = 484  # offset
    m_nCPInput = 456  # offset
    m_nField = 464  # offset
    m_nFieldOutput = 460  # offset
    m_nSetMethod = 492  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapInitialDirectionToTransformToVector:
    m_TransformInput = 456  # offset
    m_bNormalize = 584  # offset
    m_flOffsetRot = 568  # offset
    m_flScale = 564  # offset
    m_nFieldOutput = 560  # offset
    m_vecOffsetAxis = 572  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapInitialTransformDirectionToRotation:
    m_TransformInput = 456  # offset
    m_flOffsetRot = 564  # offset
    m_nComponent = 568  # offset
    m_nFieldOutput = 560  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapInitialVisibilityScalar:
    m_flInputMax = 468  # offset
    m_flInputMin = 464  # offset
    m_flOutputMax = 476  # offset
    m_flOutputMin = 472  # offset
    m_nFieldOutput = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapNamedModelBodyPartToScalar:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapNamedModelElementToScalar:
    m_bModelFromRenderer = 524  # offset
    m_hModel = 456  # offset
    m_nFieldInput = 512  # offset
    m_nFieldOutput = 516  # offset
    m_nSetMethod = 520  # offset
    m_names = 464  # offset
    m_values = 488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapNamedModelMeshGroupToScalar:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapNamedModelSequenceToScalar:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapParticleCountToNamedModelBodyPartScalar:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapParticleCountToNamedModelElementScalar:
    m_bModelFromRenderer = 528  # offset
    m_hModel = 504  # offset
    m_outputMaxName = 520  # offset
    m_outputMinName = 512  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapParticleCountToNamedModelMeshGroupScalar:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapParticleCountToNamedModelSequenceScalar:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapParticleCountToScalar:
    m_bActiveRange = 488  # offset
    m_bInvert = 489  # offset
    m_bWrap = 490  # offset
    m_flOutputMax = 480  # offset
    m_flOutputMin = 476  # offset
    m_flRemapBias = 492  # offset
    m_nFieldOutput = 456  # offset
    m_nInputMax = 464  # offset
    m_nInputMin = 460  # offset
    m_nScaleControlPoint = 468  # offset
    m_nScaleControlPointField = 472  # offset
    m_nSetMethod = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapQAnglesToRotation:
    m_TransformInput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapScalar:
    m_bActiveRange = 492  # offset
    m_flEndTime = 484  # offset
    m_flInputMax = 468  # offset
    m_flInputMin = 464  # offset
    m_flOutputMax = 476  # offset
    m_flOutputMin = 472  # offset
    m_flRemapBias = 496  # offset
    m_flStartTime = 480  # offset
    m_nFieldInput = 456  # offset
    m_nFieldOutput = 460  # offset
    m_nSetMethod = 488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapScalarToVector:
    m_bLocalCoords = 512  # offset
    m_flEndTime = 500  # offset
    m_flInputMax = 468  # offset
    m_flInputMin = 464  # offset
    m_flRemapBias = 516  # offset
    m_flStartTime = 496  # offset
    m_nControlPointNumber = 508  # offset
    m_nFieldInput = 456  # offset
    m_nFieldOutput = 460  # offset
    m_nSetMethod = 504  # offset
    m_vecOutputMax = 484  # offset
    m_vecOutputMin = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapSpeedToScalar:
    m_bPerParticle = 492  # offset
    m_flEndTime = 468  # offset
    m_flInputMax = 476  # offset
    m_flInputMin = 472  # offset
    m_flOutputMax = 484  # offset
    m_flOutputMin = 480  # offset
    m_flStartTime = 464  # offset
    m_nControlPointNumber = 460  # offset
    m_nFieldOutput = 456  # offset
    m_nSetMethod = 488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapTransformOrientationToRotations:
    m_TransformInput = 456  # offset
    m_bUseQuat = 572  # offset
    m_bWriteNormal = 573  # offset
    m_vecRotation = 560  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RemapTransformToVector:
    m_LocalSpaceTransform = 616  # offset
    m_TransformInput = 512  # offset
    m_bAccelerate = 733  # offset
    m_bOffset = 732  # offset
    m_flEndTime = 724  # offset
    m_flRemapBias = 736  # offset
    m_flStartTime = 720  # offset
    m_nFieldOutput = 456  # offset
    m_nSetMethod = 728  # offset
    m_vInputMax = 472  # offset
    m_vInputMin = 460  # offset
    m_vOutputMax = 496  # offset
    m_vOutputMin = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RingWave:
    m_TransformInput = 456  # offset
    m_bEvenDistribution = 3376  # offset
    m_bXYVelocityOnly = 3377  # offset
    m_flInitialRadius = 912  # offset
    m_flInitialSpeedMax = 1968  # offset
    m_flInitialSpeedMin = 1616  # offset
    m_flParticlesPerOrbit = 560  # offset
    m_flPitch = 2672  # offset
    m_flRoll = 2320  # offset
    m_flThickness = 1264  # offset
    m_flYaw = 3024  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_RtEnvCull:
    m_RtEnvName = 483  # offset
    m_bCullOnMiss = 481  # offset
    m_bLifeAdjust = 482  # offset
    m_bUseVelocity = 480  # offset
    m_nComponent = 616  # offset
    m_nRTEnvCP = 612  # offset
    m_vecTestDir = 456  # offset
    m_vecTestNormal = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_ScaleVelocity:
    m_vecScale = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_ScreenSpacePositionOfTarget:
    m_bOututBehindness = 2112  # offset
    m_flBehindOutputRemap = 2120  # offset
    m_nBehindFieldOutput = 2116  # offset
    m_vecTargetPosition = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SequenceFromCP:
    m_bKillUnused = 456  # offset
    m_bRadiusScale = 457  # offset
    m_nCP = 460  # offset
    m_vecOffset = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SequenceLifeTime:
    m_flFramerate = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SetAttributeToScalarExpression:
    m_flInput1 = 464  # offset
    m_flInput2 = 816  # offset
    m_flOutputRemap = 1168  # offset
    m_nExpression = 456  # offset
    m_nOutputField = 1520  # offset
    m_nSetMethod = 1524  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SetFloatAttributeToVectorExpression:
    m_flOutputRemap = 3776  # offset
    m_nExpression = 456  # offset
    m_nOutputField = 4128  # offset
    m_nSetMethod = 4132  # offset
    m_vInput1 = 464  # offset
    m_vInput2 = 2120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SetHitboxToClosest:
    m_HitboxSetName = 2120  # offset
    m_bUpdatePosition = 2608  # offset
    m_bUseBones = 2248  # offset
    m_bUseClosestPointOnHitbox = 2249  # offset
    m_flHybridRatio = 2256  # offset
    m_nControlPointNumber = 456  # offset
    m_nDesiredHitbox = 460  # offset
    m_nTestType = 2252  # offset
    m_vecHitBoxScale = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SetHitboxToModel:
    m_HitboxSetName = 2142  # offset
    m_bEvenDistribution = 464  # offset
    m_bMaintainHitbox = 2140  # offset
    m_bUseBones = 2141  # offset
    m_flShellSize = 2272  # offset
    m_nControlPointNumber = 456  # offset
    m_nDesiredHitbox = 468  # offset
    m_nForceInModel = 460  # offset
    m_vecDirectionBias = 2128  # offset
    m_vecHitBoxScale = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SetRigidAttachment:
    m_bLocalSpace = 468  # offset
    m_nControlPointNumber = 456  # offset
    m_nFieldInput = 460  # offset
    m_nFieldOutput = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_SetVectorAttributeToVectorExpression:
    m_bNormalizedOutput = 4136  # offset
    m_flLerp = 3776  # offset
    m_nExpression = 456  # offset
    m_nOutputField = 4128  # offset
    m_nSetMethod = 4132  # offset
    m_vInput1 = 464  # offset
    m_vInput2 = 2120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_StatusEffect:
    m_flAmbientScale = 484  # offset
    m_flColorWarpIntensity = 472  # offset
    m_flDetail2BlendFactor = 468  # offset
    m_flDetail2Rotation = 460  # offset
    m_flDetail2Scale = 464  # offset
    m_flDiffuseWarpBlendToFull = 476  # offset
    m_flEnvMapIntensity = 480  # offset
    m_flMetalnessBlendToFull = 520  # offset
    m_flReflectionsTintByBaseBlendToNone = 516  # offset
    m_flRimLightScale = 512  # offset
    m_flSelfIllumBlendToFull = 524  # offset
    m_flSpecularBlendToFull = 504  # offset
    m_flSpecularExponent = 496  # offset
    m_flSpecularExponentBlendToFull = 500  # offset
    m_flSpecularScale = 492  # offset
    m_nDetail2Combo = 456  # offset
    m_rimLightColor = 508  # offset
    m_specularColor = 488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_StatusEffectCitadel:
    m_flSFXColorWarpAmount = 456  # offset
    m_flSFXMetalnessAmount = 464  # offset
    m_flSFXNormalAmount = 460  # offset
    m_flSFXRoughnessAmount = 468  # offset
    m_flSFXSDetailAmount = 508  # offset
    m_flSFXSDetailScale = 512  # offset
    m_flSFXSDetailScrollX = 516  # offset
    m_flSFXSDetailScrollY = 520  # offset
    m_flSFXSDetailScrollZ = 524  # offset
    m_flSFXSOffsetX = 492  # offset
    m_flSFXSOffsetY = 496  # offset
    m_flSFXSOffsetZ = 500  # offset
    m_flSFXSScale = 476  # offset
    m_flSFXSScrollX = 480  # offset
    m_flSFXSScrollY = 484  # offset
    m_flSFXSScrollZ = 488  # offset
    m_flSFXSUseModelUVs = 528  # offset
    m_flSFXSelfIllumAmount = 472  # offset
    m_nDetailCombo = 504  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_VelocityFromCP:
    m_bDirectionOnly = 2220  # offset
    m_flVelocityScale = 2216  # offset
    m_transformInput = 2112  # offset
    m_velocityInput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_VelocityFromNormal:
    m_bIgnoreDt = 464  # offset
    m_fSpeedMax = 460  # offset
    m_fSpeedMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_VelocityRadialRandom:
    m_bIgnoreDelta = 1181  # offset
    m_fSpeedMax = 816  # offset
    m_fSpeedMin = 464  # offset
    m_nControlPointNumber = 456  # offset
    m_vecLocalCoordinateSystemSpeedScale = 1168  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_INIT_VelocityRandom:
    m_LocalCoordinateSystemSpeedMax = 2824  # offset
    m_LocalCoordinateSystemSpeedMin = 1168  # offset
    m_bIgnoreDT = 4480  # offset
    m_fSpeedMax = 816  # offset
    m_fSpeedMin = 464  # offset
    m_nControlPointNumber = 456  # offset
    m_randomnessParameters = 4484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_AlphaDecay:
    m_flMinAlpha = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_AttractToControlPoint:
    m_TransformInput = 840  # offset
    m_bApplyMinForce = 1296  # offset
    m_fFalloffPower = 832  # offset
    m_fForceAmount = 480  # offset
    m_fForceAmountMin = 944  # offset
    m_vecComponentScale = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_BasicMovement:
    m_Gravity = 448  # offset
    m_bUseNewCode = 3524  # offset
    m_fDrag = 2104  # offset
    m_massControls = 2456  # offset
    m_nMaxConstraintPasses = 3520  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_BoxConstraint:
    m_bAccountForRadius = 3765  # offset
    m_bLocalSpace = 3764  # offset
    m_nCP = 3760  # offset
    m_vecMax = 2104  # offset
    m_vecMin = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CPOffsetToPercentageBetweenCPs:
    m_bRadialCheck = 480  # offset
    m_bScaleOffset = 481  # offset
    m_flInputBias = 456  # offset
    m_flInputMax = 452  # offset
    m_flInputMin = 448  # offset
    m_nEndCP = 464  # offset
    m_nInputCP = 476  # offset
    m_nOffsetCP = 468  # offset
    m_nOuputCP = 472  # offset
    m_nStartCP = 460  # offset
    m_vecOffset = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CPVelocityForce:
    m_flScale = 472  # offset
    m_nControlPointNumber = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CalculateVectorAttribute:
    m_flControlPointScale1 = 496  # offset
    m_flControlPointScale2 = 520  # offset
    m_flInputScale1 = 464  # offset
    m_flInputScale2 = 472  # offset
    m_nControlPointInput1 = 476  # offset
    m_nControlPointInput2 = 500  # offset
    m_nFieldInput1 = 460  # offset
    m_nFieldInput2 = 468  # offset
    m_nFieldOutput = 524  # offset
    m_vFinalOutputScale = 528  # offset
    m_vStartValue = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Callback:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ChladniWave:
    m_b3D = 5184  # offset
    m_flInputMax = 808  # offset
    m_flInputMin = 456  # offset
    m_flOutputMax = 1512  # offset
    m_flOutputMin = 1160  # offset
    m_nFieldOutput = 448  # offset
    m_nLocalSpaceControlPoint = 5180  # offset
    m_nSetMethod = 5176  # offset
    m_vecHarmonics = 3520  # offset
    m_vecWaveLength = 1864  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ChooseRandomChildrenInGroup:
    m_flNumberOfChildren = 464  # offset
    m_nChildGroupID = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ClampScalar:
    m_flOutputMax = 808  # offset
    m_flOutputMin = 456  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ClampVector:
    m_nFieldOutput = 448  # offset
    m_vecOutputMax = 2112  # offset
    m_vecOutputMin = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ClientPhysics:
    m_bDeleteSim = 1258  # offset
    m_bKillParticles = 1257  # offset
    m_bRespectExclusionVolumes = 1256  # offset
    m_bStartAsleep = 536  # offset
    m_bUseHighQualitySimulation = 1248  # offset
    m_flPlayerWakeRadius = 544  # offset
    m_flVehicleWakeRadius = 896  # offset
    m_nColorBlendType = 1268  # offset
    m_nControlPoint = 1260  # offset
    m_nForcedSimId = 1264  # offset
    m_nForcedStatusEffects = 1272  # offset
    m_nMaxParticleCount = 1252  # offset
    m_strPhysicsType = 528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CollideWithParentParticles:
    m_flParentRadiusScale = 448  # offset
    m_flRadiusScale = 800  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CollideWithSelf:
    m_flMinimumSpeed = 800  # offset
    m_flRadiusScale = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ColorAdjustHSL:
    m_flHueAdjust = 448  # offset
    m_flLightnessAdjust = 1152  # offset
    m_flSaturationAdjust = 800  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ColorInterpolate:
    m_ColorFade = 448  # offset
    m_bEaseInOut = 476  # offset
    m_flFadeEndTime = 468  # offset
    m_flFadeStartTime = 464  # offset
    m_nFieldOutput = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ColorInterpolateRandom:
    m_ColorFadeMax = 476  # offset
    m_ColorFadeMin = 448  # offset
    m_bEaseInOut = 504  # offset
    m_flFadeEndTime = 496  # offset
    m_flFadeStartTime = 492  # offset
    m_nFieldOutput = 500  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ConnectParentParticleToNearest:
    m_bUseRadius = 456  # offset
    m_flParentRadiusScale = 816  # offset
    m_flRadiusScale = 464  # offset
    m_nFirstControlPoint = 448  # offset
    m_nSecondControlPoint = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ConstrainDistance:
    m_CenterOffset = 1156  # offset
    m_bGlobalCenter = 1168  # offset
    m_fMaxDistance = 800  # offset
    m_fMinDistance = 448  # offset
    m_nControlPointNumber = 1152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ConstrainDistanceToPath:
    m_PathParameters = 464  # offset
    m_fMinDistance = 448  # offset
    m_flMaxDistance0 = 452  # offset
    m_flMaxDistance1 = 460  # offset
    m_flMaxDistanceMid = 456  # offset
    m_flTravelTime = 528  # offset
    m_nFieldScale = 532  # offset
    m_nManualTField = 536  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ConstrainDistanceToUserSpecifiedPath:
    m_bLoopedPath = 460  # offset
    m_fMinDistance = 448  # offset
    m_flMaxDistance = 452  # offset
    m_flTimeScale = 456  # offset
    m_pointList = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ConstrainLineLength:
    m_flMaxDistance = 452  # offset
    m_flMinDistance = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ContinuousEmitter:
    m_bForceEmitOnFirstUpdate = 1548  # offset
    m_bForceEmitOnLastUpdate = 1549  # offset
    m_bInitFromKilledParentParticles = 1520  # offset
    m_flEmissionDuration = 456  # offset
    m_flEmissionScale = 1512  # offset
    m_flEmitRate = 1160  # offset
    m_flScalePerParentParticle = 1516  # offset
    m_flStartTime = 808  # offset
    m_nEventType = 1524  # offset
    m_nLimitPerUpdate = 1544  # offset
    m_nSnapshotControlPoint = 1528  # offset
    m_strSnapshotSubset = 1536  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ControlPointToRadialScreenSpace:
    m_nCPIn = 456  # offset
    m_nCPOut = 472  # offset
    m_nCPOutField = 476  # offset
    m_nCPSSPosOut = 480  # offset
    m_vecCP1Pos = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ControlpointLight:
    m_LightColor1 = 1712  # offset
    m_LightColor2 = 1716  # offset
    m_LightColor3 = 1720  # offset
    m_LightColor4 = 1724  # offset
    m_LightFiftyDist1 = 1680  # offset
    m_LightFiftyDist2 = 1688  # offset
    m_LightFiftyDist3 = 1696  # offset
    m_LightFiftyDist4 = 1704  # offset
    m_LightZeroDist1 = 1684  # offset
    m_LightZeroDist2 = 1692  # offset
    m_LightZeroDist3 = 1700  # offset
    m_LightZeroDist4 = 1708  # offset
    m_bClampLowerRange = 1742  # offset
    m_bClampUpperRange = 1743  # offset
    m_bLightDynamic1 = 1732  # offset
    m_bLightDynamic2 = 1733  # offset
    m_bLightDynamic3 = 1734  # offset
    m_bLightDynamic4 = 1735  # offset
    m_bLightType1 = 1728  # offset
    m_bLightType2 = 1729  # offset
    m_bLightType3 = 1730  # offset
    m_bLightType4 = 1731  # offset
    m_bUseHLambert = 1737  # offset
    m_bUseNormal = 1736  # offset
    m_flScale = 448  # offset
    m_nControlPoint1 = 1616  # offset
    m_nControlPoint2 = 1620  # offset
    m_nControlPoint3 = 1624  # offset
    m_nControlPoint4 = 1628  # offset
    m_vecCPOffset1 = 1632  # offset
    m_vecCPOffset2 = 1644  # offset
    m_vecCPOffset3 = 1656  # offset
    m_vecCPOffset4 = 1668  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CreateParticleSystemRenderer:
    m_AggregationPos = 568  # offset
    m_hEffect = 528  # offset
    m_nEventType = 536  # offset
    m_szParticleConfig = 560  # offset
    m_vecCPs = 544  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Cull:
    m_flCullEnd = 456  # offset
    m_flCullExp = 460  # offset
    m_flCullPerc = 448  # offset
    m_flCullStart = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CurlNoiseForce:
    m_flWorleyJitter = 7448  # offset
    m_flWorleySeed = 7096  # offset
    m_nNoiseType = 464  # offset
    m_vecNoiseFreq = 472  # offset
    m_vecNoiseScale = 2128  # offset
    m_vecOffset = 3784  # offset
    m_vecOffsetRate = 5440  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CycleScalar:
    m_bDoNotRepeatCycle = 464  # offset
    m_bSynchronizeParticles = 465  # offset
    m_flCycleTime = 460  # offset
    m_flEndValue = 456  # offset
    m_flStartValue = 452  # offset
    m_nCPFieldMax = 476  # offset
    m_nCPFieldMin = 472  # offset
    m_nCPScale = 468  # offset
    m_nDestField = 448  # offset
    m_nSetMethod = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_CylindricalDistanceToTransform:
    m_TransformEnd = 1968  # offset
    m_TransformStart = 1864  # offset
    m_bActiveRange = 2076  # offset
    m_bAdditive = 2077  # offset
    m_bCapsule = 2078  # offset
    m_flInputMax = 808  # offset
    m_flInputMin = 456  # offset
    m_flOutputMax = 1512  # offset
    m_flOutputMin = 1160  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 2072  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DampenToCP:
    m_flRange = 452  # offset
    m_flScale = 456  # offset
    m_nControlPointNumber = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Decay:
    m_bForcePreserveParticleOrder = 449  # offset
    m_bRopeDecay = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DecayClampCount:
    m_nCount = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DecayMaintainCount:
    m_bKillNewest = 816  # offset
    m_bLifespanDecay = 460  # offset
    m_flDecayDelay = 452  # offset
    m_flScale = 464  # offset
    m_nParticlesToMaintain = 448  # offset
    m_nSnapshotControlPoint = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DecayOffscreen:
    m_flOffscreenTime = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DensityForce:
    m_flForceScale = 468  # offset
    m_flRadiusScale = 464  # offset
    m_flTargetDensity = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DifferencePreviousParticle:
    m_bActiveRange = 476  # offset
    m_bSetPreviousParticle = 477  # offset
    m_flInputMax = 460  # offset
    m_flInputMin = 456  # offset
    m_flOutputMax = 468  # offset
    m_flOutputMin = 464  # offset
    m_nFieldInput = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nSetMethod = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Diffusion:
    m_flRadiusScale = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nVoxelGridResolution = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DirectionBetweenVecsToVec:
    m_nFieldOutput = 448  # offset
    m_vecPoint1 = 456  # offset
    m_vecPoint2 = 2112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DistanceBetweenCPsToCP:
    m_CollisionGroupName = 501  # offset
    m_bLOS = 500  # offset
    m_bSetOnce = 472  # offset
    m_flInputMax = 480  # offset
    m_flInputMin = 476  # offset
    m_flLOSScale = 496  # offset
    m_flMaxTraceLength = 492  # offset
    m_flOutputMax = 488  # offset
    m_flOutputMin = 484  # offset
    m_nEndCP = 460  # offset
    m_nOutputCP = 464  # offset
    m_nOutputCPField = 468  # offset
    m_nSetParent = 636  # offset
    m_nStartCP = 456  # offset
    m_nTraceSet = 632  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DistanceBetweenTransforms:
    m_CollisionGroupName = 2080  # offset
    m_TransformEnd = 560  # offset
    m_TransformStart = 456  # offset
    m_bLOS = 2212  # offset
    m_flInputMax = 1016  # offset
    m_flInputMin = 664  # offset
    m_flLOSScale = 2076  # offset
    m_flMaxTraceLength = 2072  # offset
    m_flOutputMax = 1720  # offset
    m_flOutputMin = 1368  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 2216  # offset
    m_nTraceSet = 2208  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DistanceBetweenVecs:
    m_bDeltaTime = 5180  # offset
    m_flInputMax = 4120  # offset
    m_flInputMin = 3768  # offset
    m_flOutputMax = 4824  # offset
    m_flOutputMin = 4472  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 5176  # offset
    m_vecPoint1 = 456  # offset
    m_vecPoint2 = 2112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DistanceCull:
    m_bCullInside = 468  # offset
    m_flDistance = 464  # offset
    m_nAttribute = 472  # offset
    m_nControlPoint = 448  # offset
    m_vecPointOffset = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DistanceToTransform:
    m_CollisionGroupName = 1969  # offset
    m_TransformStart = 1864  # offset
    m_bActiveRange = 2116  # offset
    m_bAdditive = 2117  # offset
    m_bLOS = 1968  # offset
    m_flInputMax = 808  # offset
    m_flInputMin = 456  # offset
    m_flLOSScale = 2108  # offset
    m_flMaxTraceLength = 2104  # offset
    m_flOutputMax = 1512  # offset
    m_flOutputMin = 1160  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 2112  # offset
    m_nTraceSet = 2100  # offset
    m_vecComponentScale = 2120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DragRelativeToPlane:
    m_bDirectional = 1152  # offset
    m_flDragAtPlane = 448  # offset
    m_flFalloff = 800  # offset
    m_nControlPointNumber = 2816  # offset
    m_vecPlaneNormal = 1160  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_DriveCPFromGlobalSoundFloat:
    m_FieldName = 496  # offset
    m_OperatorName = 488  # offset
    m_StackName = 480  # offset
    m_flInputMax = 468  # offset
    m_flInputMin = 464  # offset
    m_flOutputMax = 476  # offset
    m_flOutputMin = 472  # offset
    m_nOutputControlPoint = 456  # offset
    m_nOutputField = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_EnableChildrenFromParentParticleCount:
    m_bDestroyImmediately = 818  # offset
    m_bDisableChildren = 816  # offset
    m_bPlayEndcapOnStop = 817  # offset
    m_nChildGroupID = 456  # offset
    m_nFirstChild = 460  # offset
    m_nNumChildrenToEnable = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_EndCapDecay:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_EndCapTimedDecay:
    m_flDecayTime = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_EndCapTimedFreeze:
    m_flFreezeTime = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ExternalGameImpulseForce:
    m_bExplosions = 818  # offset
    m_bParticles = 819  # offset
    m_bRopes = 816  # offset
    m_bRopesZOnly = 817  # offset
    m_flForceScale = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ExternalWindForce:
    m_bDampenNearWaterPlane = 3778  # offset
    m_bSampleGravity = 3779  # offset
    m_bSampleWater = 3777  # offset
    m_bSampleWind = 3776  # offset
    m_bUseBasicMovementGravity = 5440  # offset
    m_flLocalBuoyancyScale = 5800  # offset
    m_flLocalGravityScale = 5448  # offset
    m_vecBuoyancyForce = 6152  # offset
    m_vecGravityForce = 3784  # offset
    m_vecSamplePosition = 464  # offset
    m_vecScale = 2120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_FadeAndKill:
    m_bForcePreserveParticleOrder = 472  # offset
    m_flEndAlpha = 468  # offset
    m_flEndFadeInTime = 452  # offset
    m_flEndFadeOutTime = 460  # offset
    m_flStartAlpha = 464  # offset
    m_flStartFadeInTime = 448  # offset
    m_flStartFadeOutTime = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_FadeAndKillForTracers:
    m_flEndAlpha = 468  # offset
    m_flEndFadeInTime = 452  # offset
    m_flEndFadeOutTime = 460  # offset
    m_flStartAlpha = 464  # offset
    m_flStartFadeInTime = 448  # offset
    m_flStartFadeOutTime = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_FadeIn:
    m_bProportional = 460  # offset
    m_flFadeInTimeExp = 456  # offset
    m_flFadeInTimeMax = 452  # offset
    m_flFadeInTimeMin = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_FadeInSimple:
    m_flFadeInTime = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_FadeOut:
    m_bEaseInAndOut = 513  # offset
    m_bProportional = 512  # offset
    m_flFadeBias = 460  # offset
    m_flFadeOutTimeExp = 456  # offset
    m_flFadeOutTimeMax = 452  # offset
    m_flFadeOutTimeMin = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_FadeOutSimple:
    m_flFadeOutTime = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ForceBasedOnDistanceToPlane:
    m_flExponent = 512  # offset
    m_flMaxDist = 480  # offset
    m_flMinDist = 464  # offset
    m_nControlPointNumber = 508  # offset
    m_vecForceAtMaxDist = 484  # offset
    m_vecForceAtMinDist = 468  # offset
    m_vecPlaneNormal = 496  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ForceControlPointStub:
    m_ControlPoint = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_GameDecalRenderer:
    m_bNoDecalsOnOwner = 6939  # offset
    m_bRandomDecalRotation = 6937  # offset
    m_bRandomlySelectDecalInGroup = 6938  # offset
    m_bUseGameDefaultDecalSize = 6936  # offset
    m_bVisualizeTraces = 6940  # offset
    m_flDecalRotation = 4928  # offset
    m_flDecalSize = 4224  # offset
    m_flTraceBloat = 3872  # offset
    m_nCollisionGroup = 552  # offset
    m_nDecalGroupIndex = 4576  # offset
    m_nEventType = 536  # offset
    m_nInteractionMask = 544  # offset
    m_sDecalGroupName = 528  # offset
    m_vModulationColor = 5280  # offset
    m_vecEndPos = 2216  # offset
    m_vecStartPos = 560  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_GameLiquidSpill:
    m_flExpirationTime = 880  # offset
    m_flLiquidContentsField = 528  # offset
    m_nAmountAttribute = 1232  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_GlobalLight:
    m_bClampLowerRange = 452  # offset
    m_bClampUpperRange = 453  # offset
    m_flScale = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_HSVShiftToCP:
    m_DefaultHSVColor = 468  # offset
    m_nColorCP = 456  # offset
    m_nColorGemEnableCP = 460  # offset
    m_nOutputCP = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_InheritFromParentParticles:
    m_bRandomDistribution = 460  # offset
    m_flScale = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nIncrement = 456  # offset

    __metadata__ =     [
        {
            "name": "MParticleMaxVersion",
            "type": "Unknown"
        },
        {
            "name": "MParticleReplacementOp",
            "type": "Unknown"
        },
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_InheritFromParentParticlesV2:
    m_bRandomDistribution = 1160  # offset
    m_bReverse = 1161  # offset
    m_flInterpolation = 1168  # offset
    m_flScale = 448  # offset
    m_nFieldOutput = 800  # offset
    m_nIncrement = 808  # offset
    m_nMissingParentBehavior = 1164  # offset

    __metadata__ =     [
        {
            "name": "MParticleMinVersion",
            "type": "Unknown"
        },
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_InheritFromPeerSystem:
    m_nFieldInput = 452  # offset
    m_nFieldOutput = 448  # offset
    m_nGroupID = 460  # offset
    m_nIncrement = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_InstantaneousEmitter:
    m_flInitFromKilledParentParticles = 1160  # offset
    m_flParentParticleScale = 1168  # offset
    m_flStartTime = 808  # offset
    m_nEventType = 1164  # offset
    m_nMaxEmittedPerFrame = 1520  # offset
    m_nParticlesToEmit = 456  # offset
    m_nSnapshotControlPoint = 1524  # offset
    m_strSnapshotSubset = 1528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_InterpolateRadius:
    m_bEaseInAndOut = 464  # offset
    m_flBias = 468  # offset
    m_flEndScale = 460  # offset
    m_flEndTime = 452  # offset
    m_flStartScale = 456  # offset
    m_flStartTime = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_IntraParticleForce:
    m_bUseAABB = 488  # offset
    m_flAttractionMaxDistance = 468  # offset
    m_flAttractionMaxStrength = 472  # offset
    m_flAttractionMinDistance = 464  # offset
    m_flRepulsionMaxDistance = 480  # offset
    m_flRepulsionMaxStrength = 484  # offset
    m_flRepulsionMinDistance = 476  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LagCompensation:
    m_nDesiredVelocityCP = 448  # offset
    m_nDesiredVelocityCPField = 460  # offset
    m_nLatencyCP = 452  # offset
    m_nLatencyCPField = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LazyCullCompareFloat:
    m_flComparsion1 = 448  # offset
    m_flComparsion2 = 800  # offset
    m_flCullTime = 1152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LerpEndCapScalar:
    m_flLerpTime = 456  # offset
    m_flOutput = 452  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LerpEndCapVector:
    m_flLerpTime = 464  # offset
    m_nFieldOutput = 448  # offset
    m_vecOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LerpScalar:
    m_flEndTime = 812  # offset
    m_flOutput = 456  # offset
    m_flStartTime = 808  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LerpToInitialPosition:
    m_flInterpolation = 456  # offset
    m_flScale = 816  # offset
    m_nCacheField = 808  # offset
    m_nControlPointNumber = 448  # offset
    m_vecScale = 1168  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LerpToOtherAttribute:
    m_flInterpolation = 448  # offset
    m_nFieldInput = 804  # offset
    m_nFieldInputFrom = 800  # offset
    m_nFieldOutput = 808  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LerpVector:
    m_flEndTime = 468  # offset
    m_flStartTime = 464  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 472  # offset
    m_vecOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LightningSnapshotGenerator:
    m_flBranchTwist = 2936  # offset
    m_flDedicatedPool = 4000  # offset
    m_flOffset = 824  # offset
    m_flOffsetDecay = 1176  # offset
    m_flRadiusEnd = 3648  # offset
    m_flRadiusStart = 3296  # offset
    m_flRecalcRate = 1528  # offset
    m_flSegments = 472  # offset
    m_flSplitRate = 2584  # offset
    m_flUVOffset = 2232  # offset
    m_flUVScale = 1880  # offset
    m_nBranchBehavior = 3288  # offset
    m_nCPEndPnt = 464  # offset
    m_nCPSnapshot = 456  # offset
    m_nCPStartPnt = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LocalAccelerationForce:
    m_nCP = 464  # offset
    m_nScaleCP = 468  # offset
    m_vecAccel = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LockPoints:
    m_flBlendValue = 468  # offset
    m_nControlPoint = 464  # offset
    m_nMaxCol = 452  # offset
    m_nMaxRow = 460  # offset
    m_nMinCol = 448  # offset
    m_nMinRow = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LockToBone:
    m_HitboxSetName = 664  # offset
    m_bRigid = 792  # offset
    m_bRigidRotationLock = 808  # offset
    m_bUseBones = 793  # offset
    m_flJumpThreshold = 656  # offset
    m_flLifeTimeFadeEnd = 652  # offset
    m_flLifeTimeFadeStart = 648  # offset
    m_flPrevPosScale = 660  # offset
    m_flRotLerp = 2472  # offset
    m_modelInput = 448  # offset
    m_nFieldOutput = 796  # offset
    m_nFieldOutputPrev = 800  # offset
    m_nRotationSetType = 804  # offset
    m_transformInput = 544  # offset
    m_vecRotation = 816  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LockToPointList:
    m_bClosedLoop = 481  # offset
    m_bPlaceAlongPath = 480  # offset
    m_nFieldOutput = 448  # offset
    m_nNumPointsAlongPath = 484  # offset
    m_pointList = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LockToSavedSequentialPath:
    m_PathParams = 464  # offset
    m_bCPPairs = 460  # offset
    m_flFadeEnd = 456  # offset
    m_flFadeStart = 452  # offset

    __metadata__ =     [
        {
            "name": "MParticleMaxVersion",
            "type": "Unknown"
        },
        {
            "name": "MParticleReplacementOp",
            "type": "Unknown"
        },
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_LockToSavedSequentialPathV2:
    m_PathParams = 464  # offset
    m_bCPPairs = 456  # offset
    m_flFadeEnd = 452  # offset
    m_flFadeStart = 448  # offset

    __metadata__ =     [
        {
            "name": "MParticleMinVersion",
            "type": "Unknown"
        },
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MaintainEmitter:
    m_bEmitInstantaneously = 1184  # offset
    m_bFinalEmitOnStop = 1185  # offset
    m_flEmissionDuration = 816  # offset
    m_flEmissionRate = 1168  # offset
    m_flScale = 1192  # offset
    m_flStartTime = 808  # offset
    m_nParticlesToMaintain = 456  # offset
    m_nSnapshotControlPoint = 1172  # offset
    m_strSnapshotSubset = 1176  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MaintainSequentialPath:
    m_PathParams = 480  # offset
    m_bLoop = 464  # offset
    m_bUseParticleCount = 465  # offset
    m_fMaxDistance = 448  # offset
    m_flCohesionStrength = 456  # offset
    m_flNumToAssign = 452  # offset
    m_flTolerance = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MaxVelocity:
    m_flMaxVelocity = 448  # offset
    m_flMinVelocity = 452  # offset
    m_nOverrideCP = 456  # offset
    m_nOverrideCPField = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ModelCull:
    m_HitboxSetName = 455  # offset
    m_bBoundBox = 452  # offset
    m_bCullOutside = 453  # offset
    m_bUseBones = 454  # offset
    m_nControlPointNumber = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ModelDampenMovement:
    m_HitboxSetName = 455  # offset
    m_bBoundBox = 452  # offset
    m_bOutside = 453  # offset
    m_bUseBones = 454  # offset
    m_fDrag = 2240  # offset
    m_nControlPointNumber = 448  # offset
    m_vecPosOffset = 584  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MoveToHitbox:
    m_HitboxSetName = 664  # offset
    m_bUseBones = 792  # offset
    m_flInterpolation = 800  # offset
    m_flLifeTimeLerpEnd = 656  # offset
    m_flLifeTimeLerpStart = 652  # offset
    m_flPrevPosScale = 660  # offset
    m_modelInput = 448  # offset
    m_nLerpType = 796  # offset
    m_transformInput = 544  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementLoopInsideSphere:
    m_flDistance = 456  # offset
    m_nCP = 448  # offset
    m_nDistSqrAttr = 2464  # offset
    m_vecScale = 808  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementMaintainOffset:
    m_bRadiusScale = 464  # offset
    m_nCP = 460  # offset
    m_vecOffset = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementMoveAlongSkinnedCPSnapshot:
    m_bSetNormal = 456  # offset
    m_bSetRadius = 457  # offset
    m_flInterpolation = 464  # offset
    m_flTValue = 816  # offset
    m_nControlPointNumber = 448  # offset
    m_nSnapshotControlPointNumber = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementPlaceOnGround:
    m_CollisionGroupName = 816  # offset
    m_bIncludeShotHull = 972  # offset
    m_bIncludeWater = 973  # offset
    m_bScaleOffset = 977  # offset
    m_bSetNormal = 976  # offset
    m_flLerpRate = 812  # offset
    m_flMaxTraceLength = 800  # offset
    m_flOffset = 448  # offset
    m_flTolerance = 804  # offset
    m_flTraceOffset = 808  # offset
    m_nIgnoreCP = 984  # offset
    m_nLerpCP = 956  # offset
    m_nPreserveOffsetCP = 980  # offset
    m_nRefCP1 = 948  # offset
    m_nRefCP2 = 952  # offset
    m_nTraceMissBehavior = 968  # offset
    m_nTraceSet = 944  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementRigidAttachToCP:
    m_bOffsetLocal = 468  # offset
    m_nControlPointNumber = 448  # offset
    m_nFieldInput = 460  # offset
    m_nFieldOutput = 464  # offset
    m_nScaleCPField = 456  # offset
    m_nScaleControlPoint = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementRotateParticleAroundAxis:
    m_TransformInput = 2456  # offset
    m_bLocalSpace = 2560  # offset
    m_flRotRate = 2104  # offset
    m_vecRotAxis = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_MovementSkinnedPositionFromCPSnapshot:
    m_bRandom = 456  # offset
    m_bSetNormal = 464  # offset
    m_bSetRadius = 465  # offset
    m_flIncrement = 824  # offset
    m_flInterpolation = 1880  # offset
    m_flReadIndex = 472  # offset
    m_nControlPointNumber = 452  # offset
    m_nFullLoopIncrement = 1176  # offset
    m_nIndexType = 468  # offset
    m_nRandomSeed = 460  # offset
    m_nSnapShotStartPoint = 1528  # offset
    m_nSnapshotControlPointNumber = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Noise:
    m_bAdditive = 464  # offset
    m_fl4NoiseScale = 460  # offset
    m_flNoiseAnimationTimeScale = 468  # offset
    m_flOutputMax = 456  # offset
    m_flOutputMin = 452  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_NoiseEmitter:
    m_bAbsVal = 480  # offset
    m_bAbsValInv = 481  # offset
    m_flEmissionDuration = 456  # offset
    m_flEmissionScale = 464  # offset
    m_flNoiseScale = 496  # offset
    m_flOffset = 484  # offset
    m_flOutputMax = 492  # offset
    m_flOutputMin = 488  # offset
    m_flStartTime = 460  # offset
    m_flWorldNoiseScale = 500  # offset
    m_flWorldTimeScale = 516  # offset
    m_nScaleControlPoint = 468  # offset
    m_nScaleControlPointField = 472  # offset
    m_nWorldNoisePoint = 476  # offset
    m_vecOffsetLoc = 504  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_NormalLock:
    m_nControlPointNumber = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_NormalizeVector:
    m_flScale = 452  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Orient2DRelToCP:
    m_flRotOffset = 448  # offset
    m_flSpinStrength = 452  # offset
    m_nCP = 456  # offset
    m_nFieldOutput = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_OrientTo2dDirection:
    m_flRotOffset = 448  # offset
    m_flSpinStrength = 452  # offset
    m_nFieldOutput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_OscillateScalar:
    m_FrequencyMax = 460  # offset
    m_FrequencyMin = 456  # offset
    m_RateMax = 452  # offset
    m_RateMin = 448  # offset
    m_bProportional = 468  # offset
    m_bProportionalOp = 469  # offset
    m_flEndTime_max = 484  # offset
    m_flEndTime_min = 480  # offset
    m_flOscAdd = 492  # offset
    m_flOscMult = 488  # offset
    m_flStartTime_max = 476  # offset
    m_flStartTime_min = 472  # offset
    m_nField = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_OscillateScalarSimple:
    m_Frequency = 452  # offset
    m_Rate = 448  # offset
    m_flOscAdd = 464  # offset
    m_flOscMult = 460  # offset
    m_nField = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_OscillateVector:
    m_FrequencyMax = 484  # offset
    m_FrequencyMin = 472  # offset
    m_RateMax = 460  # offset
    m_RateMin = 448  # offset
    m_bOffset = 502  # offset
    m_bProportional = 500  # offset
    m_bProportionalOp = 501  # offset
    m_flEndTime_max = 516  # offset
    m_flEndTime_min = 512  # offset
    m_flOscAdd = 872  # offset
    m_flOscMult = 520  # offset
    m_flRateScale = 1224  # offset
    m_flStartTime_max = 508  # offset
    m_flStartTime_min = 504  # offset
    m_nField = 496  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_OscillateVectorSimple:
    m_Frequency = 460  # offset
    m_Rate = 448  # offset
    m_bOffset = 484  # offset
    m_flOscAdd = 480  # offset
    m_flOscMult = 476  # offset
    m_nField = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ParentVortices:
    m_bFlipBasedOnYaw = 480  # offset
    m_flForceScale = 464  # offset
    m_vecTwistAxis = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PerParticleForce:
    m_flForceScale = 464  # offset
    m_nCP = 2472  # offset
    m_vForce = 816  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PercentageBetweenTransformLerpCPs:
    m_TransformEnd = 568  # offset
    m_TransformStart = 464  # offset
    m_bActiveRange = 692  # offset
    m_bRadialCheck = 693  # offset
    m_flInputMax = 456  # offset
    m_flInputMin = 452  # offset
    m_nFieldOutput = 448  # offset
    m_nOutputEndCP = 680  # offset
    m_nOutputEndField = 684  # offset
    m_nOutputStartCP = 672  # offset
    m_nOutputStartField = 676  # offset
    m_nSetMethod = 688  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PercentageBetweenTransforms:
    m_TransformEnd = 576  # offset
    m_TransformStart = 472  # offset
    m_bActiveRange = 684  # offset
    m_bRadialCheck = 685  # offset
    m_flInputMax = 456  # offset
    m_flInputMin = 452  # offset
    m_flOutputMax = 464  # offset
    m_flOutputMin = 460  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 680  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PercentageBetweenTransformsVector:
    m_TransformEnd = 592  # offset
    m_TransformStart = 488  # offset
    m_bActiveRange = 700  # offset
    m_bRadialCheck = 701  # offset
    m_flInputMax = 456  # offset
    m_flInputMin = 452  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 696  # offset
    m_vecOutputMax = 472  # offset
    m_vecOutputMin = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PinParticleToCP:
    m_bOffsetLocal = 2112  # offset
    m_bRetainInitialVelocity = 4248  # offset
    m_flAge = 3184  # offset
    m_flBreakDistance = 2480  # offset
    m_flBreakSpeed = 2832  # offset
    m_flBreakValue = 3544  # offset
    m_flInterpolation = 3896  # offset
    m_nBreakControlPointNumber = 3536  # offset
    m_nBreakControlPointNumber2 = 3540  # offset
    m_nControlPointNumber = 448  # offset
    m_nParticleNumber = 2120  # offset
    m_nParticleSelection = 2116  # offset
    m_nPinBreakType = 2472  # offset
    m_vecOffset = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PinRopeSegmentParticleToParent:
    m_flInterpolation = 808  # offset
    m_nParticleNumber = 456  # offset
    m_nParticleSelection = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PlanarConstraint:
    m_PlaneNormal = 460  # offset
    m_PointOnPlane = 448  # offset
    m_bGlobalNormal = 477  # offset
    m_bGlobalOrigin = 476  # offset
    m_bUseOldCode = 1184  # offset
    m_flMaximumDistanceToCP = 832  # offset
    m_flRadiusScale = 480  # offset
    m_nControlPointNumber = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PlaneCull:
    m_bLocalSpace = 464  # offset
    m_flPlaneOffset = 468  # offset
    m_nPlaneControlPoint = 448  # offset
    m_vecPlaneDirection = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PlayEndCapWhenFinished:
    m_bFireOnEmissionEnd = 456  # offset
    m_bIncludeChildren = 457  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PointVectorAtNextParticle:
    m_flInterpolation = 456  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_PositionLock:
    m_TransformInput = 448  # offset
    m_bLockRot = 944  # offset
    m_flEndTime_exp = 572  # offset
    m_flEndTime_max = 568  # offset
    m_flEndTime_min = 564  # offset
    m_flJumpThreshold = 936  # offset
    m_flPrevPosScale = 940  # offset
    m_flRange = 576  # offset
    m_flRangeBias = 584  # offset
    m_flStartTime_exp = 560  # offset
    m_flStartTime_max = 556  # offset
    m_flStartTime_min = 552  # offset
    m_nFieldOutput = 2608  # offset
    m_nFieldOutputPrev = 2612  # offset
    m_vecScale = 952  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_QuantizeCPComponent:
    m_flInputValue = 456  # offset
    m_flQuantizeValue = 816  # offset
    m_nCPOutput = 808  # offset
    m_nOutVectorField = 812  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_QuantizeFloat:
    m_InputValue = 448  # offset
    m_nOutputField = 800  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RadiusDecay:
    m_flMinRadius = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RampCPLinearRandom:
    m_nOutControlPointNumber = 456  # offset
    m_vecRateMax = 472  # offset
    m_vecRateMin = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RampScalarLinear:
    m_RateMax = 452  # offset
    m_RateMin = 448  # offset
    m_bProportionalOp = 516  # offset
    m_flEndTime_max = 468  # offset
    m_flEndTime_min = 464  # offset
    m_flStartTime_max = 460  # offset
    m_flStartTime_min = 456  # offset
    m_nField = 512  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RampScalarLinearSimple:
    m_Rate = 448  # offset
    m_flEndTime = 456  # offset
    m_flStartTime = 452  # offset
    m_nField = 496  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RampScalarSpline:
    m_RateMax = 452  # offset
    m_RateMin = 448  # offset
    m_bEaseOut = 517  # offset
    m_bProportionalOp = 516  # offset
    m_flBias = 472  # offset
    m_flEndTime_max = 468  # offset
    m_flEndTime_min = 464  # offset
    m_flStartTime_max = 460  # offset
    m_flStartTime_min = 456  # offset
    m_nField = 512  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RampScalarSplineSimple:
    m_Rate = 448  # offset
    m_bEaseOut = 500  # offset
    m_flEndTime = 456  # offset
    m_flStartTime = 452  # offset
    m_nField = 496  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RandomForce:
    m_MaxForce = 476  # offset
    m_MinForce = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ReadFromNeighboringParticle:
    m_DistanceCheck = 464  # offset
    m_flInterpolation = 816  # offset
    m_nFieldInput = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nIncrement = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ReinitializeScalarEndCap:
    m_flOutputMax = 456  # offset
    m_flOutputMin = 452  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapAverageHitboxSpeedtoCP:
    m_HitboxSetName = 3544  # offset
    m_flInputMax = 824  # offset
    m_flInputMin = 472  # offset
    m_flOutputMax = 1528  # offset
    m_flOutputMin = 1176  # offset
    m_nField = 464  # offset
    m_nHeightControlPointNumber = 1880  # offset
    m_nHitboxDataType = 468  # offset
    m_nInControlPointNumber = 456  # offset
    m_nOutControlPointNumber = 460  # offset
    m_vecComparisonVelocity = 1888  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapAverageScalarValuetoCP:
    m_flDecimalPlaces = 464  # offset
    m_flOutputRemap = 832  # offset
    m_nExpression = 456  # offset
    m_nField = 824  # offset
    m_nOutControlPointNumber = 816  # offset
    m_nOutVectorField = 820  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapBoundingVolumetoCP:
    m_flInputMax = 464  # offset
    m_flInputMin = 460  # offset
    m_flOutputMax = 472  # offset
    m_flOutputMin = 468  # offset
    m_nOutControlPointNumber = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapCPVelocityToVector:
    m_bNormalize = 460  # offset
    m_flScale = 456  # offset
    m_nControlPoint = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapCPtoCP:
    m_bDerivative = 488  # offset
    m_flInputMax = 476  # offset
    m_flInputMin = 472  # offset
    m_flInterpRate = 492  # offset
    m_flOutputMax = 484  # offset
    m_flOutputMin = 480  # offset
    m_nInputControlPoint = 456  # offset
    m_nInputField = 464  # offset
    m_nOutputControlPoint = 460  # offset
    m_nOutputField = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapCPtoScalar:
    m_flEndTime = 480  # offset
    m_flInputMax = 464  # offset
    m_flInputMin = 460  # offset
    m_flInterpRate = 484  # offset
    m_flOutputMax = 472  # offset
    m_flOutputMin = 468  # offset
    m_flStartTime = 476  # offset
    m_nCPInput = 448  # offset
    m_nField = 456  # offset
    m_nFieldOutput = 452  # offset
    m_nSetMethod = 488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapCPtoVector:
    m_bAccelerate = 525  # offset
    m_bOffset = 524  # offset
    m_flEndTime = 512  # offset
    m_flInterpRate = 516  # offset
    m_flStartTime = 508  # offset
    m_nCPInput = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nLocalSpaceCP = 456  # offset
    m_nSetMethod = 520  # offset
    m_vInputMax = 472  # offset
    m_vInputMin = 460  # offset
    m_vOutputMax = 496  # offset
    m_vOutputMin = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapControlPointDirectionToVector:
    m_flScale = 452  # offset
    m_nControlPointNumber = 456  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapControlPointOrientationToRotation:
    m_flOffsetRot = 456  # offset
    m_nCP = 448  # offset
    m_nComponent = 460  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapCrossProductOfTwoVectorsToVector:
    m_InputVec1 = 448  # offset
    m_InputVec2 = 2104  # offset
    m_bNormalize = 3764  # offset
    m_nFieldOutput = 3760  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDensityGradientToVectorAttribute:
    m_flRadiusScale = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDensityToVector:
    m_bUseParentDensity = 488  # offset
    m_flDensityMax = 460  # offset
    m_flDensityMin = 456  # offset
    m_flRadiusScale = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nVoxelGridResolution = 492  # offset
    m_vecOutputMax = 476  # offset
    m_vecOutputMin = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDirectionToCPToVector:
    m_bNormalize = 476  # offset
    m_flOffsetRot = 460  # offset
    m_flScale = 456  # offset
    m_nCP = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nFieldStrength = 480  # offset
    m_vecOffsetAxis = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDistanceToLineSegmentBase:
    m_bInfiniteLine = 464  # offset
    m_flMaxInputValue = 460  # offset
    m_flMinInputValue = 456  # offset
    m_nCP0 = 448  # offset
    m_nCP1 = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDistanceToLineSegmentToScalar:
    m_flMaxOutputValue = 480  # offset
    m_flMinOutputValue = 476  # offset
    m_nFieldOutput = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDistanceToLineSegmentToVector:
    m_nFieldOutput = 472  # offset
    m_vMaxOutputValue = 488  # offset
    m_vMinOutputValue = 476  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDotProductToCP:
    m_flInputMax = 824  # offset
    m_flInputMin = 472  # offset
    m_flOutputMax = 1528  # offset
    m_flOutputMin = 1176  # offset
    m_nInputCP1 = 456  # offset
    m_nInputCP2 = 460  # offset
    m_nOutVectorField = 468  # offset
    m_nOutputCP = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapDotProductToScalar:
    m_bActiveRange = 484  # offset
    m_bUseParticleNormal = 485  # offset
    m_bUseParticleVelocity = 476  # offset
    m_flInputMax = 464  # offset
    m_flInputMin = 460  # offset
    m_flOutputMax = 472  # offset
    m_flOutputMin = 468  # offset
    m_nFieldOutput = 456  # offset
    m_nInputCP1 = 448  # offset
    m_nInputCP2 = 452  # offset
    m_nSetMethod = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapExternalWindToCP:
    m_bSetMagnitude = 2120  # offset
    m_nCP = 456  # offset
    m_nCPOutput = 460  # offset
    m_nOutVectorField = 2124  # offset
    m_vecScale = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapGravityToVector:
    m_bNormalizedOutput = 2112  # offset
    m_nOutputField = 2104  # offset
    m_nSetMethod = 2108  # offset
    m_vInput1 = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapModelVolumetoCP:
    m_bBBoxOnly = 492  # offset
    m_bCubeRoot = 493  # offset
    m_flInputMax = 480  # offset
    m_flInputMin = 476  # offset
    m_flOutputMax = 488  # offset
    m_flOutputMin = 484  # offset
    m_nBBoxType = 456  # offset
    m_nField = 472  # offset
    m_nInControlPointNumber = 460  # offset
    m_nOutControlPointMaxNumber = 468  # offset
    m_nOutControlPointNumber = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelBodyPartEndCap:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelBodyPartOnceTimed:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelElementEndCap:
    m_bModelFromRenderer = 528  # offset
    m_fallbackNames = 504  # offset
    m_hModel = 448  # offset
    m_inNames = 456  # offset
    m_nFieldInput = 532  # offset
    m_nFieldOutput = 536  # offset
    m_outNames = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelElementOnceTimed:
    m_bModelFromRenderer = 528  # offset
    m_bProportional = 529  # offset
    m_fallbackNames = 504  # offset
    m_flRemapTime = 540  # offset
    m_hModel = 448  # offset
    m_inNames = 456  # offset
    m_nFieldInput = 532  # offset
    m_nFieldOutput = 536  # offset
    m_outNames = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelMeshGroupEndCap:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelMeshGroupOnceTimed:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelSequenceEndCap:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapNamedModelSequenceOnceTimed:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapParticleCountOnScalarEndCap:
    m_bBackwards = 468  # offset
    m_flOutputMax = 464  # offset
    m_flOutputMin = 460  # offset
    m_nFieldOutput = 448  # offset
    m_nInputMax = 456  # offset
    m_nInputMin = 452  # offset
    m_nSetMethod = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapParticleCountToScalar:
    m_bActiveRange = 1864  # offset
    m_flOutputMax = 1512  # offset
    m_flOutputMin = 1160  # offset
    m_nFieldOutput = 448  # offset
    m_nInputMax = 808  # offset
    m_nInputMin = 456  # offset
    m_nSetMethod = 1868  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapSDFDistanceToScalarAttribute:
    m_flMaxDistance = 808  # offset
    m_flMinDistance = 456  # offset
    m_flValueAboveMax = 2216  # offset
    m_flValueAtMax = 1864  # offset
    m_flValueAtMin = 1512  # offset
    m_flValueBelowMin = 1160  # offset
    m_nFieldOutput = 448  # offset
    m_nVectorFieldInput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapSDFDistanceToVectorAttribute:
    m_flMaxDistance = 808  # offset
    m_flMinDistance = 456  # offset
    m_nVectorFieldInput = 452  # offset
    m_nVectorFieldOutput = 448  # offset
    m_vValueAboveMax = 1196  # offset
    m_vValueAtMax = 1184  # offset
    m_vValueAtMin = 1172  # offset
    m_vValueBelowMin = 1160  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapSDFGradientToVectorAttribute:
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapScalar:
    m_bOldCode = 472  # offset
    m_flInputMax = 460  # offset
    m_flInputMin = 456  # offset
    m_flOutputMax = 468  # offset
    m_flOutputMin = 464  # offset
    m_nFieldInput = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapScalarEndCap:
    m_flInputMax = 460  # offset
    m_flInputMin = 456  # offset
    m_flOutputMax = 468  # offset
    m_flOutputMin = 464  # offset
    m_nFieldInput = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapScalarOnceTimed:
    m_bProportional = 448  # offset
    m_flInputMax = 464  # offset
    m_flInputMin = 460  # offset
    m_flOutputMax = 472  # offset
    m_flOutputMin = 468  # offset
    m_flRemapTime = 476  # offset
    m_nFieldInput = 452  # offset
    m_nFieldOutput = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapSpeed:
    m_bIgnoreDelta = 472  # offset
    m_flInputMax = 456  # offset
    m_flInputMin = 452  # offset
    m_flOutputMax = 464  # offset
    m_flOutputMin = 460  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapSpeedtoCP:
    m_bUseDeltaV = 484  # offset
    m_flInputMax = 472  # offset
    m_flInputMin = 468  # offset
    m_flOutputMax = 480  # offset
    m_flOutputMin = 476  # offset
    m_nField = 464  # offset
    m_nInControlPointNumber = 456  # offset
    m_nOutControlPointNumber = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapTransformOrientationToRotations:
    m_TransformInput = 448  # offset
    m_bUseQuat = 564  # offset
    m_bWriteNormal = 565  # offset
    m_vecRotation = 552  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapTransformOrientationToYaw:
    m_TransformInput = 448  # offset
    m_flRotOffset = 556  # offset
    m_flSpinStrength = 560  # offset
    m_nFieldOutput = 552  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapTransformToVelocity:
    m_TransformInput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapTransformVisibilityToScalar:
    m_TransformInput = 456  # offset
    m_flInputMax = 568  # offset
    m_flInputMin = 564  # offset
    m_flOutputMax = 576  # offset
    m_flOutputMin = 572  # offset
    m_flRadius = 580  # offset
    m_nFieldOutput = 560  # offset
    m_nSetMethod = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapTransformVisibilityToVector:
    m_TransformInput = 456  # offset
    m_flInputMax = 568  # offset
    m_flInputMin = 564  # offset
    m_flRadius = 596  # offset
    m_nFieldOutput = 560  # offset
    m_nSetMethod = 448  # offset
    m_vecOutputMax = 584  # offset
    m_vecOutputMin = 572  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapVectorComponentToScalar:
    m_nComponent = 456  # offset
    m_nFieldInput = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapVectortoCP:
    m_nFieldInput = 452  # offset
    m_nOutControlPointNumber = 448  # offset
    m_nParticleNumber = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapVelocityToVector:
    m_bNormalize = 456  # offset
    m_flScale = 452  # offset
    m_nFieldOutput = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RemapVisibilityScalar:
    m_flInputMax = 460  # offset
    m_flInputMin = 456  # offset
    m_flOutputMax = 468  # offset
    m_flOutputMin = 464  # offset
    m_flRadiusScale = 472  # offset
    m_nFieldInput = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderAsModels:
    m_ModelList = 528  # offset
    m_bFitToModelSize = 560  # offset
    m_bNonUniformScaling = 561  # offset
    m_flModelScale = 556  # offset
    m_nSizeCullBloat = 576  # offset
    m_nXAxisScalingAttribute = 564  # offset
    m_nYAxisScalingAttribute = 568  # offset
    m_nZAxisScalingAttribute = 572  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderBlobs:
    m_MaterialVars = 1600  # offset
    m_cubeWidth = 528  # offset
    m_cutoffRadius = 880  # offset
    m_hMaterial = 1648  # offset
    m_nIndexCountKb = 1588  # offset
    m_nScaleCP = 1592  # offset
    m_nVertexCountKb = 1584  # offset
    m_renderRadius = 1232  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderCables:
    m_LightingTransform = 5056  # offset
    m_MaterialFloatVars = 5160  # offset
    m_MaterialVecVars = 5192  # offset
    m_bDrawCableCaps = 5024  # offset
    m_flAlphaScale = 880  # offset
    m_flCapOffsetAmount = 5032  # offset
    m_flCapRoundness = 5028  # offset
    m_flColorMapOffsetU = 3968  # offset
    m_flColorMapOffsetV = 3616  # offset
    m_flNormalMapOffsetU = 4672  # offset
    m_flNormalMapOffsetV = 4320  # offset
    m_flRadiusScale = 528  # offset
    m_flTessScale = 5036  # offset
    m_flTextureRepeatsCircumference = 3264  # offset
    m_flTextureRepeatsPerSegment = 2912  # offset
    m_hMaterial = 2896  # offset
    m_nColorBlendType = 2888  # offset
    m_nMaxTesselation = 5044  # offset
    m_nMinTesselation = 5040  # offset
    m_nRoundness = 5048  # offset
    m_nTextureRepetitionMode = 2904  # offset
    m_vecColorScale = 1232  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderClientPhysicsImpulse:
    m_flMagnitude = 880  # offset
    m_flRadius = 528  # offset
    m_nSimIdFilter = 1232  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderClothForce:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderDeferredLight:
    m_bUseAlphaTestWindow = 528  # offset
    m_bUseTexture = 529  # offset
    m_flAlphaScale = 536  # offset
    m_flDistanceFalloff = 2212  # offset
    m_flLightDistance = 2204  # offset
    m_flRadiusScale = 532  # offset
    m_flSpotFoV = 2216  # offset
    m_flStartFalloff = 2208  # offset
    m_hTexture = 2232  # offset
    m_nAlpha2Field = 540  # offset
    m_nAlphaTestPointField = 2220  # offset
    m_nAlphaTestRangeField = 2224  # offset
    m_nAlphaTestSharpnessField = 2228  # offset
    m_nColorBlendType = 2200  # offset
    m_nHSVShiftControlPoint = 2240  # offset
    m_vecColorScale = 544  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderFlattenGrass:
    m_flFlattenStrength = 528  # offset
    m_flRadiusScale = 536  # offset
    m_nStrengthFieldOverride = 532  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderGpuImplicit:
    m_bUsePerParticleRadius = 528  # offset
    m_fGridSize = 544  # offset
    m_fIsosurfaceThreshold = 1248  # offset
    m_fRadiusScale = 896  # offset
    m_hMaterial = 1608  # offset
    m_nIndexCountKb = 536  # offset
    m_nScaleCP = 1600  # offset
    m_nVertexCountKb = 532  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderLightBeam:
    m_bCastShadows = 2544  # offset
    m_flBrightnessLumensPerMeter = 2192  # offset
    m_flRange = 2904  # offset
    m_flSkirt = 2552  # offset
    m_flThickness = 3256  # offset
    m_nColorBlendType = 2184  # offset
    m_vColorBlend = 528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderLights:
    m_bAnimateInFPS = 544  # offset
    m_flAnimationRate = 536  # offset
    m_flEndFadeSize = 560  # offset
    m_flMaxSize = 552  # offset
    m_flMinSize = 548  # offset
    m_flStartFadeSize = 556  # offset
    m_nAnimationType = 540  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderMaterialProxy:
    m_MaterialVars = 536  # offset
    m_flAlpha = 2576  # offset
    m_flMaterialOverrideEnabled = 568  # offset
    m_hOverrideMaterial = 560  # offset
    m_nColorBlendType = 2928  # offset
    m_nMaterialControlPoint = 528  # offset
    m_nProxyType = 532  # offset
    m_vecColorScale = 920  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderModels:
    m_ActivityName = 5936  # offset
    m_ClothEffectName = 6449  # offset
    m_EconSlotName = 7716  # offset
    m_MaterialVars = 6888  # offset
    m_ModelList = 536  # offset
    m_SequenceName = 6192  # offset
    m_bAcceptsDecals = 7982  # offset
    m_bAllowApproximateTransforms = 7985  # offset
    m_bAnimated = 5560  # offset
    m_bCenterOffset = 570  # offset
    m_bDisableDepthPrepass = 7981  # offset
    m_bDisableShadows = 7980  # offset
    m_bDoNotDrawInParticlePass = 7984  # offset
    m_bEnableClothSimulation = 6448  # offset
    m_bForceDrawInterlevedWithSiblings = 7983  # offset
    m_bForceLoopingAnimation = 5921  # offset
    m_bIgnoreNormal = 568  # offset
    m_bIgnoreRadius = 3888  # offset
    m_bLocalScale = 5552  # offset
    m_bManualAnimFrame = 5923  # offset
    m_bOnlyRenderInEffecsGameOverlay = 531  # offset
    m_bOnlyRenderInEffectsBloomPass = 528  # offset
    m_bOnlyRenderInEffectsWaterPass = 529  # offset
    m_bOrientZ = 569  # offset
    m_bOriginalModel = 7972  # offset
    m_bOverrideTranslucentMaterials = 6528  # offset
    m_bResetAnimOnStop = 5922  # offset
    m_bScaleAnimationRate = 5920  # offset
    m_bSuppressTint = 7973  # offset
    m_bUseMixedResolutionRendering = 530  # offset
    m_flAlphaScale = 8600  # offset
    m_flAnimationRate = 5568  # offset
    m_flManualModelSelection = 7264  # offset
    m_flRadiusScale = 8248  # offset
    m_flRenderFilter = 6912  # offset
    m_flRollScale = 8952  # offset
    m_hOverrideMaterial = 6520  # offset
    m_modelInput = 7616  # offset
    m_nAlpha2Field = 9304  # offset
    m_nAnimationField = 5928  # offset
    m_nAnimationScaleField = 5924  # offset
    m_nBodyGroupField = 560  # offset
    m_nColorBlendType = 10968  # offset
    m_nLOD = 7712  # offset
    m_nManualFrameField = 5932  # offset
    m_nModelScaleCP = 3892  # offset
    m_nSizeCullBloat = 5556  # offset
    m_nSkin = 6536  # offset
    m_nSubModelField = 564  # offset
    m_nSubModelFieldType = 7976  # offset
    m_szRenderAttribute = 7986  # offset
    m_vecColorScale = 9312  # offset
    m_vecComponentScale = 3896  # offset
    m_vecLocalOffset = 576  # offset
    m_vecLocalRotation = 2232  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderOmni2Light:
    m_bCastShadows = 2904  # offset
    m_bFog = 2905  # offset
    m_bSphericalCookie = 5032  # offset
    m_flBrightnessCandelas = 2552  # offset
    m_flBrightnessLumens = 2200  # offset
    m_flFogScale = 2912  # offset
    m_flInnerConeAngle = 4320  # offset
    m_flLuminaireRadius = 3264  # offset
    m_flOuterConeAngle = 4672  # offset
    m_flRange = 3968  # offset
    m_flSkirt = 3616  # offset
    m_hLightCookie = 5024  # offset
    m_nBrightnessUnit = 2196  # offset
    m_nColorBlendType = 2192  # offset
    m_nLightType = 528  # offset
    m_vColorBlend = 536  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderPoints:
    m_hMaterial = 528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderPostProcessing:
    m_flPostProcessStrength = 528  # offset
    m_hPostTexture = 880  # offset
    m_nPriority = 888  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderProjected:
    m_MaterialVars = 928  # offset
    m_bEnableProjectedDepthControls = 532  # offset
    m_bFlipHorizontal = 531  # offset
    m_bOrientToNormal = 924  # offset
    m_bProjectCharacter = 528  # offset
    m_bProjectWater = 530  # offset
    m_bProjectWorld = 529  # offset
    m_flAlphaScale = 1304  # offset
    m_flAnimationTimeScale = 920  # offset
    m_flMaterialSelection = 568  # offset
    m_flMaxProjectionDepth = 540  # offset
    m_flMinProjectionDepth = 536  # offset
    m_flRadiusScale = 952  # offset
    m_flRollScale = 1656  # offset
    m_nAlpha2Field = 2008  # offset
    m_nColorBlendType = 3672  # offset
    m_vecColorScale = 2016  # offset
    m_vecProjectedMaterials = 544  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderRopes:
    m_bClampV = 12396  # offset
    m_bClosedLoop = 12433  # offset
    m_bDrawAsOpaque = 12452  # offset
    m_bEnableFadingAndClamping = 11288  # offset
    m_bGenerateNormals = 12453  # offset
    m_bReverseOrder = 12432  # offset
    m_bSortBySegmentID = 12440  # offset
    m_bUseScalarForTextureCoordinate = 12421  # offset
    m_flEndFadeDot = 11312  # offset
    m_flEndFadeSize = 11304  # offset
    m_flMaxSize = 11296  # offset
    m_flMinSize = 11292  # offset
    m_flRadiusTaper = 11316  # offset
    m_flScalarAttributeTextureCoordScale = 12428  # offset
    m_flScaleVOffsetByControlPointDistance = 12416  # offset
    m_flScaleVScrollByControlPointDistance = 12412  # offset
    m_flScaleVSizeByControlPointDistance = 12408  # offset
    m_flStartFadeDot = 11308  # offset
    m_flStartFadeSize = 11300  # offset
    m_flTessScale = 11328  # offset
    m_flTextureVOffset = 12040  # offset
    m_flTextureVScrollRate = 11688  # offset
    m_flTextureVWorldSize = 11336  # offset
    m_nMaxTesselation = 11324  # offset
    m_nMinTesselation = 11320  # offset
    m_nOrientationType = 12444  # offset
    m_nScalarFieldForTextureCoordinate = 12424  # offset
    m_nScaleCP1 = 12400  # offset
    m_nScaleCP2 = 12404  # offset
    m_nSplitField = 12436  # offset
    m_nTextureVParamsCP = 12392  # offset
    m_nVectorFieldForOrientation = 12448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderScreenShake:
    m_flAmplitudeScale = 540  # offset
    m_flDurationScale = 528  # offset
    m_flFrequencyScale = 536  # offset
    m_flRadiusScale = 532  # offset
    m_nAmplitudeField = 556  # offset
    m_nDurationField = 548  # offset
    m_nFilterCP = 560  # offset
    m_nFrequencyField = 552  # offset
    m_nRadiusField = 544  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderScreenVelocityRotate:
    m_flForwardDegrees = 532  # offset
    m_flRotateRateDegrees = 528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderSimpleModelCollection:
    m_bAcceptsDecals = 994  # offset
    m_bCenterOffset = 528  # offset
    m_bDisableMotionBlur = 993  # offset
    m_bDisableShadows = 992  # offset
    m_fDrawFilter = 1000  # offset
    m_fSizeCullScale = 640  # offset
    m_hModel = 536  # offset
    m_modelInput = 544  # offset
    m_nAngularVelocityField = 1352  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderSound:
    m_bSuppressStopSoundEvent = 824  # offset
    m_flDurationScale = 528  # offset
    m_flPitchScale = 536  # offset
    m_flSndLvlScale = 532  # offset
    m_flVolumeScale = 540  # offset
    m_nCPReference = 564  # offset
    m_nChannel = 560  # offset
    m_nDurationField = 548  # offset
    m_nPitchField = 552  # offset
    m_nSndLvlField = 544  # offset
    m_nVolumeField = 556  # offset
    m_pszSoundName = 568  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderSprites:
    m_OutlineColor = 13437  # offset
    m_bDistanceAlpha = 13424  # offset
    m_bOutline = 13436  # offset
    m_bParticleShadows = 14176  # offset
    m_bSequenceNumbersAreRawSequenceIndices = 11640  # offset
    m_bSoftEdges = 13425  # offset
    m_bUseYawWithNormalAligned = 11652  # offset
    m_flAlphaAdjustWithSizeAdjust = 12360  # offset
    m_flEdgeSoftnessEnd = 13432  # offset
    m_flEdgeSoftnessStart = 13428  # offset
    m_flEndFadeDot = 13420  # offset
    m_flEndFadeSize = 13064  # offset
    m_flLightingDirectionality = 13824  # offset
    m_flLightingTessellation = 13472  # offset
    m_flMaxSize = 12008  # offset
    m_flMinSize = 11656  # offset
    m_flOutlineEnd0 = 13456  # offset
    m_flOutlineEnd1 = 13460  # offset
    m_flOutlineStart0 = 13448  # offset
    m_flOutlineStart1 = 13452  # offset
    m_flShadowDensity = 14180  # offset
    m_flStartFadeDot = 13416  # offset
    m_flStartFadeSize = 12712  # offset
    m_nLightingMode = 13464  # offset
    m_nOrientationControlPoint = 11648  # offset
    m_nOrientationType = 11644  # offset
    m_nOutlineAlpha = 13444  # offset
    m_nSequenceOverride = 11288  # offset
    m_replicationParameters = 14184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderStandardLight:
    m_bCastShadows = 2552  # offset
    m_bClosedLoop = 5065  # offset
    m_bIgnoreDT = 5080  # offset
    m_bRenderDiffuse = 4680  # offset
    m_bRenderSpecular = 4681  # offset
    m_bReverseOrder = 5064  # offset
    m_flCapsuleLength = 5060  # offset
    m_flConstrainRadiusToLengthRatio = 5084  # offset
    m_flFalloffLinearity = 3624  # offset
    m_flFiftyPercentFalloff = 3976  # offset
    m_flFogContribution = 4704  # offset
    m_flIntensity = 2200  # offset
    m_flLengthFadeInTime = 5092  # offset
    m_flLengthScale = 5088  # offset
    m_flMaxLength = 5072  # offset
    m_flMinLength = 5076  # offset
    m_flPhi = 2912  # offset
    m_flRadiusMultiplier = 3264  # offset
    m_flTheta = 2560  # offset
    m_flZeroPercentFalloff = 4328  # offset
    m_lightCookie = 4688  # offset
    m_nAttenuationStyle = 3616  # offset
    m_nCapsuleLightBehavior = 5056  # offset
    m_nColorBlendType = 2192  # offset
    m_nFogLightingMode = 4700  # offset
    m_nLightType = 528  # offset
    m_nPrevPntSource = 5068  # offset
    m_nPriority = 4696  # offset
    m_vecColorScale = 536  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderStatusEffect:
    m_pTextureColorWarp = 528  # offset
    m_pTextureDetail2 = 536  # offset
    m_pTextureDiffuseWarp = 544  # offset
    m_pTextureEnvMap = 576  # offset
    m_pTextureFresnelColorWarp = 552  # offset
    m_pTextureFresnelWarp = 560  # offset
    m_pTextureSpecularWarp = 568  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderStatusEffectCitadel:
    m_pTextureColorWarp = 528  # offset
    m_pTextureDetail = 568  # offset
    m_pTextureMetalness = 544  # offset
    m_pTextureNormal = 536  # offset
    m_pTextureRoughness = 552  # offset
    m_pTextureSelfIllum = 560  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderText:
    m_DefaultText = 536  # offset
    m_OutlineColor = 528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderTrails:
    m_bEnableFadingAndClamping = 12016  # offset
    m_bFlipUVBasedOnPitchYaw = 16788  # offset
    m_bIgnoreDT = 12040  # offset
    m_flConstrainRadiusToLengthRatio = 12044  # offset
    m_flEndFadeDot = 12024  # offset
    m_flForwardShift = 16784  # offset
    m_flHeadAlphaScale = 14064  # offset
    m_flLengthFadeInTime = 12052  # offset
    m_flLengthScale = 12048  # offset
    m_flMaxLength = 12032  # offset
    m_flMinLength = 12036  # offset
    m_flRadiusHeadTaper = 12056  # offset
    m_flRadiusTaper = 14416  # offset
    m_flStartFadeDot = 12020  # offset
    m_flTailAlphaScale = 16424  # offset
    m_nHorizCropField = 16776  # offset
    m_nPrevPntSource = 12028  # offset
    m_nVertCropField = 16780  # offset
    m_vecHeadColorScale = 12408  # offset
    m_vecTailColorScale = 14768  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderTreeShake:
    m_flControlPointOrientationAmount = 560  # offset
    m_flPeakStrength = 528  # offset
    m_flRadialAmount = 556  # offset
    m_flRadius = 536  # offset
    m_flShakeDuration = 544  # offset
    m_flTransitionTime = 548  # offset
    m_flTwistAmount = 552  # offset
    m_nControlPointForLinearDirection = 564  # offset
    m_nPeakStrengthFieldOverride = 532  # offset
    m_nRadiusFieldOverride = 540  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RenderVRHapticEvent:
    m_flAmplitude = 544  # offset
    m_nHand = 528  # offset
    m_nOutputField = 536  # offset
    m_nOutputHandCP = 532  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RepeatedTriggerChildGroup:
    m_bLimitChildCount = 1520  # offset
    m_flClusterCooldown = 1168  # offset
    m_flClusterRefireTime = 464  # offset
    m_flClusterSize = 816  # offset
    m_nChildGroupID = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RestartAfterDuration:
    m_bOnlyChildren = 468  # offset
    m_flDurationMax = 452  # offset
    m_flDurationMin = 448  # offset
    m_nCP = 456  # offset
    m_nCPField = 460  # offset
    m_nChildGroupID = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RopeSpringConstraint:
    m_flAdjustmentScale = 1504  # offset
    m_flInitialRestingLength = 1512  # offset
    m_flMaxDistance = 1152  # offset
    m_flMinDistance = 800  # offset
    m_flRestLength = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RotateVector:
    m_bNormalize = 484  # offset
    m_flRotRateMax = 480  # offset
    m_flRotRateMin = 476  # offset
    m_flScale = 488  # offset
    m_nFieldOutput = 448  # offset
    m_vecRotAxisMax = 464  # offset
    m_vecRotAxisMin = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_RtEnvCull:
    m_RtEnvName = 474  # offset
    m_bCullOnMiss = 472  # offset
    m_bStickInsteadOfCull = 473  # offset
    m_nComponent = 608  # offset
    m_nRTEnvCP = 604  # offset
    m_vecTestDir = 448  # offset
    m_vecTestNormal = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SDFConstraint:
    m_flMaxDist = 800  # offset
    m_flMinDist = 448  # offset
    m_nMaxIterations = 1152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SDFForce:
    m_flForceScale = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SDFLighting:
    m_vLightingDir = 448  # offset
    m_vTint_0 = 460  # offset
    m_vTint_1 = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ScreenSpaceDistanceToEdge:
    m_flMaxDistFromEdge = 456  # offset
    m_flOutputRemap = 808  # offset
    m_nFieldOutput = 448  # offset
    m_nSetMethod = 1160  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ScreenSpacePositionOfTarget:
    m_bOututBehindness = 2104  # offset
    m_flBehindOutputRemap = 2112  # offset
    m_nBehindFieldOutput = 2108  # offset
    m_nBehindSetMethod = 2464  # offset
    m_vecTargetPosition = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ScreenSpaceRotateTowardTarget:
    m_flOutputRemap = 2104  # offset
    m_flScreenEdgeAlignmentDistance = 2464  # offset
    m_nSetMethod = 2456  # offset
    m_vecTargetPosition = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SelectivelyEnableChildren:
    m_bDestroyImmediately = 1513  # offset
    m_bPlayEndcapOnStop = 1512  # offset
    m_nChildGroupID = 456  # offset
    m_nFirstChild = 808  # offset
    m_nNumChildrenToEnable = 1160  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SequenceFromModel:
    m_flInputMax = 464  # offset
    m_flInputMin = 460  # offset
    m_flOutputMax = 472  # offset
    m_flOutputMin = 468  # offset
    m_nControlPointNumber = 448  # offset
    m_nFieldOutput = 452  # offset
    m_nFieldOutputAnim = 456  # offset
    m_nSetMethod = 476  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetAttributeToScalarExpression:
    m_flInput1 = 456  # offset
    m_flInput2 = 808  # offset
    m_flOutputRemap = 1160  # offset
    m_nExpression = 448  # offset
    m_nOutputField = 1512  # offset
    m_nSetMethod = 1516  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetCPOrientationToDirection:
    m_nInputControlPoint = 448  # offset
    m_nOutputControlPoint = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetCPOrientationToGroundNormal:
    m_CollisionGroupName = 464  # offset
    m_bIncludeWater = 616  # offset
    m_flInterpRate = 448  # offset
    m_flMaxTraceLength = 452  # offset
    m_flTolerance = 456  # offset
    m_flTraceOffset = 460  # offset
    m_nInputCP = 596  # offset
    m_nOutputCP = 600  # offset
    m_nTraceSet = 592  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetCPOrientationToPointAtCP:
    m_b2DOrientation = 816  # offset
    m_bAvoidSingularity = 817  # offset
    m_bPointAway = 818  # offset
    m_flInterpolation = 464  # offset
    m_nInputCP = 456  # offset
    m_nOutputCP = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetCPtoVector:
    m_nCPInput = 448  # offset
    m_nFieldOutput = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetChildControlPoints:
    m_bReverse = 816  # offset
    m_bSetOrientation = 817  # offset
    m_nChildGroupID = 448  # offset
    m_nFirstControlPoint = 452  # offset
    m_nFirstSourcePoint = 464  # offset
    m_nNumControlPoints = 456  # offset
    m_nOrientation = 820  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointFieldFromVectorExpression:
    m_flLerp = 3776  # offset
    m_flOutputRemap = 4128  # offset
    m_nExpression = 456  # offset
    m_nOutVectorField = 4484  # offset
    m_nOutputCP = 4480  # offset
    m_vecInput1 = 464  # offset
    m_vecInput2 = 2120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointFieldToScalarExpression:
    m_flInput1 = 464  # offset
    m_flInput2 = 816  # offset
    m_flOutputRemap = 1168  # offset
    m_nExpression = 456  # offset
    m_nOutVectorField = 1524  # offset
    m_nOutputCP = 1520  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointFieldToWater:
    m_nCPField = 464  # offset
    m_nDestCP = 460  # offset
    m_nSourceCP = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointFromObjectScale:
    m_nCPInput = 456  # offset
    m_nCPOutput = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointOrientation:
    m_bRandomize = 458  # offset
    m_bSetOnce = 459  # offset
    m_bUseWorldLocation = 456  # offset
    m_flInterpolation = 496  # offset
    m_nCP = 460  # offset
    m_nHeadLocation = 464  # offset
    m_vecRotation = 468  # offset
    m_vecRotationB = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointOrientationToCPVelocity:
    m_nCPInput = 456  # offset
    m_nCPOutput = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointPositionToRandomActiveCP:
    m_flResetRate = 472  # offset
    m_nCP1 = 456  # offset
    m_nHeadLocationMax = 464  # offset
    m_nHeadLocationMin = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointPositionToTimeOfDayValue:
    m_nControlPointNumber = 456  # offset
    m_pszTimeOfDayParameter = 460  # offset
    m_vecDefaultValue = 588  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointPositions:
    m_bOrient = 457  # offset
    m_bSetOnce = 458  # offset
    m_bUseWorldLocation = 456  # offset
    m_nCP1 = 460  # offset
    m_nCP2 = 464  # offset
    m_nCP3 = 468  # offset
    m_nCP4 = 472  # offset
    m_nHeadLocation = 524  # offset
    m_vecCP1Pos = 476  # offset
    m_vecCP2Pos = 488  # offset
    m_vecCP3Pos = 500  # offset
    m_vecCP4Pos = 512  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointRotation:
    m_flRotRate = 2112  # offset
    m_nCP = 2464  # offset
    m_nLocalCP = 2468  # offset
    m_vecRotAxis = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToCPVelocity:
    m_bNormalize = 464  # offset
    m_nCPField = 472  # offset
    m_nCPInput = 456  # offset
    m_nCPOutputMag = 468  # offset
    m_nCPOutputVel = 460  # offset
    m_vecComparisonVelocity = 480  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToCenter:
    m_bUseAvgParticlePos = 472  # offset
    m_nCP1 = 456  # offset
    m_nSetParent = 476  # offset
    m_vecCP1Pos = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToHMD:
    m_bOrientToHMD = 472  # offset
    m_nCP1 = 456  # offset
    m_vecCP1Pos = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToHand:
    m_bOrientToHand = 476  # offset
    m_nCP1 = 456  # offset
    m_nHand = 460  # offset
    m_vecCP1Pos = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToImpactPoint:
    m_CollisionGroupName = 844  # offset
    m_bIncludeWater = 978  # offset
    m_bSetToEndpoint = 976  # offset
    m_bTraceToClosestSurface = 977  # offset
    m_flOffset = 828  # offset
    m_flStartOffset = 824  # offset
    m_flTraceLength = 472  # offset
    m_flUpdateRate = 464  # offset
    m_nCPIn = 460  # offset
    m_nCPOut = 456  # offset
    m_nTraceSet = 972  # offset
    m_vecTraceDir = 832  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToPlayer:
    m_bOrientToEyes = 472  # offset
    m_nCP1 = 456  # offset
    m_vecCP1Pos = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToVectorExpression:
    m_bNormalizedOutput = 4128  # offset
    m_flLerp = 3776  # offset
    m_nExpression = 456  # offset
    m_nOutputCP = 460  # offset
    m_vInput1 = 464  # offset
    m_vInput2 = 2120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointToWaterSurface:
    m_bAdaptiveThreshold = 832  # offset
    m_flRetestRate = 480  # offset
    m_nActiveCP = 468  # offset
    m_nActiveCPField = 472  # offset
    m_nDestCP = 460  # offset
    m_nFlowCP = 464  # offset
    m_nSourceCP = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointsToModelParticles:
    m_AttachmentName = 576  # offset
    m_HitboxSetName = 448  # offset
    m_bAttachment = 717  # offset
    m_bSkin = 716  # offset
    m_nFirstControlPoint = 704  # offset
    m_nFirstSourcePoint = 712  # offset
    m_nNumControlPoints = 708  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetControlPointsToParticle:
    m_bSetOrientation = 464  # offset
    m_nChildGroupID = 448  # offset
    m_nFirstControlPoint = 452  # offset
    m_nFirstSourcePoint = 460  # offset
    m_nNumControlPoints = 456  # offset
    m_nOrientationMode = 468  # offset
    m_nSetParent = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetFloat:
    m_InputValue = 448  # offset
    m_Lerp = 808  # offset
    m_nOutputField = 800  # offset
    m_nSetMethod = 804  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetFloatAttributeToVectorExpression:
    m_flOutputRemap = 3768  # offset
    m_nExpression = 448  # offset
    m_nOutputField = 4120  # offset
    m_nSetMethod = 4124  # offset
    m_vInput1 = 456  # offset
    m_vInput2 = 2112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetFloatCollection:
    m_InputValue = 448  # offset
    m_Lerp = 808  # offset
    m_nOutputField = 800  # offset
    m_nSetMethod = 804  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetFromCPSnapshot:
    m_bPrev = 1545  # offset
    m_bRandom = 476  # offset
    m_bReverse = 477  # offset
    m_bSubSample = 1544  # offset
    m_flInterpolation = 1192  # offset
    m_nAttributeToRead = 464  # offset
    m_nAttributeToWrite = 468  # offset
    m_nControlPointNumber = 448  # offset
    m_nLocalSpaceCP = 472  # offset
    m_nRandomSeed = 480  # offset
    m_nSnapShotIncrement = 840  # offset
    m_nSnapShotStartPoint = 488  # offset
    m_strSnapshotSubset = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetGravityToCP:
    m_bSetOrientation = 816  # offset
    m_bSetZDown = 817  # offset
    m_flScale = 464  # offset
    m_nCPInput = 456  # offset
    m_nCPOutput = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetParentControlPointsToChildCP:
    m_bSetOrientation = 472  # offset
    m_nChildControlPoint = 460  # offset
    m_nChildGroupID = 456  # offset
    m_nFirstSourcePoint = 468  # offset
    m_nNumControlPoints = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetPerChildControlPoint:
    m_bNumBasedOnParticleCount = 1176  # offset
    m_bSetOrientation = 1168  # offset
    m_nChildGroupID = 448  # offset
    m_nFirstControlPoint = 452  # offset
    m_nFirstSourcePoint = 816  # offset
    m_nNumControlPoints = 456  # offset
    m_nOrientationField = 1172  # offset
    m_nParticleIncrement = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetPerChildControlPointFromAttribute:
    m_bNumBasedOnParticleCount = 468  # offset
    m_nAttributeToRead = 472  # offset
    m_nCPField = 476  # offset
    m_nChildGroupID = 448  # offset
    m_nFirstControlPoint = 452  # offset
    m_nFirstSourcePoint = 464  # offset
    m_nNumControlPoints = 456  # offset
    m_nParticleIncrement = 460  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetRandomControlPointPosition:
    m_bOrient = 457  # offset
    m_bUseWorldLocation = 456  # offset
    m_flInterpolation = 848  # offset
    m_flReRandomRate = 472  # offset
    m_nCP1 = 460  # offset
    m_nHeadLocation = 464  # offset
    m_vecCPMaxPos = 836  # offset
    m_vecCPMinPos = 824  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetSimulationRate:
    m_flSimulationScale = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetSingleControlPointPosition:
    m_bSetOnce = 456  # offset
    m_nCP1 = 460  # offset
    m_transformInput = 2120  # offset
    m_vecCP1Pos = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetToCP:
    m_bOffsetLocal = 464  # offset
    m_nControlPointNumber = 448  # offset
    m_vecOffset = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetUserEvent:
    m_flFallingEdge = 1160  # offset
    m_flInput = 448  # offset
    m_flRisingEdge = 800  # offset
    m_nFallingEventType = 1512  # offset
    m_nRisingEventType = 1152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetVariable:
    m_floatInput = 2304  # offset
    m_positionOffset = 624  # offset
    m_rotationOffset = 636  # offset
    m_transformInput = 520  # offset
    m_variableReference = 456  # offset
    m_vecInput = 648  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetVec:
    m_InputValue = 448  # offset
    m_Lerp = 2112  # offset
    m_bNormalizedOutput = 2464  # offset
    m_nOutputField = 2104  # offset
    m_nSetMethod = 2108  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SetVectorAttributeToVectorExpression:
    m_bNormalizedOutput = 4128  # offset
    m_flLerp = 3768  # offset
    m_nExpression = 448  # offset
    m_nOutputField = 4120  # offset
    m_nSetMethod = 4124  # offset
    m_vInput1 = 456  # offset
    m_vInput2 = 2112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_ShapeMatchingConstraint:
    m_flShapeRestorationTime = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SnapshotRigidSkinToBones:
    m_bTransformNormals = 448  # offset
    m_bTransformRadii = 449  # offset
    m_nControlPointNumber = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SnapshotSkinToBones:
    m_bTransformNormals = 448  # offset
    m_bTransformRadii = 449  # offset
    m_flJumpThreshold = 464  # offset
    m_flLifeTimeFadeEnd = 460  # offset
    m_flLifeTimeFadeStart = 456  # offset
    m_flPrevPosScale = 468  # offset
    m_nControlPointNumber = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_Spin:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SpinUpdate:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SpinYaw:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_SpringToVectorConstraint:
    m_flMaxDistance = 1152  # offset
    m_flMinDistance = 800  # offset
    m_flRestLength = 448  # offset
    m_flRestingLength = 1504  # offset
    m_vecAnchorVector = 1856  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_StopAfterCPDuration:
    m_bDestroyImmediately = 808  # offset
    m_bPlayEndCap = 809  # offset
    m_flDuration = 456  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_TeleportBeam:
    m_flAlpha = 496  # offset
    m_flArcMaxDuration = 484  # offset
    m_flArcSpeed = 492  # offset
    m_flSegmentBreak = 488  # offset
    m_nCPColor = 460  # offset
    m_nCPExtraArcData = 468  # offset
    m_nCPInvalidColor = 464  # offset
    m_nCPMisc = 456  # offset
    m_nCPPosition = 448  # offset
    m_nCPVelocity = 452  # offset
    m_vGravity = 472  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_TimeVaryingForce:
    m_EndingForce = 484  # offset
    m_StartingForce = 468  # offset
    m_flEndLerpTime = 480  # offset
    m_flStartLerpTime = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_TurbulenceForce:
    m_flNoiseCoordScale0 = 464  # offset
    m_flNoiseCoordScale1 = 468  # offset
    m_flNoiseCoordScale2 = 472  # offset
    m_flNoiseCoordScale3 = 476  # offset
    m_vecNoiseAmount0 = 480  # offset
    m_vecNoiseAmount1 = 492  # offset
    m_vecNoiseAmount2 = 504  # offset
    m_vecNoiseAmount3 = 516  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_TwistAroundAxis:
    m_TwistAxis = 468  # offset
    m_bLocalSpace = 480  # offset
    m_fForceAmount = 464  # offset
    m_nControlPointNumber = 484  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_UpdateLightSource:
    m_flBrightnessScale = 452  # offset
    m_flMaximumLightingRadius = 464  # offset
    m_flMinimumLightingRadius = 460  # offset
    m_flPositionDampingConstant = 468  # offset
    m_flRadiusScale = 456  # offset
    m_vColorTint = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_VectorFieldSnapshot:
    m_bLockToSurface = 2477  # offset
    m_bSetVelocity = 2476  # offset
    m_flBoundaryDampening = 2472  # offset
    m_flGridSpacing = 2480  # offset
    m_flInterpolation = 464  # offset
    m_nAttributeToWrite = 452  # offset
    m_nControlPointNumber = 448  # offset
    m_nLocalSpaceCP = 456  # offset
    m_vecScale = 816  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_VectorNoise:
    m_bAdditive = 480  # offset
    m_bOffset = 481  # offset
    m_fl4NoiseScale = 476  # offset
    m_flNoiseAnimationTimeScale = 484  # offset
    m_nFieldOutput = 448  # offset
    m_vecOutputMax = 464  # offset
    m_vecOutputMin = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_VelocityDecay:
    m_flMinVelocity = 448  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_VelocityMatchingForce:
    m_bUseAABB = 464  # offset
    m_flDirScale = 448  # offset
    m_flFacingStrength = 460  # offset
    m_flNeighborDistance = 456  # offset
    m_flSpdScale = 452  # offset
    m_nCPBroadcast = 468  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_WaterImpulseRenderer:
    m_bIsRadialWind = 3944  # offset
    m_flMagnitude = 2536  # offset
    m_flRadius = 2184  # offset
    m_flShape = 2888  # offset
    m_flWindSpeed = 3240  # offset
    m_flWobble = 3592  # offset
    m_nEventType = 3948  # offset
    m_vecPos = 528  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_WindForce:
    m_vForce = 464  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_WorldCollideConstraint:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class C_OP_WorldTraceConstraint:
    m_CollisionGroupName = 476  # offset
    m_bBrushOnly = 605  # offset
    m_bDecayBounce = 2040  # offset
    m_bIncludeWater = 606  # offset
    m_bKillonContact = 2041  # offset
    m_bSetNormal = 2048  # offset
    m_bWorldOnly = 604  # offset
    m_flBounceAmount = 984  # offset
    m_flCollisionConfirmationSpeed = 624  # offset
    m_flCpMovementTolerance = 612  # offset
    m_flMinSpeed = 2044  # offset
    m_flRadiusScale = 632  # offset
    m_flRandomDirScale = 1688  # offset
    m_flRetestRate = 616  # offset
    m_flSlideAmount = 1336  # offset
    m_flStopSpeed = 2056  # offset
    m_flTraceTolerance = 620  # offset
    m_nCP = 448  # offset
    m_nCollisionMode = 464  # offset
    m_nCollisionModeMin = 468  # offset
    m_nEntityStickDataField = 2408  # offset
    m_nEntityStickNormalField = 2412  # offset
    m_nIgnoreCP = 608  # offset
    m_nMaxTracesPerFrame = 628  # offset
    m_nStickOnCollisionField = 2052  # offset
    m_nTraceSet = 472  # offset
    m_vecCpOffset = 452  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CollisionGroupContext_t:
    m_nCollisionGroupNumber = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ControlPointReference_t:
    m_bOffsetInLocalSpace = 16  # offset
    m_controlPointNameString = 0  # offset
    m_vOffsetFromControlPoint = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FloatInputMaterialVariable_t:
    m_flInput = 8  # offset
    m_strVariable = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class IParticleCollection:
    pass

class IParticleSystemDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialVariable_t:
    m_flScale = 12  # offset
    m_nVariableField = 8  # offset
    m_strVariable = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ModelReference_t:
    m_flRelativeProbabilityOfSpawn = 8  # offset
    m_model = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticleAttributeIndex_t:
    m_Value = 0  # offset

class ParticleChildrenInfo_t:
    m_ChildRef = 0  # offset
    m_bDisableChild = 13  # offset
    m_bEndCap = 12  # offset
    m_flDelay = 8  # offset
    m_nDetailLevel = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticleControlPointConfiguration_t:
    m_drivers = 8  # offset
    m_name = 0  # offset
    m_previewState = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticleControlPointDriver_t:
    m_angOffset = 28  # offset
    m_attachmentName = 8  # offset
    m_entityName = 40  # offset
    m_iAttachType = 4  # offset
    m_iControlPoint = 0  # offset
    m_vecOffset = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticlePreviewBodyGroup_t:
    m_bodyGroupName = 0  # offset
    m_nValue = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticlePreviewState_t:
    m_bAnimationNonLooping = 84  # offset
    m_bShouldDrawAttachmentNames = 82  # offset
    m_bShouldDrawAttachments = 81  # offset
    m_bShouldDrawControlPointAxes = 83  # offset
    m_bShouldDrawHitboxes = 80  # offset
    m_flParticleSimulationRate = 76  # offset
    m_flPlaybackSpeed = 72  # offset
    m_groundType = 12  # offset
    m_hitboxSetName = 32  # offset
    m_materialGroupName = 40  # offset
    m_nFireParticleOnSequenceFrame = 24  # offset
    m_nModSpecificData = 8  # offset
    m_previewModel = 0  # offset
    m_sequenceName = 16  # offset
    m_vecBodyGroups = 48  # offset
    m_vecPreviewGravity = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PointDefinitionWithTimeValues_t:
    m_flTimeDuration = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PointDefinition_t:
    m_bLocalCoords = 4  # offset
    m_nControlPoint = 0  # offset
    m_vOffset = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RenderProjectedMaterial_t:
    m_hMaterial = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SequenceWeightedList_t:
    m_flRelativeWeight = 4  # offset
    m_nSequence = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class TextureControls_t:
    m_bClampUVs = 2465  # offset
    m_bRandomizeOffsets = 2464  # offset
    m_flDistortion = 2112  # offset
    m_flFinalTextureOffsetU = 704  # offset
    m_flFinalTextureOffsetV = 1056  # offset
    m_flFinalTextureScaleU = 0  # offset
    m_flFinalTextureScaleV = 352  # offset
    m_flFinalTextureUVRotation = 1408  # offset
    m_flZoomScale = 1760  # offset
    m_nPerParticleBlend = 2468  # offset
    m_nPerParticleDistortion = 2492  # offset
    m_nPerParticleOffsetU = 2476  # offset
    m_nPerParticleOffsetV = 2480  # offset
    m_nPerParticleRotation = 2484  # offset
    m_nPerParticleScale = 2472  # offset
    m_nPerParticleZoom = 2488  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class TextureGroup_t:
    m_Gradient = 16  # offset
    m_TextureControls = 408  # offset
    m_bEnabled = 0  # offset
    m_bReplaceTextureWithGradient = 1  # offset
    m_flTextureBlend = 56  # offset
    m_hTexture = 8  # offset
    m_nTextureBlendMode = 48  # offset
    m_nTextureChannels = 44  # offset
    m_nTextureType = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VecInputMaterialVariable_t:
    m_strVariable = 0  # offset
    m_vecInput = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]