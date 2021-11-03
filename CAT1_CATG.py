import sys
import os
import datetime

print "STARTED AT ",str(datetime.datetime.now()),"\N"

PATH = "/Python/Scripts/MitraKavian_CSVCompare/CAT1_CATG/REF/"
SAVE_PATH = "/Python/Scripts/MitraKavian_CSVCompare/Splited/"
CAT_ONE_PATH = "/Python/Scripts/MitraKavian_CSVCompare/Splited/CAT1/"
CAT1_SPLITED_PATH = "/Python/Scripts/MitraKavian_CSVCompare/CAT1_SPLITTED/"
CAT1_SPLITED_FILENAME = "CAT_ONE_SPLITED.csv"

HEADERS_LIST = list()

FILE_LIST = os.listdir(PATH)
for each in FILE_LIST:
##    print each,"\n"
    with open(PATH + str(each),'r') as f:
        LINES_LIST = f.readlines()
        LINES_LIST = [x.split("\r") for x in LINES_LIST]
        f.close()

    for each in LINES_LIST[0]:
        if str(each.split(",")[0]) not in ["gene","type"]:
            HEADERS_LIST.append(str(each.split(",")[0]))

del HEADERS_LIST[0]
# print HEADERS_LIST[2],"\n"
# print len(HEADERS_LIST),"\n"

CAT_ONE_FILES = os.listdir(CAT_ONE_PATH)
##print CAT_ONE_FILES,"\n"
##print len(CAT_ONE_FILES),"\n"

counter = 0
for each in CAT_ONE_FILES:
    with open(CAT_ONE_PATH + str(each),"r") as f:
        FILE_LINES = f.readlines()
        # print len(FILE_LINES),"\n"
        f.close()
    try:
        # print FILE_LINES[0].strip().split(",")[1].split('"')[1]
        if (FILE_LINES[0].strip().split(",")[1].split('"')[1]) not in HEADERS_LIST:
            # print str(FILE_LINES[0].strip().split(",")[1]), "\n"
            counter += 1
            # print "YES","\n"
            WRITE_LIST = list()
            for i in range(0,len(FILE_LINES[0].split(","))):
                if str(FILE_LINES[0].strip().split(",")[i].split('"')[1]) not in HEADERS_LIST:
                    FINAL_LIST = list()
                    for h in range(len(FILE_LINES)):
                        FINAL_LIST.append(str(FILE_LINES[h].strip().split(",")[i]))
                    WRITE_LIST.append(FINAL_LIST)

            with open(CAT1_SPLITED_PATH + str(each.split(".")[0]) + str(each.split(".")[1]) + "_SPLITTED.csv",'a') as f:
                WRITE_STRING = ""
                for clm in range(len(WRITE_LIST[0])):
                    for rw in range(len(WRITE_LIST)):
                        if rw == 0 :
                            WRITE_STRING = WRITE_STRING + (WRITE_LIST[rw][clm])
                        else:
                            WRITE_STRING = WRITE_STRING + "," + str(WRITE_LIST[rw][clm])
                    WRITE_STRING = WRITE_STRING + "\n"
                f.write(WRITE_STRING)
                f.close()
        else:
            continue

    except IndexError:
        print "NO","\n"
        continue

print counter,"\n"


# ##print FILE_LINES[0].strip().split(",")
# print len(FINAL_LIST),"\n"
# print FINAL_LIST,"\n"
#
# FINAL_STRING = ""
# for j in range(0,len(FINAL_LIST)):
#     if j ==0 :
#         FINAL_STRING = str(FINAL_LIST[j])
#     else:
#         FINAL_STRING = FINAL_STRING + "," + str(FINAL_LIST[j])
# with open(CAT1_SPLITED_PATH + CAT1_SPLITED_FILENAME,"a") as f:
#     f.write(FINAL_STRING)
#     f.close()

print "FINISHED AT ",str(datetime.datetime.now())
print 120*"*"






