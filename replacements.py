ascii_replacements = {' ': ' ', '!': '!', '"': '"', '#': '#', '$': '$', '%': '%', '&': '&', 
"'": "'", '(': '(', ')': ')', '*': '*', '+': '+', ',': ',', '-': '-', 
'.': '.', '/': '/', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', 
'5': '5', '6': '6', '7': '7', '8': '8', '9': '9', ':': ':', ';': ';', 
'<': '<', '=': '=', '>': '>', '?': '?', '@': '@', 'A': 'A', 'B': 'B', 
'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 
'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 
'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 
'X': 'X', 'Y': 'Y', 'Z': 'Z', '[': '[', '\\': '\\', ']': ']', '^': '^', 
'_': '_', '`': '`', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 
'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 
'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 
't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 
'{': '{', '|': '|', '}': '}', '~': '~', '¡': '', '¢': 'c', '£': 'GBP', 
'¥': 'Y', '§': '', '°': '', '±': '+/-', '²': '', '³': '', 'µ': '', 
'·': '', '¼': '1/4', '½': '1/2', '¾': '3/4', 'À': 'A', 'Á': 'A', 'Â': 'A', 
'Æ': 'AE', 'Ç': 'C', 'È': 'E', 'É': 'E', 'Í': 'I', 'Î': 'I', 'Ð': 'D', 
'Ó': 'O', 'Ö': 'O', '×': 'x', 'Ø': 'O', 'Ú': 'U', 'Ü': 'U', 'ß': 'ss', 
'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'å': 'a', 'æ': 'ae', 
'ç': 'c', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i', 'í': 'i', 
'î': 'i', 'ï': 'i', 'ð': 'dh', 'ñ': 'n', 'ò': 'o', 'ó': 'o', 'ô': 'o', 
'õ': 'o', 'ö': 'o', 'ø': 'o', 'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 
'ý': 'y', 'þ': 'th', 'Ā': 'A', 'ā': 'a', 'ă': 'a', 'ą': 'a', 'ć': 'c', 
'Č': 'C', 'č': 'c', 'Đ': 'D', 'đ': 'd', 'Ē': 'E', 'ē': 'e', 'ė': 'e', 
'ę': 'e', 'ě': 'e', 'ğ': 'g', 'ġ': 'g', 'ĩ': 'i', 'Ī': 'I', 'ī': 'i', 
'ĭ': 'i', 'İ': 'I', 'ı': 'i', 'ĺ': 'l', 'Ł': 'L', 'ł': 'l', 'ń': 'n', 
'ŋ': 'ng', 'Ō': 'O', 'ō': 'o', 'ŏ': 'o', 'ő': 'o', 'œ': 'oe', 'Ś': 'S', 
'ś': 's', 'Ş': 'S', 'ş': 's', 'Š': 'S', 'š': 's', 'ũ': 'u', 'ū': 'u', 
'ŭ': 'u', 'ź': 'z', 'Ż': 'Z', 'Ž': 'Z', 'ž': 'z', 'Ǝ': 'E', 'ơ': 'o', 
'ư': 'u', 'ǎ': 'a', 'ǒ': 'o', 'ǔ': 'u', 'ǣ': 'ae', 'ș': 's', 'ɑ': 'a', 
'ɒ': 'a', 'ɔ': 'o', 'ə': 'e', 'ɛ': 'e', 'ɜ': '', 'ɡ': 'g', 'ɦ': 'h', 
'ɪ': 'I', 'ʃ': 'S', 'ʊ': 'u', 'ʌ': '', 'ʒ': 'zh', 'ʰ': '', 'ʻ': '', 
'ʾ': '', 'ʿ': '', 'ˈ': "'", 'ˌ': ',', 'ː': ':', '́': '', '̍': '', 
'̚': '', '̝': '', '̠': '', '̥': '', 'Α': '', 'Β': '', 'Δ': '', 
'Ζ': '', 'Η': '', 'Ι': '', 'Κ': '', 'Ν': '', 'Π': '', 'Ρ': '', 
'Τ': '', 'Ω': '', 'ά': '', 'έ': '', 'ή': '', 'ί': '', 'α': '', 
'β': '', 'γ': '', 'δ': '', 'ε': '', 'ζ': '', 'η': '', 'θ': '', 
'ι': '', 'κ': '', 'λ': '', 'μ': '', 'ν': '', 'ο': '', 'π': '', 
'ρ': '', 'ς': '', 'σ': '', 'τ': '', 'υ': '', 'χ': '', 'ψ': '', 
'ω': '', 'ό': '', 'ύ': '', 'ώ': '', 'Ϭ': '', 'А': '', 'Б': '', 
'В': '', 'Г': '', 'Д': '', 'З': '', 'И': '', 'К': '', 'М': '', 
'Н': '', 'О': '', 'П': '', 'Р': '', 'С': '', 'Т': '', 'Ф': '', 
'Х': '', 'Э': '', 'а': '', 'б': '', 'в': '', 'г': '', 'д': '', 
'е': '', 'з': '', 'и': '', 'й': '', 'к': '', 'л': '', 'м': '', 
'н': '', 'о': '', 'п': '', 'р': '', 'с': '', 'т': '', 'у': '', 
'ц': '', 'ч': '', 'щ': '', 'ы': '', 'ь': '', 'э': '', 'я': '', 
'і': '', 'ѣ': '', 'ү': '', 'ә': '', 'ְ': '', 'ִ': '', 'ַ': '', 
'י': '', 'ם': '', 'מ': '', 'צ': '', 'ר': '', 'آ': '', 'أ': '', 
'إ': '', 'ا': '', 'ب': '', 'ة': '', 'ت': '', 'ج': '', 'ح': '', 
'خ': '', 'د': '', 'ر': '', 'ز': '', 'س': '', 'ش': '', 'ص': '', 
'ط': '', 'ظ': '', 'ع': '', 'ـ': '', 'ف': '', 'ق': '', 'ك': '', 
'ل': '', 'م': '', 'ن': '', 'ه': '', 'و': '', 'ي': '', 'َ': '', 
'ِ': '', 'پ': '', 'چ': '', 'ڠ': '', 'ک': '', 'ڪ': '', 'گ': '', 
'ہ': '', 'ی': '', 'आ': '', 'क': '', 'ङ': '', 'च': '', 'ज': '', 
'ञ': '', 'त': '', 'थ': '', 'न': '', 'म': '', 'य': '', 'र': '', 
'ल': '', 'श': '', 'ष': '', 'स': '', 'ा': '', 'ी': '', 'ु': '', 
'ृ': '', 'े': '', 'ो': '', '्': '', 'ং': '', 'উ': '', 'ক': '', 
'খ': '', 'গ': '', 'ছ': '', 'জ': '', 'ট': '', 'ঠ': '', 'ঢ': '', 
'ণ': '', 'ত': '', 'দ': '', 'ধ': '', 'ন': '', 'প': '', 'ফ': '', 
'ব': '', 'ভ': '', 'ম': '', 'র': '', 'ল': '', 'শ': '', 'স': '', 
'হ': '', 'া': '', 'ি': '', 'ী': '', 'ু': '', 'ে': '', 'ৈ': '', 
'্': '', 'ৎ': '', 'ಂ': '', 'ಗ': '', 'ಬ': '', 'ರ': '', 'ಲ': '', 
'ಳ': '', 'ವ': '', 'ೀ': '', 'ು': '', 'ೂ': '', 'ೆ': '', '್': '', 
'ก': '', 'ข': '', 'ค': '', 'ง': '', 'จ': '', 'ช': '', 'ฑ': '', 
'ฒ': '', 'ณ': '', 'ด': '', 'ต': '', 'ถ': '', 'ท': '', 'ธ': '', 
'น': '', 'บ': '', 'ป': '', 'พ': '', 'ภ': '', 'ม': '', 'ย': '', 
'ร': '', 'ล': '', 'ว': '', 'ศ': '', 'ษ': '', 'ส': '', 'ห': '', 
'อ': '', 'ฯ': '', 'ะ': '', 'ั': '', 'า': '', 'ำ': '', 'ิ': '', 
'ี': '', 'ื': '', 'ุ': '', 'ู': '', '฿': 'THB', 'เ': '', 'แ': '', 
'โ': '', 'ไ': '', '้': '', '์': '', 'ሊ': '', 'ላ': '', 'ሎ': '', 
'ሕ': '', 'ሞ': '', 'ሪ': '', 'ራ': '', 'ሮ': '', 'ሲ': '', 'ብ': '', 
'ት': '', 'ቶ': '', 'አ': '', 'ኢ': '', 'ክ': '', 'ወ': '', 'ዊ': '', 
'ዘ': '', 'የ': '', 'ያ': '', 'ይ': '', 'ዮ': '', 'ዲ': '', 'ዴ': '', 
'ጥ': '', 'ጵ': '', 'ፌ': '', 'ፐ': '', 'គ': '', 'ជ': '', 'ន': '', 
'ព': '', 'រ': '', 'ា': '', 'ៃ': '', 'ះ': '', '្': '', 'ᮊ': '', 
'ᮓ': '', 'ᮔ': '', 'ᮕ': '', 'ᮜ': '', 'ᮞ': '', 'ᮥ': '', '᮪': '', 
'ḍ': 'd', 'ḗ': 'e', 'Ḥ': 'H', 'ḥ': 'h', 'ṃ': 'm', 'ṅ': 'n', 'ṇ': 'n', 
'ṓ': 'o', 'ṗ': 'p', 'ṣ': 's', 'Ṭ': 'T', 'ṭ': 't', 'ẚ': 'a', 'ạ': 'a', 
'ả': 'a', 'ấ': 'a', 'ầ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a', 'ắ': 'a', 
'ằ': 'a', 'ẵ': 'a', 'ẻ': 'e', 'ế': 'e', 'ề': 'e', 'ể': 'e', 'ễ': 'e', 
'ệ': 'e', 'ỉ': 'i', 'ị': 'i', 'ọ': 'o', 'ố': 'o', 'ồ': 'o', 'ổ': 'o', 
'ộ': 'o', 'ớ': 'o', 'ờ': 'o', 'ở': 'o', 'ợ': 'o', 'ụ': 'u', 'Ủ': 'U', 
'ủ': 'u', 'ứ': 'u', 'ừ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u', 'ỳ': 'y', 
'ỹ': 'y', 'Ἑ': '', 'ἡ': '', 'ἰ': '', 'ἱ': '', 'ἴ': '', 'ἵ': '', 
'Ἰ': '', 'Ἱ': '', 'ὤ': '', 'ὰ': '', 'ὴ': '', 'ὶ': '', 'ῆ': '', 
'Ῥ': '', 'ῷ': '', '\u2009': ' ', '\u200a': ' ', '\u200b': '', '\u200c': '', '\u200d': '', 
'\u200e': '', '‑': '-', '–': '-', '—': '-', '‘': "'", '’': "'", '‚': ',', 
'“': '"', '”': '"', '•': '*', '…': '...', '\u202c': '', '\u202f': ' ', '′': "'", 
'″': '"', '‹': '<', '›': '>', '⁄': '/', '\u2061': '', 'ⁿ': '', '₁': '', 
'₂': '', '₣': 'FF', '₨': 'Rs', '₩': 'KRW', '€': 'EUR', '₱': 'PHP', '₹': 'INR', 
'₽': 'RUB', '⅓': '1/3', '⅔': '2/3', '→': '->', '−': '-', '≈': '~=', '⊙': '', 
'⋅': '*', '☉': '', '♠': '', '♭': '', '❤': '', 'ⲏ': '', 'ⲓ': '', 
'ⲙ': '', 'ⲛ': '', 'ⲥ': '', 'Ⲭ': '', 'ⲱ': '', 'う': '', 'お': '', 
'か': '', 'き': '', 'こ': '', 'ご': '', 'し': '', 'じ': '', 'す': '', 
'た': '', 'ど': '', 'な': '', 'に': '', 'の': '', 'は': '', 'ぷ': '', 
'み': '', 'め': '', 'ゃ': '', 'や': '', 'ら': '', 'る': '', 'れ': '', 
'ん': '', 'カ': '', 'ジ': '', 'タ': '', 'ッ': '', 'テ': '', 'ノ': '', 
'バ': '', 'メ': '', 'ャ': '', 'ラ': '', 'ル': '', 'ン': '', 'ー': '', 
'一': '', '三': '', '上': '', '下': '', '不': '', '世': '', '丘': '', 
'东': '', '中': '', '主': '', '之': '', '乐': '', '九': '', '习': '', 
'书': '', '二': '', '于': '', '五': '', '京': '', '亭': '', '人': '', 
'付': '', '伐': '', '会': '', '佛': '', '侠': '', '侨': '', '倒': '', 
'倭': '', '備': '', '儿': '', '兔': '', '內': '', '全': '', '八': '', 
'公': '', '兮': '', '共': '', '关': '', '内': '', '出': '', '別': '', 
'剧': '', '劇': '', '勒': '', '包': '', '化': '', '北': '', '区': '', 
'區': '', '十': '', '华': '', '南': '', '印': '', '厥': '', '县': '', 
'反': '', '发': '', '叔': '', '古': '', '台': '', '史': '', '司': '', 
'名': '', '呂': '', '和': '', '商': '', '嘉': '', '四': '', '园': '', 
'国': '', '國': '', '土': '', '地': '', '圳': '', '坂': '', '坑': '', 
'城': '', '域': '', '堂': '', '堤': '', '場': '', '士': '', '声': '', 
'外': '', '多': '', '大': '', '天': '', '央': '', '头': '', '好': '', 
'委': '', '娘': '', '子': '', '孤': '', '学': '', '孫': '', '學': '', 
'安': '', '完': '', '官': '', '定': '', '宝': '', '宮': '', '家': '', 
'富': '', '寺': '', '寿': '', '尔': '', '尼': '', '尾': '', '屋': '', 
'展': '', '山': '', '岳': '', '岸': '', '嶺': '', '州': '', '巡': '', 
'市': '', '帝': '', '带': '', '平': '', '年': '', '广': '', '庄': '', 
'库': '', '店': '', '府': '', '康': '', '廟': '', '廣': '', '弁': '', 
'弄': '', '張': '', '律': '', '徐': '', '心': '', '志': '', '慰': '', 
'成': '', '戸': '', '所': '', '扒': '', '报': '', '抹': '', '押': '', 
'摩': '', '改': '', '政': '', '救': '', '敖': '', '文': '', '斎': '', 
'料': '', '新': '', '方': '', '日': '', '旺': '', '明': '', '星': '', 
'春': '', '時': '', '晚': '', '書': '', '朝': '', '本': '', '朵': '', 
'李': '', '村': '', '杜': '', '杨': '', '東': '', '松': '', '柏': '', 
'柳': '', '柴': '', '桂': '', '桥': '', '梅': '', '棍': '', '森': '', 
'樛': '', '横': '', '橋': '', '欢': '', '欧': '', '武': '', '段': '', 
'民': '', '汁': '', '汉': '', '江': '', '汪': '', '沙': '', '沪': '', 
'河': '', '泉': '', '法': '', '波': '', '泰': '', '洛': '', '洞': '', 
'津': '', '洲': '', '派': '', '浜': '', '浪': '', '海': '', '淀': '', 
'淞': '', '深': '', '清': '', '渎': '', '湯': '', '湾': '', '溪': '', 
'漢': '', '火': '', '炸': '', '焼': '', '熙': '', '爾': '', '牙': '', 
'特': '', '猫': '', '獅': '', '玉': '', '王': '', '理': '', '瑞': '', 
'產': '', '甫': '', '田': '', '申': '', '町': '', '画': '', '界': '', 
'百': '', '盆': '', '益': '', '盐': '', '相': '', '省': '', '眼': '', 
'石': '', '碗': '', '祖': '', '祝': '', '神': '', '祭': '', '祺': '', 
'禮': '', '穗': '', '突': '', '立': '', '粗': '', '粤': '', '粵': '', 
'糕': '', '細': '', '統': '', '絵': '', '經': '', '線': '', '緯': '', 
'織': '', '纬': '', '线': '', '组': '', '细': '', '经': '', '绣': '', 
'羅': '', '美': '', '老': '', '耳': '', '聞': '', '肺': '', '胡': '', 
'脉': '', '臨': '', '興': '', '舞': '', '舟': '', '船': '', '花': '', 
'茶': '', '草': '', '药': '', '莊': '', '菓': '', '菜': '', '華': '', 
'落': '', '蒙': '', '處': '', '蜀': '', '術': '', '街': '', '西': '', 
'视': '', '言': '', '話': '', '護': '', '记': '', '诌': '', '话': '', 
'谷': '', '豹': '', '财': '', '赤': '', '越': '', '跡': '', '路': '', 
'轩': '', '轫': '', '辕': '', '近': '', '速': '', '道': '', '遺': '', 
'那': '', '郡': '', '部': '', '都': '', '鄉': '', '鄰': '', '里': '', 
'野': '', '金': '', '錦': '', '鐵': '', '锦': '', '镇': '', '长': '', 
'門': '', '関': '', '门': '', '闻': '', '阪': '', '阳': '', '际': '', 
'陵': '', '陽': '', '隍': '', '難': '', '雨': '', '青': '', '面': '', 
'革': '', '韓': '', '須': '', '頭': '', '顶': '', '食': '', '饺': '', 
'首': '', '马': '', '驻': '', '高': '', '麻': '', '黄': '', '龍': '', 
'龙': '', '개': '', '경': '', '고': '', '구': '', '국': '', '기': '', 
'김': '', '대': '', '동': '', '된': '', '떡': '', '라': '', '례': '', 
'리': '', '마': '', '명': '', '몽': '', '민': '', '반': '', '밥': '', 
'벌': '', '볶': '', '부': '', '북': '', '불': '', '산': '', '상': '', 
'서': '', '선': '', '설': '', '성': '', '시': '', '식': '', '악': '', 
'양': '', '영': '', '오': '', '요': '', '울': '', '위': '', '은': '', 
'이': '', '임': '', '장': '', '정': '', '조': '', '족': '', '주': '', 
'지': '', '찌': '', '찬': '', '촌': '', '추': '', '치': '', '탕': '', 
'토': '', '통': '', '한': '', '행': '', '헌': '', 'ﬁ': 'fi', '\ufeff': '', 
'％': '%', '（': '(', '）': ')', '～': '~', '￥': 'Y', '𐎠': '', '𐎥': '', 
'𐎭': '', '𐎱': '', '𐎶': '', '𐎼': '', '𐎿': '', }