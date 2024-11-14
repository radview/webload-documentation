# Appendix A: WebLOAD-supported SSL Protocol Versions

 

##  SSL Handshake Combinations

 WebLOAD supports a variety of SSL versions, ranging from the earlier SSL versions and up to the most current TLS versions. The following table illustrates the results of different handshake combinations, depending on the Client and Server SSL version:

 

| **Client  setting** | **Server  Setting** |                   |              |              |
| ------------------- | ------------------- | ----------------- | ------------ | ------------ |
|                     | **Undetermined**    | **3.0W/2.0Hello** | **3.0 Only** | **2.0 Only** |
| **Undetermined**    | 3.0                 | 3.0               | (a)          | 2.0          |
| **3.0W/2.0Hello**   | 3.0                 | 3.0               | (a)          | (b)          |
| **3.0 Only**        | 3.0                 | 3.0               | 3.0          | (c)          |
| **2.0 Only**        | 3.0                 | 3.0               | 3.0          | 2.0          |

Each entry specifies the negotiated protocol version. In the noted instances, negotiation is impossible for the following reasons:

 

(a)  These protocols all support SSL 3.0, but the SSL 3.0 Only setting on the server prevents the SSL 2.0 Hello message sent by the client from being recognized.

(b)  The SSL 2.0 Hello message sent by the client is recognized, but the SSL 2.0 Only setting on the server sends a 2.0 response. The client rejects this response as it is set to communicate using only SSL 3.0.

(c)  The SSL 3.0 Hello message sent by the client will not be understood by the SSL 2.0 only server.

Commercial browsers and servers generally act as if they are set for **SSL_Version_Undetermined**, unless SSL 2.0 is disabled, in which case they act as if they are set for **SSL_Version_3_0_With_2_0_Hello**.



## SSL Ciphers – Complete List

 

