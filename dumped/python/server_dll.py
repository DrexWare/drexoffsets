# dumped by shxdows dumper (csdump)

from enum import Enum

class AmmoFlags_t(Enum):
    AMMO_FLAG_MAX = 2
    AMMO_FORCE_DROP_IF_CARRIED = 1
    AMMO_RESERVE_STAYS_WITH_WEAPON = 2

class AmmoPosition_t(Enum):
    AMMO_POSITION_COUNT = 2
    AMMO_POSITION_INVALID = -1
    AMMO_POSITION_PRIMARY = 0
    AMMO_POSITION_SECONDARY = 1

class AnimLoopMode_t(Enum):
    ANIM_LOOP_MODE_COUNT = 3
    ANIM_LOOP_MODE_INVALID = -1
    ANIM_LOOP_MODE_LOOPING = 1
    ANIM_LOOP_MODE_NOT_LOOPING = 0
    ANIM_LOOP_MODE_USE_SEQUENCE_SETTINGS = 2

class BaseExplosionTypes_t(Enum):
    EXPLOSION_TYPE_COUNT = 16
    EXPLOSION_TYPE_CUSTOM = 15
    EXPLOSION_TYPE_DEFAULT = 0
    EXPLOSION_TYPE_ELECTRICAL = 7
    EXPLOSION_TYPE_EMP = 8
    EXPLOSION_TYPE_EXPLOSIVEBARREL = 6
    EXPLOSION_TYPE_FIREWORKS = 3
    EXPLOSION_TYPE_FLASHBANG = 11
    EXPLOSION_TYPE_GASCAN = 4
    EXPLOSION_TYPE_GASCYLINDER = 5
    EXPLOSION_TYPE_GRENADE = 1
    EXPLOSION_TYPE_ICE = 13
    EXPLOSION_TYPE_MOLOTOV = 2
    EXPLOSION_TYPE_NONE = 14
    EXPLOSION_TYPE_SHRAPNEL = 9
    EXPLOSION_TYPE_SMOKEGRENADE = 10
    EXPLOSION_TYPE_TRIPMINE = 12

class BeamClipStyle_t(Enum):
    kBEAMCLIPSTYLE_NUMBITS = 2
    kGEOCLIP = 1
    kMODELCLIP = 2
    kNOCLIP = 0

class BeamType_t(Enum):
    BEAM_ENTPOINT = 2
    BEAM_ENTS = 3
    BEAM_HOSE = 4
    BEAM_INVALID = 0
    BEAM_LASER = 6
    BEAM_POINTS = 1
    BEAM_SPLINE = 5

class BeginDeathLifeStateTransition_t(Enum):
    TRANSITION_TO_LIFESTATE_DEAD = 1
    TRANSITION_TO_LIFESTATE_DYING = 0

class BloodType(Enum):
    ColorGreen = 2
    ColorRed = 0
    ColorRedLVL2 = 3
    ColorRedLVL3 = 4
    ColorRedLVL4 = 5
    ColorRedLVL5 = 6
    ColorRedLVL6 = 7
    ColorYellow = 1
    None = -1

class BreakableContentsType_t(Enum):
    BC_DEFAULT = 0
    BC_EMPTY = 1
    BC_PARTICLE_SYSTEM_OVERRIDE = 3
    BC_PROP_GROUP_OVERRIDE = 2

class BrushSolidities_e(Enum):
    BRUSHSOLID_ALWAYS = 2
    BRUSHSOLID_NEVER = 1
    BRUSHSOLID_TOGGLE = 0

class C4LightEffect_t(Enum):
    eLightEffectDropped = 1
    eLightEffectNone = 0
    eLightEffectThirdPersonHeld = 2

class CDebugOverlayCombinedTypes_t(Enum):
    ALL = 0
    ANY = 1
    COUNT = 2

class CDebugOverlayFilterTextType_t(Enum):
    COUNT = 3
    FILTER_TEXT_NONE = 0
    HIERARCHY = 2
    MATCH = 1

class CDebugOverlayFilterType_t(Enum):
    AI_EVENT = 7
    AI_PATHFINDING = 8
    AI_SCHEDULE = 5
    AI_TASK = 6
    COMBINED = -1
    COUNT = 3
    END_SIM_HISTORY_TYPES = 9
    ENTITY = 2
    NONE = 0
    TACTICAL_SEARCH = 4
    TEXT = 1

class CRR_Response__ResponseEnum_t(Enum):
    MAX_RESPONSE_NAME = 192
    MAX_RULE_NAME = 128

class CSPlayerBlockingUseAction_t(Enum):
    k_CSPlayerBlockingUseAction_DefusingDefault = 1
    k_CSPlayerBlockingUseAction_DefusingWithKit = 2
    k_CSPlayerBlockingUseAction_HostageDropping = 4
    k_CSPlayerBlockingUseAction_HostageGrabbing = 3
    k_CSPlayerBlockingUseAction_MapLongUseEntity_Pickup = 5
    k_CSPlayerBlockingUseAction_MapLongUseEntity_Place = 6
    k_CSPlayerBlockingUseAction_MaxCount = 7
    k_CSPlayerBlockingUseAction_None = 0

class CSPlayerState(Enum):
    NUM_PLAYER_STATES = 9
    STATE_ACTIVE = 0
    STATE_DEATH_ANIM = 4
    STATE_DEATH_WAIT_FOR_KEY = 5
    STATE_DORMANT = 8
    STATE_GUNGAME_RESPAWN = 7
    STATE_OBSERVER_MODE = 6
    STATE_PICKINGCLASS = 3
    STATE_PICKINGTEAM = 2
    STATE_WELCOME = 1

class CSWeaponCategory(Enum):
    WEAPONCATEGORY_COUNT = 6
    WEAPONCATEGORY_HEAVY = 5
    WEAPONCATEGORY_MELEE = 1
    WEAPONCATEGORY_OTHER = 0
    WEAPONCATEGORY_RIFLE = 4
    WEAPONCATEGORY_SECONDARY = 2
    WEAPONCATEGORY_SMG = 3

class CSWeaponMode(Enum):
    Primary_Mode = 0
    Secondary_Mode = 1
    WeaponMode_MAX = 2

class CSWeaponSilencerType(Enum):
    WEAPONSILENCER_DETACHABLE = 1
    WEAPONSILENCER_INTEGRATED = 2
    WEAPONSILENCER_NONE = 0

class CSWeaponType(Enum):
    WEAPONTYPE_C4 = 7
    WEAPONTYPE_EQUIPMENT = 10
    WEAPONTYPE_GRENADE = 9
    WEAPONTYPE_KNIFE = 0
    WEAPONTYPE_MACHINEGUN = 6
    WEAPONTYPE_PISTOL = 1
    WEAPONTYPE_RIFLE = 3
    WEAPONTYPE_SHOTGUN = 4
    WEAPONTYPE_SNIPER_RIFLE = 5
    WEAPONTYPE_STACKABLEITEM = 11
    WEAPONTYPE_SUBMACHINEGUN = 2
    WEAPONTYPE_TASER = 8
    WEAPONTYPE_UNKNOWN = 12

class CanPlaySequence_t(Enum):
    CANNOT_PLAY = 0
    CAN_PLAY_ENQUEUED = 2
    CAN_PLAY_NOW = 1

class ChatIgnoreType_t(Enum):
    CHAT_IGNORE_ALL = 1
    CHAT_IGNORE_NONE = 0
    CHAT_IGNORE_TEAM = 2

class ChickenActivity(Enum):
    FEED = 9
    GLIDE = 4
    IDLE = 0
    LAND = 5
    PANIC = 6
    RUN = 3
    SLEEP = 10
    SQUAT = 1
    TRICK = 7
    TURN_IN_PLACE = 8
    WALK = 2

class ChoreoLookAtMode_t(Enum):
    eChest = 0
    eEyesOnly = 2
    eHead = 1
    eInvalid = -1

class ChoreoLookAtSpeed_t(Enum):
    eFast = 2
    eInvalid = -1
    eMedium = 1
    eSlow = 0

class Class_T(Enum):
    CLASS_C4_FOR_RADAR = 3
    CLASS_DOOR = 11
    CLASS_FOOT_CONTACT_SHADOW = 4
    CLASS_HUDMODEL_ADDON = 9
    CLASS_HUDMODEL_ARMS = 8
    CLASS_HUDMODEL_WEAPON = 7
    CLASS_NONE = 0
    CLASS_PLANTED_C4 = 12
    CLASS_PLAYER = 1
    CLASS_PLAYER_ALLY = 2
    CLASS_WATER_SPLASHER = 6
    CLASS_WEAPON = 5
    CLASS_WORLDMODEL_GLOVES = 10
    NUM_CLASSIFY_CLASSES = 13

class DamageTypes_t(Enum):
    DMG_ACID = 262144
    DMG_BLAST = 64
    DMG_BLAST_SURFACE = 4194304
    DMG_BUCKSHOT = 2048
    DMG_BULLET = 2
    DMG_BURN = 8
    DMG_CLUB = 128
    DMG_CRUSH = 1
    DMG_DISSOLVE = 2097152
    DMG_DROWN = 16384
    DMG_DROWNRECOVER = 131072
    DMG_ENERGYBEAM = 1024
    DMG_FALL = 32
    DMG_GENERIC = 0
    DMG_HEADSHOT = 8388608
    DMG_LASTGENERICFLAG = 4194304
    DMG_PHYSGUN = 1048576
    DMG_POISON = 32768
    DMG_RADIATION = 65536
    DMG_SHOCK = 256
    DMG_SLASH = 4
    DMG_SONIC = 512
    DMG_VEHICLE = 16

class DebugOverlayBits_t(Enum):
    OVERLAY_ABSBOX_BIT = 32
    OVERLAY_ACTORNAME_BIT = 274877906944
    OVERLAY_ATTACHMENTS_BIT = 256
    OVERLAY_AUTOAIM_BIT = 65536
    OVERLAY_BBOX_BIT = 4
    OVERLAY_BUDDHA_MODE = 1073741824
    OVERLAY_HITBOX_BIT = 16384
    OVERLAY_INTERPOLATED_ATTACHMENTS_BIT = 512
    OVERLAY_INTERPOLATED_HITBOX_BIT = 32768
    OVERLAY_INTERPOLATED_PIVOT_BIT = 1024
    OVERLAY_INTERPOLATED_SKELETON_BIT = 4096
    OVERLAY_JOINT_INFO_BIT = 262144
    OVERLAY_MESSAGE_BIT = 16
    OVERLAY_MINIMAL_TEXT = 2199023255552
    OVERLAY_NAME_BIT = 2
    OVERLAY_NPC_ABILITY_RANGE_DEBUG_BIT = 1099511627776
    OVERLAY_NPC_BODYLOCATIONS = 67108864
    OVERLAY_NPC_COMBAT_BIT = 16777216
    OVERLAY_NPC_CONDITIONS_BIT = 8388608
    OVERLAY_NPC_CONDITIONS_TEXT_BIT = 549755813888
    OVERLAY_NPC_ENEMIES_BIT = 4194304
    OVERLAY_NPC_KILL_BIT = 268435456
    OVERLAY_NPC_RELATION_BIT = 17179869184
    OVERLAY_NPC_ROUTE_BIT = 524288
    OVERLAY_NPC_SCRIPTED_COMMANDS_BIT = 137438953472
    OVERLAY_NPC_SELECTED_BIT = 131072
    OVERLAY_NPC_STEERING_REGULATIONS = 2147483648
    OVERLAY_NPC_TASK_BIT = 33554432
    OVERLAY_NPC_TASK_TEXT_BIT = 4294967296
    OVERLAY_NPC_VIEWCONE_BIT = 134217728
    OVERLAY_PIVOT_BIT = 8
    OVERLAY_PROP_DEBUG = 8589934592
    OVERLAY_RBOX_BIT = 64
    OVERLAY_SHOW_BLOCKSLOS = 128
    OVERLAY_SKELETON_BIT = 2048
    OVERLAY_TEXT_BIT = 1
    OVERLAY_TRIGGER_BOUNDS_BIT = 8192
    OVERLAY_VCOLLIDE_WIREFRAME_BIT = 68719476736
    OVERLAY_VIEWOFFSET = 34359738368
    OVERLAY_VISIBILITY_TRACES_BIT = 1048576

class DecalFlags_t(Enum):
    eAll = 4294967295
    eAllButCannotClear = 4294967294
    eCannotClear = 1
    eNone = 0

class DecalMode_t(Enum):
    kDecalBlood = 0
    kDecalCloak = 1
    kDecalDefault = 0
    kDecalMax = 2

class DestructiblePartDestructionDeathBehavior_t(Enum):
    eDoNotKill = 0
    eGib = 2
    eKill = 1
    eRemove = 3

class Disposition_t(Enum):
    D_ER = 0
    D_ERROR = 0
    D_FEAR = 2
    D_FR = 2
    D_HATE = 1
    D_HT = 1
    D_LI = 3
    D_LIKE = 3
    D_NEUTRAL = 4
    D_NU = 4

class DoorState_t(Enum):
    DOOR_STATE_AJAR = 4
    DOOR_STATE_CLOSED = 0
    DOOR_STATE_CLOSING = 3
    DOOR_STATE_OPEN = 2
    DOOR_STATE_OPENING = 1

class EContributionScoreFlag_t(Enum):
    k_EContributionScoreFlag_Bullets = 2
    k_EContributionScoreFlag_Default = 0
    k_EContributionScoreFlag_Objective = 1

class EDestructiblePartDamagePassThroughType(Enum):
    Absorb = 1
    InvincibleAbsorb = 2
    InvinciblePassthrough = 3
    Normal = 0

class EDestructiblePartRadiusDamageApplyType(Enum):
    PrioritizeClosestPart = 1
    ScaleByExplosionRadius = 0

class EDestructibleParts_DestroyParameterFlags(Enum):
    Default = 3
    EnableFlinches = 2
    ForceDamageApply = 4
    GenerateBreakpieces = 1
    IgnoreHealthCheck = 16
    IgnoreKillEntityFlag = 8
    None = 0

class EInButtonState(Enum):
    IN_BUTTON_DOWN = 1
    IN_BUTTON_DOWN_UP = 2
    IN_BUTTON_DOWN_UP_DOWN = 5
    IN_BUTTON_DOWN_UP_DOWN_UP = 6
    IN_BUTTON_STATE_COUNT = 8
    IN_BUTTON_UP = 0
    IN_BUTTON_UP_DOWN = 3
    IN_BUTTON_UP_DOWN_UP = 4
    IN_BUTTON_UP_DOWN_UP_DOWN = 7

class EKillTypes_t(Enum):
    KILLTYPE_COUNT = 7
    KILL_BLAST = 3
    KILL_BURN = 4
    KILL_DEFAULT = 1
    KILL_HEADSHOT = 2
    KILL_NONE = 0
    KILL_SHOCK = 6
    KILL_SLASH = 5

class EOverrideBlockLOS_t(Enum):
    BLOCK_LOS_DEFAULT = 0
    BLOCK_LOS_FORCE_FALSE = 1
    BLOCK_LOS_FORCE_TRUE = 2

class EProceduralRagdollWeightIndexPropagationMethod(Enum):
    Bone = 0
    BoneAndChildren = 1

class EntFinderMethod_t(Enum):
    ENT_FIND_METHOD_FARTHEST = 1
    ENT_FIND_METHOD_NEAREST = 0
    ENT_FIND_METHOD_RANDOM = 2

class EntityAttachmentType_t(Enum):
    eAbsOrigin = 0
    eAttachment = 3
    eCenter = 1
    eEyes = 2

class EntityDisolveType_t(Enum):
    ENTITY_DISSOLVE_CORE = 3
    ENTITY_DISSOLVE_ELECTRICAL = 1
    ENTITY_DISSOLVE_ELECTRICAL_LIGHT = 2
    ENTITY_DISSOLVE_INVALID = -1
    ENTITY_DISSOLVE_NORMAL = 0

class EntityDistanceMode_t(Enum):
    eAxisToAxis = 2
    eCenterToCenter = 1
    eOriginToOrigin = 0

class EntityEffects_t(Enum):
    DEPRICATED_EF_NOINTERP = 8
    EF_MAX_BITS = 10
    EF_NODRAW = 32
    EF_NODRAW_BUT_TRANSMIT = 1024
    EF_NORECEIVESHADOW = 64
    EF_NOSHADOW = 16
    EF_PARENT_ANIMATES = 512

class EntityPlatformTypes_t(Enum):
    ENTITY_NOT_PLATFORM = 0
    ENTITY_PLATFORM_PLAYER_FOLLOWS_YAW = 1
    ENTITY_PLATFORM_PLAYER_IGNORES_YAW = 2

class EntitySubclassScope_t(Enum):
    SUBCLASS_SCOPE_COUNT = 2
    SUBCLASS_SCOPE_NONE = -1
    SUBCLASS_SCOPE_PLAYER_WEAPONS = 1
    SUBCLASS_SCOPE_PRECIPITATION = 0

class Explosions(Enum):
    expDirected = 1
    expRandom = 0
    expUsePrecise = 2

class FixAngleSet_t(Enum):
    Absolute = 1
    None = 0
    Relative = 2

class Flags_t(Enum):
    FL_AIMTARGET = 65536
    FL_ATCONTROLS = 64
    FL_BASEVELOCITY = 8388608
    FL_BOT = 16
    FL_CLIENT = 128
    FL_CONVEYOR = 16777216
    FL_DISSOLVING = 268435456
    FL_DONTTOUCH = 4194304
    FL_DUCKING = 2
    FL_FAKECLIENT = 256
    FL_FLY = 1024
    FL_FROZEN = 32
    FL_GODMODE = 16384
    FL_GRENADE = 1048576
    FL_IN_VEHICLE = 4096
    FL_NOTARGET = 32768
    FL_OBJECT = 33554432
    FL_ONFIRE = 134217728
    FL_ONGROUND = 1
    FL_STATICPROP = 262144
    FL_SUPPRESS_SAVE = 2048
    FL_TRANSRAGDOLL = 536870912
    FL_UNBLOCKABLE_BY_PLAYER = 1073741824
    FL_WATERJUMP = 4

class ForcedCrouchState_t(Enum):
    FORCEDCROUCH_CROUCHED = 1
    FORCEDCROUCH_NONE = 0
    FORCEDCROUCH_UNCROUCHED = 2

class FuncDoorSpawnPos_t(Enum):
    FUNC_DOOR_SPAWN_CLOSED = 0
    FUNC_DOOR_SPAWN_OPEN = 1

class GameAnimEventIndex_t(Enum):
    AE_BODYGROUP_SET_VALUE = 16
    AE_CL_CLOTH_ATTR = 19
    AE_CL_CLOTH_EFFECT = 22
    AE_CL_CLOTH_GROUND_OFFSET = 20
    AE_CL_CLOTH_STIFFEN = 21
    AE_CL_CREATE_ANIM_SCOPE_PROP = 23
    AE_CL_CREATE_PARTICLE_EFFECT = 7
    AE_CL_CREATE_PARTICLE_EFFECT_CFG = 9
    AE_CL_DISABLE_BODYGROUP = 15
    AE_CL_EJECT_MAG = 37
    AE_CL_ENABLE_BODYGROUP = 14
    AE_CL_PLAYSOUND = 1
    AE_CL_PLAYSOUND_ATTACHMENT = 2
    AE_CL_PLAYSOUND_LOOPING = 6
    AE_CL_PLAYSOUND_POSITION = 3
    AE_CL_STOPSOUND = 5
    AE_CL_STOP_PARTICLE_EFFECT = 8
    AE_CL_STOP_RAGDOLL_CONTROL = 13
    AE_CL_WEAPON_TRANSITION_INTO_HAND = 34
    AE_DESTRUCTIBLE_PART_DESTROY = 33
    AE_DISABLE_PLATFORM = 30
    AE_EMPTY = 0
    AE_ENABLE_PLATFORM_PLAYER_FOLLOWS_YAW = 31
    AE_ENABLE_PLATFORM_PLAYER_IGNORES_YAW = 32
    AE_FIRE_INPUT = 18
    AE_FOOTSTEP = 12
    AE_GRENADE_THROW_COMPLETE = 40
    AE_PULSE_GRAPH = 25
    AE_PULSE_GRAPH_AIMAT = 27
    AE_PULSE_GRAPH_IKLOCKLEFTARM = 28
    AE_PULSE_GRAPH_IKLOCKRIGHTARM = 29
    AE_PULSE_GRAPH_LOOKAT = 26
    AE_SV_ATTACH_SILENCER_COMPLETE = 35
    AE_SV_CREATE_PARTICLE_EFFECT_CFG = 10
    AE_SV_DETACH_SILENCER_COMPLETE = 36
    AE_SV_IKLOCK = 24
    AE_SV_PLAYSOUND = 4
    AE_SV_STOP_PARTICLE_EFFECT = 11
    AE_WEAPON_PERFORM_ATTACK = 17
    AE_WPN_COMPLETE_RELOAD = 38
    AE_WPN_HEALTHSHOT_INJECT = 39

class GrenadeType_t(Enum):
    GRENADE_TYPE_DECOY = 3
    GRENADE_TYPE_EXPLOSIVE = 0
    GRENADE_TYPE_FIRE = 2
    GRENADE_TYPE_FLASH = 1
    GRENADE_TYPE_SMOKE = 4
    GRENADE_TYPE_TOTAL = 5

class HierarchyType_t(Enum):
    HIERARCHY_ABSORIGIN = 3
    HIERARCHY_ATTACHMENT = 2
    HIERARCHY_BONE = 4
    HIERARCHY_BONE_MERGE = 1
    HIERARCHY_NONE = 0
    HIERARCHY_TYPE_COUNT = 5

class HitGroup_t(Enum):
    HITGROUP_CHEST = 2
    HITGROUP_COUNT = 12
    HITGROUP_GEAR = 10
    HITGROUP_GENERIC = 0
    HITGROUP_HEAD = 1
    HITGROUP_INVALID = -1
    HITGROUP_LEFTARM = 4
    HITGROUP_LEFTLEG = 6
    HITGROUP_NECK = 8
    HITGROUP_RIGHTARM = 5
    HITGROUP_RIGHTLEG = 7
    HITGROUP_SPECIAL = 11
    HITGROUP_STOMACH = 3
    HITGROUP_UNUSED = 9

class HoverPoseFlags_t(Enum):
    eAngles = 2
    eNone = 0
    ePosition = 1

class Hull_t(Enum):
    HULL_HUMAN = 0
    HULL_LARGE = 6
    HULL_LARGE_CENTERED = 7
    HULL_MEDIUM = 4
    HULL_MEDIUM_TALL = 8
    HULL_NONE = 11
    HULL_SMALL = 9
    HULL_SMALL_CENTERED = 1
    HULL_TINY = 3
    HULL_TINY_CENTERED = 5
    HULL_WIDE_HUMAN = 2
    NUM_HULLS = 10

class IChoreoServices__ChoreoState_t(Enum):
    STATE_PLAY_SCRIPT = 4
    STATE_PLAY_SCRIPT_POST_IDLE = 5
    STATE_PLAY_SCRIPT_POST_IDLE_DONE = 6
    STATE_PRE_SCRIPT = 0
    STATE_SYNCHRONIZE_SCRIPT = 3
    STATE_WAIT_FOR_SCRIPT = 1
    STATE_WALK_TO_MARK = 2

class IChoreoServices__ScriptState_t(Enum):
    SCRIPT_CLEANUP = 3
    SCRIPT_MOVE_TO_MARK = 4
    SCRIPT_PLAYING = 0
    SCRIPT_POST_IDLE = 2
    SCRIPT_WAIT = 1

class InputBitMask_t(Enum):
    IN_ALL = -1
    IN_ATTACK = 1
    IN_ATTACK2 = 2048
    IN_BACK = 16
    IN_DUCK = 4
    IN_FIRST_MOD_SPECIFIC_BIT = 4294967296
    IN_FORWARD = 8
    IN_JOYAUTOSPRINT = 131072
    IN_JUMP = 2
    IN_LOOK_AT_WEAPON = 34359738368
    IN_MOVELEFT = 512
    IN_MOVERIGHT = 1024
    IN_NONE = 0
    IN_RELOAD = 8192
    IN_SCORE = 8589934592
    IN_SPEED = 65536
    IN_TURNLEFT = 128
    IN_TURNRIGHT = 256
    IN_USE = 32
    IN_USEORRELOAD = 4294967296
    IN_ZOOM = 17179869184

class ItemFlagTypes_t(Enum):
    ITEM_FLAG_CAN_SELECT_WITHOUT_AMMO = 1
    ITEM_FLAG_DOHITLOCATIONDMG = 32
    ITEM_FLAG_EXHAUSTIBLE = 16
    ITEM_FLAG_LIMITINWORLD = 8
    ITEM_FLAG_NOAMMOPICKUPS = 64
    ITEM_FLAG_NOAUTORELOAD = 2
    ITEM_FLAG_NOAUTOSWITCHEMPTY = 4
    ITEM_FLAG_NOITEMPICKUP = 128
    ITEM_FLAG_NONE = 0

class LatchDirtyPermission_t(Enum):
    LATCH_DIRTY_CLIENT_SIMULATED = 2
    LATCH_DIRTY_DISALLOW = 0
    LATCH_DIRTY_FRAMESIMULATE = 4
    LATCH_DIRTY_PARTICLE_SIMULATE = 5
    LATCH_DIRTY_PREDICTION = 3
    LATCH_DIRTY_SERVER_CONTROLLED = 1

class LessonPanelLayoutFileTypes_t(Enum):
    LAYOUT_CUSTOM = 2
    LAYOUT_HAND_DEFAULT = 0
    LAYOUT_WORLD_DEFAULT = 1

class LifeState_t(Enum):
    LIFE_ALIVE = 0
    LIFE_DEAD = 2
    LIFE_DYING = 1
    LIFE_RESPAWNABLE = 3
    LIFE_RESPAWNING = 4

class Materials(Enum):
    matCeilingTile = 5
    matCinderBlock = 4
    matComputer = 6
    matFlesh = 3
    matGlass = 0
    matLastMaterial = 11
    matMetal = 2
    matNone = 10
    matRocks = 8
    matUnbreakableGlass = 7
    matWeb = 9
    matWood = 1

class MedalRank_t(Enum):
    MEDAL_RANK_BRONZE = 1
    MEDAL_RANK_COUNT = 4
    MEDAL_RANK_GOLD = 3
    MEDAL_RANK_NONE = 0
    MEDAL_RANK_SILVER = 2

class ModifyDamageReturn_t(Enum):
    ABORT_DO_NOT_APPLY_DAMAGE = 1
    CONTINUE_TO_APPLY_DAMAGE = 0

class MoveCollide_t(Enum):
    MOVECOLLIDE_COUNT = 4
    MOVECOLLIDE_DEFAULT = 0
    MOVECOLLIDE_FLY_BOUNCE = 1
    MOVECOLLIDE_FLY_CUSTOM = 2
    MOVECOLLIDE_FLY_SLIDE = 3
    MOVECOLLIDE_MAX_BITS = 3

class MoveLinearAuthoredPos_t(Enum):
    MOVELINEAR_AUTHORED_AT_CLOSED_POSITION = 2
    MOVELINEAR_AUTHORED_AT_OPEN_POSITION = 1
    MOVELINEAR_AUTHORED_AT_START_POSITION = 0

class MoveMountingAmount_t(Enum):
    MOVE_MOUNT_HIGH = 2
    MOVE_MOUNT_LOW = 1
    MOVE_MOUNT_MAXCOUNT = 3
    MOVE_MOUNT_NONE = 0

class MoveType_t(Enum):
    MOVETYPE_CUSTOM = 10
    MOVETYPE_FLY = 3
    MOVETYPE_FLYGRAVITY = 4
    MOVETYPE_INVALID = 11
    MOVETYPE_LADDER = 9
    MOVETYPE_LAST = 11
    MOVETYPE_MAX_BITS = 5
    MOVETYPE_NOCLIP = 7
    MOVETYPE_NONE = 0
    MOVETYPE_OBSERVER = 8
    MOVETYPE_OBSOLETE = 1
    MOVETYPE_PUSH = 6
    MOVETYPE_VPHYSICS = 5
    MOVETYPE_WALK = 2

class NPCFollowFormation_t(Enum):
    CloseCircle = 0
    Default = -1
    MediumCircle = 5
    Sidekick = 6
    WideCircle = 1

class NavAttributeEnum(Enum):
    NAV_ATTR_FIRST_GAME_INDEX = 19
    NAV_ATTR_LAST_INDEX = 63
    NAV_MESH_AVOID = 128
    NAV_MESH_CRAWL_HEIGHT = 262144
    NAV_MESH_CROUCH = 65536
    NAV_MESH_CROUCH_HEIGHT = 65536
    NAV_MESH_DONT_HIDE = 512
    NAV_MESH_JUMP = 2
    NAV_MESH_NON_ZUP = 32768
    NAV_MESH_NON_ZUP_TRANSITION = 131072
    NAV_MESH_NO_HOSTAGES = 2048
    NAV_MESH_NO_JUMP = 8
    NAV_MESH_NO_MERGE = 8192
    NAV_MESH_OBSTACLE_TOP = 16384
    NAV_MESH_RUN = 32
    NAV_MESH_STAIRS = 4096
    NAV_MESH_STAND = 1024
    NAV_MESH_STOP = 16
    NAV_MESH_TRANSIENT = 256
    NAV_MESH_WALK = 64

class NavDirType(Enum):
    EAST = 1
    NORTH = 0
    NUM_NAV_DIR_TYPE_DIRECTIONS = 4
    SOUTH = 2
    WEST = 3

class NavScopeFlags_t(Enum):
    eAir = 2
    eAll = 3
    eGround = 1
    eNone = 0

class NavScope_t(Enum):
    eAir = 1
    eCount = 2
    eFirst = 0
    eGround = 0
    eInvalid = 255

class ObserverInterpState_t(Enum):
    OBSERVER_INTERP_NONE = 0
    OBSERVER_INTERP_SETTLING = 3
    OBSERVER_INTERP_STARTING = 1
    OBSERVER_INTERP_TRAVELING = 2

class ObserverMode_t(Enum):
    NUM_OBSERVER_MODES = 5
    OBS_MODE_CHASE = 3
    OBS_MODE_FIXED = 1
    OBS_MODE_IN_EYE = 2
    OBS_MODE_NONE = 0
    OBS_MODE_ROAMING = 4

class OnFrame(Enum):
    ONFRAME_FALSE = 2
    ONFRAME_TRUE = 1
    ONFRAME_UNKNOWN = 0

class PerformanceMode_t(Enum):
    PM_NORMAL = 0
    PM_NO_GIBS = 1

class PlayerConnectedState(Enum):
    PlayerConnected = 0
    PlayerConnecting = 1
    PlayerDisconnected = 4
    PlayerDisconnecting = 3
    PlayerNeverConnected = -1
    PlayerReconnecting = 2
    PlayerReserved = 5

class PointOrientConstraint_t(Enum):
    eNone = 0
    ePreserveUpAxis = 1

class PointOrientGoalDirectionType_t(Enum):
    eAbsOrigin = 0
    eCenter = 1
    eEyesForward = 4
    eForward = 3
    eHead = 2

class PointTemplateClientOnlyEntityBehavior_t(Enum):
    CREATE_FOR_CLIENTS_WHO_CONNECT_LATER = 1
    CREATE_FOR_CURRENTLY_CONNECTED_CLIENTS_ONLY = 0

class PointTemplateOwnerSpawnGroupType_t(Enum):
    INSERT_INTO_CURRENTLY_ACTIVE_SPAWN_GROUP = 1
    INSERT_INTO_NEWLY_CREATED_SPAWN_GROUP = 2
    INSERT_INTO_POINT_TEMPLATE_SPAWN_GROUP = 0

class PointWorldTextJustifyHorizontal_t(Enum):
    POINT_WORLD_TEXT_JUSTIFY_HORIZONTAL_CENTER = 1
    POINT_WORLD_TEXT_JUSTIFY_HORIZONTAL_LEFT = 0
    POINT_WORLD_TEXT_JUSTIFY_HORIZONTAL_RIGHT = 2

class PointWorldTextJustifyVertical_t(Enum):
    POINT_WORLD_TEXT_JUSTIFY_VERTICAL_BOTTOM = 0
    POINT_WORLD_TEXT_JUSTIFY_VERTICAL_CENTER = 1
    POINT_WORLD_TEXT_JUSTIFY_VERTICAL_TOP = 2

class PointWorldTextReorientMode_t(Enum):
    POINT_WORLD_TEXT_REORIENT_AROUND_UP = 1
    POINT_WORLD_TEXT_REORIENT_NONE = 0

class PreviewCharacterMode(Enum):
    BANNER = 9
    BUY_MENU = 2
    DIORAMA = 0
    END_OF_MATCH = 4
    INVENTORY_INSPECT = 5
    MAIN_MENU = 1
    TEAM_INTRO = 7
    TEAM_SELECT = 3
    WALKING = 6
    WINGMAN_INTRO = 8

class PreviewEOMCelebration(Enum):
    AVA_DEFEAT = 12
    CRASSWATER_DEFEAT = 18
    DARRYL_DEFEAT = 19
    DOCTOR_DEFEAT = 20
    DROPDOWN = 3
    GENDARMERIE = 9
    GENDARMERIE_DEFEAT = 13
    GUERILLA = 7
    GUERILLA02 = 8
    MAE_DEFEAT = 14
    MASK_F = 6
    MUHLIK_DEFEAT = 21
    PUNCHING = 1
    RICKSAW_DEFEAT = 15
    SCUBA_FEMALE = 10
    SCUBA_FEMALE_DEFEAT = 16
    SCUBA_MALE = 11
    SCUBA_MALE_DEFEAT = 17
    STRETCH = 4
    SWAGGER = 2
    SWAT_FEMALE = 5
    VYPA_DEFEAT = 22
    WALKUP = 0

class PreviewWeaponState(Enum):
    DEPLOYED = 2
    DROPPED = 0
    HOLSTERED = 1
    ICON = 5
    INSPECT = 4
    PLANTED = 3

class PropDoorRotatingOpenDirection_e(Enum):
    DOOR_ROTATING_OPEN_BACKWARD = 2
    DOOR_ROTATING_OPEN_BOTH_WAYS = 0
    DOOR_ROTATING_OPEN_FORWARD = 1

class PropDoorRotatingSpawnPos_t(Enum):
    DOOR_SPAWN_AJAR = 3
    DOOR_SPAWN_CLOSED = 0
    DOOR_SPAWN_OPEN_BACK = 2
    DOOR_SPAWN_OPEN_FORWARD = 1

class PulseCollisionGroup_t(Enum):
    DEFAULT = 0

class PulseNPCCondition_t(Enum):
    COND_HEAR_PLAYER = 3
    COND_LOST_PLAYER = 2
    COND_NO_PRIMARY_AMMO = 5
    COND_PLAYER_PUSHING = 4
    COND_SEE_PLAYER = 1

class PulseTraceContents_t(Enum):
    SOLID = 1
    STATIC_LEVEL = 0

class QuestProgress__Reason(Enum):
    QUEST_NONINITIALIZED = 0
    QUEST_NONOFFICIAL_SERVER = 5
    QUEST_NOT_CONNECTED_TO_STEAM = 4
    QUEST_NOT_ENOUGH_PLAYERS = 2
    QUEST_NOT_SYNCED_WITH_SERVER = 11
    QUEST_NO_ENTITLEMENT = 6
    QUEST_NO_QUEST = 7
    QUEST_OK = 1
    QUEST_PLAYER_IS_BOT = 8
    QUEST_REASON_MAX = 12
    QUEST_WARMUP = 3
    QUEST_WRONG_MAP = 9
    QUEST_WRONG_MODE = 10

class RelativeLocationType_t(Enum):
    RELATIVE_TO_ENTITY_IN_LOCAL_SPACE = 1
    RELATIVE_TO_ENTITY_IN_WORLD_SPACE = 3
    RELATIVE_TO_ENTITY_YAW_ONLY = 2
    WORLD_SPACE_POSITION = 0

class RenderFx_t(Enum):
    kRenderFxFadeFast = 6
    kRenderFxFadeIn = 16
    kRenderFxFadeOut = 15
    kRenderFxFadeSlow = 5
    kRenderFxFlickerFast = 13
    kRenderFxFlickerSlow = 12
    kRenderFxGlowShell = 18
    kRenderFxMax = 19
    kRenderFxNoDissipation = 14
    kRenderFxNone = 0
    kRenderFxPulseFast = 2
    kRenderFxPulseFastWide = 4
    kRenderFxPulseFastWider = 17
    kRenderFxPulseSlow = 1
    kRenderFxPulseSlowWide = 3
    kRenderFxSolidFast = 8
    kRenderFxSolidSlow = 7
    kRenderFxStrobeFast = 10
    kRenderFxStrobeFaster = 11
    kRenderFxStrobeSlow = 9

class RenderMode_t(Enum):
    kRenderDevVisualizer = 11
    kRenderEnvironmental = 6
    kRenderGlow = 3
    kRenderModeCount = 12
    kRenderNone = 10
    kRenderNormal = 0
    kRenderTransAdd = 5
    kRenderTransAddFrameBlend = 7
    kRenderTransAlpha = 4
    kRenderTransAlphaAdd = 8
    kRenderTransColor = 1
    kRenderTransTexture = 2
    kRenderWorldGlow = 9

class RotatorTargetSpace_t(Enum):
    ROTATOR_TARGET_LOCALSPACE = 1
    ROTATOR_TARGET_WORLDSPACE = 0

class RumbleEffect_t(Enum):
    NUM_RUMBLE_EFFECTS = 25
    RUMBLE_357 = 2
    RUMBLE_AIRBOAT_GUN = 10
    RUMBLE_AR2 = 4
    RUMBLE_AR2_ALT_FIRE = 7
    RUMBLE_CROWBAR_SWING = 9
    RUMBLE_DMG_HIGH = 17
    RUMBLE_DMG_LOW = 15
    RUMBLE_DMG_MED = 16
    RUMBLE_FALL_LONG = 18
    RUMBLE_FALL_SHORT = 19
    RUMBLE_FLAT_BOTH = 14
    RUMBLE_FLAT_LEFT = 12
    RUMBLE_FLAT_RIGHT = 13
    RUMBLE_INVALID = -1
    RUMBLE_JEEP_ENGINE_LOOP = 11
    RUMBLE_PHYSCANNON_HIGH = 24
    RUMBLE_PHYSCANNON_LOW = 22
    RUMBLE_PHYSCANNON_MEDIUM = 23
    RUMBLE_PHYSCANNON_OPEN = 20
    RUMBLE_PHYSCANNON_PUNT = 21
    RUMBLE_PISTOL = 1
    RUMBLE_RPG_MISSILE = 8
    RUMBLE_SHOTGUN_DOUBLE = 6
    RUMBLE_SHOTGUN_SINGLE = 5
    RUMBLE_SMG1 = 3
    RUMBLE_STOP_ALL = 0

