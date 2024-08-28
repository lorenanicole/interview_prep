# def version_compare(version1, version2):
#     """
#     Function to determine which of version1 or version2 is the most recent version.

#     :param version1: str represent string version of software
#     :param version2: str represent string version of software

#     :return -1 if version2 more recent, 0 if they are the same version, 1 if version1
#             more recent
#     """
#     # Split version strings into list of subsequent parts
#     version1 = version1.split('.')
#     version2 = version2.split('.')

#     # Create a map of each version to understand which version makes to which one 
#     # e.g. 2.0 version1 and 2 version1, set 2.0 as the 'longer' version and 2 as 
#     # the 'shorter'
#     versions = {
#         'longer': {'version': None, 'parts': None},
#         'shorter': {'version': None, 'parts': None},
#     }

#     if len(version1) >= len(version2):
#         versions['longer']['version'] = 'version1'
#         versions['longer']['parts'] = version1
#         versions['shorter']['version'] = 'version2'
#         versions['shorter']['parts'] = version2
#     else:
#         versions['shorter']['version'] = 'version1'
#         versions['shorter']['parts'] = version1
#         versions['longer']['version'] = 'version2'
#         versions['longer']['parts'] = version2

#     # Pad the version string to make them equal in length 
#     num_parts = len(versions['longer']['parts'])
#     zeros_to_pad = num_parts - len(versions['shorter']['parts'])

#     for n in range(zeros_to_pad):
#         versions['shorter']['parts'].append('0')

#     versions['shorter']['parts'] = '.'.join(p for p in versions['shorter']['parts'])
#     versions['longer']['parts'] = '.'.join(p for p in versions['longer']['parts'])

#     # Use Python string comparison to determine if equal, or if version1 or version2 
#     # is greater than the other
#     if versions['shorter']['parts'] == versions['longer']['parts']:
#         return 0
    
#     larger_version = None
#     if versions['shorter']['parts'] > versions['longer']['parts']:
#         larger_version = versions['shorter']['version']
#     else:
#         larger_version = versions['longer']['version']

#     # when version1 > version2
#     if larger_version == "version1":
#         return 1
    
#     # when version2 > version1
#     if larger_version == "version2":
#         # return -1


def version_compare(v1, v2):
    # Split version strings into list of subsequent parts
    v1_arr, v2_arr = v1.split("."), v2.split(".") 
    
    # Cast each version string list to integer from string
    v1_arr = list(map(lambda part: int(part), v1_arr))
    v2_arr = list(map(lambda part: int(part), v2_arr))
 
    v1_size = len(v1_arr)
    v2_size = len(v2_arr)
    # Compare which version list is larger and populate the 
    # smaller version list with zero to allow for proper comparison
    if v1_size > v2_size:
        zeros_to_pad = v1_size - v2_size
        v2_arr += [0] * zeros_to_pad
    elif v2_size > v1_size:
        zeros_to_pad = v2_size - v1_size
        v1_arr += [0] * zeros_to_pad

    # Return 1 if version 1 is larger
    # Return -1 if version 2 is bigger 
    # Return 0 if the versions are equal 
    for i in range(len(v1_arr)):
        if v1_arr[i] > v2_arr[i]:
            return 1
        elif v2_arr[i] > v1_arr[i]:
            return -1

    return 0

# Driver program to check above comparison function
version1 = "1.0.3"
version2 = "1.0.7"

print(version_compare(version1, version2) == -1)
# if ans < 0:
#     print (version1 + " is smaller")
# elif ans > 0:
#     print (version2 + " is smaller")
# else:
#     print ("Both versions are equal")


print(version_compare("2", "2.0") == 0)
print(version_compare("2", "2.0.0") == 0)
print(version_compare("2", "2.0.0.0") == 0)
print(version_compare("2.0.0.0", "2.0") == 0)
print(version_compare("2.0", "2.0") == 0)
print(version_compare("2.0", "2") == 0)
print(version_compare("2.0.1", "2") == 1)
print(version_compare("2.0.1", "2.0.0") == 1)
print(version_compare("2.1", "2.0.0.1") == 1)
print(version_compare("2", "2.0.1") == -1)
print(version_compare("2.0.0", "2.0.1") == -1)
print(version_compare("2.0.0.1", "2.1") == -1)