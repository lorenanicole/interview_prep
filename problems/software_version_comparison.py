def version_compare(version1, version2):
    # version_format = f'{major}.{minor}.{patch}.{compilation}'

    # Split version strings into list of subsequent parts
    version1 = version1.split('.')
    version2 = version2.split('.')

    # Create a map of each version to understand which version makes to which one 
    # e.g. 2.0 version1 and 2 version1, set 2.0 as the 'longer' version and 2 as 
    # the 'shorter'
    versions = {
        'longer': {'version': None, 'parts': None},
        'shorter': {'version': None, 'parts': None},
    }

    if len(version1) >= len(version2):
        versions['longer']['version'] = 'version1'
        versions['longer']['parts'] = version1
        versions['shorter']['version'] = 'version2'
        versions['shorter']['parts'] = version2
    else:
        versions['shorter']['version'] = 'version1'
        versions['shorter']['parts'] = version1
        versions['longer']['version'] = 'version2'
        versions['longer']['parts'] = version2

    # Pad the version string to make them equal in length 
    num_parts = len(versions['longer']['parts'])
    zeros_to_pad = num_parts - len(versions['shorter']['parts'])

    for n in range(zeros_to_pad):
        versions['shorter']['parts'].append('0')
    
    # print(versions['shorter']['parts'])

    versions['shorter']['parts'] = '.'.join(p for p in versions['shorter']['parts'])
    versions['longer']['parts'] = '.'.join(p for p in versions['longer']['parts'])

    # print(versions)

    # Use Python string comparison to determine if equal, or if version1 or version2 
    # is greater than the other
    if versions['shorter']['parts'] == versions['longer']['parts']:
        return 0
    
    larger_version = None
    if versions['shorter']['parts'] > versions['longer']['parts']:
        larger_version = versions['shorter']['version']
    else:
        larger_version = versions['longer']['version']

    # when version1 > version2
    if larger_version == "version1":
        return 1
    
    # print(versions)
    # when version2 > version1
    if larger_version == "version2":
        return -1


print(version_compare("2", "2.0") == 0)
print(version_compare("2", "2.0.0") == 0)
print(version_compare("2", "2.0.0.0") == 0)
print(version_compare("2.0.0.0", "2.0") == 0)
print(version_compare("2.0", "2.0") == 0)
print(version_compare("2.0", "2") == 0)
print(version_compare("2.0.1", "2") == 1)
print(version_compare("2.0.1", "2.0.0") == 1)
print(version_compare("2.1", "2.0.0.1") == 1)
print(version_compare("2", "2.0.1",) == -1)
print(version_compare("2.0.0", "2.0.1") == -1)
print(version_compare("2.0.0.1", "2.1") == -1)