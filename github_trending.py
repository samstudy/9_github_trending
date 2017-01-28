import requests
import datetime

COUNT_OF_REPOS = 20
DAYS = 7

def get_trending_repositories(top_size,exactly_days):
    url = 'https://api.github.com/search/repositories'
    to_date = (datetime.date.today()-datetime.timedelta(exactly_days)).isoformat()
    payload = {'q':'created:>=%s' % to_date,'sort':'stars'}
    repos = requests.get(url,params=payload).json()
    return repos['items'][:top_size]

if __name__ == '__main__':
    most_trending_repos = get_trending_repositories(COUNT_OF_REPOS,DAYS)
    print('The most 20 trending_repositories are:')
    for repo in most_trending_repos:
        print ('Url:',repo['html_url'],'Stars:',repo['stargazers_count'],'open issues:',repo['open_issues'])
    
