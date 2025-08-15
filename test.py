from github import Github


ACCESS_TOKEN = "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"  # GitHub personal access token
REPO_NAME = "sivabalaji280/apitest"   
g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)

def get_pr_list():
    pr_list = []
    pr = repo.get_pulls(state='open')
    for p in pr:
        pr_list.append(p.number)
    return pr_list

PR_NUMBER = get_pr_list()   
print(PR_NUMBER)         # Format: owner/repo



pr = repo.get_pulls(state='open')

for p in pr:
    print(p.number)
    print(p.state)


# pulls = repo.get_pulls(state='open')

# for pr in pulls:
#     print(pr.number)
#     # print(f"PR Number: {pr.number}")
#     # print(f"Title: {pr.title}")
#     # print(f"User: {pr.user.login}")
#     # print(f"State: {pr.state}")
#     # print(f"Created At: {pr.created_at}")
#     # print(f"URL: {pr.html_url}")
#     # print("-" * 50)

