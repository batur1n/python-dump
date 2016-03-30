def file_search(folder, filename):
    res = ''
    if filename == folder:
       return folder[0]+'/'+filename
    elif isinstance(folder, list) and any(file_search(item, filename) for 
item in folder):
       res2 = folder[0]+folder[0][0][0]+filename
       return res2

print(file_search(['C:','backup.log','ideas.txt'],'ideas.txt'))
print(file_search(['/home',['user1'],['user2',['my pictures'], ['desktop','not this', 'and not this', ['new_folder', 'hereiam.py']]], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'],],'hey.py'], 'hereiam.py'))
