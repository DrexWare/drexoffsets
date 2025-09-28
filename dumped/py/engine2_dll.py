// dumped by shxdows dumper (csdump)
# dumped by shxdows dumper (csdump) 

from enum import Enum

class EntityDormancyType_t(Enum):
    ENTITY_DORMANT = 1
    ENTITY_NOT_DORMANT = 0
    ENTITY_SUSPENDED = 2

class EntityIOTargetType_t(Enum):
    ENTITY_IO_TARGET_EHANDLE = 6
    ENTITY_IO_TARGET_ENTITYNAME = 2
    ENTITY_IO_TARGET_ENTITYNAME_OR_CLASSNAME = 7
    ENTITY_IO_TARGET_INVALID = -1

class CEmptyEntityInstance:
    pass

class CEntityComponentHelper:
    m_flags = 8  # offset
    m_nPriority = 24  # offset
    m_pInfo = 16  # offset
    m_pNext = 32  # offset

class CEntityIOOutput:
    m_Value = 24  # offset

class CNetworkVarChainer:
    m_PathIndex = 32  # offset

class CVariantDefaultAllocator:
    pass

class EngineLoopState_t:
    m_nPlatWindowHeight = 28  # offset
    m_nPlatWindowWidth = 24  # offset
    m_nRenderHeight = 36  # offset
    m_nRenderWidth = 32  # offset

class EntComponentInfo_t:
    m_nFlags = 36  # offset
    m_nRuntimeIndex = 32  # offset
    m_pBaseClassComponentHelper = 96  # offset
    m_pCPPClassname = 8  # offset
    m_pName = 0  # offset
    m_pNetworkDataReferencedDescription = 16  # offset
    m_pNetworkDataReferencedPtrPropDescription = 24  # offset

class EntInput_t:
    pass

class EntOutput_t:
    pass

class EventAdvanceTick_t:
    m_nCurrentTick = 48  # offset
    m_nCurrentTickThisFrame = 52  # offset
    m_nTotalTicks = 60  # offset
    m_nTotalTicksThisFrame = 56  # offset

class EventAppShutdown_t:
    m_nDummy0 = 0  # offset

class EventClientAdvanceNonRenderedFrame_t:
    pass

class EventClientAdvanceTick_t:
    pass

class EventClientFrameSimulate_t:
    m_LoopState = 0  # offset
    m_bScheduleSendTickPacket = 48  # offset
    m_flFrameTime = 44  # offset
    m_flRealTime = 40  # offset

class EventClientOutput_t:
    m_LoopState = 0  # offset
    m_bRenderOnly = 52  # offset
    m_flRealTime = 44  # offset
    m_flRenderFrameTimeUnbounded = 48  # offset
    m_flRenderTime = 40  # offset

class EventClientPauseSimulate_t:
    pass

class EventClientPollInput_t:
    m_LoopState = 0  # offset
    m_flRealTime = 40  # offset

class EventClientPollNetworking_t:
    m_nTickCount = 0  # offset

class EventClientPostAdvanceTick_t:
    pass

class EventClientPostOutput_t:
    m_LoopState = 0  # offset
    m_bRenderOnly = 56  # offset
    m_flRenderFrameTime = 48  # offset
    m_flRenderFrameTimeUnbounded = 52  # offset
    m_flRenderTime = 40  # offset

class EventClientPostSimulate_t:
    pass

class EventClientPreOutput_t:
    m_LoopState = 0  # offset
    m_bRenderOnly = 68  # offset
    m_flRealTime = 64  # offset
    m_flRenderFrameTime = 48  # offset
    m_flRenderFrameTimeUnbounded = 56  # offset
    m_flRenderTime = 40  # offset

class EventClientPreSimulate_t:
    pass

class EventClientProcessGameInput_t:
    m_LoopState = 0  # offset
    m_flFrameTime = 44  # offset
    m_flRealTime = 40  # offset

class EventClientProcessInput_t:
    m_LoopState = 0  # offset
    m_flRealTime = 40  # offset
    m_flTickInterval = 44  # offset
    m_flTickStartTime = 48  # offset

class EventClientProcessNetworking_t:
    m_nTickCount = 0  # offset

class EventClientSceneSystemThreadStateChange_t:
    m_bThreadsActive = 0  # offset

class EventClientSimulate_t:
    pass

class EventFrameBoundary_t:
    m_flFrameTime = 0  # offset

class EventModInitialized_t:
    pass

class EventPostAdvanceTick_t:
    m_nCurrentTick = 48  # offset
    m_nCurrentTickThisFrame = 52  # offset
    m_nTotalTicks = 60  # offset
    m_nTotalTicksThisFrame = 56  # offset

class EventPostDataUpdate_t:
    m_nCount = 0  # offset

class EventPreDataUpdate_t:
    m_nCount = 0  # offset

class EventProfileStorageAvailable_t:
    m_nSplitScreenSlot = 0  # offset

class EventServerAdvanceTick_t:
    pass

class EventServerBeginAsyncPostTickWork_t:
    pass

class EventServerEndAsyncPostTickWork_t:
    pass

class EventServerPollNetworking_t:
    pass

class EventServerPostAdvanceTick_t:
    pass

class EventServerPostSimulate_t:
    pass

class EventServerProcessNetworking_t:
    pass

class EventServerSimulate_t:
    pass

class EventSetTime_t:
    m_LoopState = 0  # offset
    m_flRealTime = 48  # offset
    m_flRenderFrameTime = 64  # offset
    m_flRenderFrameTimeUnbounded = 72  # offset
    m_flRenderFrameTimeUnscaled = 80  # offset
    m_flRenderTime = 56  # offset
    m_flTickRemainder = 88  # offset
    m_nClientOutputFrames = 40  # offset

class EventSimpleLoopFrameUpdate_t:
    m_LoopState = 0  # offset
    m_flFrameTime = 44  # offset
    m_flRealTime = 40  # offset

class EventSimulate_t:
    m_LoopState = 0  # offset
    m_bFirstTick = 40  # offset
    m_bLastTick = 41  # offset

class EventSplitScreenStateChanged_t:
    pass

class GameTick_t:
    m_Value = 0  # offset

class GameTime_t:
    m_Value = 0  # offset

