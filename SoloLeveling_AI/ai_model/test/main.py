from transformers import pipeline
pipe = pipeline(model='togethercomputer/GPT-JT-6B-v1', cache_dir="./")
pipe('''"I love this!" Is it positive? A:''')