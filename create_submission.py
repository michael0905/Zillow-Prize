# -*- coding: utf-8 -*-

#generates submission based on 1-column prediction csv

sample="input/sample_submission.csv" # name of sample sybmission
prediction2016="pred2016.csv"# prediction file
prediction2017='pred2017.csv'
output="output_dataset2.csv"# output submission

#the predictions are copied 6 times

ff=open(sample, "r")
ff_pred2016=open(prediction2016, "r")
ff_pred2017=open(prediction2017, "r")
fs=open(output,"w")
fs.write(ff.readline())
s=0
for line in ff: #read sample submission file
    splits=line.split(",")
    ids=splits[0] # get id
    pre_line2016=ff_pred2016.readline().replace("\n","") # parse prediction file and get prediction for the row
    pre_line2017=ff_pred2017.readline().replace("\n","")
    fs.write(ids) # write id
    for j in range(3): # copy the prediction 3 times
        fs.write( "," +pre_line2016 )
    for j in range(3): # copy the prediction 3 times
        fs.write( "," +pre_line2017 )
    fs.write("\n")
    s+=1
ff.close()
ff_pred2016.close()
ff_pred2017.close()
fs.close()
print ("done")
