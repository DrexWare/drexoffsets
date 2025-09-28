// dumped by shxdows dumper (csdump)
# dumped by shxdows dumper (csdump) 

from enum import Enum

class AimMatrixBlendMode(Enum):
    AimMatrixBlendMode_Additive = 1
    AimMatrixBlendMode_BoneMask = 3
    AimMatrixBlendMode_ModelSpaceAdditive = 2
    AimMatrixBlendMode_None = 0

class AnimNodeNetworkMode(Enum):
    ClientSimulate = 1
    ServerAuthoritative = 0

class AnimParamButton_t(Enum):
    ANIMPARAM_BUTTON_A = 5
    ANIMPARAM_BUTTON_B = 6
    ANIMPARAM_BUTTON_DPAD_DOWN = 3
    ANIMPARAM_BUTTON_DPAD_LEFT = 4
    ANIMPARAM_BUTTON_DPAD_RIGHT = 2
    ANIMPARAM_BUTTON_DPAD_UP = 1
    ANIMPARAM_BUTTON_LEFT_SHOULDER = 9
    ANIMPARAM_BUTTON_LTRIGGER = 11
    ANIMPARAM_BUTTON_NONE = 0
    ANIMPARAM_BUTTON_RIGHT_SHOULDER = 10
    ANIMPARAM_BUTTON_RTRIGGER = 12
    ANIMPARAM_BUTTON_X = 7
    ANIMPARAM_BUTTON_Y = 8

class AnimParamNetworkSetting(Enum):
    AlwaysNetwork = 1
    Auto = 0
    NeverNetwork = 2

class AnimParamType_t(Enum):
    ANIMPARAM_BOOL = 1
    ANIMPARAM_COUNT = 8
    ANIMPARAM_ENUM = 2
    ANIMPARAM_FLOAT = 4
    ANIMPARAM_GLOBALSYMBOL = 7
    ANIMPARAM_INT = 3
    ANIMPARAM_QUATERNION = 6
    ANIMPARAM_UNKNOWN = 0
    ANIMPARAM_VECTOR = 5

class AnimScriptType(Enum):
    ANIMSCRIPT_FUSE_GENERAL = 0
    ANIMSCRIPT_FUSE_STATEMACHINE = 1
    ANIMSCRIPT_TYPE_INVALID = -1

class AnimValueSource(Enum):
    AccelerationFrontBack = 23
    AccelerationHeading = 15
    AccelerationLeftRight = 22
    AccelerationSpeed = 16
    BoundaryRadius = 12
    FacingHeading = 4
    FingerCurl_Index = 29
    FingerCurl_Middle = 30
    FingerCurl_Pinky = 32
    FingerCurl_Ring = 31
    FingerCurl_Thumb = 28
    FingerSplay_Index_Middle = 34
    FingerSplay_Middle_Ring = 35
    FingerSplay_Ring_Pinky = 36
    FingerSplay_Thumb_Index = 33
    ForwardSpeed = 2
    GoalDistance = 21
    LookDistance = 8
    LookHeading = 5
    LookHeadingNormalized = 6
    LookPitch = 7
    MaxMoveSpeed = 27
    MoveHeading = 0
    MoveHeadingRelativeToLookHeading = 26
    MoveSpeed = 1
    Parameter = 9
    RootMotionSpeed = 24
    RootMotionTurnSpeed = 25
    SlopeAngle = 18
    SlopeHeading = 17
    SlopePitch = 19
    SlopeYaw = 20
    StrafeSpeed = 3
    TargetMoveHeading = 13
    TargetMoveSpeed = 14
    WayPointDistance = 11
    WayPointHeading = 10

class AnimVectorSource(Enum):
    Acceleration = 5
    FacingPosition = 1
    GoalPosition = 11
    LookDirection = 2
    LookTarget = 8
    LookTarget_WorldSpace = 9
    ManualTarget_WorldSpace = 13
    MoveDirection = 0
    RootMotionVelocity = 12
    SlopeNormal = 6
    SlopeNormal_WorldSpace = 7
    VectorParameter = 3
    WayPointDirection = 4
    WayPointPosition = 10

class AnimationProcessingType_t(Enum):
    ANIMATION_PROCESSING_CLIENT_INTERPOLATION = 3
    ANIMATION_PROCESSING_CLIENT_PREDICTION = 2
    ANIMATION_PROCESSING_CLIENT_RENDER = 4
    ANIMATION_PROCESSING_CLIENT_SIMULATION = 1
    ANIMATION_PROCESSING_MAX = 5
    ANIMATION_PROCESSING_SERVER_SIMULATION = 0

class AnimationSnapshotType_t(Enum):
    ANIMATION_SNAPSHOT_CLIENT_INTERPOLATION = 3
    ANIMATION_SNAPSHOT_CLIENT_PREDICTION = 2
    ANIMATION_SNAPSHOT_CLIENT_RENDER = 4
    ANIMATION_SNAPSHOT_CLIENT_SIMULATION = 1
    ANIMATION_SNAPSHOT_FINAL_COMPOSITE = 5
    ANIMATION_SNAPSHOT_MAX = 6
    ANIMATION_SNAPSHOT_SERVER_SIMULATION = 0

class BinaryNodeChildOption(Enum):
    Child1 = 0
    Child2 = 1

class BinaryNodeTiming(Enum):
    SyncChildren = 2
    UseChild1 = 0
    UseChild2 = 1

class Blend2DMode(Enum):
    Blend2DMode_Directional = 1
    Blend2DMode_General = 0

class BlendKeyType(Enum):
    BlendKey_Distance = 2
    BlendKey_RemainingDistance = 3
    BlendKey_UserValue = 0
    BlendKey_Velocity = 1

class BoneMaskBlendSpace(Enum):
    BlendSpace_Model = 1
    BlendSpace_Model_RotationOnly = 2
    BlendSpace_Model_TranslationOnly = 3
    BlendSpace_Parent = 0

class BoneTransformSpace_t(Enum):
    BoneTransformSpace_Invalid = -1
    BoneTransformSpace_Model = 1
    BoneTransformSpace_Parent = 0
    BoneTransformSpace_World = 2

class CAnimationGraphVisualizerPrimitiveType(Enum):
    ANIMATIONGRAPHVISUALIZERPRIMITIVETYPE_Axis = 4
    ANIMATIONGRAPHVISUALIZERPRIMITIVETYPE_Line = 2
    ANIMATIONGRAPHVISUALIZERPRIMITIVETYPE_Pie = 3
    ANIMATIONGRAPHVISUALIZERPRIMITIVETYPE_Sphere = 1
    ANIMATIONGRAPHVISUALIZERPRIMITIVETYPE_Text = 0

class CNmCurrentSyncEventNode__InfoType_t(Enum):
    IndexAndPercentage = 0
    IndexOnly = 1
    PercentageOnly = 2

class CNmEventRelevance_t(Enum):
    ClientAndServer = 2
    ClientOnly = 0
    ServerOnly = 1

class CNmFloatAngleMathNode__Operation_t(Enum):
    ClampTo180 = 0
    ClampTo360 = 1
    FlipHemisphere = 2
    FlipHemisphereNegate = 3

class CNmFloatComparisonNode__Comparison_t(Enum):
    GreaterThan = 3
    GreaterThanEqual = 0
    LessThan = 4
    LessThanEqual = 1
    NearEqual = 2

class CNmFloatMathNode__Operator_t(Enum):
    Abs = 5
    Add = 0
    Ceiling = 8
    Div = 3
    Floor = 7
    FractionalPart = 10
    IntegerPart = 9
    InverseFractionalPart = 11
    Mod = 4
    Mul = 2
    Negate = 6
    Sub = 1

class CNmIDComparisonNode__Comparison_t(Enum):
    DoesntMatch = 1
    Matches = 0

class CNmParticleEvent__Type_t(Enum):
    Create = 0
    Create_CFG = 1

class CNmRootMotionData__SamplingMode_t(Enum):
    Delta = 0
    WorldSpace = 1

class CNmRootMotionOverrideNode__OverrideFlags_t(Enum):
    AllowFacingPitch = 3
    AllowMoveX = 0
    AllowMoveY = 1
    AllowMoveZ = 2
    ListenForEvents = 4

class CNmSoundEvent__Position_t(Enum):
    EntityAttachment = 4
    EntityEyePos = 3
    EntityPos = 2
    None = 0
    World = 1

class CNmStateNode__TimedEvent_t__Comparison_t(Enum):
    GreaterThanEqual = 1
    LessThanEqual = 0

class CNmSyncEventIndexConditionNode__TriggerMode_t(Enum):
    ExactlyAtEventIndex = 0
    GreaterThanEqualToEventIndex = 1

class CNmTargetInfoNode__Info_t(Enum):
    AngleHorizontal = 0
    AngleVertical = 1
    DeltaOrientationX = 5
    DeltaOrientationY = 6
    DeltaOrientationZ = 7
    Distance = 2
    DistanceHorizontalOnly = 3
    DistanceVerticalOnly = 4

class CNmTimeConditionNode__ComparisonType_t(Enum):
    ElapsedTime = 2
    PercentageThroughState = 0
    PercentageThroughSyncEvent = 1

class CNmTimeConditionNode__Operator_t(Enum):
    GreaterThan = 2
    GreaterThanEqual = 3
    LessThan = 0
    LessThanEqual = 1

class CNmTransitionNode__TransitionOptions_t(Enum):
    ClampDuration = 1
    MatchSourceTime = 3
    MatchSyncEventID = 5
    MatchSyncEventIndex = 4
    MatchSyncEventPercentage = 6
    MatchTimeInSeconds = 8
    None = 0
    OffsetTimeInSeconds = 9
    PreferClosestSyncEventID = 7
    Synchronized = 2

class CNmVectorInfoNode__Info_t(Enum):
    AngleHorizontal = 4
    AngleVertical = 5
    Length = 3
    X = 0
    Y = 1
    Z = 2

class ChoiceBlendMethod(Enum):
    PerChoiceBlendTimes = 1
    SingleBlendTime = 0

class ChoiceChangeMethod(Enum):
    OnCycleEnd = 1
    OnReset = 0
    OnResetOrCycleEnd = 2

class ChoiceMethod(Enum):
    Iterate = 2
    IterateRandom = 3
    WeightedRandom = 0
    WeightedRandomNoRepeat = 1

class DampingSpeedFunction(Enum):
    AsymmetricSpring = 3
    Constant = 1
    NoDamping = 0
    Spring = 2

class EDemoBoneSelectionMode(Enum):
    CaptureAllBones = 0
    CaptureSelectedBones = 1

class EIKEndEffectorRotationFixUpMode(Enum):
    Count = 4
    LookAtTargetForward = 2
    MaintainParentOrientation = 3
    MatchTargetOrientation = 1
    None = 0

class EPulseGraphExecutionHistoryFlag(Enum):
    CURSOR_ADD_TAG = 1
    CURSOR_REMOVE_TAG = 2
    CURSOR_RETIRED = 4
    NO_FLAGS = 0
    REQUIREMENT_FAIL = 16
    REQUIREMENT_PASS = 8

class FacingMode(Enum):
    FacingMode_Invalid = 0
    FacingMode_LookTarget = 3
    FacingMode_Manual = 1
    FacingMode_ManualPosition = 4
    FacingMode_Path = 2

class FieldNetworkOption(Enum):
    Auto = 0
    ForceDisable = 2
    ForceEnable = 1

class FlexOpCode_t(Enum):
    FLEX_OP_2WAY_0 = 15
    FLEX_OP_2WAY_1 = 16
    FLEX_OP_ABS = 26
    FLEX_OP_ADD = 4
    FLEX_OP_CLOSE = 11
    FLEX_OP_COMBO = 18
    FLEX_OP_COMMA = 12
    FLEX_OP_CONST = 1
    FLEX_OP_COS = 25
    FLEX_OP_DIV = 7
    FLEX_OP_DME_LOWER_EYELID = 20
    FLEX_OP_DME_UPPER_EYELID = 21
    FLEX_OP_DOMINATE = 19
    FLEX_OP_EXP = 9
    FLEX_OP_FETCH1 = 2
    FLEX_OP_FETCH2 = 3
    FLEX_OP_MAX = 13
    FLEX_OP_MIN = 14
    FLEX_OP_MUL = 6
    FLEX_OP_NEG = 8
    FLEX_OP_NWAY = 17
    FLEX_OP_OPEN = 10
    FLEX_OP_REMAPVALCLAMPED = 23
    FLEX_OP_SIN = 24
    FLEX_OP_SQRT = 22
    FLEX_OP_SUB = 5

class FootFallTagFoot_t(Enum):
    FOOT1 = 0
    FOOT2 = 1
    FOOT3 = 2
    FOOT4 = 3
    FOOT5 = 4
    FOOT6 = 5
    FOOT7 = 6
    FOOT8 = 7

class FootLockSubVisualization(Enum):
    FOOTLOCKSUBVISUALIZATION_IKSolve = 1
    FOOTLOCKSUBVISUALIZATION_ReachabilityAnalysis = 0

class FootPinningTimingSource(Enum):
    FootMotion = 0
    Parameter = 2
    Tag = 1

class FootstepLandedFootSoundType_t(Enum):
    FOOTSOUND_Left = 0
    FOOTSOUND_Right = 1
    FOOTSOUND_UseOverrideSound = 2

class HandshakeTagType_t(Enum):
    eCount = 2
    eInvalid = -1
    eMovement = 1
    eTask = 0

class IKChannelMode(Enum):
    OneBone = 2
    OneBone_Translate = 3
    TwoBone = 0
    TwoBone_Translate = 1

class IKSolverType(Enum):
    IKSOLVER_CCD = 4
    IKSOLVER_COUNT = 5
    IKSOLVER_DogLeg3Bone = 3
    IKSOLVER_Fabrik = 2
    IKSOLVER_Perlin = 0
    IKSOLVER_TwoBone = 1

class IKTargetCoordinateSystem(Enum):
    IKTARGETCOORDINATESYSTEM_COUNT = 2
    IKTARGETCOORDINATESYSTEM_ModelSpace = 1
    IKTARGETCOORDINATESYSTEM_WorldSpace = 0

class IKTargetSource(Enum):
    IKTARGETSOURCE_AnimgraphParameter = 1
    IKTARGETSOURCE_Bone = 0
    IKTARGETSOURCE_COUNT = 2

class IkEndEffectorType(Enum):
    IkEndEffector_Attachment = 0
    IkEndEffector_Bone = 1

class IkTargetType(Enum):
    IkTarget_Attachment = 0
    IkTarget_Bone = 1
    IkTarget_Parameter_ModelSpace = 2
    IkTarget_Parameter_WorldSpace = 3

class JiggleBoneSimSpace(Enum):
    SimSpace_Local = 0
    SimSpace_Model = 1
    SimSpace_World = 2

class JumpCorrectionMethod(Enum):
    AddCorrectionDelta = 1
    ScaleMotion = 0

class LinearRootMotionBlendMode_t(Enum):
    LERP = 0
    NLERP = 1
    SLERP = 2

class MatterialAttributeTagType_t(Enum):
    MATERIAL_ATTRIBUTE_TAG_COLOR = 1
    MATERIAL_ATTRIBUTE_TAG_VALUE = 0

class MeshDrawPrimitiveFlags_t(Enum):
    MESH_DRAW_FLAGS_CAN_BATCH_WITH_DYNAMIC_SHADER_CONSTANTS = 64
    MESH_DRAW_FLAGS_DRAW_LAST = 128
    MESH_DRAW_FLAGS_NONE = 0
    MESH_DRAW_FLAGS_USE_COMPRESSED_NORMAL_TANGENT = 2
    MESH_DRAW_FLAGS_USE_COMPRESSED_PER_VERTEX_LIGHTING = 16
    MESH_DRAW_FLAGS_USE_SHADOW_FAST_PATH = 1
    MESH_DRAW_FLAGS_USE_UNCOMPRESSED_PER_VERTEX_LIGHTING = 32
    MESH_DRAW_INPUT_LAYOUT_IS_NOT_MATCHED_TO_MATERIAL = 8

class ModelBoneFlexComponent_t(Enum):
    MODEL_BONE_FLEX_INVALID = -1
    MODEL_BONE_FLEX_TX = 0
    MODEL_BONE_FLEX_TY = 1
    MODEL_BONE_FLEX_TZ = 2

class ModelConfigAttachmentType_t(Enum):
    MODEL_CONFIG_ATTACHMENT_BONEMERGE = 2
    MODEL_CONFIG_ATTACHMENT_BONE_OR_ATTACHMENT = 0
    MODEL_CONFIG_ATTACHMENT_COUNT = 3
    MODEL_CONFIG_ATTACHMENT_INVALID = -1
    MODEL_CONFIG_ATTACHMENT_ROOT_RELATIVE = 1

class ModelSkeletonData_t__BoneFlags_t(Enum):
    BLEND_PREALIGNED = 1048576
    FLAG_ALL_BONE_FLAGS = 1048575
    FLAG_ANIMATION = 64
    FLAG_ATTACHMENT = 32
    FLAG_BONEFLEXDRIVER = 4
    FLAG_BONE_MERGE_READ = 262144
    FLAG_BONE_MERGE_WRITE = 524288
    FLAG_BONE_USED_BY_VERTEX_LOD0 = 1024
    FLAG_BONE_USED_BY_VERTEX_LOD1 = 2048
    FLAG_BONE_USED_BY_VERTEX_LOD2 = 4096
    FLAG_BONE_USED_BY_VERTEX_LOD3 = 8192
    FLAG_BONE_USED_BY_VERTEX_LOD4 = 16384
    FLAG_BONE_USED_BY_VERTEX_LOD5 = 32768
    FLAG_BONE_USED_BY_VERTEX_LOD6 = 65536
    FLAG_BONE_USED_BY_VERTEX_LOD7 = 131072
    FLAG_CLOTH = 8
    FLAG_HITBOX = 256
    FLAG_MESH = 128
    FLAG_NO_BONE_FLAGS = 0
    FLAG_PHYSICS = 16
    FLAG_PROCEDURAL = 4194304
    FLAG_RIGIDLENGTH = 2097152

class MoodType_t(Enum):
    eMoodType_Body = 1
    eMoodType_Head = 0

class MorphBundleType_t(Enum):
    MORPH_BUNDLE_TYPE_COUNT = 3
    MORPH_BUNDLE_TYPE_NONE = 0
    MORPH_BUNDLE_TYPE_NORMAL_WRINKLE = 2
    MORPH_BUNDLE_TYPE_POSITION_SPEED = 1

class MorphFlexControllerRemapType_t(Enum):
    MORPH_FLEXCONTROLLER_REMAP_2WAY = 1
    MORPH_FLEXCONTROLLER_REMAP_EYELID = 3
    MORPH_FLEXCONTROLLER_REMAP_NWAY = 2
    MORPH_FLEXCONTROLLER_REMAP_PASSTHRU = 0

class NPCPhysicsHullType_t(Enum):
    eCenteredCapsule = 2
    eGenericCapsule = 3
    eGroundBox = 4
    eGroundCapsule = 1
    eInvalid = 0

class NmCachedValueMode_t(Enum):
    OnEntry = 0
    OnExit = 1

class NmEasingFunction_t(Enum):
    Back = 8
    Circ = 7
    Cubic = 2
    Expo = 6
    Linear = 0
    Quad = 1
    Quart = 3
    Quint = 4
    Sine = 5

class NmEasingOperation_t(Enum):
    InCirc = 19
    InCubic = 4
    InExpo = 16
    InOutCirc = 21
    InOutCubic = 6
    InOutExpo = 18
    InOutQuad = 3
    InOutQuart = 9
    InOutQuint = 12
    InOutSine = 15
    InQuad = 1
    InQuart = 7
    InQuint = 10
    InSine = 13
    Linear = 0
    None = 22
    OutCirc = 20
    OutCubic = 5
    OutExpo = 17
    OutQuad = 2
    OutQuart = 8
    OutQuint = 11
    OutSine = 14

