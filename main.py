import requests
url = str(input('Enter video URL : '))
param = (url.strip("https://www.youtube.com/watch?v="))
print('PARAMETER = ' + (param))
thumb = requests.get('https://i.ytimg.com/vi/' + str(param)+ '/hqdefault.jpg')
url1 = ('https://i.ytimg.com/vi/' + str(param)+ '/hqdefault.jpg')
print('DOWNLOADING THUMBNAIL.... from '+ str(url1))
if thumb.status_code == 200:
    with open(str(param) + ".jpg", 'wb') as f:
        f.write(thumb.content)
        print('THUMBNAIL SAVED SUCCESSFULLY!!')
