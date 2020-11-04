import json
from re import findall
from pprint import pprint
from typing import List, Dict, Tuple


def get_apn_names(apn_data: str) -> List[str]:
    apn_regex: str = r"APN Name  : ((.*))"
    apn_name_tuples: List[Tuple[str, ...]] = findall(apn_regex, apn_data)
    apn_names: List[str] = [apn_name_tuple[0] for apn_name_tuple in apn_name_tuples]
    return apn_names


def get_apn_bearers(apn_data: str) -> List[int]:
    apn_bearers_regex: str = r"Default bearers active: \s+ (\d+)"
    apn_bearers_as_string: List[str] = findall(apn_bearers_regex, apn_data)
    apn_bearers: List[int] = [int(apn_bearer) for apn_bearer in apn_bearers_as_string]
    return apn_bearers


if __name__ == '__main__':
    with open("tstapn.txt") as file:
        data_in: str = file.read()

    apn_names: List[str] = get_apn_names(data_in)
    apns_bearers: List[int] = get_apn_bearers(data_in)
    apn_info: Dict[str, int] = {
        apn_name: apn_bearers
        for apn_name, apn_bearers in zip(apn_names, apns_bearers)
        if apn_bearers > 0
    }
    app_info_sorted_by_bearers: Dict[str, int] = {
        apn_name: apn_bearers
        for apn_name, apn_bearers in
        sorted(
            apn_info.items(),
            key=lambda apn_info: apn_info[1],  # sort by value i.e. active bearers
            reverse=True
        )
    }
    pprint(app_info_sorted_by_bearers)

    with open("tstapn_out.txt", "w") as data_out:
        json.dump(app_info_sorted_by_bearers, data_out, indent=4)   # 4 spaces indentation for pretty printing
