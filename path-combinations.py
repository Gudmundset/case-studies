#How to achieve path combinations without import
#Preserve order, these are paths or partial paths

han = 'ggggg/bbbbbbbb/cvvc/ddddd'
splitlist = han.split('/')

def path_combinations(listinput):
  result = []
  for n,_ in enumerate(splitlist):
      for i,__ in enumerate(splitlist):
          result_temp = '/'.join(splitlist[n:i+1])
          if result_temp: 
            result.append(result_temp)
  return result
  
print(path_combinations(splitlist))

#Expected output
#['ggggg', 'ggggg/bbbbbbbb', 'ggggg/bbbbbbbb/cvvc', 'ggggg/bbbbbbbb/cvvc/ddddd', 'bbbbbbbb', 'bbbbbbbb/cvvc', 'bbbbbbbb/cvvc/ddddd', 'cvvc', 'cvvc/ddddd', 'ddddd']
