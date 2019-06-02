def menu():
    print ('1.  Request with Urllib')
    print ('2.  Respnse Object')
    print ('3.  Status Codes')
    print ('4.  Handling Problem')
    print ('5.  HTTP Headers')
    print ('6.  Customizing Request')
    print ('    6a. Content Compression')
    print ('    6b. Multiple Values')
    print ('----Content Negotiation')
    print ('7a. Content Types')
    print ('8.  User Agents')
    print ('9.  Cookies')
    print ('10. Redirects')
    print ('11. URLs')
    print ('12. HTTP Methods')
    print ('13. Formal Inspection')
    print ('14. HTTPS')
    print ('15. The Request Library')
    
def request_urllib():
    from urllib.request import urlopen
    response = urlopen('http://www.debian.org')
    print()
    print('Request URLlib --> urllib.request ')
    print('merupakan modul untuk mengajukan permintaan dan menerima tanggapan')
    print('-------------------------------------------------------------------')
    print()
    print(response)
    print(response.readline())
    print()
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def response_object():
    print()
    print('Response Objects')
    print('Digunakan untuk memberi akses ke sumber data yang diminta')
    print('-------------------------------------------------------------------')
    print()
    print('melihat respon URL')
    from urllib.request import urlopen
    response = urlopen('http://www.debian.org')
    print(response.url)
    print()
    print('Membaca data di baris ke 50')
    print(response.read(50))
    print()
    print('Membaca seluruh file di link')
    print(response.read())
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def status_codes():
    print()
    print('HTTP responses/status codes')
    print('Digunakan untuk  memberi tanggapan data sebelum kita membaca data')
    print('Kode Status membantu kita melihat apakah respons berhasil atau tidak')
    print('--------------------------------------------------------------------')
    print()
    print('Response code dari debian')
    from urllib.request import urlopen
    response = urlopen('http://www.debian.org')
    print(response.status)
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()


def handling_problem():
    print()
    print('Handling Problem')
    print('Memeriksa kode status dengan memunculkan eksepsi jika menemui masalah.')
    print('-------------------------------------------------------------------')
    import urllib.error
    from urllib.request import urlopen
    try:
            urlopen('http://www.ietf.org/rfc/rfc0.txt')
    except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
            print('url', e.url)
    print()
    print('contoh dengan ip yang di tentukan -> http://192.0.2.1/index.html')
    print(urlopen('http://192.0.2.1/index.html'))
    print()
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.ietf.org/rfc/rfc0.txt')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

   

    
def http_headers():
    print()
    print('HTTP Headers')
    print('Digunakan untuk melihat respons objek')
    print('-------------------------------------------------------------------')
    from urllib.request import urlopen
    response = urlopen('http://www.debian.org')
    print(response.getheaders())
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()



def customizing_request():
    print()
    print('Customizing Request')
    print('Untuk membuat request objek')
    print('-------------------------------------------------------------------')
    print()
    print('Membuat request objek')
    from urllib.request import Request
    from urllib.request import urlopen
    req = Request('http://www.debian.org')
    print(req.add_header('Accept-Language', 'sv'))
    print()
    print('Membuat request sampai baris ke 5')
    response = urlopen(req)
    print(response.readlines()[:5])
    print()
    print('Membuat request objek')
    print(req.add_header('Accept-Language', 'sv'))
    print(req.header_items())
    print()
    print()
    response = urlopen(req)
    print(req.header_items())
    print()
    print()
    headers = {'Accept-Language': 'sv'}
    req = Request('http://www.debian.org', headers=headers)
    print(req.header_items())
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def content_compression():
    print()
    print('Content Compression')
    print('Untuk merequest sebuah dokumen dan mengambil dari server untuk menggunakan kompresi gzip untuk response body')
    print('-------------------------------------------------------------------')
    from urllib.request import Request
    from urllib.request import urlopen
    req = Request('http://www.debian.org')
    print(req.add_header('Accept-Encoding', 'gzip'))
    print()
    print('kirim dengan bantuan urlopen')
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    print()
    print('decompres tubuh data dengan modul gzip')
    import gzip
    content = gzip.decompress(response.read())
    print(content.splitlines()[:5])
    print()
    print('Mari kita lihat apa yang terjadi jika kita tidak meminta kompresi dengan menggunakan pengkodean identitas:')
    req = Request('http://www.debian.org')
    print(req.add_header('Accept-Encoding', 'identity'))
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def multiple_values():
    from urllib.request import Request
    from urllib.request import urlopen
    print()
    print('Multple Values')
    print('-------------------------------------------------------------------')
    req = Request('http://www.debian.org')
    encodings = 'deflate, gzip, identity'
    print(req.add_header('Accept-Encoding', encodings))
    print()
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    encodings = 'gzip, deflate;q=0.8, identity;q=0.0'
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()


