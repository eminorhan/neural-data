import numpy as np
from tqdm import tqdm
from datasets import load_dataset, concatenate_datasets

def count_tokens_in_dataset(dataset, column_name):
    n_tok = 0
    for sample in tqdm(dataset, total=len(dataset)):
        sh = np.array(sample[column_name]).shape
        n_tok += np.prod(sh)
    return n_tok

n_tokens = 0

# willett
willett_column_name = "tx1"
willett_train = load_dataset("eminorhan/willett", split='train').select_columns([willett_column_name])
willett_test = load_dataset("eminorhan/willett", split='test').select_columns([willett_column_name])
willett_validation = load_dataset("eminorhan/willett", split='validation').select_columns([willett_column_name])
willett = concatenate_datasets([willett_train, willett_test, willett_validation])
nt = count_tokens_in_dataset(willett, willett_column_name)
n_tokens += nt
print(f"1. Willett: {nt:,} tokens")

# h1
h1_column_name = "spike_counts"
h1_incalib = load_dataset("eminorhan/h1", "in-calib", split='train').select_columns([h1_column_name])
h1_inminival = load_dataset("eminorhan/h1", "in-minival", split='train').select_columns([h1_column_name])
h1_outcalib = load_dataset("eminorhan/h1", "out-calib", split='train').select_columns([h1_column_name])
h1 = concatenate_datasets([h1_incalib, h1_inminival, h1_outcalib])
nt = count_tokens_in_dataset(h1, h1_column_name)
n_tokens += nt
print(f"2. H1: {nt:,} tokens")

# # h2
h2_column_name = "spike_counts"
h2_incalib = load_dataset("eminorhan/h2", "in-calib", split='train').select_columns([h2_column_name])
h2_inminival = load_dataset("eminorhan/h2", "in-minival", split='train').select_columns([h2_column_name])
h2_outcalib = load_dataset("eminorhan/h2", "out-calib", split='train').select_columns([h2_column_name])
h2 = concatenate_datasets([h2_incalib, h2_inminival, h2_outcalib])
nt = count_tokens_in_dataset(h2, h2_column_name)
n_tokens += nt
print(f"3. H2: {nt:,} tokens")

# m1-a
m1a_column_name = "spike_counts"
m1a_incalib = load_dataset("eminorhan/m1-a", "in-calib", split='train').select_columns([m1a_column_name])
m1a_inminival = load_dataset("eminorhan/m1-a", "in-minival", split='train').select_columns([m1a_column_name])
m1a_outcalib = load_dataset("eminorhan/m1-a", "out-calib", split='train').select_columns([m1a_column_name])
m1a = concatenate_datasets([m1a_incalib, m1a_inminival, m1a_outcalib])
nt = count_tokens_in_dataset(m1a, m1a_column_name)
n_tokens += nt
print(f"4. M1-A: {nt:,} tokens")

# m1-b
m1b_column_name = "spike_counts"
m1b_incalib = load_dataset("eminorhan/m1-b", "in-calib", split='train').select_columns([m1b_column_name])
m1b_inminival = load_dataset("eminorhan/m1-b", "in-minival", split='train').select_columns([m1b_column_name])
m1b_outcalib = load_dataset("eminorhan/m1-b", "out-calib", split='train').select_columns([m1b_column_name])
m1b = concatenate_datasets([m1b_incalib, m1b_inminival, m1b_outcalib])
nt = count_tokens_in_dataset(m1b, m1b_column_name)
n_tokens += nt
print(f"5. M1-B: {nt:,} tokens")

# m2
m2_column_name = "spike_counts"
m2_incalib = load_dataset("eminorhan/m2", "in-calib", split='train').select_columns([m2_column_name])
m2_inminival = load_dataset("eminorhan/m2", "in-minival", split='train').select_columns([m2_column_name])
m2_outcalib = load_dataset("eminorhan/m2", "out-calib", split='train').select_columns([m2_column_name])
m2 = concatenate_datasets([m2_incalib, m2_inminival, m2_outcalib])
nt = count_tokens_in_dataset(m2, m2_column_name)
n_tokens += nt
print(f"6. M2: {nt:,} tokens")

# mc-maze
mc_maze_column_name = "spike_counts"
mc_maze = load_dataset("eminorhan/mc-maze", split='train').select_columns([mc_maze_column_name])
nt = count_tokens_in_dataset(mc_maze, mc_maze_column_name)
n_tokens += nt
print(f"7. MC-maze: {nt:,} tokens")

# mc-rtt
mc_rtt_column_name = "spike_counts"
mc_rtt = load_dataset("eminorhan/mc-rtt", split='train').select_columns([mc_rtt_column_name])
nt = count_tokens_in_dataset(mc_rtt, mc_rtt_column_name)
n_tokens += nt
print(f"8. MC-rtt: {nt:,} tokens")

# area2-bump
area2_bump_column_name = "spike_counts"
area2_bump = load_dataset("eminorhan/area2-bump", split='train').select_columns([area2_bump_column_name])
nt = count_tokens_in_dataset(area2_bump, area2_bump_column_name)
n_tokens += nt
print(f"9. Area2-bump: {nt:,} tokens")

# dmfc-rsg
dmfc_rsg_column_name = "spike_counts"
dmfc_rsg = load_dataset("eminorhan/dmfc-rsg", split='train').select_columns([dmfc_rsg_column_name])
nt = count_tokens_in_dataset(dmfc_rsg, dmfc_rsg_column_name)
n_tokens += nt
print(f"10. DMFC-rsg: {nt:,} tokens")

# xiao
xiao_column_name = "spike_counts"
xiao = load_dataset("eminorhan/xiao", split='train').select_columns([xiao_column_name])
nt = count_tokens_in_dataset(xiao, xiao_column_name)
n_tokens += nt
print(f"11. Xiao: {nt:,} tokens")

# churchland
churchland_column_name = "spike_counts"
churchland = load_dataset("eminorhan/churchland", split='train').select_columns([churchland_column_name])
nt = count_tokens_in_dataset(churchland, churchland_column_name)
n_tokens += nt
print(f"12. Churchland: {nt:,} tokens")

# perich
perich_column_name = "spike_counts"
perich = load_dataset("eminorhan/perich", split='train').select_columns([perich_column_name])
nt = count_tokens_in_dataset(perich, perich_column_name)
n_tokens += nt
print(f"13. Perich: {nt:,} tokens")

# makin
makin_column_name = "spike_counts"
makin = load_dataset("eminorhan/makin", split='train').select_columns([makin_column_name])
nt = count_tokens_in_dataset(makin, makin_column_name)
n_tokens += nt
print(f"14. Makin: {nt:,} tokens")

print(f"Total number of tokens: {n_tokens:,}")