class NmEventConditionRules_t(Enum):
    IgnoreInactiveEvents = 1
    LimitSearchToSourceState = 0
    OperatorAnd = 5
    OperatorOr = 4
    PreferHighestProgress = 3
    PreferHighestWeight = 2
    SearchBothGraphAndAnimEvents = 8
    SearchOnlyAnimEvents = 7
    SearchOnlyGraphEvents = 6

class NmFollowBoneMode_t(Enum):
    RotationAndTranslation = 0
    RotationOnly = 1
    TranslationOnly = 2

class NmFootPhaseCondition_t(Enum):
    LeftFootDown = 0
    LeftFootPassing = 1
    LeftPhase = 4
    RightFootDown = 2
    RightFootPassing = 3
    RightPhase = 5

class NmFootPhase_t(Enum):
    LeftFootDown = 0
    LeftFootPassing = 3
    RightFootDown = 2
    RightFootPassing = 1

class NmFrameSnapEventMode_t(Enum):
    Floor = 0
    Round = 1

class NmGraphEventTypeCondition_t(Enum):
    Any = 5
    Entry = 0
    Exit = 2
    FullyInState = 1
    Generic = 4
    Timed = 3

class NmGraphValueType_t(Enum):
    BoneMask = 6
    Bool = 1
    Float = 3
    ID = 2
    Pose = 7
    Special = 8
    Target = 5
    Unknown = 0
    Vector = 4

class NmIKBlendMode_t(Enum):
    Effector = 0
    Pose = 1

class NmPoseBlendMode_t(Enum):
    Additive = 1
    ModelSpace = 2
    Overlay = 0

class NmRootMotionBlendMode_t(Enum):
    Additive = 1
    Blend = 0
    IgnoreSource = 2
    IgnoreTarget = 3

class NmTargetWarpAlgorithm_t(Enum):
    Bezier = 3
    Hermite = 1
    HermiteFeaturePreserving = 2
    Lerp = 0

class NmTargetWarpRule_t(Enum):
    RotationOnly = 3
    WarpXY = 0
    WarpXYZ = 2
    WarpZ = 1

class NmTransitionRuleCondition_t(Enum):
    AnyAllowed = 0
    Blocked = 3
    ConditionallyAllowed = 2
    FullyAllowed = 1

class NmTransitionRule_t(Enum):
    AllowTransition = 0
    BlockTransition = 2
    ConditionallyAllowTransition = 1

class OrientationWarpMode_t(Enum):
    eAngle = 1
    eInvalid = 0
    eWorldPosition = 2

class OrientationWarpRootMotionSource_t(Enum):
    eAnimationOnly = 1
    eAnimationOrProcedural = 0
    eProceduralOnly = 2

class OrientationWarpTargetOffsetMode_t(Enum):
    eAnimationMovementHeading = 2
    eAnimationMovementHeadingAtEnd = 3
    eLiteralValue = 0
    eParameter = 1

class PFNoiseModifier_t(Enum):
    PF_NOISE_MODIFIER_CLUMPS = 2
    PF_NOISE_MODIFIER_LINES = 1
    PF_NOISE_MODIFIER_NONE = 0
    PF_NOISE_MODIFIER_RINGS = 3

class PFNoiseTurbulence_t(Enum):
    PF_NOISE_TURB_ALTERNATE = 5
    PF_NOISE_TURB_CONTRAST = 4
    PF_NOISE_TURB_FEEDBACK = 2
    PF_NOISE_TURB_HIGHLIGHT = 1
    PF_NOISE_TURB_LOOPY = 3
    PF_NOISE_TURB_NONE = 0

class PFNoiseType_t(Enum):
    PF_NOISE_TYPE_CURL = 3
    PF_NOISE_TYPE_PERLIN = 0
    PF_NOISE_TYPE_SIMPLEX = 1
    PF_NOISE_TYPE_WORLEY = 2

class ParticleAttachment_t(Enum):
    MAX_PATTACH_TYPES = 16
    PATTACH_ABSORIGIN = 0
    PATTACH_ABSORIGIN_FOLLOW = 1
    PATTACH_CENTER_FOLLOW = 13
    PATTACH_CUSTOMORIGIN = 2
    PATTACH_CUSTOMORIGIN_FOLLOW = 3
    PATTACH_CUSTOM_GAME_STATE_1 = 14
    PATTACH_EYES_FOLLOW = 6
    PATTACH_HEALTHBAR = 15
    PATTACH_INVALID = -1
    PATTACH_MAIN_VIEW = 11
    PATTACH_OVERHEAD_FOLLOW = 7
    PATTACH_POINT = 4
    PATTACH_POINT_FOLLOW = 5
    PATTACH_RENDERORIGIN_FOLLOW = 10
    PATTACH_ROOTBONE_FOLLOW = 9
    PATTACH_WATERWAKE = 12
    PATTACH_WORLDORIGIN = 8

class ParticleFloatBiasType_t(Enum):
    PF_BIAS_TYPE_COUNT = 3
    PF_BIAS_TYPE_EXPONENTIAL = 2
    PF_BIAS_TYPE_GAIN = 1
    PF_BIAS_TYPE_INVALID = -1
    PF_BIAS_TYPE_STANDARD = 0

class ParticleFloatInputMode_t(Enum):
    PF_INPUT_MODE_CLAMPED = 0
    PF_INPUT_MODE_COUNT = 2
    PF_INPUT_MODE_INVALID = -1
    PF_INPUT_MODE_LOOPED = 1

class ParticleFloatMapType_t(Enum):
    PF_MAP_TYPE_COUNT = 7
    PF_MAP_TYPE_CURVE = 4
    PF_MAP_TYPE_DIRECT = 0
    PF_MAP_TYPE_INVALID = -1
    PF_MAP_TYPE_MULT = 1
    PF_MAP_TYPE_NOTCHED = 5
    PF_MAP_TYPE_REMAP = 2
    PF_MAP_TYPE_REMAP_BIASED = 3
    PF_MAP_TYPE_ROUND = 6

class ParticleFloatRandomMode_t(Enum):
    PF_RANDOM_MODE_CONSTANT = 0
    PF_RANDOM_MODE_COUNT = 2
    PF_RANDOM_MODE_INVALID = -1
    PF_RANDOM_MODE_VARYING = 1

class ParticleFloatRoundType_t(Enum):
    PF_ROUND_TYPE_CEIL = 2
    PF_ROUND_TYPE_COUNT = 3
    PF_ROUND_TYPE_FLOOR = 1
    PF_ROUND_TYPE_INVALID = -1
    PF_ROUND_TYPE_NEAREST = 0

class ParticleFloatType_t(Enum):
    PF_TYPE_CLOSEST_CAMERA_DISTANCE = 11
    PF_TYPE_COLLECTION_AGE = 4
    PF_TYPE_CONCURRENT_DEF_COUNT = 10
    PF_TYPE_CONTROL_POINT_CHANGE_AGE = 7
    PF_TYPE_CONTROL_POINT_COMPONENT = 6
    PF_TYPE_CONTROL_POINT_SPEED = 8
    PF_TYPE_COUNT = 29
    PF_TYPE_ENDCAP_AGE = 5
    PF_TYPE_INVALID = -1
    PF_TYPE_LITERAL = 0
    PF_TYPE_NAMED_VALUE = 1
    PF_TYPE_PARTICLE_AGE = 16
    PF_TYPE_PARTICLE_AGE_NORMALIZED = 17
    PF_TYPE_PARTICLE_DETAIL_LEVEL = 9
    PF_TYPE_PARTICLE_FLOAT = 18
    PF_TYPE_PARTICLE_INITIAL_FLOAT = 19
    PF_TYPE_PARTICLE_INITIAL_VECTOR_COMPONENT = 21
    PF_TYPE_PARTICLE_NOISE = 15
    PF_TYPE_PARTICLE_NUMBER = 23
    PF_TYPE_PARTICLE_NUMBER_NORMALIZED = 24
    PF_TYPE_PARTICLE_ROPE_SEGMENT = 25
    PF_TYPE_PARTICLE_ROPE_SEGMENT_NORMALIZED = 26
    PF_TYPE_PARTICLE_SCREENSPACE_CAMERA_DISTANCE = 27
    PF_TYPE_PARTICLE_SCREENSPACE_CAMERA_DOT_PRODUCT = 28
    PF_TYPE_PARTICLE_SPEED = 22
    PF_TYPE_PARTICLE_VECTOR_COMPONENT = 20
    PF_TYPE_RANDOM_BIASED = 3
    PF_TYPE_RANDOM_UNIFORM = 2
    PF_TYPE_RENDERER_CAMERA_DISTANCE = 13
    PF_TYPE_RENDERER_CAMERA_DOT_PRODUCT = 14
    PF_TYPE_SNAPSHOT_COUNT = 12

class ParticleModelType_t(Enum):
    PM_TYPE_CONTROL_POINT = 3
    PM_TYPE_COUNT = 4
    PM_TYPE_INVALID = 0
    PM_TYPE_NAMED_VALUE_EHANDLE = 2
    PM_TYPE_NAMED_VALUE_MODEL = 1

class ParticleTransformType_t(Enum):
    PT_TYPE_CONTROL_POINT = 2
    PT_TYPE_CONTROL_POINT_RANGE = 3
    PT_TYPE_COUNT = 4
    PT_TYPE_INVALID = 0
    PT_TYPE_NAMED_VALUE = 1

class ParticleVecType_t(Enum):
    PVEC_TYPE_CLOSEST_CAMERA_POSITION = 17
    PVEC_TYPE_COUNT = 18
    PVEC_TYPE_CP_DELTA = 16
    PVEC_TYPE_CP_RELATIVE_DIR = 8
    PVEC_TYPE_CP_RELATIVE_POSITION = 7
    PVEC_TYPE_CP_RELATIVE_RANDOM_DIR = 9
    PVEC_TYPE_CP_VALUE = 6
    PVEC_TYPE_FLOAT_COMPONENTS = 10
    PVEC_TYPE_FLOAT_INTERP_CLAMPED = 11
    PVEC_TYPE_FLOAT_INTERP_GRADIENT = 13
    PVEC_TYPE_FLOAT_INTERP_OPEN = 12
    PVEC_TYPE_INVALID = -1
    PVEC_TYPE_LITERAL = 0
    PVEC_TYPE_LITERAL_COLOR = 1
    PVEC_TYPE_NAMED_VALUE = 2
    PVEC_TYPE_PARTICLE_INITIAL_VECTOR = 4
    PVEC_TYPE_PARTICLE_VECTOR = 3
    PVEC_TYPE_PARTICLE_VELOCITY = 5
    PVEC_TYPE_RANDOM_UNIFORM = 14
    PVEC_TYPE_RANDOM_UNIFORM_OFFSET = 15

class PermModelInfo_t__FlagEnum(Enum):
    FLAG_ANIMATION_DRIVEN_FLEXES = 2097152
    FLAG_DO_NOT_CAST_SHADOWS = 131072
    FLAG_FORCE_PHONEME_CROSSFADE = 4096
    FLAG_HAS_SKINNED_MESHES = 1024
    FLAG_IMPLICIT_BIND_POSE_SEQUENCE = 4194304
    FLAG_MODEL_DOC = 8388608
    FLAG_MODEL_IS_RUNTIME_COMBINED = 4
    FLAG_MODEL_PART_CHILD = 16
    FLAG_NAV_GEN_HULL = 64
    FLAG_NAV_GEN_NONE = 32
    FLAG_NO_ANIM_EVENTS = 1048576
    FLAG_NO_FORCED_FADE = 2048
    FLAG_SOURCE1_IMPORT = 8
    FLAG_TRANSLUCENT = 1
    FLAG_TRANSLUCENT_TWO_PASS = 2

class PoseType_t(Enum):
    POSETYPE_DYNAMIC = 1
    POSETYPE_INVALID = 255
    POSETYPE_STATIC = 0

class PulseApiFeature_t(Enum):
    AF_ENTITIES = 1
    AF_FAKE_ENTITIES = 16
    AF_NONE = 0
    AF_PANORAMA = 2
    AF_PARTICLES = 8
    AF_SELECTORS_WITHOUT_REQUIREMENTS = 32

class PulseCursorExecResult_t(Enum):
    Canceled = 1
    Failed = 2
    OngoingNotify = 3
    Succeeded = 0

class PulseDomainValueType_t(Enum):
    COUNT = 2
    ENTITY_NAME = 0
    INVALID = -1
    PANEL_ID = 1

class PulseInstructionCode_t(Enum):
    ADD = 25
    ADD_FLOAT = 50
    ADD_FLOAT_GAMETIME = 58
    ADD_GAMETIME_FLOAT = 57
    ADD_INT = 49
    ADD_STRING = 51
    ADD_VEC2 = 52
    ADD_VEC3 = 53
    ADD_VEC3WS_VEC3 = 54
    ADD_VEC3_VEC3WS = 55
    ADD_VEC4 = 56
    AND = 34
    CELL_INVOKE = 11
    CHUNK_LEAP = 7
    CHUNK_LEAP_COND = 8
    CONVERT_VALUE = 39
    COPY = 22
    DETACH_REGISTER = 16
    DIV = 28
    DIV_FLOAT = 70
    ELEMENT_ACCESS = 38
    ELEMENT_ACCESS_COLOR_RGB = 123
    ELEMENT_ACCESS_VEC2 = 119
    ELEMENT_ACCESS_VEC3 = 120
    ELEMENT_ACCESS_VEC3WS = 121
    ELEMENT_ACCESS_VEC4 = 122
    EQ = 32
    EQ_ARRAY = 94
    EQ_BOOL = 79
    EQ_COLOR_RGB = 93
    EQ_EHANDLE = 89
    EQ_ENTITY_NAME = 87
    EQ_FLOAT = 81
    EQ_GAMETIME = 95
    EQ_INT = 80
    EQ_OPAQUE_HANDLE = 91
    EQ_PANEL_HANDLE = 90
    EQ_SCHEMA_ENUM = 88
    EQ_STRING = 86
    EQ_TEST_HANDLE = 92
    EQ_VEC2 = 82
    EQ_VEC3 = 83
    EQ_VEC3WS = 84
    EQ_VEC4 = 85
    GET_ARRAY_ELEMENT = 20
    GET_BLACKBOARD_REFERENCE = 41
    GET_CONST = 19
    GET_CONST_INLINE_STORAGE = 124
    GET_DOMAIN_VALUE = 21
    GET_VAR = 14
    GET_VAR_DETACH = 15
    IMMEDIATE_HALT = 1
    INVALID = 0
    JUMP = 5
    JUMP_COND = 6
    LAST_SERIALIZED_CODE = 43
    LIBRARY_INVOKE = 12
    LT = 30
    LTE = 31
    LTE_FLOAT = 77
    LTE_GAMETIME = 78
    LTE_INT = 76
    LT_FLOAT = 74
    LT_GAMETIME = 75
    LT_INT = 73
    MOD = 29
    MOD_FLOAT = 72
    MOD_INT = 71
    MUL = 27
    MUL_FLOAT = 69
    MUL_INT = 68
    NE = 33
    NEGATE = 24
    NEGATE_FLOAT = 45
    NEGATE_INT = 44
    NEGATE_VEC2 = 46
    NEGATE_VEC3 = 47
    NEGATE_VEC4 = 48
    NE_ARRAY = 111
    NE_BOOL = 96
    NE_COLOR_RGB = 110
    NE_EHANDLE = 106
    NE_ENTITY_NAME = 104
    NE_FLOAT = 98
    NE_GAMETIME = 112
    NE_INT = 97
    NE_OPAQUE_HANDLE = 108
    NE_PANEL_HANDLE = 107
    NE_SCHEMA_ENUM = 105
    NE_STRING = 103
    NE_TEST_HANDLE = 109
    NE_VEC2 = 99
    NE_VEC3 = 100
    NE_VEC3WS = 101
    NE_VEC4 = 102
    NOP = 4
    NOT = 23
    OR = 35
    PULSE_CALL_ASYNC_FIRE = 10
    PULSE_CALL_SYNC = 9
    REINTERPRET_INSTANCE = 40
    RETURN_VALUE = 3
    RETURN_VOID = 2
    SCALE = 36
    SCALE_INV = 37
    SCALE_INV_VEC2 = 117
    SCALE_INV_VEC3 = 116
    SCALE_INV_VEC4 = 118
    SCALE_VEC2 = 114
    SCALE_VEC3 = 113
    SCALE_VEC4 = 115
    SET_BLACKBOARD_REFERENCE = 42
    SET_VAR = 13
    SET_VAR_ARRAY_ELEMENT_1D = 17
    SET_VAR_OBSERVABLE = 18
    SUB = 26
    SUB_FLOAT = 60
    SUB_GAMETIME = 67
    SUB_GAMETIME_FLOAT = 66
    SUB_INT = 59
    SUB_VEC2 = 61
    SUB_VEC3 = 62
    SUB_VEC3WS_VEC3 = 63
    SUB_VEC3WS_VEC3WS = 64
    SUB_VEC4 = 65

class PulseValueType_t(Enum):
    PVAL_ARRAY = 28
    PVAL_BOOL = 0
    PVAL_COLOR_RGB = 11
    PVAL_COUNT = 30
    PVAL_CURSOR_FLOW = 22
    PVAL_EHANDLE = 13
    PVAL_ENTITY_NAME = 18
    PVAL_FLOAT = 2
    PVAL_GAMETIME = 12
    PVAL_INT = 1
    PVAL_MODEL_MATERIAL_GROUP = 21
    PVAL_OPAQUE_HANDLE = 19
    PVAL_PANORAMA_PANEL_HANDLE = 26
    PVAL_QANGLE = 6
    PVAL_RESOURCE = 14
    PVAL_RESOURCE_NAME = 15
    PVAL_SCHEMA_ENUM = 25
    PVAL_SNDEVT_GUID = 16
    PVAL_SNDEVT_NAME = 17
    PVAL_STRING = 3
    PVAL_TEST_HANDLE = 27
    PVAL_TRANSFORM = 9
    PVAL_TRANSFORM_WORLDSPACE = 10
    PVAL_TYPESAFE_INT = 20
    PVAL_TYPESAFE_INT64 = 29
    PVAL_UNKNOWN = 24
    PVAL_VARIANT = 23
    PVAL_VEC2 = 4
    PVAL_VEC3 = 5
    PVAL_VEC3_WORLDSPACE = 7
    PVAL_VEC4 = 8
    PVAL_VOID = -1

class PulseVariableKeysSource_t(Enum):
    COUNT = 5
    CPP = 1
    PRIVATE = 0
    VMAP = 2
    VMDL = 3
    XML = 4

class RagdollPoseControl(Enum):
    Absolute = 0

class RenderMeshSlotType_t(Enum):
    RENDERMESH_SLOT_INVALID = -1
    RENDERMESH_SLOT_PER_INSTANCE = 1
    RENDERMESH_SLOT_PER_VERTEX = 0

class ResetCycleOption(Enum):
    Beginning = 0
    FixedValue = 3
    InverseSourceCycle = 2
    SameCycleAsSource = 1
    SameTimeAsSource = 4

class ScriptedHeldWeaponBehavior_t(Enum):
    eDeploy = 1
    eDrop = 2
    eHolster = 0
    eInvalid = -1

class ScriptedMoveTo_t(Enum):
    eMoveWithGait = 3
    eObsoleteBackCompat1 = 1
    eObsoleteBackCompat2 = 2
    eTeleport = 4
    eWait = 0
    eWaitFacing = 5

class SelectorTagBehavior_t(Enum):
    SelectorTagBehavior_OffBeforeFinished = 2
    SelectorTagBehavior_OffWhenFinished = 1
    SelectorTagBehavior_OnWhileCurrent = 0

