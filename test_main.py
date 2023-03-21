import unittest


from main import effect


class TestMain(unittest.TestCase):
    def test_effect(self):
        self.assertEqual(effect('なんだろう、うそつくのやめてもらっていいですか？'), ":left_side_balloon_with_tail:$[rainbow $[tada なんだろう、うそつくのやめてもらっていいですか？]]")
        self.assertEqual(effect('不快感を覚えた自分にやめてもらっていいですか？'), ":left_side_balloon_with_tail:不快感を覚えた自分にやめてもらっていいですか？")


if __name__ == '__main__':
    unittest.main()
