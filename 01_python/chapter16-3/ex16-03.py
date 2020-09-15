# 가상환경

#  가상환경(Virtual Environment)
#   ○ 파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능
#   ○ 여러개의 프로젝트를 진행하는 경우
#        프로젝트마다 동일 패키지에 대해 다른 라이브러리를 사용하는 경우 문제
#   ○ 이를 방지하기 위한 격리된 독립적인 가상환경을 제공
#   ○ 일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작

# pip는 버전을 설정하지 않으면 가장 최신 버전을 설치한다.

#  가상환경을 만드는 대표적인 모듈
#   ○ venv : Python 3.3 버전 이후 부터 기본모듈에 포함됨
#   ○ virtualenv : Python 2 버전부터 사용해오던 가상환경 라이브러리, Python 3에서도 사용가능
#   ○ conda : Anaconda Python을 설치했을 시 사용할 수 있는 모듈
#   ○ pyenv : pyenv의 경우 Python Version Manger임과 동시에 가상환경 기능을 플러그인 형태로 제공

#  가상환경 목록 보기
#   ○ conda env list (명령창)

"""
# conda environments:
#
base                  *  C:\Users\i\anaconda3
chapter10                C:\Users\i\anaconda3\envs\chapter10
chapter11                C:\Users\i\anaconda3\envs\chapter11
chapter12                C:\Users\i\anaconda3\envs\chapter12
chapter13                C:\Users\i\anaconda3\envs\chapter13
chapter14                C:\Users\i\anaconda3\envs\chapter14
chapter15                C:\Users\i\anaconda3\envs\chapter15
chapter16                C:\Users\i\anaconda3\envs\chapter16
chapter16-2              C:\Users\i\anaconda3\envs\chapter16-2
chapter16-3              C:\Users\i\anaconda3\envs\chapter16-3
chapter3                 C:\Users\i\anaconda3\envs\chapter3
chapter4                 C:\Users\i\anaconda3\envs\chapter4
chapter5                 C:\Users\i\anaconda3\envs\chapter5
chapter6                 C:\Users\i\anaconda3\envs\chapter6
chapter7                 C:\Users\i\anaconda3\envs\chapter7
chapter8                 C:\Users\i\anaconda3\envs\chapter8
chapter9                 C:\Users\i\anaconda3\envs\chapter9
"""

# 명령창과는 다르게 PyCharm이 Terminal 에는 앞에 프로젝트 명이 들어가있다.

############################################################
#  가상환경 만들기 (명령창)
#   ○ conda create --name <가상환경 이름> python=<파이썬 버전>
#   ○ conda create --name python_study python=3.7

"""
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.2
  latest version: 4.8.3

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\i\anaconda3\envs\python_study

  added / updated specs:
    - python=3.7


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2020.6.24-0
  certifi            pkgs/main/win-64::certifi-2020.6.20-py37_0
  openssl            pkgs/main/win-64::openssl-1.1.1g-he774522_0
  pip                pkgs/main/win-64::pip-20.1.1-py37_1
  python             pkgs/main/win-64::python-3.7.7-h81c818b_4
  setuptools         pkgs/main/win-64::setuptools-49.2.0-py37_0
  sqlite             pkgs/main/win-64::sqlite-3.32.3-h2a8f88b_0
  vc                 pkgs/main/win-64::vc-14.1-h0510ff6_4
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.16.27012-hf0eaf9b_3
  wheel              pkgs/main/win-64::wheel-0.34.2-py37_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py37_0
  zlib               pkgs/main/win-64::zlib-1.2.11-h62dcd97_4


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate python_study
#
# To deactivate an active environment, use
#
#     $ conda deactivate
"""

# 다시 conda env list
"""
# conda environments:
#
base                  *  C:\Users\i\anaconda3
chapter10                C:\Users\i\anaconda3\envs\chapter10
chapter11                C:\Users\i\anaconda3\envs\chapter11
chapter12                C:\Users\i\anaconda3\envs\chapter12
chapter13                C:\Users\i\anaconda3\envs\chapter13
chapter14                C:\Users\i\anaconda3\envs\chapter14
chapter15                C:\Users\i\anaconda3\envs\chapter15
chapter16                C:\Users\i\anaconda3\envs\chapter16
chapter16-2              C:\Users\i\anaconda3\envs\chapter16-2
chapter16-3              C:\Users\i\anaconda3\envs\chapter16-3
chapter3                 C:\Users\i\anaconda3\envs\chapter3
chapter4                 C:\Users\i\anaconda3\envs\chapter4
chapter5                 C:\Users\i\anaconda3\envs\chapter5
chapter6                 C:\Users\i\anaconda3\envs\chapter6
chapter7                 C:\Users\i\anaconda3\envs\chapter7
chapter8                 C:\Users\i\anaconda3\envs\chapter8
chapter9                 C:\Users\i\anaconda3\envs\chapter9
python_study             C:\Users\i\anaconda3\envs\python_study
"""

############################################################
#  가상환경 만들기
#   ○ conda 가상환경 디렉토리
#       C:\Users\i\anaconda3\envs\python_study

#  가상환경 활성화
#   ○ conda activate <가상환경 이름>
#   ○ conda activate python_study
#       (python_study) C:\workspace\01_python>
#  가상환경 비활성화
#   ○ conda deactivate
#       (python_study) C:\workspace\01_python> conda deactivate
#       C:\workspace\01_python>
#  가상 환경 삭제하기
#   ○ conda remove --name <가상환경 이름> --all
#   ○ conda remove --name python_study --all

# PyCharm 아래 Python Console
# 현재 프로젝트 가상환경이 실행되어 있다.