class SeqCmd_t(Enum):
    SeqCmd_Add = 4
    SeqCmd_Blend = 8
    SeqCmd_Copy = 7
    SeqCmd_FetchCycle = 11
    SeqCmd_FetchFrame = 12
    SeqCmd_FetchFrameRange = 2
    SeqCmd_IKLockInPlace = 13
    SeqCmd_IKRestoreAll = 14
    SeqCmd_LinearDelta = 1
    SeqCmd_Nop = 0
    SeqCmd_ReverseSequence = 15
    SeqCmd_Scale = 6
    SeqCmd_Sequence = 10
    SeqCmd_Slerp = 3
    SeqCmd_Subtract = 5
    SeqCmd_Transform = 16
    SeqCmd_Worldspace = 9

class SeqPoseSetting_t(Enum):
    SEQ_POSE_SETTING_CONSTANT = 0
    SEQ_POSE_SETTING_POSITION = 2
    SEQ_POSE_SETTING_ROTATION = 1
    SEQ_POSE_SETTING_VELOCITY = 3

class SharedMovementGait_t(Enum):
    eCount = 4
    eFast = 2
    eInvalid = -1
    eMedium = 1
    eSlow = 0
    eVeryFast = 3

class SolveIKChainAnimNodeDebugSetting(Enum):
    SOLVEIKCHAINANIMNODEDEBUGSETTING_Forward = 4
    SOLVEIKCHAINANIMNODEDEBUGSETTING_Left = 6
    SOLVEIKCHAINANIMNODEDEBUGSETTING_None = 0
    SOLVEIKCHAINANIMNODEDEBUGSETTING_Up = 5
    SOLVEIKCHAINANIMNODEDEBUGSETTING_X_Axis_Circle = 1
    SOLVEIKCHAINANIMNODEDEBUGSETTING_Y_Axis_Circle = 2
    SOLVEIKCHAINANIMNODEDEBUGSETTING_Z_Axis_Circle = 3

class StanceOverrideMode(Enum):
    Node = 1
    Sequence = 0

class StateActionBehavior(Enum):
    STATETAGBEHAVIOR_ACTIVE_WHILE_CURRENT = 0
    STATETAGBEHAVIOR_ACTIVE_WHILE_FULLY_BLENDED = 4
    STATETAGBEHAVIOR_FIRE_ON_ENTER = 1
    STATETAGBEHAVIOR_FIRE_ON_ENTER_AND_EXIT = 3
    STATETAGBEHAVIOR_FIRE_ON_EXIT = 2

class StepPhase(Enum):
    StepPhase_InAir = 1
    StepPhase_OnGround = 0

class TargetSelectorAngleMode_t(Enum):
    eFacingHeading = 0
    eMoveHeading = 1

class TargetWarpAngleMode_t(Enum):
    eFacingHeading = 0
    eMoveHeading = 1

class TargetWarpCorrectionMethod(Enum):
    AddCorrectionDelta = 1
    ScaleMotion = 0

class TargetWarpTimingMethod(Enum):
    ReachDestinationOnRootMotionEnd = 0
    ReachDestinationOnWarpTagEnd = 1

class VPhysXAggregateData_t__VPhysXFlagEnum_t(Enum):
    FLAG_IGNORE_SCALE_OBSOLETE_DO_NOT_USE = 32
    FLAG_IS_POLYSOUP_GEOMETRY = 1
    FLAG_LEVEL_COLLISION = 16

class VPhysXBodyPart_t__VPhysXFlagEnum_t(Enum):
    FLAG_ALWAYS_DYNAMIC_ON_CLIENT = 16
    FLAG_DISABLE_CCD = 32
    FLAG_JOINT = 4
    FLAG_KINEMATIC = 2
    FLAG_MASS = 8
    FLAG_STATIC = 1

class VPhysXConstraintParams_t__EnumFlags0_t(Enum):
    FLAG0_SHIFT_BREAKABLE_FORCE = 2
    FLAG0_SHIFT_BREAKABLE_TORQUE = 3
    FLAG0_SHIFT_CONSTRAIN = 1
    FLAG0_SHIFT_INTERPENETRATE = 0

class VPhysXJoint_t__Flags_t(Enum):
    JOINT_FLAGS_BODY1_FIXED = 1
    JOINT_FLAGS_NONE = 0
    JOINT_FLAGS_USE_BLOCK_SOLVER = 2

class VelocityMetricMode(Enum):
    DirectionAndMagnitude = 2
    DirectionOnly = 0
    MagnitudeOnly = 1

class AimCameraOpFixedSettings_t:
    m_nCameraJointIndex = 4  # offset
    m_nChainIndex = 0  # offset
    m_nClavicleLeftJointIndex = 12  # offset
    m_nClavicleRightJointIndex = 16  # offset
    m_nDepenetrationJointIndex = 20  # offset
    m_nPelvisJointIndex = 8  # offset
    m_propJoints = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AimMatrixOpFixedSettings_t:
    m_attachment = 0  # offset
    m_bTargetIsPosition = 212  # offset
    m_bUseBiasAndClamp = 213  # offset
    m_biasAndClampBlendCurve = 224  # offset
    m_damping = 128  # offset
    m_eBlendMode = 192  # offset
    m_flBiasAndClampPitchOffset = 220  # offset
    m_flBiasAndClampYawOffset = 216  # offset
    m_flMaxPitchAngle = 200  # offset
    m_flMaxYawAngle = 196  # offset
    m_nBoneMaskIndex = 208  # offset
    m_nSequenceMaxFrame = 204  # offset
    m_poseCacheHandles = 152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimComponentID:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimNodeID:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimNodeOutputID:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimParamID:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimScriptHandle:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimStateID:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimTagID:
    m_id = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimationDecodeDebugDumpElement_t:
    m_decodeOps = 40  # offset
    m_decodedAnims = 88  # offset
    m_internalOps = 64  # offset
    m_modelName = 8  # offset
    m_nEntityIndex = 0  # offset
    m_poseParams = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimationDecodeDebugDump_t:
    m_elems = 8  # offset
    m_processingType = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimationSnapshotBase_t:
    m_DecodeDump = 152  # offset
    m_SnapshotType = 144  # offset
    m_bBonesInWorldSpace = 64  # offset
    m_bHasDecodeDump = 148  # offset
    m_boneSetupMask = 72  # offset
    m_boneTransforms = 96  # offset
    m_flRealTime = 0  # offset
    m_flexControllers = 120  # offset
    m_rootToWorld = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AnimationSnapshot_t:
    m_modelName = 280  # offset
    m_nEntIndex = 272  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AttachmentHandle_t:
    m_Value = 0  # offset

class BlendItem_t:
    m_bUseCustomDuration = 56  # offset
    m_flDuration = 52  # offset
    m_hSequence = 40  # offset
    m_pChild = 24  # offset
    m_tags = 0  # offset
    m_vPos = 44  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class BoneDemoCaptureSettings_t:
    m_boneName = 0  # offset
    m_flErrorQuantizationRotationMax = 20  # offset
    m_flErrorQuantizationScaleMax = 28  # offset
    m_flErrorQuantizationTranslationMax = 24  # offset
    m_flErrorSplineRotationMax = 8  # offset
    m_flErrorSplineScaleMax = 16  # offset
    m_flErrorSplineTranslationMax = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CActionComponentUpdater:
    m_actions = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAddUpdateNode:
    m_bApplyChannelsSeparately = 153  # offset
    m_bApplyScale = 155  # offset
    m_bApplyToFootMotion = 152  # offset
    m_bUseModelSpace = 154  # offset
    m_footMotionTiming = 148  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAimCameraUpdateNode:
    m_hParameterCameraClearanceDistance = 128  # offset
    m_hParameterCameraOnly = 122  # offset
    m_hParameterOrientation = 114  # offset
    m_hParameterPelvisOffset = 118  # offset
    m_hParameterPosition = 112  # offset
    m_hParameterSpineRotationWeight = 116  # offset
    m_hParameterUseIK = 120  # offset
    m_hParameterWeaponDepenetrationDelta = 126  # offset
    m_hParameterWeaponDepenetrationDistance = 124  # offset
    m_opFixedSettings = 136  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAimConstraint:
    m_nUpType = 112  # offset
    m_qAimOffset = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAimMatrixUpdateNode:
    m_bLockWhenWaning = 373  # offset
    m_bResetChild = 372  # offset
    m_hSequence = 368  # offset
    m_opFixedSettings = 112  # offset
    m_paramIndex = 364  # offset
    m_target = 360  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimActionUpdater:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimActivity:
    m_nActivity = 16  # offset
    m_nFlags = 20  # offset
    m_nWeight = 24  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimAttachment:
    m_influenceIndices = 96  # offset
    m_influenceOffsets = 48  # offset
    m_influenceRotations = 0  # offset
    m_influenceWeights = 108  # offset
    m_numInfluences = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimBone:
    m_flags = 68  # offset
    m_name = 0  # offset
    m_parent = 16  # offset
    m_pos = 20  # offset
    m_qAlignment = 52  # offset
    m_quat = 32  # offset
    m_scale = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimBoneDifference:
    m_bHasMovement = 45  # offset
    m_bHasRotation = 44  # offset
    m_name = 0  # offset
    m_parent = 16  # offset
    m_posError = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimComponentUpdater:
    m_bStartEnabled = 40  # offset
    m_id = 32  # offset
    m_name = 24  # offset
    m_networkMode = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimCycle:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimData:
    m_animArray = 32  # offset
    m_decoderArray = 56  # offset
    m_nMaxUniqueFrameIndex = 80  # offset
    m_name = 16  # offset
    m_segmentArray = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimDataChannelDesc:
    m_nElementIndexArray = 96  # offset
    m_nElementMaskArray = 120  # offset
    m_nFlags = 32  # offset
    m_nType = 36  # offset
    m_szChannelClass = 0  # offset
    m_szDescription = 56  # offset
    m_szElementNameArray = 72  # offset
    m_szGrouping = 40  # offset
    m_szVariableName = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimDecoder:
    m_nType = 20  # offset
    m_nVersion = 16  # offset
    m_szName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimDemoCaptureSettings:
    m_baseSequence = 64  # offset
    m_boneSelectionMode = 76  # offset
    m_bones = 80  # offset
    m_flIkRotation_MaxQuantizationError = 56  # offset
    m_flIkRotation_MaxSplineError = 24  # offset
    m_flIkTranslation_MaxQuantizationError = 60  # offset
    m_flIkTranslation_MaxSplineError = 28  # offset
    m_ikChains = 104  # offset
    m_nBaseSequenceFrame = 72  # offset
    m_vecErrorRangeQuantizationRotation = 32  # offset
    m_vecErrorRangeQuantizationScale = 48  # offset
    m_vecErrorRangeQuantizationTranslation = 40  # offset
    m_vecErrorRangeSplineRotation = 0  # offset
    m_vecErrorRangeSplineScale = 16  # offset
    m_vecErrorRangeSplineTranslation = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimDesc:
    fps = 24  # offset
    framestalltime = 376  # offset
    m_Data = 32  # offset
    m_activityArray = 328  # offset
    m_eventArray = 304  # offset
    m_flags = 16  # offset
    m_hierarchyArray = 352  # offset
    m_movementArray = 248  # offset
    m_name = 0  # offset
    m_sequenceParams = 456  # offset
    m_vecBoneWorldMax = 432  # offset
    m_vecBoneWorldMin = 408  # offset
    m_vecRootMax = 392  # offset
    m_vecRootMin = 380  # offset
    m_xInitialOffset = 272  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimDesc_Flag:
    m_bAllZeros = 1  # offset
    m_bAnimGraphAdditive = 7  # offset
    m_bDelta = 3  # offset
    m_bHidden = 2  # offset
    m_bImplicitSeqIgnoreDelta = 6  # offset
    m_bLegacyWorldspace = 4  # offset
    m_bLooping = 0  # offset
    m_bModelDoc = 5  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimEncodeDifference:
    m_bHasMorphBitArray = 120  # offset
    m_bHasMovementBitArray = 96  # offset
    m_bHasRotationBitArray = 72  # offset
    m_bHasUserBitArray = 144  # offset
    m_boneArray = 0  # offset
    m_morphArray = 24  # offset
    m_userArray = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimEncodedFrames:
    m_fileName = 0  # offset
    m_frameblockArray = 24  # offset
    m_nFrames = 16  # offset
    m_nFramesPerBlock = 20  # offset
    m_usageDifferences = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimEnum:
    m_value = 0  # offset

class CAnimEventDefinition:
    m_EventData = 24  # offset
    m_flCycle = 16  # offset
    m_flDuration = 20  # offset
    m_nEndFrame = 12  # offset
    m_nFrame = 8  # offset
    m_sEventName = 56  # offset
    m_sLegacyOptions = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimFoot:
    m_ankleBoneIndex = 32  # offset
    m_name = 0  # offset
    m_toeBoneIndex = 36  # offset
    m_vBallOffset = 8  # offset
    m_vHeelOffset = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimFrameBlockAnim:
    m_nEndFrame = 4  # offset
    m_nStartFrame = 0  # offset
    m_segmentIndexArray = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimFrameSegment:
    m_container = 16  # offset
    m_nLocalChannel = 8  # offset
    m_nLocalElementMasks = 4  # offset
    m_nUniqueFrameIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimGraphDebugReplay:
    m_animGraphFileName = 64  # offset
    m_frameCount = 104  # offset
    m_frameList = 72  # offset
    m_startIndex = 96  # offset
    m_writeIndex = 100  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimGraphModelBinding:
    m_modelName = 8  # offset
    m_pSharedData = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimGraphNetworkSettings:
    m_bNetworkingEnabled = 32  # offset

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

class CAnimGraphSettingsGroup:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimGraphSettingsManager:
    m_settingsGroups = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimInputDamping:
    m_fFallingSpeedScale = 16  # offset
    m_fSpeedScale = 12  # offset
    m_speedFunction = 8  # offset

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

class CAnimKeyData:
    m_boneArray = 16  # offset
    m_dataChannelArray = 96  # offset
    m_morphArray = 64  # offset
    m_nChannelElements = 88  # offset
    m_name = 0  # offset
    m_userArray = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimLocalHierarchy:
    m_nEndFrame = 44  # offset
    m_nPeakFrame = 36  # offset
    m_nStartFrame = 32  # offset
    m_nTailFrame = 40  # offset
    m_sBone = 0  # offset
    m_sNewParent = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimMorphDifference:
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimMotorUpdaterBase:
    m_bDefault = 24  # offset
    m_name = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimMovement:
    angle = 16  # offset
    endframe = 0  # offset
    motionflags = 4  # offset
    position = 32  # offset
    v0 = 8  # offset
    v1 = 12  # offset
    vector = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimNodePath:
    m_nCount = 44  # offset
    m_path = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimParamHandle:
    m_index = 1  # offset
    m_type = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimParamHandleMap:
    m_list = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimParameterBase:
    m_bIsReferenced = 105  # offset
    m_bNetworkingRequested = 104  # offset
    m_componentName = 72  # offset
    m_group = 40  # offset
    m_id = 48  # offset
    m_name = 24  # offset
    m_sComment = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimParameterManagerUpdater:
    m_autoResetMap = 160  # offset
    m_autoResetParams = 136  # offset
    m_idToIndexMap = 48  # offset
    m_indexToHandle = 112  # offset
    m_nameToIndexMap = 80  # offset
    m_parameters = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimReplayFrame:
    m_inputDataBlocks = 16  # offset
    m_instanceData = 40  # offset
    m_localToWorldTransform = 96  # offset
    m_startingLocalToWorldTransform = 64  # offset
    m_timeStamp = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimScriptComponentUpdater:
    m_hScript = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimScriptManager:
    m_scriptInfo = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimSequenceParams:
    m_flFadeInTime = 0  # offset
    m_flFadeOutTime = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimSkeleton:
    m_boneNames = 64  # offset
    m_children = 88  # offset
    m_feet = 136  # offset
    m_localSpaceTransforms = 16  # offset
    m_lodBoneCounts = 184  # offset
    m_modelSpaceTransforms = 40  # offset
    m_morphNames = 160  # offset
    m_parents = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimStateMachineUpdater:
    m_startStateIndex = 80  # offset
    m_states = 8  # offset
    m_transitions = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimTagBase:
    m_bIsReferenced = 72  # offset
    m_group = 40  # offset
    m_name = 24  # offset
    m_sComment = 32  # offset
    m_tagID = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimTagManagerUpdater:
    m_tags = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimUpdateNodeBase:
    m_name = 80  # offset
    m_networkMode = 72  # offset
    m_nodePath = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimUpdateNodeRef:
    m_nodeIndex = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimUpdateSharedData:
    m_components = 72  # offset
    m_nodeIndexMap = 40  # offset
    m_nodes = 16  # offset
    m_pParamListUpdater = 96  # offset
    m_pSkeleton = 176  # offset
    m_pStaticPoseCache = 168  # offset
    m_pTagManagerUpdater = 104  # offset
    m_rootNodePath = 184  # offset
    m_scriptManager = 112  # offset
    m_settings = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimUser:
    m_nType = 16  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimUserDifference:
    m_nType = 16  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGraphVisualizerAxis:
    m_flAxisSize = 96  # offset
    m_xWsTransform = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGraphVisualizerLine:
    m_Color = 96  # offset
    m_vWsPositionEnd = 80  # offset
    m_vWsPositionStart = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGraphVisualizerPie:
    m_Color = 112  # offset
    m_vWsCenter = 64  # offset
    m_vWsEnd = 96  # offset
    m_vWsStart = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGraphVisualizerPrimitiveBase:
    m_OwningAnimNodePaths = 12  # offset
    m_Type = 8  # offset
    m_nOwningAnimNodePathCount = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGraphVisualizerSphere:
    m_Color = 84  # offset
    m_flRadius = 80  # offset
    m_vWsPosition = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGraphVisualizerText:
    m_Color = 80  # offset
    m_Text = 88  # offset
    m_vWsPosition = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAnimationGroup:
    m_AdditionalExtRefs = 296  # offset
    m_decodeKey = 152  # offset
    m_directHSeqGroup_Handle = 144  # offset
    m_includedGroupArray_Handle = 120  # offset
    m_localHAnimArray_Handle = 96  # offset
    m_nFlags = 16  # offset
    m_name = 24  # offset
    m_szScripts = 272  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAttachment:
    m_bIgnoreRotation = 132  # offset
    m_bInfluenceRootTransform = 128  # offset
    m_influenceNames = 8  # offset
    m_influenceWeights = 116  # offset
    m_nInfluences = 131  # offset
    m_name = 0  # offset
    m_vInfluenceOffsets = 80  # offset
    m_vInfluenceRotations = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CAudioAnimTag:
    m_attachmentName = 96  # offset
    m_bPlayOnClient = 111  # offset
    m_bPlayOnServer = 110  # offset
    m_bStopWhenGraphEnds = 109  # offset
    m_bStopWhenTagEnds = 108  # offset
    m_clipName = 88  # offset
    m_flVolume = 104  # offset

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

class CBaseConstraint:
    m_name = 32  # offset
    m_slaves = 56  # offset
    m_targets = 72  # offset
    m_vUpVector = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBinaryUpdateNode:
    m_bResetChild1 = 136  # offset
    m_bResetChild2 = 137  # offset
    m_flTimingBlend = 132  # offset
    m_pChild1 = 96  # offset
    m_pChild2 = 112  # offset
    m_timingBehavior = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBindPoseUpdateNode:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBlend2DUpdateNode:
    m_bAnimEventsAndTagsOnMostWeightedOnly = 243  # offset
    m_bLockBlendOnReset = 241  # offset
    m_bLockWhenWaning = 242  # offset
    m_bLoop = 240  # offset
    m_blendSourceX = 216  # offset
    m_blendSourceY = 224  # offset
    m_damping = 192  # offset
    m_eBlendMode = 232  # offset
    m_items = 96  # offset
    m_nodeItemIndices = 168  # offset
    m_paramSpans = 144  # offset
    m_paramX = 220  # offset
    m_paramY = 228  # offset
    m_playbackSpeed = 236  # offset
    m_tags = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBlendCurve:
    m_flControlPoint1 = 0  # offset
    m_flControlPoint2 = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBlendUpdateNode:
    m_bIsAngle = 216  # offset
    m_bLockBlendOnReset = 212  # offset
    m_bLockWhenWaning = 215  # offset
    m_bLoop = 214  # offset
    m_bSyncCycles = 213  # offset
    m_blendKeyType = 208  # offset
    m_blendValueSource = 172  # offset
    m_children = 96  # offset
    m_damping = 184  # offset
    m_eLinearRootMotionBlendMode = 176  # offset
    m_paramIndex = 180  # offset
    m_sortedOrder = 120  # offset
    m_targetValues = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBlockSelectionMetricEvaluator:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBodyGroupAnimTag:
    m_bodyGroupSettings = 96  # offset
    m_nPriority = 88  # offset

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

