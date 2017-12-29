#from Framework.ConstMeta import ConstMeta
import enum
from abc import ABCMeta, abstractmethod
#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#各種音階における音程

#class Intervals(enum.Enum, metaclass=ABCMeta):
class Intervals(enum.Enum):
    __metaclass__ = ABCMeta
    @abstractmethod
    def GetName(cls, target, language='ja'): pass

class ScaleIntervals:
    #自然短音階と共通
    @enum.unique
    class Major(Intervals):
        Ionian     = (2,2,1,2,2,2)      # C D E F G A B    1 2 3 4 5 6 7    長音階と同義
        Dorian     = (2,1,2,2,2,1)      # C D Eb F G A Bb    1 2 b3 4 5 6 b7
        Phrigian   = (1,2,2,2,1,2)      # C Db Eb F G Ab Bb 	1 b2 b3 4 5 b6 b7
        Lydian     = (2,2,2,1,2,2)      # C D E F# G A B 	1 2 3 #4 5 6 7
        Mixolydian = (2,2,1,2,2,1)      # C D E F G A Bb 	1 2 3 4 5 6 b7
        Aeolian    = (2,1,2,2,1,2)      # C D Eb F G Ab Bb 	1 2 b3 4 5 b6 b7    短音階と同義
        Locrian    = (1,2,2,1,2,2)      # C Db Eb F Gb Ab Bb 	1 b2 b3 4 b5 b6 b7
        @classmethod
        def GetName(cls, target, language='ja'):
            if 'ja' == language:
                if target == cls.Ionian: return 'アイオニアン・スケール。メジャー・スケール。長音階。'
                elif target == cls.Dorian: return 'ドリアン・スケール'
                elif target == cls.Phrigian: return 'フリジアン・スケール'
                elif target == cls.Lydian: return 'リディアン・スケール'
                elif target == cls.Mixolydian: return 'ミクソリディアン・スケール'
                elif target == cls.Aeolian: return 'エオリアン・スケール 。ナチュラル・マイナー・スケール。自然短音階'
                elif target == cls.Locrian: return 'ロクリアン・スケール'
                else: raise NotImplementedError(f'未実装。: target={target}')
            else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')

    #和声的短音階
    @enum.unique
    class HarmonicMinor(Intervals):
        Harmonic   = (2,1,2,2,1,3)      # C D Eb F G Ab B 	1 2 b3 4 5 b6 7    和声的短音階と同義
        Locrian    = (1,2,2,1,2,2)      # C Db Eb F Gb Ab Bb 	1 b2 b3 4 b5 b6 b7    ロクリアン♮6
        Ionian     = (2,2,1,3,1,2)      # C D E F G# A B 	1 2 3 4 #5 6 7    アイオニアン♯5
        Dorian     = (2,1,3,1,2,1)      # C D Eb F# G A Bb 	1 2 b3 #4 5 6 b7    ドリアン♯4
        Phrigian   = (1,3,1,2,1,2)      # C Db E F G Ab Bb 	1 b2 3 4 5 b6 b7    ハーモニック・マイナー・パーフェクト5th・ビロウ・スケール
        Lydian     = (3,1,2,1,2,2)      # C D# E F# G A B 	1 #2 3 #4 5 6 7  リディアン♯2
        Altered    = (1,2,1,2,2,1)      # C Db Eb Fb Gb Ab Bbb 	1 b2 b3 b4 b5 b6 bb7    スーパー・ロクリアン♭7（オルタード♭♭7）
        @classmethod
        def GetName(cls, target, language='ja'):
            if 'ja' == language:
                if target == cls.Harmonic: return 'ハーモニック・マイナー・スケール。和声短音階。'
                elif target == cls.Locrian: return 'ロクリアン♮6・スケール'
                elif target == cls.Ionian: return 'アイオニアン♯5・スケール'
                elif target == cls.Dorian: return 'ドリアン♯4・スケール'
                elif target == cls.Phrigian: return 'フリジアン・メジャー（ハーモニック・マイナー・パーフェクト5th・ビロウ）・スケール'
                elif target == cls.Lydian: return 'リディアン♯2・スケール'
                elif target == cls.Altered: return 'オルタード♭♭7（スーパーロクリアン♭7）・スケール'
                else: raise NotImplementedError(f'未実装。: target={target}')
            else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')

    #旋律的短音階
    @enum.unique
    class MelodicMinor(Intervals):
        Ionian     = (2,1,2,2,2,2)      # C D Eb F G A B 	1 2 b3 4 5 6 7    旋律的短音階と同義（スーパー・イオニアン）
        Dorian     = (1,2,2,2,2,1)      # C Db Eb F G A Bb 	1 b2 b3 4 5 6 b7    ドリアン♭2（スーパー・ドリアン）
        Phrigian   = (2,2,2,2,1,2)      # C D E F# G# A B 	1 2 3 #4 #5 6 7    スーパー・フリジアン
        Lydian     = (2,2,2,1,2,1)      # C D E F# G A Bb 	1 2 3 #4 5 6 b7    スーパー・リディアン
        Mixolydian = (2,2,1,2,1,2)      # C D E F G Ab Bb 	1 2 3 4 5 b6 b7    スーパー・ミクソリディアン
        Aeolian    = (2,1,2,1,2,2)      # C D Eb F Gb Ab Bb 	1 2 b3 4 b5 b6 b7    スーパー・エオリアン
        Locrian    = (1,2,1,2,2,2)      # C Db Eb Fb Gb Ab Bb(C Db D# E F# G# Bb) 	1 b2 b3 b4 b5 b6 b7(1 b2 #2 3 #4 #5 b7)  オルタード・スケールとスーパー・ロクリアン・スケールは実音は同じであるが表記が異なる。
        @classmethod
        def GetName(cls, target, language='ja'):
            if 'ja' == language:
                if target == cls.Ionian: return 'メロディック・マイナー・スケール。スーパー・イオニアン・スケール。旋律短音階。'
                elif target == cls.Dorian: return 'スーパー・ドリアン・スケール'
                elif target == cls.Phrigian: return 'スーパー・フリジアン・スケール'
                elif target == cls.Lydian: return 'スーパー・リディアン・スケール '
                elif target == cls.Mixolydian: return 'スーパー・ミクソリディアン・スケール'
                elif target == cls.Aeolian: return 'スーパー・エオリアン・スケール'
                elif target == cls.Locrian: return 'スーパー・ロクリアン・スケール'
                else: raise NotImplementedError(f'未実装。: target={target}')
            else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')

    #人工的に作られた音階
    @enum.unique
    class Symmetrical(Intervals):
        Diminished = (2,1,2,1,2,1,2)      # C D Eb F Gb G# A B
        Chromatic = tuple(*[[1]*11])    # C C# D D# E F F# G G# A A# B 	1 #1 2 #2 3 4 #4 5 #5 6 #6 7
        @classmethod
        def GetName(cls, target, language='ja'):
            if 'ja' == language:
                if target == cls.Diminished: return 'ディミニッシュト・スケール'
                elif target == cls.Chromatic: return 'クロマティック・スケール'
                else: raise NotImplementedError(f'未実装。: target={target}')
            else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')

    #移調の限られた旋法。（人工的に作られた音階の一種）
    @enum.unique
    class ModesOfLimitedTransposition(Intervals):
        WholeTone = (2,2,2,2,2)     # 全音音階。移調の限られた旋法第1旋法。キーがC, C#のときしか使えない  C D E F# Ab Bb 	1 2 3 #4 b6 b7
        CombinationOfDiminished = (1,2,1,2,1,2,1)   #デミニッシュト音階。移調の限られた旋法第2旋法  C Db Eb E F# G A Bb
        Tcherepnin = (2,1,1,2,1,1,2,1)#チェレプニン音階。移調の限られた旋法第3旋法     C D Eb E F# G Ab Bb B
        # 4〜6番もあるが、「移調が限られた」という特性が薄い。名前もついていないため実装しない
        #https://ja.wikipedia.org/wiki/%E7%A7%BB%E8%AA%BF%E3%81%AE%E9%99%90%E3%82%89%E3%82%8C%E3%81%9F%E6%97%8B%E6%B3%95
        @classmethod
        def GetName(cls, target, language='ja'):
            if 'ja' == language:
                if target == cls.WholeTone: return 'ホール・トーン・スケール。全音音階。移調の限られた旋法第1旋法。'
                elif target == cls.CombinationOfDiminished: return 'コンビネーション・オブ・デミニッシュト音階。移調の限られた旋法第2旋法。'
                elif target == cls.Tcherepnin: return 'チェレプニン音階。移調の限られた旋法第3旋法。'
                else: raise NotImplementedError(f'未実装。: target={target}')
            else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')

    #五音音階
    @enum.unique
    class PentaTonic(Intervals):
        Major = (2,2,3,2)#    C D E G A
        Minor = (3,2,2,3)#    C Eb F G Bb
        BlueNote = (3,2,1,1,3)#         C Eb F Gb G Bb    6音
        @classmethod
        def GetName(cls, target, language='ja'):
            if 'ja' == language:
                if target == cls.Major: return 'メジャー・ペンタトニック・スケール'
                elif target == cls.Minor: return 'マイナー・ペンタトニック・スケール'
                elif target == cls.BlueNote: return 'ブルー・ノート・スケール'
                else: raise NotImplementedError(f'未実装。: target={target}')
            else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')

    #民族音階
    #  ヨーロッパ
    #    ハンガリー, ジプシー, スペイン
    #  アラブ
    #  インド
    #  東南アジア、東アジア
    #    中国
    #    日本
    #      古典
    #      明治以降
    #    インドネシア
    #      スレンドロ
    #      ペロッグ
    class People:
        # ヨーロッパ
        class Europe(Intervals):
            Hungary = (2,1,3,1,2,2) # C D Eb F# G A B 	1 2 b3 #4 5 6 7
            Gypsy = (1,3,1,2,1,1)   # C Db E F G Ab B 	1 b2 3 4 5 b6 7
            Spain = (1,2,1,1,2,1,2) # C Db Eb E F G Ab Bb 	1 b2 b3 3 4 5 b6 b7
        # アラブ
        class Arab(Intervals):
            Rast = () # C D Eq F G A Bq 	1 2 q3 4 5 6 7
            Nahawand = () #C D Eb F G Ab B 	1 2 b3 4 5 b6 7 	ハーモニック・マイナー・スケールと同一のスケール
            ナワサル = () #C D Eb F# G Ab B 	1 2 b3 #4 5 b6 7
            ナグリーズ = () #C D Eb F# G A Bb 	1 2 b3 #4 5 6 b7 	ドリアン♯4・スケールと同一のスケール
            Hijazkar = ()#C Db E F G Ab B 	1 b2 3 4 5 b6 7 	ジプシー・スケールと同一のスケール
            Bayati = () #C Dq Eb F G Ab Bb 	1 q2 b3 4 5 b6 b7
            Saba = () #C Dq Eb Fb G Ab Bb 	1 q2 b3 b4 5 b6 b7
            ヒジャーズィー = () #C Db E F G Ab Bb 	1 b2 3 4 5 b6 b7
            クルディー = () #C Db Eb F G Ab Bb 	1 b2 b3 4 5 b6 b7
            Sikah = () #Eq, F, G, A, Bq, C, D, Eq
            フザム = ()#Eq, F, G, Ab, B, C, D, Eq
        # インド
        class India(Intervals): pass
            # ビラーヴァル・タート 	C D E F G A B 	1 2 3 4 5 6 7 	メジャー・スケールと同一のスケール        
            #カマージ・タート 	C D E F G A Bb 	1 2 3 4 5 6 b7 	ミクソリディアン・スケールと同一のスケール
            #カーフィー・タート 	C D Eb F G A Bb 	1 2 b3 4 5 6 b7 	ドリアン・スケールと同一のスケール
            #アサーワリー・タート 	C D Eb F G Ab Bb 	1 2 b3 4 5 b6 b7 	ナチュラル・マイナー・スケールと同一のスケール
            #バイラヴ・タート 	C Db E F G Ab B 	1 b2 3 4 5 b6 7 	ジプシー・スケールと同一のスケール
            #バイラヴィ・タート 	C Db Eb F G Ab Bb 	1 b2 b3 4 5 b6 b7 	フリジアン・スケールと同一のスケール
            #カリヤーン・タート 	C D E F# G A B 	1 2 3 #4 5 6 7 	リディアン・スケールと同一のスケール
            #マールワー・タート 	C Db E F# G A B 	1 b2 3 #4 5 6 7 	
            #プールヴィー・タート 	C Db E F# G Ab B 	1 b2 3 #4 5 b6 7 	
            #トーディー・タート 	C Db Eb F# G Ab B 	1 b2 b3 #4 5 b6 7 	
        class China(Intervals): pass
            #宮調式 	C D E G A 	1 2 3 5 6 	メジャー・ペンタトニック・スケールと同一のスケール
            #商調式 	C D F G Bb 	1 2 4 5 b7 	メジャー・ペンタトニック・スケールの第2音から始めたスケール
            #角調式 	C Eb F Ab Bb 	1 b3 4 b6 b7 	メジャー・ペンタトニック・スケールの第3音から始めたスケール
            #徴調式 	C D F G A 	1 2 4 5 6 	メジャー・ペンタトニック・スケールの第4音から始めたスケール
            #羽調式 	C Eb F G Bb 	1 b3 4 5 b7 	メジャー・ペンタトニック・スケールの第5音から始めたスケール。マイナー・ペンタトニック・スケールと同一のスケール
        class Japan:
            class Classical(Intervals): pass
                #呂旋法（雅楽） 	C D E G A[1] 	1 2 3 5 6 	メジャー・ペンタトニック・スケールと同一のスケール
                #律旋法（雅楽） 	C D F G A[1] 	1 2 4 5 6 	
                #陽旋法・田舎節（俗楽） 	C D F G Bb（下降形 A G F D C)[2] 	1 2 4 5 b7（下降形 6 5 4 2 1） 	
                #陰旋法・都節（俗楽） 	C Db F G Bb（下降形 Ab G F Db C)[2] 	1 b2 4 5 b7（下降形 b6 5 4 b2 1） 	
                #琉球音階 	C E F G B 	1 3 4 5 7 	
            class YoNaNuki(Intervals): pass
                #ヨナ抜き長音階 	C D E G A 	1 2 3 5 6 	呂旋法と同一のスケール
                #ヨナ抜き短音階 	C D Eb G Ab 	1 2 b3 5 b6 	第4音から始めると陰旋法
                #ニロ抜き短音階 	C Eb F G Bb 	1 b3 4 5 b7 	マイナー・ペンタトニック・スケールと同一のスケール
                #ニロ抜き長音階 	C E F G B 	1 3 4 5 7 	琉球音階と同一のスケール            
                #雲井音階 	C D Eb G A 	1 2 b3 5 6 	
                #岩戸音階 	C Db F Gb Bb 	1 b2 4 b5 b7 	
        class Indonesia(Intervals):
            Pelog = (1,2,4,1)#C Db Eb G Ab 	1 b2 b3 5 b6

