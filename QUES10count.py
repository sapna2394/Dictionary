d =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
count = 0
for i in d:
    if d[i]:
        count=count+len(d[i])
print(count)        
  