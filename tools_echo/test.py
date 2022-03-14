from timesformer.datasets_echo import loader
from timesformer.utils.parser import load_config, parse_args
args = parse_args()
if args.num_shards > 1:
    args.output_dir = str(args.job_dir)
cfg = load_config(args)
train_loader = loader.construct_loader(cfg, "train")
print(next(iter(train_loader)))