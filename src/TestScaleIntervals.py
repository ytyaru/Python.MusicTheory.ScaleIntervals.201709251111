#!python3.6
import unittest
import math
from MusicTheory.scale.ScaleIntervals import ScaleIntervals
from MusicTheory.scale.ScaleIntervals import Intervals
from MusicTheory.scale.Scale import Scale
#from MusicTheory.scale.ScaleIntervals import ScaleIntervals
"""
ScaleIntervalsのテスト。というよりenumの試用テスト。
"""
class TestScaleIntervals(unittest.TestCase):
    def test_issubclass(self):
        self.assertTrue(issubclass(ScaleIntervals.Major, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.HarmonicMinor, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.MelodicMinor, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.Symmetrical, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.ModesOfLimitedTransposition, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.PentaTonic, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.People.Europe, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.People.Arab, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.People.India, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.People.China, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.People.Japan.Classical, Intervals))
        self.assertTrue(issubclass(ScaleIntervals.People.Japan.YoNaNuki, Intervals))
    def test_MajorMinor(self):
        names = {'Ionian':'C D E F G A B'.split(),
                 'Dorian':'C D Eb F G A Bb'.split(),
                 'Phrigian':'C Db Eb F G Ab Bb'.split(),
                 'Lydian':'C D E F# G A B'.split(),
                 'Mixolydian':'C D E F G A Bb'.split(),
                 'Aeolian':'C D Eb F G Ab Bb'.split(),
                 'Locrian':'C Db Eb F Gb Ab Bb'.split()}
        s = Scale('C', ScaleIntervals.Major.Ionian)
        for n in names:
            s.Intervals = ScaleIntervals.Major[n]
            print(s.Names)
            with self.subTest(name=n):
                self.assertEqual(names[n], s.Names)
    #            self.assertEqual(names[n], ScaleIntervals.Major[n])
    def test_MajorMinor_GetName(self):
        names = {'Ionian':'長音階',
                 'Dorian':'ドリアン・スケール',
                 'Phrigian':'フリジアン・スケール',
                 'Lydian':'リディアン・スケール',
                 'Mixolydian':'ミクソリディアン・スケール',
                 'Aeolian':'短音階',
                 'Locrian':'ロクリアン・スケール'}
        for n in names:
            self.assertIn(names[n], ScaleIntervals.Major.GetName(ScaleIntervals.Major[n]))
    def test_HarmonicMinor(self):
        names = {'Harmonic':'C D Eb F G Ab B'.split(),
                 'Locrian':'C Db Eb F Gb Ab Bb'.split(),
                 'Ionian':'C D E F G# A B'.split(),
                 'Dorian':'C D Eb F# G A Bb'.split(),
                 'Phrigian':'C Db E F G Ab Bb'.split(),
                 'Lydian':'C D# E F# G A B'.split(),
                 'Altered':'C Db Eb Fb Gb Ab Bbb'.split()} # Fb -> E, Bbb -> A
        s = Scale('C', ScaleIntervals.HarmonicMinor.Ionian)
        for n in names:
            s.Intervals = ScaleIntervals.HarmonicMinor[n]
            print(s.Names)
            with self.subTest(name=n):
                self.assertEqual(names[n], s.Names)
    #            self.assertEqual(names[n], ScaleIntervals.Major[n])
    def test_HarmonicMinor_GetName(self):
        names = {'Harmonic':'和声短音階',
                 'Locrian':'ロクリアン♮6・スケール',
                 'Ionian':'アイオニアン♯5・スケール',
                 'Dorian':'ドリアン♯4・スケール',
                 'Phrigian':'フリジアン・メジャー（ハーモニック・マイナー・パーフェクト5th・ビロウ）・スケール',
                 'Lydian':'リディアン♯2・スケール',
                 'Altered':'オルタード♭♭7（スーパーロクリアン♭7）・スケール'}
        for n in names:
            with self.subTest(name=n):
                self.assertIn(names[n], ScaleIntervals.HarmonicMinor.GetName(ScaleIntervals.HarmonicMinor[n]))
    def test_MelodicMinor(self):
        names = {'Ionian':'C D Eb F G A B'.split(),
                 'Dorian':'C Db Eb F G A Bb'.split(),
                 'Phrigian':'C D E F# G# A B'.split(),
                 'Lydian':'C D E F# G A Bb'.split(),
                 'Mixolydian':'C D E F G Ab Bb'.split(),
                 'Aeolian':'C D Eb F Gb Ab Bb'.split(),
                 'Locrian':'C Db Eb Fb Gb Ab Bb'.split()}
        s = Scale('C', ScaleIntervals.MelodicMinor.Ionian)
        for n in names:
            s.Intervals = ScaleIntervals.MelodicMinor[n]
            print(s.Names)
            with self.subTest(name=n):
                self.assertEqual(names[n], s.Names)
    def test_MelodicMinor_GetName(self):
        names = {'Ionian':'旋律短音階',
                 'Dorian':'スーパー・ドリアン・スケール',
                 'Phrigian':'スーパー・フリジアン・スケール',
                 'Lydian':'スーパー・リディアン・スケール',
                 'Mixolydian':'スーパー・ミクソリディアン・スケール',
                 'Aeolian':'スーパー・エオリアン・スケール',
                 'Locrian':'スーパー・ロクリアン・スケール'}
        for n in names:
            with self.subTest(name=n):
                self.assertIn(names[n], ScaleIntervals.MelodicMinor.GetName(ScaleIntervals.MelodicMinor[n]))

    def test_Symmetrical(self):
        names = {'Diminished':'C D Eb F Gb G# A B'.split(),
                 'Chromatic':'C C# D D# E F F# G G# A A# B'.split()}
        s = Scale('C', ScaleIntervals.Symmetrical.Diminished)
        for n in names:
            s.Intervals = ScaleIntervals.Symmetrical[n]
            print(s.Names)
            with self.subTest(name=n):
                self.assertEqual(names[n], s.Names)
    def test_MelodicMinor_GetName(self):
        names = {'Diminished':'ディミニッシュト・スケール',
                 'Chromatic':'クロマティック・スケール'}
        for n in names:
            with self.subTest(name=n):
                self.assertIn(names[n], ScaleIntervals.Symmetrical.GetName(ScaleIntervals.Symmetrical[n]))

    def test_ModesOfLimitedTransposition(self):
        names = {'WholeTone':'C D E F# Ab Bb'.split(),
                 'CombinationOfDiminished':'C Db Eb E F# G A Bb'.split(),
                 'Tcherepnin':'C D Eb E F# G Ab Bb B'.split()}
        s = Scale('C', ScaleIntervals.ModesOfLimitedTransposition.WholeTone)
        for n in names:
            with self.subTest(name=n):
                s.Intervals = ScaleIntervals.ModesOfLimitedTransposition[n]
                print(s.Names)
                self.assertEqual(names[n], s.Names)
    def test_ModesOfLimitedTransposition_GetName(self):
        names = {'WholeTone':'ホール・トーン・スケール。全音音階。移調の限られた旋法第1旋法。',
                 'CombinationOfDiminished':'コンビネーション・オブ・デミニッシュト音階。移調の限られた旋法第2旋法。',
                 'Tcherepnin':'チェレプニン音階。移調の限られた旋法第3旋法。'}
        for n in names:
            with self.subTest(name=n):
                self.assertIn(names[n], ScaleIntervals.ModesOfLimitedTransposition.GetName(ScaleIntervals.ModesOfLimitedTransposition[n]))

    def test_PentaTonic(self):
        names = {'Major':'C D E G A'.split(),
                 'Minor':'C Eb F G Bb'.split(),
                 'BlueNote':'C Eb F Gb G Bb'.split()}
        s = Scale('C', ScaleIntervals.PentaTonic.Major)
        for n in names:
            with self.subTest(name=n):
                s.Intervals = ScaleIntervals.PentaTonic[n]
                print(s.Names)
                self.assertEqual(names[n], s.Names)
    def test_PentaTonic_GetName(self):
        names = {'Major':'メジャー・ペンタトニック・スケール',
                 'Minor':'マイナー・ペンタトニック・スケール',
                 'BlueNote':'ブルー・ノート・スケール'}
        for n in names:
            with self.subTest(name=n):
                self.assertIn(names[n], ScaleIntervals.PentaTonic.GetName(ScaleIntervals.PentaTonic[n]))





    """
    def test_reference(self):
        print(ScaleIntervals)
        print(dir(ScaleIntervals))
        print(ScaleIntervals.Major)
        print(ScaleIntervals == ScaleIntervals.Major)
#        print(ScaleIntervals in ScaleIntervals.Major)
        for a in ScaleIntervals: print(a)
        print(ScaleIntervals.Major in ScaleIntervals)
    def test_set(self):
        with self.assertRaises(AttributeError) as ex:
            ScaleIntervals.Major = (0,)
        self.assertIn('Cannot reassign members.', str(ex.exception))
        self.assertEqual((2,2,1,2,2,2), ScaleIntervals.Major.value)
        self.assertEqual('Major', ScaleIntervals.Major.name)
    def test_GetName(self):
        self.assertEqual('長音階', ScaleIntervals.GetName(ScaleIntervals.Major))
        self.assertEqual('短音階', ScaleIntervals.GetName(ScaleIntervals.Minor))
        self.assertEqual('和声的短音階', ScaleIntervals.GetName(ScaleIntervals.HarmonicMinor))
        self.assertEqual('旋律的短音階', ScaleIntervals.GetName(ScaleIntervals.MelodicMinor))
        with self.assertRaises(ValueError) as ex:
            ScaleIntervals.GetName('abc')
        self.assertIn("引数targetは存在しません。ScaleIntervalsにある属性のいずれかにしてください。", str(ex.exception))
    """


if __name__ == '__main__':
    unittest.main()

