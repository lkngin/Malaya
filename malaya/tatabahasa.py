tanya_list = ['kenapa','bila','siapa','mengapa','apa','bagaimana','berapa','mana']
perintah_list = ['jangan','sila','tolong','harap','usah','jemput','minta']
pangkal_list = ['maka','alkisah','arakian','syahdah','adapun','bermula','kalakian']
bantu_list = ['akan','telah','boleh','mesti','belum','sudah','dapat','masih','harus','hendak']
penguat_list = ['paling','agak','sungguh','amat','terlalu','nian','benar','paling']
penegas_list = ['jua','juga','sahaja','hanya','memang','lagi','pun']
nafi_list = ['bukan','tidak','tak','tiada','tidaklah','tidakkah']
pemeri_list = ['ialah','adalah']
sendi_list = ['akan','kepada','terhadap','bagi','untuk','dari','daripada','di','dengan','hingga','sampai',
              'ke','kepada','oleh','pada','sejak','seperti','umpama','bak','tentang','laksanabagai',
             'semenjak','dalam','antara']
pembenar_list = ['ya','benar','betul']
nombor_list = ['satu','dua','tiga','empat','lima','enam','tujuh','lapan','sembilan','kosong']
suku_bilangan_list = ['per','suku','setengah','separuh','tiga suku']
pisahan_list = ['setiap','tiap']
keterangan_list = ['begitu','begini','demikian','perlahan','cepat','lena','akan','sedang','belum',
                   'telah','sekarang','sebentar','semalam','mungkin','agak','barangkali','pasti','tentu',
                   'sudah','selalu','kadang','acapkali','sesekali','yang']
arah_list = ['atas','bawah','tepi','antara','hadapan','utara','sisi','luar']
hubung_list = ['agar','apabila','atau','bahawa','dan','hingga','jika','jikalau','kecuali','kerana',
               'lalu','manakala','sambil','serta','semenjak','sementara','sungguhpun','supaya','walaupun','tetapi','berkenan','berkenaan']
gantinama_list = ['aku','saya','hamba','patik','beta','kami','kita','anda','awak','engkau','tuanku','kalian',
                  'kamu','baginda','beliau','mereka','ini','itu','sini','situ','sana','kini','dia','rm']

# pos permulaan[:-4]
permulaan = ['bel','be','se','ter','men','memper','di','pe','me','ke','ber','pen','per']
# pos hujung [:1]
hujung = ['kan', 'kah','lah','tah','nya','an','wan','wati','ita']
alphabet = 'qwertyuiopasdfghjklzxcvbnm'

tatabahasa_dict = {'KT':tanya_list,'KP':perintah_list,'KPA':pangkal_list,'KB':bantu_list,'KPENGUAT':penguat_list,
                   'KPENEGAS':penegas_list,'NAFI':nafi_list, 'KPEMERI':pemeri_list,'KS':sendi_list,'KPEMBENAR':pembenar_list,
                   'NO':nombor_list,'SUKU':suku_bilangan_list,'PISAHAN':pisahan_list,'KETERANGAN':keterangan_list,
                   'ARAH':arah_list,'KH':hubung_list,'GN':gantinama_list}

stopword_tatabahasa = list(set(tanya_list+perintah_list+pangkal_list+bantu_list+penguat_list+\
                penegas_list+nafi_list+pemeri_list+sendi_list+pembenar_list+nombor_list+\
                suku_bilangan_list+pisahan_list+keterangan_list+arah_list+hubung_list+gantinama_list))

