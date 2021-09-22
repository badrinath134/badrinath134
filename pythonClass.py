import json
from pprint import pprint
import getopt, sys

class smf_service_stats:
    def __init__(self):
        global items
        items = {}

    def getProcType(self):
        return self.procedure_type

    def addItem(self, item, value):
        self.item = str(item)
        self.value = str(value)
        items[self.item] = value

    def delItem(self, item):
        items.remove(item)

    def displayItems(self):
        return items
    
    def getClassName(self):
        return self.__class__.__name__




smfServiceStats = smf_service_stats()
argumentList = sys.argv[1:]
long_options = ["cluster", "dnn", "gr_instance_id", "pdu_type", "procedure_type", "rat_type", "service_name", "status"]
try:
    arguments, values = getopt.getopt(argumentList, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("cluster"):
            print (("Enabling special output mode (% s)") % (currentValue))
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("dnn"):
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("gr_instance_id"):
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("pdu_type"):
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("procedure_type"):
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("rat_type"):
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("service_name"):
            smfServiceStats.addItem(currentArgument, currentValue)
        elif currentArgument in ("status"):
            smfServiceStats.addItem(currentArgument, currentValue)

except getopt.error as err:
    print (str(err))


smfServiceStats.displayItems()
#smfServiceStats.addItem("pdu_type", "ipv4v6")
#smfServiceStats.addItem("procedure_type", smfServiceStats.getProcType())

#print (smfServiceStats.getClassName() + str(smfServiceStats.displayItems()).replace(": ", "=", 2))


