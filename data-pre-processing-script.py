import pandas as pd

df = pd.read_csv('data/WhatsgoodlyData-6.csv')

# Filter the dataset to include only the required segment description and extract the percentage values
global_results = df[df['Segment Description'] == 'Global results'].set_index('Answer')['Percentage'].rename('Global')

female_voters = df[df['Segment Description'] == 'Female voters'].set_index('Answer')['Percentage'].rename('Female')
male_voters = df[df['Segment Description'] == 'Male voters'].set_index('Answer')['Percentage'].rename('Male')

college_students = df[df['Segment Description'] == "I'm in? College"].set_index('Answer')['Percentage'].rename('College students')

high_school_students = df[df['Segment Description'] == "I'm in? High School"].set_index('Answer')['Percentage'].rename('High School students')

post_grad_students = df[df['Segment Description'] == "I'm in? Post-grad"].set_index('Answer')['Percentage'].rename('Post-graduate students')

# Set the social media platform as the index and extract the percentage values
# global_percents = global_results.set_index('Answer')['Percentage'].rename('Global')

# Concatenate all the columns extracted earlier and store into a single dataframe
final_result = pd.concat([global_results, female_voters, male_voters, college_students, high_school_students, post_grad_students], axis=1)

# Convert the dataframe to a csv and save it
final_result.to_csv("processed-data.csv")

print("Data has ben processed and is ready to be used.")