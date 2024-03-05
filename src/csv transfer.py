import pandas as pd

# 读取CSV文件
df = pd.read_csv('monkey_mini.csv', delimiter='\t')

# 选择 "cell_id", "gene", "expr", "x", 和 "y" 列
df_selected = df[['cell_id', 'gene', 'expr', 'x', 'y']]

# 使用 pivot 函数重新组织数据
df_pivoted = df_selected.pivot(index='cell_id', columns='gene', values='expr')

# 将NaN值填充为0
df_pivoted = df_pivoted.fillna(0)

# 保存为 CSV 文件
df_pivoted.to_csv('slice.csv', index=False)

# 输出 "cell_id" 对应的 "x" 和 "y"
df_xy = df_selected[['cell_id', 'x', 'y']].drop_duplicates()
df_xy.set_index('cell_id', inplace=True)
df_xy.to_csv('slice_coor.csv', header=False, index=False)