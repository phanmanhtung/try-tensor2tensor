import os

def translatorAI(String):

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
