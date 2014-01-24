#####
# WHEAT AND BARLEY PLOTS
#####

import numpy as np
import matplotlib.pyplot as plt
import csv
import copy
from matplotlib import rc


class cwb(object):
    def __init__(self, dataFile = "data.csv"):
        self.dataFile = dataFile
        self.data = []
        with open(self.dataFile, 'rt') as csvfile:
            spamreader = csv.DictReader(csvfile, ["Field", "GovernmentMP", "OppositionMP", "GovernmentMP%", "OppositionMP%", "Total%"])
            for row in spamreader:
                if row["Field"] == "":
                    pass
                else:
                    self.data.append(row)

    def SimpleFarmerRepresentationPlot(self, title="Farmer Representation Arguments", x_label="Argument", y_label="Frequency of Coded Statements"):
        """
        Plot of FarmerRepresentation
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ["FarmerRepresentation", "FarmersAsEntrepreneurs", "FarmersInJail", "FarmersInRiding", "OtherFarmers", "PersonalIDWithFarmers", "YoungFarmers"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []
        
        for line in data:
            if "FarmersRepresentation" in line["Field"]:
                if "Positive" not in line["Field"]:
                    if "Negative" not in line["Field"]:
                        if "Neutral" not in line["Field"]:
                            sortedData.append(line)

        for line in sortedData:
            govt.append(int(line["GovernmentMP"]))
            opp.append(int(line["OppositionMP"]))

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        plt.grid(True, axis="y")
        
        plt.subplot(111)
        plt.subplots_adjust(bottom=0.2)
        rects1 = plt.bar(ind, govt, width, color='b')
                            #yerr=menStd,
                            #error_kw=dict(elinewidth=6, ecolor='pink'

        rects2 = plt.bar(ind+width, opp, width, color='r')
                            #yerr=womenStd,
                            #error_kw=dict(elinewidth=6, ecolor='yellow'

        # add some
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(ind+width, group_labels, rotation=45, fontsize=10)

        plt.legend( (rects1[0], rects2[0]), ('GovernmentMP', 'OppositionMP') )

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()

    def SimpleRegionalRepresentationPlot(self, title="RegionalRepresentation", x_label="Argument", y_label="Frequency of Coded Statements"):
        """
        Plot of RegionalRepresentation
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ["RegionalRepresentation", "ElectoralMandate", "OtherRegionalClaim", "RuralVsUrban", "SupplyManagement"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []
        
        for line in data:
            if "RegionalRepresentation" in line["Field"]:
                if "Positive" not in line["Field"]:
                    if "Negative" not in line["Field"]:
                        if "Neutral" not in line["Field"]:
                            sortedData.append(line)

        for line in sortedData:
            govt.append(int(line["GovernmentMP"]))
            opp.append(int(line["OppositionMP"]))

        plt.grid(True, axis="y")

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        plt.subplot(111)
        plt.subplots_adjust(bottom=0.2)
        rects1 = plt.bar(ind, govt, width, color='b')
                            #yerr=menStd,
                            #error_kw=dict(elinewidth=6, ecolor='pink'

        rects2 = plt.bar(ind+width, opp, width, color='r')
                            #yerr=womenStd,
                            #error_kw=dict(elinewidth=6, ecolor='yellow'

        # add some
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(ind+width, group_labels, rotation=45, fontsize=10)

        plt.legend( (rects1[0], rects2[0]), ('GovernmentMP', 'OppositionMP') )
        

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()

    def SimpleRationalesPlot(self, category, title="Rationales", x_label="Rationale Type", y_label="Frequency of Coded Statements"):
        """
        Plot of Rationales
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        if category == "Economics":
            group_labels = ["Economics", "CertaintyStability", "Corporations", "EconomicOpportunity", "FoodSovereignty", "InternationalTrade", "Jobs", "OtherEconomics"]
        if category == "Institutional":
            group_labels = ["Institutional", "FarmerCostsAndBenefits", "HistoryOrOutdated", "OtherInstitutional", "ValueOfMonopoly"]
        if category == "Principles":
            group_labels = ["Principles", "Democracy", "FairnessLegalRights", "Freedom", "Ideology", "OtherPrinciples"]
        if category == "ProceduralDemocracy":
            group_labels = ["ProceduralDemocracy", "OtherProceduralDemocracy", "ParliamentaryProcedure", "PolicyPlatformCommitment", "TimeForDebate"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []
        
        for line in data:
            if category in line["Field"]:
                if "Positive" not in line["Field"]:
                    if "Negative" not in line["Field"]:
                        if "Neutral" not in line["Field"]:
                            sortedData.append(line)

        for line in sortedData:
            if "RationaleForChange" in line["Field"]:
                govt.append(int(line["GovernmentMP"]))
            elif "RationaleForStatusQuo" in line["Field"]:
                opp.append(int(line["OppositionMP"]))

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        plt.grid(True, axis="y")
        
        plt.subplot(111)
        plt.subplots_adjust(bottom=0.2)
        rects1 = plt.bar(ind, govt, width, color='b')
                            #yerr=menStd,
                            #error_kw=dict(elinewidth=6, ecolor='pink'

        rects2 = plt.bar(ind+width, opp, width, color='r')
                            #yerr=womenStd,
                            #error_kw=dict(elinewidth=6, ecolor='yellow'

        # add some
        plt.ylabel(y_label)
        plt.ylim(ymax=200)
        plt.title(category + " " + title)
        plt.xticks(ind+width, group_labels, rotation=45, fontsize=10)
        plt.yticks([0, 25, 50, 75, 100, 125, 150, 175, 200], [0, 25, 50, 75, 100, 125, 150, 175, 200])

        leg = plt.legend( (rects1[0], rects2[0]), ('Government MP \n(Rationale for Change)', 'Opposition MP \n(Rationale for Status Quo)') )
        for t in leg.get_texts():
            t.set_fontsize('small')    # the legend text fontsize
            
        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()
        

    def StackedRationalesPlot(self, category, title="Rationales", x_label="Rationale Type", y_label="Frequency of Coded Statements"):
        """
        Plot of Rationales, stacked into positive, negative, neutral
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        if category == "Economics":
            group_labels = ["CertaintyStability", "Corporations", "EconomicOpportunity", "FoodSovereignty", "InternationalTrade", "OtherEconomics", "Jobs"]
        if category == "Institutional":
            group_labels = ["FarmerCostsAndBenefits", "HistoryOrOutdated", "OtherInstitutional", "ValueOfMonopoly"]
        if category == "Principles":
            group_labels = ["Democracy", "FairnessLegalRights", "Freedom", "OtherPrinciples", "Ideology"]
        if category == "ProcessLegitimacy":
            group_labels = ["ParliamentaryProcedure", "PolicyPlatformCommitment", "OtherProceduralDemocracy", "TimeForDebate"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []

        collectDict = {}
        for subgroup in group_labels:
            collectDict[subgroup]=dict([("GovernmentMP", dict([("Positive", 0), ("Negative", 0), ("Neutral", 0)])), ("OppositionMP", dict([("Positive", 0), ("Negative", 0), ("Neutral", 0)]))])
        
        for line in data:
            if category in line["Field"]:
                for subgroup in group_labels:
                    if subgroup in line["Field"]:
                        if "Positive" in line["Field"]:
                            if "RationaleForChange" in line["Field"]:
                                collectDict[subgroup]["GovernmentMP"]["Positive"]=(int(line["GovernmentMP"]))
                            if "RationaleForStatusQuo" in line["Field"]:
                                collectDict[subgroup]["OppositionMP"]["Positive"]=(int(line["OppositionMP"]))
                        if "Negative" in line["Field"]:
                            if "RationaleForChange" in line["Field"]:
                                collectDict[subgroup]["GovernmentMP"]["Negative"]=(int(line["GovernmentMP"]))
                            if "RationaleForStatusQuo" in line["Field"]:
                                collectDict[subgroup]["OppositionMP"]["Negative"]=(int(line["OppositionMP"]))
                        if "Neutral" in line["Field"]:
                            if "RationaleForChange" in line["Field"]:
                                collectDict[subgroup]["GovernmentMP"]["Neutral"]=(int(line["GovernmentMP"]))
                            if "RationaleForStatusQuo" in line["Field"]:
                                collectDict[subgroup]["OppositionMP"]["Neutral"]=(int(line["OppositionMP"]))
                             

        ## new dict list processing

        govta = []
        for subgroup in group_labels:
            govta.append(int(collectDict[subgroup]["GovernmentMP"]["Negative"]))
        
        govtb = []
        for subgroup in group_labels:
            govtb.append(int(collectDict[subgroup]["GovernmentMP"]["Neutral"]))
        
        govtc = []
        for subgroup in group_labels:
            govtc.append(int(collectDict[subgroup]["GovernmentMP"]["Positive"]))
        
        oppa = []
        for subgroup in group_labels:
            oppa.append(int(collectDict[subgroup]["OppositionMP"]["Negative"]))
        
        oppb = []
        for subgroup in group_labels:
            oppb.append(int(collectDict[subgroup]["OppositionMP"]["Neutral"]))
        
        oppc = []
        for subgroup in group_labels:
            oppc.append(int(collectDict[subgroup]["OppositionMP"]["Positive"]))
        

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        plt.grid(True, axis="y")
        
        plt.subplot(111, clip_on=False)
        plt.subplots_adjust(bottom=0.2)

        # Fix the first ba


        rect1 = plt.bar(ind, [sum(n) for n in zip(*[govta, govtb, govtc])], width, color='#ffffff')
        rect2 = plt.bar(ind+width, [sum(n) for n in zip(*[oppa, oppb, oppc])], width, color='#ffffff')




        rects1a = plt.bar(ind, govta, width, color='#99cccc')

        rects1b = plt.bar(ind, govtb, width, color='#3399ff', bottom = govta)

        rects1c = plt.bar(ind, govtc, width, color='#000099', bottom = [sum(n) for n in zip(*[govta, govtb])])

        rects2a = plt.bar(ind+width, oppa, width, color='#ff9999')

        rects2b = plt.bar(ind+width, oppb, width, color='#ff0000', bottom = oppa)

        rects2c = plt.bar(ind+width, oppc, width, color='#990000', bottom = [sum(n) for n in zip(*[oppa, oppb])])


        if category == "Economics":
            group_labels = ["Certainty and Stability", "Corporations", "Economic Opportunity", "Food Sovereignty", "International Trade", "Other Economics", "Jobs"]
        if category == "Institutional":
            group_labels = ["Farmer Costs And Benefits", "History/Outdated", "Other Institutional Value", "Value Of Monopoly"]
        if category == "Principles":
            group_labels = ["Democracy", "Legality and Fairness", "Freedom", "Other Principles", "Ideology"]
        if category == "ProcessLegitimacy":
            group_labels = ["Parliamentary Procedure", "Policy Platform Commitment", "Other Process Legitimacy", "Time For Debate"]
        
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        if category == "Principles":
            plt.ylim(ymax=200)
            plt.yticks([0, 25, 50, 75, 100, 125, 150, 175, 200], [0, 25, 50, 75, 100, 125, 150, 175, 200])
        elif category == "Institutional":
            plt.ylim(ymax=150)
            plt.yticks([0, 25, 50, 75, 100, 125, 150], [0, 25, 50, 75, 100, 125, 150])
        else:
            plt.ylim(ymax=125)
            plt.yticks([0, 25, 50, 75, 100, 125], [0, 25, 50, 75, 100, 125])
        if category == "ProcessLegitimacy":
            plt.title("Process Legitimacy" + " " + title, fontsize=18, )
        elif category == "Institutional":
            plt.title("Institutional Value" + " " + title, fontsize=18, )
        else:
            plt.title(category + " " + title, fontsize=18, )
            
        plt.xticks(ind+width, group_labels, rotation=45, fontsize=10)

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                drawheight = 1.05*height
                if height == 0:
                    drawheight += 1
                if height > 75:
                    drawheight -= 1
                plt.text(rect.get_x()+rect.get_width()/2., drawheight, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rect1)
        autolabel(rect2)
        

        leg = plt.legend( (rects1a[0], rects1b[0], rects1c[0], rects2a[0], rects2b[0], rects2c[0]), ('Government MP \n(Rationale for Change - Negative)', 'Government MP \n(Rationale for Change - Neutral)', 'Government MP \n(Rationale for Change - Positive)', 'Opposition MP \n(Rationale for Status Quo - Negative)', 'Opposition MP \n(Rationale for Status Quo - Neutral)', 'Opposition MP \n(Rationale for Status Quo - Positive)') )
        for t in leg.get_texts():
            t.set_fontsize('small')    # the legend text fontsize
            


        plt.show()



    def StackedRegionalRepresentationPlot(self, title="Regional Representation Arguments", x_label="Argument Type", y_label="Frequency of Coded Statements"):
        """
        Plot of regionalrepresentation, stacked into positive, negative, neutral
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ["ElectoralMandate", "OtherRegionalClaim", "RuralVsUrban"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []

        collectDict = {}
        for subgroup in group_labels:
            collectDict[subgroup]=dict([("GovernmentMP", dict([("Positive", 0), ("Negative", 0), ("Neutral", 0)])), ("OppositionMP", dict([("Positive", 0), ("Negative", 0), ("Neutral", 0)]))])

        
        for line in data:
            for subgroup in group_labels:
                if subgroup in line["Field"]:
                    if "Positive" in line["Field"]:
                            collectDict[subgroup]["GovernmentMP"]["Positive"]=(int(line["GovernmentMP"]))
                            collectDict[subgroup]["OppositionMP"]["Positive"]=(int(line["OppositionMP"]))
                    if "Negative" in line["Field"]:
                            collectDict[subgroup]["GovernmentMP"]["Negative"]=(int(line["GovernmentMP"]))
                            collectDict[subgroup]["OppositionMP"]["Negative"]=(int(line["OppositionMP"]))
                    if "Neutral" in line["Field"]:
                            collectDict[subgroup]["GovernmentMP"]["Neutral"]=(int(line["GovernmentMP"]))
                            collectDict[subgroup]["OppositionMP"]["Neutral"]=(int(line["OppositionMP"]))
                         

        ## new dict list processing

        govta = []
        for subgroup in group_labels:
            govta.append(int(collectDict[subgroup]["GovernmentMP"]["Negative"]))
        
        govtb = []
        for subgroup in group_labels:
            govtb.append(int(collectDict[subgroup]["GovernmentMP"]["Neutral"]))
        
        govtc = []
        for subgroup in group_labels:
            govtc.append(int(collectDict[subgroup]["GovernmentMP"]["Positive"]))
        
        oppa = []
        for subgroup in group_labels:
            oppa.append(int(collectDict[subgroup]["OppositionMP"]["Negative"]))
        
        oppb = []
        for subgroup in group_labels:
            oppb.append(int(collectDict[subgroup]["OppositionMP"]["Neutral"]))
        
        oppc = []
        for subgroup in group_labels:
            oppc.append(int(collectDict[subgroup]["OppositionMP"]["Positive"]))
        

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        plt.grid(True, axis="y")
        
        plt.subplot(111, clip_on=False)
        plt.subplots_adjust(bottom=0.2)

        # Fix the first ba


        rect1 = plt.bar(ind, [sum(n) for n in zip(*[govta, govtb, govtc])], width, color='#ffffff')
        rect2 = plt.bar(ind+width, [sum(n) for n in zip(*[oppa, oppb, oppc])], width, color='#ffffff')




        rects1a = plt.bar(ind, govta, width, color='#99cccc')

        rects1b = plt.bar(ind, govtb, width, color='#3399ff', bottom = govta)

        rects1c = plt.bar(ind, govtc, width, color='#000099', bottom = [sum(n) for n in zip(*[govta, govtb])])

        rects2a = plt.bar(ind+width, oppa, width, color='#ff9999')

        rects2b = plt.bar(ind+width, oppb, width, color='#ff0000', bottom = oppa)

        rects2c = plt.bar(ind+width, oppc, width, color='#990000', bottom = [sum(n) for n in zip(*[oppa, oppb])])


        group_labels = ["Electoral Mandate", "Other Regional Claim", "Rural Vs Urban"]
        
        plt.ylabel(y_label)
        plt.xlabel(x_label)

        plt.ylim(ymax=175)
        plt.yticks([0, 25, 50, 75, 100, 125, 150, 175], [0, 25, 50, 75, 100, 125, 150, 175])

        plt.title(title, fontsize=18, )
            
        plt.xticks(ind+width, group_labels, rotation=45, fontsize=10)

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                drawheight = 1.05*height
                if height == 0:
                    drawheight += 1
                if height > 75:
                    drawheight -= 1
                plt.text(rect.get_x()+rect.get_width()/2., drawheight, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rect1)
        autolabel(rect2)
        

        leg = plt.legend( (rects1a[0], rects1b[0], rects1c[0], rects2a[0], rects2b[0], rects2c[0]), ('Government MP \n(Argument - Negative)', 'Government MP \n(Argument - Neutral)', 'Government MP \n(Argument - Positive)', 'Opposition MP \n(Argument - Negative)', 'Opposition MP \n(Argument - Neutral)', 'Opposition MP \n(Argument - Positive)') )
        for t in leg.get_texts():
            t.set_fontsize('small')    # the legend text fontsize
            


        plt.show()



    def StackedFarmerRepresentationPlot(self, title="Farmer Representation Arguments", x_label="Argument Type", y_label="Frequency of Coded Statements"):
        """
        Plot of regionalrepresentation, stacked into positive, negative, neutral
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ["FarmersAsEntrepreneurs", "FarmersInJail", "FarmersInRiding", "OtherFarmers", "PersonalIDWithFarmers", "YoungFarmers"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []

        collectDict = {}
        for subgroup in group_labels:
            collectDict[subgroup]=dict([("GovernmentMP", dict([("Positive", 0), ("Negative", 0), ("Neutral", 0)])), ("OppositionMP", dict([("Positive", 0), ("Negative", 0), ("Neutral", 0)]))])

        
        for line in data:
            for subgroup in group_labels:
                if subgroup in line["Field"]:
                    if "Positive" in line["Field"]:
                            collectDict[subgroup]["GovernmentMP"]["Positive"]=(int(line["GovernmentMP"]))
                            collectDict[subgroup]["OppositionMP"]["Positive"]=(int(line["OppositionMP"]))
                    if "Negative" in line["Field"]:
                            collectDict[subgroup]["GovernmentMP"]["Negative"]=(int(line["GovernmentMP"]))
                            collectDict[subgroup]["OppositionMP"]["Negative"]=(int(line["OppositionMP"]))
                    if "Neutral" in line["Field"]:
                            collectDict[subgroup]["GovernmentMP"]["Neutral"]=(int(line["GovernmentMP"]))
                            collectDict[subgroup]["OppositionMP"]["Neutral"]=(int(line["OppositionMP"]))
                         

        ## new dict list processing

        govta = []
        for subgroup in group_labels:
            govta.append(int(collectDict[subgroup]["GovernmentMP"]["Negative"]))
        
        govtb = []
        for subgroup in group_labels:
            govtb.append(int(collectDict[subgroup]["GovernmentMP"]["Neutral"]))
        
        govtc = []
        for subgroup in group_labels:
            govtc.append(int(collectDict[subgroup]["GovernmentMP"]["Positive"]))
        
        oppa = []
        for subgroup in group_labels:
            oppa.append(int(collectDict[subgroup]["OppositionMP"]["Negative"]))
        
        oppb = []
        for subgroup in group_labels:
            oppb.append(int(collectDict[subgroup]["OppositionMP"]["Neutral"]))
        
        oppc = []
        for subgroup in group_labels:
            oppc.append(int(collectDict[subgroup]["OppositionMP"]["Positive"]))
        

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        plt.grid(True, axis="y")
        
        plt.subplot(111, clip_on=False)
        plt.subplots_adjust(bottom=0.2)

        # Fix the first ba


        rect1 = plt.bar(ind, [sum(n) for n in zip(*[govta, govtb, govtc])], width, color='#ffffff')
        rect2 = plt.bar(ind+width, [sum(n) for n in zip(*[oppa, oppb, oppc])], width, color='#ffffff')


        group_labels = ["Farmers As Entrepreneurs", "Farmers In Jail", "Farmers In Riding", "Other Farmers", "Personal ID With Farmers", "Young Farmers"]

        rects1a = plt.bar(ind, govta, width, color='#99cccc')

        rects1b = plt.bar(ind, govtb, width, color='#3399ff', bottom = govta)

        rects1c = plt.bar(ind, govtc, width, color='#000099', bottom = [sum(n) for n in zip(*[govta, govtb])])

        rects2a = plt.bar(ind+width, oppa, width, color='#ff9999')

        rects2b = plt.bar(ind+width, oppb, width, color='#ff0000', bottom = oppa)

        rects2c = plt.bar(ind+width, oppc, width, color='#990000', bottom = [sum(n) for n in zip(*[oppa, oppb])])


        
        
        plt.ylabel(y_label)
        plt.xlabel(x_label)

        plt.ylim(ymax=225)
        plt.yticks([0, 25, 50, 75, 100, 125, 150, 175, 200, 225], [0, 25, 50, 75, 100, 125, 150, 175, 200, 225])

        plt.title(title, fontsize=18, )
            
        plt.xticks(ind+width, group_labels, rotation=45, fontsize=10)

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                drawheight = 1.05*height
                if height == 0:
                    drawheight += 1
                if height > 75:
                    drawheight -= 1
                plt.text(rect.get_x()+rect.get_width()/2., drawheight, '%d'%int(height),
                        ha='center', va='bottom')

        def autolabelSide(rects):
            # attach some text labels
            for rect in rects:
                noDrawFlag = 0
                print (rect[0])
                print (rect[5])
                heightTest = rect[1].get_height()
                drawheight = heightTest/2
                if heightTest == 0:
                    noDrawFlag = 1
                if noDrawFlag == 0:
                    if "1" in rect[0]:

                        if "1a" in rect[0]:
                            height = rect[1].get_height()
                            drawheight = height/2
                            plt.text(rect[1].get_x()+(rect[1].get_width()/2), drawheight, "TESTa", ha='center', va='bottom')
                        elif "1b" in rect[0]:
                            drawheight = (rect[1].get_height())/2
                            plt.text(rect[1].get_x()+(rect[1].get_width()/2), drawheight+rects1a[1].get_height(), "TESTb", ha='center', va='bottom')
                        else:
                            drawheight = (rect[1].get_height())/2
                            plt.text(rect[1].get_x()+(rect[1].get_width()/2), drawheight+rects1a[1].get_height()+rects1b[1].get_height(), "TESTc", ha='center', va='bottom')
                    
                    else:
                        plt.text(rect.get_x()+(rect.get_width()/2), drawheight, "TEST",
                                ha='center', va='bottom')

        autolabel(rect1)
        autolabel(rect2)
        #autolabelSide(rects1a)
        #autolabelSide(rects1b)
        #autolabelSide(rects1c)
        

        leg = plt.legend( (rects1a[0], rects1b[0], rects1c[0], rects2a[0], rects2b[0], rects2c[0]), ('Government MP \n(Argument - Negative)', 'Government MP \n(Argument - Neutral)', 'Government MP \n(Argument - Positive)', 'Opposition MP \n(Argument - Negative)', 'Opposition MP \n(Argument - Neutral)', 'Opposition MP \n(Argument - Positive)') )
        for t in leg.get_texts():
            t.set_fontsize('small')    # the legend text fontsize
            


        plt.show()


    def TopPlot(self, topNum, dataType="total", dataValue="percent"):
        '''
        topNum = number of top bars to draw (int)
        data = government, opposition, total (str)
        value = percent, frequency (str)
        '''
        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ["FarmerPlebesciteOnCWB", "FarmersAsEntrepreneurs", "FarmersInJail", "FarmersInRiding", "OtherFarmers", "PersonalIDWithFarmers", "YoungFarmers"]
        N = topNum
        plotList = []
        plotNames = []


    def SuperSimplePlot(self, title="Overall Argument Frequencies", x_label="Argument Type", y_label="Frequency of Coded Statements"):
        """
        Plot of FarmerRepresentation
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ['Farmer Representation', 'Regional Representation', 'Economics', 'Process Legitimacy', 'Principles/Value-Driven', 'Institutional Value']

        N = len(group_labels)
        groups = []
        govt = [416, 202, 268, 89, 278, 174]
        opp = [247, 166, 238, 179, 331, 210]

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        plt.grid(True, axis="y")
        
        plt.subplot(111)
        plt.ylim(ymax=450)
        rects1 = plt.bar(ind, govt, width, color='b')
                            #yerr=menStd,
                            #error_kw=dict(elinewidth=6, ecolor='pink'

        rects2 = plt.bar(ind+width, opp, width, color='r')
                            #yerr=womenStd,
                            #error_kw=dict(elinewidth=6, ecolor='yellow'

        # add some
        plt.ylabel(y_label, fontsize = 14)
        plt.title(title, fontsize = 18)
        plt.xticks(ind+width, group_labels, fontsize=12)
        plt.xlabel(x_label, fontsize = 14)

        plt.legend( (rects1[0], rects2[0]), ('Government MP', 'Opposition MP') )

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()


    def constructsPlot(self, title="Standardized Construct Frequencies\nC-18 Debates (2011)", x_label="Argument Category", y_label="Absolute Frequency of Coded Statements"):
        """
        Plots the four constructed variables for government and opposition
        """

        data = copy.deepcopy(self.data)
        sortedData = []
        group_labels = ["Representational\nAuthority", "Value-Driven\nChange/\nStatus-Quo", "Popular\nAuthority", "Expert\nAuthority"]
        N = len(group_labels)
        groups = []
        govt = []
        opp = []

        repAuthGovt = 0.0
        repAuthOpp = 0.0
        popAuthGovt = 0.0
        popAuthOpp = 0.0
        ideologyAuthGovt = 0.0
        ideologyAuthOpp = 0.0
        expAuthGovt = 0.0
        expAuthOpp = 0.0
        
        for line in data:
            # Note that all these measures add Change for Government and Change plus status quo for opposition
            
            # Representational Authority measure: adds FarmerRepresentation minus Other and RegionalRepresentation minus Other


            if "FarmersRepresentation" in line["Field"]:
                if "Positive" not in line["Field"]:
                    if "Negative" not in line["Field"]:
                        if "Neutral" not in line["Field"]:
                            if "Other" not in line["Field"]:
                                if len(line["Field"])>31:
                                    repAuthGovt+=int(line["GovernmentMP"])
                                    repAuthOpp+=int(line["OppositionMP"])
            if "RegionalRepresentation" in line["Field"]:
                if "Positive" not in line["Field"]:
                    if "Negative" not in line["Field"]:
                        if "Neutral" not in line["Field"]:
                            if "Other" not in line["Field"]:
                                if len(line["Field"])>34:
                                    repAuthGovt+=int(line["GovernmentMP"])
                                    repAuthOpp+=int(line["OppositionMP"])

            

            # Popular Authority measure
            
            popAuthVars=["TimeForDebate", "GeneralGovernmentLegitimacy", "ParliamentaryProcedure", "FarmerPlebesciteOnCWB", "Democracy"]

            for measureField in popAuthVars:
                if measureField in line["Field"]:
                    if "Positive" not in line["Field"]:
                        if "Negative" not in line["Field"]:
                            if "Neutral" not in line["Field"]:
                                if "Change" in line["Field"]:
                                    popAuthGovt+=int(line["GovernmentMP"])
                                    popAuthOpp+=int(line["OppositionMP"])
                                elif "StatusQuo" in line["Field"]:
                                    popAuthOpp+=int(line["OppositionMP"])
                                elif "Representation" in line["Field"]:
                                    popAuthGovt+=int(line["GovernmentMP"])
                                    popAuthOpp+=int(line["OppositionMP"])
                                elif "FarmerPlebesciteOnCWB" in line["Field"]:
                                    popAuthGovt+=int(line["GovernmentMP"])
                                    popAuthOpp+=int(line["OppositionMP"])
                                    
                            


            # Ideological Commitment measure
            ideologyAuthVars=["PolicyPlatformCommitment", "GeneralGovernmentLegitimacy", "LegalityAndFairness", "Ideology", "Freedom", "ValueOfMonopoly", "HistoryOrOutdated"]

            for measureField in ideologyAuthVars:
                if measureField in line["Field"]:
                    if "Positive" not in line["Field"]:
                        if "Negative" not in line["Field"]:
                            if "Neutral" not in line["Field"]:
                                if "Change" in line["Field"]:
                                    ideologyAuthGovt+=int(line["GovernmentMP"])
                                    ideologyAuthOpp+=int(line["OppositionMP"])
                                elif "StatusQuo" in line["Field"]:
                                    ideologyAuthOpp+=int(line["OppositionMP"])
                                elif "Representation" in line["Field"]:
                                    ideologyAuthGovt+=int(line["GovernmentMP"])
                                    ideologyAuthOpp+=int(line["OppositionMP"])
                                        



            # Expert Authority measure:  Note the removal of HistoryOrOutdated and OtherInstitutions
            expAuthVars=["Economics", "FarmerCostsAndBenefits"]


            for measureField in expAuthVars:
                if measureField=="Economics":
                    if measureField in line["Field"]:
                        if "Positive" not in line["Field"]:
                            if "Negative" not in line["Field"]:
                                if "Neutral" not in line["Field"]:
                                    if len(line["Field"]) > 45:
                                        if "Change" in line["Field"]:
                                            expAuthGovt+=int(line["GovernmentMP"])
                                            expAuthOpp+=int(line["OppositionMP"])
                                    elif len(line["Field"])>52:
                                        if "StatusQuo" in line["Field"]:
                                            expAuthOpp+=int(line["OppositionMP"])

                else:
                    if measureField in line["Field"]:
                        if "Positive" not in line["Field"]:
                            if "Negative" not in line["Field"]:
                                if "Neutral" not in line["Field"]:
                                    if "Change" in line["Field"]:
                                        expAuthGovt+=int(line["GovernmentMP"])
                                        expAuthOpp+=int(line["OppositionMP"])
                                    elif "StatusQuo" in line["Field"]:
                                        expAuthOpp+=int(line["OppositionMP"])
                                    elif "Representation" in line["Field"]:
                                        expAuthGovt+=int(line["GovernmentMP"])
                                        expAuthOpp+=int(line["OppositionMP"])
                                        
            

        govt.append(repAuthGovt/10.0)
        opp.append(repAuthOpp/10.0)
        govt.append(ideologyAuthGovt/10.0)
        opp.append(ideologyAuthOpp/10.0)
        govt.append(popAuthGovt/10.0)
        opp.append(popAuthOpp/10.0)
        govt.append(expAuthGovt/10.0)
        opp.append(expAuthOpp/10.0)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        
        plt.rcParams['xtick.major.pad']='8'
        plt.rcParams['ytick.major.pad']='8'
        plt.grid(True, axis="y")
        
        plt.subplot(111)
        plt.figure(facecolor='white')
        plt.subplots_adjust(bottom=0.2)
        rects1 = plt.bar(ind, govt, width, color='black')
                            #yerr=menStd,
                            #error_kw=dict(elinewidth=6, ecolor='pink'

        rects2 = plt.bar(ind+width, opp, width, hatch="/", color ='white', edgecolor = "black")
                            #yerr=womenStd,
                            #error_kw=dict(elinewidth=6, ecolor='yellow'

        # add some
        plt.ylabel(y_label, labelpad=20)
        plt.xlabel(x_label, labelpad=20)
        plt.ylim(ymax=60)
        plt.title(title)
        plt.xticks(ind+width, group_labels, fontsize=14)
        plt.rcParams.update({'font.size': 14})



        plt.legend( (rects1[0], rects2[0]), ('Government MP', 'Opposition MP'), prop={'size':12} )

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, str(round(height, 2)),ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()

            
    
                    
                    
            
            
            
    