"""
@enum.unique
class ScaleIntervals(enum.Enum):
#class ScaleIntervals(enum.Enum, metaclass=ConstMeta):
    #===一般===
    #7音
    Major = (2,2,1,2,2,2)#          C,D,E,F,G,A,B
    Minor = (2,1,2,2,1,2)#          C,D,Eb,F,G,Ab,Bb
    Diminished = (2,1,2,1,2,1)#     C,D,Eb,F,Gb,G#,A,B
    HarmonicMinor = (2,1,2,2,1,3)#  C,D,Eb,F,G,Ab,B
    MelodicMinor = (2,1,2,2,2,2)#   C,D,Eb,F,G,A,B
    #5音
    MajorPentaTonic = (2,2,3,2)#    C,D,E,G,A
    MinorPentaTonic = (3,2,2,3)#    C,Eb,F,G,Bb
    #6音
    BlueNote = (3,2,1,1,3)#         C,Eb,F,Gb,G,Bb
    #12音
    Chromatic = tuple(*[[1]*11])
    #移調の限られた旋法
    Tcherepnin = (2,1,1,2,1,1,2,1,1)#移調の限られた旋法第3旋法
    WholeTone = (2,2,2,2,2,2,2)# キーがC, C#のときしか使えないスケール
    
    # ===民族===
    ClassicJapan = ((2,2,3,2),(2,3,2,2),(2,3,2,3),(1,4,2,3),(4,1,2,4)) #('呂旋法', '律旋法', '陽旋法・田舎節', '陰旋法・都節', '琉球音階')
    YonanukiJapan = ((2,2,3,2),(2,1,3,1),(3,2,2,3),(4,1,2,4),(2,1,4,2),(1,4,1,4)) #('ヨナ抜き長音階', 'ヨナ抜き短音階', 'ニロ抜き短音階', 'ニロ抜き長音階', '雲井音階', '岩戸音階')
    
    @classmethod
    def GetName(cls, target, language='ja'):
        if 'ja' == language:
            if target not in cls: raise ValueError(f'引数targetは存在しません。ScaleIntervalsにある属性のいずれかにしてください。: target={target}')
            if target == cls.Major: return '長音階'
            elif target == cls.Minor: return '短音階'
            elif target == cls.Diminished: return 'ディミニッシュト・スケール（移調の限られた旋法第2旋法）'
            elif target == cls.HarmonicMinor: return '和声的短音階'
            elif target == cls.MelodicMinor: return '旋律的短音階'
            elif target == cls.MajorPentaTonic: return 'メジャー・ペンタトニック・スケール'
            elif target == cls.MinorPentaTonic: return 'マイナー・ペンタトニック・スケール'
            elif target == cls.BlueNote: return 'ブルー・ノート・スケール'
            elif target == cls.Chromatic: return 'クロマティック・スケール'
            elif target == cls.Chromatic: return 'クロマティック・スケール'
            elif target == cls.Tcherepnin: return 'チェレプニン・スケール（移調の限られた旋法第3旋法）'
            elif target == cls.WholeTone: return 'ホールトーン・スケール（全音音階、移調の限られた旋法第1旋法）'
            elif target == cls.ClassicJapan: return '古典邦楽の音階（呂旋法、律旋法、陽旋法・田舎節、陰旋法・都節、琉球音階）'
            elif target == cls.ClassicJapan: return 'ヨナ抜き音階（ヨナ抜き長音階、ヨナ抜き短音階、ニロ抜き短音階、ニロ抜き長音階、雲井音階、岩戸音階）'
            else: raise NotImplementedError(f'未実装。存在する属性なのに対応する名前を返さない。開発者はソースコードを見なおせ。: target={target}')
        else: raise ValueError(f'引数languageが未対応の値です。現在は"ja"のみ対応です。: language={language}')
"""


if __name__ == '__main__':
    print('========== 一般スケール ==========')
    print('----- 7音 -----')
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Minor)
    print(ScaleIntervals.Diminished)
    print(ScaleIntervals.HarmonicMinor)
    print(ScaleIntervals.MelodicMinor)
    print('----- 5音 -----')
    print(ScaleIntervals.BlueNote)
    print(ScaleIntervals.MajorPentaTonic)
    print(ScaleIntervals.MinorPentaTonic)
    print('----- 12音 -----')
    print(ScaleIntervals.Chromatic)
    print('----- 移調の限られた旋法 -----')
    print(ScaleIntervals.Tcherepnin)
    print(ScaleIntervals.WholeTone)
    print('========== 民族スケール ==========')
    print(ScaleIntervals.ClassicJapan)
    print(ScaleIntervals.YonanukiJapan)
    """
    print(ScaleIntervals.ArabicMaqam)
    print(ScaleIntervals.Chaina)
    print(ScaleIntervals.Gypsy)
    print(ScaleIntervals.Hungary)
    print(ScaleIntervals.Pelog)
    print(ScaleIntervals.Spain)
    """
