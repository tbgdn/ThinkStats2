import nsfg

df = nsfg.ReadFemPreg()
print(df.outcome.value_counts().sort_index())
print(df.birthwgt_lb.value_counts(sort=False))

caseid = 10229
preg_map = nsfg.MakePregMap(df)
indices = preg_map[caseid]
print(df.outcome[indices].values)