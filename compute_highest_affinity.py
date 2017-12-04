# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    user_to_site = {u: [] for u in user_list}
    for i in range(0,len(site_list)):
        if site_list[i] not in user_to_site[user_list[i]]:
            user_to_site[user_list[i]].append(site_list[i])

    site_affinity = {}
    for user,sites in user_to_site.items():
        for site1 in sites:
            for site2 in sites[sites.index(site1)+1:]:
                key_var = tuple(sorted([site1, site2]))
                if key_var in site_affinity.keys():
                    site_affinity[key_var] += 1
                else:
                    site_affinity[key_var] = 1
    max_affinity = max(site_affinity, key=site_affinity.get)
    return max_affinity

