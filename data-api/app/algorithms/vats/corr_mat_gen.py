import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist,squareform
from scipy.stats import spearmanr


def cor_mat(df:pd.DataFrame,method:str)-> list:
    cor:pd.DataFrame = np.transpose(df)
    cpg_ids:list = cor.index.tolist()
    
    if method == "Pearson":
        cor = pdist(cor,"correlation")
    elif method == "Spearman":
        cor = pdist(cor,lambda x,y: spearmanr(x,y)[0])
    return (cpg_ids,squareform(cor).tolist())
    
