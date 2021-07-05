from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import colorsys
import re


class SaturationView(APIView):
    parser_classes = [JSONParser]

    @csrf_exempt
    def post(self, request, format=None):

        if not SaturationView.validateDict(request.data):
            return Response({'error': 'Invalid data.', }, status=status.HTTP_400_BAD_REQUEST)

        # print(request.data)

        respData = request.data.copy()
        amount = respData.pop('amount')
        respData['modified_color'] = respData['color'].copy()

        if respData['operation'] == 'desaturate':
            respData['modified_color'][1] = respData['modified_color'][1] * (1 - amount / 100)
        elif respData['operation'] == 'saturate':
            respData['modified_color'][1] = respData['modified_color'][1] * (1 + amount / 100)

        respData['modified_color'][1] = round(respData['modified_color'][1])

        # print(Response(respData).data)

        return Response(respData)

    @staticmethod
    def validateDict(data):
        expectedKeys = ['operation', 'color', 'representation', 'amount']

        try:
            # assert(type(data) is dict)
            assert (all([i in data for i in expectedKeys]))  # All expected are present
            assert (all([i in expectedKeys for i in data]))  # No extra keys
            assert (data['representation'] == 'hsv')
            hsv = data['color']
            assert (all([0 <= hsv[0] <= 360,
                         0 <= hsv[1] <= 100,
                         0 <= hsv[2] <= 100]))
        except AssertionError:
            return False

        return True


