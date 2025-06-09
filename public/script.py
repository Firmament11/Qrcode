import os

# 获取当前文件夹中的所有 .txt 文件
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

# 合并后的文件名
output_file = 'combined.txt'

# 打开合并后的文件，并写入内容
with open(output_file, 'w', encoding='utf-8') as outfile:
    for fname in txt_files:
        try:
            # 尝试以 utf-8 编码打开文件
            with open(fname, 'r', encoding='utf-8') as infile:
                outfile.write(f'# Content of {fname}\n')
                outfile.write(infile.read())
                outfile.write('\n\n')
        except UnicodeDecodeError:
            # 如果 utf-8 失败，尝试用其他编码（如 latin1）打开
            with open(fname, 'r', encoding='latin1') as infile:
                outfile.write(f'# Content of {fname} (decoded with latin1)\n')
                outfile.write(infile.read())
                outfile.write('\n\n')

print(f'All .txt files have been merged into {output_file}')
