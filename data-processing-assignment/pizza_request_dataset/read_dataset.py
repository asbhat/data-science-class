import codecs
import json

def read_dataset(path):
  with codecs.open(path, 'r', 'utf-8') as myFile:
    content = myFile.read()
  dataset = json.loads(content)
  return dataset

if __name__ == '__main__':
  path = './pizza_request_dataset.json'
  dataset = read_dataset(path)
  
  print 'The dataset contains %d samples.' %(len(dataset))
  print 'Available attributes: ', sorted(dataset[0].keys())
  print 'First post:'
  print json.dumps(dataset[0], sort_keys=True, indent=2)

  successes = [r['requester_received_pizza'] for r in dataset]
  success_rate = 100.0 * sum(successes) / float(len(successes))
  print 'The average success rate is: %.2f%%' %(success_rate)