class SceneOnPlayerDeath_t(Enum):
    SCENE_ONPLAYERDEATH_CANCEL = 1
    SCENE_ONPLAYERDEATH_DO_NOTHING = 0

class ScriptedConflictResponse_t(Enum):
    SS_CONFLICT_ENQUEUE = 0
    SS_CONFLICT_INTERRUPT = 1

class ScriptedOnDeath_t(Enum):
    SS_ONDEATH_ANIMATED_DEATH = 2
    SS_ONDEATH_NOT_APPLICABLE = -1
    SS_ONDEATH_RAGDOLL = 1
    SS_ONDEATH_UNDEFINED = 0

class SequenceFinishNotifyState_t(Enum):
    eDoNotNotify = 0
    eNotifyTriggered = 2
    eNotifyWhenFinished = 1

class ShadowType_t(Enum):
    SHADOWS_NONE = 0
    SHADOWS_SIMPLE = 1

class ShakeCommand_t(Enum):
    SHAKE_AMPLITUDE = 2
    SHAKE_FREQUENCY = 3
    SHAKE_START = 0
    SHAKE_START_NORUMBLE = 5
    SHAKE_START_RUMBLEONLY = 4
    SHAKE_STOP = 1

class ShardSolid_t(Enum):
    SHARD_DEBRIS = 1
    SHARD_SOLID = 0

class ShatterDamageCause(Enum):
    SHATTERDAMAGE_BULLET = 0
    SHATTERDAMAGE_EXPLOSIVE = 4
    SHATTERDAMAGE_MELEE = 1
    SHATTERDAMAGE_SCRIPT = 3
    SHATTERDAMAGE_THROWN = 2

class ShatterGlassStressType(Enum):
    SHATTERGLASS_BALLISTIC = 1
    SHATTERGLASS_BLUNT = 0
    SHATTERGLASS_EXPLOSIVE = 3
    SHATTERGLASS_PULSE = 2

class SimpleConstraintSoundProfile__SimpleConstraintsSoundProfileKeypoints_t(Enum):
    kHIGHWATER = 2
    kMIN_FULL = 1
    kMIN_THRESHOLD = 0

class SolidType_t(Enum):
    SOLID_BBOX = 2
    SOLID_BSP = 1
    SOLID_CAPSULE = 7
    SOLID_LAST = 8
    SOLID_NONE = 0
    SOLID_OBB = 3
    SOLID_POINT = 5
    SOLID_SPHERE = 4
    SOLID_VPHYSICS = 6

class SoundEventStartType_t(Enum):
    SOUNDEVENT_START_ENTITY = 2
    SOUNDEVENT_START_PLAYER = 0
    SOUNDEVENT_START_WORLD = 1

class StanceType_t(Enum):
    NUM_STANCES = 3
    STANCE_CROUCHING = 1
    STANCE_CURRENT = -1
    STANCE_DEFAULT = 0
    STANCE_PRONE = 2

class SubclassVDataChangeType_t(Enum):
    SUBCLASS_VDATA_CREATED = 0
    SUBCLASS_VDATA_RELOADED = 2
    SUBCLASS_VDATA_SUBCLASS_CHANGED = 1

class SurroundingBoundsType_t(Enum):
    SURROUNDING_TYPE_BIT_COUNT = 3
    USE_BEST_COLLISION_BOUNDS = 1
    USE_COLLISION_BOUNDS_NEVER_VPHYSICS = 7
    USE_GAME_CODE = 4
    USE_HITBOXES = 2
    USE_OBB_COLLISION_BOUNDS = 0
    USE_ROTATION_EXPANDED_BOUNDS = 5
    USE_ROTATION_EXPANDED_ORIENTED_BOUNDS = 6
    USE_ROTATION_EXPANDED_SEQUENCE_BOUNDS = 8
    USE_SPECIFIED_BOUNDS = 3

class TOGGLE_STATE(Enum):
    DOOR_CLOSED = 1
    DOOR_CLOSING = 3
    DOOR_OPEN = 0
    DOOR_OPENING = 2
    TS_AT_BOTTOM = 1
    TS_AT_TOP = 0
    TS_GOING_DOWN = 3
    TS_GOING_UP = 2

class TRAIN_CODE(Enum):
    TRAIN_BLOCKING = 1
    TRAIN_FOLLOWING = 2
    TRAIN_SAFE = 0

class TakeDamageFlags_t(Enum):
    DFLAG_ALWAYS_FIRE_DAMAGE_EVENTS = 512
    DFLAG_ALWAYS_GIB = 32
    DFLAG_FORCEREDUCEARMOR_DMG = 2048
    DFLAG_FORCE_DEATH = 16
    DFLAG_IGNORE_ARMOR = 32768
    DFLAG_IGNORE_DESTRUCTIBLE_PARTS = 8192
    DFLAG_NEVER_GIB = 64
    DFLAG_NONE = 0
    DFLAG_PREVENT_DEATH = 8
    DFLAG_RADIUS_DMG = 1024
    DFLAG_REMOVE_NO_RAGDOLL = 128
    DFLAG_SUPPRESS_BREAKABLES = 16384
    DFLAG_SUPPRESS_DAMAGE_MODIFICATION = 256
    DFLAG_SUPPRESS_EFFECTS = 4
    DFLAG_SUPPRESS_HEALTH_CHANGES = 1
    DFLAG_SUPPRESS_INTERRUPT_FLINCH = 4096
    DFLAG_SUPPRESS_PHYSICS_FORCE = 2
    DFLAG_SUPPRESS_UTILREMOVE = 65536
    DMG_LASTDFLAG = 16384

class TestInputOutputCombinationsEnum_t(Enum):
    ONE = 1
    TWO = 2
    ZERO = 0

class TimelineCompression_t(Enum):
    TIMELINE_COMPRESSION_AVERAGE = 2
    TIMELINE_COMPRESSION_AVERAGE_BLEND = 3
    TIMELINE_COMPRESSION_COUNT_PER_INTERVAL = 1
    TIMELINE_COMPRESSION_SUM = 0
    TIMELINE_COMPRESSION_TOTAL = 4

class Touch_t(Enum):
    touch_none = 0
    touch_npc_only = 2
    touch_player_only = 1
    touch_player_or_npc = 3
    touch_player_or_npc_or_physicsprop = 4

class TrackOrientationType_t(Enum):
    TrackOrientation_FacePath = 1
    TrackOrientation_FacePathAngles = 2
    TrackOrientation_Fixed = 0

class TrainOrientationType_t(Enum):
    TrainOrientation_AtPathTracks = 1
    TrainOrientation_EaseInEaseOut = 3
    TrainOrientation_Fixed = 0
    TrainOrientation_LinearBlend = 2

class TrainVelocityType_t(Enum):
    TrainVelocity_EaseInEaseOut = 2
    TrainVelocity_Instantaneous = 0
    TrainVelocity_LinearBlend = 1

class ValueRemapperHapticsType_t(Enum):
    HaticsType_Default = 0
    HaticsType_None = 1

class ValueRemapperInputType_t(Enum):
    InputType_PlayerShootPosition = 0
    InputType_PlayerShootPositionAroundAxis = 1

class ValueRemapperMomentumType_t(Enum):
    MomentumType_Friction = 1
    MomentumType_None = 0
    MomentumType_SpringAwayFromSnapValue = 3
    MomentumType_SpringTowardSnapValue = 2

class ValueRemapperOutputType_t(Enum):
    OutputType_AnimationCycle = 0
    OutputType_RotationX = 1
    OutputType_RotationY = 2
    OutputType_RotationZ = 3

class ValueRemapperRatchetType_t(Enum):
    RatchetType_Absolute = 0
    RatchetType_EachEngage = 1

class WaterLevel_t(Enum):
    WL_Chest = 4
    WL_Count = 6
    WL_Feet = 1
    WL_FullyUnderwater = 5
    WL_Knees = 2
    WL_NotInWater = 0
    WL_Waist = 3

class WeaponAttackType_t(Enum):
    eCount = 2
    eInvalid = -1
    ePrimary = 0
    eSecondary = 1

class WeaponGameplayAnimState(Enum):
    WEAPON_LEGACY_STATE_CLEAR_FIRING = 1101
    WPN_ANIMSTATE_C4_PLANT = 300
    WPN_ANIMSTATE_CHARGE = 103
    WPN_ANIMSTATE_DEPLOY = 11
    WPN_ANIMSTATE_DROPPED = 1
    WPN_ANIMSTATE_END_VALID = 1100
    WPN_ANIMSTATE_GRENADE_PULL_PIN = 200
    WPN_ANIMSTATE_GRENADE_READY = 201
    WPN_ANIMSTATE_GRENADE_THROW = 202
    WPN_ANIMSTATE_HEALTHSHOT_INJECT = 400
    WPN_ANIMSTATE_HOLSTERED = 10
    WPN_ANIMSTATE_IDLE = 50
    WPN_ANIMSTATE_INSPECT = 1000
    WPN_ANIMSTATE_INSPECT_OUTRO = 1001
    WPN_ANIMSTATE_KNIFE_PRIMARY_HIT = 500
    WPN_ANIMSTATE_KNIFE_PRIMARY_MISS = 501
    WPN_ANIMSTATE_KNIFE_PRIMARY_STAB = 504
    WPN_ANIMSTATE_KNIFE_SECONDARY_HIT = 502
    WPN_ANIMSTATE_KNIFE_SECONDARY_MISS = 503
    WPN_ANIMSTATE_KNIFE_SECONDARY_STAB = 505
    WPN_ANIMSTATE_RELOAD = 800
    WPN_ANIMSTATE_RELOAD_OUTRO = 801
    WPN_ANIMSTATE_SHOOT_DRYFIRE = 102
    WPN_ANIMSTATE_SHOOT_PRIMARY = 100
    WPN_ANIMSTATE_SHOOT_SECONDARY = 101
    WPN_ANIMSTATE_SILENCER_APPLY = 600
    WPN_ANIMSTATE_SILENCER_REMOVE = 601
    WPN_ANIMSTATE_UNINITIALIZED = 0

class WeaponSound_t(Enum):
    WEAPON_SOUND_DROP = 22
    WEAPON_SOUND_EMPTY = 0
    WEAPON_SOUND_IMPACT = 13
    WEAPON_SOUND_MELEE_HIT = 5
    WEAPON_SOUND_MELEE_HIT_NPC = 8
    WEAPON_SOUND_MELEE_HIT_PLAYER = 7
    WEAPON_SOUND_MELEE_HIT_WORLD = 6
    WEAPON_SOUND_MELEE_MISS = 4
    WEAPON_SOUND_MOUSE_PRESSED = 21
    WEAPON_SOUND_NEARLYEMPTY = 12
    WEAPON_SOUND_NUM_TYPES = 24
    WEAPON_SOUND_RADIO_USE = 23
    WEAPON_SOUND_REFLECT = 14
    WEAPON_SOUND_RELOAD = 17
    WEAPON_SOUND_SECONDARY_ATTACK = 3
    WEAPON_SOUND_SECONDARY_EMPTY = 1
    WEAPON_SOUND_SECONDARY_IMPACT = 15
    WEAPON_SOUND_SECONDARY_REFLECT = 16
    WEAPON_SOUND_SINGLE = 2
    WEAPON_SOUND_SINGLE_ACCURATE = 18
    WEAPON_SOUND_SPECIAL1 = 9
    WEAPON_SOUND_SPECIAL2 = 10
    WEAPON_SOUND_SPECIAL3 = 11
    WEAPON_SOUND_ZOOM_IN = 19
    WEAPON_SOUND_ZOOM_OUT = 20

class WeaponSwitchReason_t(Enum):
    eDrawn = 0
    eEquipped = 1
    eUserInitiatedSwitchHands = 4
    eUserInitiatedSwitchToLast = 2
    eUserInitiatedUIKeyPress = 3

class WorldTextPanelHorizontalAlign_t(Enum):
    WORLDTEXT_HORIZONTAL_ALIGN_CENTER = 1
    WORLDTEXT_HORIZONTAL_ALIGN_LEFT = 0
    WORLDTEXT_HORIZONTAL_ALIGN_RIGHT = 2

class WorldTextPanelOrientation_t(Enum):
    WORLDTEXT_ORIENTATION_DEFAULT = 0
    WORLDTEXT_ORIENTATION_FACEUSER = 1
    WORLDTEXT_ORIENTATION_FACEUSER_UPRIGHT = 2

class WorldTextPanelVerticalAlign_t(Enum):
    WORLDTEXT_VERTICAL_ALIGN_BOTTOM = 2
    WORLDTEXT_VERTICAL_ALIGN_CENTER = 1
    WORLDTEXT_VERTICAL_ALIGN_TOP = 0

class attributeprovidertypes_t(Enum):
    PROVIDER_GENERIC = 0
    PROVIDER_WEAPON = 1

class doorCheck_e(Enum):
    DOOR_CHECK_BACKWARD = 1
    DOOR_CHECK_FORWARD = 0
    DOOR_CHECK_FULL = 2

class eSplinePushType(Enum):
    k_eSplinePushAlong = 0
    k_eSplinePushAway = 1
    k_eSplinePushTowards = 2

class filter_t(Enum):
    FILTER_AND = 0
    FILTER_OR = 1

class gear_slot_t(Enum):
    GEAR_SLOT_BOOSTS = 11
    GEAR_SLOT_C4 = 4
    GEAR_SLOT_COUNT = 13
    GEAR_SLOT_FIRST = 0
    GEAR_SLOT_GRENADES = 3
    GEAR_SLOT_INVALID = -1
    GEAR_SLOT_KNIFE = 2
    GEAR_SLOT_LAST = 12
    GEAR_SLOT_PISTOL = 1
    GEAR_SLOT_RESERVED_SLOT10 = 9
    GEAR_SLOT_RESERVED_SLOT11 = 10
    GEAR_SLOT_RESERVED_SLOT6 = 5
    GEAR_SLOT_RESERVED_SLOT7 = 6
    GEAR_SLOT_RESERVED_SLOT8 = 7
    GEAR_SLOT_RESERVED_SLOT9 = 8
    GEAR_SLOT_RIFLE = 0
    GEAR_SLOT_UTILITY = 12

class loadout_slot_t(Enum):
    LOADOUT_SLOT_C4 = 1
    LOADOUT_SLOT_CLOTHING_APPEARANCE = 46
    LOADOUT_SLOT_CLOTHING_CUSTOMHEAD = 39
    LOADOUT_SLOT_CLOTHING_CUSTOMPLAYER = 38
    LOADOUT_SLOT_CLOTHING_EYEWEAR = 42
    LOADOUT_SLOT_CLOTHING_FACEMASK = 40
    LOADOUT_SLOT_CLOTHING_HANDS = 41
    LOADOUT_SLOT_CLOTHING_HAT = 43
    LOADOUT_SLOT_CLOTHING_LOWERBODY = 44
    LOADOUT_SLOT_CLOTHING_TORSO = 45
    LOADOUT_SLOT_COUNT = 57
    LOADOUT_SLOT_EQUIPMENT0 = 32
    LOADOUT_SLOT_EQUIPMENT1 = 33
    LOADOUT_SLOT_EQUIPMENT2 = 34
    LOADOUT_SLOT_EQUIPMENT3 = 35
    LOADOUT_SLOT_EQUIPMENT4 = 36
    LOADOUT_SLOT_EQUIPMENT5 = 37
    LOADOUT_SLOT_FIRST_ALL_CHARACTER = 54
    LOADOUT_SLOT_FIRST_AUTO_BUY_WEAPON = 0
    LOADOUT_SLOT_FIRST_COSMETIC = 41
    LOADOUT_SLOT_FIRST_PRIMARY_WEAPON = 8
    LOADOUT_SLOT_FIRST_WHEEL_EQUIPMENT = 32
    LOADOUT_SLOT_FIRST_WHEEL_GRENADE = 26
    LOADOUT_SLOT_FIRST_WHEEL_WEAPON = 2
    LOADOUT_SLOT_FLAIR0 = 55
    LOADOUT_SLOT_GRENADE0 = 26
    LOADOUT_SLOT_GRENADE1 = 27
    LOADOUT_SLOT_GRENADE2 = 28
    LOADOUT_SLOT_GRENADE3 = 29
    LOADOUT_SLOT_GRENADE4 = 30
    LOADOUT_SLOT_GRENADE5 = 31
    LOADOUT_SLOT_HEAVY0 = 20
    LOADOUT_SLOT_HEAVY1 = 21
    LOADOUT_SLOT_HEAVY2 = 22
    LOADOUT_SLOT_HEAVY3 = 23
    LOADOUT_SLOT_HEAVY4 = 24
    LOADOUT_SLOT_HEAVY5 = 25
    LOADOUT_SLOT_INVALID = -1
    LOADOUT_SLOT_LAST_ALL_CHARACTER = 56
    LOADOUT_SLOT_LAST_AUTO_BUY_WEAPON = 1
    LOADOUT_SLOT_LAST_COSMETIC = 41
    LOADOUT_SLOT_LAST_PRIMARY_WEAPON = 25
    LOADOUT_SLOT_LAST_WHEEL_EQUIPMENT = 37
    LOADOUT_SLOT_LAST_WHEEL_GRENADE = 31
    LOADOUT_SLOT_LAST_WHEEL_WEAPON = 25
    LOADOUT_SLOT_MELEE = 0
    LOADOUT_SLOT_MISC0 = 47
    LOADOUT_SLOT_MISC1 = 48
    LOADOUT_SLOT_MISC2 = 49
    LOADOUT_SLOT_MISC3 = 50
    LOADOUT_SLOT_MISC4 = 51
    LOADOUT_SLOT_MISC5 = 52
    LOADOUT_SLOT_MISC6 = 53
    LOADOUT_SLOT_MUSICKIT = 54
    LOADOUT_SLOT_PROMOTED = -2
    LOADOUT_SLOT_RIFLE0 = 14
    LOADOUT_SLOT_RIFLE1 = 15
    LOADOUT_SLOT_RIFLE2 = 16
    LOADOUT_SLOT_RIFLE3 = 17
    LOADOUT_SLOT_RIFLE4 = 18
    LOADOUT_SLOT_RIFLE5 = 19
    LOADOUT_SLOT_SECONDARY0 = 2
    LOADOUT_SLOT_SECONDARY1 = 3
    LOADOUT_SLOT_SECONDARY2 = 4
    LOADOUT_SLOT_SECONDARY3 = 5
    LOADOUT_SLOT_SECONDARY4 = 6
    LOADOUT_SLOT_SECONDARY5 = 7
    LOADOUT_SLOT_SMG0 = 8
    LOADOUT_SLOT_SMG1 = 9
    LOADOUT_SLOT_SMG2 = 10
    LOADOUT_SLOT_SMG3 = 11
    LOADOUT_SLOT_SMG4 = 12
    LOADOUT_SLOT_SMG5 = 13
    LOADOUT_SLOT_SPRAY0 = 56

class navproperties_t(Enum):
    NAV_IGNORE = 1

