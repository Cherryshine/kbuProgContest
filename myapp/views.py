from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from biblebot import IntranetAPI
from requests import request
from myapp.ClassroomData import Get_Classroom_Data

# 로그인 성공여부 확인 함수


async def logincheckfunc(x, y):
    response = await IntranetAPI.Login.fetch(x, y)
    result = IntranetAPI.Login.parse(response)

    # 로그인에 성공한 경우
    if "ResourceData" in str(result):
        cookie = result.data["cookies"]
        resp = await IntranetAPI.Course_plan.fetch(cookies=cookie)
        # 수업평가가 있을때 2 리턴
        if "수업평가를" in str(resp):
            return (2)

        # 수업평가가 없을때 1 리턴
        else:
            return (1)

    # 로그인에 실패한 경우 0 리턴
    elif "ErrorData" in str(result):
        return (0)

# 로그인 페이지


def loginpage(request):
    return render(request, 'statics/login.html')

# 메인페이지


def main(request):
    ident = request.POST['id']
    passwd = request.POST['password']
    k = asyncio.run(logincheckfunc(str(ident), str(passwd)))

    # 수업평가 경고가 뜨면
    if k == 2:
        return HttpResponse('''
      <html> <head>
      <script type="text/javascript">
        alert("수업평가를 하셔야 학사인트라넷을 사용할 수 있습니다.");
      </script> </head> <body> </body>
      </html>''')

    # 로그인에 성공하면
    elif k == 1:
        # # 인트라넷에서 Get_Classroom_Data 클래스의 getclass메서드 를 거쳐 강의실정보가 담긴 url을 불러옴
        # class_data = asyncio.run(Get_Classroom_Data.getclass(ident, passwd))

        # # # Get_Classroom_Data클래스 호출해 과목정보 가져오기
        # course_data = [] #course_data 리스트속 요소의 양식은 다음과 같음 : [(과목명), (과목코드), (강의실), (강의시간)]
        # course_data = Get_Classroom_Data.UrlListAnalysis(class_data)
        # print(course_data)

        # # 건물 리스트 ============================================================>>>>
        #       Calmel = []
        #       Moria = []
        #       Bokkeum = []
        #       Illip = []
        #       Miral = []
        #       for i in range (len(class_data)):
        #         p = str(course_data[i][2])
        #         if(p.startswith("갈") or p.startswith("교양정보") or p.startswith("브니엘홀") or p.startswith("컴소")):
        #           Calmel.insert(i, course_data[i])
        #         elif(p.startswith("모")):
        #           Moria.insert(i, course_data[i])
        #         elif(p.startswith("복")):
        #           Bokkeum.insert(i, course_data[i])
        #         elif(p.startswith("일") or p.startswith("기본간호") or p.startswith("보육실습") or p.startswith("수업행동분석")):
        #           Illip.insert(i, course_data[i])
        #         elif(p.startswith("로고스홀") or p.startswith("천마홀")):
        #           Miral.insert(i, course_data[i])

        # # 갈멜관 강의실 리스트=======================================================>>>>
        #       CalmelBhall = []
        #       CalmelInfo3 = []
        #       CalmelInfo4 = []
        #       Calmel301 = []
        #       Calmel303 = []
        #       Calmel305 = []
        #       CalmelLab1 = []
        #       CalmelLab2 = []
        #       CalmelLab3 = []
        #       CalmelLab4 = []

        # # 모리아관 강의실 리스트======================================================>>>>
        #       Moria109 = []
        #       Moria212 = []
        #       Moria301 = []
        #       Moria305 = []
        #       Moria308 = []
        #       Moria310 = []

        # # 복음관 강의실 리스트
        #       Bokkeum301 = []
        #       Bokkeum303 = []
        #       Bokkeum401 = []
        #       Bokkeum403 = []
        #       Bokkeum405 = []
        #       Bokkeum407 = []
        #       Bokkeum409 = []

        # # 일립관 강의실 리스트
        #       IllipBasicSNLab1 = [] # 기본간호실습실 1, 2
        #       IllipBasicSNLab2 = []
        #       IllipEduLab = [] # 보육실습실
        #       IllipBehavAnalysisLab= [] # 수업행동분석실
        #       Illip405 = []
        #       Illip501 = []
        #       Illip503 = []
        #       Illip505 = []
        #       Illip507 = []
        #       Illip509 = []

        # # 밀알관 강의실 리스트
        #       MiralChall = [] # 천마홀
        #       MiralLogos = [] # 로고스홀
        #       # 갈멜관 강의실별 정리
        #       for i in range (len(Calmel)):
        #         if(str(Calmel[i][2]) == "브니엘홀"):
        #           CalmelBhall.insert(len(CalmelBhall),Calmel[i])
        #         elif(str(Calmel[i][2]) == "교양정보3실"):
        #           CalmelInfo3.insert(len(CalmelInfo3),Calmel[i])
        #         elif(str(Calmel[i][2]) == "교양정보4실"):
        #           CalmelInfo4.insert(len(CalmelInfo4),Calmel[i])
        #         elif(str(Calmel[i][2]) == "갈멜관 301호"):
        #           Calmel301.insert(len(Calmel301),Calmel[i])
        #         elif(str(Calmel[i][2]) == "갈멜관 303호"):
        #           Calmel303.insert(len(Calmel303),Calmel[i])
        #         elif(str(Calmel[i][2]) == "갈멜관 305호"):
        #           Calmel305.insert(len(Calmel305),Calmel[i])
        #         elif(str(Calmel[i][2]) == "컴소실습실1"):
        #           CalmelLab1.insert(len(CalmelLab1),Calmel[i])
        #         elif(str(Calmel[i][2]) == "컴소실습실2"):
        #           CalmelLab2.insert(len(CalmelLab2),Calmel[i])
        #         elif(str(Calmel[i][2]) == "컴소실습실3"):
        #           CalmelLab3.insert(len(CalmelLab3),Calmel[i])
        #         elif(str(Calmel[i][2]) == "컴소실습실4"):
        #           CalmelLab4.insert(len(CalmelLab4),Calmel[i])
        #       # 모리아관 강의실별 정리
        #       for i in range (len(Moria)):
        #         if(str(Moria[i][2]) == "모리아관 109호"):
        #           Moria109.insert(len(Moria109),Moria[i])
        #         elif(str(Moria[i][2]) == "모리아관 212호"):
        #           Moria212.insert(len(Moria212),Moria[i])
        #         elif(str(Moria[i][2]) == "모리아관 301호"):
        #           Moria301.insert(len(Moria301),Moria[i])
        #         elif(str(Moria[i][2]) == "모리아관 305호"):
        #           Moria305.insert(len(Moria305),Moria[i])
        #         elif(str(Moria[i][2]) == "모리아관 308호"):
        #           Moria308.insert(len(Moria308),Moria[i])
        #         elif(str(Moria[i][2]) == "모리아관 310호"):
        #           Moria310.insert(len(Moria310),Moria[i])
        #       # 복음관 강의실별 정리
        #       for i in range (len(Bokkeum)):
        #         if(str(Bokkeum[i][2]) == "복음관 301호"):
        #             Bokkeum301.insert(len(Bokkeum301),Bokkeum[i])
        #         elif(str(Bokkeum[i][2]) == "복음관 303호"):
        #             Bokkeum303.insert(len(Bokkeum303),Bokkeum[i])
        #         elif(str(Bokkeum[i][2]) == "복음관 401호"):
        #             Bokkeum401.insert(len(Bokkeum401),Bokkeum[i])
        #         elif(str(Bokkeum[i][2]) == "복음관 403호"):
        #             Bokkeum403.insert(len(Bokkeum403),Bokkeum[i])
        #         elif(str(Bokkeum[i][2]) == "복음관 405호"):
        #           Bokkeum405.insert(len(Bokkeum405),Bokkeum[i])
        #         elif(str(Bokkeum[i][2]) == "복음관 407호"):
        #           Bokkeum407.insert(len(Bokkeum407),Bokkeum[i])
        #         elif(str(Bokkeum[i][2]) == "복음관 409호"):
        #           Bokkeum409.insert(len(Bokkeum409),Bokkeum[i])
        #       # 일립관 강의실별 정리
        #       for i in range (len(Illip)):
        #         if(str(Illip[i][2]) == "기본간호실습실"):
        #             IllipBasicSNLab1.insert(len(IllipBasicSNLab1),Illip[i])
        #         elif(str(Illip[i][2]) == "기본간호실습실2"):
        #             IllipBasicSNLab2.insert(len(IllipBasicSNLab2),Illip[i])
        #         elif(str(Illip[i][2]) == "보육실습실"):
        #             IllipEduLab.insert(len(IllipEduLab),Illip[i])
        #         elif(str(Illip[i][2]) == "수업행동분석실&amp;모의실습실"):
        #             IllipBehavAnalysisLab.insert(len(IllipBehavAnalysisLab),Illip[i])
        #         elif(str(Illip[i][2]) == "일립관 405호"):
        #             Illip405.insert(len(Illip405),Illip[i])
        #         elif(str(Illip[i][2]) == "일립관 501호"):
        #             Illip501.insert(len(Illip501),Illip[i])
        #         elif(str(Illip[i][2]) == "일립관 503호"):
        #             Illip503.insert(len(Illip503),Illip[i])
        #         elif(str(Illip[i][2]) == "일립관 505호"):
        #             Illip505.insert(len(Illip505),Illip[i])
        #         elif(str(Illip[i][2]) == "일립관 507호"):
        #             Illip507.insert(len(Illip507),Illip[i])
        #         elif(str(Illip[i][2]) == "일립관 509호"):
        #             Illip509.insert(len(Illip509),Illip[i])

        #       # 밀알관 강의실별 정리
        #       for i in range (len(Miral)):
        #         if(str(Miral[i][2]) == "천마홀"):
        #             MiralChall.insert(len(MiralChall),Miral[i])
        #         elif(str(Miral[i][2]) == "로고스홀"):
        #             MiralLogos.insert(len(MiralLogos),Miral[i])
        #       # print(IllipBehavAnalysisLab)

        return render(request, 'statics/main.html')

    # 로그인에 실패하면
    else:
        return HttpResponse('''
      <html> <head>
      <script type="text/javascript">
        alert("아이디와 비밀번호를 확인하세요");
      </script> </head> <body> </body>
      </html>''')

# 건물별 페이지 view 함수


def Bokkeum(request):
    return render(request, 'statics/bokkeum.html')


def Calmel(request):
    return render(request, 'statics/calmel.html')


def Illip(request):
    return render(request, 'statics/illip.html')


def Miral(request):
    return render(request, 'statics/miral.html')


def Moria(request):
    return render(request, 'statics/moria.html')
