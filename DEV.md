python -m venv venv

pandas -> load CSV data
numpy -> numerical arrays
scikit-learn -> logistic regression implementation

pip install -r requirements.txt

pip install scikit-learn
Collecting scikit-learn
  Downloading scikit_learn-1.9.0-cp313-cp313-win_amd64.whl.metadata (11 kB)
Requirement already satisfied: numpy>=1.24.1 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from scikit-learn) (2.4.4)
Collecting scipy>=1.10.0 (from scikit-learn)
  Downloading scipy-1.18.0-cp313-cp313-win_amd64.whl.metadata (61 kB)
Collecting joblib>=1.4.0 (from scikit-learn)
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting narwhals>=2.0.1 (from scikit-learn)
  Downloading narwhals-2.24.0-py3-none-any.whl.metadata (15 kB)
Collecting threadpoolctl>=3.5.0 (from scikit-learn)
  Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Downloading scikit_learn-1.9.0-cp313-cp313-win_amd64.whl (8.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 772.9 kB/s  0:00:10
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
Downloading narwhals-2.24.0-py3-none-any.whl (461 kB)
Downloading scipy-1.18.0-cp313-cp313-win_amd64.whl (36.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 36.6/36.6 MB 1.1 MB/s  0:00:32
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl, scipy, narwhals, joblib, scikit-learn
Successfully installed joblib-1.5.3 narwhals-2.24.0 scikit-learn-1.9.0 scipy-1.18.0 threadpoolctl-3.6.0

[notice] A new release of pip is available: 26.0.1 -> 26.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip



https://aistudio.google.com/api-keys

pip install google-generativeai
Collecting google-generativeai
  Downloading google_generativeai-0.8.6-py3-none-any.whl.metadata (3.9 kB)
Collecting google-ai-generativelanguage==0.6.15 (from google-generativeai)
  Downloading google_ai_generativelanguage-0.6.15-py3-none-any.whl.metadata (5.7 kB)
Collecting google-api-core (from google-generativeai)
  Downloading google_api_core-2.34.0-py3-none-any.whl.metadata (2.9 kB)
Collecting google-api-python-client (from google-generativeai)
  Downloading google_api_python_client-2.198.0-py3-none-any.whl.metadata (7.0 kB)
Collecting google-auth>=2.15.0 (from google-generativeai)
  Downloading google_auth-2.56.3-py3-none-any.whl.metadata (6.0 kB)
Collecting protobuf (from google-generativeai)
  Downloading protobuf-7.35.1-cp310-abi3-win_amd64.whl.metadata (595 bytes)
Collecting pydantic (from google-generativeai)
  Downloading pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
Requirement already satisfied: tqdm in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-generativeai) (4.70.0)
Requirement already satisfied: typing-extensions in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-generativeai) (4.15.0)
Collecting proto-plus<2.0.0dev,>=1.22.3 (from google-ai-generativelanguage==0.6.15->google-generativeai)
  Downloading proto_plus-1.28.3-py3-none-any.whl.metadata (2.2 kB)
Collecting protobuf (from google-generativeai)
  Downloading protobuf-5.29.6-cp310-abi3-win_amd64.whl.metadata (592 bytes)
Collecting googleapis-common-protos<2.0.0,>=1.69.2 (from google-api-core->google-generativeai)
  Downloading googleapis_common_protos-1.75.1-py3-none-any.whl.metadata (8.5 kB)
INFO: pip is looking at multiple versions of google-api-core to determine which version is compatible with other requirements. This could take a while.
Collecting google-api-core (from google-generativeai)
  Downloading google_api_core-2.33.0-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: requests<3.0.0,>=2.33.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-api-core->google-generativeai) (2.33.1)
INFO: pip is looking at multiple versions of google-api-core[grpc] to determine which version is compatible with other requirements. This could take a while.
Collecting grpcio<2.0.0,>=1.41.0 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai)
  Downloading grpcio-1.83.0-cp313-cp313-win_amd64.whl.metadata (3.8 kB)
Collecting grpcio-status<2.0.0,>=1.41.0 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai)
  Downloading grpcio_status-1.83.0-py3-none-any.whl.metadata (1.2 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth>=2.15.0->google-generativeai)
  Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting cryptography>=38.0.3 (from google-auth>=2.15.0->google-generativeai)
  Downloading cryptography-50.0.0-cp311-abi3-win_amd64.whl.metadata (4.3 kB)
INFO: pip is looking at multiple versions of googleapis-common-protos to determine which version is compatible with other requirements. This could take a while.
Collecting googleapis-common-protos<2.0.0,>=1.63.2 (from google-api-core->google-generativeai)
  Downloading googleapis_common_protos-1.75.0-py3-none-any.whl.metadata (8.6 kB)
