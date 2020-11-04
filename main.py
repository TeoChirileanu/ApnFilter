from re import findall
from pprint import pprint
from typing import List, Dict

if __name__ == '__main__':
    with open("tstapn.txt") as file:
        data: str = file.read()

    apn_regex: str = r"APN Name  : ((.*))"
    apn_name_tuples = findall(apn_regex, data)
    apn_names: List[str] = [apn_name_tuple[0] for apn_name_tuple in apn_name_tuples]

    active_bearers_regex: str = r"Default bearers active: \s+ (\d+)"
    active_bearers_nos_as_string: List[str] = findall(active_bearers_regex, data)
    active_bearers_nos: List[int] = list(map(lambda x: int(x), active_bearers_nos_as_string))

    apn_info: Dict[str, int] = {}
    for apn_name, active_bearers_no in zip(apn_names, active_bearers_nos):
        apn_info[apn_name] = active_bearers_no

    # todo: investigate inspection error
    apn_info_without_zero_bearers: Dict[str, int] = dict(filter(lambda kvp: kvp[1] > 0, apn_info.items()))

    # todo: convert to dictionary
    apn_info_without_zero_bearers_sorted = sorted(apn_info_without_zero_bearers.items(), key=lambda kvp: kvp[1], reverse=True)

    with open("tstapn_out.txt", "w") as out:
        pprint(apn_info_without_zero_bearers_sorted, stream=out, sort_dicts=False)