rules_normalizer = {'experience': 'pengalaman',
 'bagasi': 'bagasi',
 'kg': 'kampung',
 'kilo': 'kilogram',
 'g': 'gram',
 'grm': 'gram',
 'k': 'okay',
 'abgkat': 'abang dekat',
 'abis': 'habis',
 'ade': 'ada',
 'adoi': 'aduh',
 'adoii': 'aduhh',
 'aerodarat': 'kapal darat',
 'agkt': 'angkat',
 'ahh': 'ah',
 'ailior': 'air liur',
 'airasia': 'air asia x',
 'airasiax': 'penerbangan',
 'airline': 'penerbangan',
 'airlines': 'penerbangan',
 'airport': 'lapangan terbang',
 'airpot': 'lapangan terbang',
 'aje': 'sahaja',
 'ajelah': 'sahajalah',
 'ajer': 'sahaja',
 'ak': 'aku',
 'aq': 'aku',
 'all': 'semua',
 'ambik': 'ambil',
 'amek': 'ambil',
 'amer': 'amir',
 'amik': 'ambil',
 'ana': 'saya',
 'angkt': 'angkat',
 'anual': 'tahunan',
 'apapun': 'apa pun',
 'ape': 'apa',
 'arab': 'arab',
 'area': 'kawasan',
 'aritu': 'hari itu',
 'ask': 'tanya',
 'astro': 'astro',
 'at': 'pada',
 'attitude': 'sikap',
 'babi': 'khinzir',
 'back': 'belakang',
 'bag': 'beg',
 'bang': 'abang',
 'bangla': 'bangladesh',
 'banyk': 'banyak',
 'bard': 'pujangga',
 'bargasi': 'bagasi',
 'bawak': 'bawa',
 'bawanges': 'bawang',
 'be': 'jadi',
 'behave': 'berkelakuan baik',
 'belagak': 'berlagak',
 'berdisiplin': 'berdisplin',
 'berenti': 'berhenti',
 'beskal': 'basikal',
 'bff': 'rakan karib',
 'bg': 'bagi',
 'bgi': 'bagi',
 'biase': 'biasa',
 'big': 'besar',
 'bike': 'basikal',
 'bile': 'bila',
 'binawe': 'binatang',
 'bini': 'isteri',
 'bkn': 'bukan',
 'bla': 'bila',
 'blom': 'belum',
 'bnyak': 'banyak',
 'body': 'tubuh',
 'bole': 'boleh',
 'boss': 'bos',
 'bowling': 'boling',
 'bpe': 'berapa',
 'brand': 'jenama',
 'brg': 'barang',
 'briefing': 'taklimat',
 'brng': 'barang',
 'bro': 'abang',
 'bru': 'baru',
 'bruntung': 'beruntung',
 'bsikal': 'basikal',
 'btnggjwb': 'bertanggungjawab',
 'btul': 'betul',
 'buatlh': 'buatlah',
 'buh': 'letak',
 'buka': 'buka',
 'but': 'tetapi',
 'bwk': 'bawa',
 'by': 'dengan',
 'byr': 'bayar',
 'bz': 'sibuk',
 'camera': 'kamera',
 'camni': 'macam ini',
 'cane': 'macam mana',
 'cant': 'tak boleh',
 'carakerja': 'cara kerja',
 'care': 'jaga',
 'cargo': 'kargo',
 'cctv': 'kamera litar tertutup',
 'celako': 'celaka',
 'cer': 'cerita',
 'cheap': 'murah',
 'check': 'semak',
 'ciput': 'sedikit',
 'cite': 'cerita',
 'citer': 'cerita',
 'ckit': 'sikit',
 'ckp': 'cakap',
 'class': 'kelas',
 'cm': 'macam',
 'cmni': 'macam ini',
 'cmpak': 'campak',
 'committed': 'komited',
 'company': 'syarikat',
 'complain': 'aduan',
 'corn': 'jagung',
 'couldnt': 'tak boleh',
 'cr': 'cari',
 'crew': 'krew',
 'cube': 'cuba',
 'cuma': 'cuma',
 'curinyaa': 'curinya',
 'cust': 'pelanggan',
 'customer': 'pelanggan',
 'd': 'di',
 'da': 'dah',
 'dn': 'dan',
 'dahh': 'dah',
 'damaged': 'rosak',
 'dapek': 'dapat',
 'day': 'hari',
 'dazrin': 'dazrin',
 'dbalingnya': 'dibalingnya',
 'de': 'ada',
 'deep': 'dalam',
 'deliberately': 'sengaja',
 'depa': 'mereka',
 'dessa': 'desa',
 'dgn': 'dengan',
 'dh': 'dah',
 'didunia': 'di dunia',
 'diorang': 'mereka',
 'diorng': 'mereka',
 'direct': 'secara terus',
 'diving': 'junam',
 'dkt': 'dekat',
 'dlempar': 'dilempar',
 'dlm': 'dalam',
 'dlt': 'padam',
 'dlu': 'dulu',
 'done': 'siap',
 'dont': 'jangan',
 'dorg': 'mereka',
 'dpermudhkn': 'dipermudahkan',
 'dpt': 'dapat',
 'dr': 'dari',
 'dri': 'dari',
 'dsb': 'dan sebagainya',
 'dy': 'dia',
 'educate': 'mendidik',
 'ensure': 'memastikan',
 'everything': 'semua',
 'ewahh': 'wah',
 'expect': 'sangka',
 'fb': 'facebook',
 'fired': 'pecat',
 'first': 'pertama',
 'fkr': 'fikir',
 'flight': 'kapal terbang',
 'for': 'untuk',
 'free': 'percuma',
 'friend': 'kawan',
 'fyi': 'untuk pengetahuan anda',
 'gantila': 'gantilah',
 'gantirugi': 'ganti rugi',
 'gentlemen': 'lelaki budiman',
 'gerenti': 'jaminan',
 'gile': 'gila',
 'gk': 'juga',
 'gnti': 'ganti',
 'go': 'pergi',
 'gomen': 'kerajaan',
 'goment': 'kerajaan',
 'good': 'baik',
 'ground': 'tanah',
 'guarno': 'macam mana',
 'hampa': 'mereka',
 'hampeh': 'teruk',
 'hanat': 'jahanam',
 'handle': 'kawal',
 'handling': 'kawalan',
 'hanta': 'hantar',
 'haritu': 'hari itu',
 'hate': 'benci',
 'have': 'ada',
 'hawau': 'celaka',
 'henpon': 'telefon',
 'heran': 'hairan',
 'him': 'dia',
 'his': 'dia',
 'hmpa': 'mereka',
 'hntr': 'hantar',
 'hotak': 'otak',
 'hr': 'hari',
 'i': 'saya',
 'hrga': 'harga',
 'hrp': 'harap',
 'hu': 'sedih',
 'humble': 'merendah diri',
 'ibon': 'ikon',
 'ichi': 'inci',
 'idung': 'hidung',
 'if': 'jika',
 'ig': 'instagram',
 'iklas': 'ikhlas',
 'improve': 'menambah baik',
 'in': 'masuk',
 'isn t': 'tidak',
 'isyaallah': 'insyallah',
 'ja': 'sahaja',
 'japan': 'jepun',
 'jd': 'jadi',
 'je': 'saja',
 'jee': 'saja',
 'jek': 'saja',
 'jepun': 'jepun',
 'jer': 'saja',
 'jerr': 'saja',
 'jez': 'saja',
 'jg': 'juga',
 'jgk': 'juga',
 'jgn': 'jangan',
 'jgnla': 'janganlah',
 'jibake': 'celaka',
 'jjur': 'jujur',
 'job': 'kerja',
 'jobscope': 'skop kerja',
 'jogja': 'jogjakarta',
 'jpam': 'jpam',
 'jth': 'jatuh',
 'jugak': 'juga',
 'ka': 'ke',
 'kalo': 'kalau',
 'kalu': 'kalau',
 'kang': 'nanti',
 'kantoi': 'temberang',
 'kasi': 'beri',
 'kat': 'dekat',
 'kbye': 'ok bye',
 'kearah': 'ke arah',
 'kecik': 'kecil',
 'keja': 'kerja',
 'keje': 'kerja',
 'kejo': 'kerja',
 'keksongan': 'kekosongan',
 'kemana': 'ke mana',
 'kene': 'kena',
 'kenekan': 'kenakan',
 'kesah': 'kisah',
 'ketempat': 'ke tempat',
 'kije': 'kerja',
 'kijo': 'kerja',
 'kiss': 'cium',
 'kite': 'kita',
 'kito': 'kita',
 'kje': 'kerja',
 'kjr': 'kerja',
 'kk': 'okay',
 'kmi': 'kami',
 'kt': 'kat',
 'tlg': 'tolong',
 'kl': 'kuala lumpur',
 'klai': 'kalau',
 'klau': 'kalau',
 'klia': 'klia',
 'klo': 'kalau',
 'klu': 'kalau',
 'kn': 'kan',
 'knapa': 'kenapa',
 'kne': 'kena',
 'ko': 'kau',
 'kompom': 'sah',
 'korang': 'kamu semua',
 'korea': 'korea',
 'korg': 'kamu semua',
 'kot': 'mungkin',
 'krja': 'kerja',
 'ksalahan': 'kesalahan',
 'kta': 'kita',
 'kuar': 'keluar',
 'kut': 'mungkin',
 'la': 'lah',
 'laa': 'lah',
 'lahabau': 'celaka',
 'lahanat': 'celaka',
 'lainda': 'lain dah',
 'lak': 'pula',
 'last': 'akhir',
 'le': 'lah',
 'leader': 'ketua',
 'leave': 'pergi',
 'ler': 'lah',
 'less': 'kurang',
 'letter': 'surat',
 'lg': 'lagi',
 'lgi': 'lagi',
 'lngsong': 'langsung',
 'lol': 'hehe',
 'lorr': 'lah',
 'low': 'rendah',
 'lps': 'lepas',
 'luggage': 'bagasi',
 'lumbe': 'lumba',
 'lyak': 'layak',
 'maap': 'maaf',
 'maapkan': 'maafkan',
 'mahai': 'mahal',
 'mampos': 'mampus',
 'mart': 'kedai',
 'mau': 'mahu',
 'mcm': 'macam',
 'mcmtu': 'macam itu',
 'memerlukn': 'memerlukan',
 'mengembirakan': 'menggembirakan',
 'mengmbilnyer': 'mengambilnya',
 'mengtasi': 'mengatasi',
 'mg': 'memang',
 'mihak': 'memihak',
 'min': 'admin',
 'mingu': 'minggu',
 'mintak': 'minta',
 'mjtuhkn': 'menjatuhkan',
 'mkyong': 'mak yong',
 'mlibatkn': 'melibatkan',
 'mmg': 'memang',
 'mmnjang': 'memanjang',
 'mmpos': 'mampus',
 'mn': 'mana',
 'mna': 'mana',
 'mntak': 'minta',
 'mntk': 'minta',
 'mnyusun': 'menyusun',
 'mood': 'suasana',
 'most': 'paling',
 'mr': 'tuan',
 'msa': 'masa',
 'msia': 'malaysia',
 'mst': 'mesti',
 'mu': 'awak',
 'much': 'banyak',
 'muko': 'muka',
 'mum': 'emak',
 'n': 'dan',
 'nah': 'nah',
 'nanny': 'nenek',
 'napo': 'kenapa',
 'nati': 'nanti',
 'ngan': 'dengan',
 'ngn': 'dengan',
 'ni': 'ini',
 'nie': 'ini',
 'nii': 'ini',
 'nk': 'nak',
 'nmpk': 'nampak',
 'nye': 'nya',
 'ofis': 'pejabat',
 'ohh': 'oh',
 'oii': 'hoi',
 'one': 'satu',
 'online': 'dalam talian',
 'or': 'atau',
 'org': 'orang',
 'orng': 'orang',
 'otek': 'otak',
 'p': 'pergi',
 'paid': 'dah bayar',
 'palabana': 'kepala otak',
 'pasni': 'lepas ini',
 'passengers': 'penumpang',
 'passengger': 'penumpang',
 'pastu': 'lepas itu',
 'pd': 'pada',
 'pegi': 'pergi',
 'pekerje': 'pekerja',
 'pekrja': 'pekerja',
 'perabih': 'perabis',
 'perkerja': 'pekerja',
 'pg': 'pergi',
 'phuii': 'puih',
 'pikir': 'fikir',
 'pilot': 'juruterbang',
 'pk': 'fikir',
 'pkerja': 'pekerja',
 'pkerjaan': 'pekerjaan',
 'pki': 'pakai',
 'please': 'tolong',
 'pls': 'tolong',
 'pn': 'pun',
 'pnh': 'pernah',
 'pnt': 'penat',
 'pnya': 'punya',
 'pon': 'pun',
 'priority': 'keutamaan',
 'properties': 'harta benda',
 'ptugas': 'petugas',
 'pub': 'kelab malam',
 'pulak': 'pula',
 'puye': 'punya',
 'pwrcuma': 'percuma',
 'pyahnya': 'payahnya',
 'quality': 'kualiti',
 'quit': 'keluar',
 'ramly': 'ramly',
 'rege': 'harga',
 'reger': 'harga',
 'report': 'laporan',
 'resigned': 'meletakkan jawatan',
 'respect': 'hormat',
 'rizal': 'rizal',
 'rosak': 'rosak',
 'rosok': 'rosak',
 'rse': 'rasa',
 'sacked': 'buang',
 'sado': 'tegap',
 'salute': 'sanjung',
 'sam': 'sama',
 'same': 'sama',
 'samp': 'sampah',
 'sbb': 'sebab',
 'sbgai': 'sebagai',
 'sblm': 'sebelum',
 'sblum': 'sebelum',
 'sbnarnya': 'sebenarnya',
 'sbum': 'sebelum',
 'sdg': 'sedang',
 'sebb': 'sebab',
 'sebijik': 'sebiji',
 'see': 'lihat',
 'seen': 'dilihat',
 'selangor': 'selangor',
 'selfie': 'swafoto',
 'sempoi': 'cantik',
 'senaraihitam': 'senarai hitam',
 'seorg': 'seorang',
 'service': 'perkhidmatan',
 'sgt': 'sangat',
 'shared': 'kongsi',
 'shirt': 'kemeja',
 'shut': 'tutup',
 'sib': 'nasib',
 'skali': 'sekali',
 'sket': 'sikit',
 'sma': 'sama',
 'smoga': 'semoga',
 'smpoi': 'cantik',
 'sndiri': 'sendiri',
 'sndr': 'sendiri',
 'sndri': 'sendiri',
 'sne': 'sana',
 'so': 'jadi',
 'sop': 'tatacara pengendalian piawai',
 'sorang': 'seorang',
 'spoting': 'pembintikan',
 'sronok': 'seronok',
 'ssh': 'susah',
 'staff': 'staf',
 'standing': 'berdiri',
 'start': 'mula',
 'steady': 'mantap',
 'stiap': 'setiap',
 'stress': 'stres',
 'student': 'pelajar',
 'study': 'belajar',
 'studycase': 'kajian kes',
 'sure': 'pasti',
 'sykt': 'syarikat',
 'tah': 'entah',
 'taik': 'tahi',
 'takan': 'tak akan',
 'takat': 'setakat',
 'takde': 'tak ada',
 'takkan': 'tak akan',
 'taknak': 'tak nak',
 'tang': 'tentang',
 'tanggungjawab': 'bertanggungjawab',
 'taraa': 'sementara',
 'tau': 'tahu',
 'tbabit': 'terbabit',
 'team': 'pasukan',
 'terbaekk': 'terbaik',
 'teruknye': 'teruknya',
 'tgk': 'tengok',
 'that': 'itu',
 'thinking': 'fikir',
 'those': 'itu',
 'time': 'masa',
 'tk': 'tak',
 'tnggongjwb': 'tanggungjawab',
 'tngok': 'tengok',
 'tngu': 'tunggu',
 'to': 'kepada',
 'tosak': 'rosak',
 'tp': 'tapi',
 'tpi': 'tapi',
 'tpon': 'telefon',
 'transfer': 'pindah',
 'trgelak': 'tergelak',
 'ts': 'tan sri',
 'tstony': 'tan sri tony',
 'tu': 'itu',
 'tuh': 'itu',
 'tula': 'itulah',
 'umeno': 'umno',
 'unfortunately': 'malangnya',
 'unhappy': 'tidak gembira',
 'up': 'naik',
 'upkan': 'naikkan',
 'ur': 'awak',
 'utk': 'untuk',
 'very': 'sangat',
 'viral': 'tular',
 'vote': 'undi',
 'warning': 'amaran',
 'warranty': 'waranti',
 'wassap': 'whatsapp',
 'wat': 'apa',
 'weii': 'wei',
 'well': 'maklumlah',
 'win': 'menang',
 'with': 'dengan',
 'wt': 'buat',
 'x': 'tak',
 'tw': 'tahu',
 'ye': 'ya',
 'yee': 'ya',
 'yg': 'yang',
 'yng': 'yang',
 'you': 'awak',
 'your': 'awak',
 'sakai':'selekeh',
 'rmb': 'billion ringgit',
 'rmj': 'juta ringgit',
 'rmk': 'ribu ringgit',
 'rm': 'ringgit'}
