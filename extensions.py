import MeCab
import os


class NLP():
    def __init__(self):
        path = os.environ.get("MECABDIC")
        self._mecab_dic = MeCab.Tagger(f'--unk-feature "unknown" -d {path}')
        self._mecab_dic.parse("")

    def extract_parts(self, text="", select_part=[]):
        if (not text) or (not select_part):
            return text

        token = self._mecab_dic.parseToNode(text)
        result = {part: [] for part in select_part}
        while token:
            if token.feature == "unknown":
                token = token.next
                continue

            part = token.feature.split(",")[0]
            if part not in select_part:
                token = token.next
                continue

            origin = token.feature.split(",")[6]
            result[part].append(origin)
            token = token.next

        for part in select_part:
            result[part] = list(set(result[part]))
        return result
