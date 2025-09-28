// dumped by shxdows dumper (csdump)
# dumped by shxdows dumper (csdump) 

from enum import Enum

class AggregateInstanceStream_t(Enum):
    AGGREGATE_INSTANCE_STREAM_LIGHTMAPUV_UNORM16 = 1
    AGGREGATE_INSTANCE_STREAM_NONE = 0
    AGGREGATE_INSTANCE_STREAM_VERTEXBLEND_UNORM8 = 4
    AGGREGATE_INSTANCE_STREAM_VERTEXTINT_UNORM8 = 2

class ObjectTypeFlags_t(Enum):
    OBJECT_TYPE_BAKED_GEOMETRY = 131072
    OBJECT_TYPE_BLOCK_LIGHT = 16
    OBJECT_TYPE_DISABLED_IN_LOW_QUALITY = 128
    OBJECT_TYPE_DISABLE_VIS_CULLING = 65536
    OBJECT_TYPE_MODEL = 8
    OBJECT_TYPE_MODEL_HAS_LODS = 2048
    OBJECT_TYPE_NONE = 0
    OBJECT_TYPE_NO_SHADOWS = 32
    OBJECT_TYPE_NO_SUN_SHADOWS = 256
    OBJECT_TYPE_OVERLAY = 8192
    OBJECT_TYPE_PRECOMPUTED_VISMEMBERS = 16384
    OBJECT_TYPE_RENDER_TO_CUBEMAPS = 1024
    OBJECT_TYPE_RENDER_WITH_DYNAMIC = 512
    OBJECT_TYPE_STATIC_CUBE_MAP = 32768
    OBJECT_TYPE_WORLDSPACE_TEXURE_BLEND = 64

class AggregateInstanceStreamOnDiskData_t:
    m_BufferData = 8  # offset
    m_DecodedSize = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AggregateLODSetup_t:
    m_fMaxObjectScale = 12  # offset
    m_fSwitchDistances = 16  # offset
    m_vLODOrigin = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AggregateMeshInfo_t:
    m_bHasTransform = 5  # offset
    m_instanceStreams = 32  # offset
    m_nDrawCallIndex = 8  # offset
    m_nInstanceStreamOffset = 24  # offset
    m_nLODGroupMask = 6  # offset
    m_nLODSetupIndex = 10  # offset
    m_nLightProbeVolumePrecomputedHandshake = 20  # offset
    m_nVertexAlbedoStreamOffset = 28  # offset
    m_nVisClusterMemberCount = 4  # offset
    m_nVisClusterMemberOffset = 0  # offset
    m_objectFlags = 16  # offset
    m_vTintColor = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AggregateSceneObject_t:
    m_aggregateMeshes = 16  # offset
    m_allFlags = 0  # offset
    m_anyFlags = 4  # offset
    m_fragmentTransforms = 88  # offset
    m_instanceStream = 10  # offset
    m_lodSetups = 40  # offset
    m_nLayer = 8  # offset
    m_renderableModel = 112  # offset
    m_vertexAlbedoStream = 12  # offset
    m_visClusterMembership = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class AggregateVertexAlbedoStreamOnDiskData_t:
    m_BufferData = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class BakedLightingInfo_t:
    m_bBakedShadowsGamma20 = 17  # offset
    m_bCompressionEnabled = 18  # offset
    m_bHasLightmaps = 16  # offset
    m_bSHLightmaps = 19  # offset
    m_bakedShadows = 48  # offset
    m_lightMaps = 24  # offset
    m_nChartPackIterations = 20  # offset
    m_nLightmapGameVersionNumber = 4  # offset
    m_nLightmapVersionNumber = 0  # offset
    m_nVradQuality = 21  # offset
    m_vLightmapUvScale = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class BakedLightingInfo_t__BakedShadowAssignment_t:
    m_nLightHash = 0  # offset
    m_nMapHash = 4  # offset
    m_nShadowChannel = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class BaseSceneObjectOverride_t:
    m_nSceneObjectIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CVoxelVisibility:
    m_EnclosedClusterListBlock = 124  # offset
    m_EnclosedClustersBlock = 132  # offset
    m_MasksBlock = 140  # offset
    m_NodeBlock = 108  # offset
    m_RegionBlock = 116  # offset
    m_flGridSize = 96  # offset
    m_nBaseClusterCount = 64  # offset
    m_nPVSBytesPerCluster = 68  # offset
    m_nSkyVisibilityCluster = 100  # offset
    m_nSunVisibilityCluster = 104  # offset
    m_nVisBlocks = 148  # offset
    m_vMaxBounds = 84  # offset
    m_vMinBounds = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ClutterSceneObject_t:
    m_Bounds = 0  # offset
    m_flBeginCullSize = 164  # offset
    m_flEndCullSize = 168  # offset
    m_flags = 24  # offset
    m_instancePositions = 32  # offset
    m_instanceScales = 80  # offset
    m_instanceTintSrgb = 104  # offset
    m_materialGroup = 160  # offset
    m_nLayer = 28  # offset
    m_renderableModel = 152  # offset
    m_tiles = 128  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ClutterTile_t:
    m_BoundsWs = 8  # offset
    m_nFirstInstance = 0  # offset
    m_nLastInstance = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class EntityIOConnectionData_t:
    m_flDelay = 40  # offset
    m_inputName = 24  # offset
    m_nTimesToFire = 44  # offset
    m_outputName = 0  # offset
    m_overrideParam = 32  # offset
    m_paramMap = 48  # offset
    m_targetName = 16  # offset
    m_targetType = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class EntityKeyValueData_t:
    m_connections = 8  # offset
    m_keyValuesData = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class ExtraVertexStreamOverride_t:
    m_extraBufferBinding = 16  # offset
    m_nAdditionalMeshDrawPrimitiveFlags = 12  # offset
    m_nDrawCallIndex = 8  # offset
    m_nSubSceneObject = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class InfoForResourceTypeVMapResourceData_t:
    pass

    __metadata__ =     [
        {
            "name": "MResourceTypeForInfoType",
            "type": "Unknown"
        }
    ]

