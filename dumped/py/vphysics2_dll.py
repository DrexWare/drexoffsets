// dumped by shxdows dumper (csdump)
# dumped by shxdows dumper (csdump) 

from enum import Enum

class DynamicContinuousContactBehavior_t(Enum):
    DYNAMIC_CONTINUOUS_ALLOW_IF_REQUESTED_BY_OTHER_BODY = 0
    DYNAMIC_CONTINUOUS_ALWAYS = 1
    DYNAMIC_CONTINUOUS_NEVER = 2

class JointAxis_t(Enum):
    JOINT_AXIS_COUNT = 3
    JOINT_AXIS_X = 0
    JOINT_AXIS_Y = 1
    JOINT_AXIS_Z = 2

class JointMotion_t(Enum):
    JOINT_MOTION_COUNT = 2
    JOINT_MOTION_FREE = 0
    JOINT_MOTION_LOCKED = 1

class CFeIndexedJiggleBone:
    m_jiggleBone = 8  # offset
    m_nJiggleParent = 4  # offset
    m_nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFeJiggleBone:
    m_flAlongDamping = 32  # offset
    m_flAlongStiffness = 28  # offset
    m_flAngleLimit = 36  # offset
    m_flBaseDamping = 80  # offset
    m_flBaseForwardFriction = 116  # offset
    m_flBaseLeftFriction = 92  # offset
    m_flBaseMass = 72  # offset
    m_flBaseMaxForward = 112  # offset
    m_flBaseMaxLeft = 88  # offset
    m_flBaseMaxUp = 100  # offset
    m_flBaseMinForward = 108  # offset
    m_flBaseMinLeft = 84  # offset
    m_flBaseMinUp = 96  # offset
    m_flBaseStiffness = 76  # offset
    m_flBaseUpFriction = 104  # offset
    m_flLength = 4  # offset
    m_flMaxPitch = 60  # offset
    m_flMaxYaw = 44  # offset
    m_flMinPitch = 56  # offset
    m_flMinYaw = 40  # offset
    m_flPitchBounce = 68  # offset
    m_flPitchDamping = 24  # offset
    m_flPitchFriction = 64  # offset
    m_flPitchStiffness = 20  # offset
    m_flRadius0 = 120  # offset
    m_flRadius1 = 124  # offset
    m_flTipMass = 8  # offset
    m_flYawBounce = 52  # offset
    m_flYawDamping = 16  # offset
    m_flYawFriction = 48  # offset
    m_flYawStiffness = 12  # offset
    m_nCollisionMask = 152  # offset
    m_nFlags = 0  # offset
    m_vPoint0 = 128  # offset
    m_vPoint1 = 140  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFeMorphLayer:
    m_GoalDamping = 112  # offset
    m_GoalStrength = 88  # offset
    m_Gravity = 64  # offset
    m_InitPos = 40  # offset
    m_Name = 0  # offset
    m_Nodes = 16  # offset
    m_nNameHash = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFeNamedJiggleBone:
    m_jiggleBone = 52  # offset
    m_nJiggleParent = 48  # offset
    m_strParentBone = 0  # offset
    m_transform = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CFeVertexMapBuildArray:
    m_Array = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CRegionSVM:
    m_Nodes = 24  # offset
    m_Planes = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CastSphereSATParams_t:
    m_flMaxFraction = 28  # offset
    m_flRadius = 24  # offset
    m_flScale = 32  # offset
    m_pHull = 40  # offset
    m_vRayDelta = 12  # offset
    m_vRayStart = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class CovMatrix3:
    m_flXY = 12  # offset
    m_flXZ = 16  # offset
    m_flYZ = 20  # offset
    m_vDiag = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class Dop26_t:
    m_flSupport = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeAnimStrayRadius_t:
    flMaxDist = 4  # offset
    flRelaxationFactor = 8  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeAntiTunnelGroupBuild_t:
    m_nCollisionMask = 4  # offset
    m_nVertexMapHash = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeAntiTunnelProbeBuild_t:
    flActivationDistance = 4  # offset
    flBias = 8  # offset
    flCurvature = 12  # offset
    flWeight = 0  # offset
    nFlags = 16  # offset
    nProbeNode = 20  # offset
    targetNodes = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeAntiTunnelProbe_t:
    flActivationDistance = 16  # offset
    flBias = 24  # offset
    flCurvatureRadius = 20  # offset
    flWeight = 0  # offset
    nBegin = 12  # offset
    nCount = 10  # offset
    nFlags = 4  # offset
    nProbeNode = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeAxialEdgeBend_t:
    flDist = 8  # offset
    flWeight = 12  # offset
    nNode = 28  # offset
    te = 0  # offset
    tv = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeBandBendLimit_t:
    flDistMax = 4  # offset
    flDistMin = 0  # offset
    nNode = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeBoxRigid_t:
    nCollisionMask = 34  # offset
    nFlags = 50  # offset
    nNode = 32  # offset
    nVertexMapIndex = 48  # offset
    tmFrame2 = 0  # offset
    vSize = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeBuildBoxRigid_t:
    m_nAntitunnelGroupBits = 72  # offset
    m_nPriority = 64  # offset
    m_nVertexMapHash = 68  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeBuildSDFRigid_t:
    m_nAntitunnelGroupBits = 88  # offset
    m_nPriority = 80  # offset
    m_nVertexMapHash = 84  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeBuildSphereRigid_t:
    m_nAntitunnelGroupBits = 40  # offset
    m_nPriority = 32  # offset
    m_nVertexMapHash = 36  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeBuildTaperedCapsuleRigid_t:
    m_nAntitunnelGroupBits = 56  # offset
    m_nPriority = 48  # offset
    m_nVertexMapHash = 52  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeCollisionPlane_t:
    flStrength = 20  # offset
    m_Plane = 4  # offset
    nChildNode = 2  # offset
    nCtrlParent = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeCtrlOffset_t:
    nCtrlChild = 14  # offset
    nCtrlParent = 12  # offset
    vOffset = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeCtrlOsOffset_t:
    nCtrlChild = 2  # offset
    nCtrlParent = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeCtrlSoftOffset_t:
    flAlpha = 16  # offset
    nCtrlChild = 2  # offset
    nCtrlParent = 0  # offset
    vOffset = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeDynKinLink_t:
    m_nChild = 2  # offset
    m_nParent = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeEdgeDesc_t:
    nEdge = 0  # offset
    nSide = 4  # offset
    nVirtElem = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeEffectDesc_t:
    m_Params = 16  # offset
    nNameHash = 8  # offset
    nType = 12  # offset
    sName = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeFitInfluence_t:
    flWeight = 4  # offset
    nMatrixNode = 8  # offset
    nVertexNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeFitMatrix_t:
    bone = 0  # offset
    nBeginDynamic = 48  # offset
    nEnd = 44  # offset
    nNode = 46  # offset
    vCenter = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeFitWeight_t:
    flWeight = 0  # offset
    nDummy = 6  # offset
    nNode = 4  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeFollowNode_t:
    flWeight = 4  # offset
    nChildNode = 2  # offset
    nParentNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeHingeLimitBuild_t:
    flLimitCCW = 20  # offset
    flLimitCW = 16  # offset
    nFlags = 12  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeHingeLimit_t:
    flAngleCenter = 24  # offset
    flAngleExtents = 28  # offset
    flWeight4 = 16  # offset
    flWeight5 = 20  # offset
    nFlags = 12  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeKelagerBend2_t:
    flHeight0 = 12  # offset
    flWeight = 0  # offset
    nNode = 16  # offset
    nReserved = 22  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeMorphLayerDepr_t:
    m_GoalDamping = 112  # offset
    m_GoalStrength = 88  # offset
    m_Gravity = 64  # offset
    m_InitPos = 40  # offset
    m_Name = 0  # offset
    m_Nodes = 16  # offset
    m_nFlags = 136  # offset
    m_nNameHash = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeNodeBase_t:
    nDummy = 2  # offset
    nNode = 0  # offset
    nNodeX0 = 8  # offset
    nNodeX1 = 10  # offset
    nNodeY0 = 12  # offset
    nNodeY1 = 14  # offset
    qAdjust = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeNodeIntegrator_t:
    flAnimationForceAttraction = 4  # offset
    flAnimationVertexAttraction = 8  # offset
    flGravity = 12  # offset
    flPointDamping = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeNodeReverseOffset_t:
    nBoneCtrl = 12  # offset
    nTargetNode = 14  # offset
    vOffset = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeNodeWindBase_t:
    nNodeX0 = 0  # offset
    nNodeX1 = 2  # offset
    nNodeY0 = 4  # offset
    nNodeY1 = 6  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeProxyVertexMap_t:
    m_Name = 0  # offset
    m_flWeight = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeQuad_t:
    flSlack = 8  # offset
    nNode = 0  # offset
    vShape = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeRigidColliderIndices_t:
    m_nBoxRigidIndex = 4  # offset
    m_nCollisionPlaneIndex = 8  # offset
    m_nSDFRigidIndex = 6  # offset
    m_nSphereRigidIndex = 2  # offset
    m_nTaperedCapsuleRigidIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeRodConstraint_t:
    flMaxDist = 4  # offset
    flMinDist = 8  # offset
    flRelaxationFactor = 16  # offset
    flWeight0 = 12  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSDFRigid_t:
    flBounciness = 24  # offset
    m_Distances = 40  # offset
    m_nDepth = 72  # offset
    m_nHeight = 68  # offset
    m_nWidth = 64  # offset
    nCollisionMask = 30  # offset
    nFlags = 34  # offset
    nNode = 28  # offset
    nVertexMapIndex = 32  # offset
    vLocalMax = 12  # offset
    vLocalMin = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdAnimStrayRadius_t:
    flMaxDist = 16  # offset
    flRelaxationFactor = 32  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdNodeBase_t:
    nDummy = 40  # offset
    nNode = 0  # offset
    nNodeX0 = 8  # offset
    nNodeX1 = 16  # offset
    nNodeY0 = 24  # offset
    nNodeY1 = 32  # offset
    qAdjust = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdQuad_t:
    f4Slack = 32  # offset
    f4Weights = 240  # offset
    nNode = 0  # offset
    vShape = 48  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdRodConstraintAnim_t:
    f4RelaxationFactor = 32  # offset
    f4Weight0 = 16  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdRodConstraint_t:
    f4MaxDist = 16  # offset
    f4MinDist = 32  # offset
    f4RelaxationFactor = 64  # offset
    f4Weight0 = 48  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdSpringIntegrator_t:
    flNodeWeight0 = 64  # offset
    flSpringConstant = 32  # offset
    flSpringDamping = 48  # offset
    flSpringRestLength = 16  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSimdTri_t:
    nNode = 0  # offset
    v1x = 80  # offset
    v2 = 96  # offset
    w1 = 48  # offset
    w2 = 64  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSoftParent_t:
    flAlpha = 4  # offset
    nParent = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSourceEdge_t:
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSphereRigid_t:
    nCollisionMask = 18  # offset
    nFlags = 22  # offset
    nNode = 16  # offset
    nVertexMapIndex = 20  # offset
    vSphere = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeSpringIntegrator_t:
    flNodeWeight0 = 16  # offset
    flSpringConstant = 8  # offset
    flSpringDamping = 12  # offset
    flSpringRestLength = 4  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeStiffHingeBuild_t:
    flMaxAngle = 0  # offset
    flMotionBias = 8  # offset
    flStrength = 4  # offset
    nNode = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeTaperedCapsuleRigid_t:
    nCollisionMask = 34  # offset
    nFlags = 38  # offset
    nNode = 32  # offset
    nVertexMapIndex = 36  # offset
    vSphere = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeTaperedCapsuleStretch_t:
    flRadius = 8  # offset
    nCollisionMask = 4  # offset
    nDummy = 6  # offset
    nNode = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeTreeChildren_t:
    nChild = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeTri_t:
    nNode = 0  # offset
    v1x = 16  # offset
    v2 = 20  # offset
    w1 = 8  # offset
    w2 = 12  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeTwistConstraint_t:
    flSwingRelax = 8  # offset
    flTwistRelax = 4  # offset
    nNodeEnd = 2  # offset
    nNodeOrient = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeVertexMapBuild_t:
    m_Color = 12  # offset
    m_VertexMapName = 0  # offset
    m_Weights = 24  # offset
    m_flVolumetricSolveStrength = 16  # offset
    m_nNameHash = 8  # offset
    m_nScaleSourceNode = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeVertexMapDesc_t:
    flVolumetricSolveStrength = 44  # offset
    nColor = 12  # offset
    nFlags = 16  # offset
    nMapOffset = 24  # offset
    nNameHash = 8  # offset
    nNodeListCount = 50  # offset
    nNodeListOffset = 28  # offset
    nScaleSourceNode = 48  # offset
    nVertexBase = 20  # offset
    nVertexCount = 22  # offset
    sName = 0  # offset
    vCenterOfMass = 32  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeWeightedNode_t:
    nNode = 0  # offset
    nWeight = 2  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FeWorldCollisionParams_t:
    flGroundFriction = 4  # offset
    flWorldFriction = 0  # offset
    nListBegin = 8  # offset
    nListEnd = 10  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FourCovMatrices3:
    m_flXY = 48  # offset
    m_flXZ = 64  # offset
    m_flYZ = 80  # offset
    m_vDiag = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class FourVectors2D:
    x = 0  # offset
    y = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class IPhysicsPlayerController:
    pass

