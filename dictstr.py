from dict_trie import Trie
from editdistance import eval
import operator
from math import exp
from editdistance import eval
from math import log

def first_loss(prob,word):
  loss=0
  #print(prob,word)
  #prob=list(prob)
  for i in range(0,len(word)):
    
    loss=loss+log(prob[i][ord(word[i])-ord('a')])
  return -loss


def edit_distance(actual,dict):
  total=0
  distance=[]
  t=0.3 #tunable parameter
  for i in dict:
    """change=0
    #print(i,i[0])
    #print(actual,len(i[0]),len(actual))
    a=len(i)
    b=len(actual)
    if(a<b):
      x=a
    else:x=b
    for j in range(0,x):
      if(i[j]!=actual[j]):
        change+=1
    change+=abs(len(i)-len(actual))
    expo_change=exp(-change/t)
    distance.append(expo_change)
    total+=expo_change"""
    a=eval(i,actual)
    total+=a
    distance.append(a)
  return distance,total


def second_loss(prob,dict):
  total=0
  loss2=[]
  for i in dict:
    a=first_loss(prob,i)
    total+=a
    loss2.append(a)
  return loss2,total

def dict_setup():
    dictionary=open("dictionary.txt").read().replace("\n\n", "\n").split("\n")
    trie=Trie(dictionary)
def loss_(predicted,actual,preds_prob):
  #if(predicted==actual):return predicted
  p=list(trie.all_levenshtein_(predicted, 2))
  """candidates = {}
  for word in dictionary:
    #print(word)
    candidates[word] = eval(predicted, word)
  #print(candidates[:20])
  p = sorted(candidates.items(), key=operator.itemgetter(1))[:20]
  print(p)"""
  p=[i[0] for i in p]
  #print(p)
  edit_dist,total_dist=edit_distance(actual,p)
  min_=float('inf')
  ans=[]
  for j in range(len(p)):
    if(edit_dist[j]<min_):
      min_=edit_dist[j]
  for j in range(len(p)):
    if(edit_dist[j]==min_):
      ans.append(p[j])
  #for j in ans:
   # if(j==actual): return j
  #return predicted
  #print(preds_prob[i].shape)
  actual_loss=first_loss(preds_prob,actual)
  #print(actual_loss)
  #print(p)
  edit_dist,total_dist=edit_distance(actual,p)
  loss2,total_loss=second_loss(preds_prob,p)
  divergence=0
  min_=float('inf')
  loss=0
  total_edit_dist=0
  s=[]
  for j in range(len(p)):
    #print(total_loss)
    first=loss2[j]/total_loss
    s.append(first)
    #print(first,actual[i])
    #loss+=first
    #second=edit_dist[j]/total_dist
    #total_edit_dist+=second

    if(first<min_):
      min_=first
  
  ans2=[]
  for j in range(len(p)):
    if(s[j]==min_ ):ans2.append(p[j])
  for j in range(min(len(ans),len(ans2))):
    if(ans[j]==ans2[j]):return ans[j]
  return predicted

      
    

    #divergence+=(total_edit_dist*log(loss))
  #print("Training loss for"+str(i)+" is:"+str(actual_loss-divergence))
  #print("Actual=",actual,"ans=",ans)
  return ans



