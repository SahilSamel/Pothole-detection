#write train file (just the image list)
import os
with open('./data/obj.data', 'w') as out:
  out.write('classes = 3\n')
  out.write('train = data/train.txt\n')
  out.write('valid = data/valid.txt\n')
  out.write('names = data/obj.names\n')
  out.write('backup = ./backup/')


with open('./data/train.txt', 'w') as out:
  for img in [f for f in os.listdir('./data/obj/train') if f.endswith('jpg')]:
    out.write('./data/obj/' + img + '\n')

with open('./data/valid.txt', 'w') as out:
  for img in [f for f in os.listdir('./data/obj/valid') if f.endswith('jpg')]:
    out.write('./data/obj/' + img + '\n')