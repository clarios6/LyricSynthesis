import gpt_2_simple as gpt2
import os
from pathlib import Path
import tensorflow as tf
from tensorflow.core.protobuf import rewriter_config_pb2
from tensorflow.python.client import device_lib

model_name = "355M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/



basePath = Path(__file__).parent
file_name = "masterLyricFile.txt"
relativePath = "../lyrics/" + file_name
filePath = (basePath / relativePath).resolve()
print(filePath)
file_path = "../lyrics/masterLyricFile.txt"

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction=0.77
config.graph_options.rewrite_options.layout_optimizer = rewriter_config_pb2.RewriterConfig.OFF
sess = tf.compat.v1.Session(config=config)


sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              str(filePath),
              model_name=model_name,
              steps=1000)   # steps is max number of training steps

gpt2.generate(sess)