class OldFeEdge_t:
    c01 = 28  # offset
    c02 = 32  # offset
    c03 = 36  # offset
    c04 = 40  # offset
    flAxialModelDist = 44  # offset
    flAxialModelWeights = 48  # offset
    flThetaFactor = 24  # offset
    flThetaRelaxed = 20  # offset
    invA = 12  # offset
    m_flK = 0  # offset
    m_nNode = 64  # offset
    t = 16  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PhysFeModelDesc_t:
    m_AnimStrayRadii = 1104  # offset
    m_AntiTunnelBytecode = 384  # offset
    m_AntiTunnelProbes = 432  # offset
    m_AntiTunnelTargetNodes = 456  # offset
    m_AxialEdges = 480  # offset
    m_BoxRigids = 1328  # offset
    m_CollisionPlanes = 600  # offset
    m_CtrlHash = 0  # offset
    m_CtrlName = 24  # offset
    m_CtrlOffsets = 528  # offset
    m_CtrlOsOffsets = 552  # offset
    m_CtrlSoftOffsets = 1176  # offset
    m_DynKinLinks = 408  # offset
    m_DynNodeFriction = 768  # offset
    m_DynNodeVertexSet = 1352  # offset
    m_DynNodeWindBases = 1616  # offset
    m_Effects = 1520  # offset
    m_FitMatrices = 1032  # offset
    m_FitWeights = 1056  # offset
    m_FollowNodes = 576  # offset
    m_FreeNodes = 1008  # offset
    m_GoalDampedSpringIntegrators = 1248  # offset
    m_HingeLimits = 360  # offset
    m_InitPose = 288  # offset
    m_JiggleBones = 1200  # offset
    m_KelagerBends = 1152  # offset
    m_LegacyStretchForce = 720  # offset
    m_LocalForce = 816  # offset
    m_LocalRotation = 792  # offset
    m_LockToGoal = 1568  # offset
    m_LockToParent = 1544  # offset
    m_MorphLayers = 1424  # offset
    m_MorphSetData = 1448  # offset
    m_NodeBases = 120  # offset
    m_NodeCollisionRadii = 744  # offset
    m_NodeIntegrator = 624  # offset
    m_NodeInvMasses = 504  # offset
    m_Quads = 168  # offset
    m_ReverseOffsets = 1080  # offset
    m_RigidColliderPriorities = 1400  # offset
    m_Rods = 312  # offset
    m_Ropes = 96  # offset
    m_SDFRigids = 1304  # offset
    m_SimdAnimStrayRadii = 1128  # offset
    m_SimdNodeBases = 144  # offset
    m_SimdQuads = 192  # offset
    m_SimdRods = 240  # offset
    m_SimdRodsAnim = 264  # offset
    m_SimdSpringIntegrator = 672  # offset
    m_SimdTris = 216  # offset
    m_SkelParents = 1592  # offset
    m_SourceElems = 1224  # offset
    m_SphereRigids = 888  # offset
    m_SpringIntegrator = 648  # offset
    m_TaperedCapsuleRigids = 864  # offset
    m_TaperedCapsuleStretches = 840  # offset
    m_TreeChildren = 984  # offset
    m_TreeCollisionMasks = 960  # offset
    m_TreeParents = 936  # offset
    m_Tris = 1272  # offset
    m_Twists = 336  # offset
    m_VertexMapValues = 1496  # offset
    m_VertexMaps = 1472  # offset
    m_VertexSetNames = 1376  # offset
    m_WorldCollisionNodes = 912  # offset
    m_WorldCollisionParams = 696  # offset
    m_flAddWorldCollisionRadius = 1692  # offset
    m_flDefaultExpAirDrag = 1672  # offset
    m_flDefaultExpQuadAirDrag = 1680  # offset
    m_flDefaultGravityScale = 1664  # offset
    m_flDefaultSurfaceStretch = 1656  # offset
    m_flDefaultThreadStretch = 1660  # offset
    m_flDefaultTimeDilation = 1644  # offset
    m_flDefaultVelAirDrag = 1668  # offset
    m_flDefaultVelQuadAirDrag = 1676  # offset
    m_flDefaultVolumetricSolveAmount = 1696  # offset
    m_flInternalPressure = 1640  # offset
    m_flLocalDrag1 = 1704  # offset
    m_flLocalForce = 56  # offset
    m_flLocalRotation = 60  # offset
    m_flMotionSmoothCDT = 1700  # offset
    m_flQuadVelocitySmoothRate = 1688  # offset
    m_flRodVelocitySmoothRate = 1684  # offset
    m_flWindDrag = 1652  # offset
    m_flWindage = 1648  # offset
    m_nDynamicNodeFlags = 52  # offset
    m_nExtraGoalIterations = 1302  # offset
    m_nExtraIterations = 1303  # offset
    m_nExtraPressureIterations = 1301  # offset
    m_nFirstPositionDrivenNode = 70  # offset
    m_nNodeBaseJiggleboneDependsCount = 86  # offset
    m_nNodeCount = 64  # offset
    m_nQuadCount1 = 80  # offset
    m_nQuadCount2 = 82  # offset
    m_nQuadVelocitySmoothIterations = 1710  # offset
    m_nReservedUint8 = 1300  # offset
    m_nRodVelocitySmoothIterations = 1708  # offset
    m_nRopeCount = 88  # offset
    m_nRotLockStaticNodes = 68  # offset
    m_nSimdQuadCount1 = 76  # offset
    m_nSimdQuadCount2 = 78  # offset
    m_nSimdTriCount1 = 72  # offset
    m_nSimdTriCount2 = 74  # offset
    m_nStaticNodeFlags = 48  # offset
    m_nStaticNodes = 66  # offset
    m_nTreeDepth = 84  # offset
    m_nTriCount1 = 1296  # offset
    m_nTriCount2 = 1298  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class PhysicsParticleId_t:
    m_Value = 0  # offset