class ConvertView(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        print(request.data)

        if not ConvertView.validateDict(request.data):
            return Response({'error': 'Invalid data.', }, status=status.HTTP_400_BAD_REQUEST)

        respData = {'color': request.data['color']}

        if request.data['representation'] == 'hsv':
            if request.data['conversion'] == 'rgb':
                respData['converted_color'] = ConvertView.hsvToRgb(request.data['color'])
            elif request.data['conversion'] == 'hex':
                respData['converted_color'] = ConvertView.rgbToHex(ConvertView.hsvToRgb(request.data['color']))
            elif request.data['conversion'] == 'hsl':
                respData['converted_color'] = ConvertView.hsvToHsl(request.data['color'])

        elif request.data['representation'] == 'rgb':
            if request.data['conversion'] == 'hsv':
                respData['converted_color'] = ConvertView.rgbToHsv(request.data['color'])
            elif request.data['conversion'] == 'hex':
                respData['converted_color'] = ConvertView.rgbToHex(request.data['color'])
            elif request.data['conversion'] == 'hsl':
                respData['converted_color'] = ConvertView.rgbToHsl(request.data['color'])

        elif request.data['representation'] == 'hsl':
            if request.data['conversion'] == 'rgb':
                respData['converted_color'] = ConvertView.hslToRgb(request.data['color'])
            elif request.data['conversion'] == 'hex':
                respData['converted_color'] = ConvertView.rgbToHex(ConvertView.hslToRgb(request.data['color']))
            elif request.data['conversion'] == 'hsv':
                respData['converted_color'] = ConvertView.hslToHsv(request.data['color'])

        elif request.data['representation'] == 'hex':
            if request.data['conversion'] == 'rgb':
                respData['converted_color'] = ConvertView.hexToRgb(request.data['color'])
            elif request.data['conversion'] == 'hsv':
                respData['converted_color'] = ConvertView.rgbToHsv(ConvertView.hexToRgb(request.data['color']))
            elif request.data['conversion'] == 'hsl':
                respData['converted_color'] = ConvertView.rgbToHsl(ConvertView.hexToRgb(request.data['color']))

        else:
            respData['converted_color'] = request.data['color']

        print(Response(respData).data)

        return Response(respData)

    @staticmethod
    def rgbToHex(rgb):
        rhex = hex(rgb[0]).upper().split('X')[1].zfill(2)
        ghex = hex(rgb[1]).upper().split('X')[1].zfill(2)
        bhex = hex(rgb[2]).upper().split('X')[1].zfill(2)

        return '#' + ''.join([rhex, ghex, bhex])

    @staticmethod
    def rgbToHsl(rgb):
        rgbDec = [i / 255 for i in rgb]
        hDec, lDec, sDec = colorsys.rgb_to_hls(*rgbDec)
        hsl = [hDec * 360,
               sDec * 100,
               lDec * 100]

        hsl = [round(i) for i in hsl]
        return hsl

    @staticmethod
    def rgbToHsv(rgb):
        rgbDec = [i / 255 for i in rgb]
        hsvDec = colorsys.rgb_to_hsv(*rgbDec)
        hsv = [hsvDec[0] * 360,
               hsvDec[1] * 100,
               hsvDec[2] * 100]
        hsv = [round(i) for i in hsv]

        return hsv

    @staticmethod
    def hexToRgb(hexStr):
        r = int(hexStr[1:3], 16)
        g = int(hexStr[3:5], 16)
        b = int(hexStr[5:7], 16)
        return [r, g, b]

    @staticmethod
    def hslToRgb(hsl):
        hls = [hsl[0] / 360, hsl[2] / 100, hsl[1] / 100]
        rgbDec = colorsys.hls_to_rgb(*hls)
        rgb255 = [round(i * 255) for i in rgbDec]
        return rgb255

    @staticmethod
    def hsvToRgb(hsv):
        rgbDec = colorsys.hsv_to_rgb(hsv[0] / 360, hsv[1] / 100, hsv[2] / 100)
        rgb255 = [round(i * 255) for i in rgbDec]
        return rgb255

    @staticmethod
    def hsvToHsl(hsv):
        rgbDec = colorsys.hsv_to_rgb(hsv[0] / 360, hsv[1] / 100, hsv[2] / 100)
        hDec, lDec, sDec = colorsys.rgb_to_hls(*rgbDec)
        hsl = [hDec * 360,
               sDec * 100,
               lDec * 100]

        hsl = [round(i) for i in hsl]
        return hsl

    @staticmethod
    def hslToHsv(hsl):
        hls = [hsl[0] / 360, hsl[2] / 100, hsl[1] / 100]
        rgbDec = colorsys.hls_to_rgb(*hls)
        hsvDec = colorsys.rgb_to_hsv(*rgbDec)
        hsv = [hsvDec[0] * 360,
               hsvDec[1] * 100,
               hsvDec[2] * 100]
        hsv = [round(i) for i in hsv]

        return hsv

    @staticmethod
    def validateDict(data):
        expectedKeys = ['color', 'representation', 'conversion']

        try:
            # assert(type(data) is dict)
            assert (all([i in data for i in expectedKeys]))  # All expected are present
            assert (all([i in expectedKeys for i in data]))  # No extra keys
            assert (data['representation'] in ['hsv', 'rgb', 'hex', 'hsl'])
            assert (data['conversion'] in ['hsv', 'rgb', 'hex', 'hsl'])

            if data['representation'] in ['hsv', 'hsl']:
                hsv = data['color']
                assert (all([0 <= hsv[0] <= 360,
                             0 <= hsv[1] <= 100,
                             0 <= hsv[2] <= 100]))
            elif data['representation'] == 'hex':
                assert (re.match(r'#[0-9A-F][0-9A-F][0-9A-F][0-9A-F][0-9A-F][0-9A-F]', data['color']))
            else:
                assert (all([0 <= i <= 255 for i in data['color']]))
        except AssertionError:
            return False

        return True


class HarmonyView(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        print(request.data)
        if not HarmonyView.validateDict(request.data):
            print('failed')
            return Response({'error': 'Invalid data.', }, status=status.HTTP_400_BAD_REQUEST)

        respData = {'representation': 'hsv'}

        if request.data['harmony'] == 'monochromatic':
            vBase = request.data['color'][2]

            if vBase < 20:
                vNew = [vBase, vBase + 20, vBase + 40]
            elif 20 <= vBase <= 80:
                vNew = [vBase - 20, vBase, vBase + 20]
            else:  # vBase > 80
                vNew = [vBase - 40, vBase - 20, vBase]

            for i in range(len(vNew)):
                respData[f'color_{i + 1}'] = request.data['color'].copy()
                respData[f'color_{i + 1}'][2] = vNew[i]

        else:
            adobe = {
                0: 0,  # red
                35: 60,  # orange
                60: 122,  # yellow
                120: 165,  # green
                180: 218,  # cyan
                240: 275,  # blue
                300: 330,  # magenta
                360: 360  # red
            }
            hIn = request.data['color'][0]
            keyDown = 0
            for key in adobe:
                if key >= hIn:
                    keyUp = key
                    break
                keyDown = key

            if keyUp == 0:
                mappedH = 0
            else:
                mappedH = (hIn - keyDown) / (keyUp - keyDown) * (adobe[keyUp] - adobe[keyDown]) + adobe[keyDown]

            compMap = (mappedH + 180) % 360

            mapDown = 0
            for key in adobe:
                if adobe[key] >= compMap:
                    mapUp = key
                    break
                mapDown = key

            if mapUp == 0:
                outH = 0
            else:
                outH = round((compMap - adobe[mapDown]) / (adobe[mapUp] - adobe[mapDown]) * (mapUp - mapDown) +mapDown)

            respData['color'] = request.data['color']
            respData['complementary'] = [outH, request.data['color'][1], request.data['color'][2]]

        print(respData)
        return Response(respData)

    @staticmethod
    def validateDict(data):
        expectedKeys = ['harmony', 'color', 'representation']

        try:
            # assert(type(data) is dict)
            assert (all([i in data for i in expectedKeys]))  # All expected are present
            assert (all([i in expectedKeys for i in data]))  # No extra keys
            assert (data['representation'] == 'hsv')
            assert (data['harmony'] in ['monochromatic', 'complementary'])
            hsv = data['color']
            assert (all([0 <= hsv[0] <= 360,
                         0 <= hsv[1] <= 100,
                         0 <= hsv[2] <= 100]))
        except AssertionError:
            return False

        return True
