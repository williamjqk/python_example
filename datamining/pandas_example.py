import pandas as pd
import numpy as np
data = {
    'group': np.random.randint(1,5,(100,)),
    'actual': np.random.random((100,)),
    'predict': np.random.random((100,)),
}
# np.random.random((20,))
# np.random.randint(1,5,(20,))
df = pd.DataFrame(data)
df = df.sort_values(["group", "predict"], ascending=[True, True]).reset_index(drop=True)
ascending = True
df["rank"] = df.groupby("group")["actual"].rank(ascending=ascending, pct=True)
k = 10
rdf = df.groupby("group").head(k).groupby("group")[["actual", "rank"]].mean()
rdf
rdf["random"] = np.array(df.groupby("group")["actual"].mean())
rdf
rdf.reset_index(inplace=True)
rdf
