# dumped by shxdows dumper (csdump)

from enum import Enum

class DisableShadows_t(Enum):
    kDisableShadows_All = 1
    kDisableShadows_Baked = 2
    kDisableShadows_None = 0
    kDisableShadows_Realtime = 3

class CSSDSEndFrameViewInfo:
    m_ViewName = 8  # offset
    m_nViewId = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_EndFrame:
    m_Views = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_LayerBase:
    m_LayerName = 32  # offset
    m_ViewName = 16  # offset
    m_displayText = 40  # offset
    m_nLayerId = 24  # offset
    m_viewId = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_PostLayer:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_PreLayer:
    pass

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_ViewRender:
    m_ViewName = 16  # offset
    m_viewId = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_ViewTarget:
    m_Name = 0  # offset
    m_TextureId = 8  # offset
    m_nDepth = 36  # offset
    m_nFormat = 44  # offset
    m_nHeight = 20  # offset
    m_nMultisampleNumSamples = 40  # offset
    m_nNumMipLevels = 32  # offset
    m_nRequestedHeight = 28  # offset
    m_nRequestedWidth = 24  # offset
    m_nWidth = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CSSDSMsg_ViewTargetList:
    m_Targets = 24  # offset
    m_ViewName = 16  # offset
    m_viewId = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class SceneViewId_t:
    m_nFrameCount = 8  # offset
    m_nViewId = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]