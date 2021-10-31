import json
import subprocess

subprocess.call(['python', 'main.py', '--path', 'input_yolo', '--output', 'output.json'])

input_file = 'output/output.json'
output_file = 'coco_output.json'
sample_submission = 'submission_example.json' 

with open(sample_submission) as f:
    example = json.load(f)
with open(input_file) as f:
    submission = json.load(f)

img_to_idx = {}
for img in example['images']:
    img_to_idx[img['file_name']] = img['id']

old_to_new = {}
for i in range(len(submission['images'])):
    old_idx = submission['images'][i]['id']
    new_idx = img_to_idx[submission['images'][i]['file_name']]
    old_to_new[old_idx] = new_idx
    submission['images'][i]['id'] = img_to_idx[submission['images'][i]['file_name']]
    
for j in range(len(submission['annotations'])):
    submission['annotations'][j]['image_id'] = old_to_new[submission['annotations'][j]['image_id']]

with open(output_file, 'wt') as file:
    json.dump(submission, file)