# dumped by shxdows dumper (csdump)

from enum import Enum

class InputLayoutVariation_t(Enum):
    INPUT_LAYOUT_VARIATION_DEFAULT = 0
    INPUT_LAYOUT_VARIATION_MAX = 3
    INPUT_LAYOUT_VARIATION_STREAM1_INSTANCEID = 1
    INPUT_LAYOUT_VARIATION_STREAM1_INSTANCEID_MORPH_VERT_ID = 2

class RenderBufferFlags_t(Enum):
    RENDER_BUFFER_ACCELERATION_STRUCTURE = 512
    RENDER_BUFFER_BYTEADDRESS_BUFFER = 16
    RENDER_BUFFER_POOL_ALLOCATED = 2048
    RENDER_BUFFER_SHADER_BINDING_TABLE = 1024
    RENDER_BUFFER_STRUCTURED_BUFFER = 32
    RENDER_BUFFER_UAV_DRAW_INDIRECT_ARGS = 256
    RENDER_BUFFER_USAGE_CONDITIONAL_RENDERING = 4096
    RENDER_BUFFER_USAGE_INDEX_BUFFER = 2
    RENDER_BUFFER_USAGE_NONE = 0
    RENDER_BUFFER_USAGE_SHADER_RESOURCE = 4
    RENDER_BUFFER_USAGE_UNORDERED_ACCESS = 8
    RENDER_BUFFER_USAGE_VERTEX_BUFFER = 1

class RenderMultisampleType_t(Enum):
    RENDER_MULTISAMPLE_16X = 5
    RENDER_MULTISAMPLE_2X = 1
    RENDER_MULTISAMPLE_4X = 2
    RENDER_MULTISAMPLE_6X = 3
    RENDER_MULTISAMPLE_8X = 4
    RENDER_MULTISAMPLE_INVALID = -1
    RENDER_MULTISAMPLE_NONE = 0
    RENDER_MULTISAMPLE_TYPE_COUNT = 6

class RenderPrimitiveType_t(Enum):
    RENDER_PRIM_COMPUTE_SHADER = 11
    RENDER_PRIM_HETEROGENOUS = 10
    RENDER_PRIM_INSTANCED_QUADS = 9
    RENDER_PRIM_LINES = 1
    RENDER_PRIM_LINES_WITH_ADJACENCY = 2
    RENDER_PRIM_LINE_STRIP = 3
    RENDER_PRIM_LINE_STRIP_WITH_ADJACENCY = 4
    RENDER_PRIM_MESH_SHADER = 12
    RENDER_PRIM_POINTS = 0
    RENDER_PRIM_TRIANGLES = 5
    RENDER_PRIM_TRIANGLES_WITH_ADJACENCY = 6
    RENDER_PRIM_TRIANGLE_STRIP = 7
    RENDER_PRIM_TRIANGLE_STRIP_WITH_ADJACENCY = 8
    RENDER_PRIM_TYPE_COUNT = 13

class RenderSlotType_t(Enum):
    RENDER_SLOT_INVALID = -1
    RENDER_SLOT_PER_INSTANCE = 1
    RENDER_SLOT_PER_VERTEX = 0

class RsComparison_t(Enum):
    RS_CMP_ALWAYS = 7
    RS_CMP_EQUAL = 2
    RS_CMP_GREATER = 4
    RS_CMP_GREATER_EQUAL = 6
    RS_CMP_LESS = 1
    RS_CMP_LESS_EQUAL = 3
    RS_CMP_NEVER = 0
    RS_CMP_NOT_EQUAL = 5

class RsCullMode_t(Enum):
    RS_CULL_BACK = 1
    RS_CULL_FRONT = 2
    RS_CULL_NONE = 0

class RsFillMode_t(Enum):
    RS_FILL_SOLID = 0
    RS_FILL_WIREFRAME = 1

class RenderInputLayoutField_t:
    m_nOffset = 40  # offset
    m_nSemanticIndex = 32  # offset
    m_nSlot = 42  # offset
    m_nSlotType = 43  # offset
    m_pSemanticName = 0  # offset
    m_szShaderSemantic = 44  # offset

class RsBlendStateDesc_t:
    m_bAlphaToCoverageEnable = 0  # offset
    m_bIndependentBlendEnable = 0  # offset
    m_blendEnableBits = 28  # offset
    m_blendOpAlphaBits = 24  # offset
    m_blendOpBits = 0  # offset
    m_destBlendAlphaBits = 12  # offset
    m_destBlendBits = 4  # offset
    m_renderTargetWriteMaskBits = 16  # offset
    m_srcBlendAlphaBits = 8  # offset
    m_srcBlendBits = 0  # offset
    m_srgbWriteEnableBits = 29  # offset

class RsDepthStencilStateDesc_t:
    m_bDepthTestEnable = 0  # offset
    m_bDepthWriteEnable = 0  # offset
    m_depthFunc = 1  # offset
    m_stencilState = 2  # offset

class RsRasterizerStateDesc_t:
    m_bDepthClipEnable = 2  # offset
    m_bMultisampleEnable = 3  # offset
    m_flDepthBiasClamp = 8  # offset
    m_flSlopeScaledDepthBias = 12  # offset
    m_nCullMode = 1  # offset
    m_nDepthBias = 4  # offset
    m_nFillMode = 0  # offset

class RsStencilStateDesc_t:
    m_bStencilEnable = 0  # offset
    m_backStencilDepthFailOp = 0  # offset
    m_backStencilFailOp = 0  # offset
    m_backStencilFunc = 0  # offset
    m_backStencilPassOp = 0  # offset
    m_frontStencilDepthFailOp = 0  # offset
    m_frontStencilFailOp = 0  # offset
    m_frontStencilFunc = 0  # offset
    m_frontStencilPassOp = 0  # offset
    m_nStencilReadMask = 4  # offset
    m_nStencilWriteMask = 5  # offset

class SheetSequenceIntegerId_t:
    m_Value = 0  # offset

class VsInputSignatureElement_t:
    m_nD3DSemanticIndex = 192  # offset
    m_pD3DSemanticName = 128  # offset
    m_pName = 0  # offset
    m_pSemantic = 64  # offset

class VsInputSignature_t:
    m_depth_elems = 24  # offset
    m_elems = 0  # offset

