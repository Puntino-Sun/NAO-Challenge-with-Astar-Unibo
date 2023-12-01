""" Movimento Completo Rotazione Braccio Destro """import almathimport timedef right_arm(motion_proxy, posture_proxy, tts_proxy, debug=False):    if debug:        tts_proxy.say("right_arm")        time.sleep(1)    ########## Start position ###########    RShoulderPitch = 78.0    RShoulderRoll = -16.6    RElbowYaw = 68.3    RElbowRoll = 49.2    RWristYaw = 4.3    RHand = 0.10    LShoulderPitch = 78.0    LShoulderRoll = 16.6    LElbowYaw = -68.3    LElbowRoll = -49.2    LWristYaw = 4.3    LHand = 0.0    names = "LArm"    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand]    timeLists = 2    motion_proxy.post.angleInterpolation(names, angleLists, timeLists, True)    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand]    timeLists = 2    motion_proxy.angleInterpolation(names, angleLists, timeLists, True)    # Not waiting because movement is fluid and without pause    ########## Movement arms ###########    # Open/extend RArm    RShoulderPitch = -75.7    RShoulderRoll = -79.8    RElbowYaw = -57.6    RElbowRoll = 2.2    RWristYaw = 87.0    RHand = 0.35    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]    motion_proxy.setAngles(names, angleLists, 0.1)    time.sleep(2)    # Raise RArm sideways    RShoulderPitch = -79.8    RShoulderRoll = -26.2    RElbowYaw = -57.6    RElbowRoll = 2.2    RWristYaw = 87.0    RHand = 0.35    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]    motion_proxy.setAngles(names, angleLists, 0.15)    time.sleep(1)    # Align RShoulder and move forward RArm    RShoulderPitch = 11.0    RShoulderRoll = 5.4    RElbowYaw = 68.3    RElbowRoll = 2.2    RWristYaw = 88.5    RHand = 0.35    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]    timeLists = 4    motion_proxy.angleInterpolation(names, angleLists, timeLists, True)