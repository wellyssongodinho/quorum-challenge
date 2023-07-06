# import module
import pandas as pd

# read dataset
folder_path = 'datas/'
df_legislators = pd.read_csv(folder_path+'legislators.csv')
df_bills = pd.read_csv(folder_path+'bills.csv')
df_votes = pd.read_csv(folder_path+'votes.csv')
df_vote_results = pd.read_csv(folder_path+'vote_results.csv')

#column names file results
columns = ['id', 'name', 'num_supported_bills', 'num_opposed_bills']
df_legislators_count = pd.DataFrame(columns=columns)

for ind in df_legislators.index:
    df_votes_yea = df_vote_results.loc[(df_vote_results['legislator_id'] == df_legislators['id'][ind]) & (df_vote_results['vote_type'] == 1)]
    df_votes_nay = df_vote_results.loc[(df_vote_results['legislator_id'] == df_legislators['id'][ind]) & (df_vote_results['vote_type'] == 2)]
    new_row_legislators_count = {columns[0]: str(ind+1),columns[1]:df_legislators['name'][ind],columns[2]:str(len(df_votes_yea)),columns[3]: str(len(df_votes_nay))}
    df_legislators_count.loc[len(df_legislators_count)] = new_row_legislators_count

# create legislators-support-oppose-count file csv
df_legislators_count.to_csv('legislators-support-oppose-count-opt2.csv',index=False)