class MaterialOverride_t:
    m_nDrawCallIndex = 8  # offset
    m_nSubSceneObject = 4  # offset
    m_pMaterial = 16  # offset
    m_vLinearTintColor = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class NodeData_t:
    m_ChildNodeIndices = 48  # offset
    m_flMinimumDistance = 40  # offset
    m_nParent = 0  # offset
    m_vMaxBounds = 28  # offset
    m_vMinBounds = 16  # offset
    m_vOrigin = 4  # offset
    m_worldNodePrefix = 72  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PermEntityLumpData_t:
    m_childLumps = 16  # offset
    m_entityKeyValues = 40  # offset
    m_name = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SceneObject_t:
    m_flFadeEndDistance = 56  # offset
    m_flFadeStartDistance = 52  # offset
    m_nCubeMapPrecomputedHandshake = 108  # offset
    m_nLODOverride = 106  # offset
    m_nLightProbeVolumePrecomputedHandshake = 112  # offset
    m_nObjectID = 0  # offset
    m_nObjectTypeFlags = 88  # offset
    m_nOverlayRenderOrder = 104  # offset
    m_renderable = 128  # offset
    m_renderableModel = 120  # offset
    m_skin = 80  # offset
    m_vLightingOrigin = 92  # offset
    m_vTintColor = 60  # offset
    m_vTransform = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VMapResourceData_t:
    pass

class VoxelVisBlockOffset_t:
    m_nElementCount = 4  # offset
    m_nOffset = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class WorldBuilderParams_t:
    m_bAggregateInstanceStreams = 5  # offset
    m_bBuildBakedLighting = 4  # offset
    m_bakedLightingInfo = 8  # offset
    m_flMinDrawVolumeSize = 0  # offset
    m_nCompileFingerprint = 88  # offset
    m_nCompileTimestamp = 80  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class WorldNodeOnDiskBufferData_t:
    m_inputLayoutFields = 8  # offset
    m_nElementCount = 0  # offset
    m_nElementSizeInBytes = 4  # offset
    m_pData = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class WorldNode_t:
    m_aggregateInstanceStreams = 168  # offset
    m_aggregateSceneObjects = 48  # offset
    m_bHasBakedGeometryFlag = 344  # offset
    m_clutterSceneObjects = 72  # offset
    m_extraVertexStreamOverrides = 96  # offset
    m_extraVertexStreams = 144  # offset
    m_grassFileName = 264  # offset
    m_layerNames = 216  # offset
    m_materialOverrides = 120  # offset
    m_nodeLightingInfo = 272  # offset
    m_sceneObjectLayerIndices = 240  # offset
    m_sceneObjects = 0  # offset
    m_vertexAlbedoStreams = 192  # offset
    m_visClusterMembership = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class World_t:
    m_builderParams = 0  # offset
    m_entityLumps = 192  # offset
    m_worldLightingInfo = 120  # offset
    m_worldNodes = 96  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

