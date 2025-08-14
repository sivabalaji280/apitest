from github import Github
import xml.etree.ElementTree as ET


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


oldxml = "/home/balaji280/pyscripts/python/githubscripts/apitest/old.xml"
newxml = "/home/balaji280/pyscripts/python/githubscripts/apitest/new.xml"

with open(oldxml, 'r') as file:
    old_content = file.read()


with open(newxml, 'r') as file:
    new_content = file.read()

x = get_modified_members(old_content, new_content)
print(x)