class RnBlendVertex_t:
    m_nFlags = 12  # offset
    m_nIndex0 = 2  # offset
    m_nIndex1 = 6  # offset
    m_nIndex2 = 10  # offset
    m_nTargetIndex = 14  # offset
    m_nWeight0 = 0  # offset
    m_nWeight1 = 4  # offset
    m_nWeight2 = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnBodyDesc_t:
    m_LocalInertiaInv = 72  # offset
    m_bBuoyancyDragEnabled = 203  # offset
    m_bDragEnabled = 202  # offset
    m_bEnabled = 199  # offset
    m_bHasShadowController = 217  # offset
    m_bIsContinuousEnabled = 201  # offset
    m_bSleeping = 200  # offset
    m_bSpeculativeEnabled = 216  # offset
    m_flAngularBuoyancyDrag = 144  # offset
    m_flAngularDamping = 128  # offset
    m_flAngularDrag = 136  # offset
    m_flBuoyancyFactor = 172  # offset
    m_flGameMass = 112  # offset
    m_flGravityScale = 176  # offset
    m_flInertiaScaleInv = 120  # offset
    m_flLinearBuoyancyDrag = 140  # offset
    m_flLinearDamping = 124  # offset
    m_flLinearDrag = 132  # offset
    m_flMassInv = 108  # offset
    m_flMassScaleInv = 116  # offset
    m_flTimeScale = 180  # offset
    m_nBodyType = 184  # offset
    m_nDynamicContinuousContactBehavior = 218  # offset
    m_nGameFlags = 192  # offset
    m_nGameIndex = 188  # offset
    m_nMassPriority = 198  # offset
    m_nMinPositionIterations = 197  # offset
    m_nMinVelocityIterations = 196  # offset
    m_qOrientation = 20  # offset
    m_sDebugName = 0  # offset
    m_vAngularVelocity = 48  # offset
    m_vGravity = 204  # offset
    m_vLastAwakeForceAccum = 148  # offset
    m_vLastAwakeTorqueAccum = 160  # offset
    m_vLinearVelocity = 36  # offset
    m_vLocalMassCenter = 60  # offset
    m_vPosition = 8  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnCapsuleDesc_t:
    m_Capsule = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnCapsule_t:
    m_flRadius = 24  # offset
    m_vCenter = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnFace_t:
    m_nEdge = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnHalfEdge_t:
    m_nFace = 3  # offset
    m_nNext = 0  # offset
    m_nOrigin = 2  # offset
    m_nTwin = 1  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnHullDesc_t:
    m_Hull = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnHull_t:
    m_Bounds = 16  # offset
    m_Edges = 160  # offset
    m_FacePlanes = 208  # offset
    m_Faces = 184  # offset
    m_MassProperties = 52  # offset
    m_VertexPositions = 136  # offset
    m_Vertices = 112  # offset
    m_flMaxAngularRadius = 12  # offset
    m_flSurfaceArea = 104  # offset
    m_flVolume = 100  # offset
    m_nFlags = 232  # offset
    m_pRegionSVM = 240  # offset
    m_vCentroid = 0  # offset
    m_vOrthographicAreas = 40  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnMeshDesc_t:
    m_Mesh = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnMesh_t:
    m_Materials = 144  # offset
    m_Nodes = 24  # offset
    m_TriangleEdgeFlags = 120  # offset
    m_Triangles = 72  # offset
    m_Vertices = 48  # offset
    m_Wings = 96  # offset
    m_nDebugFlags = 184  # offset
    m_nFlags = 180  # offset
    m_vMax = 12  # offset
    m_vMin = 0  # offset
    m_vOrthographicAreas = 168  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnNode_t:
    m_nChildren = 12  # offset
    m_nTriangleOffset = 28  # offset
    m_vMax = 16  # offset
    m_vMin = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnPlane_t:
    m_flOffset = 12  # offset
    m_vNormal = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnShapeDesc_t:
    m_UserFriendlyName = 8  # offset
    m_bUserFriendlyNameLong = 17  # offset
    m_bUserFriendlyNameSealed = 16  # offset
    m_nCollisionAttributeIndex = 0  # offset
    m_nSurfacePropertyIndex = 4  # offset
    m_nToolMaterialHash = 20  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnSoftbodyCapsule_t:
    m_flRadius = 24  # offset
    m_nParticle = 28  # offset
    m_vCenter = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnSoftbodyParticle_t:
    m_flMassInv = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnSoftbodySpring_t:
    m_flLength = 4  # offset
    m_nParticle = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnSphereDesc_t:
    m_Sphere = 24  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnTriangle_t:
    m_nIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnVertex_t:
    m_nEdge = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class RnWing_t:
    m_nIndex = 0  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

class VertexPositionColor_t:
    m_vPosition = 0  # offset

class VertexPositionNormal_t:
    m_vNormal = 12  # offset
    m_vPosition = 0  # offset

class constraint_axislimit_t:
    flMaxRotation = 4  # offset
    flMinRotation = 0  # offset
    flMotorMaxTorque = 12  # offset
    flMotorTargetAngSpeed = 8  # offset

class constraint_breakableparams_t:
    bodyMassScale = 12  # offset
    forceLimit = 4  # offset
    isActive = 20  # offset
    strength = 0  # offset
    torqueLimit = 8  # offset

class constraint_hingeparams_t:
    constraint = 40  # offset
    hingeAxis = 24  # offset
    worldAxisDirection = 12  # offset
    worldPosition = 0  # offset

class vphysics_save_cphysicsbody_t:
    m_nOldPointer = 224  # offset

    __metadata__ =     [
        {
            "name": "MGetKV3ClassDefaults",
            "type": "Unknown"
        }
    ]

