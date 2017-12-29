# このソフトウェアについて

一般的な音階の音程を定義した。音名の取得でエラーになる。

今回はエラーがある状態。

* 民族音階は未実装または中途半端 `./src/MusicTheory/scale/ScaleIntervals.py`
* 音名の取得アルゴリズムが作りこめていない（どうするのが正しいのかの判断もできていない）

## 前回まで

* https://github.com/ytyaru/Python.MusicTheory.Chord.Triad.201709071957
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131752
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131811
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709141450
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709141657
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709171254
* https://github.com/ytyaru/Python.MusicTheory.Pitch.Key.201709171300
* https://github.com/ytyaru/Python.MusicTheory.Pitch.NoteNumber.201709171322
* https://github.com/ytyaru/Python.MusicTheory.Pitch.NoteName.201709171924
* https://github.com/ytyaru/Python.MusicTheory.Pitch.Accidental.i18n.201709172024
* https://github.com/ytyaru/Python.MusicTheory.Pitch.Key.i18n.201709172024
* https://github.com/ytyaru/Python.MusicTheory.Pitch.OctaveClass.201709211208
* https://github.com/ytyaru/Python.MusicTheory.Temperament.FundamentalTone.201709211614
* https://github.com/ytyaru/Python.MusicTheory.Temperament.PythagoreanTuning.201709220832
* https://github.com/ytyaru/Python.MusicTheory.Temperament.Equal.weakref.201709220926
* https://github.com/ytyaru/Python.MusicTheory.Temperament.JustIntonation.201709221413
* https://github.com/ytyaru/Python.MusicTheory.Scale.PitchClasses.201709230801
* https://github.com/ytyaru/Python.MusicTheory.ScaleKey.201709230939
* https://github.com/ytyaru/Python.MusicTheory.Scale.Names.201709241021

# 実行

```sh
$ cd ./src/
$ python TestScaleIntervals.py
$ python TestScale.py
```

テスト計178項目。

## src/MusicTheory/pitch

テストコード|項目数
------------|------
TestPitchClass.py|13
TestAccidental.py|16
TestDegree.py|13
TestInterval.py|16
TestKey.py|18
TestNoteNumber.py|11
TestNoteName.py|12
TestOctaveClass.py|8

計107項目

## src/MusicTheory/temperament

テストコード|項目数
------------|------
TestFundamentalTone.py|13
TestEqualTemperament.py|13
TestPythagoreanTuning.py|11
TestJustIntonation.py|7
TestScale.py, TestScaleKey.py|15
TestScaleIntervals.py|12（エラー）

計71項目

## `./src/TestScaleIntervals.py` エラーログ

すべてScaleクラスの音名取得によるエラー。

