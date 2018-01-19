# -*- coding: utf-8 -*-

base="output_dataset2_merged_v4.csv" # stacknet preds
prediction="catboost_v6.csv"#script preds
output="output_1617_v6.csv"# file to generate submissions to

ff=open(base, "r")
ff_pred=open(prediction, "r")
fs=open(output,"w")
fs.write(ff.readline())
ff_pred.readline()

s=0
for line in ff:
    splits=line.replace("\n","").split(",")
    ids=splits[0]
    preds=[]
    for j in range (1,7):
        preds.append(float(splits[j]))


    pre_line_splits=ff_pred.readline().replace("\n","").split(",")
    for j in range (1,7):
        preds[j-1]=(preds[j-1]*0.45 + float(pre_line_splits[j])*0.55)

    fs.write(ids)
    for j in range(6):
        fs.write( "," +str(preds[j] ))
    fs.write("\n")
    s+=1

ff.close()
ff_pred.close()
fs.close()

print ("done")