class CBodyGroupSetting:
    m_BodyGroupName = 0  # offset
    m_nBodyGroupOption = 8  # offset

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
            "name": "MPropertyElementNameFn",
            "type": "Unknown"
        }
    ]

class CBoneConstraintBase:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoneConstraintDotToMorph:
    m_flRemap = 56  # offset
    m_sBoneName = 32  # offset
    m_sMorphChannelName = 48  # offset
    m_sTargetBoneName = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoneConstraintPoseSpaceBone:
    m_inputList = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoneConstraintPoseSpaceBone__Input_t:
    m_inputValue = 0  # offset
    m_outputTransformList = 16  # offset

class CBoneConstraintPoseSpaceMorph:
    m_bClamp = 96  # offset
    m_inputList = 72  # offset
    m_outputMorph = 48  # offset
    m_sAttachmentName = 40  # offset
    m_sBoneName = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoneConstraintPoseSpaceMorph__Input_t:
    m_inputValue = 0  # offset
    m_outputWeightList = 16  # offset

class CBoneConstraintRbf:
    m_inputBones = 32  # offset
    m_outputBones = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoneMaskUpdateNode:
    m_bUseBlendScale = 164  # offset
    m_blendSpace = 156  # offset
    m_blendValueSource = 168  # offset
    m_flRootMotionBlend = 152  # offset
    m_footMotionTiming = 160  # offset
    m_hBlendParameter = 172  # offset
    m_nWeightListIndex = 148  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBonePositionMetricEvaluator:
    m_nBoneIndex = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoneVelocityMetricEvaluator:
    m_nBoneIndex = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CBoolAnimParameter:
    m_bDefaultValue = 128  # offset

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

class CCPPScriptComponentUpdater:
    m_scriptsToRun = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CCachedPose:
    m_flCycle = 60  # offset
    m_hSequence = 56  # offset
    m_morphWeights = 32  # offset
    m_transforms = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CChoiceUpdateNode:
    m_bCrossFade = 176  # offset
    m_bDontResetSameSelection = 178  # offset
    m_bResetChosen = 177  # offset
    m_blendMethod = 168  # offset
    m_blendTime = 172  # offset
    m_blendTimes = 136  # offset
    m_children = 88  # offset
    m_choiceChangeMethod = 164  # offset
    m_choiceMethod = 160  # offset
    m_weights = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CChoreoUpdateNode:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CClothSettingsAnimTag:
    m_flEaseIn = 92  # offset
    m_flEaseOut = 96  # offset
    m_flStiffness = 88  # offset
    m_nVertexSet = 104  # offset

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

class CCompressorGroup:
    m_boolCompressor = 320  # offset
    m_colorCompressor = 344  # offset
    m_intCompressor = 296  # offset
    m_nCompressorIndex = 128  # offset
    m_nElementMask = 200  # offset
    m_nElementUniqueID = 176  # offset
    m_nFlags = 80  # offset
    m_nTotalElementCount = 0  # offset
    m_nType = 56  # offset
    m_quaternionCompressor = 272  # offset
    m_szChannelClass = 8  # offset
    m_szElementNames = 152  # offset
    m_szGrouping = 104  # offset
    m_szVariableName = 32  # offset
    m_vector2DCompressor = 368  # offset
    m_vector4DCompressor = 392  # offset
    m_vectorCompressor = 248  # offset

class CConcreteAnimParameter:
    m_bAutoReset = 121  # offset
    m_bGameWritable = 122  # offset
    m_bGraphWritable = 123  # offset
    m_bUseMostRecentValue = 120  # offset
    m_eNetworkSetting = 116  # offset
    m_previewButton = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CConstraintSlave:
    m_flWeight = 32  # offset
    m_nBoneHash = 28  # offset
    m_qBaseOrientation = 0  # offset
    m_sName = 40  # offset
    m_vBasePosition = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CConstraintTarget:
    m_bIsAttachment = 89  # offset
    m_flWeight = 72  # offset
    m_nBoneHash = 60  # offset
    m_qOffset = 32  # offset
    m_sName = 64  # offset
    m_vOffset = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CCurrentRotationVelocityMetricEvaluator:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CCurrentVelocityMetricEvaluator:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CCycleBase:
    m_flCycle = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CCycleControlClipUpdateNode:
    m_bLockWhenWaning = 138  # offset
    m_duration = 128  # offset
    m_hSequence = 124  # offset
    m_paramIndex = 136  # offset
    m_tags = 96  # offset
    m_valueSource = 132  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CCycleControlUpdateNode:
    m_bLockWhenWaning = 118  # offset
    m_paramIndex = 116  # offset
    m_valueSource = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDampedPathAnimMotorUpdater:
    m_flAnticipationTime = 44  # offset
    m_flMaxSpringTension = 64  # offset
    m_flMinSpeedScale = 48  # offset
    m_flMinSpringTension = 60  # offset
    m_flSpringConstant = 56  # offset
    m_hAnticipationHeadingParam = 54  # offset
    m_hAnticipationPosParam = 52  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDampedValueComponentUpdater:
    m_items = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDampedValueUpdateItem:
    m_damping = 0  # offset
    m_hParamIn = 32  # offset
    m_hParamOut = 34  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDemoSettingsComponentUpdater:
    m_settings = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDirectPlaybackTagData:
    m_sequenceName = 0  # offset
    m_tags = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDirectPlaybackUpdateNode:
    m_allTags = 120  # offset
    m_bFinishEarly = 116  # offset
    m_bResetOnFinish = 117  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDirectionalBlendUpdateNode:
    m_bLockBlendOnReset = 169  # offset
    m_bLoop = 168  # offset
    m_blendValueSource = 152  # offset
    m_damping = 128  # offset
    m_duration = 164  # offset
    m_hSequences = 92  # offset
    m_paramIndex = 156  # offset
    m_playbackSpeed = 160  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDistanceRemainingMetricEvaluator:
    m_bFilterFixedMinDistance = 96  # offset
    m_bFilterGoalDistance = 97  # offset
    m_bFilterGoalOvershoot = 98  # offset
    m_flMaxDistance = 80  # offset
    m_flMaxGoalOvershootScale = 92  # offset
    m_flMinDistance = 84  # offset
    m_flStartGoalFilterDistance = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CDrawCullingData:
    m_ConeAxis = 0  # offset
    m_ConeCutoff = 3  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CEditableMotionGraph:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CEmitTagActionUpdater:
    m_bIsZeroDuration = 28  # offset
    m_nTagIndex = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CEnumAnimParameter:
    m_defaultValue = 136  # offset
    m_enumOptions = 144  # offset
    m_vecEnumReferenced = 168  # offset

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

class CExpressionActionUpdater:
    m_eParamType = 26  # offset
    m_hParam = 24  # offset
    m_hScript = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFlexController:
    m_szName = 0  # offset
    m_szType = 8  # offset
    max = 20  # offset
    min = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFlexDesc:
    m_szFacs = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFlexOp:
    m_Data = 4  # offset
    m_OpCode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFlexRule:
    m_FlexOps = 8  # offset
    m_nFlex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFloatAnimParameter:
    m_bInterpolate = 140  # offset
    m_fDefaultValue = 128  # offset
    m_fMaxValue = 136  # offset
    m_fMinValue = 132  # offset

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

class CFollowAttachmentUpdateNode:
    m_opFixedData = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFollowPathUpdateNode:
    m_bBlockNonPathMovement = 120  # offset
    m_bScaleSpeed = 122  # offset
    m_bStopFeetAtGoal = 121  # offset
    m_bTurnToFace = 180  # offset
    m_facingTarget = 168  # offset
    m_flBlendOutTime = 116  # offset
    m_flMaxAngle = 132  # offset
    m_flMinAngle = 128  # offset
    m_flScale = 124  # offset
    m_flSpeedScaleBlending = 136  # offset
    m_flTurnToFaceOffset = 176  # offset
    m_hParam = 172  # offset
    m_turnDamping = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFollowTargetUpdateNode:
    m_hParameterOrientation = 138  # offset
    m_hParameterPosition = 136  # offset
    m_opFixedData = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootAdjustmentUpdateNode:
    m_bAnimationDriven = 169  # offset
    m_bResetChild = 168  # offset
    m_clips = 120  # offset
    m_facingTarget = 148  # offset
    m_flStepHeightMax = 160  # offset
    m_flStepHeightMaxAngle = 164  # offset
    m_flTurnTimeMax = 156  # offset
    m_flTurnTimeMin = 152  # offset
    m_hBasePoseCacheHandle = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootCycle:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootCycleDefinition:
    m_flStanceDirectionMS = 24  # offset
    m_footLandCycle = 56  # offset
    m_footLiftCycle = 44  # offset
    m_footOffCycle = 48  # offset
    m_footStrikeCycle = 52  # offset
    m_stanceCycle = 40  # offset
    m_vMidpointPositionMS = 12  # offset
    m_vStancePositionMS = 0  # offset
    m_vToStrideStartPos = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootCycleMetricEvaluator:
    m_footIndices = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootDefinition:
    m_ankleBoneName = 8  # offset
    m_flBindPoseDirectionMS = 52  # offset
    m_flFootLength = 48  # offset
    m_flTraceHeight = 56  # offset
    m_flTraceRadius = 60  # offset
    m_name = 0  # offset
    m_toeBoneName = 16  # offset
    m_vBallOffset = 24  # offset
    m_vHeelOffset = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootFallAnimTag:
    m_foot = 88  # offset

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

class CFootLockUpdateNode:
    m_bApplyFootRotationLimits = 336  # offset
    m_bApplyHipShift = 337  # offset
    m_bEnableRootHeightDamping = 341  # offset
    m_bEnableVerticalCurvedPaths = 340  # offset
    m_bModulateStepHeight = 338  # offset
    m_bResetChild = 339  # offset
    m_flBlendTime = 316  # offset
    m_flHipShiftScale = 312  # offset
    m_flMaxRootHeightOffset = 320  # offset
    m_flMinRootHeightOffset = 324  # offset
    m_flStepHeightDecreaseScale = 308  # offset
    m_flStepHeightIncreaseScale = 304  # offset
    m_flStrideCurveLimitScale = 300  # offset
    m_flStrideCurveScale = 296  # offset
    m_flTiltPlanePitchSpringStrength = 328  # offset
    m_flTiltPlaneRollSpringStrength = 332  # offset
    m_footSettings = 224  # offset
    m_hipShiftDamping = 248  # offset
    m_opFixedSettings = 112  # offset
    m_rootHeightDamping = 272  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootMotion:
    m_bAdditive = 32  # offset
    m_name = 24  # offset
    m_strides = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootPinningUpdateNode:
    m_bResetChild = 200  # offset
    m_eTimingSource = 168  # offset
    m_params = 176  # offset
    m_poseOpFixedData = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootPositionMetricEvaluator:
    m_bIgnoreSlope = 104  # offset
    m_footIndices = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootStepTriggerUpdateNode:
    m_flTolerance = 140  # offset
    m_triggers = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootStride:
    m_definition = 0  # offset
    m_trajectories = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootTrajectories:
    m_trajectories = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootTrajectory:
    m_flProgression = 24  # offset
    m_flRotationOffset = 20  # offset
    m_vOffset = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFootstepLandedAnimTag:
    m_BoneName = 112  # offset
    m_DebugAnimSourceString = 104  # offset
    m_FootstepType = 88  # offset
    m_OverrideSoundName = 96  # offset

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

class CFutureFacingMetricEvaluator:
    m_flDistance = 80  # offset
    m_flTime = 84  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFutureVelocityMetricEvaluator:
    m_eMode = 92  # offset
    m_flDistance = 80  # offset
    m_flStoppingDistance = 84  # offset
    m_flTargetSpeed = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CHandshakeAnimTagBase:
    m_bIsDisableTag = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CHitBox:
    m_CRC = 64  # offset
    m_bTranslationOnly = 61  # offset
    m_cRenderColor = 68  # offset
    m_flShapeRadius = 48  # offset
    m_nBoneNameHash = 52  # offset
    m_nGroupId = 56  # offset
    m_nHitBoxIndex = 72  # offset
    m_nShapeType = 60  # offset
    m_name = 0  # offset
    m_sBoneName = 16  # offset
    m_sSurfaceProperty = 8  # offset
    m_vMaxBounds = 36  # offset
    m_vMinBounds = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CHitBoxSet:
    m_HitBoxes = 16  # offset
    m_SourceFilename = 40  # offset
    m_nNameHash = 8  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CHitBoxSetList:
    m_HitBoxSets = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CHitReactUpdateNode:
    m_bResetChild = 204  # offset
    m_flMinDelayBetweenHits = 200  # offset
    m_hitBoneParam = 190  # offset
    m_hitDirectionParam = 194  # offset
    m_hitOffsetParam = 192  # offset
    m_hitStrengthParam = 196  # offset
    m_opFixedSettings = 112  # offset
    m_triggerParam = 188  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CInputStreamUpdateNode:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CIntAnimParameter:
    m_defaultValue = 128  # offset
    m_maxValue = 136  # offset
    m_minValue = 132  # offset

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

class CJiggleBoneUpdateNode:
    m_opFixedData = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CJumpHelperUpdateNode:
    m_bScaleSpeed = 211  # offset
    m_bTranslationAxis = 208  # offset
    m_eCorrectionMethod = 204  # offset
    m_flJumpEndCycle = 200  # offset
    m_flJumpStartCycle = 196  # offset
    m_flOriginalJumpDuration = 192  # offset
    m_flOriginalJumpMovement = 180  # offset
    m_hTargetParam = 176  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CLODComponentUpdater:
    m_nServerLOD = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CLeafUpdateNode:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CLeanMatrixUpdateNode:
    m_blendSource = 192  # offset
    m_damping = 168  # offset
    m_flMaxValue = 228  # offset
    m_frameCorners = 92  # offset
    m_hSequence = 224  # offset
    m_horizontalAxis = 212  # offset
    m_nSequenceMaxFrame = 232  # offset
    m_paramIndex = 196  # offset
    m_poses = 128  # offset
    m_verticalAxis = 200  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CLookAtUpdateNode:
    m_bLockWhenWaning = 337  # offset
    m_bResetChild = 336  # offset
    m_opFixedSettings = 112  # offset
    m_paramIndex = 332  # offset
    m_target = 328  # offset
    m_weightParamIndex = 334  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CLookComponentUpdater:
    m_bNetworkLookTarget = 68  # offset
    m_hLookDirection = 62  # offset
    m_hLookDistance = 60  # offset
    m_hLookHeading = 52  # offset
    m_hLookHeadingNormalized = 54  # offset
    m_hLookHeadingVelocity = 56  # offset
    m_hLookPitch = 58  # offset
    m_hLookTarget = 64  # offset
    m_hLookTargetWorldSpace = 66  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMaterialAttributeAnimTag:
    m_AttributeName = 88  # offset
    m_AttributeType = 96  # offset
    m_Color = 104  # offset
    m_flValue = 100  # offset

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

class CMaterialDrawDescriptor:
    m_flAlpha = 16  # offset
    m_flUvDensity = 0  # offset
    m_indexBuffer = 176  # offset
    m_material = 256  # offset
    m_meshletPackedIVB = 208  # offset
    m_nAppliedIndexOffset = 32  # offset
    m_nBaseVertex = 60  # offset
    m_nDepthVertexBufferIndex = 36  # offset
    m_nFirstMeshlet = 28  # offset
    m_nIndexCount = 72  # offset
    m_nMeshletPackedIVBIndex = 37  # offset
    m_nNumMeshlets = 22  # offset
    m_nPrimitiveType = 56  # offset
    m_nStartIndex = 68  # offset
    m_nVertexCount = 64  # offset
    m_rigidMeshParts = 40  # offset
    m_vTintColor = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMaterialDrawDescriptor__RigidMeshPart_t:
    m_nBoneIndex = 2  # offset
    m_nPrimitiveCount = 8  # offset
    m_nRigidBLASIndex = 0  # offset
    m_nStartIndexOffset = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMeshletDescriptor:
    m_CullingData = 8  # offset
    m_PackedAABB = 0  # offset
    m_nTriangleCount = 21  # offset
    m_nTriangleOffset = 16  # offset
    m_nVertexCount = 20  # offset
    m_nVertexOffset = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfig:
    m_ConfigName = 0  # offset
    m_Elements = 8  # offset
    m_bActiveInEditorByDefault = 33  # offset
    m_bTopLevel = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement:
    m_ElementName = 8  # offset
    m_NestedElements = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_AttachedModel:
    m_AttachmentName = 120  # offset
    m_AttachmentType = 136  # offset
    m_BodygroupOnOtherModels = 144  # offset
    m_EntityClass = 80  # offset
    m_InstanceName = 72  # offset
    m_LocalAttachmentOffsetName = 128  # offset
    m_MaterialGroupOnOtherModels = 152  # offset
    m_aAngOffset = 108  # offset
    m_bAcceptParentMaterialDrivenDecals = 143  # offset
    m_bBoneMergeFlex = 140  # offset
    m_bUserSpecifiedColor = 141  # offset
    m_bUserSpecifiedMaterialGroup = 142  # offset
    m_hModel = 88  # offset
    m_vOffset = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_Command:
    m_Args = 80  # offset
    m_Command = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_RandomColor:
    m_Gradient = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_RandomPick:
    m_ChoiceWeights = 96  # offset
    m_Choices = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_SetBodygroup:
    m_GroupName = 72  # offset
    m_nChoice = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_SetBodygroupOnAttachedModels:
    m_GroupName = 72  # offset
    m_nChoice = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_SetMaterialGroup:
    m_MaterialGroupName = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_SetMaterialGroupOnAttachedModels:
    m_MaterialGroupName = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_SetRenderColor:
    m_Color = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigElement_UserPick:
    m_Choices = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CModelConfigList:
    m_Configs = 8  # offset
    m_bHideMaterialGroupInTools = 0  # offset
    m_bHideRenderColorInTools = 1  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMoodVData:
    m_animationLayers = 232  # offset
    m_nMoodType = 224  # offset
    m_sModelName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MVDataOverlayType",
            "type": "Unknown"
        }
    ]