```sh
======================================================================
ERROR: test_ModesOfLimitedTransposition (__main__.TestScaleIntervals) (name='CombinationOfDiminished')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 125, in test_ModesOfLimitedTransposition
    s.Intervals = ScaleIntervals.ModesOfLimitedTransposition[n]
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 31, in Intervals
    self.__Update()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 59, in __Update
    self.__calcNames()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 90, in __calcNames
    else: raise RuntimeError(f'音名を決められませんでした。アルゴリズムに問題があります。: self.__names:={self.__names}, baseNames[i]={baseNames[i]}, p[0]={p[0]}')
RuntimeError: 音名を決められませんでした。アルゴリズムに問題があります。: self.__names:=['C', 'Db', 'Eb', 'E', 'Gb', 'G', 'A'], baseNames[i]=C, p[0]=10

======================================================================
ERROR: test_ModesOfLimitedTransposition (__main__.TestScaleIntervals) (name='Tcherepnin')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 125, in test_ModesOfLimitedTransposition
    s.Intervals = ScaleIntervals.ModesOfLimitedTransposition[n]
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 31, in Intervals
    self.__Update()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 59, in __Update
    self.__calcNames()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 90, in __calcNames
    else: raise RuntimeError(f'音名を決められませんでした。アルゴリズムに問題があります。: self.__names:={self.__names}, baseNames[i]={baseNames[i]}, p[0]={p[0]}')
RuntimeError: 音名を決められませんでした。アルゴリズムに問題があります。: self.__names:=['C', 'D', 'Eb', 'E', 'Gb', 'G'], baseNames[i]=B, p[0]=8

======================================================================
ERROR: test_PentaTonic (__main__.TestScaleIntervals) (name='Minor')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 143, in test_PentaTonic
    s.Intervals = ScaleIntervals.PentaTonic[n]
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 31, in Intervals
    self.__Update()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 59, in __Update
    self.__calcNames()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 90, in __calcNames
    else: raise RuntimeError(f'音名を決められませんでした。アルゴリズムに問題があります。: self.__names:={self.__names}, baseNames[i]={baseNames[i]}, p[0]={p[0]}')
RuntimeError: 音名を決められませんでした。アルゴリズムに問題があります。: self.__names:=['C', 'D#', 'F', 'G'], baseNames[i]=G, p[0]=10

======================================================================
ERROR: test_Symmetrical (__main__.TestScaleIntervals)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 107, in test_Symmetrical
    s.Intervals = ScaleIntervals.Symmetrical[n]
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 31, in Intervals
    self.__Update()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 59, in __Update
    self.__calcNames()
  File "/tmp/Python.MusicTheory.ScaleIntervals.201709251111/src/MusicTheory/scale/Scale.py", line 90, in __calcNames
    else: raise RuntimeError(f'音名を決められませんでした。アルゴリズムに問題があります。: self.__names:={self.__names}, baseNames[i]={baseNames[i]}, p[0]={p[0]}')
RuntimeError: 音名を決められませんでした。アルゴリズムに問題があります。: self.__names:=['C', 'Db', 'D'], baseNames[i]=F, p[0]=3

======================================================================
FAIL: test_HarmonicMinor (__main__.TestScaleIntervals) (name='Altered')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 63, in test_HarmonicMinor
    self.assertEqual(names[n], s.Names)
AssertionError: Lists differ: ['C', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb'] != ['C', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'A']

First differing element 3:
'Fb'
'E'

- ['C', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb']
?                    ^^                ^^^

+ ['C', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'A']
?                    ^                ^


======================================================================
FAIL: test_MelodicMinor (__main__.TestScaleIntervals) (name='Locrian')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 89, in test_MelodicMinor
    self.assertEqual(names[n], s.Names)
AssertionError: Lists differ: ['C', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'] != ['C', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb']

First differing element 3:
'Fb'
'E'

- ['C', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']
?                    ^^

+ ['C', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb']
?                    ^


======================================================================
FAIL: test_ModesOfLimitedTransposition (__main__.TestScaleIntervals) (name='WholeTone')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 127, in test_ModesOfLimitedTransposition
    self.assertEqual(names[n], s.Names)
AssertionError: Lists differ: ['C', 'D', 'E', 'F#', 'Ab', 'Bb'] != ['C', 'D', 'E', 'F#', 'G#', 'A#']

First differing element 4:
'Ab'
'G#'

- ['C', 'D', 'E', 'F#', 'Ab', 'Bb']
?                         ^^^^^^^

+ ['C', 'D', 'E', 'F#', 'G#', 'A#']
?                       ++++++  ^


======================================================================
FAIL: test_PentaTonic (__main__.TestScaleIntervals) (name='BlueNote')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 145, in test_PentaTonic
    self.assertEqual(names[n], s.Names)
AssertionError: Lists differ: ['C', 'Eb', 'F', 'Gb', 'G', 'Bb'] != ['C', 'D#', 'F', 'F#', 'G', 'A#']

First differing element 1:
'Eb'
'D#'

- ['C', 'Eb', 'F', 'Gb', 'G', 'Bb']
?        ^^         ^^         ^^

+ ['C', 'D#', 'F', 'F#', 'G', 'A#']
?        ^^         ^^         ^^


======================================================================
FAIL: test_Symmetrical (__main__.TestScaleIntervals) (name='Diminished')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestScaleIntervals.py", line 110, in test_Symmetrical
    self.assertEqual(names[n], s.Names)
AssertionError: Lists differ: ['C', 'D', 'Eb', 'F', 'Gb', 'G#', 'A', 'B'] != ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B']

First differing element 5:
'G#'
'Ab'

- ['C', 'D', 'Eb', 'F', 'Gb', 'G#', 'A', 'B']
?                              ^^

+ ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B']
?                              ^^


----------------------------------------------------------------------
Ran 12 tests in 0.050s

FAILED (failures=5, errors=4)
```

# 課題

* 音楽理論に基づき周波数を算出したい
    * 音律、音階
* メッセージに統一性を持たせたい
* メッセージを国際化したい(gettext, Babel)
    * 自然言語用と音楽理論用語用の2種類

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## Python

### 定数

* http://fakatatuku.hatenablog.com/entry/2015/03/26/233024

### サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

## 音楽理論

### 和音

* https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3
* http://www.piano-c.com/
* https://pf-j.sakura.ne.jp/music/chord.htm

### 音程

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%A8%8B
* https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1365320628
* https://okwave.jp/qa/q6858420.html

### 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

### 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

### 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

### 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

#### 純正律で12音

* http://musica.art.coocan.jp/enharmonic.htm
* http://yppts.adam.ne.jp/music/comp.html

#### 五度圏

* http://dn-voice.info/music-theory/godoken/

### 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