def content_types():
    print()
    print('Content Types')
    print('-------------------------------------------------------------------')
    from urllib.request import urlopen
    response = urlopen('http://www.debian.org')
    print(response.getheader('Content-Type'))
    print()
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org')
    print('-------------------------------------------------------------------')
    print()
    responses = urlopen('http://www.python.org')
    format, params = responses.getheader('Content-Type').split(';')
    print(params)
    print()
    charset = params.split('=')[1]
    print()
    print(charset)
    print()
    content = responses.read().decode(charset)
    print(content)
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.python.org')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()


def user_agents():
    print()
    print('User Agents')
    print('-------------------------------------------------------------------')
    from urllib.request import Request
    from urllib.request import urlopen
    req = Request('http://www.python.org')
    print(urlopen(req))
    print(req.get_header('User-agent'))
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.python.org')
    print('-------------------------------------------------------------------')
    print()
    requests = Request('http://www.debian.org')
    print(requests.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0'))
    response = urlopen(requests)
    print(response)
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.debian.org ')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()
   

def cookie():
    print()
    print('Cookie')
    print('adalah sepotong kecil data yang dikirimkan server dalam header Set-Cookie sebagai bagian dari respon')
    print('--------------------------------------------------------------------')
    print()
    print('Cookie Handling')
    from http.cookiejar import CookieJar
    cookie_jar = CookieJar()
    from urllib.request import build_opener, HTTPCookieProcessor
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    opener.open('http://www.github.com')
    len(cookie_jar)
    print('-------------------------------------------------------------------')
    print()
    print('Know Your cookies')
    cookies = list(cookie_jar)
    print(cookies)
    print(cookies[0].name)
    print(cookies[0].value)
    print(cookies[0].domain)
    print(cookies[0].path)
    print(cookies[0].expires)
    import datetime
    print(datetime.datetime.fromtimestamp(cookies[0].expires))
    print(cookies[0].get_nonstandard_attr('HttpOnly'))
    print(cookies[0].secure)
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.github.com')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()
   

def redirect():
    print()
    print('Redirect')
    print('Merupakan pengalihan konten ke alamat baru')
    print('--------------------------------------------------------------------')
    print()
    from urllib.request import Request
    from urllib.request import urlopen
    req = Request('http://www.gmail.com')
    response = urlopen(req)
    print(response.url)
    print(req.redirect_dict)
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.gmail.com')
    print('-------------------------------------------------------------------')
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()


def URLs():
    print()
    print('URLs')
    print()
    from urllib.parse import urlparse
    result = urlparse('http://www.python.org/dev/peps')
    print(result)
    print(result.netloc)
    print(result.path)
    print(urlparse('http://www.python.org:8080/'))
    print()
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.python.org:8080/')
    print('-------------------------------------------------------------------')
    print()
    print('--------------Path and Relatuve URLs-------------------------------')
    print(urlparse('http://www.python.org/'))
    print(urlparse('../images/tux.png'))
    from urllib.parse import urljoin
    print(urljoin('http://www.debian.org', 'intro/about'))
    print(urljoin('http://www.debian.org/intro/', 'about'))
    print(urljoin('http://www.debian.org/intro', 'about'))
    print(urljoin('http://www.debian.org/intro/about', '/News'))
    print(urljoin('http://www.debian.org/intro/about/', '../News'))
    print(urljoin('http://www.debian.org/intro/about/', '../../News'))
    print(urljoin('http://www.debian.org/intro/about', '../News'))
    print(urljoin('http://www.debian.org/about', 'http://www.python.org'))
    print()
    print('-------------------------------------------------------------------')
    print('sumber link dari http://www.python.org:8080/')
    print('-------------------------------------------------------------------')
    print()
    #print('--------------Query Strings-----------------------------------')
    #print(urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default'))
    #from urllib.parse import parse_qs
    #results = urlparse
    #print(parse_qs(results.query))
    #resultt = urlparse
    #print(parse_qs(resultt.query))
    print()
    print('--------------URL Encoding-----------------------------------')
    from urllib.parse import quote
    print(quote('A duck?'))
    path = 'pypi'
    path_enc = quote(path)
    from urllib.parse import urlencode
    query_dict = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
    query_enc = urlencode(query_dict)
    print(query_enc)
    from urllib.parse import urlunparse
    netloc = 'pypi.python.org'
    print(urlunparse(('http', netloc, path_enc, '', query_enc, '')))
    from urllib.parse import quote
    pathh = '/images/users/+Zoot+/'
    print(quote(pathh))
    username = '+Zoot/Dingo+'
    pathhh = 'images/users/{}'.format(username)
    print(quote(pathhh))
    username1 = '+Zoot/Dingo+'
    user_encoded = quote(username1, safe='')
    path1 = '/'.join(('', 'images', 'users', username1))
    print(path1)
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()


def http_methods():
    print('--------------The HEAD Method-----------------------------------')
    from urllib.request import Request
    from urllib.request import urlopen
    req = Request('http://www.google.com', method='HEAD')
    response = urlopen(req)
    print(response.status)
    print(response.read())
    print('--------------The POST Method-----------------------------------')
    data_dict = {'P': 'Python'}
    data = urlencode(data_dict).encode('utf-8')
    req1 = Request('http://search.debian.org/cgi-bin/omega', data=data)
    req1.add_header('Content-Type', 'application/x-www-form-urlencode;charset=UTF-8')
    responses = urlopen(req1)
    print(responses)
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def request_library():
    print()
    print('Request Library')
    print('--------------------------------------------------------------------')
    from urllib.request import requests
    response = requests.get('http://www.debian.org')
    print(response.status_code)
    print(response.reason)
    print(response.url)
    print(response.headers['content-type'])
    print(response.ok)
    print(response.is_redirect)
    print(response.request.headers)
    print(response.headers['content-encoding'])
    print(response.content)
    print(response.text)
    print(response.encoding)
    response.encoding='utf-8'
    print(response = requests.get('http://www.github.com'))
    print(response.cookies)
    s = requests.Session()
    s.get('http://www.google.com')
    responses = s.get('http://google.com/preferences')
    print(responses.url)
    respon = requests.head('http://www.google.com')
    print(respon.status_code)
    print(respon.text)
    headers = {'User-Agent': 'Mozilla/5.0 Firefox 24'}
    res = requests.get('http://www.debian.org', headers=headers)
    print(res.url)
    params = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
    response = requests.get('http://pypi.python.org/pypi', params=params)
    print(response.url)
    data = {'P', 'Python'}
    res = requests.post('http://search.debian.org/cgi-bin/omega', data=data)
    print()
    print('------------------Handling Errors with Requests-----------------------')
    response = requests.get('http://www.google.com/notawebpage')
    print(response.status_code)
    print(response.raise_for_status())
    r = requests.get('http://www.google.com')
    print(r.status_code)
    print(r.raise_for_status())
    re = requests.get('http://192.0.2.1')
    print(re.status_code)
    print()
    print('Mau Coba Lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()
    



print('Program menampilkan kode pada HTTP')
print('----------------------------------')
menu()
while 1:
    pilih=input('Masukkan Pilihan Anda :')
    if pilih=='1':
        request_urllib()
    elif pilih=='2':
        response_object()
    elif pilih=='3':
        status_codes()
    elif pilih=='4':
        handling_problem()
    elif pilih=='5':
        http_headers()
    elif pilih=='6':
        customizing_request()
    elif pilih=='6a':
        content_compression()
    elif pilih=='6b':
        multiple_values()
    elif pilih=='7a':
        content_types()
    elif pilih=='8':
        user_agents()
    elif pilih=='9':
        cookie()
    elif pilih=='10':
        redirect()
    elif pilih=='11':
        URLs()
    elif pilih=='12':
        http_methods()
    elif pilih=='13':
        request_library()
    else:
        print('Maaf pilihan yang anda masukkan tidak terdaftar')
        print('Coba Lagi [Y/N]?')
        coba = input().upper()
        if coba == 'Y':
            menu()
        else:
            exit()
