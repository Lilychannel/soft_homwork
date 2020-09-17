import unittest
import My_test
from BeautifulReport import BeautifulReport

class make_all_text(unittest.TestCase):
    def test_self(self):
        print("测试文本为orig.txt")
        My_test.test_work('orig.txt', 'orig.txt', 'ans.txt')
    def test_add(self):
        print("测试文本为orig_0.8_add.txt")
        My_test.test_work('orig.txt','orig_0.8_add.txt','ans.txt')
    def test_del(self):
        print("测试文本为orig_0.8_del.txt")
        My_test.test_work('orig.txt', 'orig_0.8_del.txt', 'ans.txt')
    def test_dis_1(self):
        print("测试文本为orig_0.8_dis_1.txt")
        My_test.test_work('orig.txt', 'orig_0.8_dis_1.txt', 'ans.txt')
    def test_dis_3(self):
        print("测试文本为orig_0.8_dis_3.txt")
        My_test.test_work('orig.txt', 'orig_0.8_dis_3.txt', 'ans.txt')
    def test_dis_7(self):
        print("测试文本为orig_0.8_dis_7.txt")
        My_test.test_work('orig.txt', 'orig_0.8_dis_7.txt', 'ans.txt')
    def test_dis_10(self):
        print("测试文本为orig_0.8_dis_10.txt")
        My_test.test_work('orig.txt', 'orig_0.8_dis_10.txt', 'ans.txt')
    def test_dis_15(self):
        print("测试文本为orig_0.8_dis_15.txt")
        My_test.test_work('orig.txt', 'orig_0.8_dis_15.txt', 'ans.txt')
    def test_mix(self):
        print("测试文本为orig_0.8_mix.txt")
        My_test.test_work('orig.txt', 'orig_0.8_mix.txt', 'ans.txt')
    def test_rep(self):
        print("测试文本为orig_0.8_rep.txt")
        My_test.test_work('orig.txt', 'orig_0.8_rep.txt', 'ans.txt')
        print("end...")

if __name__ == '__main__':
    print("开始进行测试……")
    suite = unittest.TestSuite()
    suite.addTest(make_all_text('test_self'))
    suite.addTest(make_all_text('test_add'))
    suite.addTest(make_all_text('test_del'))
    suite.addTest(make_all_text('test_dis_1'))
    suite.addTest(make_all_text('test_dis_3'))
    suite.addTest(make_all_text('test_dis_7'))
    suite.addTest(make_all_text('test_dis_10'))
    suite.addTest(make_all_text('test_dis_15'))
    suite.addTest(make_all_text('test_mix'))
    suite.addTest(make_all_text('test_rep'))
    suite.addTest(make_all_text('test_rep'))
    runner = BeautifulReport(suite)
    runner.report(
        description='论文查重测试报告',
        filename='MinHash.html',
        log_path='.'  # 路径
    )
