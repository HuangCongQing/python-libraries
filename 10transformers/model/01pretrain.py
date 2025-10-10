#AutoModelForCausalLM是模型，AutoTokenizer是分词器
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

#将模型和分词器下载到本地，并指定保存路径
model_name="uer/gpt2-chinese-cluecorpussmall"#模型名称
cache_dir="model/uer/gpt2-chinese-cluecorpussmall"#模型保存路径

#下载模型
AutoModelForCausalLM.from_pretrained(model_name,cache_dir=cache_dir)
#下载分词器
AutoTokenizer.from_pretrained(model_name,cache_dir=cache_dir)

print(f"模型分词器已下载到：{cache_dir}")
