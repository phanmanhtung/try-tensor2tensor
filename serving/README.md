# Serving
Tensor2Tensor and the TensorFlow ecosystem make it easy to serve a model once trained.

These commands will be run in your TERMINAL; so be prepared for the dependencies and the 10000-step trained model inside your laptop

Also you need to have the first telegram version; because we will deploy to telegram

## 1. Export for Serving
- First, export it for serving:

t2t-exporter \
  --model=transformer \
  --hparams_set=transformer_base \
  --problem=translate_envi_iwslt32k \
  --data_dir=t2t/data \
  --output_dir=t2t/train
- Don't just copy-paste, you need your correct directory names 

## 2. Launch a Server
Firstly, install the _tensorflow-model-server_
- Enter these command via terminal:

wget 'http://storage.googleapis.com/tensorflow-serving-apt/pool/tensorflow-model-server/t/tensorflow-model-server/tensorflow-model-server_1.3.0_all.deb'

sudo dpkg -i tensorflow-model-server_1.3.0_all.deb

sudo apt-get upgrade tensorflow-model-server

- Start the server pointing at the export:

Run "&> translator_log &" at the same time with the "tensorflow_model_server" to create a file called "translator_log"

Be careful to provide correct model_base_path

tensorflow_model_server \
  --port=9000 \
  --model_name=translator \
  --model_base_path=$HOME/Desktop/chatbot/t2t/train/export/
&> translator_log &

Some notes here!
- "model_base_path" is the link to the FOLDER containing the serving exported in step 1;
- tensor2tensor will run the highest version among these servings (You can rename it "1" or "2" if you want)

Now, enter _ls_ in terminal, you should see a file named "translator_log"

Use "vim translator_log" command to start the server

- Reference: [link](https://www.youtube.com/watch?v=KoJmg18EN_w)

## 3. Query the Server
- Note: The t2t-query-server is meant only as an example. You may need to modify it to suit your needs. The exported model expects an input example that is structured identically to what would be found on disk during training (serialized tf.train.Example). For text problems, that means that it expects the inputs to already be encoded as integers. You can see how the t2t-query-server does this by reading the code.

Install some dependencies:

pip install tensorflow-serving-api

t2t-query-server \
  --server=localhost:9000 \
  --servable_name=translator \
  --problem=translate_envi_iwslt32k \
  --data_dir=t2t/data \
  --inputs_once='Some random string here'

get rid of "inputs_once" for the interactive environment

And we completed serving, now time to deploy to telegram

## 4. Deploy to telegram

+ Try to understand how the previous telegram program works -> all we need to do is change the funtion Translator(string) inside the Translator.py file

- Full script: _Translator.py_:

import os
def transltorAI(String):

  batcmd="t2t-query-server \
  --server=localhost:9000 \
  --servable_name=translator \
  --problem=translate_envi_iwslt32k \
  --data_dir=t2t/data \
  --inputs_once='{}'".format(String)

  print(batcmd)

  result = os.popen(batcmd).read()
  result = result[314:]

  return result

if __name__ == '__main__':
  transltorAI("Hello world")

- Run telegram again and see how it works! Good luck!
python chatbot.py


