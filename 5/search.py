def file_search(folder, filename):
	for i in folder:
		if i == filename:
			return folder[0] + '/' + i 
		elif isinstance(i, list):
			for j in i:
				if j == filename:
					return j
				elif isinstance(j, list):
					for k in j:
						if k == filename:
							return k
						elif isinstance(k, list):
							for h in k:
								if h == filename:
									return folder[0]+'/'+i[0]+'/'+j[0]+'/'+k[0]+'/'+h
	return False

print(file_search(['C:','backup.log','ideas.txt'],'ideas.txt'))
print(file_search(['D:',['recycle bin'],['tmp',['old'],['new_folder1','asd.txt','asd.bak','find.me.bak']],'hey.py'], 'find.me'))
print(file_search(['/home',['user1'],['user2',['my pictures'], ['desktop', 'not this', 'and not this', ['new_folder', 'hereiam.py']]], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'],],'hey.py'], 'hereiam.py'))