class CMorphBundleData:
    m_flULeftSrc = 0  # offset
    m_flVTopSrc = 4  # offset
    m_offsets = 8  # offset
    m_ranges = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMorphConstraint:
    m_flMax = 112  # offset
    m_flMin = 108  # offset
    m_nSlaveChannel = 104  # offset
    m_sTargetMorph = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMorphData:
    m_morphRectDatas = 8  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMorphRectData:
    m_bundleDatas = 16  # offset
    m_flUWidthSrc = 4  # offset
    m_flVHeightSrc = 8  # offset
    m_nXLeftDst = 0  # offset
    m_nYTopDst = 2  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMorphSetData:
    m_FlexControllers = 104  # offset
    m_FlexDesc = 80  # offset
    m_FlexRules = 128  # offset
    m_bundleTypes = 24  # offset
    m_morphDatas = 48  # offset
    m_nHeight = 20  # offset
    m_nWidth = 16  # offset
    m_pTextureAtlas = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionDataSet:
    m_groups = 0  # offset
    m_nDimensionCount = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionGraph:
    m_bLoop = 84  # offset
    m_nConfigCount = 80  # offset
    m_nConfigStartIndex = 76  # offset
    m_nParameterCount = 72  # offset
    m_pRootNode = 64  # offset
    m_paramSpans = 16  # offset
    m_tags = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionGraphConfig:
    m_flDuration = 16  # offset
    m_nMotionIndex = 20  # offset
    m_nSampleCount = 28  # offset
    m_nSampleStart = 24  # offset
    m_paramValues = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionGraphGroup:
    m_hIsActiveScript = 256  # offset
    m_motionGraphConfigs = 208  # offset
    m_motionGraphs = 184  # offset
    m_sampleToConfig = 232  # offset
    m_searchDB = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionGraphUpdateNode:
    m_pMotionGraph = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionMatchingUpdateNode:
    m_bEnableDistanceScaling = 320  # offset
    m_bEnableRotationCorrection = 264  # offset
    m_bGoalAssist = 265  # offset
    m_bLockClipWhenWaning = 252  # offset
    m_bSearchEveryTick = 224  # offset
    m_bSearchWhenClipEnds = 232  # offset
    m_bSearchWhenGoalChanges = 233  # offset
    m_blendCurve = 236  # offset
    m_dataSet = 88  # offset
    m_distanceScale_Damping = 280  # offset
    m_flBlendTime = 248  # offset
    m_flDistanceScale_InnerRadius = 308  # offset
    m_flDistanceScale_MaxScale = 312  # offset
    m_flDistanceScale_MinScale = 316  # offset
    m_flDistanceScale_OuterRadius = 304  # offset
    m_flGoalAssistDistance = 268  # offset
    m_flGoalAssistTolerance = 272  # offset
    m_flReselectionTimeWindow = 260  # offset
    m_flSampleRate = 244  # offset
    m_flSearchInterval = 228  # offset
    m_flSelectionThreshold = 256  # offset
    m_metrics = 120  # offset
    m_weights = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionMetricEvaluator:
    m_flWeight = 72  # offset
    m_means = 24  # offset
    m_nDimensionStartIndex = 76  # offset
    m_standardDeviations = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionNode:
    m_id = 32  # offset
    m_name = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionNodeBlend1D:
    m_blendItems = 40  # offset
    m_nParamIndex = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionNodeSequence:
    m_flPlaybackSpeed = 68  # offset
    m_hSequence = 64  # offset
    m_tags = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionSearchDB:
    m_codeIndices = 160  # offset
    m_residualQuantizer = 128  # offset
    m_rootNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMotionSearchNode:
    m_children = 0  # offset
    m_quantizer = 24  # offset
    m_sampleCodes = 56  # offset
    m_sampleIndices = 80  # offset
    m_selectableSamples = 104  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMovementComponentUpdater:
    m_bMoveVarsDisabled = 112  # offset
    m_bNetworkFacing = 114  # offset
    m_bNetworkPath = 113  # offset
    m_facingDamping = 72  # offset
    m_flDefaultRunSpeed = 108  # offset
    m_motors = 48  # offset
    m_nDefaultMotorIndex = 104  # offset
    m_paramHandles = 115  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CMovementHandshakeAnimTag:
    pass

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

class CMoverUpdateNode:
    m_bAdditive = 164  # offset
    m_bApplyMovement = 165  # offset
    m_bApplyRotation = 167  # offset
    m_bLimitOnly = 168  # offset
    m_bOrientMovement = 166  # offset
    m_damping = 120  # offset
    m_facingTarget = 144  # offset
    m_flTurnToFaceLimit = 160  # offset
    m_flTurnToFaceOffset = 156  # offset
    m_hMoveHeadingParam = 150  # offset
    m_hMoveVecParam = 148  # offset
    m_hTurnToFaceParam = 152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNPCPhysicsHull:
    m_eType = 8  # offset
    m_flCapsuleHeight = 12  # offset
    m_flCapsuleRadius = 16  # offset
    m_flGroundBoxHeight = 44  # offset
    m_flGroundBoxWidth = 48  # offset
    m_sName = 0  # offset
    m_vCapsuleCenter1 = 20  # offset
    m_vCapsuleCenter2 = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MFgdHelper",
            "type": "Unknown"
        },
        {
            "name": "MFgdHelper",
            "type": "Unknown"
        }
    ]

class CNewParticleEffect:
    m_LastMax = 140  # offset
    m_LastMin = 128  # offset
    m_RefCount = 208  # offset
    m_bAllocated = 0  # offset
    m_bAutoUpdateBBox = 0  # offset
    m_bCanFreeze = 126  # offset
    m_bDontRemove = 0  # offset
    m_bForceNoDraw = 0  # offset
    m_bFreezeTargetState = 125  # offset
    m_bFreezeTransitionActive = 124  # offset
    m_bIsFirstFrame = 0  # offset
    m_bNeedsBBoxUpdate = 0  # offset
    m_bRemove = 0  # offset
    m_bShouldCheckFoW = 0  # offset
    m_bShouldPerformCullCheck = 0  # offset
    m_bShouldSave = 0  # offset
    m_bShouldSimulateDuringGamePaused = 0  # offset
    m_bSimulate = 0  # offset
    m_bSuppressScreenSpaceEffect = 0  # offset
    m_flFreezeTransitionDuration = 116  # offset
    m_flFreezeTransitionOverride = 120  # offset
    m_flFreezeTransitionStart = 112  # offset
    m_flScale = 76  # offset
    m_hOwner = 80  # offset
    m_nSplitScreenUser = 152  # offset
    m_pDebugName = 40  # offset
    m_pNext = 16  # offset
    m_pOwningParticleProperty = 88  # offset
    m_pParticles = 32  # offset
    m_pPrev = 24  # offset
    m_vSortOrigin = 64  # offset
    m_vecAggregationCenter = 156  # offset

class CNmAdditiveBlendTask:
    pass

class CNmAndNode__CDefinition:
    m_conditionNodeIndices = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmAnimationPoseNode__CDefinition:
    m_bUseFramesAsInput = 32  # offset
    m_flUserSpecifiedTime = 28  # offset
    m_inputTimeRemapRange = 20  # offset
    m_nDataSlotIdx = 18  # offset
    m_nPoseTimeValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBitFlags:
    m_flags = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBlend1DNode__CDefinition:
    m_parameterization = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBlend2DNode__CDefinition:
    m_bAllowLooping = 264  # offset
    m_hullIndices = 224  # offset
    m_indices = 168  # offset
    m_nInputParameterNodeIdx0 = 56  # offset
    m_nInputParameterNodeIdx1 = 58  # offset
    m_sourceNodeIndices = 16  # offset
    m_values = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBlendTask:
    pass

class CNmBlendTaskBase:
    pass

class CNmBoneMaskBlendNode__CDefinition:
    m_nBlendWeightValueNodeIdx = 20  # offset
    m_nSourceMaskNodeIdx = 16  # offset
    m_nTargetMaskNodeIdx = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBoneMaskNode__CDefinition:
    m_boneMaskID = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBoneMaskSelectorNode__CDefinition:
    m_defaultMaskNodeIdx = 16  # offset
    m_flBlendTimeSeconds = 144  # offset
    m_maskNodeIndices = 24  # offset
    m_parameterValueNodeIdx = 18  # offset
    m_parameterValues = 64  # offset
    m_switchDynamically = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBoneMaskValueNode__CDefinition:
    pass

class CNmBoneWeightList:
    m_boneIDs = 224  # offset
    m_skeletonName = 0  # offset
    m_weights = 248  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmBoolValueNode__CDefinition:
    pass

class CNmCachedBoolNode__CDefinition:
    m_mode = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmCachedFloatNode__CDefinition:
    m_mode = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmCachedIDNode__CDefinition:
    m_mode = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmCachedPoseReadTask:
    pass

class CNmCachedPoseWriteTask:
    pass

class CNmCachedTargetNode__CDefinition:
    m_mode = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmCachedVectorNode__CDefinition:
    m_mode = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmChainLookatNode__CDefinition:
    m_bIsTargetInWorldSpace = 41  # offset
    m_chainEndBoneID = 24  # offset
    m_chainForwardDir = 44  # offset
    m_flBlendTimeSeconds = 36  # offset
    m_nChainLength = 40  # offset
    m_nEnabledNodeIdx = 34  # offset
    m_nLookatTargetNodeIdx = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmChainLookatTask:
    m_bIsRunningFromDeserializedData = 125  # offset
    m_bIsTargetInWorldSpace = 124  # offset
    m_chainForwardDir = 88  # offset
    m_flBlendWeight = 100  # offset
    m_flHorizontalAngleDegrees = 128  # offset
    m_flHorizontalAngleLimitDegrees = 104  # offset
    m_flVerticalAngleDegrees = 132  # offset
    m_flVerticalAngleLimitDegrees = 108  # offset
    m_lookatTarget = 112  # offset
    m_nChainEndBoneIdx = 80  # offset
    m_nNumBonesInChain = 84  # offset

class CNmChainSolverTask:
    m_bIsRunningFromDeserializedData = 201  # offset
    m_bIsTargetInWorldSpace = 200  # offset
    m_blendMode = 192  # offset
    m_chainStartTransformMS = 224  # offset
    m_debugEffectorBoneID = 208  # offset
    m_debugRequestedTargetTransformMS = 256  # offset
    m_debugTotalChainLength = 288  # offset
    m_effectorTarget = 144  # offset
    m_flBlendWeight = 196  # offset
    m_nEffectorBoneIdx = 80  # offset
    m_nEffectorTargetBoneIdx = 84  # offset
    m_nNumBonesInChain = 128  # offset
    m_targetTransform = 96  # offset

class CNmClip:
    m_bIsAdditive = 512  # offset
    m_compressedFloatCurveData = 128  # offset
    m_compressedFloatCurveOffsets = 152  # offset
    m_compressedPoseData = 16  # offset
    m_compressedPoseOffsets = 56  # offset
    m_flDuration = 12  # offset
    m_floatCurveDefs = 104  # offset
    m_floatCurveIDs = 80  # offset
    m_modelSpaceBoneSamplingIndices = 544  # offset
    m_modelSpaceSamplingChain = 520  # offset
    m_nNumFrames = 8  # offset
    m_rootMotion = 432  # offset
    m_secondaryAnimations = 216  # offset
    m_skeleton = 0  # offset
    m_syncTrack = 248  # offset
    m_trackCompressionSettings = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmClipNode__CDefinition:
    m_bAllowLooping = 29  # offset
    m_bSampleRootMotion = 28  # offset
    m_flSpeedMultiplier = 20  # offset
    m_nDataSlotIdx = 30  # offset
    m_nPlayInReverseValueNodeIdx = 16  # offset
    m_nResetTimeValueNodeIdx = 18  # offset
    m_nStartSyncEventOffset = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmClipReferenceNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmClipSelectorNode__CDefinition:
    m_conditionNodeIndices = 40  # offset
    m_optionNodeIndices = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmClip__ModelSpaceSamplingChainLink_t:
    m_nBoneIdx = 0  # offset
    m_nParentBoneIdx = 4  # offset
    m_nParentChainLinkIdx = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmConstBoolNode__CDefinition:
    m_bValue = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmConstFloatNode__CDefinition:
    m_flValue = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmConstIDNode__CDefinition:
    m_value = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmConstTargetNode__CDefinition:
    m_value = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmConstVectorNode__CDefinition:
    m_value = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmControlParameterBoolNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmControlParameterFloatNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmControlParameterIDNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmControlParameterTargetNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmControlParameterVectorNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmCurrentSyncEventIDNode__CDefinition:
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmCurrentSyncEventNode__CDefinition:
    m_infoType = 18  # offset
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmDurationScaleNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmEntityAttributeEventBase:
    m_attributeName = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmEntityAttributeFloatEvent:
    m_FloatValue = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmEntityAttributeIntEvent:
    m_nIntValue = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmEvent:
    m_bClientOnly = 24  # offset
    m_flDurationSeconds = 12  # offset
    m_flStartTimeSeconds = 8  # offset
    m_syncID = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmExternalGraphNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFixedWeightBoneMaskNode__CDefinition:
    m_flBoneWeight = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatAngleMathNode__CDefinition:
    m_nInputValueNodeIdx = 16  # offset
    m_operation = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatClampNode__CDefinition:
    m_clampRange = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatComparisonNode__CDefinition:
    m_comparison = 20  # offset
    m_flComparisonValue = 28  # offset
    m_flEpsilon = 24  # offset
    m_nComparandValueNodeIdx = 18  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatCurveEvent:
    m_ID = 32  # offset
    m_curve = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatCurveEventNode__CDefinition:
    m_eventConditionRules = 32  # offset
    m_eventID = 16  # offset
    m_flDefaultValue = 28  # offset
    m_nDefaultNodeIdx = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatCurveNode__CDefinition:
    m_curve = 24  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatEaseNode__CDefinition:
    m_bUseStartValue = 27  # offset
    m_easingOp = 26  # offset
    m_flEaseTime = 16  # offset
    m_flStartValue = 20  # offset
    m_nInputValueNodeIdx = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatMathNode__CDefinition:
    m_bReturnAbsoluteResult = 20  # offset
    m_bReturnNegatedResult = 21  # offset
    m_flValueB = 24  # offset
    m_nInputValueNodeIdxA = 16  # offset
    m_nInputValueNodeIdxB = 18  # offset
    m_operator = 22  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatRangeComparisonNode__CDefinition:
    m_bIsInclusiveCheck = 26  # offset
    m_nInputValueNodeIdx = 24  # offset
    m_range = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatRemapNode__CDefinition:
    m_inputRange = 20  # offset
    m_nInputValueNodeIdx = 16  # offset
    m_outputRange = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatRemapNode__RemapRange_t:
    m_flBegin = 0  # offset
    m_flEnd = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatSelectorNode__CDefinition:
    m_conditionNodeIndices = 16  # offset
    m_easingOp = 112  # offset
    m_flDefaultValue = 104  # offset
    m_flEaseTime = 108  # offset
    m_values = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatSwitchNode__CDefinition:
    m_flFalseValue = 24  # offset
    m_flTrueValue = 28  # offset
    m_nFalseValueNodeIdx = 20  # offset
    m_nSwitchValueNodeIdx = 16  # offset
    m_nTrueValueNodeIdx = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFloatValueNode__CDefinition:
    pass

class CNmFollowBoneNode__CDefinition:
    m_bone = 24  # offset
    m_followTargetBone = 32  # offset
    m_mode = 42  # offset
    m_nEnabledNodeIdx = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFollowBoneTask:
    pass

class CNmFootEvent:
    m_phase = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFootEventConditionNode__CDefinition:
    m_eventConditionRules = 20  # offset
    m_nSourceStateNodeIdx = 16  # offset
    m_phaseCondition = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFootstepEventIDNode__CDefinition:
    m_eventConditionRules = 20  # offset
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFootstepEventPercentageThroughNode__CDefinition:
    m_eventConditionRules = 20  # offset
    m_nSourceStateNodeIdx = 16  # offset
    m_phaseCondition = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmFrameSnapEvent:
    m_frameSnapMode = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmGraphDefinition:
    m_controlParameterIDs = 48  # offset
    m_externalGraphSlots = 144  # offset
    m_nRootNodeIdx = 40  # offset
    m_nodePaths = 280  # offset
    m_persistentNodeIndices = 16  # offset
    m_referencedGraphSlots = 120  # offset
    m_resources = 304  # offset
    m_skeleton = 8  # offset
    m_variationID = 0  # offset
    m_virtualParameterIDs = 72  # offset
    m_virtualParameterNodeIndices = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmGraphDefinition__ExternalGraphSlot_t:
    m_nNodeIdx = 0  # offset
    m_slotID = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmGraphDefinition__ReferencedGraphSlot_t:
    m_dataSlotIdx = 2  # offset
    m_nNodeIdx = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmGraphEventConditionNode__CDefinition:
    m_conditions = 24  # offset
    m_eventConditionRules = 20  # offset
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmGraphEventConditionNode__Condition_t:
    m_eventID = 0  # offset
    m_eventTypeCondition = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmGraphNode__CDefinition:
    m_nNodeIdx = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDComparisonNode__CDefinition:
    m_comparisionIDs = 24  # offset
    m_comparison = 18  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDEvent:
    m_ID = 32  # offset
    m_secondaryID = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDEventConditionNode__CDefinition:
    m_eventConditionRules = 20  # offset
    m_eventIDs = 24  # offset
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDEventNode__CDefinition:
    m_defaultValue = 24  # offset
    m_eventConditionRules = 20  # offset
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDEventPercentageThroughNode__CDefinition:
    m_eventConditionRules = 20  # offset
    m_eventID = 24  # offset
    m_nSourceStateNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDSelectorNode__CDefinition:
    m_conditionNodeIndices = 16  # offset
    m_defaultValue = 120  # offset
    m_values = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDSwitchNode__CDefinition:
    m_falseValue = 24  # offset
    m_nFalseValueNodeIdx = 20  # offset
    m_nSwitchValueNodeIdx = 16  # offset
    m_nTrueValueNodeIdx = 18  # offset
    m_trueValue = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDToFloatNode__CDefinition:
    m_IDs = 24  # offset
    m_defaultValue = 20  # offset
    m_nInputValueNodeIdx = 16  # offset
    m_values = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIDValueNode__CDefinition:
    pass

class CNmIKBody:
    m_flMass = 0  # offset
    m_flResistance = 28  # offset
    m_vLocalMassCenter = 4  # offset
    m_vRadius = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIKEffector:
    m_bEnabled = 4  # offset
    m_flWeight = 48  # offset
    m_nBodyIndex = 0  # offset
    m_qTargetOrientation = 32  # offset
    m_vTargetPosition = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIKJoint:
    m_flMaxTwistLimit = 56  # offset
    m_flMinTwistLimit = 52  # offset
    m_flSwingLimit = 48  # offset
    m_flWeight = 60  # offset
    m_nBodyIndex = 4  # offset
    m_nParentIndex = 0  # offset
    m_xLocalFrame = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIKRig:
    m_skeleton = 0  # offset
    m_vecBodies = 8  # offset
    m_vecJoints = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmIsTargetSetNode__CDefinition:
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmLayerBlendNode__CDefinition:
    m_bOnlySampleBaseRootMotion = 18  # offset
    m_layerDefinition = 24  # offset
    m_nBaseNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmLayerBlendNode__LayerDefinition_t:
    m_bIgnoreEvents = 9  # offset
    m_bIsStateMachineLayer = 10  # offset
    m_bIsSynchronized = 8  # offset
    m_blendMode = 11  # offset
    m_nBoneMaskValueNodeIdx = 4  # offset
    m_nInputNodeIdx = 0  # offset
    m_nRootMotionWeightValueNodeIdx = 6  # offset
    m_nWeightValueNodeIdx = 2  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmLegacyEvent:
    m_KV = 40  # offset
    m_animEventClassName = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmMaterialAttributeEvent:
    m_attributeName = 32  # offset
    m_attributeNameToken = 40  # offset
    m_w = 240  # offset
    m_x = 48  # offset
    m_y = 112  # offset
    m_z = 176  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmModelSpaceBlendTask:
    pass

class CNmNotNode__CDefinition:
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmOrNode__CDefinition:
    m_conditionNodeIndices = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmOrientationWarpEvent:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmOrientationWarpNode__CDefinition:
    m_bIsOffsetNode = 20  # offset
    m_bIsOffsetRelativeToCharacter = 21  # offset
    m_nClipReferenceNodeIdx = 16  # offset
    m_nTargetValueNodeIdx = 18  # offset
    m_samplingMode = 22  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmOverlayBlendTask:
    pass

