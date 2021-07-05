from hstest import dynamic_test

from test.base import ColorizerTest


class ColorizerTestRunner(ColorizerTest):
    funcs = [
##        # stage 1
##        ColorizerTest.stage1_modify_test,
##        # stage 2
##        ColorizerTest.stage2_modify_test_invalid_data,
##        ColorizerTest.stage2_convert_test1,
##        ColorizerTest.stage2_convert_test2,
##        ColorizerTest.stage2_convert_test_invalid_data,
##        # stage 3
##        ColorizerTest.stage3_convert_test1,
##        ColorizerTest.stage3_convert_test2,
##        ColorizerTest.stage3_convert_test3,
##        ColorizerTest.stage3_convert_test4,
##        ColorizerTest.stage3_convert_test5,
##        ColorizerTest.stage3_convert_test6,
##        ColorizerTest.stage3_convert_test7,
##        ColorizerTest.stage3_convert_test8,
##        ColorizerTest.stage3_convert_test9,
##        ColorizerTest.stage3_convert_test10,
##        ColorizerTest.stage3_convert_test11,
##        ColorizerTest.stage3_convert_test12,
##        ColorizerTest.stage3_convert_test_invalid_data,
##        # stage 4
##        ColorizerTest.stage4_monochromatic_test,
##        ColorizerTest.stage4_monochromatic_test_invalid_data,
        # stage 5
        ColorizerTest.stage5_complementary_test,
    ]

    @dynamic_test(data=funcs, time_limit=0)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    ColorizerTestRunner().run_tests()
