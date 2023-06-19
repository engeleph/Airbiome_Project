import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import CCA

##create table which contains samples with otu counts (species level)
df=pd.read_csv('output_analysis/total_counting_table/table.txt', sep='\t', index_col=0, header=0)  #load table with species counts
otu=df.index                                        #create array containg genus names
df=df.T                                             #invert df so that the columns are otus and rows are samples

df["group"]=0

index=0
path_groups="output_test"
number_groups=len(next(os.walk(path_groups))[1])
for group in range(1,number_groups):
    path_samples="output_test/group_{}/kraken2/db1".format(group)
    #number_samples=len(next(os.walk(path_samples))[1])-1
    number_samples=0
    for path in os.scandir(path_samples):
        if path.is_file():
            number_samples += 1
    df["group"].iloc[index:(index+number_samples)]=group
    index=index+number_samples
df["dummy"]=0
df["dummy"].iloc[5:]=10
df["dummy"].iloc[7]=3
df["dummy"].iloc[2]=33
df["dummy2"]=1000
df["dummy2"].iloc[8:]=-10
df["dummy2"].iloc[2]=103
df["dummy2"].iloc[5]=1
df["dummy2"].iloc[7]=0


# Split the data in X and Y
X = df[otu]
#print(X)
Y = df[["group","dummy","dummy2"]]

# Instantiate the Canonical Correlation Analysis with 2 components
my_cca = CCA(n_components=2)

# Fit the model
my_cca.fit(X, Y)
x,y=my_cca.transform(X,Y)

print(x)
print(y)

# Obtain the rotation matrices
#xrot = my_cca.x_rotations_
#yrot = my_cca.y_rotations_

# Put them together in a numpy matrix
#xyrot = np.vstack((xrot,yrot))

dataframe = pd.DataFrame({"x_1":x[:,0],"x_2":x[:,1],"y_1":y[:,0],"y_2":y[:,1]})

#sns.set_context("talk", font_scale=1.2)
plt.figure(figsize=(10,8))
plt.scatter(x="x_2",y="y_2",data=dataframe)
plt.title("Test")
#plt.title('Comp. 1, corr = %.2f' %
#         np.corrcoef(X_c[:, 0], Y_c[:, 0])[0, 1])
#plt.show()
plt.savefig('output_analysis/batch_effect/CCA.png')
'''
nvariables = xyrot.shape[0]

plt.figure(figsize=(15, 15))
plt.xlim((-1,1))
plt.ylim((-1,1))

# Plot an arrow and a text label for each variable
for var_i in range(nvariables):
    x = xyrot[var_i,0]
    y = xyrot[var_i,1]

    plt.arrow(0,0,x,y)
    plt.text(x,y, color='red')

#plt.show()
plt.savefig('output_analysis/batch_effect/CCA.png')
'''
