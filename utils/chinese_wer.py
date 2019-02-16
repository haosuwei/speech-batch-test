import sys


class StringDiff:

    SHUZI = ['零0', '一1', '幺1', '二2', '两2', '三3', '四4', '五5', '六6', '七7', '八8', '九9']

    def __init__(self, tag_string, rec_string):
        self._srcString = self._space_chinese_word(tag_string)   # 标注文本
        self._recString = self._space_chinese_word(rec_string)   # 识别文本
        self.addCount = 0
        self.subCount = 0
        self.errCount = 0
        self.allCount = 0
        self.sameCount = 0
        self.wer = 0.0
        self.result = {
            "allCount": None,
            "addCount": None,
            "subCount": None,
            "errCount": None,
            "sameCount": None,
            "wer": None,
            "errMsg": None
        }

    def _space_chinese_word(self, s):
        wordSpace = ''
        for c in s:
            if c >= '\u4e00' and c <= '\u9fa5':
                wordSpace += c + " "
            elif (c >= '\u0041' and c<= '\u005a') or (c >= '\u0061' and c<= '\u007a'):
                wordSpace += c + " "
            elif c >= '\u0030' and c <= '\u0039':
                wordSpace += c+ " "
        return wordSpace

    def equals(self,char_a, char_b):
        char_a = chr(ord(char_a) + 0x20) if (char_a >= 'A' and char_a <= 'Z') else char_a
        char_b = chr(ord(char_b) + 0x20) if (char_b >= 'A' and char_b <= 'Z') else char_b
        if char_a == char_b:
            return True

        for tmp in range(0, len(self.SHUZI)):
            if char_a in self.SHUZI[tmp] and char_b in self.SHUZI[tmp]:
                return True

    def lcsc(self, seqx, seqy):
        lenx = len(seqx)
        leny = len(seqy)
        print("lenx", lenx,"leny",leny)
        table = [[[] for x in range(leny  + 1)] for y in range(lenx + 1)]
        print(table)
        Matrix = [[0 for x in range(leny + 1)]for y in range(lenx + 1)]
        for tmp in range(0, lenx + 1):
            Matrix[tmp][0] = tmp
        for tmp in range(0, leny + 1):
            Matrix[0][tmp] = tmp

        Matrix[0][0] = 0

        for xline in range(1, lenx + 1):
            for yline in range(1, leny + 1):
                MinCost1 = Matrix[xline -1][yline] + 1
                MinCost2 = Matrix[xline][yline -1] + 1
                MinCost = min(MinCost1, MinCost2)

                if self.equals(seqx[xline -1], seqy[yline - 1]):
                    ReplaceCost = 0
                else:
                    ReplaceCost = 1

                if ReplaceCost + Matrix[xline -1][yline - 1] < MinCost:
                    MinCost = ReplaceCost + Matrix[xline - 1][yline - 1]
                    table[xline][yline].extend(table[xline - 1][yline - 1])
                    if ReplaceCost == 0:
                        print(table[xline][yline])
                        table[xline][yline].append([xline - 1][yline - 1])
                elif MinCost2 == MinCost1:
                    if len(table[xline][yline - 1]) >= len(table[xline - 1][yline]):
                        table[xline][yline] = table[xline][yline - 1]
                    else:
                        table[xline][yline] = table[xline - 1][yline]
                elif MinCost2 < MinCost1:
                    table[xline][yline] = table[xline][yline - 1]
                else:
                    table[xline][yline] = table[xline - 1][yline]

                Matrix[xline][yline] = MinCost
        seqcls = table[lenx][leny]
        seqcls.append([lenx, leny])
        return seqcls

    def calclate_diff_lcs2(self):
        srcparts = self._srcString.split()
        dstparts = self._recString.split()

        if len(srcparts) <= 0:   # 没有标注文本的情况
            self.result["errMsg"] = "没有标注文本"
            return self.result

        if len(dstparts) <=0 :
            self.result["errMsg"] = "没有识别文本"
            return self.result
        print("srcparts:", srcparts)
        print("dstparts:", dstparts)
        lcsparts = self.lcsc(srcparts, dstparts)
        # print(lcsparts)









if __name__ == "__main__":
    a = "我是"
    b = "我是"
    c = StringDiff(a, b)
    c.calclate_diff_lcs2()
