from github import Github
import xml.etree.ElementTree as ET

# ----------------------------
# Configuration
# ----------------------------
ACCESS_TOKEN = "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"  # GitHub personal access token
REPO_NAME = "sivabalaji280/apitest"            # Format: owner/repo
PR_NUMBER = 7                                # Pull request number

# ----------------------------
# Helper functions
# ----------------------------
def parse_members(xml_content):
    """
    Parse XML content and return a dict: {Member Name: serialized content}
    """
    members_dict = {}
    root = ET.fromstring(xml_content)
    for member in root.findall(".//Member"):
        name = member.attrib.get("Name")
        content = ET.tostring(member, encoding="unicode")
        members_dict[name] = content
    return members_dict

def get_modified_members(old_xml, new_xml):
    """
    Compare old and new XML content and return list of modified Member Names
    """
    old_members = parse_members(old_xml)
    new_members = parse_members(new_xml)

    modified = []
    for name, new_content in new_members.items():
        old_content = old_members.get(name)
        if old_content != new_content:
            modified.append(name)
    return modified

# ----------------------------
# Main logic
# ----------------------------
g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

# print(f"Modified <Member> blocks in PR #{PR_NUMBER}:")

# value = pr.get_files()
# for file in value:
#     print(file.contents_url.replace("https://api.github.com/repos/", "https://raw.githubusercontent.com/").replace(f"/{pr.base.ref}", f"/{pr.base.ref}"))


for file in pr.get_files():
    print(file.filename)
    if file.filename.endswith(".xml"):
        # Fetch old and new content
        old_xml = file.contents_url.replace("https://api.github.com/repos/", "https://raw.githubusercontent.com/").replace(f"/{pr.base.ref}", f"/{pr.base.ref}")
        new_xml = file.contents_url.replace("https://api.github.com/repos/", "https://raw.githubusercontent.com/").replace(f"/{pr.head.ref}", f"/{pr.head.ref}")

        # Simple way to fetch raw XML content
        import requests
        old_resp = requests.get(old_xml)
        new_resp = requests.get(new_xml)
        if old_resp.status_code == 200 and new_resp.status_code == 200:
            modified_names = get_modified_members(old_resp.text, new_resp.text)
            if modified_names:
                print(f"\nFile: {file.filename}")
                for name in modified_names:
                    print(f"- {name}")
        else:
            print(f"Could not fetch content for {file.filename}")
