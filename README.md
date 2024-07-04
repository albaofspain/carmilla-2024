# carmilla-2024

## 작업 배경
근래 카르밀라의 캐스팅 일정을 자주 확인하고 있는데 일정을 확인하기 까지 인터파크 티켓 > 카르밀라 검색 > 캐스팅 일정 조회 로 거쳐야 하는 depth가 많았다. 
필터도 버튼 클릭 형식 보다는 엑셀 형식의 필터로 보는 것이 편해서 카르밀라 캐스팅 일정을 보여주는 한 페이지 짜리 토이 프로젝트를 기획했다. 

인터파크를 보니 요일 필터가 제공이 되고 있어, 추가할까 고민중에 있다. 


<br>

## 작업 상세 

### 프론트엔드 결정 

얼마전에 진행한 [aws-ip-range-web](https://github.com/leeleelee3264/aws-ip-range-web)과 동일한 프레임을 사용했다. 

### 운영 환경 결정 

`Github Action`을 이용해서 주기적으로 IP 정보를 업데이트 해주고, `Github Page`를 이용해서 웹사이트를 호스팅했다. 캐스팅 정보를 가져와서 업데이트 해주는 코드는 파이썬으로 작업했다.
공연이 2024-09-08에 끝나기 때문에 공연이 끝난 이후에는 더이상 Action이 돌지 않도록 삭제용 Action을 걸어두었다. 

### 고민한 부분 
로컬 PC에서 돌렸을 때는 인터파크 API를 잘 긁어왔는데 Github Action에 올리니 제대로 돌아가지 않았다. 
Response를 확인해 봤을 떄 봇 크롤링을 막기 위해 `Cloudflare`를 사용하지는 않고 있었다. (IP가 AWS ELB로 조회되었다).
User-Agent를 추가했으나 문제가 해결이 안되어 인터파크 내부에서 WAF 등으로 특정 IP 또는 국가를 차단하고 있는 듯 해 `Proxy`를 사용했다.


[Webshare](https://www.webshare.io/) 라는 서비스의 무료 플랜을 사용했다. API 호출이 하루에 한 번이라서 인터파크에서도 막지 않을 것 같은데 만약 막힌다면 
기본으로 10개의 프록시를 주기 때문에 Proxy Rotation을 고려해야 할 것 같다. [참고](https://blog.devgenius.io/how-to-use-proxies-in-python-everything-web-scraping-002-1c28acc092cf)



 

<br>

## 산출물 

### 웹사이트
[Carmilla 2024 Schedule Table by albaofspain](https://albaofspain.github.io/carmilla-2024/)

<br>
 
### 페이지


![스크린샷 2024-07-04 오후 5 49 30](https://github.com/leeleelee3264/aws-ip-range-web/assets/79887286/74b3f195-d0bd-413d-92cd-99883c74016f)


<br>

### 동작 영상

![Jul-04-2024 17-51-05](https://github.com/leeleelee3264/aws-ip-range-web/assets/79887286/ea0a9d0e-a0a7-414c-8f75-4ceb79b63e05)