class CNmParameterizedBlendNode__BlendRange_t:
    m_nInputIdx0 = 0  # offset
    m_nInputIdx1 = 2  # offset
    m_parameterValueRange = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmParameterizedBlendNode__CDefinition:
    m_bAllowLooping = 58  # offset
    m_nInputParameterValueNodeIdx = 56  # offset
    m_sourceNodeIndices = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmParameterizedBlendNode__Parameterization_t:
    m_blendRanges = 0  # offset
    m_parameterRange = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmParameterizedClipSelectorNode__CDefinition:
    m_bHasWeightsSet = 59  # offset
    m_bIgnoreInvalidOptions = 58  # offset
    m_optionNodeIndices = 16  # offset
    m_optionWeights = 40  # offset
    m_parameterNodeIdx = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmParameterizedSelectorNode__CDefinition:
    m_bHasWeightsSet = 59  # offset
    m_bIgnoreInvalidOptions = 58  # offset
    m_optionNodeIndices = 16  # offset
    m_optionWeights = 40  # offset
    m_parameterNodeIdx = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmParticleEvent:
    m_attachmentPoint0 = 64  # offset
    m_attachmentPoint1 = 80  # offset
    m_attachmentType0 = 72  # offset
    m_attachmentType1 = 88  # offset
    m_bDetachFromOwner = 57  # offset
    m_bPlayEndCap = 58  # offset
    m_bStopImmediately = 56  # offset
    m_config = 96  # offset
    m_effectForConfig = 104  # offset
    m_hParticleSystem = 40  # offset
    m_relevance = 32  # offset
    m_tags = 48  # offset
    m_type = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmPassthroughNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmPoseNode__CDefinition:
    pass

class CNmPoseTask:
    pass

class CNmReferencePoseNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmReferencePoseTask:
    pass

class CNmReferencedGraphNode__CDefinition:
    m_nFallbackNodeIdx = 18  # offset
    m_nReferencedGraphIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmRootMotionData:
    m_flAverageAngularVelocityRadians = 32  # offset
    m_flAverageLinearVelocity = 28  # offset
    m_nNumFrames = 24  # offset
    m_totalDelta = 48  # offset
    m_transforms = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmRootMotionEvent:
    m_flBlendTimeSeconds = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmRootMotionOverrideNode__CDefinition:
    m_angularVelocityLimitNodeIdx = 30  # offset
    m_desiredFacingDirectionNodeIdx = 26  # offset
    m_desiredMovingVelocityNodeIdx = 24  # offset
    m_linearVelocityLimitNodeIdx = 28  # offset
    m_maxAngularVelocityRadians = 36  # offset
    m_maxLinearVelocity = 32  # offset
    m_overrideFlags = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSampleTask:
    pass

class CNmScaleNode__CDefinition:
    m_nEnableNodeIdx = 26  # offset
    m_nMaskNodeIdx = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmScaleTask:
    pass

class CNmSelectorNode__CDefinition:
    m_conditionNodeIndices = 40  # offset
    m_optionNodeIndices = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSkeleton:
    m_ID = 0  # offset
    m_bIsPropSkeleton = 152  # offset
    m_boneIDs = 8  # offset
    m_maskDefinitions = 104  # offset
    m_modelSpaceReferencePose = 72  # offset
    m_numBonesToSampleAtLowLOD = 96  # offset
    m_parentIndices = 24  # offset
    m_parentSpaceReferencePose = 48  # offset
    m_secondarySkeletons = 136  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSkeleton__SecondarySkeleton_t:
    m_attachToBoneID = 0  # offset
    m_skeleton = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSoundEvent:
    m_attachmentName = 56  # offset
    m_bContinuePlayingSoundAtDurationEnd = 72  # offset
    m_flDurationInterruptionThreshold = 76  # offset
    m_name = 40  # offset
    m_position = 48  # offset
    m_relevance = 32  # offset
    m_tags = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSpeedScaleBaseNode__CDefinition:
    m_flDefaultInputValue = 28  # offset
    m_nInputValueNodeIdx = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSpeedScaleNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmStateCompletedConditionNode__CDefinition:
    m_flTransitionDurationSeconds = 20  # offset
    m_nSourceStateNodeIdx = 16  # offset
    m_nTransitionDurationOverrideNodeIdx = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmStateMachineNode__CDefinition:
    m_nDefaultStateIndex = 304  # offset
    m_stateDefinitions = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmStateMachineNode__StateDefinition_t:
    m_nEntryConditionNodeIdx = 2  # offset
    m_nStateNodeIdx = 0  # offset
    m_transitionDefinitions = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmStateMachineNode__TransitionDefinition_t:
    m_bCanBeForced = 6  # offset
    m_nConditionNodeIdx = 2  # offset
    m_nTargetStateIdx = 0  # offset
    m_nTransitionNodeIdx = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmStateNode__CDefinition:
    m_bIsOffState = 174  # offset
    m_entryEvents = 24  # offset
    m_executeEvents = 56  # offset
    m_exitEvents = 88  # offset
    m_nChildNodeIdx = 16  # offset
    m_nLayerBoneMaskNodeIdx = 172  # offset
    m_nLayerRootMotionWeightNodeIdx = 170  # offset
    m_nLayerWeightNodeIdx = 168  # offset
    m_timedElapsedEvents = 144  # offset
    m_timedRemainingEvents = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmStateNode__TimedEvent_t:
    m_ID = 0  # offset
    m_comparisionOperator = 12  # offset
    m_flTimeValueSeconds = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSyncEventIndexConditionNode__CDefinition:
    m_nSourceStateNodeIdx = 16  # offset
    m_syncEventIdx = 20  # offset
    m_triggerMode = 18  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSyncTrack:
    m_nStartEventOffset = 168  # offset
    m_syncEvents = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSyncTrack__EventMarker_t:
    m_ID = 8  # offset
    m_startTime = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmSyncTrack__Event_t:
    m_ID = 0  # offset
    m_duration = 12  # offset
    m_startTime = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTarget:
    m_bHasOffsets = 42  # offset
    m_bIsBoneTarget = 40  # offset
    m_bIsSet = 43  # offset
    m_bIsUsingBoneSpaceOffsets = 41  # offset
    m_boneID = 32  # offset
    m_transform = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTargetInfoNode__CDefinition:
    m_bIsWorldSpaceTarget = 24  # offset
    m_infoType = 20  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTargetOffsetNode__CDefinition:
    m_bIsBoneSpaceOffset = 18  # offset
    m_nInputValueNodeIdx = 16  # offset
    m_rotationOffset = 32  # offset
    m_translationOffset = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTargetPointNode__CDefinition:
    m_bIsWorldSpaceTarget = 18  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTargetValueNode__CDefinition:
    pass

class CNmTargetWarpEvent:
    m_algorithm = 33  # offset
    m_rule = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTargetWarpNode__CDefinition:
    m_bAllowTargetUpdate = 21  # offset
    m_flLerpFallbackDistanceThreshold = 32  # offset
    m_flMaxTangentLength = 28  # offset
    m_flSamplingPositionErrorThresholdSq = 24  # offset
    m_flTargetUpdateAngleThresholdRadians = 40  # offset
    m_flTargetUpdateDistanceThreshold = 36  # offset
    m_nClipReferenceNodeIdx = 16  # offset
    m_nTargetValueNodeIdx = 18  # offset
    m_samplingMode = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTimeConditionNode__CDefinition:
    m_flComparand = 20  # offset
    m_nInputValueNodeIdx = 18  # offset
    m_operator = 25  # offset
    m_sourceStateNodeIdx = 16  # offset
    m_type = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTransitionEvent:
    m_ID = 40  # offset
    m_rule = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTransitionEventConditionNode__CDefinition:
    m_eventConditionRules = 24  # offset
    m_nSourceStateNodeIdx = 28  # offset
    m_requireRuleID = 16  # offset
    m_ruleCondition = 30  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTransitionNode__CDefinition:
    m_blendWeightEasing = 42  # offset
    m_boneMaskBlendInTimePercentage = 28  # offset
    m_flDuration = 24  # offset
    m_flTimeOffset = 32  # offset
    m_nDurationOverrideNodeIdx = 18  # offset
    m_nTargetStateNodeIdx = 16  # offset
    m_rootMotionBlend = 43  # offset
    m_startBoneMaskNodeIdx = 22  # offset
    m_targetSyncIDNodeIdx = 40  # offset
    m_timeOffsetOverrideNodeIdx = 20  # offset
    m_transitionOptions = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmTwoBoneIKNode__CDefinition:
    m_bIsTargetInWorldSpace = 41  # offset
    m_blendMode = 40  # offset
    m_effectorBoneID = 24  # offset
    m_flBlendTimeSeconds = 36  # offset
    m_nEffectorTargetNodeIdx = 32  # offset
    m_nEnabledNodeIdx = 34  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmValueNode__CDefinition:
    pass

class CNmVectorCreateNode__CDefinition:
    m_inputValueXNodeIdx = 18  # offset
    m_inputValueYNodeIdx = 20  # offset
    m_inputValueZNodeIdx = 22  # offset
    m_inputVectorValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVectorInfoNode__CDefinition:
    m_desiredInfo = 18  # offset
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVectorNegateNode__CDefinition:
    m_nInputValueNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVectorValueNode__CDefinition:
    pass

class CNmVelocityBasedSpeedScaleNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVelocityBlendNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVirtualParameterBoneMaskNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVirtualParameterBoolNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVirtualParameterFloatNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVirtualParameterIDNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVirtualParameterTargetNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmVirtualParameterVectorNode__CDefinition:
    m_nChildNodeIdx = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmZeroPoseNode__CDefinition:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CNmZeroPoseTask:
    pass

class COrientConstraint:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class COrientationWarpUpdateNode:
    m_bEnablePreferredRotationDirection = 176  # offset
    m_damping = 144  # offset
    m_eMode = 116  # offset
    m_ePreferredRotationDirection = 180  # offset
    m_eRootMotionSource = 168  # offset
    m_eTargetOffsetMode = 128  # offset
    m_flMaxRootMotionScale = 172  # offset
    m_flPreferredRotationThreshold = 184  # offset
    m_flTargetOffset = 132  # offset
    m_hFallbackTargetPositionParam = 124  # offset
    m_hTargetOffsetParam = 136  # offset
    m_hTargetParam = 120  # offset
    m_hTargetPositionParam = 122  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPairedSequenceComponentUpdater:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPairedSequenceUpdateNode:
    m_sPairedSequenceRole = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParamSpanUpdater:
    m_spans = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParentConstraint:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleAnimTag:
    m_attachmentCP1Name = 136  # offset
    m_attachmentCP1Type = 144  # offset
    m_attachmentName = 120  # offset
    m_attachmentType = 128  # offset
    m_bAggregate = 113  # offset
    m_bDetachFromOwner = 112  # offset
    m_bStopWhenTagEnds = 114  # offset
    m_bTagEndStopIsInstant = 115  # offset
    m_configName = 104  # offset
    m_hParticleSystem = 88  # offset
    m_particleSystemName = 96  # offset

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

class CParticleCollectionFloatInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CParticleCollectionRendererFloatInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CParticleCollectionRendererVecInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CParticleCollectionVecInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CParticleFloatInput:
    m_Curve = 288  # offset
    m_NamedValue = 32  # offset
    m_bHasRandomSignFlip = 124  # offset
    m_bNoiseImgPreviewLive = 216  # offset
    m_bReverseOrder = 112  # offset
    m_bUseBoundsCenter = 232  # offset
    m_flBiasParameter = 284  # offset
    m_flInput0 = 244  # offset
    m_flInput1 = 248  # offset
    m_flLOD0 = 140  # offset
    m_flLOD1 = 144  # offset
    m_flLOD2 = 148  # offset
    m_flLOD3 = 152  # offset
    m_flLiteralValue = 24  # offset
    m_flMultFactor = 240  # offset
    m_flNoCameraFallback = 228  # offset
    m_flNoiseImgPreviewScale = 212  # offset
    m_flNoiseOffset = 184  # offset
    m_flNoiseOutputMax = 164  # offset
    m_flNoiseOutputMin = 160  # offset
    m_flNoiseScale = 168  # offset
    m_flNoiseTurbulenceMix = 208  # offset
    m_flNoiseTurbulenceScale = 204  # offset
    m_flNotchedOutputInside = 272  # offset
    m_flNotchedOutputOutside = 268  # offset
    m_flNotchedRangeMax = 264  # offset
    m_flNotchedRangeMin = 260  # offset
    m_flOutput0 = 252  # offset
    m_flOutput1 = 256  # offset
    m_flRandomMax = 120  # offset
    m_flRandomMin = 116  # offset
    m_nBiasType = 280  # offset
    m_nControlPoint = 96  # offset
    m_nInputMode = 236  # offset
    m_nMapType = 20  # offset
    m_nNoiseInputVectorAttribute = 156  # offset
    m_nNoiseModifier = 200  # offset
    m_nNoiseOctaves = 188  # offset
    m_nNoiseTurbulence = 192  # offset
    m_nNoiseType = 196  # offset
    m_nRandomMode = 132  # offset
    m_nRandomSeed = 128  # offset
    m_nRoundType = 276  # offset
    m_nScalarAttribute = 100  # offset
    m_nType = 16  # offset
    m_nVectorAttribute = 104  # offset
    m_nVectorComponent = 108  # offset
    m_vecNoiseOffsetRate = 172  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MCustomFGDMetadata",
            "type": "Unknown"
        }
    ]

class CParticleInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CParticleModelInput:
    m_NamedValue = 24  # offset
    m_nControlPoint = 88  # offset
    m_nType = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        },
        {
            "name": "MCustomFGDMetadata",
            "type": "Unknown"
        }
    ]

class CParticleProperty:
    pass

class CParticleRemapFloatInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CParticleTransformInput:
    m_NamedValue = 24  # offset
    m_bFollowNamedValue = 88  # offset
    m_bSupportsDisabled = 89  # offset
    m_bUseOrientation = 90  # offset
    m_flEndCPGrowthTime = 100  # offset
    m_nControlPoint = 92  # offset
    m_nControlPointRangeMax = 96  # offset
    m_nType = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        },
        {
            "name": "MCustomFGDMetadata",
            "type": "Unknown"
        }
    ]

class CParticleVariableRef:
    m_variableName = 0  # offset
    m_variableType = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CParticleVecInput:
    m_FloatComponentX = 168  # offset
    m_FloatComponentY = 520  # offset
    m_FloatComponentZ = 872  # offset
    m_FloatInterp = 1224  # offset
    m_Gradient = 1608  # offset
    m_LiteralColor = 32  # offset
    m_NamedValue = 40  # offset
    m_bFollowNamedValue = 104  # offset
    m_flInterpInput0 = 1576  # offset
    m_flInterpInput1 = 1580  # offset
    m_nControlPoint = 124  # offset
    m_nDeltaControlPoint = 128  # offset
    m_nType = 16  # offset
    m_nVectorAttribute = 108  # offset
    m_vCPRelativeDir = 156  # offset
    m_vCPRelativePosition = 144  # offset
    m_vCPValueScale = 132  # offset
    m_vInterpOutput0 = 1584  # offset
    m_vInterpOutput1 = 1596  # offset
    m_vLiteralValue = 20  # offset
    m_vRandomMax = 1644  # offset
    m_vRandomMin = 1632  # offset
    m_vVectorAttributeScale = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MCustomFGDMetadata",
            "type": "Unknown"
        }
    ]

class CPathAnimMotorUpdater:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPathAnimMotorUpdaterBase:
    m_bLockToPath = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPathHelperUpdateNode:
    m_flStoppingRadius = 112  # offset
    m_flStoppingSpeedScale = 116  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPathMetricEvaluator:
    m_bExtrapolateMovement = 108  # offset
    m_flDistance = 104  # offset
    m_flMinExtrapolationSpeed = 112  # offset
    m_pathTimeSamples = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPerParticleFloatInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CPerParticleVecInput:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyCustomEditor",
            "type": "Unknown"
        }
    ]

class CPhysSurfaceProperties:
    m_audioParams = 168  # offset
    m_audioSounds = 72  # offset
    m_bHidden = 24  # offset
    m_baseNameHash = 12  # offset
    m_description = 32  # offset
    m_name = 0  # offset
    m_nameHash = 8  # offset
    m_physics = 40  # offset
    m_vehicleParams = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPhysSurfacePropertiesAudio:
    m_flOcclusionFactor = 28  # offset
    m_flStaticImpactVolume = 24  # offset
    m_hardThreshold = 16  # offset
    m_hardVelocityThreshold = 20  # offset
    m_hardnessFactor = 4  # offset
    m_reflectivity = 0  # offset
    m_roughThreshold = 12  # offset
    m_roughnessFactor = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPhysSurfacePropertiesPhysics:
    m_density = 8  # offset
    m_elasticity = 4  # offset
    m_friction = 0  # offset
    m_softContactDampingRatio = 20  # offset
    m_softContactFrequency = 16  # offset
    m_thickness = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPhysSurfacePropertiesSoundNames:
    m_break = 48  # offset
    m_bulletImpact = 32  # offset
    m_impactHard = 8  # offset
    m_impactSoft = 0  # offset
    m_meleeImpact = 64  # offset
    m_pushOff = 72  # offset
    m_resonant = 88  # offset
    m_rolling = 40  # offset
    m_scrapeRough = 24  # offset
    m_scrapeSmooth = 16  # offset
    m_skidStop = 80  # offset
    m_strain = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPhysSurfacePropertiesVehicle:
    m_wheelDrag = 0  # offset
    m_wheelFrictionScale = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPlayerInputAnimMotorUpdater:
    m_bUseAcceleration = 72  # offset
    m_flAnticipationDistance = 64  # offset
    m_flSpringConstant = 60  # offset
    m_hAnticipationHeadingParam = 70  # offset
    m_hAnticipationPosParam = 68  # offset
    m_sampleTimes = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPointConstraint:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPoseHandle:
    m_eType = 2  # offset
    m_nIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CProductQuantizer:
    m_nDimensions = 24  # offset
    m_subQuantizers = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseGraphExecutionHistory:
    m_mapCellDesc = 40  # offset
    m_mapCursorDesc = 80  # offset
    m_nInstanceID = 0  # offset
    m_strFileName = 8  # offset
    m_vecHistory = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseRuntimeMethodArg:
    m_Description = 56  # offset
    m_Name = 0  # offset
    m_Type = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_Chunk:
    m_InstructionEditorIDs = 32  # offset
    m_Instructions = 0  # offset
    m_Registers = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_Constant:
    m_Type = 0  # offset
    m_Value = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_DomainValue:
    m_RequiredRuntimeType = 16  # offset
    m_Value = 8  # offset
    m_nType = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_OutputConnection:
    m_Param = 48  # offset
    m_SourceOutput = 0  # offset
    m_TargetEntity = 16  # offset
    m_TargetInput = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_PublicOutput:
    m_Args = 24  # offset
    m_Description = 16  # offset
    m_Name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_RegisterInfo:
    m_OriginName = 32  # offset
    m_Type = 8  # offset
    m_nLastReadByInstruction = 92  # offset
    m_nReg = 0  # offset
    m_nWrittenByInstruction = 88  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulse_Variable:
    m_DefaultValue = 48  # offset
    m_Description = 16  # offset
    m_Name = 0  # offset
    m_Type = 24  # offset
    m_bIsObservable = 73  # offset
    m_bIsPublicBlackboardVariable = 72  # offset
    m_nEditorNodeID = 76  # offset
    m_nKeysSource = 68  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CQuaternionAnimParameter:
    m_bInterpolate = 144  # offset
    m_defaultValue = 128  # offset

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

class CRagdollAnimTag:
    m_profileName = 88  # offset

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