INFO: pip is looking at multiple versions of grpcio-status to determine which version is compatible with other requirements. This could take a while.
Collecting grpcio-status<2.0.0,>=1.41.0 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai)
  Downloading grpcio_status-1.82.1-py3-none-any.whl.metadata (1.2 kB)
  Downloading grpcio_status-1.81.1-py3-none-any.whl.metadata (1.2 kB)
  Downloading grpcio_status-1.81.0-py3-none-any.whl.metadata (1.2 kB)
  Downloading grpcio_status-1.80.0-py3-none-any.whl.metadata (1.3 kB)
  Downloading grpcio_status-1.78.0-py3-none-any.whl.metadata (1.3 kB)
  Downloading grpcio_status-1.76.0-py3-none-any.whl.metadata (1.1 kB)
  Downloading grpcio_status-1.75.1-py3-none-any.whl.metadata (1.1 kB)
INFO: pip is still looking at multiple versions of grpcio-status to determine which version is compatible with other requirements. This could take a while.
  Downloading grpcio_status-1.75.0-py3-none-any.whl.metadata (1.1 kB)
  Downloading grpcio_status-1.74.0-py3-none-any.whl.metadata (1.1 kB)
  Downloading grpcio_status-1.73.1-py3-none-any.whl.metadata (1.1 kB)
  Downloading grpcio_status-1.73.0-py3-none-any.whl.metadata (1.1 kB)
  Downloading grpcio_status-1.72.2-py3-none-any.whl.metadata (1.1 kB)
INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.
  Downloading grpcio_status-1.72.1-py3-none-any.whl.metadata (1.1 kB)
  Downloading grpcio_status-1.71.2-py3-none-any.whl.metadata (1.1 kB)
INFO: pip is looking at multiple versions of proto-plus to determine which version is compatible with other requirements. This could take a while.
Collecting proto-plus<2.0.0dev,>=1.22.3 (from google-ai-generativelanguage==0.6.15->google-generativeai)
  Downloading proto_plus-1.28.2-py3-none-any.whl.metadata (2.2 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from requests<3.0.0,>=2.33.0->google-api-core->google-generativeai) (3.4.6)
Requirement already satisfied: idna<4,>=2.5 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from requests<3.0.0,>=2.33.0->google-api-core->google-generativeai) (3.11)
Requirement already satisfied: urllib3<3,>=1.26 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from requests<3.0.0,>=2.33.0->google-api-core->google-generativeai) (2.6.3)
Requirement already satisfied: certifi>=2023.5.7 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from requests<3.0.0,>=2.33.0->google-api-core->google-generativeai) (2026.2.25)
Requirement already satisfied: cffi>=2.0.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from cryptography>=38.0.3->google-auth>=2.15.0->google-generativeai) (2.0.0)
Requirement already satisfied: pycparser in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth>=2.15.0->google-generativeai) (3.0)
Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth>=2.15.0->google-generativeai)
  Downloading pyasn1-0.6.4-py3-none-any.whl.metadata (8.4 kB)
Collecting httplib2<1.0.0,>=0.19.0 (from google-api-python-client->google-generativeai)
  Downloading httplib2-0.32.0-py3-none-any.whl.metadata (2.2 kB)
Collecting google-auth-httplib2<1.0.0,>=0.2.0 (from google-api-python-client->google-generativeai)
  Downloading google_auth_httplib2-0.4.1-py3-none-any.whl.metadata (3.0 kB)
Collecting uritemplate<5,>=3.0.1 (from google-api-python-client->google-generativeai)
  Downloading uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)
Collecting pyparsing<4,>=3.1 (from httplib2<1.0.0,>=0.19.0->google-api-python-client->google-generativeai)
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting annotated-types>=0.6.0 (from pydantic->google-generativeai)
  Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.46.4 (from pydantic->google-generativeai)
  Downloading pydantic_core-2.46.4-cp313-cp313-win_amd64.whl.metadata (6.7 kB)
