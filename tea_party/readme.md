# LWE暗号入門 @ 魔女のお茶会　2022/05/22

## 背景
近年,量子コンピュータの研究開発が盛んに行われており,大規模な量子コンピュータが実現するとショアのアルゴリズムによって素因数分解問題や楕円曲線上の離散対数問題が効率的に解けることが知られている.<br>
素因数分解問題はRSA暗号、楕円曲線上の離散対数問題は楕円曲線暗号の安全性の根拠となる問題であるため、量子コンピュータの実現による公開鍵暗号の安全性の低下が懸念されている.

### NIST PQC Competition
これを受けて米国標準技術研究所(NIST)が量子コンピュータにも耐性を有する耐量子計算機暗号(Post-Quantum Cryptography : PQC)の標準方式の公募を2016年に開始した。<br>
第1ラウンドでは鍵カプセル化方式と署名方式で合計64の応募があった.現在は,第3ラウンドまで進んでおり、鍵カプセル化方式（KEMs/Encryption)ではKyber,NTRU,SABER,Classic McElieceの4方式,署名方式(Signatures)ではDilithium, Falcon, Rainbowの3方式まで候補が絞られている.
| Methods | Kems/Encryption | Signatures |
| ------- | --------------- | ---------- |
| Lattice-based | Kyber,NTRU,SABER | Dilithium, Falcon |
| Code-based | Classic McEliece | |
| Multivariate-based | | Rainbow |

特にKyberとDilithiumの安全性の基となるLWE問題は,完全準同型暗号(Fully Homomorphic Encryption)を構成できることから高機能暗号としても注目されている.

## LWE問題
2005年にRegevさんが提唱した計算量的に求解困難な問題であり,秘密ベクトルに関するランダムな連立線形近似方程式から秘密ベクトルを復元する問題である.
この問題は格子問題の１つである最近ベクトル問題(Shortest Vector Problem)に帰着させることでその困難性が証明されている.  

$$
\begin{align}
  14s_1+15s_2+5s_3+2s_4  &\equiv 8\pmod{17}\\
  13s_1+14s_2+14s_3+6s_4 &\equiv 16\pmod{17}\\
  6s_1+10s_2+13s_3+s_4   &\equiv 12\pmod{17}\\
  10s_1+4s_2+12s_3+16s_4 &\equiv 12\pmod{17}\\
                         &\vdots            \\
  6s_1+7s_2+16s_3+2s_4   &\equiv 3\pmod{17}
\end{align}
$$

から秘密ベクトル$s=\{s_1,s_2,s_3,s_4\} \in \mathbb{F}_{17}^4$ を求める問題

### Notation
$q$ : 素数<br>
$\mathcal{D}_{\mathbb{F}_q^n}$ : 平均0,標準偏差$\alpha$の正規分布  
$s \in \mathbb{F}_q^n$ : $(n\times 1)$ の秘密ベクトル  

$A \leftarrow \mathcal{D}_{\mathbb{F}_q^n,\alpha}$ : $(m\times 1)$の誤差ベクトル  
### 判定LWE(Decision-LWE)

### 探索LWE(Search-LWE)
$(A,A\cdot s+e\pmod q)$が与えられた時,$s$を求める問題

## LWE問題を利用した公開鍵暗号

## RLWE問題
## RLWE問題を利用した公開鍵暗号