class CRagdollComponentUpdater:
    m_bSolidCollisionAtZeroWeight = 204  # offset
    m_boneIndices = 96  # offset
    m_boneNames = 120  # offset
    m_boneToWeightIndices = 168  # offset
    m_flMaxStretch = 200  # offset
    m_flSpringFrequencyMax = 196  # offset
    m_flSpringFrequencyMin = 192  # offset
    m_followAttachmentNodePaths = 72  # offset
    m_ragdollNodePaths = 48  # offset
    m_weightLists = 144  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRagdollUpdateNode:
    m_nWeightListIndex = 112  # offset
    m_poseControlMethod = 116  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRemapValueComponentUpdater:
    m_items = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRemapValueUpdateItem:
    m_flMaxInputValue = 8  # offset
    m_flMaxOutputValue = 16  # offset
    m_flMinInputValue = 4  # offset
    m_flMinOutputValue = 12  # offset
    m_hParamIn = 0  # offset
    m_hParamOut = 2  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRenderBufferBinding:
    m_hBuffer = 0  # offset
    m_nBindOffsetBytes = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRenderGroom:
    m_bEnableSimulation = 156  # offset
    m_hSimParamsMat = 64  # offset
    m_hairPositionOffsets = 24  # offset
    m_hairs = 0  # offset
    m_nAttachBoneIdx = 144  # offset
    m_nAttachMeshDrawCallIdx = 152  # offset
    m_nAttachMeshIdx = 148  # offset
    m_nGroomGroupID = 140  # offset
    m_nGuideHairCount = 124  # offset
    m_nHairCount = 128  # offset
    m_nMaxSegmentsPerHairStrand = 120  # offset
    m_nTotalSegmentCount = 136  # offset
    m_nTotalVertexCount = 132  # offset
    m_strandSegmentCountHist = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRenderMesh:
    m_bEmbeddedMapMesh = 437  # offset
    m_bUseUV2ForCharting = 436  # offset
    m_constraints = 168  # offset
    m_meshDeformParams = 472  # offset
    m_pGroomData = 488  # offset
    m_sceneObjects = 16  # offset
    m_skeleton = 184  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRenderSkeleton:
    m_boneParents = 48  # offset
    m_bones = 0  # offset
    m_nBoneWeightCount = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRootUpdateNode:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSceneObjectData:
    m_drawBounds = 40  # offset
    m_drawCalls = 24  # offset
    m_meshlets = 56  # offset
    m_vMaxBounds = 12  # offset
    m_vMinBounds = 0  # offset
    m_vTintColor = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSelectorUpdateNode:
    m_bLockWhenWaning = 177  # offset
    m_bResetOnChange = 176  # offset
    m_bSyncCyclesOnChange = 178  # offset
    m_blendCurve = 148  # offset
    m_children = 96  # offset
    m_eTagBehavior = 172  # offset
    m_flBlendTime = 156  # offset
    m_hParameter = 164  # offset
    m_nTagIndex = 168  # offset
    m_tags = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqAutoLayer:
    m_end = 24  # offset
    m_flags = 4  # offset
    m_nLocalPose = 2  # offset
    m_nLocalReference = 0  # offset
    m_peak = 16  # offset
    m_start = 12  # offset
    m_tail = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqAutoLayerFlag:
    m_bFetchFrame = 6  # offset
    m_bLocal = 4  # offset
    m_bNoBlend = 3  # offset
    m_bPose = 5  # offset
    m_bPost = 0  # offset
    m_bSpline = 1  # offset
    m_bSubtract = 7  # offset
    m_bXFade = 2  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqBoneMaskList:
    m_flBoneWeightArray = 40  # offset
    m_flDefaultMorphCtrlWeight = 64  # offset
    m_morphCtrlWeightArray = 72  # offset
    m_nLocalBoneArray = 16  # offset
    m_sName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqCmdLayer:
    m_bSpline = 10  # offset
    m_cmd = 0  # offset
    m_flVar1 = 12  # offset
    m_flVar2 = 16  # offset
    m_nDstResult = 6  # offset
    m_nLineNumber = 20  # offset
    m_nLocalBonemask = 4  # offset
    m_nLocalReference = 2  # offset
    m_nSrcResult = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqCmdSeqDesc:
    m_activityArray = 96  # offset
    m_cmdLayerArray = 48  # offset
    m_eventArray = 72  # offset
    m_flFPS = 40  # offset
    m_flags = 16  # offset
    m_nFrameCount = 38  # offset
    m_nFrameRangeSequence = 36  # offset
    m_nSubCycles = 44  # offset
    m_numLocalResults = 46  # offset
    m_poseSettingArray = 120  # offset
    m_sName = 0  # offset
    m_transition = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqIKLock:
    m_bBonesOrientedAlongPositiveX = 10  # offset
    m_flAngleWeight = 4  # offset
    m_flPosWeight = 0  # offset
    m_nLocalBone = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqMultiFetch:
    m_bCalculatePoseParameters = 100  # offset
    m_bFixedBlendWeight = 101  # offset
    m_flFixedBlendWeightVals = 104  # offset
    m_flags = 0  # offset
    m_localReferenceArray = 8  # offset
    m_nGroupSize = 32  # offset
    m_nLocalCyclePoseParameter = 96  # offset
    m_nLocalPose = 40  # offset
    m_poseKeyArray0 = 48  # offset
    m_poseKeyArray1 = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqMultiFetchFlag:
    m_b0D = 2  # offset
    m_b1D = 3  # offset
    m_b2D = 4  # offset
    m_b2D_TRI = 5  # offset
    m_bCylepose = 1  # offset
    m_bRealtime = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqPoseParamDesc:
    m_bLooping = 28  # offset
    m_flEnd = 20  # offset
    m_flLoop = 24  # offset
    m_flStart = 16  # offset
    m_sName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqPoseSetting:
    m_bX = 52  # offset
    m_bY = 53  # offset
    m_bZ = 54  # offset
    m_eType = 56  # offset
    m_flValue = 48  # offset
    m_sAttachment = 16  # offset
    m_sPoseParameter = 0  # offset
    m_sReferenceSequence = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqS1SeqDesc:
    m_IKLockArray = 176  # offset
    m_LegacyKeyValueText = 224  # offset
    m_SequenceKeys = 208  # offset
    m_activityArray = 240  # offset
    m_autoLayerArray = 152  # offset
    m_fetch = 32  # offset
    m_flags = 16  # offset
    m_footMotion = 264  # offset
    m_nLocalWeightlist = 144  # offset
    m_sName = 0  # offset
    m_transition = 200  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqScaleSet:
    m_bRootOffset = 16  # offset
    m_flBoneScaleArray = 56  # offset
    m_nLocalBoneArray = 32  # offset
    m_sName = 0  # offset
    m_vRootOffset = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqSeqDescFlag:
    m_bAutoplay = 2  # offset
    m_bHidden = 4  # offset
    m_bLegacyCyclepose = 8  # offset
    m_bLegacyDelta = 6  # offset
    m_bLegacyRealtime = 9  # offset
    m_bLegacyWorldspace = 7  # offset
    m_bLooping = 0  # offset
    m_bModelDoc = 10  # offset
    m_bMulti = 5  # offset
    m_bPost = 3  # offset
    m_bSnap = 1  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqSynthAnimDesc:
    m_activityArray = 40  # offset
    m_flags = 16  # offset
    m_nLocalBaseReference = 36  # offset
    m_nLocalBoneMask = 38  # offset
    m_sName = 0  # offset
    m_transition = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSeqTransition:
    m_flFadeInTime = 0  # offset
    m_flFadeOutTime = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSequenceFinishedAnimTag:
    m_sequenceName = 88  # offset

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

class CSequenceGroupData:
    m_keyValues = 272  # offset
    m_localBoneMaskArray = 160  # offset
    m_localBoneNameArray = 208  # offset
    m_localCmdSeqDescArray = 136  # offset
    m_localIKAutoplayLockArray = 288  # offset
    m_localMultiSeqDescArray = 88  # offset
    m_localNodeName = 232  # offset
    m_localPoseParamArray = 248  # offset
    m_localS1SeqDescArray = 64  # offset
    m_localScaleSetArray = 184  # offset
    m_localSequenceNameArray = 40  # offset
    m_localSynthAnimDescArray = 112  # offset
    m_nFlags = 32  # offset
    m_sName = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSequenceTagSpans:
    m_sSequenceName = 0  # offset
    m_tags = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSequenceUpdateNode:
    m_duration = 124  # offset
    m_hSequence = 120  # offset
    m_paramSpans = 128  # offset
    m_tags = 152  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSequenceUpdateNodeBase:
    m_bLoop = 112  # offset
    m_playbackSpeed = 108  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSetParameterActionUpdater:
    m_hParam = 24  # offset
    m_value = 26  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSingleFrameUpdateNode:
    m_actions = 88  # offset
    m_flCycle = 120  # offset
    m_hPoseCacheHandle = 112  # offset
    m_hSequence = 116  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSlopeComponentUpdater:
    m_flTraceDistance = 52  # offset
    m_hSlopeAngle = 56  # offset
    m_hSlopeAngleFront = 58  # offset
    m_hSlopeAngleSide = 60  # offset
    m_hSlopeHeading = 62  # offset
    m_hSlopeNormal = 64  # offset
    m_hSlopeNormal_WorldSpace = 66  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSlowDownOnSlopesUpdateNode:
    m_flSlowDownStrength = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSolveIKChainUpdateNode:
    m_opFixedData = 136  # offset
    m_targetHandles = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSolveIKTargetHandle_t:
    m_orientationHandle = 2  # offset
    m_positionHandle = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSpeedScaleUpdateNode:
    m_paramIndex = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStanceOverrideUpdateNode:
    m_eMode = 156  # offset
    m_footStanceInfo = 112  # offset
    m_hParameter = 152  # offset
    m_pStanceSourceNode = 136  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStanceScaleUpdateNode:
    m_hParam = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStateActionUpdater:
    m_eBehavior = 8  # offset
    m_pAction = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStateMachineComponentUpdater:
    m_stateMachine = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStateMachineUpdateNode:
    m_bBlockWaningTags = 252  # offset
    m_bLockStateWhenWaning = 253  # offset
    m_bResetWhenActivated = 254  # offset
    m_stateData = 200  # offset
    m_stateMachine = 112  # offset
    m_transitionData = 224  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStateNodeStateData:
    m_bExclusiveRootMotion = 0  # offset
    m_bExclusiveRootMotionFirstFrame = 0  # offset
    m_pChild = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStateNodeTransitionData:
    m_bReset = 0  # offset
    m_blendDuration = 8  # offset
    m_curve = 0  # offset
    m_resetCycleOption = 0  # offset
    m_resetCycleValue = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStateUpdateData:
    m_actions = 40  # offset
    m_bIsEndState = 0  # offset
    m_bIsPassthrough = 0  # offset
    m_bIsPassthroughRootMotion = 0  # offset
    m_bIsStartState = 0  # offset
    m_bPreEvaluatePassthroughTransitionPath = 0  # offset
    m_hScript = 8  # offset
    m_name = 0  # offset
    m_stateID = 64  # offset
    m_transitionIndices = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStaticPoseCache:
    m_nBoneCount = 40  # offset
    m_nMorphCount = 44  # offset
    m_poses = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStaticPoseCacheBuilder:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStepsRemainingMetricEvaluator:
    m_flMinStepsRemaining = 104  # offset
    m_footIndices = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStopAtGoalUpdateNode:
    m_damping = 136  # offset
    m_flInnerRadius = 120  # offset
    m_flMaxScale = 124  # offset
    m_flMinScale = 128  # offset
    m_flOuterRadius = 116  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CStringAnimTag:
    pass

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

class CSubtractUpdateNode:
    m_bApplyChannelsSeparately = 153  # offset
    m_bApplyToFootMotion = 152  # offset
    m_bUseModelSpace = 154  # offset
    m_footMotionTiming = 148  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSymbolAnimParameter:
    m_defaultValue = 128  # offset

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

class CTargetSelectorUpdateNode:
    m_bEnablePhaseMatching = 142  # offset
    m_bTargetFacePositionIsWorldSpace = 141  # offset
    m_bTargetPositionIsWorldSpace = 140  # offset
    m_children = 104  # offset
    m_eAngleMode = 96  # offset
    m_flPhaseMatchingMaxRootMotionSkip = 144  # offset
    m_hDesiredMoveHeadingParameter = 138  # offset
    m_hMoveHeadingParameter = 136  # offset
    m_hTargetFacePositionParameter = 134  # offset
    m_hTargetPosition = 132  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTargetWarpUpdateNode:
    m_bOnlyWarpWhenTagIsFound = 142  # offset
    m_bTargetFacePositionIsWorldSpace = 140  # offset
    m_bTargetPositionIsWorldSpace = 141  # offset
    m_bWarpAroundCenter = 144  # offset
    m_bWarpOrientationDuringTranslation = 143  # offset
    m_eAngleMode = 116  # offset
    m_eCorrectionMethod = 132  # offset
    m_eTargetWarpTimingMethod = 136  # offset
    m_flMaxAngle = 148  # offset
    m_hDesiredMoveHeadingParameter = 128  # offset
    m_hMoveHeadingParameter = 126  # offset
    m_hTargetFacePositionParameter = 124  # offset
    m_hTargetPositionParameter = 120  # offset
    m_hTargetUpVectorParameter = 122  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTaskHandshakeAnimTag:
    pass

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

class CTaskStatusAnimTag:
    pass

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

class CTiltTwistConstraint:
    m_nSlaveAxis = 100  # offset
    m_nTargetAxis = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTimeRemainingMetricEvaluator:
    m_bFilterByTimeRemaining = 88  # offset
    m_bMatchByTimeRemaining = 80  # offset
    m_flMaxTimeRemaining = 84  # offset
    m_flMinTimeRemaining = 92  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CToggleComponentActionUpdater:
    m_bSetEnabled = 28  # offset
    m_componentID = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTransitionUpdateData:
    m_bDisabled = 0  # offset
    m_destStateIndex = 1  # offset
    m_nHandshakeMaskToDisableFirst = 0  # offset
    m_srcStateIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTurnHelperUpdateNode:
    m_bMatchChildDuration = 128  # offset
    m_bUseManualTurnOffset = 136  # offset
    m_facingTarget = 116  # offset
    m_manualTurnOffset = 132  # offset
    m_turnDuration = 124  # offset
    m_turnStartTimeOffset = 120  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTwistConstraint:
    m_bInverse = 96  # offset
    m_qChildBindRotation = 128  # offset
    m_qParentBindRotation = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CTwoBoneIKUpdateNode:
    m_opFixedData = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CUnaryUpdateNode:
    m_pChildNode = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVPhysXSurfacePropertiesList:
    m_surfacePropertiesList = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVectorAnimParameter:
    m_bInterpolate = 140  # offset
    m_defaultValue = 128  # offset

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

class CVectorQuantizer:
    m_centroidVectors = 0  # offset
    m_nCentroids = 24  # offset
    m_nDimensions = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVirtualAnimParameter:
    m_eParamType = 120  # offset
    m_expressionString = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CWarpSectionAnimTag:
    m_bWarpOrientation = 81  # offset
    m_bWarpPosition = 80  # offset

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

class CWarpSectionAnimTagBase:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CWayPointHelperUpdateNode:
    m_bOnlyGoals = 124  # offset
    m_bPreventOvershoot = 125  # offset
    m_bPreventUndershoot = 126  # offset
    m_flEndCycle = 120  # offset
    m_flStartCycle = 116  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CZeroPoseUpdateNode:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ChainToSolveData_t:
    m_DebugSetting = 56  # offset
    m_SolverSettings = 4  # offset
    m_TargetSettings = 16  # offset
    m_flDebugNormalizedValue = 60  # offset
    m_nChainIndex = 0  # offset
    m_vDebugOffset = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ConfigIndex:
    m_nConfig = 2  # offset
    m_nGroup = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class DynamicMeshDeformParams_t:
    m_bComputeDynamicMeshTensionAfterAnimation = 9  # offset
    m_bRecomputeSmoothNormalsAfterAnimation = 8  # offset
    m_bSmoothNormalsAcrossUvSeams = 10  # offset
    m_flTensionCompressScale = 0  # offset
    m_flTensionStretchScale = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FollowAttachmentData:
    m_attachmentHandle = 4  # offset
    m_boneIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FollowAttachmentSettings_t:
    m_attachment = 0  # offset
    m_attachmentHandle = 132  # offset
    m_bMatchRotation = 134  # offset
    m_bMatchTranslation = 133  # offset
    m_boneIndex = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FollowTargetOpFixedSettings_t:
    m_bBoneTarget = 4  # offset
    m_bMatchTargetOrientation = 13  # offset
    m_bWorldCoodinateTarget = 12  # offset
    m_boneIndex = 0  # offset
    m_boneTargetIndex = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FootFixedData_t:
    m_flMaxIKLength = 48  # offset
    m_flMaxRotationLeft = 60  # offset
    m_flMaxRotationRight = 64  # offset
    m_ikChainIndex = 44  # offset
    m_nAnkleBoneIndex = 36  # offset
    m_nFootIndex = 52  # offset
    m_nIKAnchorBoneIndex = 40  # offset
    m_nTagIndex = 56  # offset
    m_nTargetBoneIndex = 32  # offset
    m_vHeelOffset = 16  # offset
    m_vToeOffset = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FootFixedSettings:
    m_bEnableTracing = 48  # offset
    m_flFootBaseLength = 32  # offset
    m_flMaxRotationLeft = 36  # offset
    m_flMaxRotationRight = 40  # offset
    m_flTraceAngleBlend = 52  # offset
    m_footstepLandedTagIndex = 44  # offset
    m_nDisableTagIndex = 56  # offset
    m_nFootIndex = 60  # offset
    m_traceSettings = 0  # offset
    m_vFootBaseBindPosePositionMS = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FootLockPoseOpFixedSettings:
    m_bAlwaysUseFallbackHinge = 58  # offset
    m_bApplyFootRotationLimits = 59  # offset
    m_bApplyHipDrop = 57  # offset
    m_bApplyLegTwistLimits = 60  # offset
    m_bApplyTilt = 56  # offset
    m_bEnableLockBreaking = 76  # offset
    m_bEnableStretching = 88  # offset
    m_flExtensionScale = 68  # offset
    m_flLockBlendTime = 84  # offset
    m_flLockBreakTolerance = 80  # offset
    m_flMaxFootHeight = 64  # offset
    m_flMaxLegTwist = 72  # offset
    m_flMaxStretchAmount = 92  # offset
    m_flStretchExtensionScale = 96  # offset
    m_footInfo = 0  # offset
    m_hipDampingSettings = 24  # offset
    m_ikSolverType = 52  # offset
    m_nHipBoneIndex = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FootPinningPoseOpFixedData_t:
    m_bApplyFootRotationLimits = 41  # offset
    m_bApplyLegTwistLimits = 40  # offset
    m_flBlendTime = 24  # offset
    m_flLockBreakDistance = 28  # offset
    m_flMaxLegTwist = 32  # offset
    m_footInfo = 0  # offset
    m_nHipBoneIndex = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FootStepTrigger:
    m_nFootIndex = 24  # offset
    m_tags = 0  # offset
    m_triggerPhase = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class HSequence:
    m_Value = 0  # offset

class HitReactFixedSettings_t:
    m_flCounterRotationScale = 20  # offset
    m_flDistanceFadeScale = 24  # offset
    m_flHipBoneTranslationScale = 52  # offset
    m_flHipDipDelay = 64  # offset
    m_flHipDipImpactScale = 60  # offset
    m_flHipDipSpringStrength = 56  # offset
    m_flMaxAngleRadians = 44  # offset
    m_flMaxImpactForce = 8  # offset
    m_flMinImpactForce = 12  # offset
    m_flPropagationScale = 28  # offset
    m_flSpringStrength = 36  # offset
    m_flWhipDelay = 32  # offset
    m_flWhipImpactScale = 16  # offset
    m_flWhipSpringStrength = 40  # offset
    m_nEffectedBoneCount = 4  # offset
    m_nHipBoneIndex = 48  # offset
    m_nWeightListIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class IKBoneNameAndIndex_t:
    m_Name = 0  # offset

class IKDemoCaptureSettings_t:
    m_eMode = 8  # offset
    m_ikChainName = 16  # offset
    m_oneBoneEnd = 32  # offset
    m_oneBoneStart = 24  # offset
    m_parentBoneName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class IKSolverSettings_t:
    m_EndEffectorRotationFixUpMode = 8  # offset
    m_SolverType = 0  # offset
    m_nNumIterations = 4  # offset

