# dumped by shxdows dumper (csdump)

from enum import Enum

class BloomBlendMode_t(Enum):
    BLOOM_BLEND_ADD = 0
    BLOOM_BLEND_BLUR = 2
    BLOOM_BLEND_SCREEN = 1

class HorizJustification_e(Enum):
    HORIZ_JUSTIFICATION_CENTER = 1
    HORIZ_JUSTIFICATION_LEFT = 0
    HORIZ_JUSTIFICATION_NONE = 3
    HORIZ_JUSTIFICATION_RIGHT = 2

class LayoutPositionType_e(Enum):
    LAYOUTPOSITIONTYPE_FRACTIONAL = 1
    LAYOUTPOSITIONTYPE_NONE = 2
    LAYOUTPOSITIONTYPE_VIEWPORT_RELATIVE = 0

class VertJustification_e(Enum):
    VERT_JUSTIFICATION_BOTTOM = 2
    VERT_JUSTIFICATION_CENTER = 1
    VERT_JUSTIFICATION_NONE = 3
    VERT_JUSTIFICATION_TOP = 0

class ViewFadeMode_t(Enum):
    VIEW_FADE_CONSTANT_COLOR = 0
    VIEW_FADE_MOD2X = 2
    VIEW_FADE_MODULATE = 1

class MaterialParamBuffer_t:
    m_value = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialParamFloat_t:
    m_flValue = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialParamInt_t:
    m_nValue = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialParamString_t:
    m_value = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialParamTexture_t:
    m_pValue = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialParamVector_t:
    m_value = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialParam_t:
    m_name = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class MaterialResourceData_t:
    m_dynamicParams = 112  # offset
    m_dynamicTextureParams = 136  # offset
    m_floatAttributes = 184  # offset
    m_floatParams = 40  # offset
    m_intAttributes = 160  # offset
    m_intParams = 16  # offset
    m_materialName = 0  # offset
    m_renderAttributesUsed = 280  # offset
    m_shaderName = 8  # offset
    m_stringAttributes = 256  # offset
    m_textureAttributes = 232  # offset
    m_textureParams = 88  # offset
    m_vectorAttributes = 208  # offset
    m_vectorParams = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PostProcessingBloomParameters_t:
    m_blendMode = 0  # offset
    m_flBloomStartValue = 28  # offset
    m_flBloomStrength = 4  # offset
    m_flBloomThreshold = 16  # offset
    m_flBloomThresholdWidth = 20  # offset
    m_flBlurBloomStrength = 12  # offset
    m_flBlurWeight = 56  # offset
    m_flComputeBloomEffectsScale = 44  # offset
    m_flComputeBloomLensDirtBlackLevel = 52  # offset
    m_flComputeBloomLensDirtStrength = 48  # offset
    m_flComputeBloomRadius = 40  # offset
    m_flComputeBloomStrength = 32  # offset
    m_flComputeBloomThreshold = 36  # offset
    m_flScreenBloomStrength = 8  # offset
    m_flSkyboxBloomStrength = 24  # offset
    m_vBlurTint = 76  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PostProcessingFogScatteringParameters_t:
    m_fCubemapScale = 8  # offset
    m_fGradientScale = 16  # offset
    m_fRadius = 0  # offset
    m_fScale = 4  # offset
    m_fVolumetricScale = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PostProcessingLocalContrastParameters_t:
    m_flLocalContrastEdgeStrength = 4  # offset
    m_flLocalContrastStrength = 0  # offset
    m_flLocalContrastVignetteBlur = 16  # offset
    m_flLocalContrastVignetteEnd = 12  # offset
    m_flLocalContrastVignetteStart = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PostProcessingResource_t:
    m_bHasBloomParams = 64  # offset
    m_bHasColorCorrection = 288  # offset
    m_bHasFogScatteringParams = 289  # offset
    m_bHasLocalContrastParams = 244  # offset
    m_bHasTonemapParams = 0  # offset
    m_bHasVignetteParams = 204  # offset
    m_bloomParams = 68  # offset
    m_colorCorrectionVolumeData = 272  # offset
    m_fogScatteringParams = 292  # offset
    m_localConstrastParams = 248  # offset
    m_nColorCorrectionVolumeDim = 268  # offset
    m_toneMapParams = 4  # offset
    m_vignetteParams = 208  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PostProcessingTonemapParameters_t:
    m_flExposureBias = 0  # offset
    m_flExposureBiasHighlights = 40  # offset
    m_flExposureBiasShadows = 36  # offset
    m_flLinearAngle = 12  # offset
    m_flLinearStrength = 8  # offset
    m_flLuminanceSource = 32  # offset
    m_flMaxHighlightLum = 56  # offset
    m_flMaxShadowLum = 48  # offset
    m_flMinHighlightLum = 52  # offset
    m_flMinShadowLum = 44  # offset
    m_flShoulderStrength = 4  # offset
    m_flToeDenom = 24  # offset
    m_flToeNum = 20  # offset
    m_flToeStrength = 16  # offset
    m_flWhitePoint = 28  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PostProcessingVignetteParameters_t:
    m_flFeather = 20  # offset
    m_flRadius = 12  # offset
    m_flRoundness = 16  # offset
    m_flVignetteStrength = 0  # offset
    m_vCenter = 4  # offset
    m_vColorTint = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]