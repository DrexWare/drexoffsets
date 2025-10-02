# dumped by shxdows dumper (csdump)

from enum import Enum

class PulseBestOutflowRules_t(Enum):
    SORT_BY_NUMBER_OF_VALID_CRITERIA = 0
    SORT_BY_OUTFLOW_INDEX = 1

class PulseCursorCancelPriority_t(Enum):
    CancelOnSucceeded = 1
    HardCancel = 3
    None = 0
    SoftCancel = 2

class PulseMethodCallMode_t(Enum):
    ASYNC_FIRE_AND_FORGET = 1
    SYNC_WAIT_FOR_COMPLETION = 0

class PulseTestEnumColor_t(Enum):
    BLACK = 0
    BLUE = 4
    GREEN = 3
    RED = 2
    WHITE = 1

class PulseTestEnumShape_t(Enum):
    CIRCLE = 100
    SQUARE = 200
    TRIANGLE = 300

class CBasePulseGraphInstance:
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

class CPulseCell_ExampleCriteria:
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
        }
    ]

class CPulseCell_ExampleCriteria__Criteria_t:
    m_bMyBool = 8  # offset
    m_flFloatValue1 = 0  # offset
    m_flFloatValue2 = 4  # offset

class CPulseCell_ExampleSelector:
    m_OutflowList = 72  # offset

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

class CPulseCell_Outflow_TestExplicitYesNo:
    m_No = 144  # offset
    m_Yes = 72  # offset

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

class CPulseCell_Outflow_TestRandomYesNo:
    m_No = 144  # offset
    m_Yes = 72  # offset

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

class CPulseCell_Step_TestDomainCreateFakeEntity:
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
        }
    ]

class CPulseCell_Step_TestDomainDestroyFakeEntity:
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
        }
    ]

class CPulseCell_Step_TestDomainEntFire:
    m_Input = 72  # offset

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
            "name": "MPulseEditorHeaderText",
            "type": "Unknown"
        }
    ]

class CPulseCell_Step_TestDomainTracepoint:
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
        }
    ]

class CPulseCell_TestWaitWithCursorState:
    m_WakeCancel = 144  # offset
    m_WakeFail = 216  # offset
    m_WakeResume = 72  # offset

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

class CPulseCell_TestWaitWithCursorState__CursorState_t:
    bFailOnCancel = 4  # offset
    flWaitValue = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Test_MultiInflow_NoDefault:
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

class CPulseCell_Test_MultiInflow_WithDefault:
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

class CPulseCell_Test_MultiOutflow_WithParams:
    m_Out1 = 72  # offset
    m_Out2 = 144  # offset

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

class CPulseCell_Test_MultiOutflow_WithParams_Yielding:
    m_AsyncChild1 = 144  # offset
    m_AsyncChild2 = 216  # offset
    m_Out1 = 72  # offset
    m_YieldResume1 = 288  # offset
    m_YieldResume2 = 360  # offset

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

class CPulseCell_Test_MultiOutflow_WithParams_Yielding__CursorState_t:
    nTestStep = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CPulseCell_Test_NoInflow:
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

class CPulseCell_Val_TestDomainFindEntityByName:
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
        }
    ]

class CPulseCell_Val_TestDomainGetEntityName:
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
        }
    ]

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

class CPulseCell_Value_TestValue50:
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

class CPulseGraphInstance_TestDomain:
    m_Tracepoints = 296  # offset
    m_bExpectingCursorTerminatedDueToMaxInstructions = 284  # offset
    m_bExpectingToDestroyWithYieldedCursors = 282  # offset
    m_bExplicitTimeStepping = 281  # offset
    m_bIsRunningUnitTests = 280  # offset
    m_bQuietTracepoints = 283  # offset
    m_bTestYesOrNoPath = 320  # offset
    m_nCursorsTerminatedDueToMaxInstructions = 288  # offset
    m_nNextValidateIndex = 292  # offset

class CPulseGraphInstance_TestDomain_Derived:
    m_nInstanceValueX = 328  # offset

class CPulseGraphInstance_TestDomain_FakeEntityOwner:
    pass

class CPulseGraphInstance_TurtleGraphics:
    pass

class CPulseMathlib:
    pass

    __metadata__ =     [
        {
            "name": "MPropertyDescription",
            "type": "Unknown"
        }
    ]

class CPulseTestFuncs_LibraryA:
    pass

    __metadata__ =     [
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

class CPulseTurtleGraphicsCursor:
    m_Color = 208  # offset
    m_bPenUp = 224  # offset
    m_flHeadingDeg = 220  # offset
    m_vPos = 212  # offset

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

class CTestDomainDerived_Cursor:
    m_nCursorValueA = 208  # offset
    m_nCursorValueB = 212  # offset

class FakeEntityDerivedA_tAPI:
    pass

class FakeEntityDerivedB_tAPI:
    pass

class FakeEntity_tAPI:
    pass

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

class SignatureOutflow_Continue:
    pass

class SignatureOutflow_Resume:
    pass