class IKTargetSettings_t:
    m_AnimgraphParameterNameOrientation = 28  # offset
    m_AnimgraphParameterNamePosition = 24  # offset
    m_Bone = 8  # offset
    m_TargetCoordSystem = 32  # offset
    m_TargetSource = 0  # offset

class IParticleEffect:
    pass

class JiggleBoneSettingsList_t:
    m_boneSettings = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class JiggleBoneSettings_t:
    m_eSimSpace = 40  # offset
    m_flDamping = 12  # offset
    m_flMaxTimeStep = 8  # offset
    m_flSpringStrength = 4  # offset
    m_nBoneIndex = 0  # offset
    m_vBoundsMaxLS = 16  # offset
    m_vBoundsMinLS = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class LookAtBone_t:
    m_index = 0  # offset
    m_weight = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class LookAtOpFixedSettings_t:
    m_attachment = 0  # offset
    m_bMaintainUpDirection = 193  # offset
    m_bRotateYawForward = 192  # offset
    m_bTargetIsPosition = 194  # offset
    m_bUseHysteresis = 195  # offset
    m_bones = 152  # offset
    m_damping = 128  # offset
    m_flHysteresisInnerAngle = 184  # offset
    m_flHysteresisOuterAngle = 188  # offset
    m_flPitchLimit = 180  # offset
    m_flYawLimit = 176  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialGroup_t:
    m_materials = 8  # offset
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ModelBoneFlexDriverControl_t:
    m_flMax = 24  # offset
    m_flMin = 20  # offset
    m_flexController = 8  # offset
    m_flexControllerToken = 16  # offset
    m_nBoneComponent = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ModelBoneFlexDriver_t:
    m_boneName = 0  # offset
    m_boneNameToken = 8  # offset
    m_controls = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ModelEmbeddedMesh_t:
    m_Name = 0  # offset
    m_indexBuffers = 56  # offset
    m_nDataBlock = 20  # offset
    m_nMeshIndex = 16  # offset
    m_nMorphBlock = 24  # offset
    m_nToolsVBBlock = 108  # offset
    m_nVBIBBlock = 104  # offset
    m_toolsBuffers = 80  # offset
    m_vertexBuffers = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ModelMeshBufferData_t:
    m_bCompressedZSTD = 14  # offset
    m_bCreateBufferSRV = 15  # offset
    m_bCreateBufferUAV = 16  # offset
    m_bCreatePooledBuffer = 18  # offset
    m_bCreateRawBuffer = 17  # offset
    m_bMeshoptCompressed = 12  # offset
    m_bMeshoptIndexSequence = 13  # offset
    m_inputLayoutFields = 24  # offset
    m_nBlockIndex = 0  # offset
    m_nElementCount = 4  # offset
    m_nElementSizeInBytes = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ModelSkeletonData_t:
    m_boneName = 0  # offset
    m_bonePosParent = 96  # offset
    m_boneRotParent = 120  # offset
    m_boneScaleParent = 144  # offset
    m_boneSphere = 48  # offset
    m_nFlag = 72  # offset
    m_nParent = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MoodAnimationLayer_t:
    m_bActiveListening = 8  # offset
    m_bActiveTalking = 9  # offset
    m_bScaleWithInts = 56  # offset
    m_flDurationScale = 48  # offset
    m_flEndOffset = 76  # offset
    m_flFadeIn = 84  # offset
    m_flFadeOut = 88  # offset
    m_flIntensity = 40  # offset
    m_flNextStart = 60  # offset
    m_flStartOffset = 68  # offset
    m_layerAnimations = 16  # offset
    m_sName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyArrayElementNameKey",
            "type": "Unknown"
        }
    ]

class MoodAnimation_t:
    m_flWeight = 8  # offset
    m_sName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        },
        {
            "name": "MPropertyArrayElementNameKey",
            "type": "Unknown"
        }
    ]

class MotionBlendItem:
    m_flKeyValue = 8  # offset
    m_pChild = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MotionDBIndex:
    m_nIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MotionIndex:
    m_nGroup = 0  # offset
    m_nMotion = 2  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MovementGaitId_t:
    m_sId = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmBoneMaskSetDefinition_t:
    m_ID = 0  # offset
    m_primaryWeightList = 8  # offset
    m_secondaryWeightLists = 280  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmCompressionSettings_t:
    m_bIsRotationStatic = 48  # offset
    m_bIsScaleStatic = 50  # offset
    m_bIsTranslationStatic = 49  # offset
    m_constantRotation = 32  # offset
    m_scaleRange = 24  # offset
    m_translationRangeX = 0  # offset
    m_translationRangeY = 8  # offset
    m_translationRangeZ = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmCompressionSettings_t__QuantizationRange_t:
    m_flRangeLength = 4  # offset
    m_flRangeStart = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmFloatCurveCompressionSettings_t:
    m_bIsStatic = 8  # offset
    m_range = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmPercent_t:
    m_flValue = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmSyncTrackTimeRange_t:
    m_endTime = 8  # offset
    m_startTime = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NmSyncTrackTime_t:
    m_nEventIdx = 0  # offset
    m_percentageThrough = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PARTICLE_EHANDLE__:
    unused = 0  # offset

class PGDInstruction_t:
    m_nBlackboardReferenceIdx = 36  # offset
    m_nCallInfoIndex = 28  # offset
    m_nChunk = 20  # offset
    m_nCode = 0  # offset
    m_nConstIdx = 32  # offset
    m_nDestInstruction = 24  # offset
    m_nDomainValueIdx = 34  # offset
    m_nInvokeBindingIndex = 16  # offset
    m_nReg0 = 8  # offset
    m_nReg1 = 10  # offset
    m_nReg2 = 12  # offset
    m_nVar = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParamSpanSample_t:
    m_flCycle = 20  # offset
    m_value = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParamSpan_t:
    m_eParamType = 26  # offset
    m_flEndCycle = 32  # offset
    m_flStartCycle = 28  # offset
    m_hParam = 24  # offset
    m_samples = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticleNamedValueConfiguration_t:
    m_BoundEntityPath = 32  # offset
    m_ConfigName = 0  # offset
    m_ConfigValue = 8  # offset
    m_iAttachType = 24  # offset
    m_strAttachmentName = 48  # offset
    m_strEntityScope = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ParticleNamedValueSource_t:
    m_DefaultConfig = 16  # offset
    m_IsPublic = 8  # offset
    m_Name = 0  # offset
    m_NamedConfigs = 72  # offset
    m_ValueType = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PermModelDataAnimatedMaterialAttribute_t:
    m_AttributeName = 0  # offset
    m_nNumChannels = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PermModelData_t:
    m_AnimatedMaterialAttributes = 688  # offset
    m_BodyGroupsHiddenInTools = 640  # offset
    m_ExtParts = 96  # offset
    m_boneFlexDrivers = 608  # offset
    m_lodGroupSwitchDistances = 216  # offset
    m_materialGroups = 360  # offset
    m_meshGroups = 336  # offset
    m_modelInfo = 8  # offset
    m_modelSkeleton = 392  # offset
    m_nDefaultMeshGroupMask = 384  # offset
    m_name = 0  # offset
    m_pModelConfigList = 632  # offset
    m_refAnimGroups = 288  # offset
    m_refAnimIncludeModels = 664  # offset
    m_refLODGroupMasks = 192  # offset
    m_refMeshGroupMasks = 144  # offset
    m_refMeshes = 120  # offset
    m_refPhysGroupMasks = 168  # offset
    m_refPhysicsData = 240  # offset
    m_refPhysicsHitboxData = 264  # offset
    m_refSequenceGroups = 312  # offset
    m_remappingTable = 560  # offset
    m_remappingTableStarts = 584  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PermModelExtPart_t:
    m_Name = 32  # offset
    m_Transform = 0  # offset
    m_nParent = 40  # offset
    m_refModel = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PermModelInfo_t:
    m_flMass = 52  # offset
    m_flMaxEyeDeflection = 68  # offset
    m_keyValueText = 80  # offset
    m_nFlags = 0  # offset
    m_sSurfaceProperty = 72  # offset
    m_vEyePosition = 56  # offset
    m_vHullMax = 16  # offset
    m_vHullMin = 4  # offset
    m_vViewMax = 40  # offset
    m_vViewMin = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PhysShapeMarkup_t:
    m_nBodyInAggregate = 0  # offset
    m_nShapeInBody = 4  # offset
    m_sHitGroup = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PhysSoftbodyDesc_t:
    m_Capsules = 72  # offset
    m_InitPose = 96  # offset
    m_ParticleBoneHash = 0  # offset
    m_ParticleBoneName = 120  # offset
    m_Particles = 24  # offset
    m_Springs = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseCursorID_t:
    m_Value = 0  # offset

class PulseCursorYieldToken_t:
    m_Value = 0  # offset

class PulseDocNodeID_t:
    m_Value = 0  # offset

class PulseGraphExecutionHistoryCursorDesc_t:
    flLastReferenced = 32  # offset
    nLastValidEntryIdx = 36  # offset
    nRetiredAtNodeID = 28  # offset
    nSpawnNodeID = 24  # offset
    vecAncestorCursorIDs = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseGraphExecutionHistoryEntry_t:
    flExecTime = 8  # offset
    nCursorID = 0  # offset
    nEditorID = 4  # offset
    tagName = 16  # offset
    unFlags = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseGraphExecutionHistoryNodeDesc_t:
    strBindingName = 16  # offset
    strCellDesc = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PulseGraphInstanceID_t:
    m_Value = 0  # offset

class PulseRegisterMap_t:
    m_Inparams = 0  # offset
    m_InparamsWhichCanBeMoved = 16  # offset
    m_Outparams = 32  # offset

class PulseRuntimeBlackboardReferenceIndex_t:
    m_Value = 0  # offset

class PulseRuntimeCallInfoIndex_t:
    m_Value = 0  # offset

class PulseRuntimeCellIndex_t:
    m_Value = 0  # offset

class PulseRuntimeChunkIndex_t:
    m_Value = 0  # offset

class PulseRuntimeConstantIndex_t:
    m_Value = 0  # offset

class PulseRuntimeDomainValueIndex_t:
    m_Value = 0  # offset

class PulseRuntimeEntrypointIndex_t:
    m_Value = 0  # offset

class PulseRuntimeInvokeIndex_t:
    m_Value = 0  # offset

class PulseRuntimeOutputIndex_t:
    m_Value = 0  # offset

class PulseRuntimeRegisterIndex_t:
    m_Value = 0  # offset

class PulseRuntimeStateOffset_t:
    m_Value = 0  # offset

class PulseRuntimeVarIndex_t:
    m_Value = 0  # offset

class RenderHairStrandInfo_t:
    m_nDataOffset_Segments = 36  # offset
    m_nGuideHairIndices_nSurfaceTriIndex = 0  # offset
    m_nPackedBaseUv = 24  # offset
    m_nPackedSurfaceNormalOs = 28  # offset
    m_nPackedSurfaceTangentOs = 32  # offset
    m_vGuideBary_vBaseBary = 8  # offset
    m_vRootOffset_flLengthScale = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RenderSkeletonBone_t:
    m_bbox = 64  # offset
    m_boneName = 0  # offset
    m_flSphereRadius = 88  # offset
    m_invBindPose = 16  # offset
    m_parentName = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SampleCode:
    m_subCode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ScriptInfo_t:
    m_code = 0  # offset
    m_eScriptType = 80  # offset
    m_paramsModified = 8  # offset
    m_proxyReadParams = 32  # offset
    m_proxyWriteParams = 56  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonAnimCapture_t:
    m_CaptureName = 40  # offset
    m_FeModelInitPose = 72  # offset
    m_Frames = 168  # offset
    m_ImportedCollision = 8  # offset
    m_ModelBindPose = 48  # offset
    m_ModelName = 32  # offset
    m_bPredicted = 100  # offset
    m_nEntIndex = 0  # offset
    m_nEntParent = 4  # offset
    m_nFlexControllers = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonAnimCapture_t__Bone_t:
    m_BindPose = 16  # offset
    m_Name = 0  # offset
    m_nParent = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonAnimCapture_t__Camera_t:
    m_flTime = 32  # offset
    m_tmCamera = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonAnimCapture_t__FrameStamp_t:
    m_bPredicted = 9  # offset
    m_bTeleportTick = 8  # offset
    m_flCurTime = 12  # offset
    m_flEntitySimTime = 4  # offset
    m_flRealTime = 16  # offset
    m_flTime = 0  # offset
    m_nFrameCount = 20  # offset
    m_nTickCount = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonAnimCapture_t__Frame_t:
    m_CompositeBones = 72  # offset
    m_FeModelAnims = 120  # offset
    m_FeModelPos = 144  # offset
    m_FlexControllerWeights = 168  # offset
    m_SimStateBones = 96  # offset
    m_Stamp = 4  # offset
    m_Transform = 32  # offset
    m_bTeleport = 64  # offset
    m_flTime = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonBoneBounds_t:
    m_vecCenter = 0  # offset
    m_vecSize = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SkeletonDemoDb_t:
    m_AnimCaptures = 0  # offset
    m_CameraTrack = 24  # offset
    m_flRecordingTime = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SolveIKChainPoseOpFixedSettings_t:
    m_ChainsToSolveData = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class StanceInfo_t:
    m_flDirection = 12  # offset
    m_vPosition = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class TagSpan_t:
    m_endCycle = 8  # offset
    m_startCycle = 4  # offset
    m_tagIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class TraceSettings_t:
    m_flTraceHeight = 0  # offset
    m_flTraceRadius = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class TwoBoneIKSettings_t:
    m_bAlwaysUseFallbackHinge = 296  # offset
    m_bConstrainTwist = 333  # offset
    m_bMatchTargetOrientation = 332  # offset
    m_endEffectorAttachment = 16  # offset
    m_endEffectorType = 0  # offset
    m_flMaxTwist = 336  # offset
    m_hPositionParam = 292  # offset
    m_hRotationParam = 294  # offset
    m_nEndBoneIndex = 328  # offset
    m_nFixedBoneIndex = 320  # offset
    m_nMiddleBoneIndex = 324  # offset
    m_targetAttachment = 160  # offset
    m_targetBoneIndex = 288  # offset
    m_targetType = 144  # offset
    m_vLsFallbackHingeAxis = 304  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXAggregateData_t:
    m_bindPose = 104  # offset
    m_boneNames = 32  # offset
    m_boneParents = 232  # offset
    m_bonesHash = 8  # offset
    m_collisionAttributes = 280  # offset
    m_constraints2 = 176  # offset
    m_debugPartNames = 304  # offset
    m_embeddedKeyvalues = 328  # offset
    m_indexHash = 80  # offset
    m_indexNames = 56  # offset
    m_joints = 200  # offset
    m_nFlags = 0  # offset
    m_nRefCounter = 2  # offset
    m_pFeModel = 224  # offset
    m_parts = 128  # offset
    m_shapeMarkups = 152  # offset
    m_surfacePropertyHashes = 256  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXBodyPart_t:
    m_bOverrideMassCenter = 152  # offset
    m_flAngularDamping = 140  # offset
    m_flAngularDrag = 148  # offset
    m_flInertiaScale = 132  # offset
    m_flLinearDamping = 136  # offset
    m_flLinearDrag = 144  # offset
    m_flMass = 4  # offset
    m_nCollisionAttributeIndex = 128  # offset
    m_nFlags = 0  # offset
    m_nReserved = 130  # offset
    m_rnShape = 8  # offset
    m_vMassCenterOverride = 156  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXCollisionAttributes_t:
    m_CollisionGroup = 0  # offset
    m_CollisionGroupString = 80  # offset
    m_InteractAs = 8  # offset
    m_InteractAsStrings = 88  # offset
    m_InteractExclude = 56  # offset
    m_InteractExcludeStrings = 136  # offset
    m_InteractWith = 32  # offset
    m_InteractWithStrings = 112  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXConstraint2_t:
    m_nChild = 6  # offset
    m_nFlags = 0  # offset
    m_nParent = 4  # offset
    m_params = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXConstraintParams_t:
    m_anchor = 4  # offset
    m_axes = 28  # offset
    m_driveDampingSlerp = 232  # offset
    m_driveDampingSwing = 228  # offset
    m_driveDampingTwist = 224  # offset
    m_driveDampingX = 200  # offset
    m_driveDampingY = 204  # offset
    m_driveDampingZ = 208  # offset
    m_driveSpringSlerp = 220  # offset
    m_driveSpringSwing = 216  # offset
    m_driveSpringTwist = 212  # offset
    m_driveSpringX = 188  # offset
    m_driveSpringY = 192  # offset
    m_driveSpringZ = 196  # offset
    m_goalAngularVelocity = 176  # offset
    m_goalOrientation = 160  # offset
    m_goalPosition = 148  # offset
    m_linearLimitDamping = 80  # offset
    m_linearLimitRestitution = 72  # offset
    m_linearLimitSpring = 76  # offset
    m_linearLimitValue = 68  # offset
    m_maxForce = 60  # offset
    m_maxTorque = 64  # offset
    m_nFlags = 3  # offset
    m_nRotateMotion = 2  # offset
    m_nTranslateMotion = 1  # offset
    m_nType = 0  # offset
    m_projectionAngularTolerance = 244  # offset
    m_projectionLinearTolerance = 240  # offset
    m_solverIterationCount = 236  # offset
    m_swing1LimitDamping = 128  # offset
    m_swing1LimitRestitution = 120  # offset
    m_swing1LimitSpring = 124  # offset
    m_swing1LimitValue = 116  # offset
    m_swing2LimitDamping = 144  # offset
    m_swing2LimitRestitution = 136  # offset
    m_swing2LimitSpring = 140  # offset
    m_swing2LimitValue = 132  # offset
    m_twistHighLimitDamping = 112  # offset
    m_twistHighLimitRestitution = 104  # offset
    m_twistHighLimitSpring = 108  # offset
    m_twistHighLimitValue = 100  # offset
    m_twistLowLimitDamping = 96  # offset
    m_twistLowLimitRestitution = 88  # offset
    m_twistLowLimitSpring = 92  # offset
    m_twistLowLimitValue = 84  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXJoint_t:
    m_Frame1 = 16  # offset
    m_Frame2 = 48  # offset
    m_LinearLimit = 84  # offset
    m_SwingLimit = 116  # offset
    m_Tag = 192  # offset
    m_TwistLimit = 128  # offset
    m_bEnableAngularMotor = 136  # offset
    m_bEnableCollision = 80  # offset
    m_bEnableLinearLimit = 83  # offset
    m_bEnableLinearMotor = 92  # offset
    m_bEnableSwingLimit = 112  # offset
    m_bEnableTwistLimit = 124  # offset
    m_bIsAngularConstraintDisabled = 82  # offset
    m_bIsLinearConstraintDisabled = 81  # offset
    m_flAngularDampingRatio = 168  # offset
    m_flAngularFrequency = 164  # offset
    m_flElasticDamping = 180  # offset
    m_flElasticity = 176  # offset
    m_flFriction = 172  # offset
    m_flLinearDampingRatio = 160  # offset
    m_flLinearFrequency = 156  # offset
    m_flMaxForce = 108  # offset
    m_flMaxTorque = 152  # offset
    m_flPlasticity = 184  # offset
    m_nBody1 = 2  # offset
    m_nBody2 = 4  # offset
    m_nFlags = 6  # offset
    m_nType = 0  # offset
    m_vAngularTargetVelocity = 140  # offset
    m_vLinearTargetVelocity = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysXRange_t:
    m_flMax = 4  # offset
    m_flMin = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VPhysics2ShapeDef_t:
    m_CollisionAttributeIndices = 96  # offset
    m_capsules = 24  # offset
    m_hulls = 48  # offset
    m_meshes = 72  # offset
    m_spheres = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class WeightList:
    m_name = 0  # offset
    m_weights = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

