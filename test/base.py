from hstest import *
import json
import requests

# REQUEST DATA
rgb_values = [
    [0, 0, 0],

    [181, 78, 60],
    [255, 92, 64],
    [71, 92, 83],

    [128, 128, 128],

    [197, 96, 240],
    [52, 108, 199],
    [255, 150, 210],

    [255, 255, 255],
]
hsv_values = [
    [0, 0, 0],

    [95, 67, 81],
    [9, 75, 100],
    [158, 83, 0],

    [0, 0, 50],

    [192, 69, 54],
    [257, 0, 98],
    [316, 31, 99],

    [0, 0, 100],
]
hex_values = [
    "#000000",

    "#B54E4C",
    "#FF8C40",
    "#579C51",

    "#808080",

    "#C360F0",
    "#346EC7",
    "#F095D2",

    "#FFFFFF",
]
hsl_values = [
    [0, 0, 0],

    [90, 54, 0],
    [9, 100, 100],
    [154, 13, 32],

    [0, 0, 50],

    [290, 83, 55],
    [217, 2, 94],
    [360, 100, 20],

    [0, 0, 100],
]
# RESPONSE DATA
# RGB
RGB_HSV = [{'color': [0.0, 0.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [181.0, 78.0, 60.0], 'converted_color': [9, 67, 71]},
           {'color': [255.0, 92.0, 64.0], 'converted_color': [9, 75, 100]},
           {'color': [71.0, 92.0, 83.0], 'converted_color': [154, 23, 36]},
           {'color': [128.0, 128.0, 128.0], 'converted_color': [0, 0, 50]},
           {'color': [197.0, 96.0, 240.0], 'converted_color': [282, 60, 94]},
           {'color': [52.0, 108.0, 199.0], 'converted_color': [217, 74, 78]},
           {'color': [255.0, 150.0, 210.0], 'converted_color': [326, 41, 100]},
           {'color': [255.0, 255.0, 255.0], 'converted_color': [0, 0, 100]}]
RGB_HEX = [{'color': [0.0, 0.0, 0.0], 'converted_color': '#000000'},
           {'color': [181.0, 78.0, 60.0], 'converted_color': '#B54E3C'},
           {'color': [255.0, 92.0, 64.0], 'converted_color': '#FF5C40'},
           {'color': [71.0, 92.0, 83.0], 'converted_color': '#475C53'},
           {'color': [128.0, 128.0, 128.0], 'converted_color': '#808080'},
           {'color': [197.0, 96.0, 240.0], 'converted_color': '#C560F0'},
           {'color': [52.0, 108.0, 199.0], 'converted_color': '#346CC7'},
           {'color': [255.0, 150.0, 210.0], 'converted_color': '#FF96D2'},
           {'color': [255.0, 255.0, 255.0], 'converted_color': '#FFFFFF'}]
RGB_HSL = [{'color': [0.0, 0.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [181.0, 78.0, 60.0], 'converted_color': [9, 50, 47]},
           {'color': [255.0, 92.0, 64.0], 'converted_color': [9, 100, 63]},
           {'color': [71.0, 92.0, 83.0], 'converted_color': [154, 13, 32]},
           {'color': [128.0, 128.0, 128.0], 'converted_color': [0, 0, 50]},
           {'color': [197.0, 96.0, 240.0], 'converted_color': [282, 83, 66]},
           {'color': [52.0, 108.0, 199.0], 'converted_color': [217, 59, 49]},
           {'color': [255.0, 150.0, 210.0], 'converted_color': [326, 100, 79]},
           {'color': [255.0, 255.0, 255.0], 'converted_color': [0, 0, 100]}]
# HSV
HSV_RGB = [{'color': [0.0, 0.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [95.0, 67.0, 81.0], 'converted_color': [126, 207, 68]},
           {'color': [9.0, 75.0, 100.0], 'converted_color': [255, 92, 64]},
           {'color': [158.0, 83.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [0.0, 0.0, 50.0], 'converted_color': [128, 128, 128]},
           {'color': [192.0, 69.0, 54.0], 'converted_color': [43, 119, 138]},
           {'color': [257.0, 0.0, 98.0], 'converted_color': [250, 250, 250]},
           {'color': [316.0, 31.0, 99.0], 'converted_color': [252, 174, 232]},
           {'color': [0.0, 0.0, 100.0], 'converted_color': [255, 255, 255]}]
HSV_HEX = [{'color': [0.0, 0.0, 0.0], 'converted_color': '#000000'},
           {'color': [95.0, 67.0, 81.0], 'converted_color': '#7ECF44'},
           {'color': [9.0, 75.0, 100.0], 'converted_color': '#FF5C40'},
           {'color': [158.0, 83.0, 0.0], 'converted_color': '#000000'},
           {'color': [0.0, 0.0, 50.0], 'converted_color': '#808080'},
           {'color': [192.0, 69.0, 54.0], 'converted_color': '#2B778A'},
           {'color': [257.0, 0.0, 98.0], 'converted_color': '#FAFAFA'},
           {'color': [316.0, 31.0, 99.0], 'converted_color': '#FCAEE8'},
           {'color': [0.0, 0.0, 100.0], 'converted_color': '#FFFFFF'}]
HSV_HSL = [{'color': [0.0, 0.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [95.0, 67.0, 81.0], 'converted_color': [95, 59, 54]},
           {'color': [9.0, 75.0, 100.0], 'converted_color': [9, 100, 62]},
           {'color': [158.0, 83.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [0.0, 0.0, 50.0], 'converted_color': [0, 0, 50]},
           {'color': [192.0, 69.0, 54.0], 'converted_color': [192, 53, 35]},
           {'color': [257.0, 0.0, 98.0], 'converted_color': [0, 0, 98]},
           {'color': [316.0, 31.0, 99.0], 'converted_color': [316, 94, 84]},
           {'color': [0.0, 0.0, 100.0], 'converted_color': [0, 0, 100]}]
# HEX
HEX_RGB = [{'color': '#000000', 'converted_color': [0, 0, 0]},
           {'color': '#B54E4C', 'converted_color': [181, 78, 76]},
           {'color': '#FF8C40', 'converted_color': [255, 140, 64]},
           {'color': '#579C51', 'converted_color': [87, 156, 81]},
           {'color': '#808080', 'converted_color': [128, 128, 128]},
           {'color': '#C360F0', 'converted_color': [195, 96, 240]},
           {'color': '#346EC7', 'converted_color': [52, 110, 199]},
           {'color': '#F095D2', 'converted_color': [240, 149, 210]},
           {'color': '#FFFFFF', 'converted_color': [255, 255, 255]}]
HEX_HSV = [{'color': '#000000', 'converted_color': [0, 0, 0]},
           {'color': '#B54E4C', 'converted_color': [1, 58, 71]},
           {'color': '#FF8C40', 'converted_color': [24, 75, 100]},
           {'color': '#579C51', 'converted_color': [115, 48, 61]},
           {'color': '#808080', 'converted_color': [0, 0, 50]},
           {'color': '#C360F0', 'converted_color': [281, 60, 94]},
           {'color': '#346EC7', 'converted_color': [216, 74, 78]},
           {'color': '#F095D2', 'converted_color': [320, 38, 94]},
           {'color': '#FFFFFF', 'converted_color': [0, 0, 100]}]
HEX_HSL = [{'color': '#000000', 'converted_color': [0, 0, 0]},
           {'color': '#B54E4C', 'converted_color': [1, 42, 50]},
           {'color': '#FF8C40', 'converted_color': [24, 100, 63]},
           {'color': '#579C51', 'converted_color': [115, 32, 46]},
           {'color': '#808080', 'converted_color': [0, 0, 50]},
           {'color': '#C360F0', 'converted_color': [281, 83, 66]},
           {'color': '#346EC7', 'converted_color': [216, 59, 49]},
           {'color': '#F095D2', 'converted_color': [320, 75, 76]},
           {'color': '#FFFFFF', 'converted_color': [0, 0, 100]}]
# HSL
HSL_RGB = [{'color': [0.0, 0.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [90.0, 54.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [9.0, 100.0, 100.0], 'converted_color': [255, 255, 255]},
           {'color': [154.0, 13.0, 32.0], 'converted_color': [71, 92, 83]},
           {'color': [0.0, 0.0, 50.0], 'converted_color': [128, 128, 128]},
           {'color': [290.0, 83.0, 55.0], 'converted_color': [204, 45, 235]},
           {'color': [217.0, 2.0, 94.0], 'converted_color': [239, 240, 240]},
           {'color': [360.0, 100.0, 20.0], 'converted_color': [0, 0, 0]},
           {'color': [0.0, 0.0, 100.0], 'converted_color': [255, 255, 255]}]
HSL_HSV = [{'color': [0.0, 0.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [90.0, 54.0, 0.0], 'converted_color': [0, 0, 0]},
           {'color': [9.0, 100.0, 100.0], 'converted_color': [0, 0, 100]},
           {'color': [154.0, 13.0, 32.0], 'converted_color': [154, 23, 36]},
           {'color': [0.0, 0.0, 50.0], 'converted_color': [0, 0, 50]},
           {'color': [290.0, 83.0, 55.0], 'converted_color': [290, 81, 92]},
           {'color': [217.0, 2.0, 94.0], 'converted_color': [217, 0, 94]},
           {'color': [360.0, 100.0, 20.0], 'converted_color': [0, 0, 0]},
           {'color': [0.0, 0.0, 100.0], 'converted_color': [0, 0, 100]}]
HSL_HEX = [{'color': [0.0, 0.0, 0.0], 'converted_color': '#000000'},
           {'color': [90.0, 54.0, 0.0], 'converted_color': '#000000'},
           {'color': [9.0, 100.0, 100.0], 'converted_color': '#FFFFFF'},
           {'color': [154.0, 13.0, 32.0], 'converted_color': '#475C53'},
           {'color': [0.0, 0.0, 50.0], 'converted_color': '#808080'},
           {'color': [290.0, 83.0, 55.0], 'converted_color': '#CC2DEB'},
           {'color': [217.0, 2.0, 94.0], 'converted_color': '#EFF0F0'},
           {'color': [360.0, 100.0, 20.0], 'converted_color': '#000000'},
           {'color': [0.0, 0.0, 100.0], 'converted_color': '#FFFFFF'}]


# def stage_convert(self):
#     url = self.get_url('convert-color/')
#     response_colors_conv = []
#     for i in range(len(rgb_values)):
#         response = requests.post(url, json={"representation": "hsl",
#                                             "color": hsl_values[i],
#                                             "conversion": "hex"})
#         response_colors_conv.append(response.json())
#
#     print(response_colors_conv)
#     return CheckResult.correct()

class ColorizerTest(DjangoTest):
    # STAGE 1 *****************************************************************************************************
    msg_500 = "encountered a server error, HTTP code 500"
    msg_200_invalid = "Received HTTP code 200, but response json data was incorrect"
    msg_400_expected = ('When receiving invalid data, your API should return json data:'
                        ' {"error": "Invalid data."}. and a status code: 400')

    def stage1_modify_test(self):
        url = self.get_url('modify-color/')
        colors = [[192, 100, 54], [257, 0, 98], [316, 31, 99]]
        operation = ["saturate", "desaturate", "saturate"]
        expected_data = [{'representation': 'hsv',
                          'color': [192.0, 100.0, 54.0],
                          'operation': 'saturate',
                          'modified_color': [192.0, 100, 54.0]},
                         {'representation': 'hsv',
                          'color': [257.0, 0.0, 98.0],
                          'operation': 'desaturate',
                          'modified_color': [257.0, 0, 98.0]},
                         {'representation': 'hsv',
                          'color': [316.0, 31.0, 99.0],
                          'operation': 'saturate',
                          'modified_color': [316.0, 33, 99.0]}]
        for i in range(len(colors)):
            response = requests.post(url, json={"representation": "hsv",
                                                "color": colors[i],
                                                "operation": operation[i],
                                                "amount": 5
                                                })
            if response.status_code == 500:
                return CheckResult.wrong(self.msg_500 + ". path_info: /modify-color/")
            if response.status_code != 200:
                return CheckResult.wrong(f"""HTTP code: {response.status_code}... Couldn't connect to /modify-color/""")
            try:
                json_response = response.json()
            except json.decoder.JSONDecodeError as e:
                raise WrongAnswer(f"The following JSONDecodeError error occurred when the response was processed:\n"
                                  f"{e}\n"
                                  f"Make sure you format the response properly.")
            if json_response != expected_data[i]:
                return CheckResult.wrong(self.msg_200_invalid + ". path_info: /modify-color/")
        return CheckResult.correct()

    # STAGE 2 *****************************************************************************************************
    def stage2_modify_test_invalid_data(self):
        # Invalid data
        url = self.get_url('modify-color/')
        data = {"representation": "hzsv",
                "color": [128, 85, 95],
                "operation": "desaturate",
                "amount": 5
                }
        response = requests.post(url, json=data)

        if response.status_code == 500:
            return CheckResult.wrong(self.msg_500 + ". path_info: /modify-color/")

        if response.status_code == 400:
            if response.json() == {"error": "Invalid data."}:
                return CheckResult.correct()
            return CheckResult.wrong(self.msg_400_expected + ". path_info: /modify-color/")

        msg = f"""received HTTP status code: {response.status_code},
         in response to invalid data: {data}. path_info: /modify-color/"""
        return CheckResult.wrong(msg)

    def stage2_convert_test1(self):
        return self.conversion_processor(rgb_values, "rgb", "hsv", RGB_HSV)

    def stage2_convert_test2(self):
        return self.conversion_processor(hsv_values, "hsv", "rgb", HSV_RGB)

    def stage2_convert_test_invalid_data(self):
        url = self.get_url('convert-color/')
        # invalid data
        data_invalid = {"representation": "hsv",
                        "color": [128, 85, 999],
                        "conversion": "rgb"
                        }
        response = requests.post(url, json=data_invalid)

        if response.status_code == 500:
            return CheckResult.wrong(self.msg_500 + ". path_info: /convert-color/")

        if response.status_code == 400:
            if response.json() == {"error": "Invalid data."}:
                return CheckResult.correct()
            return CheckResult.wrong(self.msg_400_expected + ". path_info: /convert-color/")

        msg = f"""received HTTP status code: {response.status_code},
         in response to invalid data: {data_invalid}. path_info: /convert-color/"""
        return CheckResult.wrong(msg)

    # STAGE 3 *****************************************************************************************************
    def conversion_processor(self, colors, original, conversion, conversion_dict):
        url = self.get_url('convert-color/')

        for i in range(len(colors)):
            data = {"representation": original,
                    "color": colors[i],
                    "conversion": conversion}

            response = requests.post(url, json=data)
            if response.status_code == 500:
                return CheckResult.wrong(
                    self.msg_500 + f""", while converting {original} to {conversion}. path_info: /convert-color/""")
            if response.status_code != 200:
                return CheckResult.wrong(
                    f"""HTTP code: {response.status_code}... Couldn't connect to /convert-color/""")
            if response.json() != conversion_dict[i]:
                return CheckResult.wrong(self.msg_200_invalid + ". path_info: /convert-color/")

        return CheckResult.correct()

    def stage3_convert_test1(self):
        return self.conversion_processor(rgb_values, "rgb", "hsv", RGB_HSV)

    def stage3_convert_test2(self):
        return self.conversion_processor(rgb_values, "rgb", "hex", RGB_HEX)

    def stage3_convert_test3(self):
        return self.conversion_processor(rgb_values, "rgb", "hsl", RGB_HSL)

    def stage3_convert_test4(self):
        return self.conversion_processor(hsv_values, "hsv", "rgb", HSV_RGB)

    def stage3_convert_test5(self):
        return self.conversion_processor(hsv_values, "hsv", "hex", HSV_HEX)

    def stage3_convert_test6(self):
        return self.conversion_processor(hsv_values, "hsv", "hsl", HSV_HSL)

    def stage3_convert_test7(self):
        return self.conversion_processor(hex_values, "hex", "rgb", HEX_RGB)

    def stage3_convert_test8(self):
        return self.conversion_processor(hex_values, "hex", "hsv", HEX_HSV)

    def stage3_convert_test9(self):
        return self.conversion_processor(hex_values, "hex", "hsl", HEX_HSL)

    def stage3_convert_test10(self):
        return self.conversion_processor(hsl_values, "hsl", "rgb", HSL_RGB)

    def stage3_convert_test11(self):
        return self.conversion_processor(hsl_values, "hsl", "hsv", HSL_HSV)

    def stage3_convert_test12(self):
        return self.conversion_processor(hsl_values, "hsl", "hex", HSL_HEX)

    def stage3_convert_test_invalid_data(self):
        url = self.get_url('convert-color/')
        # invalid data
        data_invalid = [{"representation": "rgb", "color": [552, 85, 95], "conversion": "hsv"},
                        {"representation": "hsv", "color": [128, -50, 95], "conversion": "rgb"},
                        {"representation": "hex", "color": "#ZZ15F8", "conversion": "rgb"},
                        {"representation": "hex", "color": "#C589", "conversion": "rgb"},
                        {"representation": "hsl", "color": [128, 85, 1000], "conversion": "rgb"},
                        {"representation": "random", "color": [128, 85, 100], "conversion": "rgb"},
                        {"representation": "rgb", "color": [128, 85, 100], "conversion": "random"},
                        {"representation": "rgb", "color": [128, 85, 100]},
                        ]

        for data in data_invalid:
            response = requests.post(url, json=data)

            if response.status_code != 400:
                if response.status_code == 500:
                    return CheckResult.wrong(self.msg_500 + ". path_info: /convert-color/")
                if response.status_code == 200:
                    return CheckResult.wrong(self.msg_400_expected + ". path_info: /convert-color/")
                msg = f"""received HTTP status code: {response.status_code},
                 in response to invalid data: {data}. path_info: /modify-color/"""
                return CheckResult.wrong(msg)
            if response.status_code == 400:
                if response.json() != {"error": "Invalid data."}:
                    return CheckResult.wrong(self.msg_400_expected + ". path_info: /convert-color/")
        return CheckResult.correct()

    # STAGE 4 *****************************************************************************************************
    def stage4_monochromatic_test(self):
        url = self.get_url('color-harmony/')
        colors = [[150, 0, 100], [150, 50, 50], [150, 100, 0]]
        harmonies = [{'representation': 'hsv',
                      'color_1': [150.0, 0.0, 60.0],
                      'color_2': [150.0, 0.0, 80.0],
                      'color_3': [150.0, 0.0, 100.0]},
                     {'representation': 'hsv',
                      'color_1': [150.0, 50.0, 30.0],
                      'color_2': [150.0, 50.0, 50.0],
                      'color_3': [150.0, 50.0, 70.0]},
                     {'representation': 'hsv',
                      'color_1': [150.0, 100.0, 0.0],
                      'color_2': [150.0, 100.0, 20.0],
                      'color_3': [150.0, 100.0, 40.0]}]

        for i in range(len(colors)):
            data = {"representation": "hsv",
                    "color": colors[i],
                    "harmony": "monochromatic"}

            response = requests.post(url, json=data)
            if response.status_code == 500:
                return CheckResult.wrong(self.msg_500 + ". (monochromatic)" + ". path_info: /color-harmony/")
            if response.status_code != 200:
                return CheckResult.wrong(
                    f"""HTTP code: {response.status_code}... (monochromatic). Couldn't connect to /color-harmony/""")
            if response.json() != harmonies[i]:
                return CheckResult.wrong(self.msg_200_invalid + ". (monochromatic)" + ". path_info: /convert-color/")
        return CheckResult.correct()

    def stage4_monochromatic_test_invalid_data(self):
        url = self.get_url('color-harmony/')
        colors = [[-50, 0, 100], [150, 50, 999], [150, 100, -10]]

        for i in range(len(colors)):
            data = {"representation": "hsv",
                    "color": colors[i],
                    "harmony": "monochromatic"}

            response = requests.post(url, json=data)

            if response.status_code != 400:
                if response.status_code == 500:
                    return CheckResult.wrong(self.msg_500 + ". (monochromatic)" + ". path_info: /color-harmony/")
                if response.status_code == 200:
                    return CheckResult.wrong(
                        self.msg_400_expected + ". (monochromatic)" + ". path_info: /color-harmony/")
                msg = f"""received HTTP status code: {response.status_code},
                     in response to invalid data: {data}.(monochromatic). path_info: /color-harmony/"""
                return CheckResult.wrong(msg)
            if response.status_code == 400:
                if response.json() != {"error": "Invalid data."}:
                    return CheckResult.wrong(
                        self.msg_400_expected + ". (monochromatic)" + ". path_info: /color-harmony/")

        return CheckResult.correct()

    # STAGE 5 *****************************************************************************************************
    def stage5_complementary_test(self):
        url = self.get_url('color-harmony/')
        colors = [[0, 0, 100],
                  [40, 50, 50],
                  [65, 100, 0],
                  [125, 90, 50],
                  [180, 80, 90],
                  [200, 80, 95],
                  [241, 80, 100],
                  [300, 85, 80],
                  [320, 90, 70],
                  [360, 50, 40]]
        harmonies = [{'representation': 'hsv', 'color': [0.0, 0.0, 100.0], 'complementary': [137, 0.0, 100.0]},
                     {'representation': 'hsv', 'color': [40.0, 50.0, 50.0], 'complementary': [216, 50.0, 50.0]},
                     {'representation': 'hsv', 'color': [65.0, 100.0, 0.0], 'complementary': [273, 100.0, 0.0]},
                     {'representation': 'hsv', 'color': [125.0, 90.0, 50.0], 'complementary': [339, 90.0, 50.0]},
                     {'representation': 'hsv', 'color': [180.0, 80.0, 90.0], 'complementary': [22, 80.0, 90.0]},
                     {'representation': 'hsv', 'color': [200.0, 80.0, 95.0], 'complementary': [33, 80.0, 95.0]},
                     {'representation': 'hsv', 'color': [241.0, 80.0, 100.0], 'complementary': [49, 80.0, 100.0]},
                     {'representation': 'hsv', 'color': [300.0, 85.0, 80.0], 'complementary': [99, 85.0, 80.0]},
                     {'representation': 'hsv', 'color': [320.0, 90.0, 70.0], 'complementary': [113, 90.0, 70.0]},
                     {'representation': 'hsv', 'color': [360.0, 50.0, 40.0], 'complementary': [137, 50.0, 40.0]}]

        for i in range(len(colors)):
            response = requests.post(url, json={"representation": "hsv",
                                                "color": colors[i],
                                                "harmony": "complementary"})
            if response.status_code == 500:
                return CheckResult.wrong(self.msg_500 + ". (complementary)" + ". path_info: /color-harmony/")
            if response.status_code != 200:
                return CheckResult.wrong(
                    f"""HTTP code: {response.status_code}... (complementary). Couldn't connect to /color-harmony/""")
            if response.json() != harmonies[i]:
                return CheckResult.wrong((self.msg_200_invalid + ". (complementary)" + ". path_info: /color-harmony/"))
        return CheckResult.correct()
