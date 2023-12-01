""" Movimento Completo Movimento Doppio """import almathimport timedef double_movement(motion_proxy, posture_proxy, tts_proxy, debug=False):    if debug:        tts_proxy.say("double_movement")        time.sleep(1)    # Moving    ########## Start position ###########    RShoulderPitch = 78.0    RShoulderRoll = -39.9    RElbowYaw = 68.3    RElbowRoll = 57.2    RWristYaw = 95    RHand = 0.10    LShoulderPitch = 78.0    LShoulderRoll = 39.9    LElbowYaw = -68.3    LElbowRoll = -57.2    LWristYaw = 4.3    LHand = 0.0    names = "LArm"    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand]    timeLists = 2    motion_proxy.post.angleInterpolation(names, angleLists, timeLists, True)    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand]    timeLists = 2    motion_proxy.angleInterpolation(names, angleLists, timeLists, True)    time.sleep(0.5)  # Waiting between the two movements    ########## Movement arms ###########    # Start rotation movement    RShoulderPitch = 77.7    RShoulderRoll = -39.5    RElbowYaw = 33.7    RElbowRoll = 70    RWristYaw = 95    RHand = 0.10    LShoulderPitch = 77.8    LShoulderRoll = 49.2    LElbowYaw = -68.5    LElbowRoll = -9.4    LWristYaw = 4.5    LHand = 0.0    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]    motion_proxy.setAngles(names, angleLists, 0.05)    time.sleep(0.2)    names = "LArm"    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]    motion_proxy.setAngles(names, angleLists, 0.08)    time.sleep(1.2)    # Arms parallel to the floor    RShoulderPitch = 15.1    RShoulderRoll = -10.6    RElbowYaw = 9.5    RElbowRoll = 70    RWristYaw = 95    RHand = 0.10    LShoulderPitch = 77.8    LShoulderRoll = 75.8    LElbowYaw = -68.5    LElbowRoll = -2.5    LWristYaw = 4.5    LHand = 0.0    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]    motion_proxy.setAngles(names, angleLists, 0.15)    time.sleep(0.3)    names = "LArm"    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]    motion_proxy.setAngles(names, angleLists, 0.1)    time.sleep(0.6)    # Go to final position    RShoulderPitch = 62.4    RShoulderRoll = -15.7    RElbowYaw = 51.7    RElbowRoll = 81    RWristYaw = 105    RHand = 0.10    LShoulderPitch = 27.0    LShoulderRoll = 29.8    LElbowYaw = -72.9    LElbowRoll = -27.2    LWristYaw = 4.5    LHand = 0.0    names = "RArm"    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]    motion_proxy.post.angleInterpolation(names, angleLists, 1.4, True)    time.sleep(0.3)    names = "LArm"    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]    motion_proxy.angleInterpolation(names, angleLists, 1.4, True)