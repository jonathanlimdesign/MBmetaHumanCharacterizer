"""
The Motion Builder Metahuman Characterizer is a tool that automatically assigns an imported Metahuman to a Motion Builder Character and T-poses the Character.
Created by Jonathan Lim - [ 18th March 2022 ] - (jonathanlim056@gmail.com)
"""


from pyfbsdk import *


#Create Character    
myChar = FBCharacter("MetaHuman")

#Change input type to Character
myChar.InputType = FBCharacterInputType.kFBCharacterInputCharacter
myChar.ActiveInput = True


#Definition for assigning Bones

def assignJoint ( characterObject, slot, jointName ):
    myJoint = FBFindModelByLabelName(jointName)
    prop = characterObject.PropertyList.Find(slot + "Link")
    prop.append (myJoint)
    
#Assign BASE Bones to Character
  
assignJoint(myChar, 'Hips', 'pelvis')
assignJoint(myChar, 'LeftUpLeg', 'thigh_l')
assignJoint(myChar, 'LeftLeg', 'calf_l')
assignJoint(myChar, 'LeftFoot', 'foot_l')
assignJoint(myChar, 'RightUpLeg', 'thigh_r')
assignJoint(myChar, 'RightLeg', 'calf_r')
assignJoint(myChar, 'RightFoot', 'foot_r')
assignJoint(myChar, 'LeftArm', 'upperarm_l')
assignJoint(myChar, 'LeftForeArm', 'lowerarm_l')
assignJoint(myChar, 'LeftHand', 'hand_l')
assignJoint(myChar, 'RightArm', 'upperarm_r')
assignJoint(myChar, 'RightForeArm', 'lowerarm_r')
assignJoint(myChar, 'RightHand', 'hand_r')
assignJoint(myChar, 'Head', 'head')

#Assign EXTRA Bones to Character

assignJoint(myChar, 'Reference', 'root')
assignJoint(myChar, 'RightShoulder', 'clavicle_r')
assignJoint(myChar, 'LeftShoulder', 'clavicle_l')
assignJoint(myChar, 'Spine', 'spine_01')
assignJoint(myChar, 'Spine1', 'spine_02')
assignJoint(myChar, 'Spine2', 'spine_03')
assignJoint(myChar, 'Spine3', 'spine_04')
assignJoint(myChar, 'Spine4', 'spine_05')
assignJoint(myChar, 'Neck', 'neck_01')
assignJoint(myChar, 'Neck1', 'neck_02')


#T-Pose Character
#Define joint finder and rotation tools
def jointFind(jointName):
    joint = FBFindModelByLabelName(jointName)
    return joint

def LjointRotate(jointName, vector = (-90,0,0)):
    jointName.SetVector(FBVector3d(vector), FBModelTransformationType.kModelRotation, True)

def RjointRotate(jointName, vector = (90,0,0)):
    jointName.SetVector(FBVector3d(vector), FBModelTransformationType.kModelRotation, True)

#Rotate bones to T-Pose
Lclavicle = jointFind('clavicle_l')
LjointRotate(Lclavicle)
LupArm = jointFind('upperarm_l')
LjointRotate(LupArm, (-90,5,0))
LlowArm = jointFind('lowerarm_l')
LjointRotate(LlowArm, (-90,-5,0))
Lhand = jointFind('hand_l')
LjointRotate(Lhand, (-180,0,0))

Rclavicle = jointFind('clavicle_r')
RjointRotate(Rclavicle)
RupArm = jointFind('upperarm_r')
RjointRotate(RupArm, (90,-5,0))
RlowArm = jointFind('lowerarm_r')
RjointRotate(RlowArm, (90,5,0))
Rhand = jointFind('hand_r')
RjointRotate(Rhand, (0,0,0))
FBSystem().Scene.Evaluate()

#Characterize
myChar.SetCharacterizeOn(True)



