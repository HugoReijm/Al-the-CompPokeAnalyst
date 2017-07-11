import matplotlib.pyplot as plt
import numpy,MetaDex,math

compressedtiers = []
tiers = MetaDex.getTiers()
for i in range(0,len(tiers),4):
    compressedtiers.append(tiers[i].split("-")[0])

#compressedtiers=["gen7ou"]

quarters = []
halves = []
thirdquarters =[]

for i in range(len(compressedtiers)):
    plt.figure(i)
    plt.subplot(121)
    plt.title("Usage for "+compressedtiers[i])
    plt.xlabel("Usage")
    plt.ylabel("Frequency")
    plt.axis([-0.05, 0.48, 0, 20])

    plt.subplot(122)
    plt.title("Usage vs. Raw Count for "+compressedtiers[i])
    plt.xlabel("Usage")
    plt.ylabel("Raw Count")

    numbers = ["0","1500","1630","1760"]
    #TODO: interesting...
    if "ou" in compressedtiers[i] and "battlespot" not in compressedtiers[i]:
        numbers = ["0","1500","1695","1825"]
    for n in numbers:
        tier=compressedtiers[i]+"-"+n
        tierfile = tier+".json"
        usageList = []
        rawcountList = []

        data = MetaDex.findTierData(tierfile)
        for poke in MetaDex.findTierData(tierfile):
            usageList.append(data[poke]["usage"])
            rawcountList.append(data[poke]["Raw count"])

        quarterUsage = sorted(usageList)[round(len(usageList)/4)]
        quarters.append(quarterUsage)
        halfUsage = sorted(usageList)[round(len(usageList)/2)]
        halves.append(halfUsage)
        thirdquarterUsage = sorted(usageList)[round(3*len(usageList)/4)]
        thirdquarters.append(thirdquarterUsage)

        usageNP = numpy.array(usageList)

        plt.figure(i)
        plt.subplot(121)
        if n == "0":
            plt.hist(usageNP, 500, color="red",alpha=0.5)
        elif n == "1500":
            plt.hist(usageNP, 500, color="yellow",alpha=0.5)
        elif n in ["1630","1695"]:
            plt.hist(usageNP, 500, color="green",alpha=0.5)
        elif n in ["1760","1825"]:
            plt.hist(usageNP, 500, color="blue",alpha=0.5)
        #plt.plot([quarterUsage, quarterUsage], [0, 20], c="black")
        #plt.plot([halfUsage, halfUsage], [0, 20], c="black")
        #plt.plot([thirdquarterUsage, thirdquarterUsage], [0, 20], c="black")

        plt.subplot(122)
        if n == "0":
            plt.scatter(usageList, rawcountList, s=2,color="red",alpha=0.75)
        elif n == "1500":
            plt.scatter(usageList, rawcountList, s=2,color="yellow",alpha=0.75)
        elif n in ["1630","1695"]:
            plt.scatter(usageList, rawcountList, s=2,color="green",alpha=0.75)
        elif n in ["1760","1825"]:
            plt.scatter(usageList, rawcountList, s=2,color="blue",alpha=0.75)

quarterav = sum(quarters)/len(compressedtiers)
quarterdeviation = 0
for i in quarters:
    quarterdeviation+=(i-quarterav)**2
quarterdeviation = math.sqrt(quarterdeviation/len(compressedtiers))

halfav = sum(halves)/len(compressedtiers)
halfdeviation = 0
for i in halves:
    halfdeviation+=(i-halfav)**2
halfdeviation = math.sqrt(halfdeviation/len(compressedtiers))

thirdquarterav = sum(thirdquarters)/len(compressedtiers)
thirdquarterdeviation = 0
for i in thirdquarters:
    thirdquarterdeviation+=(i-thirdquarterav)**2
thirdquarterdeviation = math.sqrt(thirdquarterdeviation/len(compressedtiers))

#for q in quarters:
#    print("data: %s" % q)
print("Quarter Average: %s" % quarterav)
print("Quarter Standard Deviation: %s" % quarterdeviation)
print()
#for h in halves:
#    print("data: %s" % h)
print("Half Average: %s" % halfav)
print("Half Standard Deviation: %s" % halfdeviation)
print()
#for t in thirdquarters:
#    print("data: %s" % t)
print("Third Quarter Average: %s" % thirdquarterav)
print("Third Quarter Standard Deviation: %s" % thirdquarterdeviation)
plt.show()