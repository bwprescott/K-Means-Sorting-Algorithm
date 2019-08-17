import matplotlib.pyplot as plot
import math
import random

# pokemon data, (total stats, attack)
# couldn't figure out how to automate putting the data into something python can read, so here's a lot of hardcoded data
# each point is 1 + its number, so like, line 20 on excel is p19
p1 = (23, 24)
p2 = (38, 31)
p3 = (58, 42)
p4 = (74, 51)
p5 = (22, 25)
p6 = (38, 32)
p7 = (59, 43)
p8 = (76, 68)
p9 = (22, 23)
p10 = (38, 31)
p11 = (58, 42)
p12 = (75, 53)
p13 = (3, 14)
p14 = (4, 8)
p15 = (36, 22)
p16 = (3, 16)
p17 = (4, 11)
p18 = (36, 46)
p19 = (53, 78)
p20 = (12, 22)
p21 = (28, 30)
p22 = (50, 41)
p23 = (67, 41)
p24 = (12, 28)
p25 = (39, 41)
p26 = (14, 30)
p27 = (44, 46)
p28 = (18, 30)
p29 = (43, 43)
p30 = (23, 27)
p31 = (51, 46)
p32 = (20, 38)
p33 = (45, 51)
p34 = (16, 23)
p35 = (31, 31)
p36 = (54, 47)
p37 = (16, 28)
p38 = (31, 36)
p39 = (54, 52)
p40 = (24, 22)
p41 = (51, 35)
p42 = (20, 19)
p43 = (54, 38)
p44 = (15, 22)
p45 = (43, 35)
p46 = (11, 22)
p47 = (46, 41)
p48 = (23, 24)
p49 = (36, 32)
p50 = (52, 41)
p51 = (18, 35)
p52 = (38, 49)
p53 = (21, 27)
p54 = (45, 32)
p55 = (14, 27)
p56 = (38, 41)
p57 = (18, 22)
p58 = (43, 35)
p59 = (23, 25)
p60 = (53, 42)
p61 = (21, 41)
p62 = (46, 54)
p63 = (28, 35)
p64 = (63, 57)
p65 = (20, 24)
p66 = (34, 32)
p67 = (55, 49)
p68 = (22, 8)
p69 = (37, 16)
p70 = (53, 24)
p71 = (68, 24)
p72 = (21, 41)
p73 = (38, 51)
p74 = (54, 68)
p75 = (20, 38)
p76 = (35, 46)
p77 = (52, 54)
p78 = (26, 19)
p79 = (56, 35)
p80 = (20, 41)
p81 = (35, 49)
p82 = (53, 62)
p83 = (38, 43)
p84 = (53, 51)
p85 = (23, 32)
p86 = (52, 38)
p87 = (68, 38)
p88 = (24, 16)
p89 = (48, 30)
p90 = (29, 32)
p91 = (22, 43)
p92 = (47, 57)
p93 = (24, 22)
p94 = (49, 35)
p95 = (24, 41)
p96 = (53, 54)
p97 = (21, 32)
p98 = (58, 49)
p99 = (22, 16)
p100 = (38, 24)
p101 = (53, 32)
p102 = (70, 32)
p103 = (34, 22)
p104 = (25, 23)
p105 = (51, 37)
p106 = (24, 54)
p107 = (49, 68)
p108 = (25, 14)
p109 = (50, 24)
p110 = (24, 19)
p111 = (57, 49)
p112 = (23, 24)
p113 = (41, 41)
p114 = (46, 62)
p115 = (46, 54)
p116 = (34, 27)
p117 = (27, 32)
p118 = (52, 46)
p119 = (28, 43)
p120 = (51, 68)
p121 = (45, 0)
p122 = (43, 27)
p123 = (52, 49)
p124 = (68, 65)
p125 = (19, 19)
p126 = (43, 32)
p127 = (23, 34)
p128 = (45, 47)
p129 = (27, 22)
p130 = (57, 38)
p131 = (47, 22)
p132 = (53, 57)
p133 = (46, 24)
p134 = (52, 42)
p135 = (53, 49)
p136 = (53, 65)
p137 = (70, 81)
p138 = (52, 51)
p139 = (3, 3)
p140 = (60, 65)
p141 = (77, 81)
p142 = (59, 43)
p143 = (18, 23)
p144 = (24, 27)
p145 = (58, 32)
p146 = (58, 32)
p147 = (58, 68)
p148 = (36, 30)
p149 = (29, 19)
p150 = (53, 30)
p151 = (29, 41)
p152 = (53, 59)
p153 = (56, 54)
p154 = (73, 70)
p155 = (60, 57)
p156 = (67, 43)
p157 = (67, 46)
p158 = (67, 51)
p159 = (20, 32)
p160 = (40, 43)
p161 = (70, 70)
p162 = (83, 57)
p163 = (100, 100)
p164 = (100, 78)
p165 = (70, 51)
p166 = (23, 24)
p167 = (38, 31)
p168 = (58, 42)
p169 = (22, 25)
p170 = (38, 32)
p171 = (59, 43)
p172 = (22, 32)
p173 = (38, 41)
p174 = (58, 54)
p175 = (6, 22)
p176 = (39, 38)
p177 = (14, 14)
p178 = (44, 24)
p179 = (14, 8)
p180 = (35, 16)
p181 = (12, 30)
p182 = (35, 46)
p183 = (59, 46)
p184 = (25, 18)
p185 = (47, 29)
p186 = (4, 19)
p187 = (6, 11)
p188 = (5, 14)
p189 = (11, 8)
p190 = (38, 19)
p191 = (23, 24)
p192 = (48, 38)
p193 = (17, 19)
p194 = (31, 27)
p195 = (55, 38)
p196 = (72, 49)
p197 = (52, 41)
p198 = (12, 8)
p199 = (40, 24)
p200 = (38, 51)

