# import module
import csv

import pandas as pd

# read dataset
folder_path = 'datas/'
df_legislators = pd.read_csv(folder_path+'legislators.csv')
df_bills = pd.read_csv(folder_path+'bills.csv')
df_votes = pd.read_csv(folder_path+'votes.csv')
df_vote_results = pd.read_csv(folder_path+'vote_results.csv')

#column names file results
columns = ['id', 'name', 'num_supported_bills', 'num_opposed_bills']

# create legislators-support-oppose-count file csv
with open('legislators-support-oppose-count-opt1.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(columns)

    for ind in df_legislators.index:
        #How there will only be up to 1 Vote provided for each Bill the code was simplified
        df_votes_yea = df_vote_results.loc[(df_vote_results['legislator_id'] == df_legislators['id'][ind]) & (df_vote_results['vote_type'] == 1)]
        df_votes_nay = df_vote_results.loc[(df_vote_results['legislator_id'] == df_legislators['id'][ind]) & (df_vote_results['vote_type'] == 2)]
        writer.writerow([str(ind+1),df_legislators['name'][ind],str(len(df_votes_yea)),str(len(df_votes_nay))])