WebLOAD’s SSL support is based on the OpenSSL open source project (http://www.openssl.org/). [Table 9 ](#_bookmark581)contains a complete list of ciphers supported by WebLOAD using OpenSSL. Abbreviations used in this list are explained in [Table 10.](#_bookmark582)

 

For information on how WebLOAD provides full SSL/TLS 1.0/TLS 1.2 protocol support through the Cipher Command Suite, see [*SSL Cipher Command Suite* ](#_bookmark33)on page [33.](#_bookmark33)

 

The following table lists all ciphers supported by WebLOAD.

| **Name**                                 | **Mode** | **Key  Ex.** | **Auth.** | **Encryption method (key length)** | **Message digest algorithm** | **Export** |
| ---------------------------------------- | -------- | ------------ | --------- | ---------------------------------- | ---------------------------- | ---------- |
| TLS1_CK_SRP_SHA_WITH_AES_256_CBC_SHA     | TLS1.2   | SRP          | SHA       | AES(256)-CBC                       | SHA                          |            |
| TLS1_CK_SRP_SHA_RSA_WITH_AES_256_CBC_SHA | TLS1.2   | SRP          | SHA       | AES(256)-CBC                       | SHA                          |            |
| TLS1_CK_RSA_WITH_AES_128_SHA256          | TLS1.2   | RSA          | RSA       | AES(128)                           | SHA256                       |            |
| TLS1_CK_RSA_WITH_AES_256_SHA256          | TLS1.2   | RSA          | RSA       | AES(256)                           | SHA256                       |            |
| TLS1_CK_DH_DSS_WITH_AES_128_SHA256       | TLS1.2   | DH           | DDS       | AES(128)                           | SHA256                       |            |
| TLS1_CK_DH_RSA_WITH_AES_128_SHA256       | TLS1.2   | DH           | RSA       | AES(128)                           | SHA256                       |            |
| TLS1_CK_DHE_DSS_WITH_AES_128_SHA256      | TLS1.2   | DHE          | DDS       | AES(128)                           | SHA256                       |            |
| TLS1_CK_DHE_RSA_WITH_AES_128_SHA256      | TLS1.2   | DHE          | RSA       | AES(128)                           | SHA256                       |            |
| TLS1_CK_DH_DSS_WITH_AES_256_SHA256       | TLS1.2   | DH           | DDS       | AES(256)                           | SHA256                       |            |
| TLS1_CK_DH_RSA_WITH_AES_256_SHA256       | TLS1.2   | DH           | RSA       | AES(256)                           | SHA256                       |            |
| TLS1_CK_DHE_DSS_WITH_AES_256_SHA256      | TLS1.2   | DHE          | DDS       | AES(256)                           | SHA256                       |            |
| TLS1_CK_DHE_RSA_WITH_AES_256_SHA256      | TLS1.2   | DHE          | RSA       | AES(256)                           | SHA256                       |            |
| TLS1_CK_ADH_WITH_AES_128_SHA256          | TLS1.2   | ADH          | None      | AES(128)                           | SHA256                       |            |
| TLS1_CK_ADH_WITH_AES_256_SHA256          | TLS1.2   | ADH          | None      | AES(256)                           | SHA256                       |            |
| TLS1_CK_RSA_WITH_AES_128_GCM_SHA256      | TLS1.2   | RSA          | RSA       | AES(128)-GCM                       | SHA256                       |            |
| TLS1_CK_RSA_WITH_AES_256_GCM_SHA384      | TLS1.2   | RSA          | RSA       | AES(256) -GCM                      | SHA384                       |            |
| TLS1_CK_DHE_RSA_WITH_AES_128_GCM_SHA256  | TLS1.2   | DH           | RSA       | AES(128) -GCM                      | SHA256                       |            |
| TLS1_CK_DHE_RSA_WITH_AES_256_GCM_SHA384  | TLS1.2   | DH           | RSA       | AES(256) -GCM                      | SHA384                       |            |
| TLS1_CK_DH_RSA_WITH_AES_128_GCM_SHA256   | TLS1.2   | DH           | RSA       | AES(128) -GCM                      | SHA256                       |            |
| TLS1_CK_DH_RSA_WITH_AES_256_GCM_SHA384   | TLS1.2   | DH           | RSA       | AES(256-GCM                        | SHA384                       |            |
| TLS1_CK_DHE_DSS_WITH_AES_128_GCM_SHA256  | TLS1.2   | DHE          | DDS       | AES(128) -GCM                      | SHA256                       |            |
| TLS1_CK_DHE_DSS_WITH_AES_256_GCM_SHA384  | TLS1.2   | DHE          | DDS       | AES(256) -GCM                      | SHA384                       |            |
| TLS1_CK_DH_DSS_WITH_AES_128_GCM_SHA256   | TLS1.2   | DH           | DDS       | AES(128) -GCM                      | SHA256                       |            |
| TLS1_CK_DH_DSS_WITH_AES_256_GCM_SHA384   | TLS1.2   | DH           | DDS       | AES(256) -GCM                      | SHA384                       |            |
| TLS1_CK_ADH_WITH_AES_128_GCM_SHA256      | TLS1.2   | ADH          | None      | AES(128) -GCM                      | SHA256                       |            |
| TLS1_CK_ADH_WITH_AES_256_GCM_SHA384      | TLS1.2   | ADH          | None      | AES(256) -GCM                      | SHA384                       |            |
| AECDH-DES-CBC3-SHA                       | TLS1     | ECDH         | None      | 3DES(168)                          | SHA1                         |            |
| ECDHE-RSA-DES-CBC3-SHA                   | TLS1     | ECDH         | RSA       | 3DES(168)                          | SHA1                         |            |
| ECDH-RSA-DES-CBC3-SHA                    | TLS1     | ECDH         | RSA       | 3DES(168)                          | SHA1                         |            |
| ECDHE-ECDSA-DES-CBC3-SHA                 | TLS1     | ECDH         | ECDSA     | 3DES(168)                          | SHA1                         |            |
| ECDH-ECDSA-DES-CBC3-SHA                  | TLS1     | ECDH         | ECDSA     | 3DES(168)                          | SHA1                         |            |
| ADH-DES-CBC3-SHA                         | SSLv3    | DH           | None      | 3DES(168)                          | SHA1                         |            |
| EDH-RSA-DES-CBC3-SHA                     | SSLv3    | DH           | RSA       | 3DES(168)                          | SHA1                         |            |
| EDH-DSS-DES-CBC3-SHA                     | SSLv3    | DH           | DSS       | 3DES(168)                          | SHA1                         |            |
| DH-RSA-DES-CBC3-SHA                      | SSLv3    | DH/RSA       | DH        | 3DES(168)                          | SHA1                         |            |
| DH-DSS-DES-CBC3-SHA                      | SSLv3    | DH/DSS       | DH        | 3DES(168)                          | SHA1                         |            |
| DES-CBC3-SHA–SSL3                        | SSLv3    | RSA          | RSA       | 3DES(168)                          | SHA1                         |            |
| DES-CBC3-MD5                             | SSLv2    | RSA          | RSA       | 3DES(168)                          | MD5                          |            |
| DES-CBC3-SHA–SSL2                        | SSLv2    | RSA          | RSA       | 3DES(192)                          | SHA1                         |            |
| AECDH-AES128-SHA                         | TLS1     | ECDH         | None      | AES(128)                           | SHA1                         |            |
| ECDHE-RSA-AES128-SHA                     | TLS1     | ECDH         | RSA       | AES(128)                           | SHA1                         |            |
| ECDH-RSA-AES128-SHA                      | TLS1     | ECDH         | RSA       | AES(128)                           | SHA1                         |            |
| ECDHE-ECDSA-AES128-SHA                   | TLS1     | ECDH         | ECDSA     | AES(128)                           | SHA1                         |            |
| ECDH-ECDSA-AES128-SHA                    | TLS1     | ECDH         | ECDSA     | AES(128)                           | SHA1                         |            |
| ADH-AES128-SHA                           | TLS1     | DH           | None      | AES(128)                           | SHA1                         |            |
| DHE-RSA-AES128-SHA                       | TLS1     | DH           | RSA       | AES(128)                           | SHA1                         |            |
| DHE-DSS-AES128-SHA                       | TLS1     | DH           | DSS       | AES(128)                           | SHA1                         |            |
| DH-RSA-AES128-SHA                        | TLS1     | DH/RSA       | DH        | AES(128)                           | SHA1                         |            |
| DH-DSS-AES128-SHA                        | TLS1     | DH/DSS       | DH        | AES(128)                           | SHA1                         |            |
| AES128-SHA                               | TLS1     | RSA          | RSA       | AES(128)                           | SHA1                         |            |
| AECDH-AES256-SHA                         | TLS1     | ECDH         | None      | AES(256)                           | SHA1                         |            |
| ECDHE-RSA-AES256-SHA                     | TLS1     | ECDH         | RSA       | AES(256)                           | SHA1                         |            |
| ECDH-RSA-AES256-SHA                      | TLS1     | ECDH         | RSA       | AES(256)                           | SHA1                         |            |
| ECDHE-ECDSA-AES256-SHA                   | TLS1     | ECDH         | ECDSA     | AES(256)                           | SHA1                         |            |
| ECDH-ECDSA-AES256-SHA                    | TLS1     | ECDH         | ECDSA     | AES(256)                           | SHA1                         |            |
| ADH-AES256-SHA                           | TLS1     | DH           | None      | AES(256)                           | SHA1                         |            |
| DHE-RSA-AES256-SHA                       | TLS1     | DH           | RSA       | AES(256)                           | SHA1                         |            |
| DHE-DSS-AES256-SHA                       | TLS1     | DH           | DSS       | AES(256)                           | SHA1                         |            |
| DH-RSA-AES256-SHA                        | TLS1     | DH/RSA       | DH        | AES(256)                           | SHA1                         |            |
| DH-DSS-AES256-SHA                        | TLS1     | DH/DSS       | DH        | AES(256)                           | SHA1                         |            |
| AES256-SHA                               | TLS1     | RSA          | RSA       | AES(256)                           | SHA1                         |            |
| EXP-ADH-DES-CBC-SHA                      | SSLv3    | DH(512)      | None      | DES(40)                            | SHA1                         | þ          |
| EXP-EDH-RSA-DES-CBC-SHA                  | SSLv3    | DH(512)      | RSA       | DES(40)                            | SHA1                         | þ          |
| EXP-EDH-DSS-DES-CBC-SHA                  | SSLv3    | DH(512)      | DSS       | DES(40)                            | SHA1                         | þ          |
| EXP-DH-RSA-DES-CBC-SHA                   | SSLv3    | DH/RSA       | DH        | DES(40)                            | SHA1                         | þ          |
| EXP-DH-DSS-DES-CBC-SHA                   | SSLv3    | DH/DSS       | DH        | DES(40)                            | SHA1                         | þ          |
| EXP-DES-CBC-SHA                          | SSLv3    | RSA(512)     | RSA       | DES(40)                            | SHA1                         | þ          |
| EXP1024-DHE-DSS-DES-CBC-SHA              | TLS1     | DH(1024)     | DSS       | DES(56)                            | SHA1                         | þ          |
| EXP1024-DES-CBC-SHA                      | TLS1     | RSA(1024)    | RSA       | DES(56)                            | SHA1                         | þ          |
| ADH-DES-CBC-SHA                          | SSLv3    | DH           | None      | DES(56)                            | SHA1                         |            |
| EDH-RSA-DES-CBC-SHA                      | SSLv3    | DH           | RSA       | DES(56)                            | SHA1                         |            |
| EDH-DSS-DES-CBC-SHA                      | SSLv3    | DH           | DSS       | DES(56)                            | SHA1                         |            |
| DH-RSA-DES-CBC-SHA                       | SSLv3    | DH/RSA       | DH        | DES(56)                            | SHA1                         |            |
| DH-DSS-DES-CBC-SHA                       | SSLv3    | DH/DSS       | DH        | DES(56)                            | SHA1                         |            |
| DES-CBC-SHA–SSL3                         | SSLv3    | RSA          | RSA       | DES(56)                            | SHA1                         |            |
| DES-CBC-SHA–SSL2                         | SSLv2    | RSA          | RSA       | DES(64)                            | SHA1                         |            |
| DES-CBC-MD5                              | SSLv2    | RSA          | RSA       | DES(56)                            | MD5                          |            |
| IDEA-CBC-SHA                             | SSLv3    | RSA          | RSA       | IDEA(128)                          | SHA1                         |            |
| IDEA-CBC-MD5                             | SSLv2    | RSA          | RSA       | IDEA(128)                          | MD5                          |            |
| NULL-MD5–SSL3                            | SSLv3    | RSA          | RSA       | None                               | MD5                          |            |
| NULL-MD5–SSL2                            | SSLv2    | RSA          | RSA       | None                               | MD5                          |            |
| RC2-CBC-MD5                              | SSLv2    | RSA          | RSA       | RC2(128)                           | MD5                          |            |
| EXP-RC2-CBC-MD5                          | SSLv3    | RSA(512)     | RSA       | RC2(40)                            | MD5                          | þ          |
| EXP-RC2-CBC-MD5                          | SSLv2    | RSA(512)     | RSA       | RC2(40)                            | MD5                          | þ          |
| EXP1024-RC2-CBC-MD5                      | TLS1     | RSA(1024)    | RSA       | RC2(56)                            | MD5                          | þ          |
| AECDH-RC4-SHA                            | TLS1     | ECDH         | None      | RC4(128)                           | SHA1                         |            |
| ECDHE-RSA-RC4-SHA                        | TLS1     | ECDH         | RSA       | RC4(128)                           | SHA1                         |            |
| ECDH-RSA-RC4-SHA                         | TLS1     | ECDH         | RSA       | RC4(128)                           | SHA1                         |            |
| ECDHE-ECDSA-RC4-SHA                      | TLS1     | ECDH         | ECDSA     | RC4(128)                           | SHA1                         |            |
| ECDH-ECDSA-RC4-SHA                       | TLS1     | ECDH         | ECDSA     | RC4(128)                           | SHA1                         |            |
| DHE-DSS-RC4-SHA                          | TLS1     | DH           | DSS       | RC4(128)                           | SHA1                         |            |
| ADH-RC4-MD5                              | SSLv3    | DH           | None      | RC4(128)                           | MD5                          |            |
| RC4-SHA                                  | SSLv3    | RSA          | RSA       | RC4(128)                           | SHA1                         |            |
| RC4-MD5–SSL3                             | SSLv3    | RSA          | RSA       | RC4(128)                           | MD5                          |            |
| RC4-MD5–SSL2                             | SSLv2    | RSA          | RSA       | RC4(128)                           | MD5                          |            |
| RC4-MD5                                  | SSLv2    | RSA          | RSA       | RC4(128)                           | MD5                          |            |
| EXP-ADH-RC4-MD5                          | SSLv3    | DH(512)      | None      | RC4(40)                            | MD5                          | þ          |
| EXP-RC4-MD5                              | SSLv3    | RSA(512)     | RSA       | RC4(40)                            | MD5                          | þ          |
| EXP-RC4-MD5                              | SSLv2    | RSA(512)     | RSA       | RC4(40)                            | MD5                          | þ          |
| EXP1024-DHE-DSS-RC4-SHA                  | TLS1     | DH(1024)     | DSS       | RC4(56)                            | SHA1                         | þ          |
| EXP1024-RC4-SHA                          | TLS1     | RSA(1024)    | RSA       | RC4(56)                            | SHA1                         | þ          |
| EXP1024-RC4-MD5                          | TLS1     | RSA(1024)    | RSA       | RC4(56)                            | MD5                          | þ          |
| RC4-64-MD5                               | SSLv2    | RSA          | RSA       | RC4(64)                            | MD5                          |            |
| KRB5–DES–CBC–SHA                         | SSLv3    | KRB5         | KRB5      | DES(64)                            | SHA1                         |            |
| KRB5-DES-CBC3-SHA                        | SSLv3    | KRB5         | KRB5      | DES(192)                           | SHA1                         |            |
| KRB5-RC4-SHA                             | SSLv3    | KRB5         | KRB5      | RC4(128)                           | SHA1                         |            |
| KRB5-IDEA-CBC-SHA                        | SSLv3    | KRB5         | KRB5      | IDEA(128)                          | SHA1                         |            |
| KRB5-DES-CBC-MD5                         | SSLv3    | KRB5         | KRB5      | DES(64)                            | MD5                          |            |
| KRB5-DES-CBC3-MD5                        | SSLv3    | KRB5         | KRB5      | DES(192)                           | MD5                          |            |
| KRB5-RC4-MD5                             | SSLv3    | KRB5         | KRB5      | RC4(128)                           | MD5                          |            |
| KRB5-IDEA-CBC-MD5                        | SSLv3    | KRB5         | KRB5      | IDEA(128)                          | MD5                          |            |
| EXP-KRB5-DES-CBC-SHA                     | SSLv3    | KRB5         | KRB5      | DES(40)                            | SHA1                         | þ          |
| EXP-KRB5-RC2-CBC-SHA                     | SSLv3    | KRB5         | KRB5      | RC2(40)                            | SHA1                         | þ          |
| EXP-KRB5-RC4-SHA                         | SSLv3    | KRB5         | KRB5      | RC4(40)                            | SHA1                         | þ          |
| EXP-KRB5-DES-CBC-MD5                     | SSLv3    | KRB5         | KRB5      | DES(40)                            | MD5                          | þ          |
| EXP-KRB5-RC2-CBC-MD5                     | SSLv3    | KRB5         | KRB5      | RC2(40)                            | MD5                          | þ          |
| EXP-KRB5-RC4-MD5                         | SSLv3    | KRB5         | KRB5      | RC4(40)                            | MD5                          |            |

 

The following table contains cipher abbreviations.

| **Abbreviation** | **Description**                                              |
| ---------------- | ------------------------------------------------------------ |
| 3DES             | Triple Data Encryption  Standard. 3DES is a mode of the DES encryption algorithm that encrypts data  three times. |
| ADH              | Anonymous Diffie Hellman:  The base Diffie-Hellman algorithm is used, but with no authentication. |
| AES              | Advanced Encryption Standard.                                |
| CBC              | Cipher Block Chaining encryption mode.                       |
| DES              | Data Encryption Standard (DES) is a cipher (a  method for encrypting information). |
| DH               | Diffie-Hellman key  exchange is a cryptographic protocol that enables two parties that have no  prior knowledge of each other to jointly establish a shared secret key over  an insecure communications channel. This key can then be used to encrypt  subsequent communications using a symmetric key cipher. |
| DHE              | Ephemeral Diffie-Hellman  key exchange that creates ephemeral (one- time) secret keys. This is possibly  the most secure of the three Diffie- Hellman options because it results in a  temporary, authenticated key. |
| DSS              | Digital Signature Standard. DSS is a United States  Federal Government standard for digital signatures. |
| ECDH             | Elliptic Curve  Diffie-Hellman is a key agreement protocol that enables two parties to  establish a shared secret key over an insecure channel. This key can then be  used to encrypt subsequent communications using a symmetric key cipher. ECDH  is a variant of the Diffie-Hellman protocol using elliptic curve  cryptography. |
| ECDSA            | Elliptic Curve Digital Signature Algorithm.                  |
| Fortezza         | Fortezza is an information security system  developed by the United States Federal Government. Fortezza PC Card security  tokens contain an NSA- approved security microprocessor called Capstone  (MYK-80) that implements the Skipjack encryption algorithm. |
| GCM              | Galois/Counter Mode for  symmetric key cryptographic block ciphers. It combines the well-known counter  mode of encryption with the new Galois mode of authentication. |
| IDEA             | International Data Encryption Algorithm  (IDEA). IDEA is a block cipher. |
| MD5              | Message-Digest algorithm 5.                                  |
| RC2              | Block cipher with a variable size key.                       |
| RC4              | Software stream cipher (also known as ARC4  or ARCFOUR).     |
| RSA              | An algorithm for public-key encryption.                      |
| SHA1             | Secure Hash Algorithm 1.                                     |
| SRP              | Secure Remote Password, a  cryptographically strong network authentication mechanism |





 

 

 

