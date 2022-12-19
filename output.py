import json


def gen_info(type, top, left, bottom, right, prob):
    text = {}
    text["type"] = type
    location = {}
    location["top"] = top
    location["left"] = left
    location["bottom"] = bottom
    location["right"] = right
    text["location"] = location
    text["probability"] = prob
    return text


def gen_list(arr):
    res = {}
    text_arr = []
    for text in arr:
        text_arr.append(text)
    res["info"] = text_arr
    res_json = json.dumps(res, ensure_ascii=False)
    return res_json