# put all the points into an array so they can be randomly selected, compared, etc.
points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
          p11, p12, p13, p14, p15, p16, p16, p18, p19, p20,
          p21, p22, p23, p24, p25, p26, p27, p28, p29, p30,
          p31, p32, p33, p34, p35, p36, p37, p38, p39, p40,
          p41, p42, p43, p44, p45, p46, p47, p48, p49, p50,
          p51, p52, p53, p54, p55, p56, p57, p58, p59, p60,
          p61, p62, p63, p64, p65, p66, p67, p68, p69, p70,
          p71, p72, p73, p74, p75, p76, p77, p78, p79, p80,
          p81, p82, p83, p84, p85, p86, p87, p88, p89, p90,
          p91, p92, p93, p94, p95, p96, p97, p98, p99, p100,
          p101, p102, p103, p104, p105, p106, p107, p108, p109, p110,
          p111, p112, p113, p114, p115, p116, p117, p118, p119, p120,
          p121, p122, p123, p124, p125, p126, p127, p128, p129, p130,
          p131, p132, p133, p134, p135, p136, p137, p138, p139, p140,
          p141, p142, p143, p144, p145, p146, p147, p148, p149, p150,
          p151, p152, p153, p154, p155, p156, p157, p158, p159, p160,
          p161, p162, p163, p164, p165, p166, p167, p168, p169, p170,
          p171, p172, p173, p174, p175, p176, p177, p178, p179, p180,
          p181, p182, p183, p184, p185, p186, p187, p188, p189, p190,
          p191, p192, p193, p194, p195, p196, p197, p198, p199, p200]

cluster = [0] * 200
cluster1 = []
cluster2 = []

# randomly selects centroids
centroid1 = points[random.randint(0, 199)]
centroid2 = points[random.randint(0, 199)]
# I know it's unlikely, but just in case it chooses the same point for both centroids
while centroid2 == centroid1:
    centroid2 = points[random.randint(0, 199)]


# finds the distance between 2 points
def distance(p, q):
    return int(math.fabs(p[0] - q[0]) + math.fabs(p[1] - q[1]))


# assigns points to clusters based on distances
def assignCluster(c1, c2):
    global cluster
    for i in range(len(cluster)):
        if distance(points[i], c1) < distance(points[i], c2):
            cluster[i] = 1
        else:
            cluster[i] = 2


# updates the content of clusters in order to find new centroids
def updateClusters():
    global cluster
    for i in range(len(cluster)):
        if cluster[i] == 1:
            cluster1.append(i)
        if cluster[i] == 2:
            cluster2.append(i)


