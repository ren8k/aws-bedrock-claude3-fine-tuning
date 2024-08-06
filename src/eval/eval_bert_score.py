from bert_score import score


def calc_bert_score(cands, refs):
    P, R, F1 = score(cands, refs, lang="ja", verbose=True)
    return F1.numpy().tolist()  # 複数のデータを一気に計算する場合はこちら
    # return F1.item() # データを1つずつ計算する場合はこちら


refs = [
    "夕食には寿司を食べるのが好きです。",
    "今日はいい天気ですね",
    "今日は本当にいい天気",
    "暇な時間にはビデオゲームをするのが好きです。",
    "太陽が空で輝いています。",
    "今週末、海に旅行に行くつもりです。",
]
cands = [
    "夕食に食べるのは寿司が一番好きな食べ物です。",
    "今日は良くない天気ですね",
    "今日は本当にいい天気",
    "暇な時間にはビデオゲームをするのは楽しいです。",
    "外では今、激しい雨が降っています。",
    "週末は仕事で、楽しいことをすることができません。",
]

# 複数データを一気に計算するプログラム
f1_score = calc_bert_score(refs, cands)
for r, c, f1 in zip(refs, cands, f1_score):
    print(f"refs: {r}, cands: {c}, f1_score: {f1}")


# データを一つずつ計算するプログラム
# for i in range(len(refs)):
#     f1_score = calc_bert_score([refs[i]], [cands[i]])
#     print(f"refs: {refs[i]}, cands: {cands[i]}, f1_score: {f1_score}")