class vote_create_failed_t(Enum):
    VOTE_FAILED_CANNOT_KICK_ADMIN = 12
    VOTE_FAILED_CANT_ROUND_END = 31
    VOTE_FAILED_CONTINUE = 33
    VOTE_FAILED_DISABLED = 21
    VOTE_FAILED_FAILED_RECENTLY = 8
    VOTE_FAILED_FAILED_RECENT_CHANGEMAP = 16
    VOTE_FAILED_FAILED_RECENT_KICK = 15
    VOTE_FAILED_FAILED_RECENT_RESTART = 19
    VOTE_FAILED_FAILED_RECENT_SCRAMBLETEAMS = 18
    VOTE_FAILED_FAILED_RECENT_SWAPTEAMS = 17
    VOTE_FAILED_GENERIC = 0
    VOTE_FAILED_ISSUE_DISABLED = 5
    VOTE_FAILED_MAP_NAME_REQUIRED = 7
    VOTE_FAILED_MAP_NOT_FOUND = 6
    VOTE_FAILED_MATCH_NOT_PAUSED = 25
    VOTE_FAILED_MATCH_PAUSED = 24
    VOTE_FAILED_MAX = 34
    VOTE_FAILED_NEXTLEVEL_SET = 22
    VOTE_FAILED_NOT_10_PLAYERS = 27
    VOTE_FAILED_NOT_IN_WARMUP = 26
    VOTE_FAILED_PLAYERNOTFOUND = 11
    VOTE_FAILED_QUORUM_FAILURE = 4
    VOTE_FAILED_RATE_EXCEEDED = 2
    VOTE_FAILED_REMATCH = 32
    VOTE_FAILED_SCRAMBLE_IN_PROGRESS = 13
    VOTE_FAILED_SPECTATOR = 14
    VOTE_FAILED_SWAP_IN_PROGRESS = 20
    VOTE_FAILED_TEAM_CANT_CALL = 9
    VOTE_FAILED_TIMEOUT_ACTIVE = 28
    VOTE_FAILED_TIMEOUT_EXHAUSTED = 30
    VOTE_FAILED_TIMEOUT_INACTIVE = 29
    VOTE_FAILED_TOO_EARLY_SURRENDER = 23
    VOTE_FAILED_TRANSITIONING_PLAYERS = 1
    VOTE_FAILED_WAITINGFORPLAYERS = 10
    VOTE_FAILED_YES_MUST_EXCEED_NO = 3

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
            "type_name": "CHandle<CBaseModelEntity>"
        },
        {
            "name": "m_AssociatedEntityNames",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class CAI_ChangeHintGroup(CBaseEntity):
    m_flRadius = 1288  # offset
    m_iSearchType = 1264  # offset
    m_strNewHintGroup = 1280  # offset
    m_strSearchName = 1272  # offset

class CAK47(CCSWeaponBaseGun):
    pass

class CAmbientGeneric(CPointEntity):
    m_dpv = 1276  # offset
    m_fActive = 1376  # offset
    m_fLooping = 1377  # offset
    m_flMaxRadius = 1268  # offset
    m_hSoundSource = 1400  # offset
    m_iSoundLevel = 1272  # offset
    m_iszSound = 1384  # offset
    m_nSoundSourceEntIndex = 1404  # offset
    m_radius = 1264  # offset
    m_sSourceEntName = 1392  # offset

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

class CAttributeContainer(CAttributeManager):
    m_Item = 80  # offset

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

class CBarnLight(CBaseModelEntity):
    m_Color = 2040  # offset
    m_LightStyleEvents = 2128  # offset
    m_LightStyleString = 2088  # offset
    m_LightStyleTargets = 2152  # offset
    m_QueuedLightStyleStrings = 2104  # offset
    m_StyleEvent = 2176  # offset
    m_VisClusters = 2808  # offset
    m_bContactShadow = 2452  # offset
    m_bEnabled = 2032  # offset
    m_bFogMixedShadows = 2500  # offset
    m_bForceShadowsEnabled = 2453  # offset
    m_bPrecomputedFieldsValid = 2520  # offset
    m_bPvsModifyEntity = 2804  # offset
    m_fAlternateColorBrightness = 2480  # offset
    m_flBounceScale = 2460  # offset
    m_flBrightness = 2048  # offset
    m_flBrightnessScale = 2052  # offset
    m_flColorTemperature = 2044  # offset
    m_flFadeSizeEnd = 2508  # offset
    m_flFadeSizeStart = 2504  # offset
    m_flFogScale = 2496  # offset
    m_flFogStrength = 2488  # offset
    m_flLightStyleStartTime = 2096  # offset
    m_flLuminaireAnisotropy = 2080  # offset
    m_flLuminaireSize = 2076  # offset
    m_flMinRoughness = 2464  # offset
    m_flRange = 2408  # offset
    m_flShadowFadeSizeEnd = 2516  # offset
    m_flShadowFadeSizeStart = 2512  # offset
    m_flShape = 2376  # offset
    m_flSkirt = 2388  # offset
    m_flSkirtNear = 2392  # offset
    m_flSoftX = 2380  # offset
    m_flSoftY = 2384  # offset
    m_hLightCookie = 2368  # offset
    m_nBakeSpecularToCubemaps = 2424  # offset
    m_nBakedShadowIndex = 2060  # offset
    m_nBounceLight = 2456  # offset
    m_nCastShadows = 2440  # offset
    m_nColorMode = 2036  # offset
    m_nDirectLight = 2056  # offset
    m_nFog = 2484  # offset
    m_nFogShadows = 2492  # offset
    m_nLightMapUniqueId = 2068  # offset
    m_nLightPathUniqueId = 2064  # offset
    m_nLuminaireShape = 2072  # offset
    m_nPrecomputedSubFrusta = 2584  # offset
    m_nShadowMapSize = 2444  # offset
    m_nShadowPriority = 2448  # offset
    m_vAlternateColor = 2468  # offset
    m_vBakeSpecularToCubemapsSize = 2428  # offset
    m_vPrecomputedBoundsMaxs = 2536  # offset
    m_vPrecomputedBoundsMins = 2524  # offset
    m_vPrecomputedOBBAngles = 2560  # offset
    m_vPrecomputedOBBAngles0 = 2600  # offset
    m_vPrecomputedOBBAngles1 = 2636  # offset
    m_vPrecomputedOBBAngles2 = 2672  # offset
    m_vPrecomputedOBBAngles3 = 2708  # offset
    m_vPrecomputedOBBAngles4 = 2744  # offset
    m_vPrecomputedOBBAngles5 = 2780  # offset
    m_vPrecomputedOBBExtent = 2572  # offset
    m_vPrecomputedOBBExtent0 = 2612  # offset
    m_vPrecomputedOBBExtent1 = 2648  # offset
    m_vPrecomputedOBBExtent2 = 2684  # offset
    m_vPrecomputedOBBExtent3 = 2720  # offset
    m_vPrecomputedOBBExtent4 = 2756  # offset
    m_vPrecomputedOBBExtent5 = 2792  # offset
    m_vPrecomputedOBBOrigin = 2548  # offset
    m_vPrecomputedOBBOrigin0 = 2588  # offset
    m_vPrecomputedOBBOrigin1 = 2624  # offset
    m_vPrecomputedOBBOrigin2 = 2660  # offset
    m_vPrecomputedOBBOrigin3 = 2696  # offset
    m_vPrecomputedOBBOrigin4 = 2732  # offset
    m_vPrecomputedOBBOrigin5 = 2768  # offset
    m_vShear = 2412  # offset
    m_vSizeParams = 2396  # offset

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
            "type_name": "CHandle<CBaseModelEntity>"
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

class CBaseAnimGraph(CBaseModelEntity):
    m_RagdollPose = 2232  # offset
    m_bAnimGraphUpdateEnabled = 2176  # offset
    m_bAnimationUpdateScheduled = 2196  # offset
    m_bInitiallyPopulateInterpHistory = 2160  # offset
    m_bRagdollClientSide = 2273  # offset
    m_bRagdollEnabled = 2272  # offset
    m_flMaxSlopeDistance = 2180  # offset
    m_nForceBone = 2212  # offset
    m_pChoreoServices = 2168  # offset
    m_vLastSlopeCheckPos = 2184  # offset
    m_vecForce = 2200  # offset

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
    m_bIsUsingAG2 = 1424  # offset
    m_bLastUpdateSkipped = 588  # offset
    m_bNetworkedAnimationInputsChanged = 586  # offset
    m_bNetworkedSequenceChanged = 587  # offset
    m_bSequenceFinished = 544  # offset
    m_flPlaybackRate = 572  # offset
    m_flPrevAnimUpdateTime = 592  # offset
    m_flSeqFixedCycle = 564  # offset
    m_flSeqStartTime = 560  # offset
    m_flSoundSyncTime = 548  # offset
    m_hGraphDefinitionAG2 = 1416  # offset
    m_hSequence = 556  # offset
    m_nActiveIKChainMask = 552  # offset
    m_nAnimLoopMode = 568  # offset
    m_nGraphCreationFlagsAG2 = 1464  # offset
    m_nNotifyState = 584  # offset
    m_nSerializePoseRecipeSizeAG2 = 1456  # offset
    m_nSerializePoseRecipeVersionAG2 = 1460  # offset
    m_nServerGraphDefReloadCountAG2 = 1528  # offset
    m_serializedPoseRecipeAG2 = 1432  # offset

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

class CBaseButton(CBaseToggle):
    m_OnDamaged = 2256  # offset
    m_OnIn = 2376  # offset
    m_OnOut = 2416  # offset
    m_OnPressed = 2296  # offset
    m_OnUseLocked = 2336  # offset
    m_angMoveEntitySpace = 2160  # offset
    m_bDisabled = 2241  # offset
    m_bForceNpcExclude = 2468  # offset
    m_bLocked = 2240  # offset
    m_bSolidBsp = 2248  # offset
    m_fRotating = 2173  # offset
    m_fStayPushed = 2172  # offset
    m_flUseLockedTime = 2244  # offset
    m_glowEntity = 2480  # offset
    m_hConstraint = 2460  # offset
    m_hConstraintParent = 2464  # offset
    m_ls = 2176  # offset
    m_nState = 2456  # offset
    m_sGlowEntity = 2472  # offset
    m_sLockedSound = 2216  # offset
    m_sOverrideAnticipationName = 2232  # offset
    m_sUnlockedSound = 2224  # offset
    m_sUseSound = 2208  # offset
    m_szDisplayText = 2488  # offset
    m_usable = 2484  # offset

    __metadata__ =     [
        {
            "name": "m_glowEntity",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseModelEntity>"
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

class CBaseCSGrenade(CCSWeaponBase):
    m_bIsHeldByPlayer = 4521  # offset
    m_bJumpThrow = 4523  # offset
    m_bJustPulledPin = 4544  # offset
    m_bPinPulled = 4522  # offset
    m_bRedraw = 4520  # offset
    m_bThrowAnimating = 4524  # offset
    m_fDropTime = 4536  # offset
    m_fPinPullTime = 4540  # offset
    m_fThrowTime = 4528  # offset
    m_flNextHoldFrac = 4552  # offset
    m_flThrowStrength = 4532  # offset
    m_hSwitchToWeaponAfterThrow = 4556  # offset
    m_nNextHoldTick = 4548  # offset

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
            "name": "m_flThrowStrength",
            "type": "NetworkVarNames",
            "type_name": "float"
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

class CBaseCSGrenadeProjectile(CBaseGrenade):
    m_bDetonationRecorded = 3061  # offset
    m_bHasEverHitEnemy = 3108  # offset
    m_flLastBounceSoundTime = 3076  # offset
    m_flSpawnTime = 3056  # offset
    m_nBounces = 3024  # offset
    m_nExplodeEffectIndex = 3032  # offset
    m_nExplodeEffectTickBegin = 3040  # offset
    m_nItemIndex = 3062  # offset
    m_nTicksAtZeroVelocity = 3104  # offset
    m_unOGSExtraFlags = 3060  # offset
    m_vInitialPosition = 3000  # offset
    m_vInitialVelocity = 3012  # offset
    m_vecExplodeEffectOrigin = 3044  # offset
    m_vecGrenadeSpin = 3080  # offset
    m_vecLastHitSurfaceNormal = 3092  # offset
    m_vecOriginalSpawnLocation = 3064  # offset

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

class CBaseClientUIEntity(CBaseModelEntity):
    m_CustomOutput0 = 2064  # offset
    m_CustomOutput1 = 2104  # offset
    m_CustomOutput2 = 2144  # offset
    m_CustomOutput3 = 2184  # offset
    m_CustomOutput4 = 2224  # offset
    m_CustomOutput5 = 2264  # offset
    m_CustomOutput6 = 2304  # offset
    m_CustomOutput7 = 2344  # offset
    m_CustomOutput8 = 2384  # offset
    m_CustomOutput9 = 2424  # offset
    m_DialogXMLName = 2040  # offset
    m_PanelClassName = 2048  # offset
    m_PanelID = 2056  # offset
    m_bEnabled = 2032  # offset

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

class CBaseCombatCharacter(CBaseFlex):
    m_bApplyStressDamage = 2872  # offset
    m_bDeathEventsDispatched = 2873  # offset
    m_bForceServerRagdoll = 2832  # offset
    m_eHull = 2960  # offset
    m_hMyWearables = 2840  # offset
    m_impactEnergyScale = 2864  # offset
    m_movementStats = 2968  # offset
    m_nMinVehicleDamageToTempRagdoll = 2868  # offset
    m_nNavHullIdx = 2964  # offset
    m_pVecRelationships = 2944  # offset
    m_strRelationships = 2952  # offset

    __metadata__ =     [
        {
            "name": "MNetworkExcludeByUserGroup",
            "type": "Unknown"
        },
        {
            "name": "m_hMyWearables",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CEconWearable>"
        }
    ]

class CBaseDMStart(CPointEntity):
    m_Master = 1264  # offset

class CBaseDoor(CBaseToggle):
    m_ChainTarget = 2280  # offset
    m_NoiseArrived = 2256  # offset
    m_NoiseArrivedClosed = 2272  # offset
    m_NoiseMoving = 2248  # offset
    m_NoiseMovingClosed = 2264  # offset
    m_OnBlockedClosing = 2288  # offset
    m_OnBlockedOpening = 2328  # offset
    m_OnClose = 2528  # offset
    m_OnFullyClosed = 2448  # offset
    m_OnFullyOpen = 2488  # offset
    m_OnLockedUse = 2608  # offset
    m_OnOpen = 2568  # offset
    m_OnUnblockedClosing = 2368  # offset
    m_OnUnblockedOpening = 2408  # offset
    m_angMoveEntitySpace = 2176  # offset
    m_bCreateNavObstacle = 2680  # offset
    m_bDoorGroup = 2233  # offset
    m_bForceClosed = 2232  # offset
    m_bIgnoreDebris = 2235  # offset
    m_bIsUsable = 2682  # offset
    m_bLocked = 2234  # offset
    m_bLoopMoveSound = 2648  # offset
    m_bNoNPCs = 2236  # offset
    m_eSpawnPosition = 2240  # offset
    m_flBlockDamage = 2244  # offset
    m_isChaining = 2681  # offset
    m_ls = 2200  # offset
    m_vecMoveDirParentSpace = 2188  # offset

    __metadata__ =     [
        {
            "name": "m_bIsUsable",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CBaseEntity:
    m_CBodyComponent = 56  # offset
    m_MoveCollide = 754  # offset
    m_MoveType = 755  # offset
    m_NetworkTransmitComponent = 64  # offset
    m_OnKilled = 872  # offset
    m_OnUser1 = 1056  # offset
    m_OnUser2 = 1096  # offset
    m_OnUser3 = 1136  # offset
    m_OnUser4 = 1176  # offset
    m_ResponseContexts = 656  # offset
    m_aThinkFunctions = 584  # offset
    m_bAnimatedEveryTick = 1041  # offset
    m_bClientSideRagdoll = 812  # offset
    m_bDisableLowViolence = 1049  # offset
    m_bDisabledContextThinks = 616  # offset
    m_bGravityActuallyDisabled = 1048  # offset
    m_bGravityDisabled = 1040  # offset
    m_bLagCompensate = 1237  # offset
    m_bNetworkQuantizeOriginAndAngles = 1236  # offset
    m_bRestoreInHierarchy = 759  # offset
    m_bTakesDamage = 736  # offset
    m_fEffects = 1008  # offset
    m_fFlags = 912  # offset
    m_flActualGravityScale = 1044  # offset
    m_flAnimTime = 800  # offset
    m_flCreateTime = 808  # offset
    m_flDamageAccumulator = 732  # offset
    m_flElasticity = 1024  # offset
    m_flFriction = 1020  # offset
    m_flGravityScale = 1028  # offset
    m_flLocalTime = 1244  # offset
    m_flMoveDoneTime = 784  # offset
    m_flNavIgnoreUntilTime = 1220  # offset
    m_flSimulationTime = 804  # offset
    m_flSpeed = 844  # offset
    m_flTimeScale = 1032  # offset
    m_flVPhysicsUpdateLocalTime = 1248  # offset
    m_flWaterLevel = 1036  # offset
    m_hDamageFilter = 768  # offset
    m_hEffectEntity = 1000  # offset
    m_hGroundEntity = 1012  # offset
    m_hOwnerEntity = 1004  # offset
    m_iCurrentThinkContext = 608  # offset
    m_iEFlags = 1052  # offset
    m_iGlobalname = 832  # offset
    m_iHealth = 720  # offset
    m_iInitialTeamNum = 1216  # offset
    m_iMaxHealth = 724  # offset
    m_iSentToClients = 840  # offset
    m_iTeamNum = 828  # offset
    m_isSteadyState = 632  # offset
    m_iszDamageFilterName = 776  # offset
    m_iszResponseContext = 680  # offset
    m_lastNetworkChange = 640  # offset
    m_lifeState = 728  # offset
    m_nActualMoveType = 756  # offset
    m_nBloodType = 1252  # offset
    m_nGroundBodyIndex = 1016  # offset
    m_nLastThinkTick = 612  # offset
    m_nNextThinkTick = 860  # offset
    m_nPlatformType = 752  # offset
    m_nPushEnumCount = 988  # offset
    m_nSimulationTick = 864  # offset
    m_nSlimeTouch = 758  # offset
    m_nSubclassID = 788  # offset
    m_nTakeDamageFlags = 744  # offset
    m_nWaterTouch = 757  # offset
    m_nWaterType = 1050  # offset
    m_pBlocker = 1240  # offset
    m_pCollision = 992  # offset
    m_pPulseGraphInstance = 1256  # offset
    m_sUniqueHammerID = 848  # offset
    m_spawnflags = 856  # offset
    m_target = 760  # offset
    m_ubInterpolationFrame = 813  # offset
    m_vPrevVPhysicsUpdatePos = 816  # offset
    m_vecAbsVelocity = 916  # offset
    m_vecAngVelocity = 1224  # offset
    m_vecBaseVelocity = 976  # offset
    m_vecVelocity = 928  # offset

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
            "name": "m_CBodyComponent",
            "type": "NetworkVarNames",
            "type_name": "CBodyComponent::Storage_t"
        },
        {
            "name": "m_iHealth",
            "type": "NetworkVarNames",
            "type_name": "int32"
        },
        {
            "name": "m_iMaxHealth",
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
            "name": "m_nSubclassID",
            "type": "NetworkVarNames",
            "type_name": "EntitySubclassID_t"
        },
        {
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
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
            "name": "m_bClientSideRagdoll",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_ubInterpolationFrame",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_iTeamNum",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_flSpeed",
            "type": "NetworkVarNames",
            "type_name": "float"
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
            "name": "m_vecVelocity",
            "type": "NetworkVarNames",
            "type_name": "CNetworkVelocityVector"
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
            "name": "m_flWaterLevel",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_bGravityDisabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bAnimatedEveryTick",
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

class CBaseEntityAPI:
    pass

class CBaseFilter(CLogicalEntity):
    m_OnFail = 1312  # offset
    m_OnPass = 1272  # offset
    m_bNegated = 1264  # offset

class CBaseFlex(CBaseAnimGraph):
    m_bUpdateLayerPriorities = 2820  # offset
    m_blinktoggle = 2724  # offset
    m_flAllowResponsesEndTime = 2808  # offset
    m_flLastFlexAnimationTime = 2812  # offset
    m_flexWeight = 2688  # offset
    m_nNextSceneEventId = 2816  # offset
    m_vLookTargetPosition = 2712  # offset

    __metadata__ =     [
        {
            "name": "m_flexWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_vLookTargetPosition",
            "type": "NetworkVarNames",
            "type_name": "Vector"
        },
        {
            "name": "m_blinktoggle",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CBaseFlexAlias_funCBaseFlex(CBaseFlex):
    pass

class CBaseGrenade(CBaseFlex):
    m_DmgRadius = 2924  # offset
    m_ExplosionSound = 2952  # offset
    m_OnExplode = 2880  # offset
    m_OnPlayerPickup = 2840  # offset
    m_bHasWarnedAI = 2920  # offset
    m_bIsLive = 2922  # offset
    m_bIsSmokeGrenade = 2921  # offset
    m_flDamage = 2936  # offset
    m_flDetonateTime = 2928  # offset
    m_flNextAttack = 2988  # offset
    m_flWarnAITime = 2932  # offset
    m_hOriginalThrower = 2992  # offset
    m_hThrower = 2964  # offset
    m_iszBounceSound = 2944  # offset

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

class CBaseModelEntity(CBaseEntity):
    m_CHitboxComponent = 1272  # offset
    m_CRenderComponent = 1264  # offset
    m_Collision = 1584  # offset
    m_ConfigEntitiesToPropagateMaterialDecalsTo = 1912  # offset
    m_Glow = 1760  # offset
    m_LastHitGroup = 1360  # offset
    m_OnIgnite = 1392  # offset
    m_bAllowFadeInView = 1434  # offset
    m_bNoInterpolate = 1577  # offset
    m_bRenderToCubemaps = 1576  # offset
    m_bvDisabledHitGroups = 2024  # offset
    m_clrRender = 1464  # offset
    m_fadeMaxDist = 1856  # offset
    m_fadeMinDist = 1852  # offset
    m_flDecalHealBloodRate = 1900  # offset
    m_flDecalHealHeightRate = 1904  # offset
    m_flDissolveStartTime = 1388  # offset
    m_flFadeScale = 1860  # offset
    m_flGlowBackfaceMult = 1848  # offset
    m_flShadowStrength = 1864  # offset
    m_nAddDecal = 1872  # offset
    m_nDecalMode = 1908  # offset
    m_nDestructiblePartInitialStateDestructed0 = 1312  # offset
    m_nDestructiblePartInitialStateDestructed0_PartIndex = 1332  # offset
    m_nDestructiblePartInitialStateDestructed1 = 1316  # offset
    m_nDestructiblePartInitialStateDestructed1_PartIndex = 1336  # offset
    m_nDestructiblePartInitialStateDestructed2 = 1320  # offset
    m_nDestructiblePartInitialStateDestructed2_PartIndex = 1340  # offset
    m_nDestructiblePartInitialStateDestructed3 = 1324  # offset
    m_nDestructiblePartInitialStateDestructed3_PartIndex = 1344  # offset
    m_nDestructiblePartInitialStateDestructed4 = 1328  # offset
    m_nDestructiblePartInitialStateDestructed4_PartIndex = 1348  # offset
    m_nObjectCulling = 1868  # offset
    m_nRenderFX = 1433  # offset
    m_nRenderMode = 1432  # offset
    m_nRequiredDecalMode = 1909  # offset
    m_pDestructiblePartsSystemComponent = 1352  # offset
    m_sLastDamageSourceName = 1368  # offset
    m_vDecalForwardAxis = 1888  # offset
    m_vDecalPosition = 1876  # offset
    m_vLastDamagePosition = 1376  # offset
    m_vecRenderAttributes = 1472  # offset
    m_vecViewOffset = 1976  # offset

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
            "type_name": "CHandle<CBaseModelEntity>"
        },
        {
            "name": "m_vecViewOffset",
            "type": "NetworkVarNames",
            "type_name": "CNetworkViewOffsetVector"
        },
        {
            "name": "m_bvDisabledHitGroups",
            "type": "NetworkVarNames",
            "type_name": "uint32"
        }
    ]

class CBaseModelEntityAPI:
    pass

class CBaseMoveBehavior(CPathKeyFrame):
    m_flAnimEndTime = 1372  # offset
    m_flAnimStartTime = 1368  # offset
    m_flAverageSpeedAcrossFrame = 1376  # offset
    m_flTimeIntoFrame = 1416  # offset
    m_iDirection = 1420  # offset
    m_iPositionInterpolator = 1360  # offset
    m_iRotationInterpolator = 1364  # offset
    m_pCurrentKeyFrame = 1384  # offset
    m_pPostKeyFrame = 1408  # offset
    m_pPreKeyFrame = 1400  # offset
    m_pTargetKeyFrame = 1392  # offset

class CBasePlatTrain(CBaseToggle):
    m_NoiseArrived = 2168  # offset
    m_NoiseMoving = 2160  # offset
    m_flTLength = 2192  # offset
    m_flTWidth = 2188  # offset
    m_volume = 2184  # offset

class CBasePlayerController(CBaseEntity):
    m_bGamePaused = 1517  # offset
    m_bHasAnySteadyStateEnts = 1848  # offset
    m_bIsHLTV = 1360  # offset
    m_bIsLowViolence = 1516  # offset
    m_bKnownTeamMismatch = 1324  # offset
    m_bLagCompensation = 1508  # offset
    m_bNoClipEnabled = 1872  # offset
    m_bPredict = 1509  # offset
    m_fLerpTime = 1504  # offset
    m_flLastEntitySteadyState = 1840  # offset
    m_flLastPlayerTalkTime = 1836  # offset
    m_hPawn = 1320  # offset
    m_hSplitOwner = 1332  # offset
    m_hSplitScreenPlayers = 1336  # offset
    m_iConnected = 1364  # offset
    m_iDesiredFOV = 1876  # offset
    m_iIgnoreGlobalChat = 1832  # offset
    m_iszPlayerName = 1368  # offset
    m_nAvailableEntitySteadyState = 1844  # offset
    m_nInButtonsWhichAreToggles = 1272  # offset
    m_nSplitScreenSlot = 1328  # offset
    m_nTickBase = 1280  # offset
    m_steamID = 1864  # offset
    m_szNetworkIDString = 1496  # offset

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
        }
    ]

class CBasePlayerControllerAPI:
    pass

class CBasePlayerPawn(CBaseCombatCharacter):
    m_ServerViewAngleChanges = 3112  # offset
    m_fHltvReplayDelay = 3428  # offset
    m_fHltvReplayEnd = 3432  # offset
    m_fInitHUD = 3404  # offset
    m_fNextSuicideTime = 3400  # offset
    m_fTimeLastHurt = 3392  # offset
    m_flDeathTime = 3396  # offset
    m_hController = 3416  # offset
    m_hDefaultController = 3420  # offset
    m_iHideHUD = 3240  # offset
    m_iHltvReplayEntity = 3436  # offset
    m_pAutoaimServices = 3048  # offset
    m_pCameraServices = 3088  # offset
    m_pExpresser = 3408  # offset
    m_pFlashlightServices = 3080  # offset
    m_pItemServices = 3040  # offset
    m_pMovementServices = 3096  # offset
    m_pObserverServices = 3056  # offset
    m_pUseServices = 3072  # offset
    m_pWaterServices = 3064  # offset
    m_pWeaponServices = 3032  # offset
    m_skybox3d = 3248  # offset
    m_sndOpvarLatchData = 3440  # offset
    v_angle = 3216  # offset
    v_anglePrevious = 3228  # offset

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
            "name": "MNetworkUserGroupProxy",
            "type": "Unknown"
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

class CBasePlayerWeapon(CEconEntity):
    m_OnPlayerUse = 3672  # offset
    m_flNextPrimaryAttackTickRatio = 3644  # offset
    m_flNextSecondaryAttackTickRatio = 3652  # offset
    m_iClip1 = 3656  # offset
    m_iClip2 = 3660  # offset
    m_nNextPrimaryAttackTick = 3640  # offset
    m_nNextSecondaryAttackTick = 3648  # offset
    m_pReserveAmmo = 3664  # offset

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
    m_bConformToCollisionBounds = 2696  # offset
    m_bModelOverrodeBlockLOS = 2688  # offset
    m_iShapeType = 2692  # offset
    m_mPreferredCatchTransform = 2704  # offset

class CBasePropDoor(CDynamicProp):
    m_OnAjarOpen = 4016  # offset
    m_OnBlockedClosing = 3656  # offset
    m_OnBlockedOpening = 3696  # offset
    m_OnClose = 3896  # offset
    m_OnFullyClosed = 3816  # offset
    m_OnFullyOpen = 3856  # offset
    m_OnLockedUse = 3976  # offset
    m_OnOpen = 3936  # offset
    m_OnUnblockedClosing = 3736  # offset
    m_OnUnblockedOpening = 3776  # offset
    m_SlaveName = 3640  # offset
    m_SoundClose = 3576  # offset
    m_SoundJiggle = 3616  # offset
    m_SoundLatch = 3600  # offset
    m_SoundLock = 3584  # offset
    m_SoundLockedAnim = 3624  # offset
    m_SoundMoving = 3560  # offset
    m_SoundOpen = 3568  # offset
    m_SoundPound = 3608  # offset
    m_SoundUnlock = 3592  # offset
    m_bFirstBlocked = 3484  # offset
    m_bForceClosed = 3520  # offset
    m_bLocked = 3452  # offset
    m_bNeedsHardware = 3444  # offset
    m_bNoNPCs = 3453  # offset
    m_closedAngles = 3468  # offset
    m_closedPosition = 3456  # offset
    m_eDoorState = 3448  # offset
    m_flAutoReturnDelay = 3408  # offset
    m_hActivator = 3536  # offset
    m_hBlocker = 3480  # offset
    m_hDoorList = 3416  # offset
    m_hMaster = 3648  # offset
    m_ls = 3488  # offset
    m_nHardwareType = 3440  # offset
    m_nPhysicsMaterial = 3636  # offset
    m_numCloseAttempts = 3632  # offset
    m_vecLatchWorldPosition = 3524  # offset

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
            "type_name": "CHandle<CBasePropDoor>"
        }
    ]

class CBasePulseGraphInstance:
    pass

class CBaseToggle(CBaseModelEntity):
    m_bAlwaysFireBlockedOutputs = 2048  # offset
    m_flHeight = 2112  # offset
    m_flLip = 2044  # offset
    m_flMoveDistance = 2036  # offset
    m_flWait = 2040  # offset
    m_hActivator = 2116  # offset
    m_movementType = 2144  # offset
    m_sMaster = 2152  # offset
    m_toggle_state = 2032  # offset
    m_vecAngle1 = 2088  # offset
    m_vecAngle2 = 2100  # offset
    m_vecFinalAngle = 2132  # offset
    m_vecFinalDest = 2120  # offset
    m_vecMoveAng = 2076  # offset
    m_vecPosition1 = 2052  # offset
    m_vecPosition2 = 2064  # offset

class CBaseTrigger(CBaseToggle):
    m_OnEndTouch = 2240  # offset
    m_OnEndTouchAll = 2280  # offset
    m_OnNotTouching = 2400  # offset
    m_OnStartTouch = 2160  # offset
    m_OnStartTouchAll = 2200  # offset
    m_OnTouching = 2320  # offset
    m_OnTouchingEachEntity = 2360  # offset
    m_bDisabled = 2476  # offset
    m_bUseAsyncQueries = 2488  # offset
    m_hFilter = 2472  # offset
    m_hTouchingEntities = 2440  # offset
    m_iFilterName = 2464  # offset

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

class CBaseTriggerAPI:
    pass

class CBeam(CBaseModelEntity):
    m_bTurnedOff = 2168  # offset
    m_fAmplitude = 2148  # offset
    m_fEndWidth = 2136  # offset
    m_fFadeLength = 2140  # offset
    m_fHaloScale = 2144  # offset
    m_fSpeed = 2156  # offset
    m_fStartFrame = 2152  # offset
    m_fWidth = 2132  # offset
    m_flDamage = 2044  # offset
    m_flFireTime = 2040  # offset
    m_flFrame = 2160  # offset
    m_flFrameRate = 2032  # offset
    m_flHDRColorScale = 2036  # offset
    m_hAttachEntity = 2080  # offset
    m_hBaseMaterial = 2056  # offset
    m_hEndEntity = 2184  # offset
    m_nAttachIndex = 2120  # offset
    m_nBeamFlags = 2076  # offset
    m_nBeamType = 2072  # offset
    m_nClipStyle = 2164  # offset
    m_nDissolveType = 2188  # offset
    m_nHaloIndex = 2064  # offset
    m_nNumBeamEnts = 2048  # offset
    m_vecEndPos = 2172  # offset

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

class CBlood(CPointEntity):
    m_Color = 1292  # offset
    m_flAmount = 1288  # offset
    m_vecSprayAngles = 1264  # offset
    m_vecSprayDir = 1276  # offset

class CBodyComponent(CEntityComponent):
    __m_pChainEntity = 72  # offset
    m_pSceneNode = 8  # offset

class CBodyComponentBaseAnimGraph(CBodyComponentSkeletonInstance):
    m_animationController = 1296  # offset

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

class CBombTarget(CBaseTrigger):
    m_OnBombDefused = 2576  # offset
    m_OnBombExplode = 2496  # offset
    m_OnBombPlanted = 2536  # offset
    m_bBombPlantedHere = 2618  # offset
    m_bIsBombSiteB = 2616  # offset
    m_bIsHeistBombTarget = 2617  # offset
    m_hInstructorHint = 2632  # offset
    m_nBombSiteDesignation = 2636  # offset
    m_szMountTarget = 2624  # offset

    __metadata__ =     [
        {
            "name": "m_bBombPlantedHere",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CBot:
    m_bHasSpawned = 32  # offset
    m_buttonFlags = 208  # offset
    m_forwardSpeed = 196  # offset
    m_id = 36  # offset
    m_isCrouching = 193  # offset
    m_isRunning = 192  # offset
    m_jumpTimestamp = 216  # offset
    m_leftSpeed = 200  # offset
    m_pController = 16  # offset
    m_pPlayer = 24  # offset
    m_postureStackIndex = 248  # offset
    m_verticalSpeed = 204  # offset
    m_viewForward = 220  # offset

class CBreakable(CBaseModelEntity):
    m_CPropDataComponent = 2040  # offset
    m_Explosion = 2112  # offset
    m_Material = 2104  # offset
    m_OnBreak = 2152  # offset
    m_OnHealthChanged = 2192  # offset
    m_PerformanceMode = 2232  # offset
    m_flLastPhysicsInfluenceTime = 2240  # offset
    m_flPressureDelay = 2128  # offset
    m_hBreaker = 2108  # offset
    m_hPhysicsAttacker = 2236  # offset
    m_iMinHealthDmg = 2132  # offset
    m_impactEnergyScale = 2144  # offset
    m_iszPropData = 2136  # offset
    m_iszSpawnObject = 2120  # offset
    m_nOverrideBlockLOS = 2148  # offset

    __metadata__ =     [
        {
            "name": "m_CPropDataComponent",
            "type": "NetworkVarNames",
            "type_name": "CPropDataComponent::Storage_t"
        }
    ]

class CBreakableProp(CBaseProp):
    m_BreakableContentsType = 3020  # offset
    m_CPropDataComponent = 2744  # offset
    m_OnBreak = 2848  # offset
    m_OnHealthChanged = 2888  # offset
    m_OnStartDeath = 2808  # offset
    m_OnTakeDamage = 2928  # offset
    m_PerformanceMode = 3012  # offset
    m_bHasBreakPiecesOrCommands = 3040  # offset
    m_bOriginalBlockLOS = 3121  # offset
    m_bUsePuntSound = 3120  # offset
    m_explodeDamage = 3044  # offset
    m_explodeRadius = 3048  # offset
    m_explosionBuildupSound = 3064  # offset
    m_explosionCustomEffect = 3072  # offset
    m_explosionCustomSound = 3080  # offset
    m_explosionDelay = 3056  # offset
    m_explosionModifier = 3088  # offset
    m_flDefBurstScale = 2992  # offset
    m_flDefaultFadeScale = 3104  # offset
    m_flLastPhysicsInfluenceTime = 3100  # offset
    m_flPressureDelay = 2988  # offset
    m_flPreventDamageBeforeTime = 3016  # offset
    m_hBreaker = 3008  # offset
    m_hLastAttacker = 3108  # offset
    m_hPhysicsAttacker = 3096  # offset
    m_iMinHealthDmg = 2972  # offset
    m_impactEnergyScale = 2968  # offset
    m_iszPuntSound = 3112  # offset
    m_preferredCarryAngles = 2976  # offset
    m_strBreakableContentsParticleOverride = 3032  # offset
    m_strBreakableContentsPropGroupOverride = 3024  # offset
    m_vDefBurstOffset = 2996  # offset

    __metadata__ =     [
        {
            "name": "m_CPropDataComponent",
            "type": "NetworkVarNames",
            "type_name": "CPropDataComponent::Storage_t"
        }
    ]

class CBtActionAim:
    m_AimTimer = 168  # offset
    m_FocusIntervalTimer = 216  # offset
    m_NextLookTarget = 156  # offset
    m_SniperHoldTimer = 192  # offset
    m_bAcquired = 240  # offset
    m_bDoneAiming = 140  # offset
    m_flLerpStartTime = 144  # offset
    m_flNextLookTargetLerpTime = 148  # offset
    m_flPenaltyReductionRatio = 152  # offset
    m_flZoomCooldownTimestamp = 136  # offset
    m_szAimReadyKey = 128  # offset
    m_szSensorInputKey = 104  # offset

class CBtActionCombatPositioning:
    m_ActionTimer = 136  # offset
    m_bCrouching = 160  # offset
    m_szIsAttackingKey = 128  # offset
    m_szSensorInputKey = 104  # offset

class CBtActionMoveTo:
    m_CheckApproximateCornersTimer = 144  # offset
    m_CheckHighPriorityItem = 168  # offset
    m_RepathTimer = 192  # offset
    m_bAutoLookAdjust = 132  # offset
    m_bComputePath = 133  # offset
    m_flAdditionalArrivalEpsilon2D = 220  # offset
    m_flArrivalEpsilon = 216  # offset
    m_flDamagingAreasPenaltyCost = 136  # offset
    m_flHidingSpotCheckDistanceThreshold = 224  # offset
    m_flNearestAreaDistanceThreshold = 228  # offset
    m_szDestinationInputKey = 96  # offset
    m_szHidingSpotInputKey = 104  # offset
    m_szThreatInputKey = 112  # offset
    m_vecDestination = 120  # offset

class CBtActionParachutePositioning:
    m_ActionTimer = 88  # offset

class CBtNodeCondition:
    m_bNegated = 88  # offset

class CBtNodeConditionInactive:
    m_SensorInactivityTimer = 128  # offset
    m_flRoundStartThresholdSeconds = 120  # offset
    m_flSensorInactivityThresholdSeconds = 124  # offset

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

class CBuyZone(CBaseTrigger):
    m_LegacyTeamNum = 2496  # offset

class CC4(CCSWeaponBase):
    m_bBombPlacedAnimation = 4600  # offset
    m_bBombPlanted = 4643  # offset
    m_bDoValidDroppedPositionCheck = 4592  # offset
    m_bIsPlantingViaUse = 4601  # offset
    m_bPlayedArmingBeeps = 4636  # offset
    m_bStartedArming = 4593  # offset
    m_entitySpottedState = 4608  # offset
    m_fArmedTime = 4596  # offset
    m_nSpotRules = 4632  # offset
    m_vecLastValidDroppedPosition = 4580  # offset
    m_vecLastValidPlayerHeldPosition = 4568  # offset

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

class CCSBot(CBot):
    m_aimError = 26832  # offset
    m_aimFocus = 26860  # offset
    m_aimFocusInterval = 26864  # offset
    m_aimFocusNextUpdate = 26868  # offset
    m_aimGoal = 26844  # offset
    m_alertTimer = 464  # offset
    m_allowAutoFollowTime = 436  # offset
    m_approachPointCount = 25640  # offset
    m_approachPointViewPosition = 25644  # offset
    m_areaEnteredTimestamp = 24092  # offset
    m_attackedTimestamp = 27508  # offset
    m_attacker = 27504  # offset
    m_attentionInterval = 27488  # offset
    m_avgVel = 27876  # offset
    m_avgVelCount = 27920  # offset
    m_avgVelIndex = 27916  # offset
    m_avoid = 1276  # offset
    m_avoidFriendTimer = 24120  # offset
    m_avoidTimestamp = 1280  # offset
    m_bAllowActive = 424  # offset
    m_bEyeAnglesUnderPathFinderControl = 1304  # offset
    m_bIsSleeping = 27608  # offset
    m_bendNoisePositionValid = 25180  # offset
    m_bentNoisePosition = 25168  # offset
    m_blindFire = 396  # offset
    m_bomber = 27472  # offset
    m_burnedByFlamesTimer = 27512  # offset
    m_checkedHidingSpotCount = 26776  # offset
    m_closestVisibleFriend = 27480  # offset
    m_closestVisibleHumanFriend = 27484  # offset
    m_combatRange = 340  # offset
    m_currentEnemyAcquireTimestamp = 26932  # offset
    m_desiredTeam = 25040  # offset
    m_diedLastRound = 380  # offset
    m_enemy = 26904  # offset
    m_enemyDeathTimestamp = 26936  # offset
    m_enemyQueueAttendIndex = 27802  # offset
    m_enemyQueueCount = 27801  # offset
    m_enemyQueueIndex = 27800  # offset
    m_equipTimer = 27536  # offset
    m_eyePosition = 264  # offset
    m_fireWeaponTimestamp = 27576  # offset
    m_firstSawEnemyTimestamp = 26928  # offset
    m_followTimestamp = 432  # offset
    m_forwardAngle = 25192  # offset
    m_friendDeathTimestamp = 26940  # offset
    m_goalEntity = 1272  # offset
    m_goalPosition = 1260  # offset
    m_hasJoined = 25044  # offset
    m_hasVisitedEnemySpawn = 1285  # offset
    m_hostageEscortCount = 25032  # offset
    m_hostageEscortCountTimestamp = 25036  # offset
    m_hurryTimer = 440  # offset
    m_ignoreEnemiesTimer = 26880  # offset
    m_inhibitLookAroundTimestamp = 25196  # offset
    m_inhibitWaitingForHostageTimer = 25048  # offset
    m_isAimingAtEnemy = 27532  # offset
    m_isAttacking = 1236  # offset
    m_isAvoidingGrenade = 25712  # offset
    m_isEnemySniperVisible = 27609  # offset
    m_isEnemyVisible = 26908  # offset
    m_isFollowing = 425  # offset
    m_isFriendInTheWay = 24144  # offset
    m_isLastEnemyDead = 26944  # offset
    m_isOpeningDoor = 1237  # offset
    m_isRapidFiring = 27533  # offset
    m_isRogue = 344  # offset
    m_isStopping = 1284  # offset
    m_isStuck = 27803  # offset
    m_isWaitingBehindFriend = 24176  # offset
    m_isWaitingForHostage = 25045  # offset
    m_lastEnemyPosition = 26912  # offset
    m_lastOrigin = 27924  # offset
    m_lastRadioRecievedTimestamp = 27940  # offset
    m_lastRadioSentTimestamp = 27944  # offset
    m_lastSawEnemyTimestamp = 26924  # offset
    m_lastValidReactionQueueFrame = 27976  # offset
    m_lastVictimID = 27528  # offset
    m_leader = 428  # offset
    m_lookAheadAngle = 25188  # offset
    m_lookAroundStateTimestamp = 25184  # offset
    m_lookAtDesc = 25240  # offset
    m_lookAtSpot = 25204  # offset
    m_lookAtSpotAngleTolerance = 25228  # offset
    m_lookAtSpotAttack = 25233  # offset
    m_lookAtSpotClearIfClose = 25232  # offset
    m_lookAtSpotDuration = 25220  # offset
    m_lookAtSpotTimestamp = 25224  # offset
    m_lookForWeaponsOnGroundTimer = 27584  # offset
    m_lookPitch = 26780  # offset
    m_lookPitchVel = 26784  # offset
    m_lookYaw = 26788  # offset
    m_lookYawVel = 26792  # offset
    m_mustRunTimer = 24296  # offset
    m_name = 276  # offset
    m_nearbyEnemyCount = 26948  # offset
    m_nearbyFriendCount = 27476  # offset
    m_nextCleanupCheckTimestamp = 27872  # offset
    m_noiseBendTimer = 25144  # offset
    m_noisePosition = 25096  # offset
    m_noiseSource = 25120  # offset
    m_noiseTimestamp = 25112  # offset
    m_noiseTravelDistance = 25108  # offset
    m_panicTimer = 512  # offset
    m_pathIndex = 24088  # offset
    m_pathLadderEnd = 24220  # offset
    m_peripheralTimestamp = 25248  # offset
    m_playerTravelDistance = 24368  # offset
    m_politeTimer = 24152  # offset
    m_radioPosition = 27952  # offset
    m_radioSubject = 27948  # offset
    m_repathTimer = 24096  # offset
    m_rogueTimer = 352  # offset
    m_safeTime = 384  # offset
    m_sawEnemySniperTimer = 27616  # offset
    m_sneakTimer = 488  # offset
    m_spotCheckTimestamp = 25744  # offset
    m_stateTimestamp = 1232  # offset
    m_stillTimer = 1288  # offset
    m_stuckJumpTimer = 27848  # offset
    m_stuckSpot = 27808  # offset
    m_stuckTimestamp = 27804  # offset
    m_surpriseTimer = 400  # offset
    m_targetSpot = 26796  # offset
    m_targetSpotPredicted = 26820  # offset
    m_targetSpotTime = 26856  # offset
    m_targetSpotVelocity = 26808  # offset
    m_taskEntity = 1244  # offset
    m_tossGrenadeTimer = 25680  # offset
    m_travelDistancePhase = 24624  # offset
    m_updateTravelDistanceTimer = 24344  # offset
    m_viewSteadyTimer = 25656  # offset
    m_visibleEnemyParts = 26909  # offset
    m_voiceEndTimestamp = 27964  # offset
    m_waitForHostageTimer = 25072  # offset
    m_waitTimer = 24320  # offset
    m_wasSafe = 388  # offset
    m_wiggleTimer = 27824  # offset
    m_zoomTimer = 27552  # offset

class CCSGO_TeamIntroCharacterPosition(CCSGO_TeamPreviewCharacterPosition):
    pass

class CCSGO_TeamIntroCounterTerroristPosition(CCSGO_TeamIntroCharacterPosition):
    pass

class CCSGO_TeamIntroTerroristPosition(CCSGO_TeamIntroCharacterPosition):
    pass

class CCSGO_TeamPreviewCharacterPosition(CBaseEntity):
    m_agentItem = 1296  # offset
    m_glovesItem = 1976  # offset
    m_nOrdinal = 1272  # offset
    m_nRandom = 1268  # offset
    m_nVariant = 1264  # offset
    m_sWeaponName = 1280  # offset
    m_weaponItem = 2656  # offset
    m_xuid = 1288  # offset

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

class CCSGO_TeamSelectCharacterPosition(CCSGO_TeamPreviewCharacterPosition):
    pass

class CCSGO_TeamSelectCounterTerroristPosition(CCSGO_TeamSelectCharacterPosition):
    pass

class CCSGO_TeamSelectTerroristPosition(CCSGO_TeamSelectCharacterPosition):
    pass

class CCSGO_WingmanIntroCharacterPosition(CCSGO_TeamIntroCharacterPosition):
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

class CCSGameRules:
    mTeamDMLastThinkTime = 3684  # offset
    mTeamDMLastWinningTeamNumber = 3680  # offset
    m_BtGlobalBlackboard = 4240  # offset
    m_CTSpawnPoints = 3992  # offset
    m_CTSpawnPointsMasterList = 3920  # offset
    m_MatchDevice = 304  # offset
    m_MinimapVerticalSectionHeights = 3260  # offset
    m_RetakeRules = 4400  # offset
    m_TeamRespawnWaveTimes = 2980  # offset
    m_TerroristSpawnPoints = 4016  # offset
    m_TerroristSpawnPointsMasterList = 3944  # offset
    m_arrProhibitedItemIndices = 2380  # offset
    m_arrSelectedHostageSpawnIndices = 3472  # offset
    m_arrTeamUniqueKillWeaponsMatch = 4808  # offset
    m_arrTournamentActiveCasterAccounts = 2580  # offset
    m_bAllowWeaponSwitch = 4104  # offset
    m_bAnyHostageReached = 284  # offset
    m_bBombDefused = 3825  # offset
    m_bBombDropped = 2604  # offset
    m_bBombPlanted = 2605  # offset
    m_bBuyTimeEnded = 3816  # offset
    m_bCTCantBuy = 2617  # offset
    m_bCTTimeOutActive = 213  # offset
    m_bCanDonateWeapons = 3751  # offset
    m_bCompleteReset = 3501  # offset
    m_bFirstConnected = 3500  # offset
    m_bForceTeamChangeSilent = 3592  # offset
    m_bFreezePeriod = 200  # offset
    m_bGameRestart = 252  # offset
    m_bHasHostageBeenTouched = 3424  # offset
    m_bHasMatchStarted = 308  # offset
    m_bHasTriggeredRoundStartMusic = 4204  # offset
    m_bIsDroppingItems = 2376  # offset
    m_bIsHltvActive = 2378  # offset
    m_bIsQuestEligible = 2377  # offset
    m_bIsQueuedMatchmaking = 288  # offset
    m_bIsUnreservedGameServer = 4040  # offset
    m_bIsValveDS = 296  # offset
    m_bLevelInitialized = 3436  # offset
    m_bLoadingRoundBackupData = 3593  # offset
    m_bLogoMap = 297  # offset
    m_bMapHasBombTarget = 285  # offset
    m_bMapHasBombZone = 3826  # offset
    m_bMapHasBuyZone = 287  # offset
    m_bMapHasRescueZone = 286  # offset
    m_bMatchWaitingForResume = 233  # offset
    m_bNeedToAskPlayersForContinueVote = 3540  # offset
    m_bNoCTsKilled = 3749  # offset
    m_bNoEnemiesKilled = 3750  # offset
    m_bNoTerroristsKilled = 3748  # offset
    m_bPickNewTeamsOnReset = 3502  # offset
    m_bPlayAllStepSoundsOnServer = 298  # offset
    m_bPlayedTeamIntroVO = 4964  # offset
    m_bRespawningAllRespawnablePlayers = 3968  # offset
    m_bRoundEndNoMusic = 5020  # offset
    m_bRoundEndShowTimerDefend = 4976  # offset
    m_bRoundTimeWarningTriggered = 4105  # offset
    m_bScrambleTeamsOnRestart = 3503  # offset
    m_bServerVoteOnReset = 3809  # offset
    m_bSwapTeamsOnRestart = 3504  # offset
    m_bSwitchingTeamsAtRoundReset = 4205  # offset
    m_bTCantBuy = 2616  # offset
    m_bTargetBombed = 3824  # offset
    m_bTeamIntroPeriod = 4956  # offset
    m_bTeamLastKillUsedUniqueWeaponMatch = 4904  # offset
    m_bTechnicalTimeOut = 232  # offset
    m_bTerroristTimeOutActive = 212  # offset
    m_bVoiceWonMatchBragFired = 3724  # offset
    m_bVoteCalled = 3808  # offset
    m_bWarmupPeriod = 201  # offset
    m_eRoundEndReason = 4972  # offset
    m_eRoundWinReason = 2612  # offset
    m_endMatchOnRoundReset = 3448  # offset
    m_endMatchOnThink = 3449  # offset
    m_fAccumulatedRoundOffDamage = 4120  # offset
    m_fAutobalanceDisplayTime = 4044  # offset
    m_fAvgPlayerRank = 3548  # offset
    m_fMatchStartTime = 240  # offset
    m_fNextUpdateTeamClanNamesTime = 4112  # offset
    m_fRoundStartTime = 244  # offset
    m_fTeamIntroPeriodEnd = 4960  # offset
    m_fWarmupNextChatNoticeTime = 3728  # offset
    m_fWarmupPeriodEnd = 204  # offset
    m_fWarmupPeriodStart = 208  # offset
    m_firstBloodTime = 3764  # offset
    m_firstKillTime = 3756  # offset
    m_flCMMItemDropRevealEndTime = 2372  # offset
    m_flCMMItemDropRevealStartTime = 2368  # offset
    m_flCTSpawnPointUsedTime = 3976  # offset
    m_flCTTimeOutRemaining = 220  # offset
    m_flGameStartTime = 256  # offset
    m_flIntermissionEndTime = 3432  # offset
    m_flIntermissionStartTime = 3428  # offset
    m_flLastPerfSampleTime = 21432  # offset
    m_flLastThinkTime = 4116  # offset
    m_flMatchInfoDecidedTime = 3652  # offset
    m_flNextHostageAnnouncement = 3744  # offset
    m_flNextRespawnWave = 3108  # offset
    m_flRestartRoundTime = 248  # offset
    m_flTeamDMLastAnnouncementTime = 3688  # offset
    m_flTerroristSpawnPointUsedTime = 3984  # offset
    m_flTerroristTimeOutRemaining = 216  # offset
    m_flVoteCheckThrottle = 3812  # offset
    m_gamePhase = 264  # offset
    m_hPlayerResource = 4392  # offset
    m_hostageWasInjured = 3792  # offset
    m_hostageWasKilled = 3793  # offset
    m_iAccountCT = 3696  # offset
    m_iAccountTerrorist = 3692  # offset
    m_iFreezeTime = 3452  # offset
    m_iHostagesRemaining = 280  # offset
    m_iHostagesRescued = 3736  # offset
    m_iHostagesTouched = 3740  # offset
    m_iLoserBonusMostRecentTeam = 3716  # offset
    m_iMatchStats_PlayersAlive_CT = 2740  # offset
    m_iMatchStats_PlayersAlive_T = 2860  # offset
    m_iMatchStats_RoundResults = 2620  # offset
    m_iMaxNumCTs = 3712  # offset
    m_iMaxNumTerrorists = 3708  # offset
    m_iNextCTSpawnPoint = 3972  # offset
    m_iNextTerroristSpawnPoint = 3980  # offset
    m_iNumCT = 3460  # offset
    m_iNumConsecutiveCTLoses = 3388  # offset
    m_iNumConsecutiveTerroristLoses = 3392  # offset
    m_iNumSpawnableCT = 3468  # offset
    m_iNumSpawnableTerrorist = 3464  # offset
    m_iNumTerrorist = 3456  # offset
    m_iRoundEndFunFactData1 = 4996  # offset
    m_iRoundEndFunFactData2 = 5000  # offset
    m_iRoundEndFunFactData3 = 5004  # offset
    m_iRoundEndFunFactPlayerSlot = 4992  # offset
    m_iRoundEndLegacy = 5024  # offset
    m_iRoundEndPlayerCount = 5016  # offset
    m_iRoundEndTimerTime = 4980  # offset
    m_iRoundEndWinnerTeam = 4968  # offset
    m_iRoundStartRoundNumber = 5032  # offset
    m_iRoundTime = 236  # offset
    m_iRoundWinStatus = 2608  # offset
    m_iSpawnPointCount_CT = 3704  # offset
    m_iSpawnPointCount_Terrorist = 3700  # offset
    m_iSpectatorSlotCount = 300  # offset
    m_iTotalRoundsPlayed = 3440  # offset
    m_iUnBalancedRounds = 3444  # offset
    m_nCTTeamIntroVariant = 4952  # offset
    m_nCTTimeOuts = 228  # offset
    m_nCTsAliveAtFreezetimeEnd = 3584  # offset
    m_nEndMatchMapGroupVoteOptions = 3344  # offset
    m_nEndMatchMapGroupVoteTypes = 3304  # offset
    m_nEndMatchMapVoteWinner = 3384  # offset
    m_nEndMatchTiedVotes = 3512  # offset
    m_nHalloweenMaskListSeed = 2600  # offset
    m_nLastFreezeEndBeep = 3820  # offset
    m_nMatchAbortedEarlyReason = 4200  # offset
    m_nMatchEndCount = 4944  # offset
    m_nMatchInfoShowType = 3648  # offset
    m_nNextMapInMapgroup = 312  # offset
    m_nOvertimePlaying = 276  # offset
    m_nQueuedMatchmakingMode = 292  # offset
    m_nRoundEndCount = 5028  # offset
    m_nRoundStartCount = 5036  # offset
    m_nRoundsPlayedThisPhase = 272  # offset
    m_nShorthandedBonusLastEvalRound = 4124  # offset
    m_nSpawnPointsRandomSeed = 3496  # offset
    m_nTTeamIntroVariant = 4948  # offset
    m_nTerroristTimeOuts = 224  # offset
    m_nTerroristsAliveAtFreezetimeEnd = 3588  # offset
    m_nTournamentPredictionsPct = 2364  # offset
    m_numBestOfMaps = 2596  # offset
    m_numQueuedMatchmakingAccounts = 3544  # offset
    m_numSpectatorsCountMax = 3564  # offset
    m_numSpectatorsCountMaxLnk = 3572  # offset
    m_numSpectatorsCountMaxTV = 3568  # offset
    m_numTotalTournamentDrops = 3560  # offset
    m_pGameModeRules = 4232  # offset
    m_pQueuedMatchmakingReservationString = 3552  # offset
    m_phaseChangeAnnouncementTime = 4108  # offset
    m_sRoundEndFunFactToken = 4984  # offset
    m_sRoundEndMessage = 5008  # offset
    m_szMatchStatTxt = 1340  # offset
    m_szTournamentEventName = 316  # offset
    m_szTournamentEventStage = 828  # offset
    m_szTournamentPredictionsTxt = 1852  # offset
    m_timeUntilNextPhaseStarts = 260  # offset
    m_tmNextPeriodicThink = 3720  # offset
    m_totalRoundsPlayed = 268  # offset
    m_ullLocalMatchID = 3296  # offset
    m_vMinimapMaxs = 3248  # offset
    m_vMinimapMins = 3236  # offset
    m_vecMainCTSpawnPos = 3904  # offset

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

class CCSGameRulesProxy(CGameRulesProxy):
    m_pGameRules = 1264  # offset

    __metadata__ =     [
        {
            "name": "m_pGameRules",
            "type": "NetworkVarNames",
            "type_name": "CCSGameRules*"
        }
    ]

class CCSMinimapBoundary(CBaseEntity):
    pass

class CCSObserverPawn(CCSPlayerPawnBase):
    pass

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

class CCSObserver_CameraServices(CCSPlayerBase_CameraServices):
    pass

class CCSObserver_MovementServices(CPlayer_MovementServices):
    pass

class CCSObserver_ObserverServices(CPlayer_ObserverServices):
    pass

class CCSObserver_UseServices(CPlayer_UseServices):
    pass

class CCSPetPlacement(CBaseEntity):
    pass

class CCSPlace(CServerOnlyModelEntity):
    m_name = 2056  # offset

class CCSPlayerBase_CameraServices(CPlayer_CameraServices):
    m_flFOVRate = 380  # offset
    m_flFOVTime = 376  # offset
    m_hLastFogTrigger = 416  # offset
    m_hTriggerFogList = 392  # offset
    m_hZoomOwner = 384  # offset
    m_iFOV = 368  # offset
    m_iFOVStart = 372  # offset

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
    m_DesiredObserverMode = 2348  # offset
    m_LastTeamDamageWarningTime = 2488  # offset
    m_LastTimePlayerWasDisconnectedForPawnsRemove = 2492  # offset
    m_bAbandonAllowsSurrender = 2306  # offset
    m_bAbandonOffersInstantSurrender = 2307  # offset
    m_bAttemptedToGetColor = 2149  # offset
    m_bCanControlObservedBot = 2336  # offset
    m_bCannotBeKicked = 2304  # offset
    m_bControllingBot = 2328  # offset
    m_bDisconnection1MinWarningPrinted = 2308  # offset
    m_bEverFullyConnected = 2305  # offset
    m_bEverPlayedOnTeam = 2148  # offset
    m_bFireBulletsSeedSynchronized = 2665  # offset
    m_bGaveTeamDamageWarning = 2474  # offset
    m_bGaveTeamDamageWarningThisRound = 2475  # offset
    m_bHasBeenControlledByPlayerThisRound = 2330  # offset
    m_bHasCommunicationAbuseMute = 2116  # offset
    m_bHasControlledBotThisRound = 2329  # offset
    m_bHasSeenJoinGame = 2158  # offset
    m_bInSwitchTeam = 2157  # offset
    m_bJustBecameSpectator = 2159  # offset
    m_bJustDidTeamKill = 2472  # offset
    m_bMvpNoMusic = 2410  # offset
    m_bPawnHasDefuser = 2368  # offset
    m_bPawnHasHelmet = 2369  # offset
    m_bPawnIsAlive = 2356  # offset
    m_bPunishForTeamKill = 2473  # offset
    m_bRemoveAllItemsOnNextRoundReset = 2161  # offset
    m_bScoreReported = 2309  # offset
    m_bShowHints = 2464  # offset
    m_bSwitchTeamsOnNextRoundReset = 2160  # offset
    m_bTeamChanged = 2156  # offset
    m_dblLastReceivedPacketPlatFloatTime = 2480  # offset
    m_eMvpReason = 2412  # offset
    m_eNetworkDisconnectionReason = 2300  # offset
    m_flForceTeamTime = 2140  # offset
    m_flLastJoinTeamTime = 2164  # offset
    m_flSmoothedPing = 2432  # offset
    m_hDesiredObserverTarget = 2352  # offset
    m_hObserverPawn = 2344  # offset
    m_hOriginalControllerOfCurrentPawn = 2384  # offset
    m_hPlayerPawn = 2340  # offset
    m_iCoachingTeam = 2176  # offset
    m_iCompTeammateColor = 2144  # offset
    m_iCompetitiveRankType = 2208  # offset
    m_iCompetitiveRanking = 2200  # offset
    m_iCompetitiveRankingPredicted_Loss = 2216  # offset
    m_iCompetitiveRankingPredicted_Tie = 2220  # offset
    m_iCompetitiveRankingPredicted_Win = 2212  # offset
    m_iCompetitiveWins = 2204  # offset
    m_iDraftIndex = 2288  # offset
    m_iMVPs = 2424  # offset
    m_iMusicKitID = 2416  # offset
    m_iMusicKitMVPs = 2420  # offset
    m_iNextTimeCheck = 2468  # offset
    m_iPawnArmor = 2364  # offset
    m_iPawnBotDifficulty = 2380  # offset
    m_iPawnHealth = 2360  # offset
    m_iPawnLifetimeEnd = 2376  # offset
    m_iPawnLifetimeStart = 2372  # offset
    m_iPendingTeamNum = 2136  # offset
    m_iPing = 2112  # offset
    m_iRoundScore = 2392  # offset
    m_iRoundsWon = 2396  # offset
    m_iScore = 2388  # offset
    m_iTeammatePreferredColor = 2152  # offset
    m_lastHeldVoteTimer = 2440  # offset
    m_msQueuedModeDisconnectionTimestamp = 2292  # offset
    m_nBotsControlledThisRound = 2332  # offset
    m_nDisconnectionTick = 2312  # offset
    m_nEndMatchNextMapVote = 2224  # offset
    m_nFirstKill = 2408  # offset
    m_nKillCount = 2409  # offset
    m_nNonSuspiciousHitStreak = 2500  # offset
    m_nPawnCharacterDefIndex = 2370  # offset
    m_nPlayerDominated = 2184  # offset
    m_nPlayerDominatingMe = 2192  # offset
    m_nQuestProgressReason = 2236  # offset
    m_nSuspiciousHitCount = 2496  # offset
    m_nUpdateCounter = 2428  # offset
    m_pActionTrackingServices = 2096  # offset
    m_pDamageServices = 2104  # offset
    m_pInGameMoneyServices = 2080  # offset
    m_pInventoryServices = 2088  # offset
    m_recentKillQueue = 2400  # offset
    m_rtActiveMissionPeriod = 2232  # offset
    m_szClan = 2168  # offset
    m_szCrosshairCodes = 2128  # offset
    m_uiAbandonRecordedReason = 2296  # offset
    m_uiCommunicationMuteFlags = 2120  # offset
    m_unActiveQuestId = 2228  # offset
    m_unPlayerTvControlFlags = 2240  # offset

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
    m_flTotalRoundDamageDealt = 400  # offset
    m_iNumRoundKills = 392  # offset
    m_iNumRoundKillsHeadshots = 396  # offset
    m_matchStats = 200  # offset
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
    m_bReceivesMoneyNextRound = 64  # offset
    m_iAccount = 72  # offset
    m_iCashSpentThisRound = 84  # offset
    m_iMoneyEarnedForNextRound = 68  # offset
    m_iStartAccount = 76  # offset
    m_iTotalCashSpent = 80  # offset

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
    m_nPersonaDataPublicCommendsFriendly = 104  # offset
    m_nPersonaDataPublicCommendsLeader = 96  # offset
    m_nPersonaDataPublicCommendsTeacher = 100  # offset
    m_nPersonaDataPublicLevel = 92  # offset
    m_nPersonaDataXpTrailLevel = 108  # offset
    m_rank = 68  # offset
    m_unCurrentLoadoutHash = 3920  # offset
    m_unEquippedPlayerSprayIDs = 3912  # offset
    m_unMusicID = 64  # offset
    m_vecServerAuthoritativeWeaponSlots = 3928  # offset

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

class CCSPlayerPawn(CCSPlayerPawnBase):
    m_ArmorValue = 6972  # offset
    m_EconGloves = 6048  # offset
    m_GunGameImmunityColor = 7044  # offset
    m_LastHealth = 6912  # offset
    m_LastHitBox = 6908  # offset
    m_PredictedDamageTags = 7168  # offset
    m_RetakesMVPBoostExtraUtility = 4100  # offset
    m_TouchingBuyZones = 4056  # offset
    m_aimPunchAngle = 4112  # offset
    m_aimPunchAngleVel = 4124  # offset
    m_aimPunchCache = 4144  # offset
    m_aimPunchTickBase = 4136  # offset
    m_aimPunchTickFraction = 4140  # offset
    m_allowAutoFollowTime = 6792  # offset
    m_angEyeAngles = 7292  # offset
    m_angShootAngleHistory = 7092  # offset
    m_angStashedShootAngles = 7056  # offset
    m_bBotAllowActive = 6928  # offset
    m_bCommittingSuicideOnTeamChange = 7276  # offset
    m_bGrenadeParametersStashed = 7052  # offset
    m_bGunGameImmunity = 7284  # offset
    m_bHasDeathInfo = 7004  # offset
    m_bHasFemaleVoice = 3842  # offset
    m_bInBombZone = 4082  # offset
    m_bInBombZoneTrigger = 6860  # offset
    m_bInBuyZone = 4049  # offset
    m_bInHostageRescueZone = 4081  # offset
    m_bInHostageResetZone = 4048  # offset
    m_bInNoDefuseArea = 6848  # offset
    m_bIsBuyMenuOpen = 4168  # offset
    m_bIsDefusing = 6838  # offset
    m_bIsGrabbingHostage = 6839  # offset
    m_bIsScoped = 6836  # offset
    m_bIsSpawning = 6988  # offset
    m_bIsWalking = 6768  # offset
    m_bKilledByHeadshot = 6904  # offset
    m_bLastHeadBoneTransformIsValid = 5904  # offset
    m_bLeftHanded = 6745  # offset
    m_bNextSprayDecalTimeExpedited = 5932  # offset
    m_bOnGroundLastTick = 5912  # offset
    m_bRagdollDamageHeadshot = 6028  # offset
    m_bResetArmorNextSpawn = 6796  # offset
    m_bResumeZoom = 6837  # offset
    m_bRetakesHasDefuseKit = 4092  # offset
    m_bRetakesMVPLastRound = 4093  # offset
    m_bSkipOneHeadConstraintUpdate = 6744  # offset
    m_bWaitForNoAttack = 6896  # offset
    m_bWasInBombZoneTrigger = 6861  # offset
    m_bWasInBuyZone = 4080  # offset
    m_bWasInHostageRescueZone = 4083  # offset
    m_entitySpottedState = 6808  # offset
    m_fImmuneToGunGameDamageTime = 7280  # offset
    m_fLastGivenBombTime = 6776  # offset
    m_fLastGivenDefuserTime = 6772  # offset
    m_fMolotovDamageTime = 7288  # offset
    m_fSwitchedHandednessTime = 6748  # offset
    m_flDealtDamageToEnemyMostRecentTimestamp = 6780  # offset
    m_flDeathInfoTime = 7008  # offset
    m_flEmitSoundTime = 6844  # offset
    m_flFlinchStack = 6868  # offset
    m_flHealthShotBoostExpirationTime = 4104  # offset
    m_flHitHeading = 6876  # offset
    m_flLandingTimeSeconds = 4108  # offset
    m_flLastAttackedTeammate = 6788  # offset
    m_flLastPickupPriorityTime = 6968  # offset
    m_flNextSprayDecalTime = 5928  # offset
    m_flSlopeDropHeight = 6948  # offset
    m_flSlopeDropOffset = 6944  # offset
    m_flTimeOfLastInjury = 5924  # offset
    m_flVelocityModifier = 6872  # offset
    m_flViewmodelFOV = 6764  # offset
    m_flViewmodelOffsetX = 6752  # offset
    m_flViewmodelOffsetY = 6756  # offset
    m_flViewmodelOffsetZ = 6760  # offset
    m_grenadeParameterStashTime = 7048  # offset
    m_iBlockingUseActionInProgress = 6840  # offset
    m_iBombSiteIndex = 6852  # offset
    m_iDeathFlags = 7000  # offset
    m_iDisplayHistoryBits = 6784  # offset
    m_iLastWeaponFireUsercmd = 6984  # offset
    m_iPlayerLocked = 5916  # offset
    m_iRetakesMVPBoostItem = 4096  # offset
    m_iRetakesOffering = 4084  # offset
    m_iRetakesOfferingCard = 4088  # offset
    m_iShotsFired = 6864  # offset
    m_ignoreLadderJumpTime = 6900  # offset
    m_lastLandTime = 5908  # offset
    m_nCharacterDefIndex = 3840  # offset
    m_nEconGlovesChanged = 6728  # offset
    m_nHighestAppliedDamageTagTick = 7272  # offset
    m_nHitBodyPart = 6880  # offset
    m_nLastKillerIndex = 6800  # offset
    m_nLastPickupPriority = 6964  # offset
    m_nRagdollDamageBone = 5936  # offset
    m_nSpotRules = 6832  # offset
    m_nWhichBombZone = 6856  # offset
    m_pActionTrackingServices = 3816  # offset
    m_pBot = 6920  # offset
    m_pBulletServices = 3792  # offset
    m_pBuyServices = 3808  # offset
    m_pDamageReactServices = 3832  # offset
    m_pHostageServices = 3800  # offset
    m_pRadioServices = 3824  # offset
    m_qDeathEyeAngles = 6732  # offset
    m_strVOPrefix = 3848  # offset
    m_szLastPlaceName = 3856  # offset
    m_szRagdollDamageWeaponName = 5964  # offset
    m_thirdPersonHeading = 6932  # offset
    m_unCurrentEquipmentValue = 6976  # offset
    m_unFreezetimeEndEquipmentValue = 6980  # offset
    m_unRoundStartEquipmentValue = 6978  # offset
    m_vHeadConstraintOffset = 6952  # offset
    m_vRagdollDamageForce = 5940  # offset
    m_vRagdollDamagePosition = 5952  # offset
    m_vRagdollServerOrigin = 6032  # offset
    m_vecDeathInfoOrigin = 7012  # offset
    m_vecPlayerPatchEconIndices = 7024  # offset
    m_vecStashedGrenadeThrowPosition = 7068  # offset
    m_vecStashedVelocity = 7080  # offset
    m_vecThrowPositionHistory = 7116  # offset
    m_vecTotalBulletForce = 6884  # offset
    m_vecVelocityHistory = 7140  # offset
    m_wasNotKilledNaturally = 7277  # offset
    m_xLastHeadBoneTransform = 5872  # offset

    __metadata__ =     [
        {
            "name": "MNetworkOutOfPVSUpdates",
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
            "name": "MNetworkVarTypeOverride",
            "type": "Unknown"
        },
        {
            "name": "MNetworkIncludeByName",
            "type": "Unknown"
        },
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
            "name": "m_pActionTrackingServices",
            "type": "NetworkVarNames",
            "type_name": "CCSPlayer_ActionTrackingServices*"
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
            "name": "m_flHealthShotBoostExpirationTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
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
            "name": "m_bIsWalking",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_nLastKillerIndex",
            "type": "NetworkVarNames",
            "type_name": "CEntityIndex"
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
            "name": "m_thirdPersonHeading",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        },
        {
            "name": "m_flSlopeDropOffset",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flSlopeDropHeight",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_vHeadConstraintOffset",
            "type": "NetworkVarNames",
            "type_name": "Vector"
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
        },
        {
            "name": "m_angEyeAngles",
            "type": "NetworkVarNames",
            "type_name": "QAngle"
        }
    ]

class CCSPlayerPawnBase(CBasePlayerPawn):
    m_CTouchExpansionComponent = 3472  # offset
    m_bHasMovedSinceSpawn = 3745  # offset
    m_bRespawning = 3744  # offset
    m_blindStartTime = 3564  # offset
    m_blindUntilTime = 3560  # offset
    m_fNextRadarUpdateTime = 3760  # offset
    m_flFlashDuration = 3764  # offset
    m_flFlashMaxAlpha = 3768  # offset
    m_flIdleTimeSinceLastAction = 3756  # offset
    m_flProgressBarStartTime = 3772  # offset
    m_hOriginalController = 3780  # offset
    m_iNumSpawns = 3748  # offset
    m_iPlayerState = 3568  # offset
    m_iProgressBarDuration = 3776  # offset
    m_pPingServices = 3552  # offset

    __metadata__ =     [
        {
            "name": "m_CTouchExpansionComponent",
            "type": "NetworkVarNames",
            "type_name": "CTouchExpansionComponent::Storage_t"
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
            "name": "m_flFlashDuration",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flFlashMaxAlpha",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_flProgressBarStartTime",
            "type": "NetworkVarNames",
            "type_name": "float"
        },
        {
            "name": "m_iProgressBarDuration",
            "type": "NetworkVarNames",
            "type_name": "int"
        },
        {
            "name": "m_hOriginalController",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerController>"
        }
    ]

class CCSPlayerResource(CBaseEntity):
    m_bEndMatchNextMapAllVoted = 1408  # offset
    m_bHostageAlive = 1264  # offset
    m_bombsiteCenterA = 1336  # offset
    m_bombsiteCenterB = 1348  # offset
    m_foundGoalPositions = 1409  # offset
    m_hostageRescueX = 1360  # offset
    m_hostageRescueY = 1376  # offset
    m_hostageRescueZ = 1392  # offset
    m_iHostageEntityIDs = 1288  # offset
    m_isHostageFollowingSomeone = 1276  # offset

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

class CCSPlayer_ActionTrackingServices(CPlayerPawnComponent):
    m_bIsRescuing = 540  # offset
    m_hLastWeaponBeforeC4AutoSwitch = 496  # offset
    m_weaponPurchasesThisMatch = 544  # offset
    m_weaponPurchasesThisRound = 656  # offset

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
    m_vecSellbackPurchaseEntries = 200  # offset

    __metadata__ =     [
        {
            "name": "m_vecSellbackPurchaseEntries",
            "type": "NetworkVarNames",
            "type_name": "SellbackPurchaseEntry_t"
        }
    ]

class CCSPlayer_CameraServices(CCSPlayerBase_CameraServices):
    pass

class CCSPlayer_DamageReactServices(CPlayerPawnComponent):
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
    m_StuckLast = 1236  # offset
    m_bDesiresDuck = 665  # offset
    m_bDuckOverride = 664  # offset
    m_bHasWalkMovedSinceLastJump = 705  # offset
    m_bInStuckTest = 706  # offset
    m_bMadeFootstepNoise = 1292  # offset
    m_bOldJumpPressed = 1300  # offset
    m_bSpeedCropped = 1240  # offset
    m_bWasSurfing = 1356  # offset
    m_duckUntilOnGround = 704  # offset
    m_fStashGrenadeParameterWhen = 1308  # offset
    m_flAccumulatedJumpError = 1348  # offset
    m_flDuckAmount = 656  # offset
    m_flDuckOffset = 668  # offset
    m_flDuckSpeed = 660  # offset
    m_flHeightAtJumpStart = 1332  # offset
    m_flJumpPressedTime = 1304  # offset
    m_flLastDuckTime = 684  # offset
    m_flMaxJumpHeightLastJump = 1340  # offset
    m_flMaxJumpHeightThisJump = 1336  # offset
    m_flOffsetTickCompleteTime = 1320  # offset
    m_flOffsetTickStashedSpeed = 1324  # offset
    m_flStamina = 1328  # offset
    m_flStaminaAtJumpStart = 1344  # offset
    m_flTicksSinceLastSurfingDetected = 1352  # offset
    m_flWaterEntryTime = 1248  # offset
    m_iFootsteps = 1296  # offset
    m_nButtonDownMaskPrev = 1312  # offset
    m_nDuckJumpTimeMsecs = 676  # offset
    m_nDuckTimeMsecs = 672  # offset
    m_nGameCodeHasMovedPlayerAfterCommand = 1288  # offset
    m_nJumpTimeMsecs = 680  # offset
    m_nLadderSurfacePropIndex = 652  # offset
    m_nOldWaterLevel = 1244  # offset
    m_nTraceCount = 1232  # offset
    m_vecForward = 1252  # offset
    m_vecInputRotated = 1500  # offset
    m_vecLadderNormal = 640  # offset
    m_vecLastPositionAtFullCrouchSpeed = 696  # offset
    m_vecLeft = 1264  # offset
    m_vecUp = 1276  # offset

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
    m_flPlayerPingTokens = 64  # offset
    m_hPlayerPing = 84  # offset

    __metadata__ =     [
        {
            "name": "m_hPlayerPing",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        }
    ]

class CCSPlayer_RadioServices(CPlayerPawnComponent):
    m_bIgnoreRadio = 88  # offset
    m_flC4PlantTalkTimer = 72  # offset
    m_flDefusingTalkTimer = 68  # offset
    m_flGotHostageTalkTimer = 64  # offset
    m_flRadioTokenSlots = 76  # offset

class CCSPlayer_UseServices(CPlayer_UseServices):
    m_flLastUseTimeStamp = 68  # offset
    m_flTimeLastUsedWindow = 72  # offset
    m_hLastKnownUseEntity = 64  # offset

class CCSPlayer_WaterServices(CPlayer_WaterServices):
    m_AirFinishedTime = 72  # offset
    m_NextDrownDamageTime = 64  # offset
    m_flSwimSoundTime = 92  # offset
    m_flWaterJumpTime = 76  # offset
    m_nDrownDmgRate = 68  # offset
    m_vecWaterJumpVel = 80  # offset

class CCSPlayer_WeaponServices(CPlayer_WeaponServices):
    m_bBlockInspectUntilNextGraphUpdate = 6360  # offset
    m_bDisableAutoDeploy = 215  # offset
    m_bIsBeingGivenItem = 212  # offset
    m_bIsHoldingLookAtWeapon = 189  # offset
    m_bIsLookingAtWeapon = 188  # offset
    m_bIsPickingUpGroundWeapon = 216  # offset
    m_bIsPickingUpItemWithUse = 213  # offset
    m_bPickedUpWeapon = 214  # offset
    m_flNextAttack = 184  # offset
    m_hSavedWeapon = 192  # offset
    m_nTimeToMelee = 196  # offset
    m_nTimeToPrimary = 204  # offset
    m_nTimeToSecondary = 200  # offset
    m_nTimeToSniperRifle = 208  # offset
    m_networkAnimTiming = 6336  # offset

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

class CCSPointPulseAPI:
    pass

class CCSPointScriptEntity(CBaseEntity):
    pass

class CCSServerPointScriptEntity(CCSPointScriptEntity):
    pass

class CCSSprite(CSprite):
    pass

class CCSTeam(CTeam):
    m_bSurrendered = 1456  # offset
    m_flNextResourceTime = 2140  # offset
    m_iClanID = 2120  # offset
    m_iLastUpdateSentAt = 2144  # offset
    m_nLastRecievedShorthandedRoundBonus = 1448  # offset
    m_nShorthandedRoundBonusStartRound = 1452  # offset
    m_numMapVictories = 1972  # offset
    m_scoreFirstHalf = 1976  # offset
    m_scoreOvertime = 1984  # offset
    m_scoreSecondHalf = 1980  # offset
    m_szClanTeamname = 1988  # offset
    m_szTeamFlagImage = 2124  # offset
    m_szTeamLogoImage = 2132  # offset
    m_szTeamMatchStat = 1457  # offset

    __metadata__ =     [
        {
            "name": "m_bSurrendered",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
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

class CCSWeaponBase(CBasePlayerWeapon):
    m_IronSightController = 4048  # offset
    m_OnPlayerPickup = 3824  # offset
    m_bBurstMode = 3908  # offset
    m_bCanBePickedUp = 3968  # offset
    m_bDroppedNearBuyZone = 3944  # offset
    m_bFireOnEmpty = 3816  # offset
    m_bInReload = 3920  # offset
    m_bInspectPending = 3740  # offset
    m_bInspectShouldLoop = 3741  # offset
    m_bIsHauledBack = 3928  # offset
    m_bPlayerAmmoStockOnPickup = 3728  # offset
    m_bRemoveable = 3712  # offset
    m_bRequireUseToTouch = 3729  # offset
    m_bSilencerOn = 3929  # offset
    m_bUseCanOverrideNextOwnerTouchTime = 3969  # offset
    m_bWasActiveWeaponWhenDropped = 3996  # offset
    m_bWasOwnedByCT = 4036  # offset
    m_bWasOwnedByTerrorist = 4037  # offset
    m_donated = 4028  # offset
    m_fAccuracyPenalty = 3888  # offset
    m_fAccuracySmoothedForZoom = 3896  # offset
    m_fLastShotTime = 4032  # offset
    m_flDroppedAtTime = 3924  # offset
    m_flInspectCancelCompleteTime = 3736  # offset
    m_flLastAccuracyUpdateTime = 3892  # offset
    m_flLastLOSTraceFailureTime = 4076  # offset
    m_flLastShakeTime = 4096  # offset
    m_flNextAttackRenderTimeOffset = 3948  # offset
    m_flPostponeFireReadyFrac = 3916  # offset
    m_flRecoilIndex = 3904  # offset
    m_flTimeSilencerSwitchComplete = 3932  # offset
    m_flTurningInaccuracy = 3884  # offset
    m_flTurningInaccuracyDelta = 3868  # offset
    m_flWatTickOffset = 4080  # offset
    m_flWeaponGameplayAnimStateTimestamp = 3732  # offset
    m_hPrevOwner = 3988  # offset
    m_iIronSightMode = 4072  # offset
    m_iMostRecentTeamNumber = 3940  # offset
    m_iOriginalTeamNumber = 3936  # offset
    m_iRecoilIndex = 3900  # offset
    m_iWeaponGameplayAnimState = 3730  # offset
    m_nDropTick = 3992  # offset
    m_nLastEmptySoundCmdNum = 3784  # offset
    m_nPostponeFireReadyTicks = 3912  # offset
    m_nextOwnerTouchTime = 3972  # offset
    m_nextPrevOwnerTouchTime = 3976  # offset
    m_nextPrevOwnerUseTime = 3984  # offset
    m_numRemoveUnownedWeaponThink = 4040  # offset
    m_vecTurningInaccuracyEyeDirLast = 3872  # offset
    m_weaponMode = 3864  # offset

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

class CCSWeaponBaseGun(CCSWeaponBase):
    m_bNeedsBoltAction = 4541  # offset
    m_bSkillBoltInterruptAvailable = 4550  # offset
    m_bSkillBoltLiftedFireKey = 4551  # offset
    m_bSkillReloadAvailable = 4548  # offset
    m_bSkillReloadLiftedReloadKey = 4549  # offset
    m_iBurstShotsRemaining = 4524  # offset
    m_inPrecache = 4540  # offset
    m_nRevolverCylinderIdx = 4544  # offset
    m_silencedModelIndex = 4536  # offset
    m_zoomLevel = 4520  # offset

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

class CCSWeaponBaseShotgun(CCSWeaponBase):
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

class CChangeLevel(CBaseTrigger):
    m_OnChangeLevel = 2512  # offset
    m_bNewChapter = 2554  # offset
    m_bNoTouch = 2553  # offset
    m_bOnChangeLevelFired = 2555  # offset
    m_bTouched = 2552  # offset
    m_sLandmarkName = 2504  # offset
    m_sMapName = 2496  # offset

class CChicken(CDynamicProp):
    m_AttributeManager = 3424  # offset
    m_BlockDirectionTimer = 12896  # offset
    m_activityTimer = 4296  # offset
    m_bInJump = 4492  # offset
    m_collisionStuckTimer = 4248  # offset
    m_currentActivity = 4292  # offset
    m_desiredActivity = 4288  # offset
    m_flActiveFollowStartTime = 12860  # offset
    m_flLastJumpTime = 4488  # offset
    m_flWhenZombified = 4400  # offset
    m_fleeFrom = 4324  # offset
    m_followMinuteTimer = 12864  # offset
    m_hasBeenUsed = 4456  # offset
    m_isOnGround = 4272  # offset
    m_jumpTimer = 4464  # offset
    m_jumpedThisFrame = 4404  # offset
    m_leader = 4408  # offset
    m_moveRateThrottleTimer = 4328  # offset
    m_repathTimer = 12696  # offset
    m_reuseTimer = 4432  # offset
    m_startleTimer = 4352  # offset
    m_stuckAnchor = 4208  # offset
    m_stuckTimer = 4224  # offset
    m_turnRate = 4320  # offset
    m_updateTimer = 4184  # offset
    m_vFallVelocity = 4276  # offset
    m_vecPathGoal = 12848  # offset
    m_vocalizeTimer = 4376  # offset

    __metadata__ =     [
        {
            "name": "m_AttributeManager",
            "type": "NetworkVarNames",
            "type_name": "CAttributeContainer"
        },
        {
            "name": "m_jumpedThisFrame",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_leader",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CCSPlayerPawn>"
        }
    ]

class CCitadelSoundOpvarSetOBB(CBaseEntity):
    m_iszOperatorName = 1272  # offset
    m_iszOpvarName = 1280  # offset
    m_iszStackName = 1264  # offset
    m_nAABBDirection = 1336  # offset
    m_vDistanceInnerMaxs = 1300  # offset
    m_vDistanceInnerMins = 1288  # offset
    m_vDistanceOuterMaxs = 1324  # offset
    m_vDistanceOuterMins = 1312  # offset

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

class CColorCorrection(CBaseEntity):
    m_MaxFalloff = 1304  # offset
    m_MinFalloff = 1300  # offset
    m_bClientSide = 1295  # offset
    m_bEnabled = 1293  # offset
    m_bExclusive = 1296  # offset
    m_bMaster = 1294  # offset
    m_bStartDisabled = 1292  # offset
    m_flCurWeight = 1308  # offset
    m_flFadeInDuration = 1264  # offset
    m_flFadeOutDuration = 1268  # offset
    m_flMaxWeight = 1288  # offset
    m_flStartFadeInWeight = 1272  # offset
    m_flStartFadeOutWeight = 1276  # offset
    m_flTimeStartFadeIn = 1280  # offset
    m_flTimeStartFadeOut = 1284  # offset
    m_lookupFilename = 1824  # offset
    m_netlookupFilename = 1312  # offset

    __metadata__ =     [
        {
            "name": "MNetworkIncludeByUserGroup",
            "type": "Unknown"
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
            "name": "m_flCurWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_netlookupFilename",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class CColorCorrectionVolume(CBaseTrigger):
    m_FadeDuration = 2500  # offset
    m_LastEnterTime = 3024  # offset
    m_LastEnterWeight = 3020  # offset
    m_LastExitTime = 3032  # offset
    m_LastExitWeight = 3028  # offset
    m_MaxWeight = 2496  # offset
    m_Weight = 2504  # offset
    m_lookupFilename = 2508  # offset

    __metadata__ =     [
        {
            "name": "m_MaxWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_FadeDuration",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_Weight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_lookupFilename",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class CCommentaryAuto(CBaseEntity):
    m_OnCommentaryMidGame = 1304  # offset
    m_OnCommentaryMultiplayerSpawn = 1344  # offset
    m_OnCommentaryNewGame = 1264  # offset

class CCommentaryViewPosition(CSprite):
    pass

class CConstraintAnchor(CBaseAnimGraph):
    m_massScale = 2688  # offset

class CCredits(CPointEntity):
    m_OnCreditsDone = 1264  # offset
    m_bRolledOutroCredits = 1304  # offset
    m_flLogoLength = 1308  # offset

class CDEagle(CCSWeaponBaseGun):
    pass

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

class CDebugHistory(CBaseEntity):
    m_nNpcEvents = 4097328  # offset

class CDecoyGrenade(CBaseCSGrenade):
    pass

class CDecoyProjectile(CBaseCSGrenadeProjectile):
    m_decoyWeaponDefIndex = 3160  # offset
    m_fExpireTime = 3144  # offset
    m_nDecoyShotTick = 3136  # offset
    m_shotsRemaining = 3140  # offset

    __metadata__ =     [
        {
            "name": "m_nDecoyShotTick",
            "type": "NetworkVarNames",
            "type_name": "int"
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

class CDynamicLight(CBaseModelEntity):
    m_ActualFlags = 2032  # offset
    m_Exponent = 2040  # offset
    m_Flags = 2033  # offset
    m_InnerAngle = 2044  # offset
    m_LightStyle = 2034  # offset
    m_On = 2035  # offset
    m_OuterAngle = 2048  # offset
    m_Radius = 2036  # offset
    m_SpotRadius = 2052  # offset

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

class CDynamicNavConnectionsVolume(CTriggerMultiple):
    m_bConnectionsEnabled = 2576  # offset
    m_flMaxConnectionDistance = 2588  # offset
    m_flTargetAreaSearchRadius = 2580  # offset
    m_flUpdateDistance = 2584  # offset
    m_iszConnectionTarget = 2536  # offset
    m_sTransitionType = 2568  # offset
    m_vecConnections = 2544  # offset

class CDynamicProp(CBreakableProp):
    m_OnAnimReachedEnd = 3312  # offset
    m_OnAnimReachedStart = 3272  # offset
    m_bCreateNavObstacle = 3144  # offset
    m_bCreateNonSolid = 3368  # offset
    m_bFiredStartEndOutput = 3366  # offset
    m_bForceNpcExclude = 3367  # offset
    m_bIsOverrideProp = 3369  # offset
    m_bNavObstacleUpdatesOverridden = 3145  # offset
    m_bRandomizeCycle = 3364  # offset
    m_bStartDisabled = 3365  # offset
    m_bUseAnimGraph = 3147  # offset
    m_bUseHitboxesForRenderBox = 3146  # offset
    m_glowColor = 3384  # offset
    m_iInitialGlowState = 3372  # offset
    m_iszIdleAnim = 3352  # offset
    m_nGlowRange = 3376  # offset
    m_nGlowRangeMin = 3380  # offset
    m_nGlowTeam = 3388  # offset
    m_nIdleAnimLoopMode = 3360  # offset
    m_pOutputAnimBegun = 3152  # offset
    m_pOutputAnimLoopCycleOver = 3232  # offset
    m_pOutputAnimOver = 3192  # offset

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

class CDynamicPropAlias_cable_dynamic(CDynamicProp):
    pass

class CDynamicPropAlias_dynamic_prop(CDynamicProp):
    pass

class CDynamicPropAlias_prop_dynamic_override(CDynamicProp):
    pass

class CEconEntity(CBaseFlex):
    m_AttributeManager = 2848  # offset
    m_OriginalOwnerXuidHigh = 3612  # offset
    m_OriginalOwnerXuidLow = 3608  # offset
    m_flFallbackWear = 3624  # offset
    m_hOldProvidee = 3632  # offset
    m_iOldOwnerClass = 3636  # offset
    m_nFallbackPaintKit = 3616  # offset
    m_nFallbackSeed = 3620  # offset
    m_nFallbackStatTrak = 3628  # offset

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

class CEconItemView:
    m_AttributeList = 112  # offset
    m_NetworkedDynamicAttributes = 232  # offset
    m_bInitialized = 104  # offset
    m_iAccountID = 88  # offset
    m_iEntityLevel = 64  # offset
    m_iEntityQuality = 60  # offset
    m_iInventoryPosition = 92  # offset
    m_iItemDefinitionIndex = 56  # offset
    m_iItemID = 72  # offset
    m_iItemIDHigh = 80  # offset
    m_iItemIDLow = 84  # offset
    m_szCustomName = 352  # offset
    m_szCustomNameOverride = 513  # offset

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

class CEconWearable(CEconEntity):
    m_bAlwaysAllow = 3644  # offset
    m_nForceSkin = 3640  # offset

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

class CEnableMotionFixup(CBaseEntity):
    pass

class CEntityBlocker(CBaseModelEntity):
    pass

class CEntityComponent:
    pass

class CEntityDissolve(CBaseModelEntity):
    m_flFadeInLength = 2036  # offset
    m_flFadeInStart = 2032  # offset
    m_flFadeOutLength = 2052  # offset
    m_flFadeOutModelLength = 2044  # offset
    m_flFadeOutModelStart = 2040  # offset
    m_flFadeOutStart = 2048  # offset
    m_flStartTime = 2056  # offset
    m_nDissolveType = 2060  # offset
    m_nMagnitude = 2076  # offset
    m_vDissolverOrigin = 2064  # offset

    __metadata__ =     [
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
            "name": "m_flStartTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
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

class CEntityFlame(CBaseEntity):
    m_bCheapEffect = 1268  # offset
    m_bUseHitboxes = 1276  # offset
    m_flDirectDamagePerSecond = 1296  # offset
    m_flHitboxFireScale = 1284  # offset
    m_flLifetime = 1288  # offset
    m_flSize = 1272  # offset
    m_hAttacker = 1292  # offset
    m_hEntAttached = 1264  # offset
    m_iCustomDamageType = 1300  # offset
    m_iNumHitboxFires = 1280  # offset

    __metadata__ =     [
        {
            "name": "m_hEntAttached",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_bCheapEffect",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

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

class CEnvBeam(CBeam):
    m_OnTouchedByEntity = 2320  # offset
    m_TouchType = 2288  # offset
    m_active = 2192  # offset
    m_boltWidth = 2228  # offset
    m_frameStart = 2256  # offset
    m_hFilter = 2304  # offset
    m_iFilterName = 2296  # offset
    m_iszDecal = 2312  # offset
    m_iszEndEntity = 2216  # offset
    m_iszSpriteName = 2248  # offset
    m_iszStartEntity = 2208  # offset
    m_life = 2224  # offset
    m_noiseAmplitude = 2232  # offset
    m_radius = 2284  # offset
    m_restrike = 2240  # offset
    m_speed = 2236  # offset
    m_spriteTexture = 2200  # offset
    m_vEndPointRelative = 2272  # offset
    m_vEndPointWorld = 2260  # offset

class CEnvBeverage(CBaseEntity):
    m_CanInDispenser = 1264  # offset
    m_nBeverageType = 1268  # offset

class CEnvCombinedLightProbeVolume(CBaseEntity):
    m_Entity_Color = 5480  # offset
    m_Entity_bCustomCubemapTexture = 5496  # offset
    m_Entity_bEnabled = 5681  # offset
    m_Entity_bMoveable = 5600  # offset
    m_Entity_bStartDisabled = 5616  # offset
    m_Entity_flBrightness = 5484  # offset
    m_Entity_flEdgeFadeDist = 5620  # offset
    m_Entity_hCubemapTexture = 5488  # offset
    m_Entity_hLightProbeDirectLightIndicesTexture = 5552  # offset
    m_Entity_hLightProbeDirectLightScalarsTexture = 5560  # offset
    m_Entity_hLightProbeDirectLightShadowsTexture = 5568  # offset
    m_Entity_hLightProbeTexture_AmbientCube = 5504  # offset
    m_Entity_hLightProbeTexture_SDF = 5512  # offset
    m_Entity_hLightProbeTexture_SH2_B = 5544  # offset
    m_Entity_hLightProbeTexture_SH2_DC = 5520  # offset
    m_Entity_hLightProbeTexture_SH2_G = 5536  # offset
    m_Entity_hLightProbeTexture_SH2_R = 5528  # offset
    m_Entity_nEnvCubeMapArrayIndex = 5608  # offset
    m_Entity_nHandshake = 5604  # offset
    m_Entity_nLightProbeAtlasX = 5648  # offset
    m_Entity_nLightProbeAtlasY = 5652  # offset
    m_Entity_nLightProbeAtlasZ = 5656  # offset
    m_Entity_nLightProbeSizeX = 5636  # offset
    m_Entity_nLightProbeSizeY = 5640  # offset
    m_Entity_nLightProbeSizeZ = 5644  # offset
    m_Entity_nPriority = 5612  # offset
    m_Entity_vBoxMaxs = 5588  # offset
    m_Entity_vBoxMins = 5576  # offset
    m_Entity_vEdgeFadeDists = 5624  # offset

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

class CEnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume(CEnvCombinedLightProbeVolume):
    pass

class CEnvCubemap(CBaseEntity):
    m_Entity_bCopyDiffuseFromDefaultCubemap = 1472  # offset
    m_Entity_bCustomCubemapTexture = 1400  # offset
    m_Entity_bDefaultEnvMap = 1469  # offset
    m_Entity_bDefaultSpecEnvMap = 1470  # offset
    m_Entity_bEnabled = 1488  # offset
    m_Entity_bIndoorCubeMap = 1471  # offset
    m_Entity_bMoveable = 1432  # offset
    m_Entity_bStartDisabled = 1468  # offset
    m_Entity_flDiffuseScale = 1464  # offset
    m_Entity_flEdgeFadeDist = 1448  # offset
    m_Entity_flInfluenceRadius = 1404  # offset
    m_Entity_hCubemapTexture = 1392  # offset
    m_Entity_nEnvCubeMapArrayIndex = 1440  # offset
    m_Entity_nHandshake = 1436  # offset
    m_Entity_nPriority = 1444  # offset
    m_Entity_vBoxProjectMaxs = 1420  # offset
    m_Entity_vBoxProjectMins = 1408  # offset
    m_Entity_vEdgeFadeDists = 1452  # offset

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

class CEnvCubemapBox(CEnvCubemap):
    pass

class CEnvCubemapFog(CBaseEntity):
    m_bActive = 1300  # offset
    m_bFirstTime = 1337  # offset
    m_bHasHeightFogEnd = 1336  # offset
    m_bHeightFogEnabled = 1276  # offset
    m_bStartDisabled = 1301  # offset
    m_flEndDistance = 1264  # offset
    m_flFogFalloffExponent = 1272  # offset
    m_flFogHeightEnd = 1284  # offset
    m_flFogHeightExponent = 1292  # offset
    m_flFogHeightStart = 1288  # offset
    m_flFogHeightWidth = 1280  # offset
    m_flFogMaxOpacity = 1304  # offset
    m_flLODBias = 1296  # offset
    m_flStartDistance = 1268  # offset
    m_hFogCubemapTexture = 1328  # offset
    m_hSkyMaterial = 1312  # offset
    m_iszSkyEntity = 1320  # offset
    m_nCubemapSourceType = 1308  # offset

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

class CEnvDecal(CBaseModelEntity):
    m_bProjectOnCharacters = 2057  # offset
    m_bProjectOnWater = 2058  # offset
    m_bProjectOnWorld = 2056  # offset
    m_flDepth = 2048  # offset
    m_flDepthSortBias = 2060  # offset
    m_flHeight = 2044  # offset
    m_flWidth = 2040  # offset
    m_hDecalMaterial = 2032  # offset
    m_nRenderOrder = 2052  # offset

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

class CEnvDetailController(CBaseEntity):
    m_flFadeEndDist = 1268  # offset
    m_flFadeStartDist = 1264  # offset

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

class CEnvEntityIgniter(CBaseEntity):
    m_flLifetime = 1264  # offset

class CEnvEntityMaker(CPointEntity):
    m_angPostSpawnDirection = 1308  # offset
    m_bPostSpawnUseAngles = 1328  # offset
    m_flPostSpawnDirectionVariance = 1320  # offset
    m_flPostSpawnSpeed = 1324  # offset
    m_hCurrentBlocker = 1292  # offset
    m_hCurrentInstance = 1288  # offset
    m_iszTemplate = 1336  # offset
    m_pOutputOnFailedSpawn = 1384  # offset
    m_pOutputOnSpawned = 1344  # offset
    m_vecBlockerOrigin = 1296  # offset
    m_vecEntityMaxs = 1276  # offset
    m_vecEntityMins = 1264  # offset

class CEnvExplosion(CModelPointEntity):
    m_bCreateDebris = 2060  # offset
    m_bSuppressParticleImpulse = 2088  # offset
    m_flDamageForce = 2048  # offset
    m_flInnerRadius = 2044  # offset
    m_flPlayerDamage = 2036  # offset
    m_hEntityIgnore = 2112  # offset
    m_hInflictor = 2052  # offset
    m_iClassIgnore = 2092  # offset
    m_iClassIgnore2 = 2096  # offset
    m_iCustomDamageType = 2056  # offset
    m_iMagnitude = 2032  # offset
    m_iRadiusOverride = 2040  # offset
    m_iszCustomEffectName = 2072  # offset
    m_iszCustomSoundName = 2080  # offset
    m_iszEntityIgnoreName = 2104  # offset

class CEnvFade(CLogicalEntity):
    m_Duration = 1268  # offset
    m_HoldDuration = 1272  # offset
    m_OnBeginFade = 1280  # offset
    m_fadeColor = 1264  # offset

    __metadata__ =     [
        {
            "name": "m_fadeColor",
            "type": "NetworkVarNames",
            "type_name": "Color"
        }
    ]

class CEnvGlobal(CLogicalEntity):
    m_counter = 1320  # offset
    m_globalstate = 1304  # offset
    m_initialstate = 1316  # offset
    m_outCounter = 1264  # offset
    m_triggermode = 1312  # offset

class CEnvHudHint(CPointEntity):
    m_iszMessage = 1264  # offset

class CEnvInstructorHint(CPointEntity):
    m_Color = 1328  # offset
    m_bAllowNoDrawTarget = 1368  # offset
    m_bAutoStart = 1369  # offset
    m_bForceCaption = 1345  # offset
    m_bLocalPlayerOnly = 1370  # offset
    m_bNoOffscreen = 1344  # offset
    m_bStatic = 1343  # offset
    m_bSuppressRest = 1352  # offset
    m_fIconOffset = 1332  # offset
    m_fRange = 1336  # offset
    m_iAlphaOption = 1341  # offset
    m_iDisplayLimit = 1292  # offset
    m_iInstanceType = 1348  # offset
    m_iPulseOption = 1340  # offset
    m_iShakeOption = 1342  # offset
    m_iTimeout = 1288  # offset
    m_iszActivatorCaption = 1320  # offset
    m_iszBinding = 1360  # offset
    m_iszCaption = 1312  # offset
    m_iszHintTargetEntity = 1280  # offset
    m_iszIcon_Offscreen = 1304  # offset
    m_iszIcon_Onscreen = 1296  # offset
    m_iszName = 1264  # offset
    m_iszReplace_Key = 1272  # offset

class CEnvInstructorVRHint(CPointEntity):
    m_flHeightOffset = 1324  # offset
    m_iAttachType = 1320  # offset
    m_iLayoutFileType = 1304  # offset
    m_iTimeout = 1280  # offset
    m_iszCaption = 1288  # offset
    m_iszCustomLayoutFile = 1312  # offset
    m_iszHintTargetEntity = 1272  # offset
    m_iszName = 1264  # offset
    m_iszStartSound = 1296  # offset

class CEnvLaser(CBeam):
    m_firePosition = 2216  # offset
    m_flStartFrame = 2228  # offset
    m_iszLaserTarget = 2192  # offset
    m_iszSpriteName = 2208  # offset
    m_pSprite = 2200  # offset

class CEnvLightProbeVolume(CBaseEntity):
    m_Entity_bEnabled = 5497  # offset
    m_Entity_bMoveable = 5448  # offset
    m_Entity_bStartDisabled = 5460  # offset
    m_Entity_hLightProbeDirectLightIndicesTexture = 5400  # offset
    m_Entity_hLightProbeDirectLightScalarsTexture = 5408  # offset
    m_Entity_hLightProbeDirectLightShadowsTexture = 5416  # offset
    m_Entity_hLightProbeTexture_AmbientCube = 5352  # offset
    m_Entity_hLightProbeTexture_SDF = 5360  # offset
    m_Entity_hLightProbeTexture_SH2_B = 5392  # offset
    m_Entity_hLightProbeTexture_SH2_DC = 5368  # offset
    m_Entity_hLightProbeTexture_SH2_G = 5384  # offset
    m_Entity_hLightProbeTexture_SH2_R = 5376  # offset
    m_Entity_nHandshake = 5452  # offset
    m_Entity_nLightProbeAtlasX = 5476  # offset
    m_Entity_nLightProbeAtlasY = 5480  # offset
    m_Entity_nLightProbeAtlasZ = 5484  # offset
    m_Entity_nLightProbeSizeX = 5464  # offset
    m_Entity_nLightProbeSizeY = 5468  # offset
    m_Entity_nLightProbeSizeZ = 5472  # offset
    m_Entity_nPriority = 5456  # offset
    m_Entity_vBoxMaxs = 5436  # offset
    m_Entity_vBoxMins = 5424  # offset

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

class CEnvMuzzleFlash(CPointEntity):
    m_flScale = 1264  # offset
    m_iszParentAttachment = 1272  # offset

class CEnvParticleGlow(CParticleSystem):
    m_ColorTint = 3444  # offset
    m_flAlphaScale = 3432  # offset
    m_flRadiusScale = 3436  # offset
    m_flSelfIllumScale = 3440  # offset
    m_hTextureOverride = 3448  # offset

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

class CEnvShake(CPointEntity):
    m_Amplitude = 1272  # offset
    m_Duration = 1280  # offset
    m_Frequency = 1276  # offset
    m_Radius = 1284  # offset
    m_currentAmp = 1296  # offset
    m_limitToEntity = 1264  # offset
    m_maxForce = 1300  # offset
    m_nextShake = 1292  # offset
    m_shakeCallback = 1320  # offset
    m_stopTime = 1288  # offset

class CEnvSky(CBaseModelEntity):
    m_bEnabled = 2084  # offset
    m_bStartDisabled = 2048  # offset
    m_flBrightnessScale = 2060  # offset
    m_flFogMaxEnd = 2080  # offset
    m_flFogMaxStart = 2076  # offset
    m_flFogMinEnd = 2072  # offset
    m_flFogMinStart = 2068  # offset
    m_hSkyMaterial = 2032  # offset
    m_hSkyMaterialLightingOnly = 2040  # offset
    m_nFogType = 2064  # offset
    m_vTintColor = 2049  # offset
    m_vTintColorLightingOnly = 2053  # offset

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

class CEnvSoundscape(CBaseEntity):
    m_OnPlay = 1264  # offset
    m_bDisabled = 1404  # offset
    m_bOverrideWithEvent = 1320  # offset
    m_flRadius = 1304  # offset
    m_hProxySoundscape = 1400  # offset
    m_positionNames = 1336  # offset
    m_soundEventHash = 1416  # offset
    m_soundEventName = 1312  # offset
    m_soundscapeEntityListId = 1328  # offset
    m_soundscapeIndex = 1324  # offset
    m_soundscapeName = 1408  # offset

class CEnvSoundscapeAlias_snd_soundscape(CEnvSoundscape):
    pass

class CEnvSoundscapeProxy(CEnvSoundscape):
    m_MainSoundscapeName = 1424  # offset

class CEnvSoundscapeProxyAlias_snd_soundscape_proxy(CEnvSoundscapeProxy):
    pass

class CEnvSoundscapeTriggerable(CEnvSoundscape):
    pass

class CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable(CEnvSoundscapeTriggerable):
    pass

class CEnvSpark(CPointEntity):
    m_OnSpark = 1280  # offset
    m_flDelay = 1264  # offset
    m_nMagnitude = 1268  # offset
    m_nTrailLength = 1272  # offset
    m_nType = 1276  # offset

class CEnvSplash(CPointEntity):
    m_flScale = 1264  # offset

class CEnvTilt(CPointEntity):
    m_Duration = 1264  # offset
    m_Radius = 1268  # offset
    m_TiltTime = 1272  # offset
    m_stopTime = 1276  # offset

class CEnvViewPunch(CPointEntity):
    m_angViewPunch = 1268  # offset
    m_flRadius = 1264  # offset

class CEnvVolumetricFogController(CBaseEntity):
    m_TintColor = 1268  # offset
    m_bActive = 1340  # offset
    m_bEnableIndirect = 1381  # offset
    m_bFirstTime = 1432  # offset
    m_bIsMaster = 1382  # offset
    m_bStartDisabled = 1380  # offset
    m_fFirstVolumeSliceThickness = 1300  # offset
    m_fNoiseSpeed = 1396  # offset
    m_fNoiseStrength = 1400  # offset
    m_fWindSpeed = 1416  # offset
    m_flAnisotropy = 1272  # offset
    m_flDefaultAnisotropy = 1368  # offset
    m_flDefaultDrawDistance = 1376  # offset
    m_flDefaultScattering = 1372  # offset
    m_flDrawDistance = 1280  # offset
    m_flFadeInEnd = 1288  # offset
    m_flFadeInStart = 1284  # offset
    m_flFadeSpeed = 1276  # offset
    m_flIndirectStrength = 1292  # offset
    m_flScattering = 1264  # offset
    m_flStartAnisoTime = 1344  # offset
    m_flStartAnisotropy = 1356  # offset
    m_flStartDrawDistance = 1364  # offset
    m_flStartDrawDistanceTime = 1352  # offset
    m_flStartScatterTime = 1348  # offset
    m_flStartScattering = 1360  # offset
    m_hFogIndirectTexture = 1384  # offset
    m_nForceRefreshCount = 1392  # offset
    m_nIndirectTextureDimX = 1304  # offset
    m_nIndirectTextureDimY = 1308  # offset
    m_nIndirectTextureDimZ = 1312  # offset
    m_nVolumeDepth = 1296  # offset
    m_vBoxMaxs = 1328  # offset
    m_vBoxMins = 1316  # offset
    m_vNoiseScale = 1404  # offset
    m_vWindDirection = 1420  # offset

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

class CEnvVolumetricFogVolume(CBaseEntity):
    m_TintColor = 1328  # offset
    m_bActive = 1264  # offset
    m_bIndirectUseLPVs = 1293  # offset
    m_bOverrideIndirectLightStrength = 1333  # offset
    m_bOverrideNoiseStrength = 1335  # offset
    m_bOverrideSunLightStrength = 1334  # offset
    m_bOverrideTintColor = 1332  # offset
    m_bStartDisabled = 1292  # offset
    m_fHeightFogEdgeWidth = 1312  # offset
    m_fIndirectLightStrength = 1316  # offset
    m_fNoiseStrength = 1324  # offset
    m_fSunLightStrength = 1320  # offset
    m_flFalloffExponent = 1304  # offset
    m_flHeightFogDepth = 1308  # offset
    m_flStrength = 1296  # offset
    m_nFalloffShape = 1300  # offset
    m_vBoxMaxs = 1280  # offset
    m_vBoxMins = 1268  # offset

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

class CEnvWind(CBaseEntity):
    m_EnvWindShared = 1264  # offset

    __metadata__ =     [
        {
            "name": "m_EnvWindShared",
            "type": "NetworkVarNames",
            "type_name": "CEnvWindShared"
        }
    ]

class CEnvWindController(CBaseEntity):
    m_EnvWindShared = 1264  # offset
    m_bFirstTime = 1633  # offset
    m_bIsMaster = 1632  # offset
    m_fDirectionVariation = 1600  # offset
    m_fSpeedVariation = 1604  # offset
    m_fTurbulence = 1608  # offset
    m_fVolumeHalfExtentXY = 1612  # offset
    m_fVolumeHalfExtentZ = 1616  # offset
    m_nClipmapLevels = 1628  # offset
    m_nVolumeResolutionXY = 1620  # offset
    m_nVolumeResolutionZ = 1624  # offset

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

class CEnvWindShared:
    m_OnGustEnd = 104  # offset
    m_OnGustStart = 64  # offset
    m_flGustDuration = 36  # offset
    m_flInitialWindSpeed = 44  # offset
    m_flMaxGustDelay = 32  # offset
    m_flMinGustDelay = 28  # offset
    m_flStartTime = 8  # offset
    m_hEntOwner = 144  # offset
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

class CEnvWindVolume(CBaseEntity):
    m_bActive = 1264  # offset
    m_bStartDisabled = 1292  # offset
    m_fWindDirectionVariationMultiplier = 1312  # offset
    m_fWindSpeedMultiplier = 1300  # offset
    m_fWindSpeedVariationMultiplier = 1308  # offset
    m_fWindTurbulenceMultiplier = 1304  # offset
    m_nShape = 1296  # offset
    m_vBoxMaxs = 1280  # offset
    m_vBoxMins = 1268  # offset

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

class CFilterAttributeInt(CBaseFilter):
    m_sAttributeName = 1352  # offset

class CFilterClass(CBaseFilter):
    m_iFilterClass = 1352  # offset

class CFilterContext(CBaseFilter):
    m_iFilterContext = 1352  # offset

class CFilterEnemy(CBaseFilter):
    m_flOuterRadius = 1364  # offset
    m_flRadius = 1360  # offset
    m_iszEnemyName = 1352  # offset
    m_iszPlayerName = 1376  # offset
    m_nMaxSquadmatesPerEnemy = 1368  # offset

class CFilterLOS(CBaseFilter):
    pass

class CFilterMassGreater(CBaseFilter):
    m_fFilterMass = 1352  # offset

class CFilterModel(CBaseFilter):
    m_iFilterModel = 1352  # offset

class CFilterMultiple(CBaseFilter):
    m_hFilter = 1440  # offset
    m_iFilterName = 1360  # offset
    m_nFilterType = 1352  # offset

class CFilterMultipleAPI:
    pass

class CFilterName(CBaseFilter):
    m_iFilterName = 1352  # offset

class CFilterProximity(CBaseFilter):
    m_flRadius = 1352  # offset

class CFilterTeam(CBaseFilter):
    m_iFilterTeam = 1352  # offset

class CFireCrackerBlast(CInferno):
    pass

class CFish(CBaseAnimGraph):
    m_angle = 2708  # offset
    m_angleChange = 2712  # offset
    m_avoidRange = 2772  # offset
    m_calmSpeed = 2764  # offset
    m_desiredSpeed = 2760  # offset
    m_disperseTimer = 2880  # offset
    m_forward = 2716  # offset
    m_goTimer = 2808  # offset
    m_id = 2692  # offset
    m_moveTimer = 2832  # offset
    m_panicSpeed = 2768  # offset
    m_panicTimer = 2856  # offset
    m_perp = 2728  # offset
    m_pool = 2688  # offset
    m_poolOrigin = 2740  # offset
    m_proximityTimer = 2904  # offset
    m_speed = 2756  # offset
    m_turnClockwise = 2800  # offset
    m_turnTimer = 2776  # offset
    m_visible = 2928  # offset
    m_waterLevel = 2752  # offset
    m_x = 2696  # offset
    m_y = 2700  # offset
    m_z = 2704  # offset

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
        }
    ]

class CFishPool(CBaseEntity):
    m_fishCount = 1280  # offset
    m_fishes = 1304  # offset
    m_isDormant = 1296  # offset
    m_maxRange = 1284  # offset
    m_swimDepth = 1288  # offset
    m_visTimer = 1328  # offset
    m_waterLevel = 1292  # offset

class CFlashbang(CBaseCSGrenade):
    pass

class CFlashbangProjectile(CBaseCSGrenadeProjectile):
    m_flTimeToDetonate = 3112  # offset
    m_numOpponentsHit = 3116  # offset
    m_numTeammatesHit = 3117  # offset

class CFogController(CBaseEntity):
    m_bUseAngles = 1368  # offset
    m_fog = 1264  # offset
    m_iChangedVariables = 1372  # offset

    __metadata__ =     [
        {
            "name": "m_fog",
            "type": "NetworkVarNames",
            "type_name": "fogparams_t"
        }
    ]

class CFogTrigger(CBaseTrigger):
    m_fog = 2496  # offset

class CFogVolume(CServerOnlyModelEntity):
    m_bDisabled = 2064  # offset
    m_bInFogVolumesList = 2065  # offset
    m_colorCorrectionName = 2048  # offset
    m_fogName = 2032  # offset
    m_postProcessName = 2040  # offset

class CFootstepControl(CBaseTrigger):
    m_destination = 2504  # offset
    m_source = 2496  # offset

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

class CFuncBrush(CBaseModelEntity):
    m_bInvertExclusion = 2056  # offset
    m_bScriptedMovement = 2057  # offset
    m_bSolidBsp = 2040  # offset
    m_iDisabled = 2036  # offset
    m_iSolidity = 2032  # offset
    m_iszExcludedClass = 2048  # offset

class CFuncConveyor(CBaseModelEntity):
    m_angMoveEntitySpace = 2044  # offset
    m_flTargetSpeed = 2068  # offset
    m_flTransitionDurationSeconds = 2040  # offset
    m_flTransitionStartSpeed = 2080  # offset
    m_hConveyorModels = 2088  # offset
    m_nTransitionDurationTicks = 2076  # offset
    m_nTransitionStartTick = 2072  # offset
    m_szConveyorModels = 2032  # offset
    m_vecMoveDirEntitySpace = 2056  # offset

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

class CFuncElectrifiedVolume(CFuncBrush):
    m_EffectInterpenetrateName = 2072  # offset
    m_EffectName = 2064  # offset
    m_EffectZapName = 2080  # offset
    m_iszEffectSource = 2088  # offset

    __metadata__ =     [
        {
            "name": "m_EffectName",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        }
    ]

class CFuncIllusionary(CBaseModelEntity):
    pass

class CFuncInteractionLayerClip(CBaseModelEntity):
    m_bDisabled = 2032  # offset
    m_iszInteractsAs = 2040  # offset
    m_iszInteractsWith = 2048  # offset

class CFuncLadder(CBaseModelEntity):
    m_Dismounts = 2048  # offset
    m_OnPlayerGotOffLadder = 2168  # offset
    m_OnPlayerGotOnLadder = 2128  # offset
    m_bDisabled = 2112  # offset
    m_bFakeLadder = 2113  # offset
    m_bHasSlack = 2114  # offset
    m_flAutoRideSpeed = 2108  # offset
    m_surfacePropName = 2120  # offset
    m_vecLadderDir = 2032  # offset
    m_vecLocalTop = 2072  # offset
    m_vecPlayerMountPositionBottom = 2096  # offset
    m_vecPlayerMountPositionTop = 2084  # offset

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

class CFuncLadderAlias_func_useableladder(CFuncLadder):
    pass

class CFuncMonitor(CFuncBrush):
    m_bDraw3DSkybox = 2093  # offset
    m_bEnabled = 2092  # offset
    m_bRenderShadows = 2076  # offset
    m_bStartEnabled = 2094  # offset
    m_bUseUniqueColorTarget = 2077  # offset
    m_brushModelName = 2080  # offset
    m_hTargetCamera = 2088  # offset
    m_nResolutionEnum = 2072  # offset
    m_targetCamera = 2064  # offset

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

class CFuncMoveLinear(CBaseToggle):
    m_OnFullyClosed = 2272  # offset
    m_OnFullyOpen = 2232  # offset
    m_angMoveEntitySpace = 2164  # offset
    m_authoredPosition = 2160  # offset
    m_bAllowMovableNavMeshDockingOnEntireEntity = 2313  # offset
    m_bCreateMovableNavMesh = 2312  # offset
    m_bCreateNavObstacle = 2314  # offset
    m_currentSound = 2208  # offset
    m_flBlockDamage = 2216  # offset
    m_flStartPosition = 2220  # offset
    m_soundStart = 2192  # offset
    m_soundStop = 2200  # offset
    m_vecMoveDirParentSpace = 2176  # offset

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

class CFuncMoveLinearAlias_momentary_door(CFuncMoveLinear):
    pass

class CFuncMover(CBaseModelEntity):
    m_OnLerpToPositionComplete = 2384  # offset
    m_OnMovementEnd = 2224  # offset
    m_OnNodePassed = 2296  # offset
    m_OnStart = 2480  # offset
    m_OnStartForward = 2520  # offset
    m_OnStartReverse = 2560  # offset
    m_OnStop = 2600  # offset
    m_OnStopped = 2640  # offset
    m_bAllowMovableNavMeshDockingOnEntireEntity = 2289  # offset
    m_bCreateMovableNavMesh = 2288  # offset
    m_bIsMoving = 2105  # offset
    m_bIsPaused = 2424  # offset
    m_bIsReversing = 2068  # offset
    m_bIsVerboseLogging = 2436  # offset
    m_bNextNodeReturnsCurrent = 2680  # offset
    m_bStartAtClosestPoint = 2264  # offset
    m_bStartAtEnd = 2265  # offset
    m_bStartedMoving = 2681  # offset
    m_eFollowEntityDirection = 2712  # offset
    m_eMoveType = 2064  # offset
    m_eOrientationUpdate = 2268  # offset
    m_eSolidType = 2104  # offset
    m_eTransitionedToPathNodeAction = 2428  # offset
    m_flCurFollowEntityT = 2452  # offset
    m_flCurFollowSpeed = 2456  # offset
    m_flDistanceToReachMaxSpeed = 2112  # offset
    m_flDistanceToReachZeroSpeed = 2120  # offset
    m_flDurationBlendToNewOrientationRan = 2280  # offset
    m_flFollowDistance = 2444  # offset
    m_flFollowMinimumSpeed = 2448  # offset
    m_flLerpToPositionDeltaT = 2380  # offset
    m_flLerpToPositionT = 2376  # offset
    m_flPathLocation = 2088  # offset
    m_flPathLocationToBeginStop = 2136  # offset
    m_flStartSpeed = 2084  # offset
    m_flT = 2092  # offset
    m_flTimeMovementStart = 2124  # offset
    m_flTimeMovementStop = 2128  # offset
    m_flTimeStartOrientationChange = 2272  # offset
    m_flTimeToBlendToNewOrientation = 2276  # offset
    m_flTimeToReachMaxSpeed = 2108  # offset
    m_flTimeToReachZeroSpeed = 2116  # offset
    m_flTimeToTraverseToNextNode = 2348  # offset
    m_hFollowEntity = 2440  # offset
    m_hOrientationFaceEntity = 2472  # offset
    m_hOrientationMatchEntity = 2344  # offset
    m_hPathMover = 2040  # offset
    m_hPrevPathMover = 2044  # offset
    m_hStopAtNode = 2132  # offset
    m_iszArriveAtDestinationSound = 2192  # offset
    m_iszLoopForwardSound = 2152  # offset
    m_iszLoopReverseSound = 2176  # offset
    m_iszOrientationMatchEntityName = 2336  # offset
    m_iszPathName = 2032  # offset
    m_iszPathNodeEnd = 2056  # offset
    m_iszPathNodeStart = 2048  # offset
    m_iszStartForwardSound = 2144  # offset
    m_iszStartReverseSound = 2168  # offset
    m_iszStopForwardSound = 2160  # offset
    m_iszStopReverseSound = 2184  # offset
    m_nCurrentNodeIndex = 2096  # offset
    m_nDelayedTeleportToNode = 2432  # offset
    m_nOriginalOrientationIndex = 2284  # offset
    m_nPreviousNodeIndex = 2100  # offset
    m_strOrientationFaceEntityName = 2464  # offset
    m_vLerpToNewPosEndInPathEntitySpace = 2364  # offset
    m_vLerpToNewPosStartInPathEntitySpace = 2352  # offset
    m_vTarget = 2072  # offset

class CFuncMoverAPI:
    pass

class CFuncNavBlocker(CBaseModelEntity):
    m_bDisabled = 2040  # offset
    m_nBlockedTeamNumber = 2044  # offset

class CFuncNavObstruction(CBaseModelEntity):
    m_bDisabled = 2056  # offset
    m_bUseAsyncObstacleUpdate = 2057  # offset

class CFuncPlat(CBasePlatTrain):
    m_sNoise = 2200  # offset

class CFuncPlatRot(CFuncPlat):
    m_end = 2208  # offset
    m_start = 2220  # offset

class CFuncPropRespawnZone(CBaseEntity):
    pass

class CFuncRotating(CBaseModelEntity):
    m_NoiseRunning = 2192  # offset
    m_OnReachedStart = 2112  # offset
    m_OnStarted = 2072  # offset
    m_OnStopped = 2032  # offset
    m_angStart = 2236  # offset
    m_bAccelDecel = 2201  # offset
    m_bReversed = 2200  # offset
    m_bStopAtStartPos = 2248  # offset
    m_flAttenuation = 2168  # offset
    m_flBlockDamage = 2184  # offset
    m_flFanFriction = 2164  # offset
    m_flMaxSpeed = 2180  # offset
    m_flTargetSpeed = 2176  # offset
    m_flVolume = 2172  # offset
    m_localRotationVector = 2152  # offset
    m_prevLocalAngles = 2224  # offset
    m_vecClientAngles = 2264  # offset
    m_vecClientOrigin = 2252  # offset

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

class CFuncRotator(CBaseModelEntity):
    m_OnOscillate = 2224  # offset
    m_OnOscillateEndArrive = 2344  # offset
    m_OnOscillateEndDepart = 2384  # offset
    m_OnOscillateStartArrive = 2264  # offset
    m_OnOscillateStartDepart = 2304  # offset
    m_OnRotationCompleted = 2184  # offset
    m_OnRotationStarted = 2144  # offset
    m_bHasTargetOverride = 2440  # offset
    m_bIsReversing = 2037  # offset
    m_bIsRotating = 2036  # offset
    m_bOscillateDepart = 2424  # offset
    m_bRecordHistory = 2504  # offset
    m_bReturningToPreviousOrientation = 2536  # offset
    m_ePrevRotateType = 2436  # offset
    m_eRotateType = 2432  # offset
    m_eSpaceOverride = 2464  # offset
    m_flDistanceAlongArcTraveled = 2048  # offset
    m_flTimeRotationStart = 2056  # offset
    m_flTimeToReachMaxSpeed = 2040  # offset
    m_flTimeToReachZeroSpeed = 2044  # offset
    m_flTimeToWaitOscillate = 2052  # offset
    m_hRotatorTarget = 2032  # offset
    m_nOscillateCount = 2428  # offset
    m_qAngularVelocity = 2468  # offset
    m_qLSInit = 2112  # offset
    m_qLSOrientation = 2128  # offset
    m_qLSPrevChange = 2064  # offset
    m_qOrientationOverride = 2448  # offset
    m_qWSInit = 2096  # offset
    m_qWSPrev = 2080  # offset
    m_strRotatorTarget = 2496  # offset
    m_vLookAtForcedUp = 2480  # offset
    m_vecRotatorHistory = 2512  # offset
    m_vecRotatorQueue = 2544  # offset
    m_vecRotatorQueueHistory = 2568  # offset

class CFuncShatterglass(CBaseModelEntity):
    m_OnBroken = 2296  # offset
    m_PanelSize = 2152  # offset
    m_bBreakShardless = 2181  # offset
    m_bBreakSilent = 2180  # offset
    m_bBroken = 2182  # offset
    m_bGlassInFrame = 2184  # offset
    m_bGlassNavIgnore = 2183  # offset
    m_bStartBroken = 2185  # offset
    m_flGlassThickness = 2172  # offset
    m_flInitAtTime = 2168  # offset
    m_flLastCleanupTime = 2164  # offset
    m_flLastShatterSoundEmitTime = 2160  # offset
    m_flSpawnInvulnerability = 2176  # offset
    m_hMaterialDamageBase = 2344  # offset
    m_iInitialDamageType = 2186  # offset
    m_iSurfaceType = 2336  # offset
    m_matPanelTransform = 2032  # offset
    m_matPanelTransformWsTemp = 2080  # offset
    m_szDamagePositioningEntityName01 = 2192  # offset
    m_szDamagePositioningEntityName02 = 2200  # offset
    m_szDamagePositioningEntityName03 = 2208  # offset
    m_szDamagePositioningEntityName04 = 2216  # offset
    m_vExtraDamagePositions = 2248  # offset
    m_vInitialDamagePositions = 2224  # offset
    m_vInitialPanelVertices = 2272  # offset
    m_vecShatterGlassShards = 2128  # offset

class CFuncTankTrain(CFuncTrackTrain):
    m_OnDeath = 2376  # offset

class CFuncTimescale(CBaseEntity):
    m_flAcceleration = 1268  # offset
    m_flBlendDeltaMultiplier = 1276  # offset
    m_flDesiredTimescale = 1264  # offset
    m_flMinBlendRate = 1272  # offset
    m_isStarted = 1280  # offset

class CFuncTrackAuto(CFuncTrackChange):
    pass

class CFuncTrackChange(CFuncPlatRot):
    m_code = 2280  # offset
    m_targetState = 2284  # offset
    m_trackBottom = 2240  # offset
    m_trackBottomName = 2264  # offset
    m_trackTop = 2232  # offset
    m_trackTopName = 2256  # offset
    m_train = 2248  # offset
    m_trainName = 2272  # offset
    m_use = 2288  # offset

class CFuncTrackTrain(CBaseModelEntity):
    m_OnArrivedAtDestinationNode = 2304  # offset
    m_OnNext = 2264  # offset
    m_OnStart = 2224  # offset
    m_angPrev = 2052  # offset
    m_bAccelToSpeed = 2364  # offset
    m_bManualSpeedChanges = 2344  # offset
    m_controlMaxs = 2076  # offset
    m_controlMins = 2064  # offset
    m_dir = 2128  # offset
    m_eOrientationType = 2196  # offset
    m_eVelocityType = 2200  # offset
    m_flAccelSpeed = 2356  # offset
    m_flBank = 2108  # offset
    m_flBlockDamage = 2116  # offset
    m_flDecelSpeed = 2360  # offset
    m_flDesiredSpeed = 2348  # offset
    m_flMoveSoundMaxDuration = 2180  # offset
    m_flMoveSoundMaxPitch = 2192  # offset
    m_flMoveSoundMinDuration = 2176  # offset
    m_flMoveSoundMinPitch = 2188  # offset
    m_flNextMPSoundTime = 2368  # offset
    m_flNextMoveSoundTime = 2184  # offset
    m_flSpeedChangeTime = 2352  # offset
    m_flVolume = 2104  # offset
    m_height = 2120  # offset
    m_iszSoundMove = 2136  # offset
    m_iszSoundMovePing = 2144  # offset
    m_iszSoundStart = 2152  # offset
    m_iszSoundStop = 2160  # offset
    m_lastBlockPos = 2088  # offset
    m_lastBlockTick = 2100  # offset
    m_length = 2036  # offset
    m_maxSpeed = 2124  # offset
    m_oldSpeed = 2112  # offset
    m_ppath = 2032  # offset
    m_strPathTarget = 2168  # offset
    m_vPosPrev = 2040  # offset

class CFuncTrain(CBasePlatTrain):
    m_activated = 2204  # offset
    m_flBlockDamage = 2212  # offset
    m_flNextBlockTime = 2216  # offset
    m_hCurrentTarget = 2200  # offset
    m_hEnemy = 2208  # offset
    m_iszLastTarget = 2224  # offset

class CFuncTrainControls(CBaseModelEntity):
    pass

class CFuncVPhysicsClip(CBaseModelEntity):
    m_bDisabled = 2032  # offset

class CFuncVehicleClip(CBaseModelEntity):
    pass

class CFuncWall(CBaseModelEntity):
    m_nState = 2032  # offset

class CFuncWallToggle(CFuncWall):
    pass

class CFuncWater(CBaseModelEntity):
    m_BuoyancyHelper = 2032  # offset

class CGameEnd(CRulePointEntity):
    pass

class CGameGibManager(CBaseEntity):
    m_bAllowNewGibs = 1288  # offset
    m_iCurrentMaxPieces = 1292  # offset
    m_iLastFrame = 1300  # offset
    m_iMaxPieces = 1296  # offset

class CGameMoney(CRulePointEntity):
    m_OnMoneySpent = 2048  # offset
    m_OnMoneySpentFail = 2088  # offset
    m_nMoney = 2128  # offset
    m_strAwardText = 2136  # offset

class CGamePlayerEquip(CRulePointEntity):
    pass

class CGamePlayerZone(CRuleBrushEntity):
    m_OnPlayerInZone = 2040  # offset
    m_OnPlayerOutZone = 2080  # offset
    m_PlayersInCount = 2120  # offset
    m_PlayersOutCount = 2160  # offset

class CGameRules:
    __m_pChainEntity = 8  # offset
    m_bGamePaused = 188  # offset
    m_nPauseStartTick = 184  # offset
    m_nQuestPhase = 176  # offset
    m_nTotalPausedTicks = 180  # offset
    m_szQuestName = 48  # offset

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

class CGameRulesProxy(CBaseEntity):
    pass

class CGameSceneNode:
    m_angAbsRotation = 220  # offset
    m_angRotation = 192  # offset
    m_bBoneMergeFlex = 0  # offset
    m_bDebugAbsOriginChanges = 238  # offset
    m_bDirtyBoneMergeBoneToRoot = 0  # offset
    m_bDirtyBoneMergeInfo = 0  # offset
    m_bDirtyHierarchy = 0  # offset
    m_bDormant = 239  # offset
    m_bForceParentToBeNetworked = 240  # offset
    m_bNetworkedAnglesChanged = 0  # offset
    m_bNetworkedPositionChanged = 0  # offset
    m_bNetworkedScaleChanged = 0  # offset
    m_bWillBeCallingPostDataUpdate = 0  # offset
    m_flAbsScale = 232  # offset
    m_flClientLocalScale = 320  # offset
    m_flScale = 204  # offset
    m_flZOffset = 316  # offset
    m_hParent = 120  # offset
    m_hierarchyAttachName = 312  # offset
    m_nDoNotSetAnimTimeInInvalidatePhysicsCount = 245  # offset
    m_nHierarchicalDepth = 243  # offset
    m_nHierarchyType = 244  # offset
    m_nLatchAbsOrigin = 0  # offset
    m_nParentAttachmentOrBone = 236  # offset
    m_name = 248  # offset
    m_nodeToWorld = 16  # offset
    m_pChild = 64  # offset
    m_pNextSibling = 72  # offset
    m_pOwner = 48  # offset
    m_pParent = 56  # offset
    m_vRenderOrigin = 324  # offset
    m_vecAbsOrigin = 208  # offset
    m_vecOrigin = 136  # offset

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

class CGameText(CRulePointEntity):
    m_iszMessage = 2048  # offset
    m_textParms = 2056  # offset

class CGenericConstraint(CPhysConstraint):
    m_NotifyForceReachedX = 1560  # offset
    m_NotifyForceReachedY = 1600  # offset
    m_NotifyForceReachedZ = 1640  # offset
    m_bAxisNotifiedX = 1504  # offset
    m_bAxisNotifiedY = 1505  # offset
    m_bAxisNotifiedZ = 1506  # offset
    m_flAngularDampingRatioX = 1532  # offset
    m_flAngularDampingRatioY = 1536  # offset
    m_flAngularDampingRatioZ = 1540  # offset
    m_flAngularFrequencyX = 1520  # offset
    m_flAngularFrequencyY = 1524  # offset
    m_flAngularFrequencyZ = 1528  # offset
    m_flBreakAfterTimeStartTimeX = 1444  # offset
    m_flBreakAfterTimeStartTimeY = 1448  # offset
    m_flBreakAfterTimeStartTimeZ = 1452  # offset
    m_flBreakAfterTimeThresholdX = 1456  # offset
    m_flBreakAfterTimeThresholdY = 1460  # offset
    m_flBreakAfterTimeThresholdZ = 1464  # offset
    m_flBreakAfterTimeX = 1432  # offset
    m_flBreakAfterTimeY = 1436  # offset
    m_flBreakAfterTimeZ = 1440  # offset
    m_flLinearDampingRatioX = 1408  # offset
    m_flLinearDampingRatioY = 1412  # offset
    m_flLinearDampingRatioZ = 1416  # offset
    m_flLinearFrequencyX = 1396  # offset
    m_flLinearFrequencyY = 1400  # offset
    m_flLinearFrequencyZ = 1404  # offset
    m_flMaxAngularImpulseX = 1544  # offset
    m_flMaxAngularImpulseY = 1548  # offset
    m_flMaxAngularImpulseZ = 1552  # offset
    m_flMaxLinearImpulseX = 1420  # offset
    m_flMaxLinearImpulseY = 1424  # offset
    m_flMaxLinearImpulseZ = 1428  # offset
    m_flNotifyForceLastTimeX = 1492  # offset
    m_flNotifyForceLastTimeY = 1496  # offset
    m_flNotifyForceLastTimeZ = 1500  # offset
    m_flNotifyForceMinTimeX = 1480  # offset
    m_flNotifyForceMinTimeY = 1484  # offset
    m_flNotifyForceMinTimeZ = 1488  # offset
    m_flNotifyForceX = 1468  # offset
    m_flNotifyForceY = 1472  # offset
    m_flNotifyForceZ = 1476  # offset
    m_nAngularMotionX = 1508  # offset
    m_nAngularMotionY = 1512  # offset
    m_nAngularMotionZ = 1516  # offset
    m_nLinearMotionX = 1384  # offset
    m_nLinearMotionY = 1388  # offset
    m_nLinearMotionZ = 1392  # offset

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

class CGradientFog(CBaseEntity):
    m_bGradientFogNeedsTextures = 1322  # offset
    m_bHeightFogEnabled = 1280  # offset
    m_bIsEnabled = 1321  # offset
    m_bStartDisabled = 1320  # offset
    m_flFadeTime = 1316  # offset
    m_flFarZ = 1292  # offset
    m_flFogEndDistance = 1276  # offset
    m_flFogEndHeight = 1288  # offset
    m_flFogFalloffExponent = 1300  # offset
    m_flFogMaxOpacity = 1296  # offset
    m_flFogStartDistance = 1272  # offset
    m_flFogStartHeight = 1284  # offset
    m_flFogStrength = 1312  # offset
    m_flFogVerticalExponent = 1304  # offset
    m_fogColor = 1308  # offset
    m_hGradientFogTexture = 1264  # offset

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

class CGunTarget(CBaseToggle):
    m_OnDeath = 2168  # offset
    m_hTargetEnt = 2164  # offset
    m_on = 2160  # offset

class CHEGrenade(CBaseCSGrenade):
    pass

class CHEGrenadeProjectile(CBaseCSGrenadeProjectile):
    pass

class CHandleDummy(CBaseEntity):
    pass

class CHandleTest(CBaseEntity):
    m_Handle = 1264  # offset
    m_bSendHandle = 1268  # offset

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

class CHitboxComponent(CEntityComponent):
    m_flBoundsExpandRadius = 32  # offset

class CHostage(CHostageExpresserShim):
    m_OnDroppedNotRescued = 3136  # offset
    m_OnFirstPickedUp = 3096  # offset
    m_OnHostageBeginGrab = 3056  # offset
    m_OnRescued = 3176  # offset
    m_accel = 3316  # offset
    m_bHandsHaveBeenCut = 11797  # offset
    m_bRemove = 3252  # offset
    m_entitySpottedState = 3216  # offset
    m_fLastGrabTime = 11804  # offset
    m_flDropStartTime = 11840  # offset
    m_flGrabSuccessTime = 11836  # offset
    m_flRescueStartTime = 11832  # offset
    m_hHostageGrabber = 11800  # offset
    m_hasBeenUsed = 3312  # offset
    m_inhibitDoorTimer = 11592  # offset
    m_inhibitObstacleAvoidanceTimer = 11736  # offset
    m_isAdjusted = 11796  # offset
    m_isCrouching = 3329  # offset
    m_isRescued = 3268  # offset
    m_isRunning = 3328  # offset
    m_isWaitingForLeader = 3360  # offset
    m_jumpTimer = 3336  # offset
    m_jumpedThisFrame = 3269  # offset
    m_lastLeader = 3280  # offset
    m_leader = 3276  # offset
    m_nApproachRewardPayouts = 11844  # offset
    m_nHostageSpawnRandomFactor = 3248  # offset
    m_nHostageState = 3272  # offset
    m_nPickupEventCount = 11848  # offset
    m_nSpotRules = 3240  # offset
    m_repathTimer = 11568  # offset
    m_reuseTimer = 3288  # offset
    m_uiHostageSpawnExclusionGroupMask = 3244  # offset
    m_vecGrabbedPos = 11820  # offset
    m_vecHostageResetPosition = 11908  # offset
    m_vecPositionWhenStartedDroppingToGround = 11808  # offset
    m_vecSpawnGroundPos = 11852  # offset
    m_vel = 3256  # offset
    m_wiggleTimer = 11768  # offset

    __metadata__ =     [
        {
            "name": "m_entitySpottedState",
            "type": "NetworkVarNames",
            "type_name": "EntitySpottedState_t"
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

class CHostageAlias_info_hostage_spawn(CHostage):
    pass

class CHostageCarriableProp(CBaseAnimGraph):
    pass

class CHostageExpresserShim(CBaseCombatCharacter):
    m_pExpresser = 3032  # offset

class CHostageRescueZone(CHostageRescueZoneShim):
    pass

class CHostageRescueZoneShim(CBaseTrigger):
    pass

class CIncendiaryGrenade(CMolotovGrenade):
    pass

class CInferno(CBaseModelEntity):
    m_BookkeepingTimer = 5088  # offset
    m_BurnNormal = 3632  # offset
    m_InitialSplashVelocity = 5020  # offset
    m_NextSpreadTimer = 5112  # offset
    m_activeTimer = 5056  # offset
    m_bFireIsBurning = 3568  # offset
    m_bInPostEffectTime = 4416  # offset
    m_bWasCreatedInSmoke = 4417  # offset
    m_damageRampTimer = 4984  # offset
    m_damageTimer = 4960  # offset
    m_extent = 4936  # offset
    m_fireCount = 4400  # offset
    m_fireParentPositions = 2800  # offset
    m_firePositions = 2032  # offset
    m_fireSpawnOffset = 5072  # offset
    m_nFireEffectTickBegin = 4408  # offset
    m_nFireLifetime = 4412  # offset
    m_nInfernoType = 4404  # offset
    m_nMaxFlames = 5076  # offset
    m_nSourceItemDefIndex = 5136  # offset
    m_nSpreadCount = 5080  # offset
    m_splashVelocity = 5008  # offset
    m_startPos = 5032  # offset
    m_vecOriginalSpawnLocation = 5044  # offset

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
            "name": "m_nFireEffectTickBegin",
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
        }
    ]

class CInfoData(CServerOnlyEntity):
    pass

class CInfoDeathmatchSpawn(SpawnPoint):
    pass

class CInfoDynamicShadowHint(CPointEntity):
    m_bDisabled = 1264  # offset
    m_flRange = 1268  # offset
    m_hLight = 1280  # offset
    m_nImportance = 1272  # offset
    m_nLightChoice = 1276  # offset

class CInfoDynamicShadowHintBox(CInfoDynamicShadowHint):
    m_vBoxMaxs = 1300  # offset
    m_vBoxMins = 1288  # offset

class CInfoFan(CPointEntity):
    m_FanForceCurveString = 1344  # offset
    m_fFanForceMaxRadius = 1328  # offset
    m_fFanForceMinRadius = 1332  # offset
    m_flCurveDistRange = 1336  # offset

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

class CInfoGameEventProxy(CPointEntity):
    m_flRange = 1272  # offset
    m_iszEventName = 1264  # offset

class CInfoInstructorHintBombTargetA(CPointEntity):
    pass

class CInfoInstructorHintBombTargetB(CPointEntity):
    pass

class CInfoInstructorHintHostageRescueZone(CPointEntity):
    pass

class CInfoInstructorHintTarget(CPointEntity):
    pass

class CInfoLadderDismount(CBaseEntity):
    pass

class CInfoLandmark(CPointEntity):
    pass

class CInfoOffscreenPanoramaTexture(CPointEntity):
    m_AdditionalTargetEntities = 1360  # offset
    m_RenderAttrName = 1288  # offset
    m_TargetEntities = 1296  # offset
    m_bDisabled = 1264  # offset
    m_nResolutionX = 1268  # offset
    m_nResolutionY = 1272  # offset
    m_nTargetChangeCount = 1320  # offset
    m_szLayoutFileName = 1280  # offset
    m_szTargetsName = 1352  # offset
    m_vecCSSClasses = 1328  # offset

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
            "type_name": "CHandle<CBaseModelEntity>"
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

class CInfoParticleTarget(CPointEntity):
    pass

class CInfoPlayerCounterterrorist(SpawnPoint):
    pass

class CInfoPlayerStart(CPointEntity):
    m_bDisabled = 1264  # offset
    m_bIsMaster = 1265  # offset
    m_pPawnSubclass = 1272  # offset

class CInfoPlayerTerrorist(SpawnPoint):
    pass

class CInfoSpawnGroupLandmark(CPointEntity):
    pass

class CInfoSpawnGroupLoadUnload(CLogicalEntity):
    m_OnSpawnGroupLoadFinished = 1304  # offset
    m_OnSpawnGroupLoadStarted = 1264  # offset
    m_OnSpawnGroupUnloadFinished = 1384  # offset
    m_OnSpawnGroupUnloadStarted = 1344  # offset
    m_bAutoActivate = 1460  # offset
    m_bQueueActiveSpawnGroupChange = 1462  # offset
    m_bQueueFinishLoading = 1463  # offset
    m_bUnloadingStarted = 1461  # offset
    m_flTimeoutInterval = 1456  # offset
    m_iszLandmarkName = 1440  # offset
    m_iszSpawnGroupFilterName = 1432  # offset
    m_iszSpawnGroupName = 1424  # offset
    m_sFixedSpawnGroupName = 1448  # offset

class CInfoTarget(CPointEntity):
    pass

class CInfoTargetServerOnly(CServerOnlyPointEntity):
    pass

class CInfoTeleportDestination(CPointEntity):
    pass

class CInfoVisibilityBox(CBaseEntity):
    m_bEnabled = 1284  # offset
    m_nMode = 1268  # offset
    m_vBoxSize = 1272  # offset

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

class CInfoWorldLayer(CBaseEntity):
    m_bCreateAsChildSpawnGroup = 1322  # offset
    m_bEntitiesSpawned = 1321  # offset
    m_bWorldLayerVisible = 1320  # offset
    m_hLayerSpawnGroup = 1324  # offset
    m_layerName = 1312  # offset
    m_pOutputOnEntitiesSpawned = 1264  # offset
    m_worldName = 1304  # offset

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

class CInstancedSceneEntity(CSceneEntity):
    m_bHadOwner = 2644  # offset
    m_bIsBackground = 2656  # offset
    m_bRemoveOnCompletion = 2657  # offset
    m_flPostSpeakDelay = 2648  # offset
    m_flPreDelay = 2652  # offset
    m_hOwner = 2640  # offset
    m_hTarget = 2660  # offset

class CInstructorEventEntity(CPointEntity):
    m_hTargetPlayer = 1280  # offset
    m_iszHintTargetEntity = 1272  # offset
    m_iszName = 1264  # offset

class CItem(CBaseAnimGraph):
    m_OnCacheInteraction = 2784  # offset
    m_OnGlovePulled = 2824  # offset
    m_OnPlayerPickup = 2736  # offset
    m_OnPlayerTouch = 2696  # offset
    m_bActivateWhenAtRest = 2776  # offset
    m_bPhysStartAsleep = 2888  # offset
    m_vOriginalSpawnAngles = 2876  # offset
    m_vOriginalSpawnOrigin = 2864  # offset

class CItemAssaultSuit(CItem):
    pass

class CItemDefuser(CItem):
    m_entitySpottedState = 2904  # offset
    m_nSpotRules = 2928  # offset

class CItemDefuserAlias_item_defuser(CItemDefuser):
    pass

class CItemDogtags(CItem):
    m_KillingPlayer = 2908  # offset
    m_OwningPlayer = 2904  # offset

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

class CItemGeneric(CItem):
    m_OnPickup = 3040  # offset
    m_OnTimeout = 3080  # offset
    m_OnTriggerEndTouch = 3200  # offset
    m_OnTriggerStartTouch = 3120  # offset
    m_OnTriggerTouch = 3160  # offset
    m_bAutoStartAmbientSound = 2960  # offset
    m_bGlowWhenInTrigger = 3264  # offset
    m_bHasPickupRadius = 2925  # offset
    m_bHasTriggerRadius = 2924  # offset
    m_bPlayerCounterListenerAdded = 2940  # offset
    m_bPlayerInTriggerRadius = 2941  # offset
    m_bUseable = 3269  # offset
    m_flLastPickupCheck = 2936  # offset
    m_flPickupRadius = 3248  # offset
    m_flPickupRadiusSqr = 2928  # offset
    m_flTriggerRadius = 3252  # offset
    m_flTriggerRadiusSqr = 2932  # offset
    m_glowColor = 3265  # offset
    m_hPickupFilter = 3032  # offset
    m_hPickupParticleEffect = 2976  # offset
    m_hSpawnParticleEffect = 2944  # offset
    m_hTimeoutParticleEffect = 3000  # offset
    m_hTriggerHelper = 3272  # offset
    m_pAllowPickupScriptFunction = 3240  # offset
    m_pAmbientSoundEffect = 2952  # offset
    m_pPickupFilterName = 3024  # offset
    m_pPickupScriptFunction = 2992  # offset
    m_pPickupSoundEffect = 2984  # offset
    m_pSpawnScriptFunction = 2968  # offset
    m_pTimeoutScriptFunction = 3016  # offset
    m_pTimeoutSoundEffect = 3008  # offset
    m_pTriggerSoundEffect = 3256  # offset

class CItemGenericTriggerHelper(CBaseModelEntity):
    m_hParentItem = 2032  # offset

class CItemKevlar(CItem):
    pass

class CItemSoda(CBaseAnimGraph):
    pass

class CItem_Healthshot(CWeaponBaseItem):
    pass

class CKeepUpright(CPointEntity):
    m_angularLimit = 1316  # offset
    m_attachedObject = 1312  # offset
    m_bActive = 1320  # offset
    m_bDampAllRotation = 1321  # offset
    m_localTestAxis = 1284  # offset
    m_nameAttach = 1304  # offset
    m_worldGoalAxis = 1272  # offset

class CKnife(CCSWeaponBase):
    m_bFirstAttack = 4520  # offset

    __metadata__ =     [
        {
            "name": "m_bFirstAttack",
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
    m_bPvsModifyEntity = 432  # offset
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

class CLightDirectionalEntity(CLightEntity):
    pass

class CLightEntity(CBaseModelEntity):
    m_CLightComponent = 2032  # offset

    __metadata__ =     [
        {
            "name": "m_CLightComponent",
            "type": "NetworkVarNames",
            "type_name": "CLightComponent::Storage_t"
        }
    ]

class CLightEnvironmentEntity(CLightDirectionalEntity):
    pass

class CLightOrthoEntity(CLightEntity):
    pass

class CLightSpotEntity(CLightEntity):
    pass

class CLogicAchievement(CLogicalEntity):
    m_OnFired = 1280  # offset
    m_bDisabled = 1264  # offset
    m_iszAchievementEventID = 1272  # offset

class CLogicActiveAutosave(CLogicAutosave):
    m_TriggerHitPoints = 1280  # offset
    m_flDangerousTime = 1292  # offset
    m_flStartTime = 1288  # offset
    m_flTimeToTrigger = 1284  # offset

class CLogicAuto(CBaseEntity):
    m_OnBackgroundMap = 1464  # offset
    m_OnDemoMapSpawn = 1304  # offset
    m_OnLoadGame = 1384  # offset
    m_OnMapSpawn = 1264  # offset
    m_OnMapTransition = 1424  # offset
    m_OnMultiNewMap = 1504  # offset
    m_OnMultiNewRound = 1544  # offset
    m_OnNewGame = 1344  # offset
    m_OnVREnabled = 1584  # offset
    m_OnVRNotEnabled = 1624  # offset
    m_globalstate = 1664  # offset

class CLogicAutosave(CLogicalEntity):
    m_bForceNewLevelUnit = 1264  # offset
    m_minHitPoints = 1268  # offset
    m_minHitPointsToCommit = 1272  # offset

class CLogicBranch(CLogicalEntity):
    m_Listeners = 1272  # offset
    m_OnFalse = 1336  # offset
    m_OnTrue = 1296  # offset
    m_bInValue = 1264  # offset

class CLogicBranchList(CLogicalEntity):
    m_LogicBranchList = 1392  # offset
    m_OnAllFalse = 1464  # offset
    m_OnAllTrue = 1424  # offset
    m_OnMixed = 1504  # offset
    m_eLastState = 1416  # offset
    m_nLogicBranchNames = 1264  # offset

class CLogicCase(CLogicalEntity):
    m_OnCase = 1560  # offset
    m_OnDefault = 2840  # offset
    m_nCase = 1264  # offset
    m_nLastShuffleCase = 1524  # offset
    m_nShuffleCases = 1520  # offset
    m_uchShuffleCaseMap = 1528  # offset

class CLogicCollisionPair(CLogicalEntity):
    m_disabled = 1281  # offset
    m_nameAttach1 = 1264  # offset
    m_nameAttach2 = 1272  # offset
    m_succeeded = 1282  # offset
    m_supportMultipleEntitiesWithSameName = 1280  # offset

class CLogicCompare(CLogicalEntity):
    m_OnEqualTo = 1312  # offset
    m_OnGreaterThan = 1392  # offset
    m_OnLessThan = 1272  # offset
    m_OnNotEqualTo = 1352  # offset
    m_flCompareValue = 1268  # offset
    m_flInValue = 1264  # offset

class CLogicDistanceAutosave(CLogicalEntity):
    m_bCheckCough = 1277  # offset
    m_bForceNewLevelUnit = 1276  # offset
    m_bThinkDangerous = 1278  # offset
    m_flDangerousTime = 1280  # offset
    m_flDistanceToPlayer = 1272  # offset
    m_iszTargetEntity = 1264  # offset

class CLogicDistanceCheck(CLogicalEntity):
    m_InZone1 = 1288  # offset
    m_InZone2 = 1328  # offset
    m_InZone3 = 1368  # offset
    m_flZone1Distance = 1280  # offset
    m_flZone2Distance = 1284  # offset
    m_iszEntityA = 1264  # offset
    m_iszEntityB = 1272  # offset

class CLogicEventListener(CLogicalEntity):
    m_OnEventFired = 1296  # offset
    m_bIsEnabled = 1288  # offset
    m_nTeam = 1292  # offset
    m_strEventName = 1280  # offset

class CLogicGameEvent(CLogicalEntity):
    m_iszEventName = 1264  # offset

class CLogicGameEventListener(CLogicalEntity):
    m_OnEventFired = 1280  # offset
    m_bEnabled = 1336  # offset
    m_bStartDisabled = 1337  # offset
    m_iszGameEventItem = 1328  # offset
    m_iszGameEventName = 1320  # offset

    __metadata__ =     [
        {
            "name": "m_bEnabled",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CLogicLineToEntity(CLogicalEntity):
    m_EndEntity = 1316  # offset
    m_Line = 1264  # offset
    m_SourceName = 1304  # offset
    m_StartEntity = 1312  # offset

class CLogicMeasureMovement(CLogicalEntity):
    m_flScale = 1304  # offset
    m_hMeasureReference = 1292  # offset
    m_hMeasureTarget = 1288  # offset
    m_hTarget = 1296  # offset
    m_hTargetReference = 1300  # offset
    m_nMeasureType = 1308  # offset
    m_strMeasureReference = 1272  # offset
    m_strMeasureTarget = 1264  # offset
    m_strTargetReference = 1280  # offset

class CLogicNPCCounter(CBaseEntity):
    m_OnFactorAll = 1344  # offset
    m_OnFactor_1 = 1504  # offset
    m_OnFactor_2 = 1664  # offset
    m_OnFactor_3 = 1824  # offset
    m_OnMaxCountAll = 1304  # offset
    m_OnMaxCount_1 = 1464  # offset
    m_OnMaxCount_2 = 1624  # offset
    m_OnMaxCount_3 = 1784  # offset
    m_OnMinCountAll = 1264  # offset
    m_OnMinCount_1 = 1424  # offset
    m_OnMinCount_2 = 1584  # offset
    m_OnMinCount_3 = 1744  # offset
    m_OnMinPlayerDistAll = 1384  # offset
    m_OnMinPlayerDist_1 = 1544  # offset
    m_OnMinPlayerDist_2 = 1704  # offset
    m_OnMinPlayerDist_3 = 1864  # offset
    m_bDisabled = 1924  # offset
    m_bInvertState_1 = 1964  # offset
    m_bInvertState_2 = 2004  # offset
    m_bInvertState_3 = 2044  # offset
    m_flDefaultDist_1 = 1988  # offset
    m_flDefaultDist_2 = 2028  # offset
    m_flDefaultDist_3 = 2068  # offset
    m_flDistanceMax = 1920  # offset
    m_hSource = 1904  # offset
    m_iszNPCClassname_1 = 1952  # offset
    m_iszNPCClassname_2 = 1992  # offset
    m_iszNPCClassname_3 = 2032  # offset
    m_iszSourceEntityName = 1912  # offset
    m_nMaxCountAll = 1932  # offset
    m_nMaxCount_1 = 1972  # offset
    m_nMaxCount_2 = 2012  # offset
    m_nMaxCount_3 = 2052  # offset
    m_nMaxFactorAll = 1940  # offset
    m_nMaxFactor_1 = 1980  # offset
    m_nMaxFactor_2 = 2020  # offset
    m_nMaxFactor_3 = 2060  # offset
    m_nMinCountAll = 1928  # offset
    m_nMinCount_1 = 1968  # offset
    m_nMinCount_2 = 2008  # offset
    m_nMinCount_3 = 2048  # offset
    m_nMinFactorAll = 1936  # offset
    m_nMinFactor_1 = 1976  # offset
    m_nMinFactor_2 = 2016  # offset
    m_nMinFactor_3 = 2056  # offset
    m_nNPCState_1 = 1960  # offset
    m_nNPCState_2 = 2000  # offset
    m_nNPCState_3 = 2040  # offset

class CLogicNPCCounterAABB(CLogicNPCCounter):
    m_vDistanceOuterMaxs = 2108  # offset
    m_vDistanceOuterMins = 2096  # offset
    m_vOuterMaxs = 2132  # offset
    m_vOuterMins = 2120  # offset

class CLogicNPCCounterOBB(CLogicNPCCounterAABB):
    pass

class CLogicNavigation(CLogicalEntity):
    m_isOn = 1272  # offset
    m_navProperty = 1276  # offset

class CLogicPlayerProxy(CLogicalEntity):
    m_PlayerDied = 1352  # offset
    m_PlayerHasAmmo = 1272  # offset
    m_PlayerHasNoAmmo = 1312  # offset
    m_RequestedPlayerHealth = 1392  # offset
    m_hPlayer = 1264  # offset

class CLogicProximity(CPointEntity):
    pass

class CLogicRelay(CLogicalEntity):
    m_bDisabled = 1264  # offset
    m_bFastRetrigger = 1267  # offset
    m_bPassthoughCaller = 1268  # offset
    m_bTriggerOnce = 1266  # offset
    m_bWaitForRefire = 1265  # offset

class CLogicRelayAPI:
    pass

class CLogicScript(CPointEntity):
    pass

class CLogicalEntity(CServerOnlyEntity):
    pass

class CMapInfo(CPointEntity):
    m_bDisableAutoGeneratedDMSpawns = 1277  # offset
    m_bFadePlayerVisibilityFarZ = 1288  # offset
    m_bRainTraceToSkyEnabled = 1289  # offset
    m_bUseNormalSpawnsForDM = 1276  # offset
    m_flBombRadius = 1268  # offset
    m_flBotMaxVisionDistance = 1280  # offset
    m_flEnvPuddleRippleDirection = 1300  # offset
    m_flEnvPuddleRippleStrength = 1296  # offset
    m_flEnvRainStrength = 1292  # offset
    m_flEnvWetnessCoverage = 1304  # offset
    m_flEnvWetnessDryingAmount = 1308  # offset
    m_iBuyingStatus = 1264  # offset
    m_iHostageCount = 1284  # offset
    m_iPetPopulation = 1272  # offset

class CMapSharedEnvironment(CLogicalEntity):
    m_targetMapName = 1264  # offset

class CMapVetoPickController(CBaseEntity):
    m_OnLevelTransition = 3824  # offset
    m_OnMapPicked = 3704  # offset
    m_OnMapVetoed = 3664  # offset
    m_OnNewPhaseStarted = 3784  # offset
    m_OnSidesPicked = 3744  # offset
    m_bNeedToPlayFiveSecondsRemaining = 1265  # offset
    m_bPlayedIntroVcd = 1264  # offset
    m_bPreMatchDraftStateChanged = 1304  # offset
    m_dblPreMatchDraftSequenceTime = 1296  # offset
    m_nAccountIDs = 1600  # offset
    m_nCurrentPhase = 3648  # offset
    m_nDraftType = 1308  # offset
    m_nMapId0 = 1856  # offset
    m_nMapId1 = 2112  # offset
    m_nMapId2 = 2368  # offset
    m_nMapId3 = 2624  # offset
    m_nMapId4 = 2880  # offset
    m_nMapId5 = 3136  # offset
    m_nPhaseDurationTicks = 3656  # offset
    m_nPhaseStartTick = 3652  # offset
    m_nStartingSide0 = 3392  # offset
    m_nTeamWinningCoinToss = 1312  # offset
    m_nTeamWithFirstChoice = 1316  # offset
    m_nVoteMapIdsList = 1572  # offset

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

class CMarkupVolume(CBaseModelEntity):
    m_bDisabled = 2032  # offset

class CMarkupVolumeTagged(CMarkupVolume):
    m_GroupNames = 2040  # offset
    m_Tags = 2064  # offset
    m_bGroupByPrefab = 2089  # offset
    m_bGroupByVolume = 2090  # offset
    m_bGroupOtherGroups = 2091  # offset
    m_bIsGroup = 2088  # offset
    m_bIsInGroup = 2092  # offset

class CMarkupVolumeTagged_Nav(CMarkupVolumeTagged):
    m_nScopes = 2096  # offset

class CMarkupVolumeTagged_NavGame(CMarkupVolumeWithRef):
    m_bFloodFillAttribute = 2137  # offset
    m_bSplitNavSpace = 2138  # offset
    m_nScopes = 2136  # offset

class CMarkupVolumeWithRef(CMarkupVolumeTagged):
    m_bUseRef = 2104  # offset
    m_flRefDot = 2132  # offset
    m_vRefPosEntitySpace = 2108  # offset
    m_vRefPosWorldSpace = 2120  # offset

class CMathColorBlend(CLogicalEntity):
    m_OutColor1 = 1272  # offset
    m_OutColor2 = 1276  # offset
    m_OutValue = 1280  # offset
    m_flInMax = 1268  # offset
    m_flInMin = 1264  # offset

class CMathCounter(CLogicalEntity):
    m_OnChangedFromMax = 1480  # offset
    m_OnChangedFromMin = 1440  # offset
    m_OnGetValue = 1320  # offset
    m_OnHitMax = 1400  # offset
    m_OnHitMin = 1360  # offset
    m_OutValue = 1280  # offset
    m_bDisabled = 1274  # offset
    m_bHitMax = 1273  # offset
    m_bHitMin = 1272  # offset
    m_flMax = 1268  # offset
    m_flMin = 1264  # offset

class CMathRemap(CLogicalEntity):
    m_OnFellBelowMax = 1448  # offset
    m_OnFellBelowMin = 1408  # offset
    m_OnRoseAboveMax = 1368  # offset
    m_OnRoseAboveMin = 1328  # offset
    m_OutValue = 1288  # offset
    m_bEnabled = 1284  # offset
    m_flInMax = 1268  # offset
    m_flInMin = 1264  # offset
    m_flOldInValue = 1280  # offset
    m_flOut1 = 1272  # offset
    m_flOut2 = 1276  # offset

class CMessage(CPointEntity):
    m_MessageAttenuation = 1276  # offset
    m_MessageVolume = 1272  # offset
    m_OnShowMessage = 1296  # offset
    m_Radius = 1280  # offset
    m_iszMessage = 1264  # offset
    m_sNoise = 1288  # offset

class CMessageEntity(CPointEntity):
    m_bDeveloperOnly = 1281  # offset
    m_bEnabled = 1282  # offset
    m_drawText = 1280  # offset
    m_messageText = 1272  # offset
    m_radius = 1264  # offset

class CModelPointEntity(CBaseModelEntity):
    pass

class CModelState:
    m_MeshGroupMask = 464  # offset
    m_ModelName = 216  # offset
    m_bClientClothCreationSuppressed = 293  # offset
    m_hModel = 208  # offset
    m_nBodyGroupChoices = 544  # offset
    m_nClothUpdateFlags = 620  # offset
    m_nForceLOD = 619  # offset
    m_nIdealMotionType = 618  # offset

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

class CMolotovGrenade(CBaseCSGrenade):
    pass

class CMolotovProjectile(CBaseCSGrenadeProjectile):
    m_bDetonated = 3136  # offset
    m_bHasBouncedOffPlayer = 3368  # offset
    m_bIsIncGrenade = 3112  # offset
    m_stillTimer = 3144  # offset

    __metadata__ =     [
        {
            "name": "m_bIsIncGrenade",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CMomentaryRotButton(CRotButton):
    m_IdealYaw = 2724  # offset
    m_OnFullyClosed = 2616  # offset
    m_OnFullyOpen = 2576  # offset
    m_OnReachedPosition = 2656  # offset
    m_OnUnpressed = 2536  # offset
    m_Position = 2496  # offset
    m_bUpdateTarget = 2736  # offset
    m_direction = 2740  # offset
    m_end = 2712  # offset
    m_flStartPosition = 2748  # offset
    m_lastUsed = 2696  # offset
    m_returnSpeed = 2744  # offset
    m_sNoise = 2728  # offset
    m_start = 2700  # offset

class CMoverPathNode(CPointEntity):
    m_OnPassThrough = 1384  # offset
    m_OnPassThroughForward = 1424  # offset
    m_OnPassThroughReverse = 1464  # offset
    m_OnStartFromOrInSegment = 1304  # offset
    m_OnStoppedAtOrInSegment = 1344  # offset
    m_hMover = 1504  # offset
    m_szParentPathUniqueID = 1288  # offset
    m_szPathNodeParameter = 1296  # offset
    m_vInTangentLocal = 1264  # offset
    m_vOutTangentLocal = 1276  # offset
    m_xWSPrevParent = 1520  # offset

class CMultiLightProxy(CLogicalEntity):
    m_bPerformScreenFade = 1288  # offset
    m_flBrightnessDelta = 1284  # offset
    m_flCurrentBrightnessMultiplier = 1296  # offset
    m_flLightRadiusFilter = 1280  # offset
    m_flTargetBrightnessMultiplier = 1292  # offset
    m_iszLightClassFilter = 1272  # offset
    m_iszLightNameFilter = 1264  # offset
    m_vecLights = 1304  # offset

class CMultiSource(CLogicalEntity):
    m_OnTrigger = 1520  # offset
    m_globalstate = 1568  # offset
    m_iTotal = 1560  # offset
    m_rgEntities = 1264  # offset
    m_rgTriggered = 1392  # offset

class CMultiplayRules:
    pass

class CNavLinkAreaEntity(CPointEntity):
    m_OnNavLinkFinish = 1424  # offset
    m_OnNavLinkStart = 1384  # offset
    m_bAllowCrossMovableConnections = 1361  # offset
    m_bEnabled = 1360  # offset
    m_bIsTerminus = 1464  # offset
    m_flWidth = 1264  # offset
    m_hFilter = 1376  # offset
    m_nSplits = 1468  # offset
    m_qLocatorAnglesOffset = 1280  # offset
    m_strFilterName = 1368  # offset
    m_strMovementForward = 1296  # offset
    m_strMovementReverse = 1304  # offset
    m_vLocatorOffset = 1268  # offset

class CNavSpaceInfo(CPointEntity):
    pass

class CNavWalkable(CPointEntity):
    pass

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

class CNullEntity(CBaseEntity):
    pass

class COmniLight(CBarnLight):
    m_bShowLight = 2848  # offset
    m_flInnerAngle = 2840  # offset
    m_flOuterAngle = 2844  # offset

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

class COrnamentProp(CDynamicProp):
    m_initialOwner = 3392  # offset

class CParticleSystem(CBaseModelEntity):
    m_bActive = 2544  # offset
    m_bAnimateDuringGameplayPause = 2556  # offset
    m_bFrozen = 2545  # offset
    m_bNoFreeze = 2885  # offset
    m_bNoRamp = 2886  # offset
    m_bNoSave = 2884  # offset
    m_bStartActive = 2887  # offset
    m_clrTint = 3428  # offset
    m_flFreezeTransitionDuration = 2548  # offset
    m_flPreSimTime = 2572  # offset
    m_flStartTime = 2568  # offset
    m_hControlPointEnts = 2628  # offset
    m_iEffectIndex = 2560  # offset
    m_iServerControlPointAssignments = 2624  # offset
    m_iszControlPointNames = 2896  # offset
    m_iszEffectName = 2888  # offset
    m_nDataCP = 3408  # offset
    m_nStopType = 2552  # offset
    m_nTintCP = 3424  # offset
    m_szSnapshotFileName = 2032  # offset
    m_vServerControlPoints = 2576  # offset
    m_vecDataCPValue = 3412  # offset

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

class CPathCorner(CPointEntity):
    m_OnPass = 1272  # offset
    m_flRadius = 1268  # offset
    m_flWait = 1264  # offset

class CPathCornerCrash(CPathCorner):
    pass

class CPathKeyFrame(CLogicalEntity):
    m_Angles = 1276  # offset
    m_Origin = 1264  # offset
    m_flMoveSpeed = 1344  # offset
    m_flNextTime = 1320  # offset
    m_iNextKey = 1312  # offset
    m_pNextKey = 1328  # offset
    m_pPrevKey = 1336  # offset
    m_qAngle = 1296  # offset

class CPathMover(CPathSimple):
    m_vecMovers = 1560  # offset
    m_vecPathNodes = 1536  # offset
    m_xInitialPathWorldToLocal = 1584  # offset

class CPathParticleRope(CBaseEntity):
    m_ColorTint = 1324  # offset
    m_PathNodes_Color = 1416  # offset
    m_PathNodes_Name = 1288  # offset
    m_PathNodes_PinEnabled = 1440  # offset
    m_PathNodes_Position = 1344  # offset
    m_PathNodes_RadiusScale = 1464  # offset
    m_PathNodes_TangentIn = 1368  # offset
    m_PathNodes_TangentOut = 1392  # offset
    m_bStartActive = 1272  # offset
    m_flMaxSimulationTime = 1276  # offset
    m_flParticleSpacing = 1312  # offset
    m_flRadius = 1320  # offset
    m_flSlack = 1316  # offset
    m_iEffectIndex = 1336  # offset
    m_iszEffectName = 1280  # offset
    m_nEffectState = 1328  # offset

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

class CPathParticleRopeAlias_path_particle_rope_clientside(CPathParticleRope):
    pass

class CPathQueryComponent(CEntityComponent):
    pass

class CPathSimple(CBaseEntity):
    m_CPathQueryComponent = 1280  # offset
    m_bClosedLoop = 1528  # offset
    m_pathString = 1520  # offset

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

class CPathTrack(CPointEntity):
    m_OnPass = 1312  # offset
    m_altName = 1296  # offset
    m_eOrientationType = 1308  # offset
    m_flRadius = 1288  # offset
    m_length = 1292  # offset
    m_nIterVal = 1304  # offset
    m_paltpath = 1280  # offset
    m_pnext = 1264  # offset
    m_pprevious = 1272  # offset

class CPhysBallSocket(CPhysConstraint):
    m_bEnableSwingLimit = 1380  # offset
    m_bEnableTwistLimit = 1388  # offset
    m_flJointFriction = 1376  # offset
    m_flMaxTwistAngle = 1396  # offset
    m_flMinTwistAngle = 1392  # offset
    m_flSwingLimit = 1384  # offset

class CPhysBox(CBreakable):
    m_OnAwakened = 2336  # offset
    m_OnDamaged = 2296  # offset
    m_OnMotionEnabled = 2376  # offset
    m_OnPlayerUse = 2416  # offset
    m_OnStartTouch = 2456  # offset
    m_angHoverPoseAngles = 2272  # offset
    m_bEnableUseOutput = 2285  # offset
    m_bNotSolidToWorld = 2284  # offset
    m_damageToEnableMotion = 2252  # offset
    m_damageType = 2248  # offset
    m_flForceToEnableMotion = 2256  # offset
    m_flTouchOutputPerEntityDelay = 2288  # offset
    m_hCarryingPlayer = 2496  # offset
    m_nHoverPoseFlags = 2286  # offset
    m_vHoverPosePosition = 2260  # offset

class CPhysConstraint(CLogicalEntity):
    m_OnBreak = 1336  # offset
    m_bSnapObjectPositions = 1332  # offset
    m_breakSound = 1312  # offset
    m_forceLimit = 1320  # offset
    m_hAttach1 = 1288  # offset
    m_hAttach2 = 1292  # offset
    m_minTeleportDistance = 1328  # offset
    m_nameAttach1 = 1272  # offset
    m_nameAttach2 = 1280  # offset
    m_nameAttachment1 = 1296  # offset
    m_nameAttachment2 = 1304  # offset
    m_torqueLimit = 1324  # offset

class CPhysExplosion(CPointEntity):
    m_OnPushedPlayer = 1304  # offset
    m_bAffectInvulnerableEnts = 1297  # offset
    m_bConvertToDebrisWhenPossible = 1296  # offset
    m_bExplodeOnSpawn = 1264  # offset
    m_flDamage = 1272  # offset
    m_flInnerRadius = 1288  # offset
    m_flMagnitude = 1268  # offset
    m_flPushScale = 1292  # offset
    m_radius = 1276  # offset
    m_targetEntityName = 1280  # offset

class CPhysFixed(CPhysConstraint):
    m_bEnableAngularConstraint = 1393  # offset
    m_bEnableLinearConstraint = 1392  # offset
    m_flAngularDampingRatio = 1388  # offset
    m_flAngularFrequency = 1384  # offset
    m_flLinearDampingRatio = 1380  # offset
    m_flLinearFrequency = 1376  # offset
    m_sBoneName1 = 1400  # offset
    m_sBoneName2 = 1408  # offset

class CPhysForce(CPointEntity):
    m_attachedObject = 1288  # offset
    m_force = 1280  # offset
    m_forceTime = 1284  # offset
    m_integrator = 1296  # offset
    m_nameAttach = 1272  # offset
    m_wasRestored = 1292  # offset

class CPhysHinge(CPhysConstraint):
    m_NotifyMaxLimitReached = 1576  # offset
    m_NotifyMinLimitReached = 1536  # offset
    m_OnStartMoving = 1728  # offset
    m_OnStopMoving = 1768  # offset
    m_bAtMaxLimit = 1617  # offset
    m_bAtMinLimit = 1616  # offset
    m_bIsAxisLocal = 1692  # offset
    m_flAngleSpeed = 1716  # offset
    m_flAngleSpeedThreshold = 1720  # offset
    m_flInitialRotation = 1704  # offset
    m_flMaxRotation = 1700  # offset
    m_flMinRotation = 1696  # offset
    m_flMotorDampingRatio = 1712  # offset
    m_flMotorFrequency = 1708  # offset
    m_hinge = 1620  # offset
    m_hingeFriction = 1684  # offset
    m_soundInfo = 1384  # offset
    m_systemLoadScale = 1688  # offset

class CPhysHingeAlias_phys_hinge_local(CPhysHinge):
    pass

class CPhysImpact(CPointEntity):
    m_damage = 1264  # offset
    m_directionEntityName = 1272  # offset
    m_distance = 1268  # offset

class CPhysLength(CPhysConstraint):
    m_addLength = 1412  # offset
    m_bEnableCollision = 1424  # offset
    m_minLength = 1416  # offset
    m_offset = 1376  # offset
    m_totalLength = 1420  # offset
    m_vecAttach = 1400  # offset

class CPhysMagnet(CBaseAnimGraph):
    m_MagnettedEntities = 2784  # offset
    m_OnMagnetAttach = 2688  # offset
    m_OnMagnetDetach = 2728  # offset
    m_bActive = 2808  # offset
    m_bHasHitSomething = 2809  # offset
    m_flNextSuckTime = 2820  # offset
    m_flRadius = 2816  # offset
    m_flTotalMass = 2812  # offset
    m_forceLimit = 2772  # offset
    m_iMaxObjectsAttached = 2824  # offset
    m_massScale = 2768  # offset
    m_torqueLimit = 2776  # offset

class CPhysMotor(CLogicalEntity):
    m_additionalAcceleration = 1300  # offset
    m_angularAcceleration = 1304  # offset
    m_flMotorFriction = 1296  # offset
    m_flSpeedWhenSpinUpOrSpinDownStarted = 1316  # offset
    m_flTargetSpeed = 1312  # offset
    m_flTorqueScale = 1308  # offset
    m_hAnchorObject = 1284  # offset
    m_hAttachedObject = 1280  # offset
    m_motor = 1336  # offset
    m_nameAnchor = 1272  # offset
    m_nameAttach = 1264  # offset
    m_spinDown = 1292  # offset
    m_spinUp = 1288  # offset

class CPhysMotorAPI:
    pass

class CPhysPulley(CPhysConstraint):
    m_addLength = 1412  # offset
    m_gearRatio = 1416  # offset
    m_offset = 1388  # offset
    m_position2 = 1376  # offset

class CPhysSlideConstraint(CPhysConstraint):
    m_axisEnd = 1384  # offset
    m_bEnableAngularConstraint = 1409  # offset
    m_bEnableLinearConstraint = 1408  # offset
    m_bUseEntityPivot = 1420  # offset
    m_flMotorDampingRatio = 1416  # offset
    m_flMotorFrequency = 1412  # offset
    m_initialOffset = 1404  # offset
    m_slideFriction = 1396  # offset
    m_soundInfo = 1424  # offset
    m_systemLoadScale = 1400  # offset

class CPhysThruster(CPhysForce):
    m_localOrigin = 1360  # offset

class CPhysTorque(CPhysForce):
    m_axis = 1360  # offset

class CPhysWheelConstraint(CPhysConstraint):
    m_bEnableSteeringLimit = 1400  # offset
    m_bEnableSuspensionLimit = 1388  # offset
    m_flMaxSteeringAngle = 1408  # offset
    m_flMaxSuspensionOffset = 1396  # offset
    m_flMinSteeringAngle = 1404  # offset
    m_flMinSuspensionOffset = 1392  # offset
    m_flSpinAxisFriction = 1416  # offset
    m_flSteeringAxisFriction = 1412  # offset
    m_flSuspensionDampingRatio = 1380  # offset
    m_flSuspensionFrequency = 1376  # offset
    m_flSuspensionHeightOffset = 1384  # offset
    m_hSteeringMimicsEntity = 1420  # offset

class CPhysicalButton(CBaseButton):
    pass

class CPhysicsEntitySolver(CLogicalEntity):
    m_cancelTime = 1300  # offset
    m_hMovingEntity = 1288  # offset
    m_hPhysicsBlocker = 1292  # offset
    m_separationDuration = 1296  # offset

class CPhysicsProp(CBreakableProp):
    m_CrateType = 3508  # offset
    m_MotionEnabled = 3152  # offset
    m_OnAsleep = 3272  # offset
    m_OnAwake = 3232  # offset
    m_OnAwakened = 3192  # offset
    m_OnOutOfWorld = 3352  # offset
    m_OnPlayerPickup = 3392  # offset
    m_OnPlayerUse = 3312  # offset
    m_bAcceptDamageFromHeldObjects = 3503  # offset
    m_bAttachedToReferenceFrame = 3562  # offset
    m_bAwake = 3561  # offset
    m_bDroppedByPlayer = 3457  # offset
    m_bEnableUseOutput = 3504  # offset
    m_bFirstCollisionAfterLaunch = 3459  # offset
    m_bForceNavIgnore = 3432  # offset
    m_bForceNpcExclude = 3434  # offset
    m_bHasBeenAwakened = 3460  # offset
    m_bIsOverrideProp = 3461  # offset
    m_bMuteImpactEffects = 3493  # offset
    m_bNoNavmeshBlocker = 3433  # offset
    m_bRemovableForAmmoBalancing = 3560  # offset
    m_bShouldAutoConvertBackFromDebris = 3492  # offset
    m_bThrownByPlayer = 3456  # offset
    m_bTouchedByPlayer = 3458  # offset
    m_buoyancyScale = 3440  # offset
    m_damageToEnableMotion = 3448  # offset
    m_damageType = 3444  # offset
    m_fNextCheckDisableMotionContactsTime = 3472  # offset
    m_flForceToEnableMotion = 3452  # offset
    m_flLastBurn = 3464  # offset
    m_glowColor = 3488  # offset
    m_iInitialGlowState = 3476  # offset
    m_massScale = 3436  # offset
    m_nDynamicContinuousContactBehavior = 3468  # offset
    m_nGlowRange = 3480  # offset
    m_nGlowRangeMin = 3484  # offset
    m_nItemCount = 3544  # offset
    m_strItemClass = 3512  # offset

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

class CPhysicsPropMultiplayer(CPhysicsProp):
    pass

class CPhysicsPropOverride(CPhysicsProp):
    pass

class CPhysicsPropRespawnable(CPhysicsProp):
    m_flRespawnDuration = 3616  # offset
    m_vOriginalMaxs = 3604  # offset
    m_vOriginalMins = 3592  # offset
    m_vOriginalSpawnAngles = 3580  # offset
    m_vOriginalSpawnOrigin = 3568  # offset

class CPhysicsSpring(CBaseEntity):
    m_end = 1316  # offset
    m_flDampingRatio = 1276  # offset
    m_flFrequency = 1272  # offset
    m_flRestLength = 1280  # offset
    m_nameAttachEnd = 1296  # offset
    m_nameAttachStart = 1288  # offset
    m_start = 1304  # offset
    m_teleportTick = 1328  # offset

class CPhysicsWire(CBaseEntity):
    m_nDensity = 1264  # offset

class CPlantedC4(CBaseAnimGraph):
    m_AttributeManager = 2712  # offset
    m_OnBombBeginDefuse = 3512  # offset
    m_OnBombDefuseAborted = 3552  # offset
    m_OnBombDefused = 3472  # offset
    m_angCatchUpToPlayerEye = 3688  # offset
    m_bBeingDefused = 3636  # offset
    m_bBombDefused = 3660  # offset
    m_bBombTicking = 2696  # offset
    m_bCannotBeDefused = 3592  # offset
    m_bHasExploded = 3629  # offset
    m_bTrainingPlacedByPlayer = 3628  # offset
    m_bVoiceAlertFired = 3672  # offset
    m_bVoiceAlertPlayed = 3673  # offset
    m_entitySpottedState = 3600  # offset
    m_fLastDefuseTime = 3644  # offset
    m_flC4Blow = 2700  # offset
    m_flDefuseCountDown = 3656  # offset
    m_flDefuseLength = 3652  # offset
    m_flLastSpinDetectionTime = 3700  # offset
    m_flNextBotBeepTime = 3680  # offset
    m_flTimerLength = 3632  # offset
    m_hBombDefuser = 3664  # offset
    m_iProgressBarTime = 3668  # offset
    m_nBombSite = 2704  # offset
    m_nSourceSoundscapeHash = 2708  # offset
    m_nSpotRules = 3624  # offset

    __metadata__ =     [
        {
            "name": "m_bBombTicking",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_flC4Blow",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
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
            "name": "m_AttributeManager",
            "type": "NetworkVarNames",
            "type_name": "CAttributeContainer"
        },
        {
            "name": "m_bCannotBeDefused",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_entitySpottedState",
            "type": "NetworkVarNames",
            "type_name": "EntitySpottedState_t"
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
        }
    ]

class CPlatTrigger(CBaseModelEntity):
    m_pPlatform = 2032  # offset

class CPlayerPing(CBaseEntity):
    m_bUrgent = 1284  # offset
    m_hPingedEntity = 1276  # offset
    m_hPlayer = 1272  # offset
    m_iType = 1280  # offset
    m_szPlaceName = 1285  # offset

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

class CPlayerSprayDecal(CModelPointEntity):
    m_flCreationTime = 2108  # offset
    m_nEntity = 2100  # offset
    m_nHitbox = 2104  # offset
    m_nPlayer = 2096  # offset
    m_nTintID = 2112  # offset
    m_nUniqueID = 2032  # offset
    m_nVersion = 2116  # offset
    m_rtGcTime = 2044  # offset
    m_ubSignature = 2117  # offset
    m_unAccountID = 2036  # offset
    m_unTraceID = 2040  # offset
    m_vecEndPos = 2048  # offset
    m_vecLeft = 2072  # offset
    m_vecNormal = 2084  # offset
    m_vecStart = 2060  # offset

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

class CPlayerVisibility(CBaseEntity):
    m_bIsEnabled = 1281  # offset
    m_bStartDisabled = 1280  # offset
    m_flFadeTime = 1276  # offset
    m_flFogDistanceMultiplier = 1268  # offset
    m_flFogMaxDensityMultiplier = 1272  # offset
    m_flVisibilityStrength = 1264  # offset

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

class CPlayer_AutoaimServices(CPlayerPawnComponent):
    pass

class CPlayer_CameraServices(CPlayerPawnComponent):
    m_PlayerFog = 88  # offset
    m_PostProcessingVolumes = 288  # offset
    m_audio = 168  # offset
    m_flCsViewPunchAngleTickRatio = 80  # offset
    m_flOldPlayerViewOffsetZ = 316  # offset
    m_flOldPlayerZ = 312  # offset
    m_hColorCorrectionCtrl = 152  # offset
    m_hTonemapController = 160  # offset
    m_hTriggerSoundscapeList = 344  # offset
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
            "type_name": "CHandle<CPostProcessingVolume>"
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
    m_vecSmoothedVelocity = 628  # offset

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
    m_bPreventWeaponPickup = 160  # offset
    m_hActiveWeapon = 88  # offset
    m_hLastWeapon = 92  # offset
    m_hMyWeapons = 64  # offset
    m_iAmmo = 96  # offset

    __metadata__ =     [
        {
            "name": "m_hMyWeapons",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBasePlayerWeapon>"
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

class CPointAngleSensor(CPointEntity):
    m_FacingPercentage = 1424  # offset
    m_OnFacingLookat = 1304  # offset
    m_OnNotFacingLookat = 1344  # offset
    m_TargetDir = 1384  # offset
    m_bDisabled = 1264  # offset
    m_bFired = 1300  # offset
    m_flDotTolerance = 1292  # offset
    m_flDuration = 1288  # offset
    m_flFacingTime = 1296  # offset
    m_hLookAtEntity = 1284  # offset
    m_hTargetEntity = 1280  # offset
    m_nLookAtName = 1272  # offset

class CPointAngularVelocitySensor(CPointEntity):
    m_AngularVelocity = 1320  # offset
    m_OnEqualTo = 1520  # offset
    m_OnGreaterThan = 1440  # offset
    m_OnGreaterThanOrEqualTo = 1480  # offset
    m_OnLessThan = 1360  # offset
    m_OnLessThanOrEqualTo = 1400  # offset
    m_bUseHelper = 1316  # offset
    m_flFireInterval = 1284  # offset
    m_flFireTime = 1280  # offset
    m_flLastAngVelocity = 1288  # offset
    m_flThreshold = 1268  # offset
    m_hTargetEntity = 1264  # offset
    m_lastOrientation = 1292  # offset
    m_nLastCompareResult = 1272  # offset
    m_nLastFireResult = 1276  # offset
    m_vecAxis = 1304  # offset

class CPointBroadcastClientCommand(CPointEntity):
    pass

class CPointCamera(CBaseEntity):
    m_DegreesPerSecond = 1344  # offset
    m_FOV = 1264  # offset
    m_FogColor = 1273  # offset
    m_Resolution = 1268  # offset
    m_TargetFOV = 1340  # offset
    m_bActive = 1292  # offset
    m_bAlignWithParent = 1317  # offset
    m_bCanHLTVUse = 1316  # offset
    m_bDofEnabled = 1318  # offset
    m_bFogEnable = 1272  # offset
    m_bIsOn = 1348  # offset
    m_bNoSky = 1300  # offset
    m_bUseScreenAspectRatio = 1293  # offset
    m_fBrightness = 1304  # offset
    m_flAspectRatio = 1296  # offset
    m_flDofFarBlurry = 1332  # offset
    m_flDofFarCrisp = 1328  # offset
    m_flDofNearBlurry = 1320  # offset
    m_flDofNearCrisp = 1324  # offset
    m_flDofTiltToGround = 1336  # offset
    m_flFogEnd = 1284  # offset
    m_flFogMaxDensity = 1288  # offset
    m_flFogStart = 1280  # offset
    m_flZFar = 1308  # offset
    m_flZNear = 1312  # offset
    m_pNext = 1352  # offset

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

class CPointCameraVFOV(CPointCamera):
    m_flVerticalFOV = 1360  # offset

class CPointChildModifier(CPointEntity):
    m_bOrphanInsteadOfDeletingChildrenOnRemove = 1264  # offset

class CPointClientCommand(CPointEntity):
    pass

class CPointClientUIDialog(CBaseClientUIEntity):
    m_bStartEnabled = 2468  # offset
    m_hActivator = 2464  # offset

    __metadata__ =     [
        {
            "name": "m_hActivator",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        }
    ]

class CPointClientUIWorldPanel(CBaseClientUIEntity):
    m_bAllowInteractionFromAllSceneWorlds = 2504  # offset
    m_bDisableMipGen = 2544  # offset
    m_bExcludeFromSaveGames = 2541  # offset
    m_bFollowPlayerAcrossTeleport = 2466  # offset
    m_bGrabbable = 2542  # offset
    m_bIgnoreInput = 2464  # offset
    m_bLit = 2465  # offset
    m_bNoDepth = 2537  # offset
    m_bOnlyRenderToTexture = 2543  # offset
    m_bOpaque = 2536  # offset
    m_bRenderBackface = 2539  # offset
    m_bUseOffScreenIndicator = 2540  # offset
    m_bVisibleWhenParentNoDraw = 2538  # offset
    m_flDPI = 2476  # offset
    m_flDepthOffset = 2484  # offset
    m_flHeight = 2472  # offset
    m_flInteractDistance = 2480  # offset
    m_flWidth = 2468  # offset
    m_nExplicitImageLayout = 2548  # offset
    m_unHorizontalAlign = 2492  # offset
    m_unOrientation = 2500  # offset
    m_unOwnerContext = 2488  # offset
    m_unVerticalAlign = 2496  # offset
    m_vecCSSClasses = 2512  # offset

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

class CPointClientUIWorldTextPanel(CPointClientUIWorldPanel):
    m_messageText = 2552  # offset

    __metadata__ =     [
        {
            "name": "m_messageText",
            "type": "NetworkVarNames",
            "type_name": "char"
        }
    ]

class CPointCommentaryNode(CBaseAnimGraph):
    m_bActive = 2888  # offset
    m_bDisabled = 2789  # offset
    m_bListenedTo = 2928  # offset
    m_bPreventChangesWhileMoving = 2788  # offset
    m_bPreventMovement = 2744  # offset
    m_bUnderCrosshair = 2745  # offset
    m_bUnstoppable = 2746  # offset
    m_flAbortedPlaybackAt = 2804  # offset
    m_flFinishedTime = 2748  # offset
    m_flStartTime = 2892  # offset
    m_flStartTimeInCommentary = 2896  # offset
    m_hViewPosition = 2736  # offset
    m_hViewPositionMover = 2740  # offset
    m_hViewTarget = 2720  # offset
    m_hViewTargetAngles = 2724  # offset
    m_iNodeNumber = 2920  # offset
    m_iNodeNumberMax = 2924  # offset
    m_iszCommentaryFile = 2704  # offset
    m_iszPostCommands = 2696  # offset
    m_iszPreCommands = 2688  # offset
    m_iszSpeakers = 2912  # offset
    m_iszTitle = 2904  # offset
    m_iszViewPosition = 2728  # offset
    m_iszViewTarget = 2712  # offset
    m_pOnCommentaryStarted = 2808  # offset
    m_pOnCommentaryStopped = 2848  # offset
    m_vecFinishAngles = 2776  # offset
    m_vecFinishOrigin = 2752  # offset
    m_vecOriginalAngles = 2764  # offset
    m_vecTeleportOrigin = 2792  # offset

    __metadata__ =     [
        {
            "name": "m_iszCommentaryFile",
            "type": "NetworkVarNames",
            "type_name": "string_t"
        },
        {
            "name": "m_hViewPosition",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
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
        }
    ]

class CPointEntity(CBaseEntity):
    pass

class CPointEntityFinder(CBaseEntity):
    m_FindMethod = 1300  # offset
    m_OnFoundEntity = 1304  # offset
    m_hEntity = 1264  # offset
    m_hFilter = 1280  # offset
    m_hReference = 1296  # offset
    m_iFilterName = 1272  # offset
    m_iRefName = 1288  # offset

class CPointGamestatsCounter(CPointEntity):
    m_bDisabled = 1272  # offset
    m_strStatisticName = 1264  # offset

class CPointGiveAmmo(CPointEntity):
    m_pActivator = 1264  # offset

class CPointHurt(CPointEntity):
    m_bitsDamageType = 1268  # offset
    m_flDelay = 1276  # offset
    m_flRadius = 1272  # offset
    m_nDamage = 1264  # offset
    m_pActivator = 1288  # offset
    m_strTarget = 1280  # offset

class CPointOrient(CBaseEntity):
    m_bActive = 1276  # offset
    m_flLastGameTime = 1292  # offset
    m_flMaxTurnRate = 1288  # offset
    m_hTarget = 1272  # offset
    m_iszSpawnTargetName = 1264  # offset
    m_nConstraint = 1284  # offset
    m_nGoalDirection = 1280  # offset

class CPointPrefab(CServerOnlyPointEntity):
    m_associatedRelayEntity = 1292  # offset
    m_associatedRelayTargetName = 1280  # offset
    m_bLoadDynamic = 1289  # offset
    m_fixupNames = 1288  # offset
    m_forceWorldGroupID = 1272  # offset
    m_targetMapName = 1264  # offset

class CPointProximitySensor(CPointEntity):
    m_Distance = 1272  # offset
    m_bDisabled = 1264  # offset
    m_hTargetEntity = 1268  # offset

class CPointPulse(CBaseEntity):
    pass

class CPointPush(CPointEntity):
    m_bEnabled = 1264  # offset
    m_flConeOfInfluence = 1280  # offset
    m_flInnerRadius = 1276  # offset
    m_flMagnitude = 1268  # offset
    m_flRadius = 1272  # offset
    m_hFilter = 1296  # offset
    m_iszFilterName = 1288  # offset

class CPointServerCommand(CPointEntity):
    pass

class CPointTeleport(CServerOnlyPointEntity):
    m_bTeleportParentedEntities = 1288  # offset
    m_bTeleportUseCurrentAngle = 1289  # offset
    m_vSaveAngles = 1276  # offset
    m_vSaveOrigin = 1264  # offset

class CPointTeleportAPI:
    pass

class CPointTemplate(CLogicalEntity):
    m_ScriptCallbackScope = 1360  # offset
    m_ScriptSpawnCallback = 1352  # offset
    m_SpawnedEntityHandles = 1328  # offset
    m_bAsynchronouslySpawnEntities = 1292  # offset
    m_clientOnlyEntityBehavior = 1296  # offset
    m_createdSpawnGroupHandles = 1304  # offset
    m_flTimeoutInterval = 1288  # offset
    m_iszEntityFilterName = 1280  # offset
    m_iszSource2EntityLumpName = 1272  # offset
    m_iszWorldName = 1264  # offset
    m_ownerSpawnGroupType = 1300  # offset

class CPointTemplateAPI:
    pass

class CPointValueRemapper(CBaseEntity):
    m_OnDisengage = 1744  # offset
    m_OnEngage = 1704  # offset
    m_OnReachedValueCustom = 1664  # offset
    m_OnReachedValueOne = 1624  # offset
    m_OnReachedValueZero = 1584  # offset
    m_Position = 1504  # offset
    m_PositionDelta = 1544  # offset
    m_bDisabled = 1264  # offset
    m_bEngaged = 1408  # offset
    m_bFirstUpdate = 1409  # offset
    m_bRequiresUseKey = 1308  # offset
    m_bUpdateOnClient = 1265  # offset
    m_flCurrentMomentum = 1392  # offset
    m_flCustomOutputValue = 1436  # offset
    m_flDisengageDistance = 1300  # offset
    m_flEngageDistance = 1304  # offset
    m_flInputOffset = 1404  # offset
    m_flMaximumChangePerSecond = 1296  # offset
    m_flMomentumModifier = 1384  # offset
    m_flPreviousUpdateTickTime = 1416  # offset
    m_flPreviousValue = 1412  # offset
    m_flRatchetOffset = 1400  # offset
    m_flSnapValue = 1388  # offset
    m_hOutputEntities = 1352  # offset
    m_hRemapLineEnd = 1292  # offset
    m_hRemapLineStart = 1288  # offset
    m_hUsingPlayer = 1432  # offset
    m_iszOutputEntity2Name = 1328  # offset
    m_iszOutputEntity3Name = 1336  # offset
    m_iszOutputEntity4Name = 1344  # offset
    m_iszOutputEntityName = 1320  # offset
    m_iszRemapLineEndName = 1280  # offset
    m_iszRemapLineStartName = 1272  # offset
    m_iszSoundDisengage = 1448  # offset
    m_iszSoundEngage = 1440  # offset
    m_iszSoundMovingLoop = 1472  # offset
    m_iszSoundReachedValueOne = 1464  # offset
    m_iszSoundReachedValueZero = 1456  # offset
    m_nHapticsType = 1376  # offset
    m_nInputType = 1268  # offset
    m_nMomentumType = 1380  # offset
    m_nOutputType = 1312  # offset
    m_nRatchetType = 1396  # offset
    m_vecPreviousTestPoint = 1420  # offset

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
            "type_name": "CHandle<CBaseEntity>"
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

class CPointVelocitySensor(CPointEntity):
    m_Velocity = 1296  # offset
    m_bEnabled = 1280  # offset
    m_fPrevVelocity = 1284  # offset
    m_flAvgInterval = 1288  # offset
    m_hTargetEntity = 1264  # offset
    m_vecAxis = 1268  # offset

class CPointWorldText(CModelPointEntity):
    m_BackgroundMaterialName = 2608  # offset
    m_Color = 2704  # offset
    m_FontName = 2544  # offset
    m_bDrawBackground = 2688  # offset
    m_bEnabled = 2672  # offset
    m_bFullbright = 2673  # offset
    m_flBackgroundBorderHeight = 2696  # offset
    m_flBackgroundBorderWidth = 2692  # offset
    m_flBackgroundWorldToUV = 2700  # offset
    m_flDepthOffset = 2684  # offset
    m_flFontSize = 2680  # offset
    m_flWorldUnitsPerPx = 2676  # offset
    m_messageText = 2032  # offset
    m_nJustifyHorizontal = 2708  # offset
    m_nJustifyVertical = 2712  # offset
    m_nReorientMode = 2716  # offset

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

class CPostProcessingVolume(CBaseTrigger):
    m_bExposureControl = 2557  # offset
    m_bMaster = 2556  # offset
    m_flExposureCompensation = 2540  # offset
    m_flExposureFadeSpeedDown = 2548  # offset
    m_flExposureFadeSpeedUp = 2544  # offset
    m_flFadeDuration = 2520  # offset
    m_flMaxExposure = 2536  # offset
    m_flMaxLogExposure = 2528  # offset
    m_flMinExposure = 2532  # offset
    m_flMinLogExposure = 2524  # offset
    m_flTonemapEVSmoothingRange = 2552  # offset
    m_hPostSettings = 2512  # offset

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

class CPrecipitation(CBaseTrigger):
    pass

class CPrecipitationBlocker(CBaseModelEntity):
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

class CPropDoorRotating(CBasePropDoor):
    m_angGoal = 4144  # offset
    m_angRotationAjarDeprecated = 4096  # offset
    m_angRotationClosed = 4108  # offset
    m_angRotationOpenBack = 4132  # offset
    m_angRotationOpenForward = 4120  # offset
    m_bAjarDoorShouldntAlwaysOpen = 4204  # offset
    m_eCurrentOpenDirection = 4088  # offset
    m_eOpenDirection = 4084  # offset
    m_eSpawnPosition = 4080  # offset
    m_flAjarAngle = 4092  # offset
    m_flDistance = 4076  # offset
    m_hEntityBlocker = 4208  # offset
    m_vecAxis = 4064  # offset
    m_vecBackBoundsMax = 4192  # offset
    m_vecBackBoundsMin = 4180  # offset
    m_vecForwardBoundsMax = 4168  # offset
    m_vecForwardBoundsMin = 4156  # offset

class CPropDoorRotatingBreakable(CPropDoorRotating):
    m_bBreakable = 4224  # offset
    m_currentDamageState = 4228  # offset
    m_damageStates = 4232  # offset
    m_isAbleToCloseAreaPortals = 4225  # offset

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

class CPulseCell_Outflow_ListenForAnimgraphTag:
    m_OnCanceled = 216  # offset
    m_OnEnd = 144  # offset
    m_OnStart = 72  # offset
    m_TagName = 288  # offset

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
            "name": "MPulseEditorSubHeaderText",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_ListenForEntityOutput:
    m_OnCanceled = 144  # offset
    m_OnFired = 72  # offset
    m_bListenUntilCanceled = 232  # offset
    m_strEntityOutput = 216  # offset
    m_strEntityOutputParam = 224  # offset

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
            "name": "MPulseEditorSubHeaderText",
            "type": "Unknown"
        },
        {
            "name": "MPulseEditorHeaderIcon",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_ListenForEntityOutput__CursorState_t:
    m_entity = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_PlaySceneBase:
    m_OnCanceled = 144  # offset
    m_OnFinished = 72  # offset
    m_Triggers = 216  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_PlaySceneBase__CursorState_t:
    m_mainActor = 4  # offset
    m_sceneInstance = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Outflow_PlaySequence:
    m_ParamSequenceName = 240  # offset

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

class CPulseCell_Outflow_PlayVCD:
    m_vcdFilename = 240  # offset

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

class CPulseCell_Outflow_ScriptedSequence:
    m_OnCanceled = 240  # offset
    m_OnFinished = 168  # offset
    m_Triggers = 312  # offset
    m_bDisallowInterrupts = 86  # offset
    m_bDontTeleportAtEnd = 85  # offset
    m_bEnsureOnNavmeshOnFinish = 84  # offset
    m_nExpectedNumSequencesInSyncGroup = 80  # offset
    m_scriptedSequenceDataMain = 88  # offset
    m_szSyncGroup = 72  # offset
    m_vecAdditionalActors = 144  # offset

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

class CPulseCell_Outflow_ScriptedSequence__CursorState_t:
    m_scriptedSequence = 0  # offset

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

class CPulseCell_SoundEventStart:
    m_Type = 72  # offset

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

class CPulseCell_Step_FollowEntity:
    m_ParamBoneOrAttachName = 72  # offset
    m_ParamBoneOrAttachNameChild = 80  # offset

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

class CPulseCell_Step_SetAnimGraphParam:
    m_ParamName = 72  # offset

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

class CPulseFuncs_GameParticleManager:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        }
    ]

class CPulseGameBlackboard(CBaseEntity):
    m_strGraphName = 1264  # offset
    m_strStateBlob = 1272  # offset

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

class CPulseGraphInstance_GameBlackboard:
    pass

class CPulseGraphInstance_ServerEntity:
    m_bActivated = 396  # offset
    m_hOwner = 392  # offset
    m_sNameFixupLocal = 416  # offset
    m_sNameFixupParent = 408  # offset
    m_sNameFixupStaticPrefix = 400  # offset
    m_sProceduralWorldNameForRelays = 424  # offset

class CPulseMathlib:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulsePhysicsConstraintsFuncs:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseServerCursor:
    m_hActivator = 216  # offset
    m_hCaller = 220  # offset

class CPulseServerFuncs:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseServerFuncs_Sounds:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyFriendlyName",
            "type": "Unknown"
        },
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

class CPushable(CBreakable):
    pass

class CRagdollConstraint(CPhysConstraint):
    m_xfriction = 1400  # offset
    m_xmax = 1380  # offset
    m_xmin = 1376  # offset
    m_yfriction = 1404  # offset
    m_ymax = 1388  # offset
    m_ymin = 1384  # offset
    m_zfriction = 1408  # offset
    m_zmax = 1396  # offset
    m_zmin = 1392  # offset

class CRagdollMagnet(CPointEntity):
    m_axis = 1276  # offset
    m_bDisabled = 1264  # offset
    m_force = 1272  # offset
    m_radius = 1268  # offset

class CRagdollManager(CBaseEntity):
    m_bCanTakeDamage = 1273  # offset
    m_bSaveImportant = 1272  # offset
    m_iCurrentMaxRagdollCount = 1264  # offset
    m_iMaxRagdollCount = 1268  # offset

    __metadata__ =     [
        {
            "name": "m_iCurrentMaxRagdollCount",
            "type": "NetworkVarNames",
            "type_name": "int8"
        }
    ]

class CRagdollProp(CBaseAnimGraph):
    m_allAsleep = 2872  # offset
    m_bAllowStretch = 2937  # offset
    m_bFirstCollisionAfterLaunch = 2873  # offset
    m_bHasBeenPhysgunned = 2936  # offset
    m_bShouldDeleteActivationRecord = 3000  # offset
    m_bStartDisabled = 2784  # offset
    m_flAwakeTime = 2912  # offset
    m_flBlendWeight = 2940  # offset
    m_flDefaultFadeScale = 2944  # offset
    m_flFadeOutStartTime = 2892  # offset
    m_flFadeTime = 2896  # offset
    m_flLastOriginChangeTime = 2916  # offset
    m_flLastPhysicsInfluenceTime = 2888  # offset
    m_hDamageEntity = 2876  # offset
    m_hKiller = 2880  # offset
    m_hPhysicsAttacker = 2884  # offset
    m_hRagdollSource = 2864  # offset
    m_lastUpdateTickCount = 2868  # offset
    m_ragAngles = 2840  # offset
    m_ragEnabled = 2792  # offset
    m_ragPos = 2816  # offset
    m_ragdoll = 2704  # offset
    m_ragdollMaxs = 2976  # offset
    m_ragdollMins = 2952  # offset
    m_strOriginClassName = 2920  # offset
    m_strSourceClassName = 2928  # offset
    m_vecLastOrigin = 2900  # offset

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
            "name": "m_hRagdollSource",
            "type": "NetworkVarNames",
            "type_name": "EHANDLE"
        },
        {
            "name": "m_flBlendWeight",
            "type": "NetworkVarNames",
            "type_name": "float32"
        }
    ]

class CRagdollPropAlias_physics_prop_ragdoll(CRagdollProp):
    pass

class CRagdollPropAttached(CRagdollProp):
    m_attachmentPointBoneSpace = 3032  # offset
    m_attachmentPointRagdollSpace = 3044  # offset
    m_bShouldDeleteAttachedActivationRecord = 3072  # offset
    m_bShouldDetach = 3056  # offset
    m_boneIndexAttached = 3024  # offset
    m_ragdollAttachedObjectIndex = 3028  # offset

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

class CRectLight(CBarnLight):
    m_bShowLight = 2840  # offset

    __metadata__ =     [
        {
            "name": "m_bShowLight",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CRenderComponent(CEntityComponent):
    __m_pChainEntity = 16  # offset
    m_bEnableRendering = 88  # offset
    m_bInterpolationReadyToDraw = 168  # offset
    m_bIsRenderingWithViewModels = 80  # offset
    m_nSplitscreenFlags = 84  # offset

class CRetakeGameRules:
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

class CRevertSaved(CModelPointEntity):
    m_Duration = 2036  # offset
    m_HoldTime = 2040  # offset
    m_loadTime = 2032  # offset

class CRopeKeyframe(CBaseModelEntity):
    m_RopeFlags = 2040  # offset
    m_RopeLength = 2090  # offset
    m_Slack = 2056  # offset
    m_Subdiv = 2088  # offset
    m_TextureScale = 2064  # offset
    m_Width = 2060  # offset
    m_bConstrainBetweenEndpoints = 2069  # offset
    m_bCreatedFromMapFile = 2093  # offset
    m_bEndPointValid = 2101  # offset
    m_bStartPointValid = 2100  # offset
    m_fLockedPoints = 2092  # offset
    m_flScrollSpeed = 2096  # offset
    m_hEndPoint = 2108  # offset
    m_hStartPoint = 2104  # offset
    m_iEndAttachment = 2113  # offset
    m_iNextLinkName = 2048  # offset
    m_iRopeMaterialModelIndex = 2080  # offset
    m_iStartAttachment = 2112  # offset
    m_nChangeCount = 2089  # offset
    m_nSegments = 2068  # offset
    m_strRopeMaterialModel = 2072  # offset

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
            "name": "m_RopeFlags",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        },
        {
            "name": "m_Slack",
            "type": "NetworkVarNames",
            "type_name": "int16"
        },
        {
            "name": "m_Width",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_TextureScale",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_nSegments",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_bConstrainBetweenEndpoints",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_iRopeMaterialModelIndex",
            "type": "NetworkVarNames",
            "type_name": "HMaterialStrong"
        },
        {
            "name": "m_Subdiv",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_nChangeCount",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_RopeLength",
            "type": "NetworkVarNames",
            "type_name": "int16"
        },
        {
            "name": "m_fLockedPoints",
            "type": "NetworkVarNames",
            "type_name": "uint8"
        },
        {
            "name": "m_flScrollSpeed",
            "type": "NetworkVarNames",
            "type_name": "float32"
        },
        {
            "name": "m_hStartPoint",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
        },
        {
            "name": "m_hEndPoint",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseEntity>"
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
        }
    ]

class CRopeKeyframeAlias_move_rope(CRopeKeyframe):
    pass

class CRotButton(CBaseButton):
    pass

class CRotDoor(CBaseDoor):
    m_bSolidBsp = 2688  # offset

class CRotatorTarget(CPointEntity):
    m_OnArrivedAt = 1264  # offset
    m_eSpace = 1304  # offset

class CRuleBrushEntity(CRuleEntity):
    pass

class CRuleEntity(CBaseModelEntity):
    m_iszMaster = 2032  # offset

class CRulePointEntity(CRuleEntity):
    m_Score = 2040  # offset

class CSMatchStats_t:
    m_flHealthPointsDealtTotal = 152  # offset
    m_flHealthPointsRemovedTotal = 148  # offset
    m_i1v1Count = 164  # offset
    m_i1v1Wins = 168  # offset
    m_i1v2Count = 172  # offset
    m_i1v2Wins = 176  # offset
    m_iEnemy2Ks = 124  # offset
    m_iEnemy3Ks = 112  # offset
    m_iEnemy4Ks = 108  # offset
    m_iEnemy5Ks = 104  # offset
    m_iEnemyKnifeKills = 116  # offset
    m_iEnemyTaserKills = 120  # offset
    m_iEntryCount = 180  # offset
    m_iEntryWins = 184  # offset
    m_iFlash_Count = 140  # offset
    m_iFlash_Successes = 144  # offset
    m_iUtility_Count = 128  # offset
    m_iUtility_Enemies = 136  # offset
    m_iUtility_Successes = 132  # offset
    m_nShotsFiredTotal = 156  # offset
    m_nShotsOnTargetTotal = 160  # offset

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

class CSceneEntity(CPointEntity):
    m_BusyActor = 2624  # offset
    m_OnCanceled = 1632  # offset
    m_OnCompletion = 1592  # offset
    m_OnPaused = 1672  # offset
    m_OnResumed = 1712  # offset
    m_OnStart = 1552  # offset
    m_OnTrigger = 1752  # offset
    m_bAutogenerated = 1395  # offset
    m_bAutomated = 1416  # offset
    m_bBreakOnNonIdle = 1446  # offset
    m_bCancelAtNextInterrupt = 1408  # offset
    m_bCompletedEarly = 2546  # offset
    m_bInterruptSceneFinished = 2547  # offset
    m_bInterrupted = 2545  # offset
    m_bInterruptedActorsScenes = 1445  # offset
    m_bIsPlayingBack = 1392  # offset
    m_bMultiplayer = 1394  # offset
    m_bPauseAtNextInterrupt = 1442  # offset
    m_bPaused = 1393  # offset
    m_bPausedViaInput = 1441  # offset
    m_bRestoring = 2548  # offset
    m_bSceneFinished = 1447  # offset
    m_bSceneMissing = 2544  # offset
    m_bWaitingForActor = 1443  # offset
    m_bWaitingForInterrupt = 1444  # offset
    m_bWaitingForResumeScene = 1440  # offset
    m_fPitch = 1412  # offset
    m_flAutomationDelay = 1424  # offset
    m_flAutomationTime = 1428  # offset
    m_flCurrentTime = 1400  # offset
    m_flForceClientTime = 1396  # offset
    m_flFrameTime = 1404  # offset
    m_hActivator = 2620  # offset
    m_hActor = 2616  # offset
    m_hActorList = 1448  # offset
    m_hInterruptScene = 2536  # offset
    m_hListManagers = 2576  # offset
    m_hNotifySceneCompletion = 2552  # offset
    m_hRemoveActorList = 1472  # offset
    m_hTarget1 = 1352  # offset
    m_hTarget2 = 1356  # offset
    m_hTarget3 = 1360  # offset
    m_hTarget4 = 1364  # offset
    m_hTarget5 = 1368  # offset
    m_hTarget6 = 1372  # offset
    m_hTarget7 = 1376  # offset
    m_hTarget8 = 1380  # offset
    m_hWaitingForThisResumeScene = 1436  # offset
    m_iPlayerDeathBehavior = 2628  # offset
    m_iszResumeSceneFile = 1280  # offset
    m_iszSceneFile = 1272  # offset
    m_iszSequenceName = 2608  # offset
    m_iszSoundName = 2600  # offset
    m_iszTarget1 = 1288  # offset
    m_iszTarget2 = 1296  # offset
    m_iszTarget3 = 1304  # offset
    m_iszTarget4 = 1312  # offset
    m_iszTarget5 = 1320  # offset
    m_iszTarget6 = 1328  # offset
    m_iszTarget7 = 1336  # offset
    m_iszTarget8 = 1344  # offset
    m_nAutomatedAction = 1420  # offset
    m_nInterruptCount = 2540  # offset
    m_nSceneFlushCounter = 1544  # offset
    m_nSceneStringIndex = 1548  # offset
    m_nSpeechPriority = 1432  # offset
    m_sTargetAttachment = 1384  # offset

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
            "name": "m_hActorList",
            "type": "NetworkVarNames",
            "type_name": "CHandle<CBaseFlex>"
        },
        {
            "name": "m_nSceneStringIndex",
            "type": "NetworkVarNames",
            "type_name": "uint16"
        }
    ]

class CSceneEntityAlias_logic_choreographed_scene(CSceneEntity):
    pass

class CSceneListManager(CLogicalEntity):
    m_hListManagers = 1264  # offset
    m_hScenes = 1416  # offset
    m_iszScenes = 1288  # offset

class CScriptComponent(CEntityComponent):
    m_scriptClassName = 48  # offset

class CScriptItem(CItem):
    m_MoveTypeOverride = 2904  # offset

class CScriptNavBlocker(CFuncNavBlocker):
    m_vExtent = 2056  # offset

class CScriptTriggerHurt(CTriggerHurt):
    m_vExtent = 2656  # offset

class CScriptTriggerMultiple(CTriggerMultiple):
    m_vExtent = 2536  # offset

class CScriptTriggerOnce(CTriggerOnce):
    m_vExtent = 2536  # offset

class CScriptTriggerPush(CTriggerPush):
    m_vExtent = 2552  # offset

class CScriptedSequence(CBaseEntity):
    m_ConflictResponse = 1452  # offset
    m_OnActionStartOrLoop = 1496  # offset
    m_OnBeginSequence = 1456  # offset
    m_OnCancelFailedSequence = 1656  # offset
    m_OnCancelSequence = 1616  # offset
    m_OnEndSequence = 1536  # offset
    m_OnPostIdleEndSequence = 1576  # offset
    m_OnScriptEvent = 1696  # offset
    m_bAllowCustomInterruptConditions = 1439  # offset
    m_bCanOverrideNPCState = 1353  # offset
    m_bContinueOnDeath = 1357  # offset
    m_bDisableAimingWhileMoving = 1367  # offset
    m_bDisableNPCCollisions = 1364  # offset
    m_bDisallowInterrupts = 1352  # offset
    m_bDontAddModifiers = 1366  # offset
    m_bDontCancelOtherSequences = 1444  # offset
    m_bDontRotateOther = 1348  # offset
    m_bDontTeleportAtEnd = 1354  # offset
    m_bEnsureOnNavmeshOnFinish = 1447  # offset
    m_bForceSynch = 1445  # offset
    m_bHideDebugComplaints = 1356  # offset
    m_bHighPriority = 1355  # offset
    m_bIgnoreGravity = 1363  # offset
    m_bIgnoreLookAt = 1362  # offset
    m_bIgnoreRotation = 1368  # offset
    m_bInitiatedSelfDelete = 1437  # offset
    m_bInterruptable = 1424  # offset
    m_bIsPlayingAction = 1346  # offset
    m_bIsPlayingEntry = 1345  # offset
    m_bIsPlayingPostIdle = 1347  # offset
    m_bIsPlayingPreIdle = 1344  # offset
    m_bIsRepeatable = 1349  # offset
    m_bIsTeleportingDueToMoveTo = 1438  # offset
    m_bKeepAnimgraphLockedPost = 1365  # offset
    m_bLoopActionSequence = 1359  # offset
    m_bLoopPostIdleSequence = 1360  # offset
    m_bLoopPreIdleSequence = 1358  # offset
    m_bPositionRelativeToOtherEntity = 1426  # offset
    m_bPreventUpdateYawOnFinish = 1446  # offset
    m_bShouldLeaveCorpse = 1350  # offset
    m_bSkipFadeIn = 2056  # offset
    m_bStartOnSpawn = 1351  # offset
    m_bSynchPostIdles = 1361  # offset
    m_bThinking = 1436  # offset
    m_bWaitForBeginSequence = 1408  # offset
    m_bWaitUntilMoveCompletesToStartAnimation = 1396  # offset
    m_flAngRate = 1388  # offset
    m_flMoveInterpTime = 1384  # offset
    m_flMoveSpeed = 1392  # offset
    m_flPlayAnimFadeInTime = 1380  # offset
    m_flRadius = 1372  # offset
    m_flRepeat = 1376  # offset
    m_hForcedTarget = 1440  # offset
    m_hInteractionMainEntity = 2048  # offset
    m_hNextCine = 1432  # offset
    m_hTargetEnt = 1428  # offset
    m_iPlayerDeathBehavior = 2052  # offset
    m_iszEntity = 1312  # offset
    m_iszEntry = 1264  # offset
    m_iszModifierToAddOnPlay = 1296  # offset
    m_iszNextScript = 1304  # offset
    m_iszPlay = 1280  # offset
    m_iszPostIdle = 1288  # offset
    m_iszPreIdle = 1272  # offset
    m_iszSyncGroup = 1320  # offset
    m_matOtherToMain = 2016  # offset
    m_nForcedCrouchState = 1340  # offset
    m_nHeldWeaponBehavior = 1336  # offset
    m_nMoveTo = 1328  # offset
    m_nMoveToGait = 1332  # offset
    m_nNotReadySequenceCount = 1400  # offset
    m_onDeathBehavior = 1448  # offset
    m_savedCollisionGroup = 1420  # offset
    m_savedFlags = 1416  # offset
    m_saved_effects = 1412  # offset
    m_sequenceStarted = 1425  # offset
    m_startTime = 1404  # offset

class CServerOnlyEntity(CBaseEntity):
    pass

class CServerOnlyModelEntity(CBaseModelEntity):
    pass

class CServerOnlyPointEntity(CServerOnlyEntity):
    pass

class CServerRagdollTrigger(CBaseTrigger):
    pass

class CShatterGlassShardPhysics(CPhysicsProp):
    m_ShardDesc = 3576  # offset
    m_bDebris = 3568  # offset
    m_hParentShard = 3572  # offset

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

class CShower(CModelPointEntity):
    pass

class CSimpleMarkupVolumeTagged(CMarkupVolumeTagged):
    pass

class CSingleplayRules:
    m_bSinglePlayerGameEnding = 192  # offset

class CSkeletonInstance(CGameSceneNode):
    m_bDirtyMotionType = 0  # offset
    m_bDisableSolidCollisionsForHierarchy = 1010  # offset
    m_bIsAnimationEnabled = 1008  # offset
    m_bIsGeneratingLatchedParentSpaceState = 0  # offset
    m_bUseParentRenderBounds = 1009  # offset
    m_materialGroup = 1012  # offset
    m_modelState = 368  # offset
    m_nHitboxSet = 1016  # offset

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

class CSkyCamera(CBaseEntity):
    m_bUseAngles = 1412  # offset
    m_pNext = 1416  # offset
    m_skyboxData = 1264  # offset
    m_skyboxSlotToken = 1408  # offset

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

class CSkyboxReference(CBaseEntity):
    m_hSkyCamera = 1268  # offset
    m_worldGroupId = 1264  # offset

class CSmokeGrenade(CBaseCSGrenade):
    pass

class CSmokeGrenadeProjectile(CBaseCSGrenadeProjectile):
    m_VoxelFrameData = 3192  # offset
    m_bDidGroundScorch = 12065  # offset
    m_bDidSmokeEffect = 3156  # offset
    m_bExplodeFromInferno = 12064  # offset
    m_flLastBounce = 3224  # offset
    m_fllastSimulationTime = 3228  # offset
    m_nRandomSeed = 3160  # offset
    m_nSmokeEffectTickBegin = 3152  # offset
    m_nVoxelFrameDataSize = 3216  # offset
    m_nVoxelUpdate = 3220  # offset
    m_vSmokeColor = 3164  # offset
    m_vSmokeDetonationPos = 3176  # offset

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

class CSoundAreaEntityBase(CBaseEntity):
    m_bDisabled = 1264  # offset
    m_iszSoundAreaType = 1272  # offset
    m_vPos = 1280  # offset

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

class CSoundAreaEntityOrientedBox(CSoundAreaEntityBase):
    m_vMax = 1308  # offset
    m_vMin = 1296  # offset

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

class CSoundAreaEntitySphere(CSoundAreaEntityBase):
    m_flRadius = 1296  # offset

    __metadata__ =     [
        {
            "name": "m_flRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CSoundEventAABBEntity(CSoundEventEntity):
    m_vMaxs = 1476  # offset
    m_vMins = 1464  # offset

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

class CSoundEventEntity(CBaseEntity):
    m_bSaveRestore = 1267  # offset
    m_bSavedIsPlaying = 1268  # offset
    m_bStartOnSpawn = 1264  # offset
    m_bStopOnNew = 1266  # offset
    m_bToLocalPlayer = 1265  # offset
    m_flClientCullRadius = 1376  # offset
    m_flSavedElapsedTime = 1272  # offset
    m_hSource = 1452  # offset
    m_iszAttachmentName = 1288  # offset
    m_iszSoundName = 1424  # offset
    m_iszSourceEntityName = 1280  # offset
    m_nEntityIndexSelection = 1456  # offset
    m_onGUIDChanged = 1296  # offset
    m_onSoundFinished = 1336  # offset

class CSoundEventEntityAlias_snd_event_point(CSoundEventEntity):
    pass

class CSoundEventOBBEntity(CSoundEventEntity):
    m_vMaxs = 1476  # offset
    m_vMins = 1464  # offset

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

class CSoundEventParameter(CBaseEntity):
    m_flFloatValue = 1296  # offset
    m_iszParamName = 1288  # offset

class CSoundEventPathCornerEntity(CSoundEventEntity):
    m_bPlaying = 1488  # offset
    m_flDistMaxSqr = 1480  # offset
    m_flDistanceMax = 1476  # offset
    m_flDotProductMax = 1484  # offset
    m_iCountMax = 1472  # offset
    m_iszPathCorner = 1464  # offset
    m_vecCornerPairsNetworked = 1528  # offset

    __metadata__ =     [
        {
            "name": "m_vecCornerPairsNetworked",
            "type": "NetworkVarNames",
            "type_name": "SoundeventPathCornerPairNetworked_t"
        }
    ]

class CSoundEventSphereEntity(CSoundEventEntity):
    m_flRadius = 1464  # offset

    __metadata__ =     [
        {
            "name": "m_flRadius",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CSoundOpvarSetAABBEntity(CSoundOpvarSetPointEntity):
    m_nAABBDirection = 1752  # offset
    m_vDistanceInnerMaxs = 1716  # offset
    m_vDistanceInnerMins = 1704  # offset
    m_vDistanceOuterMaxs = 1740  # offset
    m_vDistanceOuterMins = 1728  # offset
    m_vInnerMaxs = 1768  # offset
    m_vInnerMins = 1756  # offset
    m_vOuterMaxs = 1792  # offset
    m_vOuterMins = 1780  # offset

class CSoundOpvarSetAutoRoomEntity(CSoundOpvarSetPointEntity):
    m_doorwayPairs = 1728  # offset
    m_flHeightTolerance = 1756  # offset
    m_flSize = 1752  # offset
    m_flSizeSqr = 1760  # offset
    m_traceResults = 1704  # offset

class CSoundOpvarSetEntity(CBaseEntity):
    m_OpvarValueString = 1328  # offset
    m_bSetOnSpawn = 1336  # offset
    m_flOpvarValue = 1320  # offset
    m_iszOperatorName = 1296  # offset
    m_iszOpvarName = 1304  # offset
    m_iszStackName = 1288  # offset
    m_nOpvarIndex = 1316  # offset
    m_nOpvarType = 1312  # offset

class CSoundOpvarSetOBBEntity(CSoundOpvarSetAABBEntity):
    pass

class CSoundOpvarSetOBBWindEntity(CSoundOpvarSetPointBase):
    m_flWindMapMax = 1492  # offset
    m_flWindMapMin = 1488  # offset
    m_flWindMax = 1484  # offset
    m_flWindMin = 1480  # offset
    m_vDistanceMaxs = 1468  # offset
    m_vDistanceMins = 1456  # offset
    m_vMaxs = 1444  # offset
    m_vMins = 1432  # offset

class CSoundOpvarSetPathCornerEntity(CSoundOpvarSetPointEntity):
    m_flDistMaxSqr = 1732  # offset
    m_flDistMinSqr = 1728  # offset
    m_iszPathCornerEntityName = 1736  # offset

class CSoundOpvarSetPointBase(CBaseEntity):
    m_bDisabled = 1264  # offset
    m_bUseAutoCompare = 1428  # offset
    m_hSource = 1268  # offset
    m_iOpvarIndex = 1424  # offset
    m_iszOperatorName = 1408  # offset
    m_iszOpvarName = 1416  # offset
    m_iszSourceEntityName = 1296  # offset
    m_iszStackName = 1400  # offset
    m_vLastPosition = 1384  # offset

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

class CSoundOpvarSetPointEntity(CSoundOpvarSetPointBase):
    m_OnEnter = 1432  # offset
    m_OnExit = 1472  # offset
    m_bAutoDisable = 1512  # offset
    m_bReloading = 1613  # offset
    m_bSetValueOnDisable = 1612  # offset
    m_flDistanceMapMax = 1592  # offset
    m_flDistanceMapMin = 1588  # offset
    m_flDistanceMax = 1584  # offset
    m_flDistanceMin = 1580  # offset
    m_flDynamicMaximumOcclusion = 1636  # offset
    m_flOcclusionMax = 1604  # offset
    m_flOcclusionMin = 1600  # offset
    m_flOcclusionRadius = 1596  # offset
    m_flPathingDistanceNormFactor = 1656  # offset
    m_flValSetOnDisable = 1608  # offset
    m_hDynamicEntity = 1640  # offset
    m_iszDynamicEntityName = 1648  # offset
    m_nPathingSourceIndex = 1696  # offset
    m_nSimulationMode = 1616  # offset
    m_nVisibilitySamples = 1620  # offset
    m_vDynamicProxyPoint = 1624  # offset
    m_vPathingDirection = 1684  # offset
    m_vPathingListenerPos = 1672  # offset
    m_vPathingSourcePos = 1660  # offset

class CSoundStackSave(CLogicalEntity):
    m_iszStackName = 1264  # offset

class CSplineConstraint(CPhysConstraint):
    m_bEnableAngularConstraint = 1482  # offset
    m_bEnableLateralConstraint = 1480  # offset
    m_bEnableLimit = 1483  # offset
    m_bEnableVerticalConstraint = 1481  # offset
    m_bFireEventsOnPath = 1484  # offset
    m_flJointFriction = 1496  # offset
    m_flLinarDampingRatio = 1492  # offset
    m_flLinearFrequency = 1488  # offset
    m_hSplineEntity = 1468  # offset
    m_vAnchorOffsetRestore = 1456  # offset
    m_vPreSolveAnchorPos = 1536  # offset

class CSpotlightEnd(CBaseModelEntity):
    m_Radius = 2036  # offset
    m_flLightScale = 2032  # offset
    m_vSpotlightDir = 2040  # offset
    m_vSpotlightOrg = 2052  # offset

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

class CSprite(CBaseModelEntity):
    m_bWorldSpaceScale = 2088  # offset
    m_flBrightnessDuration = 2076  # offset
    m_flBrightnessTimeStart = 2128  # offset
    m_flDestScale = 2112  # offset
    m_flDieTime = 2056  # offset
    m_flFrame = 2052  # offset
    m_flGlowProxySize = 2092  # offset
    m_flHDRColorScale = 2096  # offset
    m_flLastTime = 2100  # offset
    m_flMaxFrame = 2104  # offset
    m_flScaleDuration = 2084  # offset
    m_flScaleTimeStart = 2116  # offset
    m_flSpriteFramerate = 2048  # offset
    m_flSpriteScale = 2080  # offset
    m_flStartScale = 2108  # offset
    m_hAttachedToEntity = 2040  # offset
    m_hSpriteMaterial = 2032  # offset
    m_nAttachment = 2044  # offset
    m_nBrightness = 2072  # offset
    m_nDestBrightness = 2124  # offset
    m_nSpriteHeight = 2136  # offset
    m_nSpriteWidth = 2132  # offset
    m_nStartBrightness = 2120  # offset

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

class CSpriteAlias_env_glow(CSprite):
    pass

class CSpriteOriented(CSprite):
    pass

class CTakeDamageInfoAPI:
    pass

class CTankTargetChange(CPointEntity):
    m_newTarget = 1264  # offset
    m_newTargetName = 1280  # offset

class CTankTrainAI(CPointEntity):
    m_engineSoundName = 1304  # offset
    m_hTargetEntity = 1268  # offset
    m_hTrain = 1264  # offset
    m_movementSoundName = 1312  # offset
    m_soundPlaying = 1272  # offset
    m_startSoundName = 1296  # offset
    m_targetEntityName = 1320  # offset

class CTeam(CBaseEntity):
    m_aPlayerControllers = 1264  # offset
    m_aPlayers = 1288  # offset
    m_iScore = 1312  # offset
    m_szTeamname = 1316  # offset

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
            "type_name": "CHandle<CBasePlayerPawn>"
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

class CTeamplayRules:
    pass

class CTestEffect(CBaseEntity):
    m_flBeamTime = 1464  # offset
    m_flStartTime = 1560  # offset
    m_iBeam = 1268  # offset
    m_iLoop = 1264  # offset
    m_pBeam = 1272  # offset

class CTestPulseIO(CLogicalEntity):
    m_OnVariantBool = 1304  # offset
    m_OnVariantColor = 1464  # offset
    m_OnVariantFloat = 1384  # offset
    m_OnVariantInt = 1344  # offset
    m_OnVariantString = 1424  # offset
    m_OnVariantVector = 1504  # offset
    m_OnVariantVoid = 1264  # offset
    m_bAllowEmptyInputs = 1544  # offset

class CTestPulseIOAPI:
    pass

class CTextureBasedAnimatable(CBaseModelEntity):
    m_bLoop = 2032  # offset
    m_flFPS = 2036  # offset
    m_flStartFrame = 2084  # offset
    m_flStartTime = 2080  # offset
    m_hPositionKeys = 2040  # offset
    m_hRotationKeys = 2048  # offset
    m_vAnimationBoundsMax = 2068  # offset
    m_vAnimationBoundsMin = 2056  # offset

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

class CTimerEntity(CLogicalEntity):
    m_OnTimer = 1264  # offset
    m_OnTimerHigh = 1304  # offset
    m_OnTimerLow = 1344  # offset
    m_bPauseAfterFiring = 1404  # offset
    m_bPaused = 1420  # offset
    m_bUpDownState = 1396  # offset
    m_flInitialDelay = 1388  # offset
    m_flLowerRandomBound = 1408  # offset
    m_flRefireTime = 1392  # offset
    m_flRemainingTime = 1416  # offset
    m_flUpperRandomBound = 1412  # offset
    m_iDisabled = 1384  # offset
    m_iUseRandomTime = 1400  # offset

class CTonemapController2(CBaseEntity):
    m_flAutoExposureMax = 1268  # offset
    m_flAutoExposureMin = 1264  # offset
    m_flExposureAdaptationSpeedDown = 1276  # offset
    m_flExposureAdaptationSpeedUp = 1272  # offset
    m_flTonemapEVSmoothingRange = 1280  # offset

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

class CTonemapController2Alias_env_tonemap_controller2(CTonemapController2):
    pass

class CTonemapTrigger(CBaseTrigger):
    m_hTonemapController = 2504  # offset
    m_tonemapControllerName = 2496  # offset

class CTouchExpansionComponent(CEntityComponent):
    pass

class CTriggerActiveWeaponDetect(CBaseTrigger):
    m_OnTouchedActiveWeapon = 2496  # offset
    m_iszWeaponClassName = 2536  # offset

class CTriggerBombReset(CBaseTrigger):
    pass

class CTriggerBrush(CBaseModelEntity):
    m_OnEndTouch = 2072  # offset
    m_OnStartTouch = 2032  # offset
    m_OnUse = 2112  # offset
    m_iDontMessageParent = 2156  # offset
    m_iInputFilter = 2152  # offset

class CTriggerBuoyancy(CBaseTrigger):
    m_BuoyancyHelper = 2496  # offset
    m_flFluidDensity = 2776  # offset

    __metadata__ =     [
        {
            "name": "m_flFluidDensity",
            "type": "NetworkVarNames",
            "type_name": "float"
        }
    ]

class CTriggerCallback(CBaseTrigger):
    pass

class CTriggerDetectBulletFire(CBaseTrigger):
    m_OnDetectedBulletFire = 2504  # offset
    m_bPlayerFireOnly = 2496  # offset

class CTriggerDetectExplosion(CBaseTrigger):
    m_OnDetectedExplosion = 2528  # offset

class CTriggerFan(CBaseTrigger):
    m_RampTimer = 2592  # offset
    m_bFalloff = 2584  # offset
    m_bPlayerWindblock = 2636  # offset
    m_bPushAwayFromInfoTarget = 2557  # offset
    m_bPushPlayer = 2656  # offset
    m_bPushTowardsInfoTarget = 2556  # offset
    m_bRampDown = 2657  # offset
    m_fNoiseDegrees = 2648  # offset
    m_fNoiseSpeed = 2652  # offset
    m_flForce = 2580  # offset
    m_flNPCForce = 2640  # offset
    m_flParticleForceScale = 2628  # offset
    m_flPlayerForce = 2632  # offset
    m_flRampTime = 2644  # offset
    m_flRopeForceScale = 2624  # offset
    m_hInfoFan = 2576  # offset
    m_iszInfoFan = 2616  # offset
    m_nManagerFanIdx = 2660  # offset
    m_qNoiseDelta = 2560  # offset
    m_vDirection = 2544  # offset
    m_vFanEnd = 2520  # offset
    m_vFanOrigin = 2496  # offset
    m_vFanOriginOffset = 2508  # offset
    m_vNoiseDirectionTarget = 2532  # offset

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

class CTriggerGameEvent(CBaseTrigger):
    m_strEndTouchEventName = 2504  # offset
    m_strStartTouchEventName = 2496  # offset
    m_strTriggerID = 2512  # offset

    __metadata__ =     [
        {
            "name": "m_strStartTouchEventName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_strEndTouchEventName",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        },
        {
            "name": "m_strTriggerID",
            "type": "NetworkVarNames",
            "type_name": "CUtlString"
        }
    ]

class CTriggerGravity(CBaseTrigger):
    pass

class CTriggerHostageReset(CBaseTrigger):
    pass

class CTriggerHurt(CBaseTrigger):
    m_OnHurt = 2552  # offset
    m_OnHurtPlayer = 2592  # offset
    m_bNoDmgForce = 2524  # offset
    m_bitsDamageInflict = 2516  # offset
    m_damageModel = 2520  # offset
    m_flDamage = 2500  # offset
    m_flDamageCap = 2504  # offset
    m_flForgivenessDelay = 2512  # offset
    m_flLastDmgTime = 2508  # offset
    m_flOriginalDamage = 2496  # offset
    m_hurtEntities = 2632  # offset
    m_hurtThinkPeriod = 2544  # offset
    m_thinkAlways = 2540  # offset
    m_vDamageForce = 2528  # offset

class CTriggerImpact(CTriggerMultiple):
    m_flMagnitude = 2536  # offset
    m_flNoise = 2540  # offset
    m_flViewkick = 2544  # offset
    m_pOutputForce = 2552  # offset

class CTriggerLerpObject(CBaseTrigger):
    m_OnDetached = 2664  # offset
    m_OnLerpFinished = 2624  # offset
    m_OnLerpStarted = 2584  # offset
    m_bAttachTouchingObject = 2576  # offset
    m_bLerpRestoreMoveType = 2528  # offset
    m_bSingleLerpObject = 2529  # offset
    m_flLerpDuration = 2524  # offset
    m_hEntityToWaitForDisconnect = 2580  # offset
    m_hLerpTarget = 2504  # offset
    m_hLerpTargetAttachment = 2520  # offset
    m_iszLerpEffect = 2560  # offset
    m_iszLerpSound = 2568  # offset
    m_iszLerpTarget = 2496  # offset
    m_iszLerpTargetAttachment = 2512  # offset
    m_vecLerpingObjects = 2536  # offset

class CTriggerLook(CTriggerOnce):
    m_OnEndLook = 2648  # offset
    m_OnStartLook = 2608  # offset
    m_OnTimeout = 2568  # offset
    m_b2DFOV = 2562  # offset
    m_bIsLooking = 2561  # offset
    m_bTestAllVisibleOcclusion = 2565  # offset
    m_bTestOcclusion = 2564  # offset
    m_bTimeoutFired = 2560  # offset
    m_bUseVelocity = 2563  # offset
    m_flFieldOfView = 2540  # offset
    m_flLookTime = 2544  # offset
    m_flLookTimeLast = 2552  # offset
    m_flLookTimeTotal = 2548  # offset
    m_flTimeoutDuration = 2556  # offset
    m_hLookTarget = 2536  # offset

    __metadata__ =     [
        {
            "name": "m_bTestOcclusion",
            "type": "NetworkVarNames",
            "type_name": "bool"
        },
        {
            "name": "m_bTestAllVisibleOcclusion",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CTriggerMultiple(CBaseTrigger):
    m_OnTrigger = 2496  # offset

class CTriggerOnce(CTriggerMultiple):
    pass

class CTriggerPhysics(CBaseTrigger):
    m_angularDamping = 2528  # offset
    m_angularLimit = 2524  # offset
    m_bCollapseToForcePoint = 2556  # offset
    m_bConvertToDebrisWhenPossible = 2584  # offset
    m_flDampingRatio = 2540  # offset
    m_flFrequency = 2536  # offset
    m_gravityScale = 2512  # offset
    m_linearDamping = 2520  # offset
    m_linearForce = 2532  # offset
    m_linearLimit = 2516  # offset
    m_vecLinearForceDirection = 2572  # offset
    m_vecLinearForcePointAt = 2544  # offset
    m_vecLinearForcePointAtWorld = 2560  # offset

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

class CTriggerProximity(CBaseTrigger):
    m_NearestEntityDistance = 2520  # offset
    m_fRadius = 2512  # offset
    m_hMeasureTarget = 2496  # offset
    m_iszMeasureTarget = 2504  # offset
    m_nTouchers = 2516  # offset

class CTriggerPush(CBaseTrigger):
    m_PathSimple = 2536  # offset
    m_angPushEntitySpace = 2496  # offset
    m_bTriggerOnStartTouch = 2520  # offset
    m_bUsePathSimple = 2521  # offset
    m_iszPathSimpleName = 2528  # offset
    m_splinePushType = 2544  # offset
    m_vecPushDirEntitySpace = 2508  # offset

class CTriggerRemove(CBaseTrigger):
    m_OnRemove = 2496  # offset

class CTriggerSave(CBaseTrigger):
    m_bForceNewLevelUnit = 2496  # offset
    m_fDangerousTimer = 2500  # offset
    m_minHitPoints = 2504  # offset

class CTriggerSndSosOpvar(CBaseTrigger):
    m_VecNormPos = 3340  # offset
    m_bVolIs2D = 2568  # offset
    m_flCenterSize = 2532  # offset
    m_flMaxVal = 2540  # offset
    m_flMinVal = 2536  # offset
    m_flNormCenterSize = 3352  # offset
    m_flPosition = 2520  # offset
    m_hTouchingPlayers = 2496  # offset
    m_operatorName = 2560  # offset
    m_operatorNameChar = 3081  # offset
    m_opvarName = 2544  # offset
    m_opvarNameChar = 2569  # offset
    m_stackName = 2552  # offset
    m_stackNameChar = 2825  # offset

class CTriggerSoundscape(CBaseTrigger):
    m_SoundscapeName = 2504  # offset
    m_hSoundscape = 2496  # offset
    m_spectators = 2512  # offset

class CTriggerTeleport(CBaseTrigger):
    m_bCheckDestIfClearForPlayer = 2506  # offset
    m_bMirrorPlayer = 2505  # offset
    m_bUseLandmarkAngles = 2504  # offset
    m_iLandmark = 2496  # offset

class CTriggerToggleSave(CBaseTrigger):
    pass

class CTriggerVolume(CBaseModelEntity):
    m_hFilter = 2040  # offset
    m_iFilterName = 2032  # offset

class CVoteController(CBaseEntity):
    m_VoteOptions = 1672  # offset
    m_acceptingVotesTimer = 1304  # offset
    m_bIsYesNoVote = 1296  # offset
    m_executeCommandTimer = 1328  # offset
    m_iActiveIssueIndex = 1264  # offset
    m_iOnlyTeamToVote = 1268  # offset
    m_nHighestCountIndex = 1640  # offset
    m_nPotentialVotes = 1292  # offset
    m_nVoteOptionCount = 1272  # offset
    m_nVotesCast = 1376  # offset
    m_playerHoldingVote = 1632  # offset
    m_playerOverrideForVote = 1636  # offset
    m_potentialIssues = 1648  # offset
    m_resetVoteTimer = 1352  # offset

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

class CWaterBullet(CBaseAnimGraph):
    pass

class CWeaponAWP(CCSWeaponBaseGun):
    pass

class CWeaponAug(CCSWeaponBaseGun):
    pass

class CWeaponBaseItem(CCSWeaponBase):
    m_bRedraw = 4521  # offset
    m_bSequenceInProgress = 4520  # offset

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

class CWeaponBizon(CCSWeaponBaseGun):
    pass

class CWeaponCZ75a(CCSWeaponBaseGun):
    m_bMagazineRemoved = 4552  # offset

    __metadata__ =     [
        {
            "name": "m_bMagazineRemoved",
            "type": "NetworkVarNames",
            "type_name": "bool"
        }
    ]

class CWeaponElite(CCSWeaponBaseGun):
    pass

class CWeaponFamas(CCSWeaponBaseGun):
    pass

class CWeaponFiveSeven(CCSWeaponBaseGun):
    pass

class CWeaponG3SG1(CCSWeaponBaseGun):
    pass

class CWeaponGalilAR(CCSWeaponBaseGun):
    pass

class CWeaponGlock(CCSWeaponBaseGun):
    pass

class CWeaponHKP2000(CCSWeaponBaseGun):
    pass

class CWeaponM249(CCSWeaponBaseGun):
    pass

class CWeaponM4A1(CCSWeaponBaseGun):
    pass

class CWeaponM4A1Silencer(CCSWeaponBaseGun):
    pass

class CWeaponMAC10(CCSWeaponBaseGun):
    pass

class CWeaponMP5SD(CCSWeaponBaseGun):
    pass

class CWeaponMP7(CCSWeaponBaseGun):
    pass

class CWeaponMP9(CCSWeaponBaseGun):
    pass

class CWeaponMag7(CCSWeaponBaseGun):
    pass

class CWeaponNOVA(CCSWeaponBaseShotgun):
    pass

class CWeaponNegev(CCSWeaponBaseGun):
    pass

class CWeaponP250(CCSWeaponBaseGun):
    pass

class CWeaponP90(CCSWeaponBaseGun):
    pass

class CWeaponRevolver(CCSWeaponBaseGun):
    pass

class CWeaponSCAR20(CCSWeaponBaseGun):
    pass

class CWeaponSG556(CCSWeaponBaseGun):
    pass

class CWeaponSSG08(CCSWeaponBaseGun):
    pass

class CWeaponSawedoff(CCSWeaponBaseShotgun):
    pass

class CWeaponTaser(CCSWeaponBaseGun):
    m_fFireTime = 4552  # offset
    m_nLastAttackTick = 4556  # offset

    __metadata__ =     [
        {
            "name": "m_fFireTime",
            "type": "NetworkVarNames",
            "type_name": "GameTime_t"
        }
    ]

class CWeaponTec9(CCSWeaponBaseGun):
    pass

class CWeaponUMP45(CCSWeaponBaseGun):
    pass

class CWeaponUSPSilencer(CCSWeaponBaseGun):
    pass

class CWeaponXM1014(CCSWeaponBaseShotgun):
    pass

class CWorld(CBaseModelEntity):
    pass

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
    m_iDamageType = 1352  # offset

class FilterHealth(CBaseFilter):
    m_bAdrenalineActive = 1352  # offset
    m_iHealthMax = 1360  # offset
    m_iHealthMin = 1356  # offset

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

class SpawnPoint(CServerOnlyPointEntity):
    m_bEnabled = 1268  # offset
    m_iPriority = 1264  # offset
    m_nType = 1272  # offset

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

class fogplayerparams_t:
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