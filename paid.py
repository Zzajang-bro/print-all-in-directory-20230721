from os  import walk
from os.path  import join
from sys import argv

if len(argv) < 3:
	tar_path = input('타겟 경로: ')
	proj_name = input('프로젝트 이름: ')
else:
	tar_path = argv[1]
	projName = argv[2]

with open('header.html', 'r') as f:
	header = f.read()
footer = '</body></html>'


def html_style_sanitize( damn_str ):
	damn_str = damn_str.replace('&', '&amp;')
	damn_str = damn_str.replace('<', '&lt;')
	damn_str = damn_str.replace('>', '&gt;')
	damn_str = damn_str.replace(' ', '&nbsp;')
	damn_str = damn_str.replace('"', '&quot;')
	damn_str = damn_str.replace("'", '&apos;')
	damn_str = damn_str.replace('¢', '&cent;')
	damn_str = damn_str.replace('£', '&pound;')
	damn_str = damn_str.replace('¥', '&yen;')
	damn_str = damn_str.replace('€', '&euro;')
	damn_str = damn_str.replace('©', '&copy;')
	damn_str = damn_str.replace('®', '&reg;')
	damn_str = damn_str.replace('\n', '<br>')
	return damn_str

with open('paid.result.html','w', encoding='utf-8', errors='ignore') as f:
	f.write(header)
	for (root, dirs, files) in walk(tar_path):
		for file in files:
			#print(f'{proj_name}/{root[len(tar_path):]}/{file}')
			f.write(f'<h1>{join(proj_name, root[len(tar_path):],file)}</h1>')
			f.write('<p>')
			with open(f'{join(root,file)}','r', encoding='utf-8', errors='ignore') as d:
				dat = html_style_sanitize(d.read())
				f.write(dat)
			f.write('</p>')
	f.write(footer)
