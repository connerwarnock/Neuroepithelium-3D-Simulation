# Author: Conner Warnock
# This program is a simulation of the neuroepithelium of the paddlefish's ampullary organs.
# The simulation tests whether some mathematical assumptions are true pertaining to the 3D modeling
# of the neuroepithelium as a tri-axial ellipsoid
# Date: November 9, 2021

import random
import math

s = 100000
averageExpectedMajor = 184.06
averageExpectedMinor = 136.34
averageExpectedDepth = 69.3
averageExpectedMajorMinor = (averageExpectedMajor + averageExpectedMinor) / 2

# Finds a random major axis value within a range
major = []
for i in range(0, s):
    # Random distribution
    # major.append(random.randint(100, 200))

    # Normal distribution instead of random gives the same result within <1%
    singleMajor = random.normalvariate(184.06, 42.7)
    if singleMajor < 0:
        singleMajor = 56
    major.append(singleMajor)

averageMajor = 0
for i in range(0, s):
    averageMajor += major[i]
averageMajor = averageMajor / len(major)

# Assigns a corresponding minor axis value by the known average major/minor ratio
minor = []
for i in range(0, s):
    minor.append(major[i] / 1.35)

averageMinor = 0
for i in range(0, s):
    averageMinor += minor[i]
averageMinor = averageMinor / len(minor)

# print("Major: ", major)
# print("Minor: ", minor)

# Makes a random measurement between the two random major/minor axes
meas = []
for i in range(0, s):
    meas.append(random.randint(int(minor[i]), int(major[i])))

# print("Measurement: ", meas)

averageMeas = 0
for i in range(0, s):
    averageMeas += meas[i]
averageMeas = averageMeas / len(meas)

# These two should be close to equal to within <1%
# This confirms that the average width in Table 1A is the average of the major/minor widths
# Thus the whiteboard result (picture on my phone) is accurate
print("Actual Average Measurement: ", averageMeas)
print("Expected Average Measurement: ", averageExpectedMajorMinor)
print("Actual Average Major: ", averageMajor)
print("Expected Average Major: ", averageExpectedMajor)
print("Actual Average Minor: ", averageMinor)
print("Expected Average Minor: ", averageExpectedMinor)

# Generate random depths
depth = []
for i in range(0, s):
    # Random distribution
    # depth.append(random.randint(50, 99))

    # Normal distribution
    singleDepth = random.normalvariate(69.3, 29.1)
    if singleDepth < 0:
        singleDepth = 15
    depth.append(singleDepth)

averageDepth = 0
for i in range(0, s):
    averageDepth += depth[i]
averageDepth = averageDepth / len(depth)
print("Actual Average Depth: ", averageDepth)
print("Expected Average Depth: ", averageExpectedDepth)

# Calculate surface areas
SAs = []
for i in range(0, s):
    SA = 4*math.pi*( ( ( ((major[i]*minor[i])**1.6075) +
                         ((major[i]*depth[i])**1.6075) +
                         ((minor[i]*depth[i])**1.6075) ) / 3 ) )**(1/1.6075)
    SAs.append(SA)

# print("SAs: ", SAs)

# Average SA
averageSA = 0
for i in range(0, s):
    averageSA += SAs[i]

averageSA = (1/2) * averageSA / len(SAs)
print("Average of All SAs: ", averageSA)

# SA using only actual major/minor/depth
# These SA averages are about the same, but the reason this discrepancy exists is because the SA averages are biased
# away from the mean due to them being raised to a >1 power. That is to say that inputs under the mean are not
# treated equal to inputs over the mean
singleAverageSA = (1/2)*4*math.pi*( ( ( ((averageMajor*averageMinor)**1.6075) +
                                        ((averageMajor*averageDepth)**1.6075) +
                                        ((averageMinor*averageDepth)**1.6075) ) / 3 ) )**(1/1.6075)
print("Average Using Average Major/Minor/Depth: ", singleAverageSA)
singleAverageExpectedSA = (1/2)*4*math.pi*( ( ( ((averageExpectedMajor*averageExpectedMinor)**1.6075) +
                                                ((averageExpectedMajor*averageExpectedDepth)**1.6075) +
                                                ((averageExpectedMinor*averageExpectedDepth)**1.6075) ) / 3 ) )**(1/1.6075)
print("Average Using Expected Average Major/Minor/Depth: ", singleAverageExpectedSA)