Collecting typing-inspection>=0.4.2 (from pydantic->google-generativeai)
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Requirement already satisfied: colorama in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from tqdm->google-generativeai) (0.4.6)
Downloading google_generativeai-0.8.6-py3-none-any.whl (155 kB)
Downloading google_ai_generativelanguage-0.6.15-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 66.3 kB/s  0:00:20
Downloading google_api_core-2.33.0-py3-none-any.whl (176 kB)
Downloading google_auth-2.56.3-py3-none-any.whl (259 kB)
Downloading googleapis_common_protos-1.75.0-py3-none-any.whl (300 kB)
Downloading grpcio-1.83.0-cp313-cp313-win_amd64.whl (5.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 67.5 kB/s  0:01:04
Downloading grpcio_status-1.71.2-py3-none-any.whl (14 kB)
Downloading proto_plus-1.28.2-py3-none-any.whl (50 kB)
Downloading protobuf-5.29.6-cp310-abi3-win_amd64.whl (435 kB)
Downloading cryptography-50.0.0-cp311-abi3-win_amd64.whl (3.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 97.8 kB/s  0:00:46
Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
Downloading pyasn1-0.6.4-py3-none-any.whl (84 kB)
Downloading google_api_python_client-2.198.0-py3-none-any.whl (15.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.6/15.6 MB 86.1 kB/s  0:03:22
Downloading google_auth_httplib2-0.4.1-py3-none-any.whl (9.5 kB)
Downloading httplib2-0.32.0-py3-none-any.whl (93 kB)
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
Downloading pydantic-2.13.4-py3-none-any.whl (472 kB)
Downloading pydantic_core-2.46.4-cp313-cp313-win_amd64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 122.5 kB/s  0:00:17
Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Installing collected packages: uritemplate, typing-inspection, pyparsing, pydantic-core, pyasn1, protobuf, grpcio, annotated-types, pydantic, pyasn1-modules, proto-plus, httplib2, googleapis-common-protos, cryptography, grpcio-status, google-auth, google-auth-httplib2, google-api-core, google-api-python-client, google-ai-generativelanguage, google-generativeai
Successfully installed annotated-types-0.8.0 cryptography-50.0.0 google-ai-generativelanguage-0.6.15 google-api-core-2.33.0 google-api-python-client-2.198.0 google-auth-2.56.3 google-auth-httplib2-0.4.1 google-generativeai-0.8.6 googleapis-common-protos-1.75.0 grpcio-1.83.0 grpcio-status-1.71.2 httplib2-0.32.0 proto-plus-1.28.2 protobuf-5.29.6 pyasn1-0.6.4 pyasn1-modules-0.4.2 pydantic-2.13.4 pydantic-core-2.46.4 pyparsing-3.3.2 typing-inspection-0.4.2 uritemplate-4.2.0

pip install google-genai
Collecting google-genai
  Downloading google_genai-2.17.0-py3-none-any.whl.metadata (56 kB)
Requirement already satisfied: anyio<5.0.0,>=4.8.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-genai) (4.13.0)
Requirement already satisfied: google-auth<3.0.0,>=2.56.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-auth[requests]<3.0.0,>=2.56.0->google-genai) (2.56.3)
Requirement already satisfied: httpx<1.0.0,>=0.28.1 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-genai) (0.28.1)
Requirement already satisfied: pydantic<3.0.0,>=2.12.5 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-genai) (2.13.4)
Requirement already satisfied: requests<3.0.0,>=2.28.1 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-genai) (2.33.1)
Collecting tenacity<9.2.0,>=8.2.3 (from google-genai)
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting websockets<17.0,>=13.0.0 (from google-genai)
  Downloading websockets-16.1.1-cp313-cp313-win_amd64.whl.metadata (7.0 kB)
Requirement already satisfied: typing-extensions<5.0.0,>=4.14.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-genai) (4.15.0)
Collecting distro<2,>=1.7.0 (from google-genai)
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting sniffio (from google-genai)
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: idna>=2.8 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from anyio<5.0.0,>=4.8.0->google-genai) (3.11)
Requirement already satisfied: pyasn1-modules>=0.2.1 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai) (0.4.2)
Requirement already satisfied: cryptography>=38.0.3 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai) (50.0.0)
Requirement already satisfied: certifi in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from httpx<1.0.0,>=0.28.1->google-genai) (2026.2.25)
Requirement already satisfied: httpcore==1.* in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from httpx<1.0.0,>=0.28.1->google-genai) (1.0.9)
Requirement already satisfied: h11>=0.16 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from httpcore==1.*->httpx<1.0.0,>=0.28.1->google-genai) (0.16.0)
Requirement already satisfied: annotated-types>=0.6.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from pydantic<3.0.0,>=2.12.5->google-genai) (0.8.0)
Requirement already satisfied: pydantic-core==2.46.4 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from pydantic<3.0.0,>=2.12.5->google-genai) (2.46.4)
Requirement already satisfied: typing-inspection>=0.4.2 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from pydantic<3.0.0,>=2.12.5->google-genai) (0.4.2)
Requirement already satisfied: charset_normalizer<4,>=2 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from requests<3.0.0,>=2.28.1->google-genai) (3.4.6)
Requirement already satisfied: urllib3<3,>=1.26 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from requests<3.0.0,>=2.28.1->google-genai) (2.6.3)
Requirement already satisfied: cffi>=2.0.0 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from cryptography>=38.0.3->google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai) (2.0.0)
Requirement already satisfied: pycparser in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai) (3.0)
Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in C:\Users\intel\AppData\Local\Programs\Python\Python313\Lib\site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai) (0.6.4)
Downloading google_genai-2.17.0-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 150.1 kB/s  0:00:06
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading websockets-16.1.1-cp313-cp313-win_amd64.whl (180 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Installing collected packages: websockets, tenacity, sniffio, distro, google-genai
Successfully installed distro-1.9.0 google-genai-2.17.0 sniffio-1.3.1 tenacity-9.1.4 websockets-16.1.1