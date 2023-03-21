import unittest


from main import effect, msky_emoji_replace


class TestMain(unittest.TestCase):
    def test_effect(self):
        self.assertEqual(msky_emoji_replace(effect('あさのきよこ')), ':_a::_sa::_no::_ki::_yo::_ko:')
        self.assertEqual(msky_emoji_replace(effect('よさのあきこ')), '$[spin.left,speed=2s $[position.x=2 $[spin.speed=1s \
$[position.x=2 $[spin.left,speed=2s $[rainbow 　　　　　:_yo::_sa::_no::_a::_ki::_ko:]]]]]]\
\n\n$[x2 $[rainbow $[tada :yosano_party:]$[tada :yosano_akiko:]$[tada :yosano_party:]]]')
        self.assertEqual(msky_emoji_replace(effect('タッパークレ')), ':_ta::_ltsu::_pa::_prolong::_ku::_re:')
        self.assertEqual(msky_emoji_replace(effect('レターパック')), '$[spin.left,speed=2s $[position.x=2 $[spin.speed=1s \
$[position.x=2 $[spin.left,speed=2s $[rainbow 　　　　　:_re::_ta::_prolong::_pa::_ltsu::_ku:]]]]]]\
\n\n$[rainbow $[tada :send_money:]]')


if __name__ == '__main__':
    unittest.main()
