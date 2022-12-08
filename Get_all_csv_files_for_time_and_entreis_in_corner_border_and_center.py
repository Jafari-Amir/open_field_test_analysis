import glob
import numpy as np
import pandas as pd

path = '/Users/YOUR_SYSTEM_NAME/NEW_FOLDER/'  # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filenamess in all_files:
    df = pd.read_csv(filenamess, index_col=None)
    df2= df.drop(df.index[np.where(df.index > 9000)])
    GTP_df= df2.groupby(pd.Grouper(key='ROI_location')).size()
    li.append(GTP_df)
all_frame = pd.concat(li, axis=1).T.fillna(0).reset_index(drop=True)

df_melted = all_frame.melt(id_vars=[], value_vars=['c1','c2','c3','c4', 'b1', 'b2' ,'b3','b4', 'center',
                                                   'b1_center', 'b2_center','b3_center', 'b4_center','c1_b1','c1_b4',
                                                    'c4_b4', 'c4_b3', 'c3_b3', 'c3_b2','c2_b2',
                                                    'c2_b1' ,'non_roi'], var_name='Label', value_name='Value')
# print the melted DataFrame
print(df_melted)
df_melted.to_csv('/Users//Users/YOUR_SYSTEM_NAME/NEW_FOLDER/grouping_areas.csv', header=False, index=False)