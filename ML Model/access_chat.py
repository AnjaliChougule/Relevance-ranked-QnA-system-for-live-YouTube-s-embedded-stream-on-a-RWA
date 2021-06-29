def accessingLiveChat(link):
    
  #link='https://youtu.be/AYsolQwS-lk'
  chat = LiveChat(video_id = link[17:])
  chat_list,count=[],0
  print('Stream started')
  while chat.is_alive():
    try:
      #print('----nside try block')
      data = chat.get()
      items = data.items
      for c in items:
        chat_list.append((str(f"{c.message}")+'?').lower())
        #print(chat_list[::-1][0])
        #fil_list.append(str(removeStopWords(chat_list[::-1][0])).lower())
        if count>20:
          makeClusters(chat_list)
        time.sleep(0)
        count+=1  
      if not chat.is_alive():
        print('Live Stream Ended!!!')
        break 
    except Exception:
      chat.terminate()

final_clu=[]
s=set()
accessingLiveChat('https://youtu.be/cFrq28LAJK8')
print('summ started')
time.sleep(5)
#print(final_clu)
summ(final_clu)
print('summ ended')
#print(s)
for i in s:
  #print(i)
  db.child('user_name').push(i)
print('end of prg')
