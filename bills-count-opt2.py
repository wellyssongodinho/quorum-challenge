# import module
import pandas as pd

# read datasetd
folder_path = 'datas/'
df_legislators = pd.read_csv(folder_path+'legislators.csv')
df_bills = pd.read_csv(folder_path+'bills.csv')
df_votes = pd.read_csv(folder_path+'votes.csv')
df_vote_results = pd.read_csv(folder_path+'vote_results.csv')

#group by vote results
df_vote_results_gb = df_vote_results.groupby(['vote_id','vote_type'])['legislator_id'].agg('count').reset_index()

#column names file results
columns = ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor']
df_bills_count = pd.DataFrame(columns=columns)

#id bill counts result
id=0

for ind_bill in df_bills.index:
    df_bill_votes = df_votes.loc[(df_votes['bill_id'] == df_bills['id'][ind_bill])]
    for ind_bill_votes in df_bill_votes.index:
      id=id+1
      df_legislator_yea = df_vote_results_gb.loc[(df_vote_results_gb['vote_id'] == df_bill_votes['id'][ind_bill_votes]) & (df_vote_results_gb['vote_type'] == 1)]
      df_legislator_nay = df_vote_results_gb.loc[(df_vote_results_gb['vote_id'] == df_bill_votes['id'][ind_bill_votes]) & (df_vote_results_gb['vote_type'] == 2)]
      new_row_bills_count = {columns[0]: str(id),columns[1]:df_bills['title'][ind_bill],columns[2]:str(df_legislator_yea['legislator_id'].values[0]),columns[3]: str(df_legislator_nay['legislator_id'].values[0]),columns[4]: df_bills['sponsor_id'][ind_bill]}
      df_bills_count.loc[len(df_bills_count)] = new_row_bills_count

# create bills-support-oppose-count file csv
df_bills_count.to_csv('bills-support-oppose-count-opt2.csv',index=False)