from tqdm import tqdm
import requests 
#Paste a down link
dlink = 'https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe'

resp = requests.get(dlink, stream = True)
total_work = int(resp.headers['Content-Length'])

#split function will split after the /
filename = dlink.split('/')[-1]

#this section will make sure the file closes before it ruins into any errors
with open(filename, 'wb') as fout:
	#displays the progress bars wsowing how many bits hs beend downloaded
	with tqdm(total = total_work, desc = 'File Download', unit='B' , unit_divisor = 1024, unit_scale = True) as pbar:
		for chunk in resp.iter_content(chunk_size = 4096):
			fout.write(chunk)
			pbar.update(len(chunk))