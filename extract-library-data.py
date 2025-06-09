import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime, timedelta

# Set env variables, using .env here
load_dotenv()
figma_access_token = os.getenv("FIGMA_ACCESS_TOKEN")
file_key = os.getenv("FILE_KEY") # something like '6p8e19mTHzCJfRfShcRH9K'

# Endpoint
base_url = 'https://api.figma.com/v1/analytics/libraries/'

# Set the dates
start_date = '2021-07-01'
end_date = '2023-07-31'

def month_ranges(start, end):
    """Yield (month_start, month_end) pairs from start to end (inclusive)."""
    current = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    while current <= end_dt:
        month_start = current.replace(day=1)
        next_month = (month_start + timedelta(days=32)).replace(day=1)
        month_end = min(next_month - timedelta(days=1), end_dt)
        yield month_start.strftime("%Y-%m-%d"), month_end.strftime("%Y-%m-%d")
        current = next_month

# COMPONENTS
def actions_by_component(start_date, end_date):
    params = f"/component/actions?group_by=component&start_date={start_date}&end_date={end_date}&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    output = pd.DataFrame()

    while url:
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'component_key', 'component_name', 'detachments','insertions'])
        output = pd.concat([output, normalisedRows])

        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv(f"output/actions_by_component_{start_date}.csv", encoding='utf-8',  index=False)

def actions_by_team(start_date, end_date):
    params = f"/actions?group_by=team&start_date={start_date}&end_date={end_date}&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    output = pd.DataFrame()

    while url:
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'team_name', 'workspace_name', 'detachments','insertions'])
        output = pd.concat([output, normalisedRows])

        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv(f"output/actions_by_team_{start_date}.csv", encoding='utf-8',  index=False)

def usages_by_component(start_date, end_date):
    params = f"/usages?group_by=component&start_date={start_date}&end_date={end_date}&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    output = pd.DataFrame()

    while url:
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['components'], meta=['component_key', 'component_name', 'num_instances', 'num_teams_using','num_files_using'])
        output = pd.concat([output, normalisedRows])

        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv(f"output/usages_by_component_{start_date}.csv", encoding='utf-8',  index=False)

def usages_by_file(start_date, end_date):
    params = f"/usages?group_by=file&start_date={start_date}&end_date={end_date}&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    output = pd.DataFrame()

    while url:
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['files'], meta=['team_name', 'workspace_name', 'file_name', 'num_instances'])
        output = pd.concat([output, normalisedRows])

        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv(f"output/usages_by_file_{start_date}.csv", encoding='utf-8',  index=False)

# VARIABLES
def variable_actions_by_variable(start_date, end_date):
    params = f"/variable/actions?group_by=variable&start_date={start_date}&end_date={end_date}&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    while url:
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'variable_key', 'variable_name', 'detachments','insertions', 'collection_key', 'collection_name'])
        output = pd.concat([output, normalisedRows])

        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv(f"output/variable_actions_by_variable_{start_date}.csv", encoding='utf-8',  index=False)

def variable_actions_by_team(start_date, end_date):
    params = f"/variable/actions?group_by=team&start_date={start_date}&end_date={end_date}&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    while url:
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'variable_key', 'variable_name', 'detachments','insertions', 'collection_key', 'collection_name'])
        output = pd.concat([output, normalisedRows])

        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv(f"output/variable_actions_by_team_{start_date}.csv", encoding='utf-8',  index=False)

def main():
    for month_start, month_end in month_ranges(start_date, end_date):
        print(f"Processing {month_start} to {month_end}")
        actions_by_component(month_start, month_end)
        actions_by_team(month_start, month_end)
        usages_by_component(month_start, month_end)
        usages_by_file(month_start, month_end)
        variable_actions_by_variable(month_start, month_end)
        variable_actions_by_team(month_start, month_end)

if __name__ == "__main__":
    main()