# determines the new centroids of the clusters
def new_centroids(p):
    sum_of_x = 0
    sum_of_y = 0
    for i in range(len(p)):
        sum_of_x = points[p[i]][0] + sum_of_x
    for i in range(len(p)):
        sum_of_y = points[p[i]][1] + sum_of_y
    return sum_of_x / len(p), sum_of_y / len(p)


# k means algorithm
def kMeansCluster():
    global cluster1
    global cluster2
    global cluster
    global centroid1
    global centroid2

    newCluster1 = []
    newCluster2 = []

    firstCluster1 = []
    firstCluster2 = []

    newCentroid1 = (1, 1)
    newCentroid2 = (1, 1)

    x = 0

    # startup loop
    assignCluster(centroid1, centroid2)
    for i in range(len(points)):
        if cluster[i] == 1:
            firstCluster1.append(points[i])
        else:
            firstCluster2.append(points[i])
    print("First Clusters")
    print(firstCluster1)
    print(firstCluster2)
    print(centroid1)
    print(centroid2)
    print(cluster)

    # Matplotlib stuff
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    for i in range(len(points)):
        if cluster[i] == 1:
            X1.append(points[i][0])
            Y1.append(points[i][1])
        else:
            X2.append(points[i][0])
            Y2.append(points[i][1])
    plot.ylim([0, 100])
    plot.xlim([0, 100])
    plot.plot(X1, Y1, 'go')
    plot.plot(X2, Y2, 'bo')
    plot.plot([centroid1[0]], [centroid1[1]], 'ro')
    plot.plot([centroid2[0]], [centroid2[1]], 'r^')
    plot.show()

    oldCentroid1 = centroid1
    oldCentroid2 = centroid2

    # Repeating Loop
    # Doesn't repeat for some reason. Conditions get satisfied too easily?
    # Or it repeats too much
    # Might just be satisfied quickly
    while (newCentroid1 != oldCentroid1) & (newCentroid2 != oldCentroid2):
        # If this is the first loop, ignore this line
        if x > 0:
            oldCentroid1 = newCentroid1
            oldCentroid2 = newCentroid2
        x = x + 1

        updateClusters()
        c1 = new_centroids(cluster1)
        c2 = new_centroids(cluster2)
        newCentroid1 = c1
        newCentroid2 = c2
        newCluster1 = []
        newCluster2 = []
        for i in range(len(points)):
            if cluster[i] == 1:
                newCluster1.append(points[i])
            else:
                newCluster2.append(points[i])
        print("Middle Clusters")
        print(newCluster1)
        print(newCluster2)
        cluster1 = []
        cluster2 = []
        assignCluster(c1, c2)
        print(c1)
        print(c2)
        print(cluster)

        # Matplotlib stuff
        X1 = []
        Y1 = []
        X2 = []
        Y2 = []
        for i in range(len(points)):
            if cluster[i] == 1:
                X1.append(points[i][0])
                Y1.append(points[i][1])
            else:
                X2.append(points[i][0])
                Y2.append(points[i][1])
        plot.ylim([0, 100])
        plot.xlim([0, 100])
        plot.plot(X1, Y1, 'go')
        plot.plot(X2, Y2, 'bo')
        plot.plot([c1[0]], [c1[1]], 'ro')
        plot.plot([c2[0]], [c2[1]], 'r^')
        plot.show()

    print("Final Clusters")
    print(newCluster1)
    print(newCluster2)
    print(c1)
    print(c2)
    print(cluster)

    # Matplotlib stuff
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    for i in range(len(points)):
        if cluster[i] == 1:
            X1.append(points[i][0])
            Y1.append(points[i][1])
        else:
            X2.append(points[i][0])
            Y2.append(points[i][1])
    plot.ylim([0, 100])
    plot.xlim([0, 100])
    plot.plot(X1, Y1, 'go')
    plot.plot(X2, Y2, 'bo')
    plot.plot([c1[0]], [c1[1]], 'ro')
    plot.plot([c2[0]], [c2[1]], 'r^')
    plot.show()


def main():
    kMeansCluster()


if __name__ == "__main__": main()
